#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K411."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k411_order_ten_hybrid_face_atlas.py")
STORED = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"


def load():
    spec = importlib.util.spec_from_file_location("k411_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K411 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K411 replay differs")
    rows = stored["hybrid_face_atlas"]
    checks = [
        len(rows) == 22,
        [row["moving_dimension"] for row in rows] == list(range(22, 0, -1)),
        rows[0]["reachable_kernel_zero_masks"] == 71,
        rows[0]["reachable_row_coalescence_masks"] == 25,
        rows[0]["reachable_column_coalescence_masks"] == 25,
        [row["all_twenty_two_axis_origin_reachable"] for row in rows] == [True] + [False] * 21,
        all(row["ordered_entries_touched"] == 13300 for row in rows),
        stored["face_ownership_rule"]["ordered_orientation_preserved"],
        stored["atlas_summary"]["reachable_face_counts_monotone_nonincreasing"],
        not stored["atlas_summary"]["complete_hybrid_integrals_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K411 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("hybrid_terms", 21),
        lambda p: p["fixed_control"].__setitem__("native_axes", p["fixed_control"]["native_axes"][:-1]),
        lambda p: p["hybrid_face_atlas"].pop(),
        lambda p: p["hybrid_face_atlas"][0].__setitem__("moving_dimension", 21),
        lambda p: p["hybrid_face_atlas"][1].__setitem__("all_twenty_two_axis_origin_reachable", True),
        lambda p: p["face_ownership_rule"].__setitem__("ordered_orientation_preserved", False),
        lambda p: p["atlas_summary"].__setitem__("reachable_face_counts_monotone_nonincreasing", False),
        lambda p: p["atlas_summary"].__setitem__("all_13300_ordered_entries_retained_on_every_axis", False),
        lambda p: p["atlas_summary"].__setitem__("complete_partial_face_preconditioners_implemented", True),
        lambda p: p["atlas_summary"].__setitem__("complete_hybrid_integrals_emitted", True),
        lambda p: p["decision"].__setitem__("all_22_hybrid_domains_compiled", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K411 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K411 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
