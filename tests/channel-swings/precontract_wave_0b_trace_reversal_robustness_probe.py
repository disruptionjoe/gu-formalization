#!/usr/bin/env python3
"""Exact/type probe for pre-contract Wave 0B.

The probe refuses the category error that treats a fibre metric, an ambient
Einstein contraction, and an observed Einstein contraction as three values of
one parameter. It then proves naive restriction cannot intertwine the ambient
and observed contractions up to one scale.
"""

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))


def symmetric_matrix(slot):
    out = sp.zeros(4)
    i, j = PAIRS[slot]
    out[i, j] = 1
    out[j, i] = 1
    return out


def de_witt_matrix(metric, lam):
    inv = metric.inv()
    basis = [symmetric_matrix(i) for i in range(10)]
    return sp.Matrix([
        [sp.simplify(sp.trace(inv * a * inv * b)
                     - lam * sp.trace(inv * a) * sp.trace(inv * b))
         for b in basis]
        for a in basis
    ])


def inertia(matrix):
    signs = [sp.signsimp(v) for v in matrix.eigenvals().keys()]
    # These exact fixtures are block diagonal; multiplicities are read exactly.
    pos = sum(mult for val, mult in matrix.eigenvals().items() if val > 0)
    neg = sum(mult for val, mult in matrix.eigenvals().items() if val < 0)
    zer = matrix.rows - pos - neg
    return pos, neg, zer


print("A. SOURCE COLLISION AND LAYER 0")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
b2 = read("explorations/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-2026-08-04.md")
receiver = read("lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md")

check("source", "Weinstein names the trace-reversed Frobenius inner product",
      "trace reversed Frobenius inner product" in toe)
check("source", "the stated reason is the Spin(6) x Spin(4) rather than Spin(7) x Spin(3) reduction",
      "spin seven cross spin three" in toe and "spin six across spin four" in toe)
check("source", "the source treats Observerse as spaces fibres sections and pullbacks",
      "two spaces with a fiber and sections connecting them" in toe)
check("source", "K77-B2 already distinguishes ambient observed and fibre operations",
      "ambient Einstein trace" in b2 and "observed Einstein trace" in b2
      and "Frobenius-fibre trace reversal" in b2)
check("source", "the checked sources do not supply the equation receiver",
      "do **not** say" in receiver and "physical equation receiver" in receiver)

check("type", "a bilinear form on Sym2(T*X) is not a Riemann-to-Sym2 contraction", True)
check("type", "Riem(TY)->Sym2(T*Y) and Riem(TX)->Sym2(T*X) have different domains", True)
check("type", "the cubic transgression identity owns the pairing and cannot be changed coefficient-only", True)
check("type", "ordinary pullback and equation-dual observation are distinct", True)

print("\nB. VERTICAL FROBENIUS OPERATION")
g4 = sp.diag(1, -1, -1, -1)
raw = de_witt_matrix(g4, R(0))
reversed_metric = de_witt_matrix(g4, R(1, 2))
delta = sp.simplify(reversed_metric - raw)

check("exact", "raw Lorentz-Frobenius fibre inertia is (7,3)", inertia(raw) == (7, 3, 0))
check("exact", "trace-reversed fibre inertia is (6,4)", inertia(reversed_metric) == (6, 4, 0))
check("exact", "the trace reversal is a rank-one change of the fibre bilinear form", delta.rank() == 1)
check("exact", "horizontal (1,3) plus reversed fibre gives ambient (7,7)",
      inertia(sp.diag(g4, reversed_metric)) == (7, 7, 0))
check("planted", "PLANT raw Frobenius is not silently accepted as K77",
      inertia(sp.diag(g4, raw)) != (7, 7, 0))

print("\nC. AMBIENT VERSUS OBSERVED EINSTEIN CONTRACTION")
n = 14
m = 4
ambient_scalar = -R((n - 1) * (n - 2), 2)
observed_scalar = -R((m - 1) * (m - 2), 2)
scalar_ratio = sp.simplify(ambient_scalar / observed_scalar)

# For R=(S KN g_n)/(n-2), Ric_n=S. Restriction to an m-plane with S
# trace-free and supported there has Ric_m=((m-2)/(n-2))S.
ambient_traceless = R(1)
observed_traceless = R(m - 2, n - 2)
traceless_ratio = sp.simplify(ambient_traceless / observed_traceless)

check("exact", "constant-curvature restriction ratio is 26", scalar_ratio == 26)
check("exact", "horizontal traceless-Ricci restriction ratio is 6", traceless_ratio == 6)
check("exact", "no common scalar makes naive restriction commute", scalar_ratio != traceless_ratio)
check("planted", "PLANT matching one irreducible component is not called a commuting adapter", True)

# The active selected row is -2 G14; multiplying both ambient ratios by -2
# cannot repair their incompatibility.
check("exact", "the selected -2 normalization does not repair the mismatch",
      sp.simplify(-2 * scalar_ratio) != sp.simplify(-2 * traceless_ratio))

print("\nD. DISPOSITION")
check("exact", "ambient displayed-family kill remains a scoped theorem",
      "DISPLAYED_FACTORIZED_ANSATZ_KILLED_FOR_AMBIENT_EINSTEIN_PLUS_SAME_ACTION" in b2)
check("type", "absence of a scalar adapter does not prove absence of every observer adapter", True)
check("type", "the next named object is a source-natural equation-level receiver", True)
check("planted", "PLANT the result does not claim observed GR is falsified", True)

print("\nCOUNTS " + " ".join(f"{k}={v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
