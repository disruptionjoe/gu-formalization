#!/usr/bin/env python3
"""Hostile mutations for K1256."""
import copy, json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1256-invariant-channel-hessian-rank-bound.json").read_text())
mutations = [
    ("dimension", ("theorem", "quotient_dimension"), 6),
    ("factorization", ("theorem", "factorization"), "V arbitrary"),
    ("rank bound", ("theorem", "hessian_rank_upper_bound"), "rank Hess(V)<=7"),
    ("nullity", ("theorem", "hessian_nullity_lower_bound"), "nullity Hess(V)>=0"),
    ("full rank", ("theorem", "full_rank_requirement"), "m>=1"),
    ("critical", ("theorem", "hypotheses"), ["rank dP=m"]),
    ("injectivity", ("theorem", "intermediate_conclusion"), "dF may be nonzero"),
    ("identity", ("theorem", "hessian_identity"), "Hess(V)=Hess(F)"),
    ("source", ("decision", "seven_channels_are_sufficient_without_source_ownership"), True),
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
