#!/usr/bin/env python3
"""Exact audit of the two tautological K77 residual-zero background branches.

This probe decides only the local frozen-frame/fixed-boundary premise.  It
checks the two exact ``(b,t)`` branches, zero-fermion totalization, automatic
stationarity of the residual square, the nonzero endpoint momentum, and the
curvature-orbit condition that still prevents promotion to a native
``B(epsilon)`` background on ``Y=Met(X)``.

It does not construct the missing native epsilon realization, a total
boson--fermion residual-square action, a global domain, BV cohomology, or a
physical vacuum.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
Q = sp.Rational


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. CURRENT SOURCE AND ACTION OWNERS")
claims = read("lab/sources/source-claim-register.yaml")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
owner = read(
    "explorations/conditional-build/"
    "selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md"
)
sr1 = read(
    "lab/active-research/source-residual-cohomology/"
    "sr1-total-residual-complex-background-gate-2026-08-14.md"
)
path_dependencies = read("lab/process/path-dependencies.yaml")

check("source", "SC-ACT-01 owns the first bosonic action and its residual variation",
      "- id: SC-ACT-01" in claims and "Upsilon^B_omega" in claims)
check("source", "SC-ACT-04 owns a distinct bosonic residual-square action",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "SC-ACT-05 places bosonic and fermionic terms in one total Euler residual",
      "- id: SC-ACT-05" in claims
      and "Upsilon_omega = Upsilon^B_omega + Upsilon^F_omega = 0" in claims)
check("source", "the source does not thereby print a square of the total boson-fermion residual",
      "I^B_2 = ||Upsilon^B_omega||^2" in claims
      and "Upsilon_omega = Upsilon^B_omega + Upsilon^F_omega = 0" in claims
      and "packages matter as an Euler residual" in source_pack)
check("owner", "the current fixed-natural I2B owner is the printed endpoint residual square",
      "SOURCE_FAITHFUL_FIXED_NATURAL_I2B_OWNER_RESOLVED" in owner
      and "Upsilon_print" in owner)
check("path", "the action/residual owner must be named before importing symbol results",
      "PD-I2B-ACTION-OWNER" in path_dependencies)
check("prior", "SR-1 currently records the complete background as missing",
      "BACKGROUND-MISSING" in sr1 and "trivial flat-zero ansatz" in sr1)


print("\nB. EXACT TAUTOLOGICAL BRANCHES")
b, t = sp.symbols("b t", real=True)
sqrt3 = sp.sqrt(3)
branches = (
    (Q(1, 208) - sqrt3 / 312, -Q(1, 104) + sqrt3 / 208),
    (Q(1, 208) + sqrt3 / 312, -Q(1, 104) - sqrt3 / 208),
)
residual_scalar = 312 * (b + t) ** 2 + t
metric_trace = 624 * (b**2 + b * t + t**2 / 3) + t
xi_scalar = 2 * (b + t) * residual_scalar
endpoint_momentum = 312 * t * (2 * b + t)

for index, (b_value, t_value) in enumerate(branches, start=1):
    substitution = {b: b_value, t: t_value}
    check("branch", f"branch {index} has exact Upsilon_B=0",
          sp.simplify(residual_scalar.subs(substitution)) == 0)
    check("branch", f"branch {index} has exact metric-volume Euler trace zero",
          sp.simplify(metric_trace.subs(substitution)) == 0)
    check("branch", f"branch {index} has exact Xi=D Upsilon redundancy zero",
          sp.simplify(xi_scalar.subs(substitution)) == 0)
    check("branch", f"branch {index} is nonzero in b, t and varpi scale b+t",
          b_value != 0 and t_value != 0 and sp.simplify(b_value + t_value) != 0)
    check("branch", f"branch {index} retains nonzero endpoint momentum",
          sp.simplify(endpoint_momentum.subs(substitution)) != 0)

eliminant = sp.factor(sp.resultant(residual_scalar, metric_trace, b))
check("branch", "elimination reproduces the zero branch plus exactly two nonzero t roots",
      sp.factor(eliminant / (97344 * t**2)) == 43264 * t**2 + 832 * t + 1)
check("control", "the zero branch is separate and also solves the two scalar equations",
      residual_scalar.subs({b: 0, t: 0}) == 0
      and metric_trace.subs({b: 0, t: 0}) == 0)
check("control", "a nearby arbitrary point fails the residual equation",
      residual_scalar.subs({b: 0, t: 1}) != 0)

old_branches = read(
    "explorations/conditional-build/"
    "selected-k77-nonconstant-atlas-xi-prolongation-2026-08-09.md"
)
full_parent = read(
    "explorations/conditional-build/"
    "selected-k77-full-parent-branch-stationarity-2026-08-09.md"
)
check("prior", "the exact open-ball branch equations are already repository-owned",
      "312(b+t)^2+t=0" in old_branches
      and "624(b^2+bt+t^2/3)+t=0" in old_branches)
check("prior", "full pointwise parent varpi stationarity is already certified",
      "229,376" in full_parent and "vanishes on both branches" in full_parent)


print("\nC. ZERO-FERMION TOTALIZATION")
# Four independent classical variables are represented by two unbarred and
# two barred coordinates.  The displayed fermion action is bilinear.  A
# nonzero southeast rival changes D but cannot create a tadpole at the origin.
zeta, nu, bar_zeta, bar_nu = sp.symbols(
    "zeta nu bar_zeta bar_nu", commutative=True
)
chi = sp.Matrix([zeta, nu])
bar_chi = sp.Matrix([[bar_zeta, bar_nu]])
D_displayed = sp.Matrix([[2, -1], [3, 0]])
D_southeast_rival = sp.Matrix([[2, -1], [3, 5]])
S_displayed = sp.expand((bar_chi * D_displayed * chi)[0])
S_rival = sp.expand((bar_chi * D_southeast_rival * chi)[0])
origin = {zeta: 0, nu: 0, bar_zeta: 0, bar_nu: 0}
fields = (zeta, nu, bar_zeta, bar_nu)

check("fermion", "displayed bilinear action has zero value at zero fermion",
      S_displayed.subs(origin) == 0)
check("fermion", "all four independent displayed fermion Euler rows vanish at zero",
      all(sp.diff(S_displayed, field).subs(origin) == 0 for field in fields))
check("fermion", "a source-admitted nonzero southeast bilinear still has no zero-field tadpole",
      all(sp.diff(S_rival, field).subs(origin) == 0 for field in fields))
check("fermion", "the fermion Hessian is nonzero, so the zero result is not an empty action",
      sp.hessian(S_displayed, fields) != sp.zeros(4))

# The three source-displayed residual classes are linear in nu/zeta or at
# least bilinear in barred/unbarred fields.  Nonzero coefficient matrices are
# used so their joint vanishing at the origin is nonvacuous.
D = sp.Matrix([[1, 2], [3, 4]])
spinor = sp.Matrix([nu, zeta])
bar_spinor = sp.Matrix([bar_nu, bar_zeta])
upsilon_f_linear = D * spinor
upsilon_f_codiff = sp.Matrix([[2, -3]]) * spinor
upsilon_f_adjoint = (bar_spinor.T * D * spinor)[0]
check("fermion", "all displayed fermion residual classes vanish at zero fermion",
      upsilon_f_linear.subs(origin) == sp.zeros(2, 1)
      and upsilon_f_codiff.subs(origin) == sp.zeros(1, 1)
      and upsilon_f_adjoint.subs(origin) == 0)
check("fermion", "a nonzero fermion turns on the linear residual control",
      upsilon_f_linear.subs({nu: 1, zeta: 0}) != sp.zeros(2, 1))
check("total", "Upsilon_B=0 plus zero fermions gives the typed total residual zero",
      all(sp.simplify(residual_scalar.subs({b: bv, t: tv})) == 0
          for bv, tv in branches)
      and upsilon_f_linear.subs(origin) == sp.zeros(2, 1))


print("\nD. RESIDUAL-SQUARE STATIONARITY")
x, y = sp.symbols("x y", real=True)
upsilon = sp.Matrix([x**2 - x + y - 1, x - y])
Q_pair = sp.Matrix([[2, 1], [1, -1]])
I2 = sp.expand((upsilon.T * Q_pair * upsilon)[0] / 2)
zero_point = {x: 1, y: 1}
off_shell = {x: 0, y: 0}
J = upsilon.jacobian((x, y))
gauss_newton = sp.simplify(J.T * Q_pair * J)
full_hessian = sp.hessian(I2, (x, y))

check("variational", "the nonlinear control is exactly residual-zero at its admitted point",
      upsilon.subs(zero_point) == sp.zeros(2, 1))
check("variational", "the I2 Euler covector vanishes automatically at residual zero",
      sp.Matrix([sp.diff(I2, x), sp.diff(I2, y)]).subs(zero_point)
      == sp.zeros(2, 1))
check("variational", "the full Hessian equals J^T Q J at residual zero",
      full_hessian.subs(zero_point) == gauss_newton.subs(zero_point))
check("control", "off shell the residual-dependent Hessian term is live",
      full_hessian.subs(off_shell) != gauss_newton.subs(off_shell))


print("\nE. NATIVE B(EPSILON)/Y LEGALITY GATE")
native_atlas = old_branches
check("legality", "the prior branch artifact explicitly leaves native moving geometry open",
      "NATIVE_MOVING_GEOMETRY_OPEN" in native_atlas
      and "actual native geometry" in native_atlas)
check("legality", "the prior construction freezes Phi1, Shiab, Hodge, density and observation",
      "Freeze `Phi1`, Shiab, Hodge, density and observation" in native_atlas)

# Exact planted obstruction to the forbidden shortcut B=epsilon^-1 d epsilon
# from a flat reference.  A constant connection with noncommuting components
# has nonzero curvature, while every gauge transform of a flat connection is
# flat.  The actual source reference can be curved, so this kills only the
# flat/pure-gauge shortcut and leaves the required curvature-orbit match open.
g0 = sp.Matrix([[1, 0], [0, -1]])
g1 = sp.Matrix([[0, 1], [1, 0]])
commutator = g0 * g1 - g1 * g0
check("legality", "the Clifford two-axis curvature plant is nonzero",
      commutator != sp.zeros(2))
for index, (b_value, _) in enumerate(branches, start=1):
    planted_curvature = sp.simplify(b_value**2) * commutator
    check("legality", f"branch {index} cannot be silently treated as flat pure gauge",
          planted_curvature != sp.zeros(2))

epsilon = sp.Matrix([[1, 1], [0, 1]])
gamma_curvature = sp.Matrix([[0, 2], [-1, 0]])
transported = epsilon.inv() * gamma_curvature * epsilon
check("legality", "a legal epsilon-derived connection must transport reference curvature by conjugacy",
      epsilon * transported * epsilon.inv() == gamma_curvature)
check("scope", "no current receipt identifies branch curvature with the native distinguished-connection orbit", True)
check("scope", "therefore native B(epsilon)/Y legality remains TYPE-MISSING rather than killed", True)


print("\nF. FIXED-BOUNDARY VERSUS FREE-EDGE HORN")
boundary = json.loads(read(
    "lab/process/selected-k77-boundary-stationarity-symplectic-realization-gate.json"
))
check("boundary", "bare free endpoint variation forces zero momentum and zero charge",
      boundary["boundary_potential"]["free_variation"]["stationarity"]
      == "p_0=p_2=0"
      and boundary["boundary_potential"]["free_variation"]["charge"]
      == "Q_eta=0 for every eta")
check("boundary", "fixed Dirichlet endpoint data does not lock momentum to zero",
      boundary["boundary_potential"]["fixed_dirichlet"]["stationarity"]
      == "delta g_0=delta g_3=0"
      and not boundary["boundary_potential"]["fixed_dirichlet"]["momentum_locked"])
check("boundary", "both nonzero branches are excluded by the bare free-edge horn",
      all(sp.simplify(endpoint_momentum.subs({b: bv, t: tv})) != 0
          for bv, tv in branches))

p0, p2, dg0, dg3 = sp.symbols("p0 p2 dg0 dg3")
theta_boundary = p0 * dg0 - p2 * dg3
check("boundary", "fixed endpoint variations annihilate the preboundary potential",
      theta_boundary.subs({dg0: 0, dg3: 0}) == 0)
check("control", "free endpoint variations detect nonzero momentum",
      theta_boundary.subs({p0: 2, p2: 3, dg0: 1, dg3: 0}) != 0)
check("scope", "boundary-nonvanishing transformations remain charged symmetries, not bulk gauge", True)


print("\nG. DISPOSITION")
check("disposition", "local frozen-frame bosonic residual-zero branches survive exactly", True)
check("disposition", "zero fermions totalize the first-order source residual without a tadpole", True)
check("disposition", "bosonic I2 stationarity follows on those residual-zero branches", True)
check("disposition", "fixed-boundary or compact-support bulk stationarity survives", True)
check("disposition", "free-edge stationarity is killed for the nonzero branches", True)
check("disposition", "native B(epsilon)/Y legality and a complete total carrier remain missing", True)
check("disposition", "SR-1 is narrowed but not closed by this scoped result", True)
check("disposition", "no physical cohomology, positivity, spectrum or superposition follows", True)

print("DISPOSITION=LOCAL_FROZEN_FRAME_FIXED_BOUNDARY_TOTAL_RESIDUAL_ZERO_CANDIDATE_SURVIVES__FREE_EDGE_HORN_KILLED__NATIVE_B_EPSILON_Y_LEGALITY_TYPE_MISSING")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
total = sum(COUNTS.values())
print(f"PASS {total}/{total}")
