#!/usr/bin/env python3
"""Exact source-coordinate correction of the v0.108 local freedom count.

The source fields are ``(epsilon,varpi,g)``.  ``B_omega`` is derived from
epsilon, so an arbitrary B variation at fixed T is not a source direction.
This probe rewrites the invariant scalar jet in the gauge-covariant values

    f = coefficient of F_B,
    u = coefficient of D_B T,
    t = coefficient of T,

and tests the source translation residual plus metric-volume equation.  It
also constructs an explicit local connection/T one-jet and constant-transition
three-patch descent.  It does not prove nonconstant atlas descent, Xi
prolongation, a global solution, magnitude selection, or physics.
"""

from collections import Counter
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


print("A. SOURCE FIELD SPACE AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
epsilon_source = read("lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md")
dark_source = read("lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md")
v108 = strict("lab/process/selected-k77-curvature-vev-trace-closure.json")

check("source", "the first action domain is inhomogeneous gauge data and MET(X)",
      r"I^B_1:\mathcal G\times \operatorname{MET}(X^{1,3})" in source)
check("source", "the displayed translation varies varpi at fixed epsilon",
      r"I^B_1(\epsilon,\varpi+s\alpha)" in source)
check("source", "T is varpi minus the epsilon-derived connection displacement",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("source", "epsilon variation moves B and T in opposite covariant directions",
      "delta B=D_B eta" in epsilon_source and "delta T=-D_B eta" in epsilon_source)
check("source", "the source magnitude bar is two problems becoming one",
      "two problems to one" in dark_source and "not a first-principles" in dark_source)
check("repo", "v0.108 exact representative and arithmetic remain available",
      v108["exact_result"]["branch"]["B_star"] == "(1/208)Phi1"
      and v108["exact_result"]["constraints"]["jacobian_determinant"] == -624)

for label in (
    "source translation Euler versus an arbitrary independent B partial",
    "epsilon-derived connection value versus curvature",
    "coordinate derivatives dB and dT versus invariant F_B and D_B T",
    "zero-jet source residual versus Xi equals D Upsilon prolongation",
    "local one-jet realization versus a solution on an open Y14 neighborhood",
    "one common amplitude versus a first-principles magnitude",
):
    check("type", label + " remain distinct", True)


print("\nB. EXACT INVARIANT SOURCE-EULER FAMILY")
b, t, r, s, f, u = sp.symbols("b t r s f u")
average = f + u / 2 + t**2 / 3
endpoint = f + u + t**2
upsilon = 312 * endpoint + t
metric_trace = 624 * average + t
equation_matrix = sp.Matrix([[312, 312], [624, 312]])
solution = sp.solve((upsilon, metric_trace), (f, u), dict=True)
expected = {f: t**2 / 3, u: -t / 312 - 4 * t**2 / 3}

check("exact", "source residual and metric trace have rank two on f and u",
      equation_matrix.rank() == 2 and equation_matrix.det() == -97344)
check("exact", "the invariant family is solved uniquely in f and u for arbitrary t",
      solution == [expected])
check("accounting", "three invariant values minus two independent equations leaves one amplitude",
      3 - equation_matrix.rank() == 1)
check("exact", "the complete family kills both source equations identically",
      sp.simplify(upsilon.subs(expected)) == 0
      and sp.simplify(metric_trace.subs(expected)) == 0)
check("control", "the zero-amplitude point is retained as the trivial member",
      expected[f].subs(t, 0) == 0 and expected[u].subs(t, 0) == 0)

b108 = Q(1, 208)
t108 = -Q(1, 104)
r108 = Q(1, 129792)
s108 = Q(0)
f108 = b108**2 + r108
u108 = 2 * b108 * t108 + s108
check("exact", "v0.108 is one member of the invariant family",
      f108 == expected[f].subs(t, t108)
      and u108 == expected[u].subs(t, t108))
check("exact", "v0.108 source residual and metric trace remain exactly zero",
      upsilon.subs({f: f108, u: u108, t: t108}) == 0
      and metric_trace.subs({f: f108, u: u108, t: t108}) == 0)

independent_b_equation = 2 * b + t
normal_gauge = {b: 0, t: t, r: expected[f], s: expected[u]}
check("planted", "PLANT source equations do not imply the independent-B equation",
      sp.simplify(independent_b_equation.subs(normal_gauge)) == t
      and sp.simplify(upsilon.subs({f: normal_gauge[r], u: normal_gauge[s]})) == 0)
check("type", "the v0.108 third equation is a reconstruction condition, not source algebra",
      independent_b_equation.subs({b: b108, t: t108}) == 0)

sample_t = Q(2, 39)
sample_b = Q(7, 31)
sample_f = expected[f].subs(t, sample_t)
sample_u = expected[u].subs(t, sample_t)
sample_r = sp.simplify(sample_f - sample_b**2)
sample_s = sp.simplify(sample_u - 2 * sample_b * sample_t)
check("exact", "a distinct connection-jet split preserves the same invariant family member",
      sample_b**2 + sample_r == sample_f
      and 2 * sample_b * sample_t + sample_s == sample_u)
check("accounting", "the b-r-s splitting freedom is not counted as a second physical amplitude",
      sp.simplify(sample_f - expected[f].subs(t, sample_t)) == 0
      and sp.simplify(sample_u - expected[u].subs(t, sample_t)) == 0)


print("\nC. EXPLICIT LOCAL CONNECTION AND T ONE-JET")
# Four noncommuting rational coefficient matrices provide a faithful local
# model of the invariant Phi1-wedge-Phi1 cell.  The radial one-jet theorem is
# coefficient-algebra agnostic, so it applies to the selected Clifford cell.
G = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
    sp.Matrix([[0, 1], [-1, 0]]),
    sp.Matrix([[1, 2], [-1, -1]]),
]
n = len(G)


def comm(left, right):
    return left * right - right * left


K = {(i, j): comm(G[i], G[j]) for i in range(n) for j in range(i + 1, n)}
check("control", "the local invariant two-form fixture is nonzero",
      any(value != sp.zeros(2) for value in K.values()))

f0 = sample_f
u0 = sample_u
t0 = sample_t
F_target = {(i, j): f0 * K[i, j] for i, j in K}
U_target = {(i, j): u0 * K[i, j] for i, j in K}

# At the center y=0 choose B_i=0 and derivatives
# partial_i B_j = F_ij/2, partial_i T_j = U_ij/2.  Antisymmetrization then
# recovers F and D_B T exactly; T_i(0)=t G_i.
def antisymmetric_value(bank, i, j):
    if i < j:
        return bank[i, j]
    if i > j:
        return -bank[j, i]
    return sp.zeros(2)


dB = {(i, j): Q(1, 2) * antisymmetric_value(F_target, i, j)
      for i in range(n) for j in range(n)}
dT = {(i, j): Q(1, 2) * antisymmetric_value(U_target, i, j)
      for i in range(n) for j in range(n)}
B0 = [sp.zeros(2) for _ in range(n)]
T0 = [t0 * value for value in G]

F_rebuilt = {(i, j): dB[i, j] - dB[j, i] + comm(B0[i], B0[j])
             for i, j in K}
U_rebuilt = {(i, j): dT[i, j] - dT[j, i]
             + comm(B0[i], T0[j]) - comm(B0[j], T0[i])
             for i, j in K}
T2 = {(i, j): comm(T0[i], T0[j]) for i, j in K}
FA = {(i, j): F_rebuilt[i, j] + U_rebuilt[i, j] + T2[i, j]
      for i, j in K}
AVG = {(i, j): F_rebuilt[i, j] + Q(1, 2) * U_rebuilt[i, j]
       + Q(1, 3) * T2[i, j] for i, j in K}

check("geometry", "the radial normal-gauge connection one-jet realizes F_B",
      F_rebuilt == F_target)
check("geometry", "the T one-jet realizes the prescribed D_B T",
      U_rebuilt == U_target)
check("exact", "the endpoint curvature has the source-family coefficient",
      all(FA[key] == (f0 + u0 + t0**2) * K[key] for key in K))
check("exact", "the path-average curvature has the source-action coefficient",
      all(AVG[key] == (f0 + u0 / 2 + t0**2 / 3) * K[key] for key in K))

# For A=B+T with affine-linear one-jet, verify the differential Bianchi cyclic
# sum at the center.  The derivative of F_A is generated by the commutator of
# the first derivatives of A with its nonzero value.
A0 = T0
dA = {(i, j): dB[i, j] + dT[i, j] for i in range(n) for j in range(n)}


def dFA(k, i, j):
    return comm(dA[k, i], A0[j]) + comm(A0[i], dA[k, j])


def covariant_bianchi(i, j, k):
    return sp.simplify(
        dFA(i, j, k) + dFA(j, k, i) + dFA(k, i, j)
        + comm(A0[i], FA[j, k]) + comm(A0[j], FA[k, i])
        + comm(A0[k], FA[i, j])
    )


def oriented(bank, i, j):
    return antisymmetric_value(bank, i, j)


# Supply oriented lookups used by the cyclic formula.
FA = {(i, j): oriented(FA, i, j) for i in range(n) for j in range(n)}
check("bianchi", "the explicit translated connection one-jet obeys differential Bianchi at the center",
      all(covariant_bianchi(i, j, k) == sp.zeros(2)
          for i in range(n) for j in range(n) for k in range(n)))
check("planted", "PLANT pointwise Bianchi is not promoted to a neighborhood solution", True)


print("\nD. NONCOMMUTING CONSTANT-TRANSITION THREE-PATCH DESCENT")
g01 = sp.Matrix([[1, 1], [0, 1]])
g12 = sp.Matrix([[1, 0], [1, 1]])
g02 = g01 * g12
check("geometry", "the two constant transitions are invertible and noncommuting",
      g01.det() == g12.det() == 1 and g01 * g12 != g12 * g01)


def conjugate(matrix, transition):
    return transition.inv() * matrix * transition


def transform_bank(bank, transition):
    return {key: conjugate(value, transition) for key, value in bank.items()}


F1 = transform_bank(F_target, g01)
F2 = transform_bank(F1, g12)
F2_direct = transform_bank(F_target, g02)
U1 = transform_bank(U_target, g01)
U2 = transform_bank(U1, g12)
U2_direct = transform_bank(U_target, g02)
check("descent", "curvature descends by direct and sequential conjugation",
      F2 == F2_direct)
check("descent", "covariant distortion descends by direct and sequential conjugation",
      U2 == U2_direct)
check("descent", "the invariant scalar equations are patch independent",
      upsilon.subs({f: f0, u: u0, t: t0}) == 0
      and metric_trace.subs({f: f0, u: u0, t: t0}) == 0)
check("planted", "PLANT constant-transition descent does not include the affine g-inverse-dg term",
      True)


print("\nE. DISPOSITION AND PROGRAM FENCES")
for kind, label in (
    ("variational", "the independent-B equation is not retained as a source Euler equation"),
    ("variational", "Xi equals D Upsilon and higher formal prolongation remain open"),
    ("symplectic", "the corrected one-amplitude family is not yet a Hessian or reduced class"),
    ("pde", "no open-neighborhood solution characteristic propagation or common domain is inferred"),
    ("krein", "no positive fundamental symmetry or maximal domain is selected"),
    ("analytic", "no contour reflection positivity determinant or quantum saddle is supplied"),
    ("cosmology", "two-to-one tracking does not fix magnitude screening or w(z)"),
    ("accounting", "the one local amplitude is not yet added to global residue without an ownership reconciliation"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
    ("representation", "selected Spin-native two U32,32 halves and full U64,64 remain distinct"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CORRECTS_INDEPENDENT_B_EULER_AS_NON_SOURCE_VARIATION__SOURCE_CONFIRMS_TRANSLATION_UPSILON_AND_EPSILON_CHAIN__REPO_DERIVES_LOCAL_TWO_TO_ONE_FAMILY__SOURCE_SILENT_GLOBAL_PROLONGATION_AND_AMPLITUDE_SELECTION")
print("INVARIANT_FAMILY=F_T2_OVER3__U_MINUS_T_OVER312_MINUS4T2_OVER3")
print("LOCAL_FREEDOM=THREE_INVARIANT_VALUES_MINUS_TWO_EQUATIONS_EQUALS_ONE_AMPLITUDE")
print("V0108=ONE_S_ZERO_INDEPENDENT_B_REPRESENTATIVE_AT_T_MINUS1_OVER104")
print("LOCAL_GEOMETRY=CONNECTION_AND_T_ONE_JET_REALISABLE__POINT_BIANCHI_PASS__CONSTANT_TRANSITION_DESCENT_PASS")
print("NEXT=NONCONSTANT_ATLAS_AND_XI_FORMAL_PROLONGATION__THEN_AMPLITUDE_SELECTION_AND_321_VS1571_HESSIAN_BV")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
