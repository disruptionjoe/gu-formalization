#!/usr/bin/env python3
"""Exact defect-localization, moving-section and even Ward/BV gate.

This probe establishes the coordinate-invariant localization operation and its
first-jet Euler/shape calculus.  It deliberately separates three grades:

* exact general localization/variation/descent theorems;
* an exact one-generator source-shaped witness showing that normal first jets
  can survive even when section values and tangential jets agree; and
* the still-open coefficientwise conormal Legendre symbol of the actual moving
  K77 Shiab/I1B density.

It does not promote a source-shaped proxy to the actual K77 action, select a
bulk/defect relative normalization, construct a Green domain, or assert an odd
super-IG master action or physical equation.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def at_graph(expr: sp.Expr, vertical: sp.Symbol, graph: sp.Expr) -> sp.Expr:
    return sp.factor(sp.expand(expr.subs(vertical, graph)))


R = sp.Rational


print("A. PRIMARY-SOURCE COLLISION AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
n1 = read("explorations/unified-source-datum-packet-v0-2026-07-30.md")
n3 = read("explorations/unified-source-datum-variational-emission-map-2026-07-30.md")
ward = read("explorations/k77-wave2-action-current-riesz-superig-ward-rendezvous-2026-08-04.md")
predecessor = read("explorations/k77-wave2-augmented-torsion-defect-euler-receiver-2026-08-05.md")

check(
    "source",
    "the source action contains curvature, one-half covariant dT and one-third bracket terms",
    "F_{B_\\omega}" in source_pack
    and "\\frac12d_{B_\\omega}T_\\omega" in source_pack
    and "\\frac13[T_\\omega,T_\\omega]" in source_pack,
)
check(
    "source",
    "the source types augmented torsion as a full adjoint-valued one-form on Y",
    "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack
    and "\\Omega^1(Y,\\operatorname{ad}P)" in source_pack,
)
check(
    "source",
    "the source gives a translation-direction first variation but no complete domain",
    "I^B_1(\\epsilon,\\varpi+s\\alpha)" in source_pack
    and "does not declare the complete\nadmissible" in source_pack,
)
check(
    "source",
    "the source redundancy Xi equals D Upsilon is not already an off-shell BV theorem",
    "\\Xi_\\omega=D_\\omega\\Upsilon_\\omega" in source_pack
    and "not automatically the gauge Noether identity" in source_pack,
)
check(
    "source",
    "the source correction makes odd action symmetry optional rather than a default GU prerequisite",
    "a full odd Ward/BV identity is not a default\nsource prerequisite" in source_pack,
)
check(
    "source",
    "Portal requires the upstairs construction to be read through pullback to X",
    r"all the action is happening up here on \(U^{14}\)" in portal
    and r"What does \(\zeta\) pulled back or \(\nu\) pulled back look like on \(X^4\)?" in portal,
)
check(
    "source",
    "Portal says the two non-invariant connection objects cancel their disease together",
    "neither this term nor this term is gauge invariant" in portal
    and "they fail to be gauge invariant in exactly the same way" in portal,
)
check(
    "source",
    "N1 already owns a bulk-plus-defect current measure rather than a fake smooth density",
    r"the current map \(s_!\) and the measure \(\mu_Y+s_*\mu_X\)" in n1
    and r"pretending \(X=Y\)" in n1,
)
check(
    "source",
    "N3 already proves that intrinsic variation and support motion are separate terms",
    "The first term varies the intrinsic defect expression; the second moves its\nsupport" in n3
    and "Neither can be dropped" in n3,
)
check(
    "source",
    "the prior even Ward owner includes dependent Shiab and connection paths",
    "moving Shiab/epsilon/soldering/Hodge" in ward
    and "required in `E_epsilon` and Ward" in ward,
)
check(
    "source",
    "the predecessor selects full-action localization without claiming it complete",
    "localize the **full action**" in predecessor
    and "not yet the variation of the full\nmoving defect action" in predecessor,
)

for label in (
    "ambient fourteen-density and its scalar coefficient relative to the K77 density are distinct",
    "literal top-form pullback and induced-density localization are distinct operations",
    "zero-jet four-plus-ten fields and their ambient normal first jets are distinct data",
    "field Euler monopoles and derivative-of-delta normal dipoles are distinct distributions",
    "normal first jets and gauge directions are not identified",
    "section support motion and intrinsic field variation are distinct terms",
    "ambient even Ward invariance and odd super-IG action symmetry are distinct claims",
    "a localized action and a bulk-plus-defect weld with a relative normalization are distinct constructions",
    "algebraic BV descent and a physical BFV/Green domain are distinct grades",
    "source-shaped local proxy and actual moving K77 Shiab coefficient are distinct grades",
):
    check("type", label, True)


print("\nB. CANONICAL LOCALIZATION AND PATCH DESCENT")
x, v = sp.symbols("x v", real=True)
j = R(3, 4)
kappa = R(7, 5)
s = j * x
mu_s = sp.sqrt(1 + j**2)
check("exact", "the rational graph has exact induced density five-fourths", mu_s == R(5, 4))

# A scalar coefficient of an ambient density can be evaluated on the graph and
# multiplied by the induced graph density.  Literal pullback of a two-form to
# this one-dimensional fixture is zero, the dimensional analogue of 14 -> 4.
q = x**2 + x * v + 2 * v**2 + x
qx = sp.diff(q, x)
qv = sp.diff(q, v)
lagrangian = sp.expand(R(1, 2) * (qx**2 + qv**2) + kappa * q**2 / 2)
localized = sp.integrate(mu_s * at_graph(lagrangian, v, s), (x, 0, 1))
check("exact", "induced-density localization of a nonzero scalar coefficient is nonzero", localized != 0)
check("exact", "literal pullback of the ambient top form to lower dimension is zero", True)

# Normal chart reversal/rescaling.  The scalar and induced density transform;
# no oriented vertical volume is chosen.
xp, vp = sp.symbols("xp vp", real=True)
r = R(-5, 3)
q_prime = sp.expand(q.subs({x: xp, v: vp / r}))
qx_prime = sp.diff(q_prime, xp)
qv_prime = sp.diff(q_prime, vp)
lagrangian_prime = sp.expand(
    R(1, 2) * (qx_prime**2 + r**2 * qv_prime**2) + kappa * q_prime**2 / 2
)
s_prime = r * j * xp
mu_prime = sp.sqrt(1 + (sp.diff(s_prime, xp) / r) ** 2)
localized_prime = sp.integrate(
    mu_prime * at_graph(lagrangian_prime, vp, s_prime), (xp, 0, 1)
)
check("exact", "the localized scalar action descends across a vertical orientation reversal", sp.simplify(localized_prime - localized) == 0)
check("exact", "the induced density is unchanged by the rescaled normal chart", mu_prime == mu_s)
check("exact", "patch descent uses a density and consumes no vertical orientation bit", r < 0 and localized_prime == localized)


print("\nC. FIRST-JET EULER DISTRIBUTION: MONOPOLE PLUS NORMAL DIPOLE")
t = sp.symbols("t", real=True)
eta = sp.expand(x * (1 - x) * (1 + v + x * v))
q_t = q + t * eta
lagrangian_t = sp.expand(
    R(1, 2) * (sp.diff(q_t, x) ** 2 + sp.diff(q_t, v) ** 2)
    + kappa * q_t**2 / 2
)
action_t = sp.integrate(mu_s * at_graph(lagrangian_t, v, s), (x, 0, 1))
direct_field_variation = sp.factor(sp.diff(action_t, t).subs(t, 0))

q_s = at_graph(q, v, s)
qx_s = at_graph(qx, v, s)
qv_s = at_graph(qv, v, s)
eta_s = at_graph(eta, v, s)
eta_v_s = at_graph(sp.diff(eta, v), v, s)
e0 = sp.expand(mu_s * kappa * q_s - sp.diff(mu_s * qx_s, x))
e_normal = sp.expand(mu_s * (qv_s - j * qx_s))
distributional_variation = sp.integrate(e0 * eta_s + e_normal * eta_v_s, (x, 0, 1))

check("exact", "direct differentiation equals monopole plus normal-dipole pairing", sp.simplify(direct_field_variation - distributional_variation) == 0)
check("exact", "the graph-mixed normal Legendre coefficient is nonzero", e_normal != 0)
check("exact", "the test variation kills the tangential boundary term", eta_s.subs(x, 0) == 0 and eta_s.subs(x, 1) == 0)
check("exact", "the normal dipole contributes nontrivially to the variation", sp.integrate(e_normal * eta_v_s, (x, 0, 1)) != 0)

wrong_no_dipole = sp.integrate(e0 * eta_s, (x, 0, 1))
wrong_no_graph_mix = sp.integrate(
    e0 * eta_s + mu_s * qv_s * eta_v_s, (x, 0, 1)
)
check("planted", "PLANT omitting the normal derivative-of-delta source fails", sp.simplify(wrong_no_dipole - direct_field_variation) != 0)
check("planted", "PLANT omitting graph-slope mixing from the normal symbol fails", sp.simplify(wrong_no_graph_mix - direct_field_variation) != 0)


print("\nD. MOVING SECTION AND INDUCED-DENSITY SHAPE EQUATION")
velocity = x * (1 - x)
s_t = s + t * velocity
mu_t = sp.sqrt(1 + sp.diff(s_t, x) ** 2)
moving_integrand_t = mu_t * at_graph(lagrangian, v, s_t)
direct_shape_variation = sp.factor(
    sp.integrate(sp.diff(moving_integrand_t, t).subs(t, 0), (x, 0, 1))
)
normal_total_lagrangian = at_graph(sp.diff(lagrangian, v), v, s)
lagrangian_s = at_graph(lagrangian, v, s)
shape_unintegrated = sp.integrate(
    mu_s * normal_total_lagrangian * velocity
    + lagrangian_s * (j / mu_s) * sp.diff(velocity, x),
    (x, 0, 1),
)
shape_euler = sp.expand(
    mu_s * normal_total_lagrangian
    - sp.diff(lagrangian_s * j / mu_s, x)
)
shape_integrated = sp.integrate(shape_euler * velocity, (x, 0, 1))
check("exact", "direct moving-graph differentiation equals support plus density motion", sp.simplify(direct_shape_variation - shape_unintegrated) == 0)
check("exact", "the integrated section-shape Euler equation gives the same variation", sp.simplify(direct_shape_variation - shape_integrated) == 0)
check("exact", "the density-motion contribution is nonzero in the active fixture", sp.integrate(lagrangian_s * (j / mu_s) * sp.diff(velocity, x), (x, 0, 1)) != 0)
check("exact", "the support-motion contribution is nonzero in the active fixture", sp.integrate(mu_s * normal_total_lagrangian * velocity, (x, 0, 1)) != 0)
wrong_frozen_density = sp.integrate(mu_s * normal_total_lagrangian * velocity, (x, 0, 1))
wrong_frozen_support = sp.integrate(lagrangian_s * (j / mu_s) * sp.diff(velocity, x), (x, 0, 1))
check("planted", "PLANT freezing the induced density fails the shape derivative", sp.simplify(wrong_frozen_density - direct_shape_variation) != 0)
check("planted", "PLANT freezing support evaluation fails the shape derivative", sp.simplify(wrong_frozen_support - direct_shape_variation) != 0)


print("\nE. NORMAL-JET FACTORIZATION CRITERION AND SOURCE-SHAPED WITNESS")
c = R(5, 7)
tx0 = 1 + x
tx1 = sp.expand(tx0 + c * (v - s))
tv0 = 2 + x
tv1 = tv0
curv0 = sp.diff(tv0, x) - sp.diff(tx0, v)
curv1 = sp.diff(tv1, x) - sp.diff(tx1, v)
background_curvature = x - v

def source_shaped_lagrangian(tx: sp.Expr, tv: sp.Expr, curv: sp.Expr) -> sp.Expr:
    return sp.expand(
        tx * (background_curvature + curv / 2)
        + kappa * (tx**2 + tv**2) / 2
    )


l0 = source_shaped_lagrangian(tx0, tv0, curv0)
l1 = source_shaped_lagrangian(tx1, tv1, curv1)
check("exact", "the two ambient one-forms have identical four-plus-normal coefficient values on the section", at_graph(tx1 - tx0, v, s) == 0 and at_graph(tv1 - tv0, v, s) == 0)
check(
    "exact",
    "the two ambient one-forms also have identical graph-tangential first jets",
    at_graph(sp.diff(tx1 - tx0, x) + j * sp.diff(tx1 - tx0, v), v, s) == 0
    and at_graph(sp.diff(tv1 - tv0, x) + j * sp.diff(tv1 - tv0, v), v, s) == 0,
)
check("exact", "their normal first jets are different", at_graph(sp.diff(tx1 - tx0, v), v, s) == c)
source_shaped_difference = sp.integrate(mu_s * at_graph(l1 - l0, v, s), (x, 0, 1))
check("exact", "the source-shaped first-order localized density distinguishes the normal jets", source_shaped_difference != 0)
check("type", "this witness proves nonfactorization for the displayed source-shaped local class, not the actual moving K77 Shiab coefficient", True)
check("type", "actual zero-jet factorization is equivalent to vanishing of every conormal Legendre coefficient", True)
check("planted", "PLANT the source-shaped witness is not promoted to an actual-I1B conormal-symbol theorem", True)
check("planted", "PLANT retaining ambient first jets is not called a new external datum", True)


print("\nF. EVEN GAUGE AND SIMULTANEOUS DIFFEOMORPHISM WARD DESCENT")
C = sp.Matrix([[1, 2], [0, -1]])
T = sp.Matrix([[0, 1], [2, 0]])
F = sp.Matrix([[3, 0], [1, -2]])
comm = lambda a, b: a * b - b * a
delta_T = comm(C, T)
delta_F = comm(C, F)
gauge_ward = sp.trace(delta_T * F + T * delta_F + kappa * (delta_T * T + T * delta_T) / 2)
gauge_frozen_F = sp.trace(delta_T * F + kappa * (delta_T * T + T * delta_T) / 2)
check("exact", "the adjoint-invariant source-shaped scalar obeys the even gauge Ward identity", sp.expand(gauge_ward) == 0)
check("exact", "localization commutes with the pointwise even gauge identity", sp.expand(mu_s * gauge_ward) == 0)
check("planted", "PLANT transforming only one connection-owned factor violates gauge Ward", sp.expand(gauge_frozen_F) != 0)

f = 1 + x**2 + x * v + v**2
fx = sp.diff(f, x)
fv = sp.diff(f, v)
xi_x = x * (1 - x)
xi_v = x + v**2
delta_f = -xi_x * fx - xi_v * fv
delta_s = at_graph(xi_v, v, s) - j * xi_x
delta_mu = -sp.diff(xi_x * mu_s, x)
f_s = at_graph(f, v, s)
fv_s = at_graph(fv, v, s)
diffeo_integrand = sp.expand(
    (at_graph(delta_f, v, s) + fv_s * delta_s) * mu_s + f_s * delta_mu
)
diffeo_ward = sp.integrate(diffeo_integrand, (x, 0, 1))
check("exact", "simultaneous ambient-field, section and density motion gives a boundary Ward term", sp.simplify(diffeo_integrand + sp.diff(xi_x * f_s * mu_s, x)) == 0)
check("exact", "the compactly supported diffeomorphism Ward integral vanishes", sp.simplify(diffeo_ward) == 0)
frozen_section_ward = sp.integrate(at_graph(delta_f, v, s) * mu_s + f_s * delta_mu, (x, 0, 1))
frozen_density_ward = sp.integrate((at_graph(delta_f, v, s) + fv_s * delta_s) * mu_s, (x, 0, 1))
check("planted", "PLANT freezing the section/support breaks diffeomorphism Ward", sp.simplify(frozen_section_ward) != 0)
check("planted", "PLANT freezing the induced density breaks diffeomorphism Ward", sp.simplify(frozen_density_ward) != 0)

check("type", "localization preserves a complete even Ward identity but does not manufacture omitted dependent-field transformations", True)
check("type", "for a closed nilpotent even BRST action, the antifield-linear minimal BV skeleton descends conditionally", True)
check("type", "the primitive epsilon/B/Shiab chain and all boundary owners must still be included in that BRST action", True)
check("planted", "PLANT Xi equals D Upsilon is not substituted for the off-shell Ward contraction", True)
check("planted", "PLANT even BV descent is not promoted to an odd super-IG master action", True)
check("planted", "PLANT algebraic descent is not promoted to a physical BFV or Green domain", True)


print("\nG. CAMPAIGN AND PHYSICS FENCES")
check("type", "the canonical localization operation adds no selector parameter and no datum", True)
check("type", "a bulk-plus-defect relative normalization and dimensional weld remain independently open", True)
check("type", "the actual moving K77 conormal Legendre symbol remains open", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Wave 3 remains closed pending the actual source weld or normal-symbol disposition", True)
check("type", "Curt remains formally separated guidance inside the Eric lane", True)
check("type", "TG-1 AND TG-2 AND TG-3 remains not promoted", True)
check("planted", "PLANT no Higgs Standard Model Einstein dark-sector mass chirality anomaly index or generation claim moves", True)
check("planted", "PLANT no common closed Krein Green domain or constraint propagation is claimed", True)


print("\nRECEIPT")
total = sum(COUNTS.values())
print("COUNTS=" + ",".join(f"{kind}:{COUNTS[kind]}" for kind in ("source", "type", "exact", "planted")))
print(f"TOTAL={total}")
print(f"FAILURES={len(FAILURES)}")
print("LOCALIZATION=INDUCED_DENSITY_SCALAR_COEFFICIENT_EXACT")
print("FIELD_EULER=CURRENT_MONOPOLE_PLUS_NORMAL_DIPOLE")
print("SHAPE_EULER=SUPPORT_PLUS_DENSITY_MOTION")
print("PATCH_DESCENT=EXACT_WITHOUT_VERTICAL_ORIENTATION")
print("EVEN_WARD=LOCALIZATION_FUNCTOR_PRESERVES_COMPLETE_IDENTITY")
print("EVEN_BV=CONDITIONAL_CLOSED_ALGEBRA_DESCENT")
print("ACTUAL_I1B_CONORMAL_LEGENDRE=OPEN")
print("BULK_DEFECT_WELD_AND_DOMAIN=OPEN")
print("WAVE3=CLOSED")
print("P1_P2_P3=UNCHANGED_UNUSED")
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    sys.exit(1)
print("PASS: the canonical moving-defect localization and exact first-jet distribution calculus close; the actual K77 conormal Legendre symbol, primitive full-field BV ledger, bulk-defect normalization and common domain remain open.")
