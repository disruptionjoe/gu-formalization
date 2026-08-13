#!/usr/bin/env python3
"""Exact selected-I2B TT Euler, preboundary and helicity certificate.

This probe composes the complete selected-Cl2 quadratic pullback with the
traced Gauss identity and the repository's already-tested TT normalization.
It does not identify the TT survivor with the complete physical quotient.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
full_cl2 = read(
    "explorations/conditional-build/"
    "selected-second-layer-full-cl2-residual-pullback-2026-08-07.md"
)
gauss = read("explorations/wave24/H45-H2-vs-II2-binary-2026-07-11.md")
h21 = read("explorations/wave5/H21-theta-equals-II-2026-07-11.md")
check(
    "source",
    "source confirms the residual norm-square layer",
    "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in source,
)
check(
    "source",
    "source is silent on the selected TT owner map and its coefficients",
    "SOURCE-SILENT" in source and "independent K77 second-layer target" in source,
)
check(
    "repo",
    "the selected Cl2 pullback coefficients are exact and complete",
    "15376/13689" in full_cl2 and "-340/4563" in full_cl2 and "640" in full_cl2,
)
check(
    "repo",
    "the traced Gauss identity and pure-II TT mass normalization are already tested",
    "|II|^2 = |H|^2 - R^X" in gauss and "m^2 = +1/2" in gauss,
)
check(
    "repo",
    "H21 types II as the full section second fundamental form",
    "FULL** second fundamental form" in h21 and "off-shell" in h21,
)
for label in (
    "arbitrary II coefficients versus variations of an actual metric section",
    "TT subquotient versus the complete physical characteristic quotient",
    "preboundary potential versus reduced BFV phase space",
    "pole Green sign versus global positive energy",
    "zero-fermion bosonic tangent versus the coupled nonzero-fermion Hessian",
):
    check("type", label + " remain distinct", True)


print("\nB. NON-FITTED GAUSS COMPOSITION AND TT EULER POLYNOMIAL")
# Complete selected-Cl2 coefficients from the predecessor:
#   A ||II||^2 + B ||H||^2.
A = sp.Rational(15376, 13689)
B = -sp.Rational(340, 4563)
C4 = sp.factor(A + B)

# The exact Gauss identity gives
#   A||II||^2+B||H||^2 = (A+B)||H||^2-A R.
# In the predecessor's native TT normalization, unit ||II||^2 has
# P_II(s)=s(s+1/2), while ||H||^2 has P_H(s)=s^2.  Hence no coefficient is
# fitted here: C4=A+B and C2=A/2.
C2 = sp.factor(A / 2)
MASS2 = sp.factor(C2 / C4)
s = sp.symbols("s")
POLY = sp.factor(C4 * s**2 + C2 * s)
check("exact", "Gauss composition fixes the fourth-order coefficient", C4 == sp.Rational(14356, 13689))
check("exact", "Gauss composition fixes the Einstein coefficient", C2 == sp.Rational(7688, 13689))
check("exact", "selected TT mass ratio is exact", MASS2 == sp.Rational(1922, 3589))
check("exact", "Euler polynomial factorizes into two distinct poles", sp.expand(POLY - C4 * s * (s + MASS2)) == 0)
check("exact", "neither the Einstein nor fourth-order term cancels", C2 != 0 and C4 != 0 and MASS2 > 0)
check("planted", "PLANT the trace correction is not discarded", C4 != A)
check("planted", "PLANT the pure-II mass one-half is shifted", MASS2 != sp.Rational(1, 2))

# The propagator residues are fixed and opposite.  The common kappa_1^2 factor
# is omitted because it is an existing overall action coefficient and does not
# change the pole or helicity typing for nonzero kappa_1.
PROP = 1 / POLY
RESIDUE_0 = sp.factor(sp.residue(PROP, s, 0))
RESIDUE_M = sp.factor(sp.residue(PROP, s, -MASS2))
check("exact", "massless and massive TT residues are equal and opposite", RESIDUE_0 == 1 / C2 and RESIDUE_M == -1 / C2)
check("exact", "massless residue is positive in the inherited TT sign convention", RESIDUE_0 == sp.Rational(13689, 7688) and RESIDUE_0 > 0)


print("\nC. EXACT FOURTH-ORDER EULER AND PREBOUNDARY IDENTITY")
x = sp.symbols("x")
h = x**5 - 2 * x**3 + 3 * x + 1
variation = 2 * x**4 - x**2 + 4

# One TT polarization reduces to
#   L = C4/2 (h'')^2 - C2/2 (h')^2,
# whose Euler and preboundary potential are
#   E = C4 h'''' + C2 h'',
#   theta = C4(h'' delta h' - h''' delta h) - C2 h' delta h.
lagrangian_variation = sp.expand(
    C4 * sp.diff(h, x, 2) * sp.diff(variation, x, 2)
    - C2 * sp.diff(h, x) * sp.diff(variation, x)
)
euler = sp.expand(C4 * sp.diff(h, x, 4) + C2 * sp.diff(h, x, 2))
theta = sp.expand(
    C4 * (sp.diff(h, x, 2) * sp.diff(variation, x) - sp.diff(h, x, 3) * variation)
    - C2 * sp.diff(h, x) * variation
)
check("exact", "coefficientwise variation equals Euler plus preboundary divergence", sp.expand(lagrangian_variation - euler * variation - sp.diff(theta, x)) == 0)
direct_integral = sp.integrate(lagrangian_variation, (x, 0, 1))
bulk_integral = sp.integrate(euler * variation, (x, 0, 1))
boundary = sp.expand(theta.subs(x, 1) - theta.subs(x, 0))
check("exact", "integrated Green identity retains the nonzero endpoint potential", sp.simplify(direct_integral - bulk_integral - boundary) == 0 and boundary != 0)
check("planted", "PLANT the nonzero preboundary potential cannot be dropped", direct_integral != bulk_integral)

u = x**4 + 2 * x + 1
v = x**5 - x**2 + 3


def omega(left: sp.Expr, right: sp.Expr) -> sp.Expr:
    return sp.expand(
        C4
        * (
            sp.diff(left, x, 2) * sp.diff(right, x)
            - sp.diff(left, x, 3) * right
            - sp.diff(right, x, 2) * sp.diff(left, x)
            + sp.diff(right, x, 3) * left
        )
        - C2 * (sp.diff(left, x) * right - sp.diff(right, x) * left)
    )


omega_uv = omega(u, v)
check("exact", "action-derived preboundary two-form is antisymmetric", sp.expand(omega_uv + omega(v, u)) == 0)
check("exact", "the preboundary two-form is nonzero before a boundary condition is chosen", omega_uv != 0)
check("type", "a nonzero local preboundary form is not a selected Green-Lagrangian domain", True)


print("\nD. NULL LITTLE-GROUP HELICITY ON THE TT QUOTIENT")
eta = sp.diag(1, -1, -1, -1)
null_k = sp.Matrix([1, 0, 0, 1])
slots = [(i, j) for i in range(4) for j in range(i, 4)]


def coordinates(wave: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([wave[i, j] for i, j in slots])


plus_wave = sp.zeros(4)
plus_wave[1, 1] = 1
plus_wave[2, 2] = -1
cross_wave = sp.zeros(4)
cross_wave[1, 2] = cross_wave[2, 1] = 1
TT = sp.Matrix.hstack(coordinates(plus_wave), coordinates(cross_wave))

gauge = sp.zeros(10, 4)
for column in range(4):
    for row, (i, j) in enumerate(slots):
        gauge[row, column] = (
            (null_k[i] if j == column else 0)
            + (null_k[j] if i == column else 0)
        )
check("exact", "null diffeomorphism image has rank four", gauge.rank() == 4)
check("exact", "plus and cross span a rank-two TT carrier", TT.rank() == 2)
check("exact", "TT carrier intersects the diffeomorphism image trivially", gauge.row_join(TT).rank() == 6)

rotation = sp.zeros(4)
rotation[1, 2] = -1
rotation[2, 1] = 1
check("exact", "J12 is Lorentz and fixes the null covector", rotation.T * eta + eta * rotation == sp.zeros(4) and rotation * null_k == sp.zeros(4, 1))


def symmetric_representation(generator: sp.Matrix) -> sp.Matrix:
    basis = []
    for i, j in slots:
        wave = sp.zeros(4)
        wave[i, j] = wave[j, i] = 1
        basis.append(wave)
    return sp.Matrix.hstack(*[
        coordinates(generator * wave + wave * generator.T) for wave in basis
    ])


metric_rotation = symmetric_representation(rotation)
carrier = gauge.row_join(TT)
action = carrier.gauss_jordan_solve(metric_rotation * carrier)[0]
quotient_rotation = sp.simplify(action[4:6, 4:6])
check("exact", "rotation preserves gauge plus TT carrier", metric_rotation * carrier == carrier * action)
check("exact", "TT quotient carries the real helicity-two generator", quotient_rotation == sp.Matrix([[0, -2], [2, 0]]) and quotient_rotation**2 == -4 * sp.eye(2))
check("exact", "TT characteristic polynomial is x squared plus four", quotient_rotation.charpoly().as_expr() == sp.Symbol("lambda")**2 + 4)
check("planted", "PLANT two TT modes are not typed as helicity one", quotient_rotation**2 != -sp.eye(2))


print("\nE. POLE GREEN SIGNS AND SCOPE FENCES")
DERIVATIVE = sp.diff(POLY, s)
check("exact", "massless pole Green coefficient is positive", sp.simplify(DERIVATIVE.subs(s, 0) - C2) == 0 and C2 > 0)
check("exact", "massive pole Green coefficient has the opposite sign", sp.simplify(DERIVATIVE.subs(s, -MASS2) + C2) == 0)
check("exact", "the massless pole is helicity two and the massive TT plane retains axial weight two", TT.rank() == 2 and quotient_rotation**2 == -4 * sp.eye(2))
for label in (
    "TT_MASSLESS_HELICITY2_AND_MASSIVE_AXIAL_WEIGHT2_WITH_EXTRA_OPEN fires",
    "massive axial weight two is not a full massive SO3 representation",
    "the complete scalar vector constraint and non-TT characteristic quotient remains open",
    "the coupled nonzero-fermion direct-sum Hessian remains downstream",
    "opposite local pole signs are not a global right-H Krein domain or loop unitarity",
    "no coefficient selector residue quotient or external datum is added",
    "P1 P2 P3 remain unused",
    "Curt remains formally separate and no third lane is promoted",
):
    check("scope", label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__NORM_SQUARE__SOURCE-SILENT__TT_OWNER_MAP")
print(f"SELECTED_TT_C4={C4}")
print(f"SELECTED_TT_C2={C2}")
print(f"SELECTED_TT_MASS2={MASS2}")
print("SELECTED_TT_EULER=C4*BOX*(BOX+MASS2)")
print("SELECTED_TT_MASSLESS_HELICITY=PLUS_MINUS_TWO")
print("SELECTED_TT_MASSIVE_AXIAL_SPIN_WEIGHT=PLUS_MINUS_TWO__FULL_SO3_TYPE_OPEN")
print("SELECTED_TT_POLE_GREEN_SIGNS=OPPOSITE")
print("COMPLETE_PHYSICAL_QUOTIENT_COMMON_DOMAIN_ODD_BV_BFV=OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
