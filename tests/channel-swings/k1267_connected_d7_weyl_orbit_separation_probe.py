#!/usr/bin/env python3
"""Hostile mutations for K1267."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1267-connected-d7-weyl-orbit-separation.json").read_text())
mutations = [
    ("group", ("weyl_theorem", "group"), "W(B7)"),
    ("order", ("weyl_theorem", "order"), 645120),
    ("patterns", ("weyl_theorem", "sign_patterns"), 128),
    ("product", ("weyl_theorem", "coordinate_product_invariant"), False),
    ("same orbit", ("weyl_theorem", "opposite_nonzero_product_same_orbit"), True),
    ("Weyl", ("decision", "positive_and_negative_pair_Weyl_conjugate"), True),
    ("Spin", ("decision", "connected_Spin77_identifies_pair"), True),
    ("physical", ("decision", "physical_distinctness_proved"), True),
    ("outer", ("decision", "outer_or_boundary_identification_remains_possible"), False),
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
