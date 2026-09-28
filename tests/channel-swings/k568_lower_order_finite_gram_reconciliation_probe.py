#!/usr/bin/env python3
"""Replay K568 and reject missing groups, entries, intervals, and overclaims."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k568_lower_order_finite_gram_reconciliation.py")
STORED = ROOT / "lab/process/k568-lower-order-finite-gram-reconciliation.json"


def load():
    spec = importlib.util.spec_from_file_location("k568_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K568 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    checks = [
        module.build() == stored,
        stored["fixed_control"]["resolved_vectors"] == 142,
        stored["fixed_control"]["coherent_groups"] == 57,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 352,
        len(stored["order_reconciliation"]) == 5,
        stored["lower_order_finite_square"]["all_352_entries_reconciled"],
        stored["lower_order_finite_square"]["cross_terms_retained_inside_coherent_group_intervals"],
        stored["decision"]["orders_two_through_six_numerically_complete"],
        not stored["decision"]["K152_shifted_form_dual_residual_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("resolved_vectors", 141),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 56),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 351),
        lambda p: p["fixed_control"].__setitem__("orders", [2, 3, 4, 5]),
        lambda p: p["order_reconciliation"].pop(),
        lambda p: p["order_reconciliation"][0].__setitem__("complete_norm_square_interval_exact", ["1", "0"]),
        lambda p: p["release_test"].__setitem__("all_352_lower_order_entries_retained", False),
        lambda p: p["decision"].__setitem__("full_Q_12_emitted", True),
        lambda p: p["decision"].__setitem__("complete_M_dual_residual_emitted", True),
        lambda p: p["decision"].__setitem__("K152_shifted_form_dual_residual_emitted", True),
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
        raise AssertionError("K568 probe failed")
    print(f"K568 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
