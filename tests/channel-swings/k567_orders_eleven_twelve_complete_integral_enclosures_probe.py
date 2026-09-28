#!/usr/bin/env python3
"""Replay K567 and reject missing terms, double normalization, and overclaims."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k567_orders_eleven_twelve_complete_integral_enclosures.py")
STORED = ROOT / "lab/process/k567-orders-eleven-twelve-complete-integral-enclosures.json"


def load():
    spec = importlib.util.spec_from_file_location("k567_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K567 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    checks = [
        module.build() == stored,
        stored["fixed_control"]["combined_ordered_descriptors"] == 94752,
        stored["fixed_control"]["combined_coherent_groups"] == 57,
        stored["fixed_control"]["combined_hybrid_remainder_terms"] == 50,
        stored["fixed_control"]["native_prefactor_application_count_by_order"] == {"11": 1, "12": 1},
        all(row["complete_integral_enclosure"]["node_interval_contained"] for row in stored["order_enclosures"]),
        stored["composition_contract"]["complete_order_eleven_and_twelve_integrals_enclosed"],
        stored["decision"]["complete_order_eleven_integral_enclosure_emitted"],
        not stored["decision"]["native_K152_interval_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_ordered_descriptors", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_coherent_groups", 56),
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_remainder_terms", 49),
        lambda p: p["fixed_control"].__setitem__("native_prefactor_application_count_by_order", {"11": 1, "12": 2}),
        lambda p: p["order_enclosures"].pop(),
        lambda p: p["composition_contract"].__setitem__("native_prefactors_applied_exactly_once", False),
        lambda p: p["composition_contract"].__setitem__("K555_product_weights_reapplied", True),
        lambda p: p["composition_contract"].__setitem__("lower_order_normalization_reused", True),
        lambda p: p["decision"].__setitem__("base_action_column_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    candidate = copy.deepcopy(stored)
    candidate["order_enclosures"][0]["complete_integral_enclosure"]["complete_integral_interval_exact"] = ["1", "-1"]
    try:
        module.validate_payload(candidate)
    except AssertionError:
        rejected += 1
    if not all(checks) or rejected != len(mutations) + 1:
        raise AssertionError("K567 probe failed")
    print(f"K567 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations) + 1} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
