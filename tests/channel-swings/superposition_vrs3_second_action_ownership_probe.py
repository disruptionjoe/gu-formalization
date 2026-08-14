#!/usr/bin/env python3
"""Exact finite controls for VRS-3 second-action ownership."""

from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(name, value):
    CHECKS.append((name, bool(value)))


def tr(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


I2 = [[F(1), F(0)], [F(0), F(1)]]
A = [[F(1), F(2)], [F(0), F(1)]]
Q = [[F(2), F(0)], [F(0), F(-1)]]
H = mm(mm(tr(A), Q), A)
check("pullback symmetric", H == tr(H))
check("pullback exact", H == [[F(2), F(4)], [F(4), F(7)]])
check("receiver indefinite", Q[0][0] > 0 and Q[1][1] < 0)
check("pullback not complex endomorphism", mm(H, H) != [[F(-1), F(0)], [F(0), F(-1)]])

# A residual-dependent second derivative fires away from Upsilon=0.
residual_term = [[F(3), F(1)], [F(1), F(0)]]
check("residual term symmetric", residual_term == tr(residual_term))
check("residual term fires off shell", add(H, residual_term) != H)

boundary = [[F(1), F(-1)], [F(-1), F(1)]]
check("boundary Hessian symmetric", boundary == tr(boundary))
check("boundary changes total Hessian", add(H, boundary) != H)

J = [[F(0), F(-1)], [F(1), F(0)]]
minus_I = [[F(-1), F(0)], [F(0), F(-1)]]
check("separate J squares minus one", mm(J, J) == minus_I)
check("identity Hessian J invariant", mm(mm(tr(J), I2), J) == I2)
check("selected H not automatically J invariant", mm(mm(tr(J), H), J) != H)
omega = mm(tr(J), I2)
check("omega alternating after J supplied", tr(omega) == [[-x for x in row] for row in omega])
check("H alone symmetric not alternating", H != [[-x for x in row] for row in tr(H)])

registry = json.loads((ROOT / "lab/process/superposition-vrs3-second-action-ownership-discriminator.json").read_text())
check("registry status", registry["status"] == "EXECUTED_EXACT_TYPE_THEOREM")
check("complex not produced", "COMPLEX_STRUCTURE" in registry["not_produced"])
check("symplectic not produced", "SYMPLECTIC_FORM" in registry["not_produced"])
check("positivity not produced", "POSITIVE_PHYSICAL_INNER_PRODUCT" in registry["not_produced"])
check("boundary required", registry["boundary_status"].endswith("TYPE_MISSING"))
check("next VRS4", registry["next_reverse_swing"] == "VRS-4")
check("claim ceiling", registry["claim_ceiling"].startswith("NO_BACKGROUND"))

failed = [name for name, ok in CHECKS if not ok]
for name, ok in CHECKS:
    print(("PASS" if ok else "FAIL"), name)
print(f"SUMMARY {len(CHECKS)-len(failed)}/{len(CHECKS)}")
raise SystemExit(1 if failed else 0)
