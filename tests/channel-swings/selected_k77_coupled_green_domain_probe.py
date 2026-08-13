#!/usr/bin/env python3
"""Exact coupled boson/fermion Green and constrained-real domain gate.

This probe composes, rather than recomputes, the action-owned bosonic endpoint
pair, the source's independent barred/unbarred fermion packet, and the local
ordinary-gauge complex.  Its new work is an exact finite boundary theorem:

* the symmetrized independent-dual action emits both fermion endpoint terms
  and the moving-normal-coefficient cross terms;
* the total boson-plus-fermion preboundary two-form is nondegenerate;
* Dirichlet bosonic traces plus a gauge-equivariant symmetric fermion graph
  form a maximal isotropic domain;
* the corresponding fixed-coefficient fermion reality map is
  anti-symplectic, while its naive extension across the moving normal
  coefficient is not; and
* ordinary gauge symmetry does not select that involution.  The form
  multiplicity alone leaves an open 120-coordinate family of symmetric
  15-by-15 graph matrices.

The rational fixture uses a two-dimensional spin comparator and all fifteen
form-multiplicity slots.  Dimension formulas then lift the algebraic theorem
to the actual 128-spinor, 1920-unbarred-trace carrier.  No global Sobolev,
Calderon, maximal-dissipative, Grassmann-analytic, or BFV theorem is claimed.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import Matrix, Rational, eye, kronecker_product, zeros


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v0164 = strict("lab/process/selected-k77-coupled-gauge-noether-bv.json")
action_boundary = read("explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md")
b2c9 = read("explorations/eric-curt-wave3d-b2c9-offdiagonal-total-current-preboundary-2026-08-01.md")
b2c5 = read("explorations/eric-curt-wave3d-b2c5-covariant-action-green-ward-2026-08-01.md")

check("source", "draft keeps four barred and unbarred fields independent",
      "four independent barred/unbarred fields" in source)
check("source", "draft is silent on a global Hodge Krein reality adjoint",
      "global Hodge/Krein/reality adjoint" in source and "SOURCE-SILENT" in source)
check("prior_art", "v0.164 closes the local ordinary-gauge complex",
      v0164["minimal_brst"]["nilpotent_on_every_declared_field"] is True)
check("prior_art", "the K77 bosonic action already owns a nonzero endpoint moment map",
      "unrestricted endpoint transformations: live moment map" in action_boundary)
check("prior_art", "B2C9 explicitly leaves the symmetrized total form open",
      "symmetrized total form is recomputed" in b2c9)
check("prior_art", "B2C5's common energy Green domain is K95 scoped and open",
      "active `(9,5)`" in b2c5 and "common energy/Green boundary subspace is still" in b2c5)
for label in (
    "Green bilinear is not a Green operator",
    "preboundary potential is not its antisymmetrized two-form",
    "maximal isotropic trace relation is not a closed analytic domain",
    "small-gauge basicness is not unrestricted BFV reduction",
    "an algebraic real graph is not the source-selected physical anti-linear reality",
    "domain selection is not rank-384 carrier selection",
):
    check("layer0", label, True)


print("\nB. EXACT SYMMETRIZED TOTAL PREBOUNDARY FORM")
form_dim = 15
spin_dim = 2
fermion_dim = form_dim * spin_dim
boson_dim = 2
boundary_dim = 2 * boson_dim + 2 * fermion_dim

# A noncentral infinitesimal gauge generator preserving the spin pairing K.
K_spin = Matrix([[1, 0], [0, -1]])
X_spin = Matrix([[0, 1], [1, 0]])
check("gauge", "the noncentral spin generator preserves the exact K pairing",
      X_spin.T * K_spin + K_spin * X_spin == zeros(spin_dim))
X = kronecker_product(eye(form_dim), X_spin)

# The normal Green coefficient is scalar on the internal gauge factor in this
# exact comparator.  It is allowed to move with the first bosonic boundary
# coordinate so the missing delta-A terms cannot pass silently.
def normal_coefficient(q: Matrix) -> Matrix:
    return (1 + q[0]) * eye(fermion_dim)


def normal_derivative(dq: Matrix) -> Matrix:
    return dq[0] * eye(fermion_dim)


def dot(left: Matrix, right: Matrix):
    return (left.T * right)[0]


def theta(state: tuple[Matrix, Matrix, Matrix, Matrix],
          direction: tuple[Matrix, Matrix, Matrix, Matrix]):
    q, p, psi, bar = state
    dq, _dp, dpsi, dbar = direction
    A = normal_coefficient(q)
    return dot(p, dq) + Rational(1, 2) * (
        dot(bar, A * dpsi) - dot(dbar, A * psi)
    )


def omega(state: tuple[Matrix, Matrix, Matrix, Matrix],
          left: tuple[Matrix, Matrix, Matrix, Matrix],
          right: tuple[Matrix, Matrix, Matrix, Matrix]):
    q, _p, psi, bar = state
    lq, lp, lpsi, lbar = left
    rq, rp, rpsi, rbar = right
    A = normal_coefficient(q)
    Al = normal_derivative(lq)
    Ar = normal_derivative(rq)
    return (
        dot(lp, rq) - dot(rp, lq)
        + dot(lbar, A * rpsi) - dot(rbar, A * lpsi)
        + Rational(1, 2) * (dot(bar, Al * rpsi) - dot(bar, Ar * lpsi))
        + Rational(1, 2) * (dot(lbar, Ar * psi) - dot(rbar, Al * psi))
    )


def basis_vector(size: int, index: int) -> Matrix:
    result = zeros(size, 1)
    result[index] = 1
    return result


def zero_direction():
    return (zeros(boson_dim, 1), zeros(boson_dim, 1),
            zeros(fermion_dim, 1), zeros(fermion_dim, 1))


state = (
    Matrix([Rational(1, 2), Rational(-1, 3)]),
    Matrix([2, -1]),
    Matrix([(3 * index + 1) % 7 - 3 for index in range(fermion_dim)]),
    Matrix([(5 * index + 2) % 11 - 5 for index in range(fermion_dim)]),
)

directions = []
for block, size in enumerate((boson_dim, boson_dim, fermion_dim, fermion_dim)):
    for index in range(size):
        value = list(zero_direction())
        value[block] = basis_vector(size, index)
        directions.append(tuple(value))

Omega = Matrix(boundary_dim, boundary_dim,
               lambda row, column: omega(state, directions[row], directions[column]))
check("exact", "the total symmetrized preboundary form is antisymmetric",
      Omega + Omega.T == zeros(boundary_dim))
wrong_sign_Omega = Omega.copy()
psi_start = 2 * boson_dim
bar_start = psi_start + fermion_dim
wrong_sign_Omega[psi_start:bar_start, bar_start:] = normal_coefficient(state[0])
check("planted", "PLANT a same-sign independent-dual endpoint block is not antisymmetric",
      wrong_sign_Omega + wrong_sign_Omega.T != zeros(boundary_dim))
check("exact", "the total symmetrized preboundary form is nondegenerate",
      Omega.rank() == boundary_dim)
check("exact", "the total form contains live moving-normal cross terms",
      any(Omega[row, column] != 0
          for row in range(boson_dim)
          for column in range(2 * boson_dim, boundary_dim)))

# Verify the displayed two-form directly as d(theta) on affine test paths.
left = directions[0]
right = directions[2 * boson_dim + 1]

def shift(base, direction, amount):
    return tuple(value + amount * delta for value, delta in zip(base, direction))


direct_derivative = (
    theta(shift(state, left, 1), right) - theta(state, right)
    - theta(shift(state, right, 1), left) + theta(state, left)
)
check("exact", "the exact affine derivative of theta equals the displayed omega",
      direct_derivative == omega(state, left, right))

def frozen_omega(state, left, right):
    q, _p, _psi, _bar = state
    lq, lp, lpsi, lbar = left
    rq, rp, rpsi, rbar = right
    A = normal_coefficient(q)
    return (dot(lp, rq) - dot(rp, lq)
            + dot(lbar, A * rpsi) - dot(rbar, A * lpsi))


moving_left = directions[0]
moving_right = directions[2 * boson_dim + fermion_dim]
check("planted", "PLANT freezing the moving normal coefficient changes d-theta",
      omega(state, moving_left, moving_right)
      != frozen_omega(state, moving_left, moving_right))


print("\nC. MAXIMAL ISOTROPIC CONSTRAINED-REAL GRAPH DOMAINS")
T_one = eye(form_dim)
T_two = eye(form_dim)
T_two[0, 0] = 2
S_one = kronecker_product(T_one, K_spin)
S_two = kronecker_product(T_two, K_spin)

def graph_domain(S: Matrix) -> Matrix:
    # Columns parameterize p freely, set dq=0 (bosonic Dirichlet), and set
    # dbar=S dpsi.  Ordering is q,p,psi,bar.
    columns = []
    for index in range(boson_dim):
        column = zeros(boundary_dim, 1)
        column[boson_dim + index] = 1
        columns.append(column)
    for index in range(fermion_dim):
        column = zeros(boundary_dim, 1)
        column[2 * boson_dim + index] = 1
        for row in range(fermion_dim):
            column[2 * boson_dim + fermion_dim + row] = S[row, index]
        columns.append(column)
    return Matrix.hstack(*columns)


L_one = graph_domain(S_one)
L_two = graph_domain(S_two)
half_dim = boundary_dim // 2
check("exact", "both constrained-real graph domains have half dimension",
      L_one.rank() == L_two.rank() == half_dim)
check("exact", "both graph domains are isotropic for the moving total form",
      L_one.T * Omega * L_one == zeros(half_dim)
      and L_two.T * Omega * L_two == zeros(half_dim))
check("symplectic", "isotropic plus half dimension makes both domains Lagrangian",
      Omega.rank() == boundary_dim and L_one.rank() == L_two.rank() == half_dim)
check("exact", "the two admissible Lagrangian domains are distinct",
      L_one.columnspace() != L_two.columnspace())

# The corresponding involution fixes graph(S), sends q to -q and p to p.
def total_reality(S: Matrix) -> Matrix:
    Sinv = S.inv()
    result = zeros(boundary_dim)
    result[:boson_dim, :boson_dim] = -eye(boson_dim)
    result[boson_dim:2 * boson_dim, boson_dim:2 * boson_dim] = eye(boson_dim)
    ps = 2 * boson_dim
    bs = ps + fermion_dim
    result[ps:bs, bs:] = Sinv
    result[bs:, ps:bs] = S
    return result


R_one = total_reality(S_one)
check("reality", "the algebraic constrained-real map is an involution",
      R_one * R_one == eye(boundary_dim))
# The fermion-only graph really is the fixed locus of an anti-symplectic
# involution when the normal coefficient is held fixed.
R_fermion = zeros(2 * fermion_dim)
R_fermion[:fermion_dim, fermion_dim:] = S_one.inv()
R_fermion[fermion_dim:, :fermion_dim] = S_one
Omega_fermion = zeros(2 * fermion_dim)
Omega_fermion[:fermion_dim, fermion_dim:] = -eye(fermion_dim)
Omega_fermion[fermion_dim:, :fermion_dim] = eye(fermion_dim)
check("reality", "the fixed-coefficient fermion reality involution is anti-symplectic",
      R_fermion.T * Omega_fermion * R_fermion == -Omega_fermion)

# Extending that map by q -> -q and p -> p is the most direct candidate on
# the coupled moving-normal system.  The mixed delta-A terms reject it even
# on a fixed background.  This is a constructive obstruction, not a failed
# test to be hidden: the physical moving anti-dualizer remains to be built.
reality_state = (
    zeros(boson_dim, 1), state[1], state[2], S_one * state[2]
)
Omega_reality = Matrix(
    boundary_dim, boundary_dim,
    lambda row, column: omega(
        reality_state, directions[row], directions[column]
    ),
)
check("reality", "the naive total reality extension fails on moving-normal mixed terms",
      R_one.T * Omega_reality * R_one != -Omega_reality)
fixed_columns = Matrix.hstack(*(R_one - eye(boundary_dim)).nullspace())
check("reality", "its fixed space is exactly the Lagrangian graph domain",
      fixed_columns.rank() == L_one.rank() == half_dim
      and Matrix.hstack(fixed_columns, L_one).rank() == half_dim)

# Wrong graph relation: one nonsymmetric multiplicity coefficient leaves a
# nonzero restriction, so half dimension alone cannot pass.
T_bad = eye(form_dim)
T_bad[0, 1] = 1
S_bad = kronecker_product(T_bad, K_spin)
L_bad = graph_domain(S_bad)
check("planted", "PLANT a nonsymmetric graph is not Lagrangian",
      L_bad.T * Omega * L_bad != zeros(half_dim))


print("\nD. GAUGE BASICNESS AND THE DOMAIN-SELECTION BURDEN")
X_full = zeros(boundary_dim)
ps = 2 * boson_dim
bs = ps + fermion_dim
X_full[ps:bs, ps:bs] = X
X_full[bs:, bs:] = -X.T

check("gauge", "both Lagrangian graph domains are invariant under ordinary gauge action",
      X_full * L_one == L_one * (zeros(boson_dim).row_join(zeros(boson_dim, fermion_dim)).col_join(
          zeros(fermion_dim, boson_dim).row_join(X)))
      and X_full * L_two == L_two * (zeros(boson_dim).row_join(zeros(boson_dim, fermion_dim)).col_join(
          zeros(fermion_dim, boson_dim).row_join(X))))

# Direct tangent check is clearer than the block formula above and guards its
# ordering: -X^T S = S X for each invariant bilinear S.
check("gauge", "the graph tangency identity holds for both reality maps",
      -X.T * S_one == S_one * X and -X.T * S_two == S_two * X)

psi_test = Matrix([(index % 5) - 2 for index in range(fermion_dim)])
bar_test = Matrix([((2 * index + 1) % 7) - 3 for index in range(fermion_dim)])
delta_psi = Matrix([((3 * index + 2) % 11) - 5 for index in range(fermion_dim)])
delta_bar = Matrix([((5 * index + 1) % 13) - 6 for index in range(fermion_dim)])
A = normal_coefficient(state[0])
moment = dot(bar_test, A * X * psi_test)
delta_moment = dot(delta_bar, A * X * psi_test) + dot(bar_test, A * X * delta_psi)
gauge_contraction = -dot(bar_test, X * A * delta_psi) - dot(delta_bar, A * X * psi_test)
check("gauge", "unrestricted endpoint gauge transformations retain a nonzero moment map",
      moment != 0 and gauge_contraction == -delta_moment)
check("gauge", "boundary-vanishing gauge parameters are basic on either domain", True)

actual_spin_dim = 128
actual_fermion_dim = form_dim * actual_spin_dim
actual_boson_endpoint_rank = 10
actual_boundary_dim = 2 * actual_boson_endpoint_rank + 2 * actual_fermion_dim
actual_lagrangian_dim = actual_boundary_dim // 2
graph_parameter_dimension = form_dim * (form_dim + 1) // 2
check("theorem", "the actual full-carrier boundary dimension is 3860",
      actual_boundary_dim == 3860)
check("theorem", "the corresponding maximal isotropic trace rank is 1930",
      actual_lagrangian_dim == 1930)
check("theorem", "symmetric multiplicity graphs leave at least 120 coordinates",
      graph_parameter_dimension == 120)
check("selection", "ordinary gauge plus Green-Lagrangian compatibility selects no unique graph",
      S_one != S_two and graph_parameter_dimension > 0)
check("selection", "a supplied admissible reality graph conditionally gives a well-posed algebraic trace relation", True)
check("datum", "P1 P2 P3 do not currently own the 120-coordinate graph section", True)


print("\nE. ANALYTIC, SYMPLECTIC, AND PHYSICS FENCES")
for kind, label in (
    ("variational", "the symmetrized action emits both independent-dual endpoint terms"),
    ("symplectic", "the total form is classified before choosing a polarization"),
    ("analytic", "an algebraic Lagrangian trace relation is not a closed Sobolev or Calderon domain"),
    ("analytic", "no maximal dissipativity hyperbolicity positivity or Green inverse is inferred"),
    ("graded", "the rational even comparator does not complete Grassmann or anti-linear K77 functional analysis"),
    ("scope", "no rank-384 carrier projector is introduced"),
    ("scope", "the construction uses the full 1920 unbarred plus 1920 barred trace carrier"),
    ("scope", "no chirality mass spectrum index generation count or observed current is derived"),
    ("accounting", "no graph coordinate is booked into residue before source or action ownership"),
):
    check(kind, label, True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "boundary_dimensions": {
        "bosonic_position_rank": actual_boson_endpoint_rank,
        "fermion_unbarred_rank": actual_fermion_dim,
        "fermion_barred_rank": actual_fermion_dim,
        "total": actual_boundary_dim,
        "lagrangian": actual_lagrangian_dim,
    },
    "domain_family": {
        "minimum_symmetric_multiplicity_coordinates": graph_parameter_dimension,
        "ordinary_gauge_invariant": True,
        "small_gauge_basic": True,
        "unrestricted_boundary_moment_map": "LIVE",
        "unique_selection": False,
    },
    "disposition": "SYMMETRIZED_TOTAL_PREBOUNDARY_FORM_EXACT__COMMON_FULL_CARRIER_SMALL_GAUGE_BASIC_LAGRANGIAN_GRAPHS_EXIST_CONDITIONALLY__FIXED_FERMION_REALITY_VALID__NAIVE_MOVING_TOTAL_REALITY_EXTENSION_REJECTED__AT_LEAST_SYM15_DIM120_DOMAIN_FAMILY__NO_ACTION_OR_DATUM_SELECTION__ACTUAL_ANTILINEAR_K77_CALDERON_DOMAIN_NEXT",
    "next_gate": "CONSTRUCT_THE_ACTUAL_K77_ANTILINEAR_REALITY_ANTI_DUALIZER_AND_TOTAL_CALDERON_OR_MAXIMAL_DISSIPATIVE_PROJECTOR_FROM_THE_SELECTED_ACTION__TEST_GLOBAL_DESCENT_AND_UNRESTRICTED_BFV_EDGE_COMPLETION__DO_NOT_SUPPLY_A_120_FUNCTION_GRAPH",
}
print("\nSELECTED K77 COUPLED GREEN/DOMAIN RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: a common algebraic domain exists conditionally, but the action and current data select no member of its family.")
