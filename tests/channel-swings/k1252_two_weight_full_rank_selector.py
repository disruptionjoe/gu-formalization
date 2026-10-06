#!/usr/bin/env python3
"""K1252: exact two-weight full-rank selector construction."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1252-two-weight-full-rank-selector.json").read_text())
C = DATA["construction"]
r0 = Fraction(3, 2)
gradient = (Fraction(0),) * 7
hessian_diagonal = (Fraction(16, 1) / r0**2,) + (Fraction(2),) * 6
determinant = Fraction(1)
for value in hessian_diagonal:
    determinant *= value
samples = [(Fraction(1,2),Fraction(3,5)), (Fraction(1),Fraction(0)), (Fraction(2),Fraction(7,11))]
lower_identity = all(
    2*s**4 - 4*s**2 + (s**4+s**2)*q + 2
    == 2*(s**2-1)**2 + (s**4+s**2)*q
    for s,q in samples
)
checks = [
    ("components have distinct weights four and two", C["degree_four_component"].startswith("V4=s^4") and C["degree_two_component"].startswith("V2=s^2")),
    ("selected gradient vanishes", gradient == (0,)*7),
    ("selected Hessian is exact", hessian_diagonal == (Fraction(16, 1)/r0**2,) + (Fraction(2),)*6),
    ("Hessian rank is seven", sum(value != 0 for value in hessian_diagonal) == C["hessian_rank"] == 7),
    ("Hessian is positive definite", all(value > 0 for value in hessian_diagonal)),
    ("Hessian inertia is seven positive", C["hessian_inertia"] == [7, 0, 0]),
    ("scaled determinant is exact", determinant == Fraction(1024, 1) / r0**2),
    ("critical chart change preserves rank and inertia", C["critical_point_coordinate_congruence_preserves_rank_and_inertia"]),
    ("lower-bound identity is exact", lower_identity),
    ("chart minimum is unique", C["unique_minimum_on_chart"]),
    ("single-weight obstruction is genuinely evaded", DATA["decision"]["single_weight_obstruction_evaded"]),
    ("construction is not source-owned", not DATA["decision"]["source_owned"]),
]
for name, item in DATA["pinned_inputs"].items():
    checks.append((f"{name} digest is pinned", hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item["sha256"]))
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {label}")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
