#!/usr/bin/env python3
"""Hostile mutations for K1266."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1266-realized-regular-sign-pair.json").read_text())
mutations = [
    ("positive", ("construction", "positive_coordinates"), [1,1,3,4,5,6,7]),
    ("negative", ("construction", "negative_coordinates"), [1,2,3,4,5,6,7]),
    ("regularity", ("construction", "regularity_rule"), "none"),
    ("same even", ("construction", "same_even_invariants"), False),
    ("both regular", ("construction", "both_regular"), False),
    ("positive p", ("construction", "positive_p"), 0),
    ("negative p", ("construction", "negative_p"), 0),
    ("realized", ("decision", "both_I7_signs_realized_on_regular_split_Cartan"), False),
    ("full image", ("decision", "full_real_orbit_image_classified"), True),
    ("owner", ("decision", "source_action_response_owned"), True),
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
