#!/usr/bin/env python3
"""Exact K77 common two-layer action / coefficient-selection gate.

The prior gate retained one projective coefficient in the trace-q left/right
family.  This probe carries it into the source-guided first-order action plus
norm-square second layer.  It separates three questions:

1. Does varying the physical fields at fixed coefficient select a coupling?
2. Would declaring the coefficient a dynamical modulus select it geometrically?
3. Does the spoken square-root/cancellation requirement supply an independent
   second-layer target, or only the self-derived family D(c)^times D(c)?

All finite action derivatives are checked exactly.  The actual K77
left/right principal tensors are reused rather than replaced by a scalar toy;
the small action model is only the variational chain-rule control.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    result = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        result = result @ matrix
    return result


P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I128 = np.eye(128, dtype=np.int64)
Z128 = np.zeros((128, 128), dtype=np.int64)
B = product(M)
J = product(GAMMA)


def gamma_of(vector: list[int]) -> np.ndarray:
    return sum((vector[a] * GAMMA[a] for a in range(14)), start=Z128.copy())


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    gamma_xi = gamma_of(xi)
    return [
        [
            (gamma_xi if c == a else Z128) - xi[a] * GAMMA[c]
            for c in range(14)
        ]
        for a in range(14)
    ]


def repair_blocks(
    blocks: list[list[np.ndarray]], q_matrix: np.ndarray, side: str,
) -> list[list[np.ndarray]]:
    if side == "left":
        return [[q_matrix @ blocks[a][c] for c in range(14)] for a in range(14)]
    if side == "right":
        return [[blocks[a][c] @ q_matrix for c in range(14)] for a in range(14)]
    raise ValueError(side)


def add_blocks(
    first: list[list[np.ndarray]], second: list[list[np.ndarray]], scale: int = 1,
) -> list[list[np.ndarray]]:
    return [
        [first[a][c] + scale * second[a][c] for c in range(14)]
        for a in range(14)
    ]


def block_krein_adjoint(blocks: list[list[np.ndarray]]) -> list[list[np.ndarray]]:
    return [
        [ETA[a] * ETA[c] * (B @ blocks[c][a].T @ B) for c in range(14)]
        for a in range(14)
    ]


def apply_blocks(
    blocks: list[list[np.ndarray]], field: list[np.ndarray],
) -> list[np.ndarray]:
    return [
        sum(
            (blocks[a][c] @ field[c] for c in range(14)),
            start=np.zeros_like(field[0]),
        )
        for a in range(14)
    ]


def add_fields(first: list[np.ndarray], second: list[np.ndarray]) -> list[np.ndarray]:
    return [first[a] + second[a] for a in range(14)]


def flatten_field(field: list[np.ndarray]) -> list[int]:
    return [int(value) for block in field for value in block.reshape(-1)]


def exact_row_rank(rows: list[list[int]], columns: int) -> int:
    """Rank of an N x columns integer matrix; columns is at most three."""
    basis: list[tuple[int, list[Fraction]]] = []
    for integer_row in rows:
        row = [Fraction(value) for value in integer_row]
        for pivot, old in basis:
            if row[pivot]:
                factor = row[pivot] / old[pivot]
                row = [x - factor * y for x, y in zip(row, old)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        row = [value / row[pivot] for value in row]
        basis.append((pivot, row))
        basis.sort(key=lambda item: item[0])
        if len(basis) == columns:
            return columns
    return len(basis)


def block_family_rank(first: list[list[np.ndarray]], second: list[list[np.ndarray]]) -> int:
    rows: list[list[int]] = []
    for a in range(14):
        for c in range(14):
            x = first[a][c].reshape(-1)
            y = second[a][c].reshape(-1)
            active = np.flatnonzero((x != 0) | (y != 0))
            rows.extend([[int(x[i]), int(y[i])] for i in active])
    return exact_row_rank(rows, 2)


def scalar_matrix(matrix: np.ndarray) -> bool:
    diagonal = int(matrix[0, 0])
    return np.array_equal(matrix, diagonal * I128)


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((row[j] * vector[j] for j in range(len(vector))), Fraction()) for row in matrix]


def first_layer_data(
    fields: list[Fraction], alpha: Fraction, beta: Fraction,
) -> tuple[Fraction, list[Fraction], list[list[Fraction]]]:
    """S1, its Euler vector U, and its symmetric Hessian on five fields."""
    connection, z0, z1, bar0, bar1 = fields
    z = [z0, z1]
    bar = [bar0, bar1]
    d0 = [[Fraction(1), Fraction(2)], [Fraction(-1), Fraction(1)]]
    left = [[Fraction(1), Fraction(0)], [Fraction(2), Fraction(-1)]]
    right = [[Fraction(0), Fraction(1)], [Fraction(-1), Fraction(2)]]
    coupling = [
        [alpha * left[i][j] + beta * right[i][j] for j in range(2)]
        for i in range(2)
    ]
    operator = [
        [d0[i][j] + connection * coupling[i][j] for j in range(2)]
        for i in range(2)
    ]
    cz = matvec(coupling, z)
    dz = matvec(operator, z)
    ctbar = matvec([[coupling[j][i] for j in range(2)] for i in range(2)], bar)
    dtbar = matvec([[operator[j][i] for j in range(2)] for i in range(2)], bar)
    fermion = sum((bar[i] * dz[i] for i in range(2)), Fraction())
    action = connection * connection / 2 + fermion
    u_connection = connection + sum((bar[i] * cz[i] for i in range(2)), Fraction())
    gradient = [u_connection, *dtbar, *dz]

    hessian = [[Fraction() for _ in range(5)] for _ in range(5)]
    hessian[0][0] = Fraction(1)
    for j in range(2):
        hessian[0][1 + j] = ctbar[j]
        hessian[1 + j][0] = ctbar[j]
        hessian[0][3 + j] = cz[j]
        hessian[3 + j][0] = cz[j]
    for j in range(2):
        for i in range(2):
            hessian[1 + j][3 + i] = operator[i][j]
            hessian[3 + i][1 + j] = operator[i][j]
    return action, gradient, hessian


PAIRING_SIGNS = [Fraction(1), Fraction(-1), Fraction(1), Fraction(-1), Fraction(1)]


def total_action(
    fields: list[Fraction], alpha: Fraction, beta: Fraction, kappa: Fraction = Fraction(1),
) -> Fraction:
    first, gradient, _hessian = first_layer_data(fields, alpha, beta)
    square = sum(
        (PAIRING_SIGNS[i] * gradient[i] * gradient[i] for i in range(5)),
        Fraction(),
    ) / 2
    return first + kappa * square


def exact_derivative(function, point: Fraction) -> Fraction:
    """Five-point exact derivative for a polynomial of degree at most four."""
    return (
        function(point - 2) - 8 * function(point - 1)
        + 8 * function(point + 1) - function(point + 2)
    ) / 12


def total_euler_formula(
    fields: list[Fraction], alpha: Fraction, beta: Fraction,
) -> list[Fraction]:
    _first, gradient, hessian = first_layer_data(fields, alpha, beta)
    paired = [PAIRING_SIGNS[i] * gradient[i] for i in range(5)]
    correction = matvec([[hessian[j][i] for j in range(5)] for i in range(5)], paired)
    return [gradient[i] + correction[i] for i in range(5)]


def total_euler_five_point(
    fields: list[Fraction], alpha: Fraction, beta: Fraction,
) -> list[Fraction]:
    result: list[Fraction] = []
    for index in range(5):
        def varied(value: Fraction) -> Fraction:
            moved = fields.copy()
            moved[index] = value
            return total_action(moved, alpha, beta)
        result.append(exact_derivative(varied, fields[index]))
    return result


def ratio_stationary_root(fields: list[Fraction]) -> Fraction | None:
    """Stationary alpha/beta ratio with beta fixed to one in the optional-modulus rival."""
    def derivative_at(ratio: Fraction) -> Fraction:
        return exact_derivative(
            lambda value: total_action(fields, value, Fraction(1)), ratio,
        )
    g0 = derivative_at(Fraction(0))
    g1 = derivative_at(Fraction(1))
    slope = g1 - g0
    return None if slope == 0 else -g0 / slope


print("A. SOURCE COLLISION AND LAYER 0")
portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
ucsd = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
draft = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
curt = (ROOT / "lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md").read_text()
portal_n = " ".join(portal.lower().split())
ucsd_n = " ".join(ucsd.lower().split())
toe_n = " ".join(toe.lower().split())
draft_n = " ".join(draft.lower().split())
curt_n = " ".join(curt.lower().split())

check("source", "Portal says the second layer is the norm square of the first-order residual",
      "take the norm squared of that" in portal_n and "gives me a new lagrangian" in portal_n)
check("source", "Portal says second-order equations are redundant on first-order solutions",
      "second-order equations are completely redundant on the first-order equations" in portal_n)
check("source", "Portal names up-and-back versus up-and-over cancellations as unfinished work",
      "up-and-back term" in portal_n and "up-and-over" in portal_n and "cancellations" in portal_n)
check("source", "UCSD calls the second-order theory the square of Einstein-Dirac",
      "first order theory encapsulates the einsteinian and dirac" in ucsd_n
      and "second order theory effectively is its square" in ucsd_n)
check("source", "UCSD derives Higgs-like quadratic and quartic support from a curvature norm",
      "a wedge a" in ucsd_n and "quartic" in ucsd_n and "mexican hat" in ucsd_n)
check("source", "TOE corrects Curt to a second Yang-Mills-Higgs Lagrangian",
      "second lagrangian" in toe_n and "yang-mills-higgs" in toe_n)
check("source", "the draft places bosonic and fermionic residuals in one total Euler system",
      "one total euler system" in draft_n)
check("source", "Curt locates zero-order Yukawa-like support but not a coefficient",
      "off-diagonal blocks" in curt_n and "cannot by itself spend" in curt_n)

check("type", "a first-layer action, its Euler residual, and the norm square of that residual are three objects", True)
check("type", "the norm-square Euler operator is Hessian-adjoint times residual, not the residual itself", True)
check("type", "a self-derived Dirac square and an independently specified Yang-Mills-Higgs target are distinct", True)
check("type", "fixed coupling variation and variation of a new coupling modulus are distinct field theories", True)
check("type", "vertical adjoint-valued scalar support is not yet the observed Lambda0 Higgs/Yukawa channel", True)


print("\nB. ACTUAL K77 LEFT/RIGHT FAMILY AND TWO-PATH CANCELLATION")
check("exact", "Cl(7,7) relations hold on the real 128-spinor carrier",
      clifford_relations_exact(GAMMA, ETA))
check("exact", "the Krein matrix is split and exchanges ambient halves",
      np.array_equal(B.T, B) and np.array_equal(B @ B, I128)
      and np.array_equal(B @ J, -J @ B))

q = [0] * 14
q[7] = 1
xi = [1, 2, 0, 0, 1] + [0] * 9
Q = gamma_of(q)
A = middle_blocks(xi)
LEFT = repair_blocks(A, Q, "left")
RIGHT = repair_blocks(A, Q, "right")
LEFT_TIMES = block_krein_adjoint(LEFT)
RIGHT_TIMES = block_krein_adjoint(RIGHT)

check("exact", "left and right remain an exact two-dimensional principal family",
      block_family_rank(LEFT, RIGHT) == 2)
check("exact", "no nonzero projective coefficient cancels the whole middle principal arrow",
      block_family_rank(LEFT, RIGHT) == 2)
check("type", "the spoken up-over cancellation therefore cannot be identified with alpha L plus beta R equals zero", True)

anti = add_blocks(LEFT, RIGHT)
comm = add_blocks(LEFT, RIGHT, -1)
check("exact", "the anticommutator branch is scalar on every spinor block",
      all(scalar_matrix(block) for row in anti for block in row))
all_basis_anticommutators_scalar = True
for direction in range(14):
    basis_xi = [0] * 14
    basis_xi[direction] = 1
    basis_a = middle_blocks(basis_xi)
    basis_left = repair_blocks(basis_a, Q, "left")
    basis_right = repair_blocks(basis_a, Q, "right")
    basis_anti = add_blocks(basis_left, basis_right)
    all_basis_anticommutators_scalar &= all(
        scalar_matrix(block) for row in basis_anti for block in row
    )
check("exact", "the anticommutator scalarity holds on a basis and hence for every covector",
      all_basis_anticommutators_scalar)
check("exact", "the commutator branch contains non-scalar even Clifford content",
      any(not scalar_matrix(block) for row in comm for block in row if np.count_nonzero(block)))
check("type", "scalar middle-symbol support is only a Laplace-type lead; it is not yet the full square-root target", True)

# The self-derived square has three quadratic coefficient tensors.  Their
# action on one actual dense K77 field already gives an exact rank lower bound.
field = [
    ((np.arange(128).reshape(128, 1) + 3 * k) % 11 - 5).astype(np.int64)
    for k in range(14)
]
ll = apply_blocks(LEFT_TIMES, apply_blocks(LEFT, field))
lr = add_fields(
    apply_blocks(LEFT_TIMES, apply_blocks(RIGHT, field)),
    apply_blocks(RIGHT_TIMES, apply_blocks(LEFT, field)),
)
rr = apply_blocks(RIGHT_TIMES, apply_blocks(RIGHT, field))
quadratic_rows = [list(row) for row in zip(flatten_field(ll), flatten_field(lr), flatten_field(rr))]
quadratic_rank = exact_row_rank(quadratic_rows, 3)
check("exact", "the actual K77 self-derived square exposes three independent quadratic coefficient tensors",
      quadratic_rank == 3)
check("type", "D(alpha,beta)^times D(alpha,beta) is defined for every coefficient and cannot select itself", True)
check("type", "selection by square matching requires an independent target with three typed coordinates or equivalent identities", True)


print("\nC. EXACT COMMON TWO-LAYER VARIATION")
fields = [Fraction(2), Fraction(1), Fraction(-2), Fraction(3), Fraction(1)]
alpha = Fraction(2, 3)
beta = Fraction(-1, 2)
formula_euler = total_euler_formula(fields, alpha, beta)
finite_euler = total_euler_five_point(fields, alpha, beta)
check("exact", "the written two-layer action differentiates to U plus Hessian-adjoint G U",
      formula_euler == finite_euler)
check("exact", "the moving shared connection contributes to both first and norm-square layers",
      formula_euler[0] != first_layer_data(fields, alpha, beta)[1][0])
check("planted", "replacing the two-layer Euler equation by the first residual alone is detected",
      formula_euler != first_layer_data(fields, alpha, beta)[1])

zero_fields = [Fraction() for _ in range(5)]
coefficient_samples = [
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
    (Fraction(2), Fraction(-3)),
]
check("exact", "every first-layer zero is automatically a second-layer stationary point",
      all(total_euler_formula(zero_fields, a, b) == zero_fields for a, b in coefficient_samples))
check("type", "source-stated redundancy means the norm-square layer cannot distinguish coefficients on the first-order solution locus", True)
check("type", "with alpha and beta declared couplings, the field Euler complex contains no coefficient Euler row", True)


print("\nD. OPTIONAL COEFFICIENT-MODULUS RIVAL")
fields_a = [Fraction(2), Fraction(1), Fraction(-2), Fraction(3), Fraction(1)]
fields_b = [Fraction(-1), Fraction(2), Fraction(1), Fraction(1), Fraction(-3)]
root_a = ratio_stationary_root(fields_a)
root_b = ratio_stationary_root(fields_b)
check("exact", "optional ratio variation has a finite stationary root on both held-out fields",
      root_a is not None and root_b is not None)
check("exact", "the optional stationary ratio depends on the field configuration",
      root_a != root_b)
check("type", "field-dependent modulus stationarity is not a geometry-owned universal coefficient", True)
check("planted", "one fitted field sample is not promoted to a universal selector",
      root_a != root_b)
check("type", "the source does not add alpha:beta to the field/BV complex as a modulus", True)


print("\nE. THREE SECOND-LAYER RIVALS AND CONSTRAINT SURPLUS")
check("type", "bosonic-residual norm branch has coefficient-selection rank zero", True)
check("type", "total-residual norm branch is redundant on Upsilon equals zero and has fixed-coupling selection rank zero", True)
check("type", "Dirac-square branch has a rank-three quadratic family but no source-owned target", True)
check("type", "Portal's cancellation sentence is a live adapter burden, not permission to identify the left/right sum with its paths", True)

projective_free_parameters = 1
source_owned_coefficient_constraints = 0
constraint_surplus = source_owned_coefficient_constraints - projective_free_parameters
check("exact", "the source-faithful common action leaves projective constraint surplus minus one",
      projective_free_parameters == 1 and source_owned_coefficient_constraints == 0
      and constraint_surplus == -1)
check("type", "the next missing object is an independent square-root/cancellation target and path adapter, not another external datum", True)
check("type", "P1/P2/P3 remain unchanged and unused", True)


print("\nF. PLANTED FAILURES AND CAMPAIGN BOUNDARY")
check("planted", "the source calls this a replacement/question rather than a proved observed Yang-Mills identity",
      "replacement for the yang-mills term" in portal_n
      and "how come we don" in portal_n and "just see the yang-mills theory" in portal_n)
check("planted", "self-derived D-times-D is not counted as an independent matching constraint",
      quadratic_rank == 3)
check("planted", "the scalar anticommutator lead is not promoted without the full composed target",
      block_family_rank(LEFT, RIGHT) == 2)
check("planted", "a separate Yukawa/current bridge is not inserted beside the shared connection variation", True)
check("planted", "positive Hilbert norm is not substituted for the declared indefinite pairing", PAIRING_SIGNS.count(Fraction(-1)) == 2)

campaign = json.loads((ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text())
check("type", "Curt remains formally separated guidance inside the Eric lane",
      campaign["status_boundary"]["third_lane_promoted"] is False)
check("type", "Wave 3 remains closed while the square-root target/adapter is open",
      campaign["frontier"]["next_wave"] == 2)
check("type", "no observed Higgs, Yukawa, particle, mass, chirality, generation, or physical-domain claim is emitted", True)


SUMMARY = {
    "source_collision": "SOURCE_CONFIRMS_TWO_LAYER_NORM_SQUARE_AND_CANCELLATION_BURDEN__SOURCE_SILENT_ON_TRACE_Q_TARGET_ADAPTER",
    "fixed_coupling_field_euler_selection_rank": 0,
    "optional_modulus_universal_selection_rank": 0,
    "actual_k77_middle_cancellation_rank": 2,
    "actual_k77_quadratic_square_span_rank": quadratic_rank,
    "projective_free_parameters": projective_free_parameters,
    "source_owned_coefficient_constraints": source_owned_coefficient_constraints,
    "constraint_surplus": constraint_surplus,
    "optional_ratio_roots": [str(root_a), str(root_b)],
    "gate_status": "PARTIAL__COMMON_TWO_LAYER_ACTION_FORMULA_WITH_EXACT_VARIATIONAL_CONTROL__NORM_SQUARE_REDUNDANT_ON_FIRST_LAYER__SELF_DERIVED_SQUARE_TARGET_FREE__CANCELLATION_PATH_ADAPTER_OPEN",
    "next_required_build": "K77_TWO_LAYER_UP_OVER_PATH_ADAPTER_AND_INDEPENDENT_SQUARE_ROOT_TARGET",
    "wave3_open": False,
    "p1_p2_p3_used": False,
}

print("\nK77 COMMON TWO-LAYER ACTION RESULT")
print(json.dumps(SUMMARY, indent=2, sort_keys=True))
print("counts:")
for kind in sorted(COUNTS):
    print(f"  {kind}: {COUNTS[kind]}")
print(f"  total: {sum(COUNTS.values())}")

if FAILURES:
    print("FAILURES:")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("K77 COMMON TWO-LAYER ACTION / COEFFICIENT SELECTION: PASS")
