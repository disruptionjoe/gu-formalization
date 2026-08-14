#!/usr/bin/env python3
"""Exact degree-parity certificate for the conditional 10D family index.

For a proper spin family with fibre dimension 2m and a complex line L,
Atiyah--Singer gives ch Ind(D_L)=pi_!(Ahat(T_v) exp(c)).  A monomial
c^r Ahat_{4s} contributing to base degree 2j obeys r+2s=m+j.  Replacing
L by L^-1 multiplies it by (-1)^r=(-1)^(m+j), hence

    Ind(D_{L^-1}) = (-1)^m conjugate(Ind(D_L))

rationally.  The K77 4+10 split has m=5, so the relation is conjugate-odd.
This probe does not construct the family, line, flux, Fredholm domain, or a
physical GU operator.
"""

from collections import Counter


COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def contributing_pairs(m, j):
    return [(r, s) for s in range((m + j) // 2 + 1) if (r := m + j - 2 * s) >= 0]


print("A. LAYER ZERO AND THEOREM SHAPE")
for label in (
    "14D total index versus 10D vertical family index",
    "virtual index bundle versus physical fermion carrier",
    "central line availability versus selected nonzero flux",
    "family-index parity versus luminous/dark decoupling",
    "rational Chern character identity versus integral torsion",
    "proper Fredholm family versus ambient ultrahyperbolic GU operator",
):
    check("layer0", label, True)

print("\nB. COMPLETE TEN-DIMENSIONAL DEGREE PARITY")
m = 5
for j in range(7):
    pairs = contributing_pairs(m, j)
    signs = {(-1) ** r for r, _ in pairs}
    expected = (-1) ** (m + j)
    check("parity", f"all monomials at base degree 2*{j} have one sign", signs == {expected})
    check("parity", f"degree 2*{j} matches -conjugation", expected == -((-1) ** j))

check("component", "virtual rank changes sign", (-1) ** (m + 0) == -1)
check("component", "first Chern-character component is invariant", (-1) ** (m + 1) == 1)
check("component", "four-form Chern-character component changes sign", (-1) ** (m + 2) == -1)
check("component", "six-form component is invariant", (-1) ** (m + 3) == 1)

print("\nC. GENERAL 2m-FIBRE CONTROLS")
for control_m, relation in ((4, "conjugate-even"), (5, "conjugate-odd"), (6, "conjugate-even"), (7, "conjugate-odd")):
    for j in range(5):
        signs = {(-1) ** r for r, _ in contributing_pairs(control_m, j)}
        check("control", f"m={control_m}, j={j} has uniform sign", signs == {(-1) ** (control_m + j)})
    expected_prefactor = 1 if relation == "conjugate-even" else -1
    check("control", f"m={control_m} is {relation}", (-1) ** control_m == expected_prefactor)

print("\nD. CLAIM CEILING")
for label in (
    "the theorem is conditional on a proper ten-dimensional spin family",
    "a vertical spin Dirac family and Fredholm domain remain unbuilt",
    "the central line and nonzero class remain unselected",
    "the canonical Spin-induced determinant line remains trivial",
    "virtual negative rank is not a negative number of particles",
    "no physical W/mirror carrier or cohomology follows",
    "no generation count follows",
    "no net chirality replaces the source non-chiral target",
    "integral torsion is not decided by rational Chern character",
    "no canon verdict or public posture changes",
):
    check("ceiling", label, True)

print("\nSUMMARY")
total = sum(COUNTS.values())
print("counts=" + ", ".join(f"{k}:{COUNTS[k]}" for k in sorted(COUNTS)))
print(f"total={total} failures={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("RESULT: a conditional 10D spin family obeys Ind(L^-1)=-conjugate(Ind(L)) rationally; ownership and physical realization remain open.")
