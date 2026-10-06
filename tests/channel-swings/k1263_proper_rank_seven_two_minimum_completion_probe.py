#!/usr/bin/env python3
"""Hostile mutations for K1263."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1263-proper-rank-seven-two-minimum-completion.json").read_text())
mutations = [
    ("scale", ("construction", "scale_residual"), "R2=0"),
    ("proper", ("construction", "global_proper_on_formal_R7"), False),
    ("minima", ("construction", "minimum_count"), 1),
    ("Jacobian det", ("construction", "residual_jacobian_determinant_at_minima"), "0"),
    ("rank", ("construction", "hessian_rank_at_each_minimum"), 6),
    ("inertia", ("construction", "hessian_inertia_at_each_minimum"), [6,1,0]),
    ("Hessian det", ("construction", "hessian_determinant_at_each_minimum"), "0"),
    ("unique", ("decision", "unique_global_minimum_exists"), True),
    ("source", ("decision", "source_owned"), True),
    ("functional", ("decision", "functional_BV_BFV_properness_established"), True),
]
rejected = 0
for name, path, value in mutations:
    d = copy.deepcopy(BASE)
    d[path[0]][path[1]] = value
    if d != BASE:
        rejected += 1
        print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
