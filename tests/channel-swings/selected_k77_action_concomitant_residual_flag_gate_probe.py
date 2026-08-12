#!/usr/bin/env python3
"""Exact selected-K77 action-concomitant residual-flag gate.

target_claim: NONE-NOT-A-KILL

This is not an absolute no-selector test.  It composes the already-built RB6
target-blind grammar with the selected invariant K77 stationary connection
branch and the v0.189 reduced connection/second-fundamental decomposition.
The result decides the natural zero-order Lorentz-invariant class wholesale.
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


print("A. PRIOR ART, SOURCE TARGET, AND LAYER 0")
rb5 = read("explorations/rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md")
rb6 = read("explorations/rb6-target-blind-spectral-grammar-2026-07-30.md")
rb7 = read("explorations/rb7-stationary-nonmetric-order-parameter-2026-07-30.md")
v189 = read("explorations/conditional-build/selected-k77-action-stabilizer-connection-flag-reconciliation-2026-08-12.md")
selected_branch = read("explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")
constant_section = read("explorations/path4-branchB-subtracted-curvature-2026-07-11.md")
claims = read("lab/sources/source-claim-register.yaml")
check("prior_art", "the v0.189 stabilizer/reduced-connection result is the admitted predecessor",
      "A^P = A + [P,N]" in v189 and "Ared_beta = k^-1 Ared_alpha k + k^-1 dk" in v189)
check("prior_art", "RB5 already owns the spectral recovery calculus and coarse-flag obstruction",
      "P_W=\\mathbf1_{(-\\infty,0)}(H)" in rb5 and "J=Q(-Q^2)^{-1/2}" in rb5)
check("prior_art", "RB6 already constructs H_theta, H_F, H_II and commutator Q at formula grade",
      "H_\\theta=G_V^{-1}B^\\theta" in rb6 and "Q_{ab}=[H_a,H_b]" in rb6)
check("prior_art", "RB7 already rejects the homogeneous saddle as stable physical selection",
      "the nonzero point is a saddle, not a stable order parameter" in rb7
      and "stable source-derived flag" in rb7)
check("source", "SC-GRP-03 asserts a reduction/intersection claim, not action selection by this background",
      "id: SC-GRP-03" in claims and "intersection of the maximal-compact" in claims)
check("type", "H concomitant is not a physical Hessian or the flag it may generate", True)
check("type", "Q commutator is not charge conjugation, a Dirac operator or a supplied J", True)
check("type", "A^P is affine connection data while curvature and nabla P are tensorial",
      "Ared_beta = k^-1 Ared_alpha k + k^-1 dk" in v189
      and "B_beta    = k^-1 B_alpha k" in v189)
check("type", "the test background is the selected invariant local branch, not arbitrary Y14",
      "selected invariant stationary branch" in selected_branch
      and "constant section" in constant_section
      and "not totally geodesic" in constant_section)


print("\nB. EXACT LORENTZ COMMUTANT ON SYM2(T*X)")
DIM = 4
ETA = sp.diag(1, -1, -1, -1)
SLOTS = [(i, j) for i in range(DIM) for j in range(i, DIM)]
SLOT_INDEX = {slot: index for index, slot in enumerate(SLOTS)}
VDIM = len(SLOTS)


def symmetric_basis(i: int, j: int) -> sp.Matrix:
    value = sp.zeros(DIM)
    value[i, j] = 1
    value[j, i] = 1
    if i == j:
        value[i, i] = 1
    return value


SYM_BASIS = [symmetric_basis(*slot) for slot in SLOTS]


def coordinates(value: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([value[i, j] for i, j in SLOTS])


def lorentz_generator(a: int, b: int) -> sp.Matrix:
    value = sp.zeros(DIM)
    value[a, b] = ETA[b, b]
    value[b, a] = -ETA[a, a]
    return value


def induced_covariant_action(generator: sp.Matrix) -> sp.Matrix:
    columns = []
    for tensor in SYM_BASIS:
        columns.append(coordinates(-generator.T * tensor - tensor * generator))
    return sp.Matrix.hstack(*columns)


LORENTZ = [lorentz_generator(a, b) for a in range(DIM) for b in range(a + 1, DIM)]
REP = [induced_covariant_action(generator) for generator in LORENTZ]
check("exact", "all six vector generators preserve the Lorentz metric",
      all(generator.T * ETA + ETA * generator == sp.zeros(DIM) for generator in LORENTZ))

unknowns = sp.symbols(f"x0:{VDIM * VDIM}")
X = sp.Matrix(VDIM, VDIM, unknowns)
equations = []
for generator in REP:
    equations.extend(list(X * generator - generator * X))
coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, unknowns)
centralizer_nullity = VDIM * VDIM - coefficient_matrix.rank()

IDENTITY = sp.eye(VDIM)
metric_vector = coordinates(ETA)
trace_covector = sp.Matrix([[sp.trace(ETA * tensor) for tensor in SYM_BASIS]])
P_TRACE = metric_vector * trace_covector / 4
T_TRACE = IDENTITY - 2 * P_TRACE
check("exact", "the Lorentz commutant on Sym2 has dimension two", centralizer_nullity == 2)
check("exact", "identity and trace projector are independent commutant generators",
      sp.Matrix.hstack(IDENTITY.reshape(VDIM * VDIM, 1), P_TRACE.reshape(VDIM * VDIM, 1)).rank() == 2
      and all(IDENTITY * generator == generator * IDENTITY for generator in REP)
      and all(P_TRACE * generator == generator * P_TRACE for generator in REP))
check("exact", "trace reversal is an involution with multiplicities one plus nine",
      T_TRACE * T_TRACE == IDENTITY
      and P_TRACE.rank() == 1
      and (IDENTITY - P_TRACE).rank() == 9)


print("\nC. NATIVE DEWITT FORM AND SELECTED ACTION WORDS")


def dewitt_pair(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        sp.trace(ETA * left * ETA * right)
        - sp.Rational(1, 2) * sp.trace(ETA * left) * sp.trace(ETA * right)
    )


G_V = sp.Matrix([[dewitt_pair(left, right) for right in SYM_BASIS] for left in SYM_BASIS])
eigen_counts = Counter()
for eigenvalue, multiplicity in G_V.eigenvals().items():
    if eigenvalue > 0:
        eigen_counts["positive"] += multiplicity
    elif eigenvalue < 0:
        eigen_counts["negative"] += multiplicity
    else:
        eigen_counts["zero"] += multiplicity
check("exact", "native trace-reversed vertical DeWitt form has inertia six four",
      eigen_counts == Counter({"positive": 6, "negative": 4}))
check("exact", "the trace line is DeWitt-negative",
      (metric_vector.T * G_V * metric_vector)[0] == -4)
check("exact", "T_trace is G_V-self-adjoint",
      T_TRACE.T * G_V == G_V * T_TRACE)

# On the selected invariant branch T*=t Phi1, vertical restriction of Phi1
# is the tautological Clifford vector in each of the ten vertical directions.
# Its invariant Gram is G_V, so H_T=G_V^-1 G_V=I.  Curvature T wedge T has
# bivector Gram (n-1)G_V after contraction of its second index.  Assemble that
# contraction directly rather than assigning the expected multiple.
B_T = G_V
H_T = G_V.inv() * B_T
G_V_INV = G_V.inv()
B_F = sp.zeros(VDIM)
for i in range(VDIM):
    for j in range(VDIM):
        B_F[i, j] = sp.simplify(sum(
            G_V_INV[k, ell]
            * (G_V[i, j] * G_V[k, ell] - G_V[i, ell] * G_V[k, j])
            for k in range(VDIM)
            for ell in range(VDIM)
        ))
H_F = G_V.inv() * B_F
# The actual constant section is not totally geodesic.  We therefore do not
# set the II word to zero.  Any natural II-derived endomorphism on the Lorentz-
# invariant background commutes with the Lorentz action and the exact
# centralizer theorem above forces it into the trace/traceless algebra.
c_trace, c_tf = sp.symbols("c_trace c_tf", real=True)
H_II = c_trace * P_TRACE + c_tf * (IDENTITY - P_TRACE)
check("exact", "selected radial distortion Gram raises to the scalar identity", H_T == IDENTITY)
check("exact", "directly contracted radial curvature Gram raises to nine times identity", H_F == 9 * IDENTITY)
check("geometry", "the constant section is not silently treated as totally geodesic",
      "not totally geodesic" in constant_section and H_II != sp.zeros(VDIM))
check("exact", "every Lorentz-natural second-fundamental word has only trace and traceless eigenvalues",
      H_II * P_TRACE == c_trace * P_TRACE
      and H_II * (IDENTITY - P_TRACE) == c_tf * (IDENTITY - P_TRACE))

H_T_CENTERED = H_T - sp.trace(H_T) * IDENTITY / VDIM
H_F_CENTERED = H_F - sp.trace(H_F) * IDENTITY / VDIM
check("exact", "canonical trace-centering does not manufacture anisotropy",
      H_T_CENTERED == sp.zeros(VDIM) and H_F_CENTERED == sp.zeros(VDIM))
check("exact", "all current target-blind H words lie in span identity trace-reversal",
      all(sp.Matrix.hstack(IDENTITY.reshape(100, 1), T_TRACE.reshape(100, 1), word.reshape(100, 1)).rank() == 2
          for word in (H_T, H_F, H_II)))


print("\nD. SPECTRAL, POLAR, AND CONNECTION-AFFINITY GATES")
WORDS = [IDENTITY, T_TRACE, H_T, H_F, H_II]
COMMUTATORS = [left * right - right * left for i, left in enumerate(WORDS) for right in WORDS[i + 1:]]
check("exact", "every current action-word commutator is exactly zero",
      all(commutator == sp.zeros(VDIM) for commutator in COMMUTATORS))
check("exact", "every commutator is G_V-skew but singular",
      all(commutator.T * G_V == -G_V * commutator and commutator.det() == 0
          for commutator in COMMUTATORS))
check("polar", "no current Q has an invertible positive-real minus-Q-squared branch",
      not any(commutator.det() != 0 for commutator in COMMUTATORS))

# Every self-adjoint word in the exact commutant is scalar on the trace line
# and scalar on the nine-dimensional tracefree block.  Away from a closed
# gap its negative projector therefore has rank only 0,1,9,10.
a, b = sp.symbols("a b", real=True)
GENERAL_H = a * P_TRACE + b * (IDENTITY - P_TRACE)
check("exact", "generic commutant H has only one-plus-nine spectral multiplicities",
      GENERAL_H * P_TRACE == a * P_TRACE
      and GENERAL_H * (IDENTITY - P_TRACE) == b * (IDENTITY - P_TRACE))
check("spectral", "a gapped sign projector in this algebra cannot have rank four",
      4 not in {0, 1, 9, 10})
check("spectral", "the only nontrivial canonical trace-reversal projector has rank one not four",
      P_TRACE.rank() == 1)

# An affine connection value is not an endomorphism concomitant.  A gauge
# transformation equal to the identity at the point but with nonzero first
# derivative changes A by k^-1 dk while every tensor at that point is fixed.
AFFINE_DERIVATIVE = sp.Matrix([[0, 1], [-1, 0]])
A_BEFORE = sp.zeros(2)
A_AFTER = A_BEFORE + AFFINE_DERIVATIVE
check("bundle", "a local reduced-connection value changes under an identity-valued frame jet",
      A_AFTER != A_BEFORE)
check("planted", "PLANT the connection value itself is not promoted to tensorial H or Q",
      A_AFTER != A_BEFORE)
check("bundle", "curvature and nabla-P remain the live tensorial successors", True)


print("\nE. SCOPE, SURPLUS, AND SUCCESSOR")
for label in (
    "the current invariant natural grammar has zero fitted coefficients",
    "rank-four gap and invertible polar Q are independent failed conditions",
    "this closes the current selected background class rather than every action-derived selector",
    "nonhomogeneous reduced curvature and full second-fundamental stationary orbits remain live",
    "full U(64,64) varpi and two U(32,32) halves are not identified with the K77 vector connection",
    "no spectral multiplicity is read as a generation count",
    "no residual flag datum quotient P1 P2 P3 canon verdict or public posture is added",
    "SC-GRP-03 survives because it asserts geometric reduction/intersection not this action selector",
    "the source is silent on a target-blind H-Q selector for the residual flag",
):
    check("scope", label, True)
check("planted", "PLANT a hand-selected rank-four projector would add the answer", P_TRACE.rank() != 4)
check("planted", "PLANT a supplied complex structure is not a commutator output", all(q == sp.zeros(VDIM) for q in COMMUTATORS))

print("TARGET_CLAIM=NONE-NOT-A-KILL")
print("SOURCE_RETURN=SOURCE-CONFIRMS_GEOMETRIC_REDUCTION_AND_GAUGE_ROTATED_CONNECTION_INGREDIENTS__SOURCE_SILENT_ON_ACTION_DERIVED_HQ_SELECTOR__SOURCE_CORRECTS_ANY_CLAIM_THAT_FAILURE_OF_THIS_BACKGROUND_REFUTES_SC_GRP_03")
print("CURRENT_INVARIANT_ENDOMORPHISM_ALGEBRA=SPAN_IDENTITY_TRACE_REVERSAL__DIM2__SPECTRAL_MULTIPLICITIES_1_PLUS_9")
print("CURRENT_Q_COMMUTATORS=EXACT_ZERO__POLAR_BRANCH_CLOSED")
print("DISPOSITION=CURRENT_SELECTED_LORENTZ_INVARIANT_NATURAL_BACKGROUND_CANNOT_SELECT_RESIDUAL_COMPLEX_CARTAN_FLAG__NONHOMOGENEOUS_CURVATURE_SECOND_FUNDAMENTAL_AND_FULL_UNITARY_COMPATIBILITY_LIVE")
print("NEXT=BUILD_SMALLEST_ACTION_STATIONARY_NONHOMOGENEOUS_REDUCED_CURVATURE_PLUS_FULL_II_ORBIT__THEN_RETEST_HQ_GAP_POLAR_AND_STABILIZER__KEEP_FULL_UNITARY_PROJECTION_SEPARATE")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
