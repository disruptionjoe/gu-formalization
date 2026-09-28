#!/usr/bin/env python3
"""Replay K565 and reject lost-owner, overlap, and overclaim mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k565_orders_eleven_twelve_disjoint_hybrid_majorants.py")
STORED = ROOT / "lab/process/k565-orders-eleven-twelve-disjoint-hybrid-majorants.json"


def load():
    spec = importlib.util.spec_from_file_location("k565_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K565 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rows = [row for order in stored["order_hybrid_majorants"] for row in order["hybrid_majorant_bank"]]
    checks = [
        module.build() == stored,
        len(rows) == 50,
        stored["fixed_control"]["logical_low_coordinate_subsets_replayed"] == 167772156,
        stored["fixed_control"]["face_owner_unions_available"] == 2733,
        stored["fixed_control"]["recursive_positive_interior_max_cells"] == 25949861,
        all(row["interior_radial_power_before_exponential_integration"] >= 0 for row in rows),
        all(row["exact_complete_hybrid_abs_upper"] != "0" for row in rows),
        stored["disjoint_owner_contract"]["overlapping_K563_rows_summed_directly"] is False,
        not stored["decision"]["complete_higher_order_remainders_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_terms", 49),
        lambda p: p["fixed_control"].__setitem__("logical_low_coordinate_subsets_replayed", 167772155),
        lambda p: p["fixed_control"].__setitem__("face_owner_unions_available", 2732),
        lambda p: p["fixed_control"].__setitem__("recursive_positive_interior_max_cells", 25949860),
        lambda p: p["order_hybrid_majorants"][0]["hybrid_majorant_bank"].pop(),
        lambda p: p["order_hybrid_majorants"][0]["hybrid_majorant_bank"][0].__setitem__("interior_radial_power_before_exponential_integration", -1),
        lambda p: p["disjoint_owner_contract"].__setitem__("face_and_interior_owner_regions_pairwise_disjoint", False),
        lambda p: p["disjoint_owner_contract"].__setitem__("overlapping_K563_rows_summed_directly", True),
        lambda p: p["decision"].__setitem__("complete_higher_order_remainders_emitted", True),
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
        raise AssertionError("K565 probe failed")
    print(f"K565 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
