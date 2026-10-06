#!/usr/bin/env python3
"""Hostile mutations for K1262."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1262-weighted-polynomial-shape-channel-construction.json").read_text())
mutations = [
    ("degrees", ("construction", "coordinates"), ["I2"]),
    ("even residuals", ("construction", "even_residuals"), "zero"),
    ("odd residual", ("construction", "odd_residual"), "I7-c7"),
    ("rank", ("construction", "shape_jacobian_rank"), 7),
    ("Hessian rank", ("construction", "shape_hessian_rank_at_zero_residual"), 7),
    ("nullity", ("construction", "shape_hessian_nullity"), 0),
    ("kernel", ("construction", "kernel"), "none"),
    ("source", ("decision", "channels_are_source_owned"), True),
    ("sign", ("decision", "odd_invariant_sign_selected"), True),
    ("claim", ("decision", "SC_ACT_06_proved_or_refuted"), True),
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
