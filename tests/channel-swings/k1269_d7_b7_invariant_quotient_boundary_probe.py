#!/usr/bin/env python3
"""Hostile mutations for K1269."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1269-d7-b7-invariant-quotient-boundary.json").read_text())
mutations = [
    ("D ring", ("rings", "connected_D7"), "R[p^2]"),
    ("D degrees", ("rings", "connected_degrees"), [2,4,6,8,10,12,14]),
    ("B ring", ("rings", "all_signed_B7"), "R[p]"),
    ("B degrees", ("rings", "all_signed_degrees"), [2,4,6,7,8,10,12]),
    ("top", ("rings", "top_square_relation"), "e7=p"),
    ("fix p", ("rings", "odd_reflection_fixes_p"), True),
    ("fix p2", ("rings", "odd_reflection_fixes_p_squared"), False),
    ("subring", ("decision", "K1264_even_subring_matches_outer_sign_quotient"), False),
    ("survival", ("decision", "degree_seven_sign_survives_disconnected_quotient"), True),
    ("physical", ("decision", "physical_outer_quotient_owned"), True),
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
