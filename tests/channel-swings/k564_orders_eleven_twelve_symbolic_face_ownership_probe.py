#!/usr/bin/env python3
"""Replay K564 and reject lost-state, overlap, and partition mutations."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k564_orders_eleven_twelve_symbolic_face_ownership.py")
STORED = ROOT / "lab/process/k564-orders-eleven-twelve-symbolic-face-ownership.json"


def load():
    spec = importlib.util.spec_from_file_location("k564_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K564 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    hybrids = [row for order in stored["order_ownership"] for row in order["hybrid_owner_bank"]]
    checks = [
        module.build() == stored,
        len(hybrids) == 50,
        stored["fixed_control"]["logical_low_coordinate_subsets_replayed"] == 167772156,
        stored["fixed_control"]["combined_face_owner_unions"] == 2733,
        stored["fixed_control"]["combined_interior_owned_subsets"] == 1542213,
        all(sum(owner["assigned_low_coordinate_subsets"] for owner in row["owner_rows"]) + row["interior_owned_subsets"] == row["logical_low_coordinate_subsets"] for row in hybrids),
        all(owner["assigned_low_coordinate_subsets"] > 0 for row in hybrids for owner in row["owner_rows"]),
        stored["symbolic_ownership_contract"]["logical_subsets_dropped"] == 0,
        not stored["decision"]["complete_hybrid_integrals_emitted"],
        all(stored["release_test"].values()),
    ]
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_hybrid_terms", 49),
        lambda p: p["fixed_control"].__setitem__("logical_low_coordinate_subsets_replayed", 167772155),
        lambda p: p["fixed_control"].__setitem__("combined_face_owner_unions", 2732),
        lambda p: p["fixed_control"].__setitem__("combined_interior_owned_subsets", 1542212),
        lambda p: p["order_ownership"][0]["hybrid_owner_bank"][0]["owner_rows"].pop(),
        lambda p: p["symbolic_ownership_contract"].__setitem__("first_match_owner_unions_pairwise_disjoint", False),
        lambda p: p["symbolic_ownership_contract"].__setitem__("owner_unions_plus_interior_are_exhaustive", False),
        lambda p: p["symbolic_ownership_contract"].__setitem__("logical_subsets_dropped", 1),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
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
        raise AssertionError("K564 probe failed")
    print(f"K564 probe passed {sum(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
