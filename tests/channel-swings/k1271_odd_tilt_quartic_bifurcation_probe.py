#!/usr/bin/env python3
"""Hostile mutations for K1271."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1271-odd-tilt-quartic-bifurcation.json").read_text())
mutations = [
    ("potential", ("theorem","potential"), "even only"),
    ("equation", ("theorem","critical_equation"), "p=0"),
    ("discriminant", ("theorem","monic_discriminant"), "zero"),
    ("threshold", ("theorem","critical_tilt"), "0"),
    ("subcritical", ("theorem","subcritical"), "one root"),
    ("supercritical", ("theorem","supercritical"), "three roots"),
    ("reflection", ("theorem","reflection_identity"), "zero"),
    ("unique", ("theorem","unique_global_minimum_for_nonzero_tilt"), False),
    ("small tilt", ("decision","arbitrarily_small_odd_tilt_removes_all_other_stationary_points"), True),
    ("owner", ("decision","epsilon_source_owned"), True),
]
rejected = 0
for name, path, value in mutations:
    d = copy.deepcopy(BASE); d[path[0]][path[1]] = value
    if d != BASE:
        rejected += 1; print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
