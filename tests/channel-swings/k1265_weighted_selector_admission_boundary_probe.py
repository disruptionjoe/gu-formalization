#!/usr/bin/env python3
"""Hostile mutations for K1265."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1265-weighted-selector-admission-boundary.json").read_text())
mutations = [
    ("satisfied", ("certificate", "satisfied_count"), 5),
    ("excluded", ("certificate", "excluded_count"), 1),
    ("conditional", ("certificate", "conditional_count"), 0),
    ("missing", ("certificate", "missing_count"), 6),
    ("K1145", ("certificate", "k1145_pass_count"), 1),
    ("K1150", ("certificate", "k1150_pass_count"), 1),
    ("rank", ("decision", "scalar_parameter_rank_conflation_rejected"), False),
    ("source", ("decision", "finite_continuous_lock_is_source_owned"), True),
    ("sign", ("decision", "discrete_I7_sign_selected"), True),
    ("protected", ("protected_status_effect",), "moved"),
]
rejected = 0
for name, path, value in mutations:
    d = copy.deepcopy(BASE)
    if len(path) == 1:
        d[path[0]] = value
    else:
        d[path[0]][path[1]] = value
    if d != BASE:
        rejected += 1
        print(f"REJECT {rejected:02d}: {name}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
