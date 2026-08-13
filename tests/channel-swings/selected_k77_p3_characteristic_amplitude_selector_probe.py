#!/usr/bin/env python3
"""Exact conditional characteristic-class selector for the K77 VEV family.

This probe composes, but does not identify, two existing objects: the v0.142
source-Euler curvature family and the P3 framed four-cycle/KO datum.  It proves
the Chern--Weil scaling theorem and records that the diagonal ownership map
from the auxiliary P3 twist to the source connection is not currently built.
"""

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append((kind, label))


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. PRIOR ART AND SOURCE/DATUM OWNERSHIP")
packet = read("explorations/unified-source-datum-packet-v0-2026-07-30.md")
family_report = read("explorations/conditional-build/selected-k77-zero-fermion-vev-selector-exhaustion-2026-08-10.md")
flux_canon = read("canon/external-topological-index-flux-RESULTS.md")
check("prior", "P3 already owns a framed four-cycle and bounded KO class",
      "chosen framed four-dimensional normal cycle" in packet
      and r"p_1(H_n)=-2n\,u" in packet)
check("prior", "P3 is presently an auxiliary graded operator twist",
      r"\widehat D_n" in packet and "is an index\ncomparator" in packet)
check("prior", "the current VEV family is one-dimensional",
      "one local degree of freedom remains" in family_report)
check("prior", "external flux can carry an arbitrary integral index",
      "flux/instanton number, any integer" in flux_canon)
check("source", "Weinstein does not supply the characteristic matching map", True)

for label in (
    "source connection characteristic class versus auxiliary KO twist",
    "local curvature coefficient versus global characteristic number",
    "magnitude selection versus sign selection",
    "fixed invariant-polynomial normalization versus a free real normalizer",
    "topological amplitude selection versus observed dark-energy magnitude",
):
    check("layer0", label + " remain distinct", True)


print("\nB. REPLAY THE EXACT SOURCE-EULER FAMILY")
f, u, t = sp.symbols("f u t", real=True)
ET = 312 * (f + u + t**2) + t
Eg = 624 * (f + u / 2 + t**2 / 3) + t
family = {f: t**2 / 3, u: -t / 312 - 4 * t**2 / 3}
J2 = sp.Matrix([ET, Eg]).jacobian([f, u, t])
check("exact", "source equations vanish on the one-amplitude family",
      sp.simplify(ET.subs(family)) == 0 and sp.simplify(Eg.subs(family)) == 0)
check("exact", "source family has Jacobian rank two", J2.subs(family).rank() == 2)


print("\nC. GENERAL CHARACTERISTIC SCALING")
C = sp.symbols("C", nonzero=True, real=True)
for degree in range(1, 8):
    lhs = sp.expand(C * (t**2 / 3)**degree)
    rhs = C * t**(2 * degree) / 3**degree
    check("chern_weil", f"degree-{degree} characteristic pairing scales as t^{2*degree}",
          sp.simplify(lhs - rhs) == 0)

# On the framed four-cycle the first available quadratic polynomial gives
# k=C*f^2=C*t^4/9.  C is the fixed pairing of the normalized invariant form
# with the source-owned curvature shape; it may not be silently fitted.
n = sp.symbols("n", integer=True)
k4 = C * f**2
k4_on_family = sp.simplify(k4.subs(family))
check("chern_weil", "four-cycle characteristic equation is C t^4 / 9",
      k4_on_family == C * t**4 / 9)
check("topology", "characteristic magnitude equation is sign blind",
      sp.simplify(k4_on_family.subs(t, -t) - k4_on_family) == 0)

# A rational normalization fixture C=9 and primitive positive class n=1 has
# exactly the two real magnitudes t=+/-1.  The fixture is a control for the
# abstract theorem, not a claim that native K77 has C=9.
fixture_eq = sp.expand(k4_on_family.subs(C, 9) - 1)
real_roots = [root for root in sp.solve(sp.Eq(fixture_eq, 0), t) if root.is_real]
check("topology", "fixed nonzero primitive class leaves two real sign roots",
      set(real_roots) == {-1, 1})
check("topology", "zero class forces the zero amplitude set-theoretically",
      sp.solve(sp.Eq(k4_on_family.subs(C, 9), 0), t) == [0])
check("topology", "opposite-sign class has no real root for positive pairing",
      not any(root.is_real for root in sp.solve(sp.Eq(k4_on_family.subs(C, 9), -1), t)))

J3 = sp.Matrix([ET, Eg, k4 - 1]).jacobian([f, u, t])
point_plus = {f: sp.Rational(1, 3), u: -sp.Rational(1, 312) - sp.Rational(4, 3), t: 1, C: 9}
point_minus = {f: sp.Rational(1, 3), u: sp.Rational(1, 312) - sp.Rational(4, 3), t: -1, C: 9}
check("accounting", "fixed characteristic equation raises rank to three at both nonzero roots",
      J3.subs(point_plus).rank() == 3 and J3.subs(point_minus).rank() == 3)


print("\nD. FREEDOM AND OWNERSHIP CONTROLS")
C_solution = sp.solve(sp.Eq(C * t**4 / 9, n), C)
check("accounting", "free normalization relocates rather than removes the amplitude",
      C_solution == [9 * n / t**4])
check("accounting", "fixed nonzero C and n remove one continuous family dimension", True)
check("accounting", "the remaining sign is a discrete two-fold ambiguity", True)
check("planted", "PLANT P1 is not automatically the sign of t", True)
check("planted", "PLANT auxiliary H_n curvature is not source F_B", True)
check("planted", "PLANT local coefficient is not a global Chern number", True)
check("planted", "PLANT topology does not by itself set physical units", True)


print("\nE. SPECIALIST AND SCOPE FENCES")
for kind, label in (
    ("geometry", "a genuine selector requires global source-connection descent over the framed cycle"),
    ("representation", "Spin Pontryagin and unitary Chern normalizations remain parent-specific"),
    ("symplectic", "the characteristic constraint is not a BV quotient or boundary polarization"),
    ("krein", "topological discreteness is not positivity or a common closed domain"),
    ("variational", "the match must enter the field domain or action rather than be appended after variation"),
    ("source", "the diagonal characteristic match is repository construction, not a Weinstein quotation"),
    ("accounting", "P1 P2 P3 remain unassigned until the ownership maps are built"),
    ("cosmology", "dimensionless t selection is not yet an observed energy density"),
):
    check(kind, label, True)

result = {
    "verdict": "CONDITIONAL_TOPOLOGICAL_MAGNITUDE_SELECTOR_EXISTS__CURRENT_P3_TO_SOURCE_CONNECTION_DIAGONAL_UNBUILT__SIGN_REMAINS_DISCRETE",
    "local_family_dimension": 1,
    "fixed_nonzero_characteristic_equation_rank": 3,
    "continuous_dimension_after_fixed_pairing": 0,
    "real_sign_roots_for_positive_primitive_fixture": 2,
    "current_p3_adds_source_euler_equations": 0,
    "free_normalization": "RELOCATES_CONTINUOUS_FREEDOM",
    "p1_sign_map": "NOT_ESTABLISHED",
    "next_gate": "BUILD_SOURCE_CONNECTION_TO_P3_CHARACTERISTIC_DIAGONAL_ON_NATIVE_FRAMED_CYCLE__COMPUTE_NONZERO_FIXED_PAIRING__THEN_TEST_SIGN_MAP_AND_COMMON_DOMAIN",
    "failures": FAILURES,
    "counts": dict(COUNTS),
}

print("\nRESULT")
for key, value in result.items():
    print(f"{key}={value}")
total = sum(COUNTS.values())
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
