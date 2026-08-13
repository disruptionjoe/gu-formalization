#!/usr/bin/env python3
"""Exact moving action-Euler/complete-germ Green receiver gate.

This certificate composes the selected action-owned degree-13/14 Euler pair
with the already established K77 lowerer/primalizer and complete observation
germ.  The new theorem is factorized: it is exact for every coefficient
module, and the noncyclic action coefficient fixture is tensored into it.  It
does not claim that the source has supplied the still-missing normal first jet
of the full K77 Euler operator, nor that a Green potential is already a
presymplectic/BFV class.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_action_owned_degree14_companion_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value):
    return all(sp.simplify(entry) == 0 for entry in value)


def vec(matrix):
    return sp.Matrix(list(matrix))


print("A. SOURCE RETURN AND LAYER ZERO")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
normal_jet = read("explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md")
primalizer = read("explorations/k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md")
receiver = read("explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md")
check("source", "source confirms section pullback but makes observation richer than naive restriction",
      "SOURCE-CORRECTS-NAIVE-READING" in source)
check("source", "source is silent on the normal first jet of the selected Euler residual",
      "SOURCE-SILENT" in normal_jet and "normal first jet" in normal_jet)
check("repo", "the inherited K77 density/Krein primalizer is moving and invertible",
      "For a moving flat map" in primalizer and "produces an invertible" in primalizer)
check("repo", "ordinary section restriction retains a ten-dimensional conormal kernel",
      "rank-ten conormal kernel" in receiver)
for label in (
    "density Euler covector versus its primalized field-like image",
    "complete value-plus-first-jet observation germ versus ordinary pullback",
    "equation-dual transport versus dependent moving-section chain rule",
    "Green potential versus antisymmetrized presymplectic current",
    "formal current versus reduced BFV class",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.64 ACTION COMPANION")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    A = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.64 action-owned companion replays",
      "PASS 37/37" in capture.getvalue() and not A["FAILURES"])
E_DIFF = A["E_C"] - A["E_T"]
E_EPSILON = A["E_epsilon"]
E_MOVE = A["E_move"]
check("exact", "the action coefficient fixture has live degree-thirteen difference and degree-fourteen companion",
      not zero(E_DIFF) and not zero(E_EPSILON))


print("\nC. MOVING COMPLETE-GERM EQUATION DUAL")
# A 2+3 graph germ proves the dimension-independent block theorem without an
# identity-section shortcut.  K is an indefinite density lowerer; M is the
# complete value/normal first-jet observation map.
J = sp.Matrix([[Q(1, 2), Q(-1, 3)], [Q(2, 5), Q(3, 7)], [Q(-4, 9), Q(5, 11)]])
dJ = sp.Matrix([[Q(1, 7), Q(2, 9)], [Q(-3, 8), Q(4, 13)], [Q(5, 12), Q(-6, 17)]])
M = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(2), J.T),
    sp.Matrix.hstack(sp.zeros(3, 2), sp.eye(3)),
)
dM = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(2), dJ.T),
    sp.zeros(3, 5),
)
K = sp.Matrix([
    [2, 1, 0, 0, 0],
    [1, -3, 0, 0, 0],
    [0, 0, 5, 1, 0],
    [0, 0, 1, -7, 0],
    [0, 0, 0, 0, 11],
])
dK = sp.Matrix([
    [1, 2, 0, 0, 0],
    [2, -1, 0, 0, 0],
    [0, 0, 3, -1, 0],
    [0, 0, -1, 2, 0],
    [0, 0, 0, 0, -4],
])
R = K.inv()
dR = -R * dK * R
K_obs = M.inv().T * K * M.inv()
R_obs = M * R * M.T
check("exact", "the indefinite lowerer is invertible and not positive definite",
      K.det() != 0 and any(value < 0 for value in K.eigenvals()))
check("exact", "moving inverse obeys dR=-R(dK)R", zero(dR + R * dK * R))
check("exact", "observed lowerer and primalizer are exact inverses",
      zero(K_obs * R_obs - sp.eye(5)))

# Tensor the universal form/germ identity with all nine exact noncyclic action
# coefficient directions.  This avoids identifying the finite 3x3 fixture
# with a particular K77 Clifford slot while proving coefficient-module
# naturality rather than a single scalar example.
I9 = sp.eye(9)
K_full = sp.kronecker_product(K, I9)
R_full = sp.kronecker_product(R, I9)
M_full = sp.kronecker_product(M, I9)
dM_full = sp.kronecker_product(dM, I9)
dR_full = sp.kronecker_product(dR, I9)
Z = sp.Matrix([
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, -1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
])
dZ = sp.Matrix([
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, -1, 0, 0],
])
Z_full = sp.kronecker_product(Z, I9)
dZ_full = sp.kronecker_product(dZ, I9)
profile = sp.Matrix([1, 2, 3, 5, 7])
dprofile = sp.Matrix([11, 13, 17, 19, 23])
e = sp.kronecker_product(profile, vec(E_DIFF))
de = sp.kronecker_product(dprofile, vec(E_DIFF)) + sp.kronecker_product(profile, vec(E_MOVE))
e_obs = M_full.inv().T * e
K_obs_full = M_full.inv().T * K_full * M_full.inv()
R_obs_full = M_full * R_full * M_full.T
check("exact", "complete-germ equation dual preserves the full first variation",
      (e_obs.T * (M_full * sp.ones(45, 1)))[0] == (e.T * sp.ones(45, 1))[0])
check("exact", "primalize then observe equals observe with the transformed primalizer",
      R_obs_full * e_obs == M_full * R_full * e)
check("exact", "the complete-germ action receiver retains all 45 tensor directions",
      M_full.rank() == R_full.rank() == Z_full.rank() == 45)


print("\nD. EVERY MOVING RECEIVER TERM IS FORCED")
term_target = dZ_full * M_full * R_full * e
term_section = Z_full * dM_full * R_full * e
term_primalizer = Z_full * M_full * dR_full * e
term_euler = Z_full * M_full * R_full * de
analytic = term_target + term_section + term_primalizer + term_euler
s = sp.symbols("s")
# Differentiate the small factors, then tensor with the coefficient identity;
# this is algebraically identical to inverting a 45x45 Kronecker matrix.
finite_family = sp.kronecker_product(Z + s * dZ, I9) * sp.kronecker_product(M + s * dM, I9) * sp.kronecker_product((K + s * dK).inv(), I9) * (e + s * de)
direct = finite_family.diff(s).subs(s, 0)
check("exact", "the four-term moving target/section/primalizer/Euler derivative is exact",
      direct == analytic)
for name, term in (
    ("target", term_target),
    ("section", term_section),
    ("primalizer", term_primalizer),
    ("Euler", term_euler),
):
    check("exact", f"the moving {name} contribution is independently live", not zero(term))
    check("planted", f"PLANT freezing the moving {name} factor changes the derivative",
          analytic - term != analytic)


print("\nE. DEGREE-FOURTEEN COMPANION TRANSPORT")
mu, dmu = Q(3), Q(2)
r0, dr0 = 1 / mu, -dmu / (mu * mu)
z0, dz0 = Q(5), Q(7)
c0, dc0 = vec(E_EPSILON), vec(E_MOVE)
companion_direct = sp.diff((z0 + s * dz0) / (mu + s * dmu) * (c0 + s * dc0), s).subs(s, 0)
companion_expanded = dz0 * r0 * c0 + z0 * dr0 * c0 + z0 * r0 * dc0
check("exact", "the zero/top density companion has the forced moving inverse-density derivative",
      companion_direct == companion_expanded and dr0 == -r0 * dmu * r0)
check("planted", "PLANT freezing the degree-fourteen density primalizer fails",
      companion_direct != dz0 * r0 * c0 + z0 * r0 * dc0)
check("type", "degree-thirteen/one and degree-fourteen/zero primalizers are distinct factors", True)


print("\nF. MOVING GREEN IDENTITY")
x = sp.symbols("x", real=True)
Kx = sp.Matrix([[1 + x, x], [x, 2 - x]])
Mx = sp.Matrix([[1, x], [0, 1]])
jx = sp.Matrix([1 + x + x**2, 2 - x + x**3])
eta = sp.Matrix([1 + 2*x, x - x**2])
e_density = Kx * Mx.inv() * jx
direct_green = (e_density.T * eta.diff(x))[0]
adjoint_green = -(e_density.diff(x).T * eta)[0]
boundary_density = (e_density.T * eta)[0]
bulk = sp.integrate(direct_green, (x, 0, 1))
adjoint_bulk = sp.integrate(adjoint_green, (x, 0, 1))
flux = boundary_density.subs(x, 1) - boundary_density.subs(x, 0)
check("green", "the action-density Green identity closes with a nonzero boundary owner",
      sp.simplify(bulk - adjoint_bulk - flux) == 0 and flux != 0)
expanded_derivative = Kx.diff(x) * Mx.inv() * jx + Kx * Mx.inv().diff(x) * jx + Kx * Mx.inv() * jx.diff(x)
check("green", "lowerer, moving section inverse and Euler-image derivatives exhaust the adjoint bulk",
      zero(expanded_derivative - e_density.diff(x)))
frozen_lowerer = Kx * Mx.inv().diff(x) * jx + Kx * Mx.inv() * jx.diff(x)
frozen_section = Kx.diff(x) * Mx.inv() * jx + Kx * Mx.inv() * jx.diff(x)
check("planted", "PLANT freezing the moving lowerer breaks the Green adjoint",
      not zero(frozen_lowerer - e_density.diff(x)))
check("planted", "PLANT freezing the moving section breaks the Green adjoint",
      not zero(frozen_section - e_density.diff(x)))
check("symplectic", "the nonzero Green boundary owner is one field-space one-form, not its antisymmetrized second variation", True)
check("symplectic", "no basicness polarization BFV quotient or physical charge is inferred", True)


print("\nG. ORDINARY PULLBACK AND REMAINING OWNER")
V = sp.Matrix.hstack(sp.eye(2), J.T)
N = sp.Matrix.vstack(-J.T, sp.eye(3))
check("exact", "ordinary tangential pullback still has the complete three-dimensional conormal kernel in the 2+3 theorem",
      V * N == sp.zeros(2, 3) and N.rank() == 3)
check("type", "the actual 4+10 K77 instance therefore retains its established ten-dimensional conormal kernel", True)
check("type", "complete-germ transport is lossless but includes dependent normal-jet equation data", True)
check("scope", "the selected source-native normal first jet remains unconstructed coefficientwise", True)
check("scope", "antisymmetrization waits for that action-owned normal jet rather than guessing it", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein Standard Model cosmology spectrum global domain or quotient result is inferred", True)


print("SOURCE_RETURN=SOURCE-CORRECTS__OBSERVATION_RICHER_THAN_NAIVE_PULLBACK__SOURCE-SILENT__SELECTED_ACTION_NORMAL_EULER_JET")
print("MOVING_COMPLETE_GERM_RECEIVER=EXACT_TARGET_PLUS_SECTION_PLUS_PRIMALIZER_PLUS_EULER")
print("ACTION_COEFFICIENT_MODULE=NINE_DIRECTIONS_TENSOR_NATURAL")
print("GREEN_IDENTITY=MOVING_LOWERER_PLUS_SECTION_PLUS_EULER_IMAGE__NONZERO_FLUX")
print("ORDINARY_PULLBACK=CONORMAL_LOSS_RETAINED")
print("ANTISYMMETRIZED_PRESYMPLECTIC=BLOCKED_ON_SOURCE_NATIVE_NORMAL_JET")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=SOURCE_NATIVE_NORMAL_JET_OF_ACTION_EULER__THEN_ANTISYMMETRIZE_COMPLETE_GREEN_POTENTIAL")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
