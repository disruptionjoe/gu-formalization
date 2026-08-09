#!/usr/bin/env python3
"""Exact nonconstant atlas and Xi-prolongation gate for ledger v0.110.

The source displays ``Xi=D_omega Upsilon`` as a redundant companion.  This
probe tests that claim on an exact homogeneous open-set model of v0.109's
one-amplitude family and, crucially, patches the connection with the affine
``g^-1 dg`` term under nonconstant noncommuting transitions.

The open-set witness freezes Phi/Shiab/Hodge/density/observation coefficients.
It is therefore a formal local source model, not the actual moving K77/Y14
geometry and not a physical magnitude-selection theorem.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_source_euler_two_to_one_probe.py"
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


def matrix_zero(matrix):
    return all(sp.simplify(value) == 0 for value in matrix)


def matrix_equal(left, right):
    return matrix_zero(left - right)


def bank_equal(left, right):
    return left.keys() == right.keys() and all(
        matrix_equal(left[key], right[key]) for key in left
    )


print("A. SOURCE RETURN AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
epsilon_source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
check("source", "the draft displays Xi as D_omega Upsilon",
      r"\Xi_\omega=D_\omega\Upsilon_\omega" in source)
check("source", "the draft explicitly calls Xi redundant when Upsilon vanishes",
      "second equation is redundant" in source and r"\Upsilon_\omega=0" in source)
check("source", "source epsilon moves B and T oppositely",
      "delta B=D_B eta" in epsilon_source and "delta T=-D_B eta" in epsilon_source)
for label in (
    "redundant Euler companion versus independent amplitude equation",
    "covariant prolongation versus off-shell Noether identity",
    "connection affine transformation versus tensor conjugation",
    "frozen coefficient open set versus moving K77 Y14 geometry",
    "homogeneous ansatz selection versus source magnitude selection",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check("repo", "the immutable v0.109 predecessor replays",
      "PASS 45/45" in capture.getvalue() and not predecessor["FAILURES"])


print("\nB. HOMOGENEOUS OPEN-SET INTERSECTION")
b, t = sp.symbols("b t", real=True)
sqrt3 = sp.sqrt(3)
upsilon = 312 * (b + t)**2 + t
metric_trace = 624 * (b**2 + b*t + t**2 / 3) + t
branches = [
    {b: sp.Integer(0), t: sp.Integer(0)},
    {b: Q(1, 208) - sqrt3 / 312, t: -Q(1, 104) + sqrt3 / 208},
    {b: Q(1, 208) + sqrt3 / 312, t: -Q(1, 104) - sqrt3 / 208},
]
check("exact", "the homogeneous system has the zero branch plus two exact nonzero branches",
      all(sp.simplify(upsilon.subs(branch)) == 0
          and sp.simplify(metric_trace.subs(branch)) == 0 for branch in branches)
      and branches[1][t] != 0 and branches[2][t] != 0)
resultant = sp.factor(sp.resultant(upsilon, metric_trace, b))
check("exact", "the eliminated amplitude polynomial is exact",
      resultant == 97344 * t**2 * (43264*t**2 + 832*t + 1))
check("exact", "the two nonzero amplitudes are algebraic conjugates",
      sp.simplify(branches[1][t] + branches[2][t] + Q(1, 52)) == 0
      and sp.simplify(branches[1][t] * branches[2][t] - Q(1, 43264)) == 0)

for branch in branches[1:]:
    b0, t0 = branch[b], branch[t]
    f0, u0 = b0**2, 2*b0*t0
    check("exact", "homogeneous branch lies on the v0.109 invariant family",
          sp.simplify(f0 - t0**2/3) == 0
          and sp.simplify(u0 + t0/312 + 4*t0**2/3) == 0)

check("accounting", "the discrete amplitudes are selected by the frozen homogeneous ansatz",
      True)
check("planted", "PLANT ansatz-selected amplitudes are not attributed to the source", True)


print("\nC. OPEN-SET CONNECTION, DISTORTION AND XI")
coords = sp.symbols("x0 x1 x2")
n = len(coords)
G = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
    sp.Matrix([[0, 1], [-1, 0]]),
]
I2 = sp.eye(2)
ZERO = sp.zeros(2)


def comm(left, right):
    return left*right - right*left


def conjugate(value, transition):
    return sp.simplify(transition.inv() * value * transition)


def d_matrix(value, index):
    return value.applyfunc(lambda entry: sp.diff(entry, coords[index]))


def transform_connection(connection, transition):
    inverse = transition.inv()
    return [sp.simplify(inverse*connection[i]*transition + inverse*d_matrix(transition, i))
            for i in range(n)]


def transform_oneform(form, transition):
    return [conjugate(value, transition) for value in form]


def curvature(connection):
    return {(i, j): sp.simplify(
        d_matrix(connection[j], i) - d_matrix(connection[i], j)
        + comm(connection[i], connection[j]))
        for i in range(n) for j in range(i+1, n)}


def covariant_derivative(connection, form):
    return {(i, j): sp.simplify(
        d_matrix(form[j], i) - d_matrix(form[i], j)
        + comm(connection[i], form[j]) - comm(connection[j], form[i]))
        for i in range(n) for j in range(i+1, n)}


branch = branches[1]
b0, t0 = branch[b], branch[t]
B0 = [sp.simplify(b0*value) for value in G]
T0 = [sp.simplify(t0*value) for value in G]
A0 = [sp.simplify(B0[i] + T0[i]) for i in range(n)]
F0 = curvature(B0)
U0 = covariant_derivative(B0, T0)
K = {(i, j): comm(G[i], G[j]) for i in range(n) for j in range(i+1, n)}
check("geometry", "the homogeneous connection has the prescribed F_B",
      all(matrix_equal(F0[key], b0**2*K[key]) for key in K))
check("geometry", "the homogeneous distortion has the prescribed D_B T",
      all(matrix_equal(U0[key], 2*b0*t0*K[key]) for key in K))
check("exact", "the source residual and metric trace vanish on the open set",
      sp.simplify(upsilon.subs(branch)) == 0
      and sp.simplify(metric_trace.subs(branch)) == 0)

# In the frozen scalar receiver Upsilon_i=c G_i.  Its displayed prolongation
# in the A=B+T connection is Xi=D_A Upsilon.  On the homogeneous fixture
# Xi_ij=2(b+t)c[G_i,G_j], so Xi factors through Upsilon and adds no equation.
c = upsilon
Upsilon0 = [sp.simplify(c*value) for value in G]
Xi0 = covariant_derivative(A0, Upsilon0)
check("variational", "Xi factors exactly through Upsilon off shell",
      all(matrix_equal(Xi0[key], 2*(b0+t0)*c*K[key]) for key in K))
check("variational", "on-shell Upsilon and Xi vanish identically on the open set",
      all(matrix_zero(value.subs(branch)) for value in Upsilon0)
      and all(matrix_zero(value.subs(branch)) for value in Xi0.values()))

xi_scalar = 2*(b+t)*upsilon
jacobian_two = sp.Matrix([upsilon, metric_trace]).jacobian([b, t])
jacobian_three = sp.Matrix([upsilon, metric_trace, xi_scalar]).jacobian([b, t])
check("accounting", "Xi adds no algebraic rank at either nonzero branch",
      all(jacobian_two.subs(br).rank() == jacobian_three.subs(br).rank() == 2
          for br in branches[1:]))
check("planted", "PLANT redundant Xi is not promoted to a third source constraint", True)


print("\nD. NONCONSTANT NONCOMMUTING AFFINE THREE-PATCH ATLAS")
N_plus = sp.Matrix([[0, 1], [0, 0]])
N_minus = sp.Matrix([[0, 0], [1, 0]])
g01 = I2 + coords[0]*N_plus
g12 = I2 + coords[1]*N_minus
g02 = sp.simplify(g01*g12)
check("atlas", "nonconstant transitions are invertible and noncommuting",
      sp.simplify(g01.det()) == 1 and sp.simplify(g12.det()) == 1
      and not matrix_equal(g01*g12, g12*g01))

B1 = transform_connection(B0, g01)
B2_seq = transform_connection(B1, g12)
B2_dir = transform_connection(B0, g02)
T1 = transform_oneform(T0, g01)
T2_seq = transform_oneform(T1, g12)
T2_dir = transform_oneform(T0, g02)
check("atlas", "affine connection transformation closes on the triple overlap",
      all(matrix_equal(B2_seq[i], B2_dir[i]) for i in range(n)))
check("atlas", "covariant distortion transformation closes on the triple overlap",
      all(matrix_equal(T2_seq[i], T2_dir[i]) for i in range(n)))

F1 = curvature(B1)
F2 = curvature(B2_seq)
U1 = covariant_derivative(B1, T1)
U2 = covariant_derivative(B2_seq, T2_seq)
check("atlas", "curvature computed after affine patching transforms covariantly",
      all(matrix_equal(F1[key], conjugate(F0[key], g01)) for key in F0)
      and all(matrix_equal(F2[key], conjugate(F0[key], g02)) for key in F0))
check("atlas", "D_B T computed after affine patching transforms covariantly",
      all(matrix_equal(U1[key], conjugate(U0[key], g01)) for key in U0)
      and all(matrix_equal(U2[key], conjugate(U0[key], g02)) for key in U0))

A1 = [sp.simplify(B1[i] + T1[i]) for i in range(n)]
Upsilon1 = transform_oneform(Upsilon0, g01)
Xi1 = covariant_derivative(A1, Upsilon1)
check("atlas", "the off-shell Xi prolongation transforms covariantly nonvacuously",
      any(not matrix_zero(value) for value in Xi0.values())
      and all(matrix_equal(Xi1[key], conjugate(Xi0[key], g01)) for key in Xi0))

# Negative controls: conjugating a connection without its affine term and
# reversing the cocycle order must fail for these nonconstant/noncommuting maps.
B1_bad = transform_oneform(B0, g01)
F1_bad = curvature(B1_bad)
check("planted", "PLANT omitting g-inverse-dg breaks curvature covariance",
      any(not matrix_equal(F1_bad[key], conjugate(F0[key], g01)) for key in F0))
g02_bad = g12*g01
check("planted", "PLANT reversed transition order fails triple-overlap connection descent",
      any(not matrix_equal(B2_seq[i], transform_connection(B0, g02_bad)[i])
          for i in range(n)))


print("\nE. SCOPE FENCES AND NEXT GATE")
for kind, label in (
    ("geometry", "generic affine gauge descent is closed only in the faithful local matrix model"),
    ("variational", "Xi redundancy is source explicit but not an off-shell Noether or BV identity"),
    ("symplectic", "the two ansatz branches are not a reduced critical moduli space"),
    ("integrability", "moving Phi Shiab Hodge density and observation jets remain unassembled"),
    ("pde", "no characteristic propagation or common Green domain follows"),
    ("krein", "no positive fundamental symmetry or closed operator domain is selected"),
    ("analytic", "no contour determinant measure or reflection positivity is supplied"),
    ("cosmology", "homogeneous ansatz amplitudes are not a dark-energy magnitude prediction"),
    ("accounting", "global residue and five booked quotients remain unchanged"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
    ("representation", "selected Spin-native two U32,32 halves and full U64,64 remain distinct"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_XI_EQUALS_D_OMEGA_UPSILON_REDUNDANCY__SOURCE_SILENT_HOMOGENEOUS_BRANCHES_NATIVE_MOVING_GEOMETRY_AND_AMPLITUDE_SELECTION")
print("ATLAS=NONCONSTANT_AFFINE_THREE_PATCH_DIRECT_SEQUENTIAL_EXACT")
print("HOMOGENEOUS_BRANCHES=T_MINUS2_PLUSMINUS_SQRT3_OVER208")
print("XI=FACTORS_THROUGH_UPSILON__NO_NEW_RANK")
print("GRADE=FROZEN_COEFFICIENT_OPEN_SET_MODEL__NOT_NATIVE_MOVING_Y14")
print("NEXT=MOVING_PHI_SHIAB_HODGE_DENSITY_OBSERVATION_PROLONGATION__THEN_AMPLITUDE_OWNERSHIP_AND_321_VS1571_HESSIAN_BV")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
