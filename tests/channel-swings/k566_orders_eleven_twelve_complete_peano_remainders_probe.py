#!/usr/bin/env python3
"""Replay K566 and reject missing-term, mixed-derivative, and prefactor mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k566_orders_eleven_twelve_complete_peano_remainders.py")
STORED = ROOT / "lab/process/k566-orders-eleven-twelve-complete-peano-remainders.json"


def load():
    spec = importlib.util.spec_from_file_location("k566_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K566 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    checks = [
        module.build() == stored,
        stored["fixed_control"]["combined_hybrid_terms"] == 50,
        stored["fixed_control"]["hybrid_terms_by_order"] == {"11": 24, "12": 26},
        [len(row["hybrid_remainder_bank"]) for row in stored["order_remainders"]] == [24, 26],
        all(row["native_prefactor_still_unapplied"] for row in stored["order_remainders"]),
        stored["remainder_contract"]["mixed_derivatives_required"] is False,
        stored["remainder_contract"]["separate_24_and_26_term_tensor_identities_preserved"],
        stored["decision"]["all_fifty_K558_hybrids_summed"],
        not stored["decision"]["complete_higher_order_integrals_enclosed"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_terms", 49),
        lambda p: p["fixed_control"].__setitem__("hybrid_terms_by_order", {"11": 24, "12": 25}),
        lambda p: p["fixed_control"].__setitem__("native_prefactors_applied", True),
        lambda p: p["order_remainders"][0]["hybrid_remainder_bank"].pop(),
        lambda p: p["order_remainders"][1].__setitem__("native_prefactor_still_unapplied", False),
        lambda p: p["remainder_contract"].__setitem__("mixed_derivatives_required", True),
        lambda p: p["remainder_contract"].__setitem__("separate_24_and_26_term_tensor_identities_preserved", False),
        lambda p: p["decision"].__setitem__("complete_higher_order_integrals_enclosed", True),
        lambda p: p["release_test"].__setitem__("native_prefactors_not_double_applied", False),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if not all(checks) or rejected != len(mutations):
        raise AssertionError("K566 probe failed")
    print(f"K566 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
