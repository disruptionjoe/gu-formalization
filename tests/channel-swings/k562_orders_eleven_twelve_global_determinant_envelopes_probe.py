#!/usr/bin/env python3
"""Replay K562 and reject coefficient, primitive-order, and overclaim mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k562_orders_eleven_twelve_global_determinant_envelopes.py")
STORED = ROOT / "lab/process/k562-orders-eleven-twelve-global-determinant-envelopes.json"


def load():
    spec = importlib.util.spec_from_file_location("k562_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K562 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    checks = [
        module.build() == stored,
        stored["fixed_control"]["singular_templates"] == 97,
        stored["fixed_control"]["confluent_templates"] == 131,
        stored["envelope_summary"]["maximum_primitive_order_used"] == 12,
        stored["fixed_control"]["rank_compatible_template_envelopes"] == 3540,
        all([env["derivative_order"] for env in row["derivative_envelopes"]] == [0, 1, 2] for row in stored["determinant_envelope_bank"]),
        stored["global_determinant_contract"]["vandermonde_factors_retained"],
        stored["global_determinant_contract"]["raw_Bessel_evaluation_at_zero_used"] is False,
        not stored["decision"]["complete_hybrid_integrals_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("singular_templates", 96),
        lambda p: p["fixed_control"].__setitem__("confluent_templates", 130),
        lambda p: p["determinant_envelope_bank"].pop(),
        lambda p: p["determinant_envelope_bank"][0].__setitem__("maximum_primitive_order_used", 13),
        lambda p: p["global_determinant_contract"].__setitem__("vandermonde_factors_retained", False),
        lambda p: p["global_determinant_contract"].__setitem__("confluent_factorials_applied_before_absolute_enclosure", False),
        lambda p: p["global_determinant_contract"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False),
        lambda p: p["release_test"].__setitem__("maximum_primitive_order_is_twelve", False),
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
        raise AssertionError("K562 probe failed")
    print(f"K562 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
