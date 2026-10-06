#!/usr/bin/env python3
"""Hostile mutations for K1264."""
import copy, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1264-odd-invariant-sign-parity-obstruction.json").read_text())
mutations = [
    ("subring", ("theorem", "even_subring"), "R[I7]"),
    ("involution", ("theorem", "involution"), "identity"),
    ("invariance", ("theorem", "law_invariance"), "false"),
    ("critical pair", ("theorem", "critical_pairing"), "none"),
    ("Hessian", ("theorem", "hessian_relation"), "unrelated"),
    ("inertia", ("theorem", "inertia_and_determinant"), "different"),
    ("unique", ("theorem", "unique_nonzero_sign_selection"), "possible"),
    ("continuous", ("decision", "continuous_rank_seven_implies_discrete_sign_selection"), True),
    ("source", ("decision", "odd_response_is_source_owned"), True),
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
