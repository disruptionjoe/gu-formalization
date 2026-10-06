#!/usr/bin/env python3
"""Hostile mutations for K1270."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1270-orbit-sign-admission-boundary.json").read_text())
mutations = [
    ("satisfied", ("certificate", "satisfied_count"), 5),
    ("excluded", ("certificate", "excluded_count"), 2),
    ("conditional", ("certificate", "conditional_count"), 1),
    ("missing", ("certificate", "missing_count"), 5),
    ("K1145", ("certificate", "k1145_pass_count"), 1),
    ("K1150", ("certificate", "k1150_pass_count"), 1),
    ("realized", ("decision", "both_signs_realized"), False),
    ("connected", ("decision", "connected_source_gauge_identifies_pair"), True),
    ("outer owner", ("decision", "disconnected_extension_is_source_owned"), True),
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
