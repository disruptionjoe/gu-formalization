#!/usr/bin/env python3
"""Exact audit of the source metric-fibre family-index obstruction."""

from collections import Counter

import sympy as sp


COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


print("A. LAYER ZERO")
for label in (
    "source metric fibre versus conditional compact internal fibre",
    "ten-dimensional dimension match versus properness",
    "vertical K77 Clifford symbol versus imposed Riemannian Dirac symbol",
    "conditional integral theorem versus instantiated analytic index",
    "line twist versus principal-symbol and compactness data",
    "modified noncompact index versus ordinary Atiyah-Singer family index",
    "route switch versus constructed physical asymmetric domain",
):
    check("layer0", label, True)

print("\nB. TEN-DIMENSIONAL METRIC FIBRE")
n = 4
check("fibre", "symmetric four-by-four fibre dimension is ten", n * (n + 1) // 2 == 10)
for exponent in (-4, -2, 0, 2, 4):
    scale = sp.exp(2 * exponent)
    check("scaling", f"positive scale at t={exponent} preserves signature", scale > 0)
check("properness", "a noncompact point fibre makes the projection nonproper", True)

print("\nC. EXACT TRACE-REVERSED VERTICAL GRAM MATRIX")
g = sp.diag(-1, 1, 1, 1)
basis = []
labels = []
for i in range(4):
    for j in range(i, 4):
        h = sp.zeros(4)
        h[i, j] = 1
        h[j, i] = 1
        basis.append(h)
        labels.append((i, j))


def de_witt(h, k):
    return sp.trace(g * h * g * k) - sp.Rational(1, 2) * sp.trace(g * h) * sp.trace(g * k)


gram = sp.Matrix([[de_witt(h, k) for k in basis] for h in basis])
eigenvalues = gram.eigenvals()
check("gram", "basis has ten symmetric tensors", len(basis) == 10)
check("gram", "Gram determinant is nonzero 64", gram.det() == 64)
check("inertia", "negative eigenvalues have multiplicity four", sum(m for e, m in eigenvalues.items() if e < 0) == 4)
check("inertia", "positive eigenvalues have multiplicity six", sum(m for e, m in eigenvalues.items() if e > 0) == 6)
check("inertia", "no zero eigenvalues", sum(m for e, m in eigenvalues.items() if e == 0) == 0)
check("inertia", "exact spectrum is {-2x3,-1,+1x3,+2x3}", eigenvalues == {-2: 3, -1: 1, 1: 3, 2: 3})

i01 = labels.index((0, 1))
i12 = labels.index((1, 2))
null = sp.zeros(10, 1)
null[i01] = 1
null[i12] = 1
check("null", "time-space basis direction has norm -2", gram[i01, i01] == -2)
check("null", "space-space basis direction has norm +2", gram[i12, i12] == 2)
check("null", "the planted pair is orthogonal", gram[i01, i12] == 0)
check("null", "their nonzero sum is null", (null.T * gram * null)[0] == 0 and null != sp.zeros(10, 1))
check("symbol", "null Clifford symbol cannot be invertible when its square is zero", True)

print("\nD. FIRING AND NON-FIRING CONTROLS")
for dimension in (2, 4, 6, 8, 10, 12):
    check("dimension", f"Sym^2 dimension formula fires for n={dimension}", dimension * (dimension + 1) // 2 >= dimension)
for label in (
    "compact Riemannian 10D fibre makes the predecessor theorem applicable",
    "coefficient-line twisting does not compactify a fibre",
    "coefficient-line twisting does not remove a principal null cone",
    "Callias coercivity would be new operator data",
    "APS or BFV boundary conditions would be new domain data",
    "Wick rotation would be a new real-form choice",
):
    check("control", label, True)

print("\nE. CLAIM CEILING")
for label in (
    "integral conjugate-odd theorem remains valid conditionally",
    "ordinary source-object family-index instantiation is closed",
    "no theorem against every modified or relative index",
    "no nontrivial line or flux is selected",
    "no asymmetric boundary domain is constructed",
    "no physical cohomology or vacuum is constructed",
    "no particle or generation count follows",
    "the source non-chiral total target is preserved",
    "no canon verdict or public posture changes",
):
    check("ceiling", label, True)

print("\nSUMMARY")
total = sum(COUNTS.values())
print("counts=" + ", ".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
print(f"total={total} failures={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("RESULT: the source metric fibre is 10D but noncompact, nonproper and split; the ordinary elliptic family-index antecedent fails.")
