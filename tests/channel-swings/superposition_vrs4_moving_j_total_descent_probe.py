#!/usr/bin/env python3
"""Exact finite controls for the VRS-4 total-complex descent theorem."""

from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(name, value):
    CHECKS.append((name, bool(value)))


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(x) for x in zip(*a)]


J2 = [[F(0), F(-1)], [F(1), F(0)]]
J4 = [[F(0), F(-1), F(0), F(0)], [F(1), F(0), F(0), F(0)],
      [F(0), F(0), F(0), F(-1)], [F(0), F(0), F(1), F(0)]]
K = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)], [F(0), F(0)]]
L = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
Z22 = [[F(0), F(0)], [F(0), F(0)]]
minus_I4 = [[F(-1 if i == j else 0) for j in range(4)] for i in range(4)]

check("complex condition LK zero", mm(L, K) == Z22)
check("J_E square minus one", mm(J4, J4) == minus_I4)
check("K intertwiner", mm(J4, K) == mm(K, J2))
check("L intertwiner", mm(L, J4) == mm(J2, L))
check("image K invariant", mm(J4, K) == mm(K, J2))
check("kernel L invariant", mm(L, J4) == mm(J2, L))

# The quotient is represented by the last complex plane.
QJ = [[J4[i + 2][j + 2] for j in range(2)] for i in range(2)]
check("quotient J square minus one", mm(QJ, QJ) == [[F(-1), F(0)], [F(0), F(-1)]])

K_bad = [[F(1), F(0)], [F(0), F(0)], [F(0), F(1)], [F(0), F(0)]]
check("bad K control fires", mm(J4, K_bad) != mm(K_bad, J2))
L_bad = [[F(1), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
check("bad L control fires", mm(L_bad, J4) != mm(J2, L_bad))

# Boundary line span(e3) is not J invariant; full last plane is.
e3 = [[F(0)], [F(0)], [F(1)], [F(0)]]
Je3 = mm(J4, e3)
check("boundary line negative control", Je3[3][0] != 0)
check("boundary plane positive control", Je3[0][0] == 0 and Je3[1][0] == 0)

H = [[F(1 if i == j else 0) for j in range(4)] for i in range(4)]
check("pairing J compatible", mm(mm(tr(J4), H), J4) == H)
H_bad = [[F(2), F(0), F(0), F(0)], [F(0), F(1), F(0), F(0)],
         [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
check("pairing compatibility independent", mm(mm(tr(J4), H_bad), J4) != H_bad)

registry = json.loads((ROOT / "lab/process/superposition-vrs4-moving-j-total-descent-conditional-theorem.json").read_text())
check("registry conditional status", registry["status"].endswith("TYPE_MISSING_INSTANTIATION"))
check("total KL missing", "TOTAL_K_L" in registry["current_missing"])
check("boundary extension missing", "CHARGED_BOUNDARY_EXTENSION" in registry["current_missing"])
check("positive pairing missing", "DESCENDED_POSITIVE_PAIRING" in registry["current_missing"])
check("HQ survives", registry["H_Q_star"] == "NOT_KILLED")
check("H0 not proved", registry["H0"] == "STRENGTHENED_NOT_PROVED")
check("VRS5 next", registry["next_reverse_swing"] == "VRS-5-FORWARD-ENABLER")
check("claim ceiling", registry["claim_ceiling"].startswith("NO_INSTANTIATED_TOTAL_COMPLEX"))

failed = [name for name, ok in CHECKS if not ok]
for name, ok in CHECKS:
    print(("PASS" if ok else "FAIL"), name)
print(f"SUMMARY {len(CHECKS)-len(failed)}/{len(CHECKS)}")
raise SystemExit(1 if failed else 0)
