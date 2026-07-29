#!/usr/bin/env python3
r"""Actual-fibre start for the C_perp / B5 naturality question.

This probe keeps four objects separate:

1. the generator loop h_t = B_t^T eta B_t in the Lorentzian metric fibre;
2. its ACTUAL induced frame on TX + Sym^2 T*X with the DeWitt metric;
3. a reference Clifford lift, which transports K, J_obs, J_H, chirality, and
   the RS4/RS10 algebraic projectors; and
4. an extension of that return to the 20 normalized B5 provenance slots.

The first three are computable from existing repository data.  The fourth is
not selected by the support ledger: a mirror-compatible commutant sign family
survives.  A planted noncentral member is accepted by a deliberately
permissive support matcher and rejected by a strict centrality test.

This is a deterministic, small-matrix, numpy-only exploration certificate.
It builds no differential, Green form, domain, physical index, or source
action.  Exit 0 means the scoped controls passed; the printed verdict remains
OPEN at the named associated-bundle map.
"""
from __future__ import annotations

from itertools import product as cartesian_product
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_observer_symbol_multiplicity_matrix as b5_matrix  # noqa: E402


TOL = 1.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    rows = sum(block.shape[0] for block in blocks)
    cols = sum(block.shape[1] for block in blocks)
    out = np.zeros((rows, cols), dtype=np.result_type(*blocks))
    row = 0
    col = 0
    for block in blocks:
        out[row : row + block.shape[0], col : col + block.shape[1]] = block
        row += block.shape[0]
        col += block.shape[1]
    return out


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


# =============================================================================
# A. The actual TX + Sym^2 T*X DeWitt carrier
# =============================================================================

ETA4_MATRIX = np.diag([1.0, 1.0, 1.0, -1.0])
PAIRS = [(left, right) for left in range(4) for right in range(left, 4)]
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
N_FIBRE = len(PAIRS)


def symmetric_matrix(components: np.ndarray) -> np.ndarray:
    matrix = np.zeros((4, 4))
    for component, (left, right) in zip(components, PAIRS):
        matrix[left, right] = component
        matrix[right, left] = component
    return matrix


def symmetric_components(matrix: np.ndarray) -> np.ndarray:
    return np.array([matrix[left, right] for left, right in PAIRS])


SYMMETRIC_BASIS = [
    symmetric_matrix(np.eye(N_FIBRE)[index]) for index in range(N_FIBRE)
]


def dewitt_metric(metric: np.ndarray) -> np.ndarray:
    r"""The repository's trace-reversed DeWitt form on Sym^2 T*X."""
    inverse = np.linalg.inv(metric)
    actions = [inverse @ basis for basis in SYMMETRIC_BASIS]
    gram = np.zeros((N_FIBRE, N_FIBRE))
    for left in range(N_FIBRE):
        for right in range(N_FIBRE):
            gram[left, right] = (
                np.trace(actions[left] @ actions[right])
                - 0.5 * np.trace(actions[left]) * np.trace(actions[right])
            )
    return gram


def gimmel_metric(metric: np.ndarray) -> np.ndarray:
    return block_diag(metric, dewitt_metric(metric))


def mixed_rotation(angle: float, positive_leg: int = 0) -> np.ndarray:
    """Ordinary rotation in one spatial and the timelike coordinate."""
    rotation = np.eye(4)
    cosine = np.cos(angle)
    sine = np.sin(angle)
    timelike_leg = 3
    rotation[positive_leg, positive_leg] = cosine
    rotation[timelike_leg, timelike_leg] = cosine
    rotation[positive_leg, timelike_leg] = -sine
    rotation[timelike_leg, positive_leg] = sine
    return rotation


def induced_sym2_frame(change: np.ndarray) -> np.ndarray:
    r"""Columns encode E -> change^T E change on covariant two-tensors."""
    columns = [
        symmetric_components(change.T @ basis @ change)
        for basis in SYMMETRIC_BASIS
    ]
    return np.column_stack(columns)


def diagonal_components(values: list[float]) -> np.ndarray:
    components = np.zeros(N_FIBRE)
    for index, value in enumerate(values):
        components[PAIR_INDEX[(index, index)]] = value
    return components


def pair_component(pair: tuple[int, int], scale: float) -> np.ndarray:
    components = np.zeros(N_FIBRE)
    components[PAIR_INDEX[pair]] = scale
    return components


# An explicit DeWitt-orthonormal frame.  The diagonal block is
# I - (1/2) eta eta^T: three eta-orthogonal positive vectors and eta/2
# as its one negative vector.  Off-diagonal E_ab has norm 2 eta_a eta_b.
DIAGONAL_POSITIVE = [
    diagonal_components([1.0, -1.0, 0.0, 0.0]) / np.sqrt(2.0),
    diagonal_components([1.0, 1.0, -2.0, 0.0]) / np.sqrt(6.0),
    diagonal_components([1.0, 1.0, 1.0, 3.0]) / np.sqrt(12.0),
]
SPATIAL_OFF_DIAGONAL = [
    pair_component(pair, 1.0 / np.sqrt(2.0))
    for pair in ((0, 1), (0, 2), (1, 2))
]
DIAGONAL_NEGATIVE = [diagonal_components([0.5, 0.5, 0.5, -0.5])]
TIMELIKE_OFF_DIAGONAL = [
    pair_component(pair, 1.0 / np.sqrt(2.0))
    for pair in ((0, 3), (1, 3), (2, 3))
]
DEWITT_FRAME = np.column_stack(
    DIAGONAL_POSITIVE
    + SPATIAL_OFF_DIAGONAL
    + DIAGONAL_NEGATIVE
    + TIMELIKE_OFF_DIAGONAL
)
ETA10_MATRIX = np.diag([1.0] * 6 + [-1.0] * 4)
REFERENCE_FRAME = block_diag(np.eye(4), DEWITT_FRAME)
REFERENCE_METRIC = block_diag(ETA4_MATRIX, ETA10_MATRIX)


def actual_frame_data(
    parameter: float, positive_leg: int = 0, turns: int = 1
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    change = mixed_rotation(turns * np.pi * parameter, positive_leg)
    metric = change.T @ ETA4_MATRIX @ change
    induced = induced_sym2_frame(change)
    coordinate_frame = block_diag(np.linalg.inv(change), induced)
    orthonormal_frame = coordinate_frame @ REFERENCE_FRAME
    return change, metric, induced, orthonormal_frame


print("=" * 92)
print("A. ACTUAL TX + Sym^2 T*X DeWitt lift")
print("=" * 92)

dewitt_reference_error = max_abs(
    DEWITT_FRAME.T @ dewitt_metric(ETA4_MATRIX) @ DEWITT_FRAME
    - ETA10_MATRIX
)
check(
    "explicit Sym^2 frame has DeWitt signature (6,4)",
    dewitt_reference_error < TOL,
    f"orthonormality defect {dewitt_reference_error:.2e}",
)

frame_errors: list[float] = []
signatures: list[tuple[int, int]] = []
for parameter in np.linspace(0.0, 1.0, 17):
    _change, metric, _induced, frame = actual_frame_data(parameter)
    gimmel = gimmel_metric(metric)
    frame_errors.append(max_abs(frame.T @ gimmel @ frame - REFERENCE_METRIC))
    eigenvalues = np.linalg.eigvalsh(gimmel)
    signatures.append(
        (
            int(np.sum(eigenvalues > TOL)),
            int(np.sum(eigenvalues < -TOL)),
        )
    )
check(
    "E -> B_t^T E B_t is the actual DeWitt-isometric Sym^2 frame along the loop",
    max(frame_errors) < TOL,
    f"max frame defect {max(frame_errors):.2e}",
)
check(
    "the actual gimmel carrier stays signature (9,5)",
    all(signature == (9, 5) for signature in signatures),
)

_change_mid, metric_mid, _induced_mid, _frame_mid = actual_frame_data(0.25)
bad_coordinate_frame = block_diag(
    np.linalg.inv(_change_mid), np.eye(N_FIBRE)
)
bad_frame = bad_coordinate_frame @ REFERENCE_FRAME
bad_sym2_defect = max_abs(
    bad_frame.T @ gimmel_metric(metric_mid) @ bad_frame - REFERENCE_METRIC
)
check(
    "planted trivial-Sym^2 lift fails the DeWitt frame equation",
    bad_sym2_defect > 1.0e-3,
    f"defect {bad_sym2_defect:.2e}",
)

_change_end, metric_end, sym2_end, frame_end = actual_frame_data(1.0)
closed_defect = max_abs(metric_end - ETA4_MATRIX)
return_map = np.linalg.inv(REFERENCE_FRAME) @ frame_end
return_map[np.abs(return_map) < 1.0e-12] = 0.0
return_isometry_defect = max_abs(
    return_map.T @ REFERENCE_METRIC @ return_map - REFERENCE_METRIC
)
check(
    "the metric loop closes and its full 14-frame return lies in O(3,1) x O(6,4)",
    closed_defect < TOL and return_isometry_defect < TOL,
    f"closure {closed_defect:.2e}, isometry {return_isometry_defect:.2e}",
)

sym2_eigenvalues = np.linalg.eigvalsh(sym2_end)
check(
    "the actual Sym^2 endpoint is nontrivial with exactly four reversed tensor legs",
    int(np.sum(sym2_eigenvalues < -0.5)) == 4
    and int(np.sum(sym2_eigenvalues > 0.5)) == 6,
)

positive_indices = np.flatnonzero(np.diag(REFERENCE_METRIC) > 0)
negative_indices = np.flatnonzero(np.diag(REFERENCE_METRIC) < 0)
positive_return = return_map[np.ix_(positive_indices, positive_indices)]
negative_return = return_map[np.ix_(negative_indices, negative_indices)]
positive_determinant = float(np.linalg.det(positive_return))
negative_determinant = float(np.linalg.det(negative_return))
positive_reversals = int(
    np.sum(np.linalg.eigvalsh(positive_return) < -0.5)
)
negative_reversals = int(
    np.sum(np.linalg.eigvalsh(negative_return) < -0.5)
)
check(
    "endpoint reverses three positive and three negative gimmel legs",
    positive_reversals == 3 and negative_reversals == 3,
    f"reversals (+,-)=({positive_reversals},{negative_reversals})",
)
check(
    "Krein positive-volume line has monodromy -1 on the actual carrier",
    positive_determinant < -1.0 + TOL,
    f"det(H_+)={positive_determinant:+.0f}, det(H_-)={negative_determinant:+.0f}",
)

_change_double, metric_double, _sym2_double, frame_double = actual_frame_data(
    1.0, turns=2
)
double_return = np.linalg.inv(REFERENCE_FRAME) @ frame_double
double_positive = double_return[np.ix_(positive_indices, positive_indices)]
check(
    "doubled loop closes the full frame and has Krein-line monodromy +1",
    max_abs(metric_double - ETA4_MATRIX) < TOL
    and max_abs(double_return - np.eye(14)) < TOL
    and float(np.linalg.det(double_positive)) > 1.0 - TOL,
)


# =============================================================================
# B. Reference Clifford lift: K, J_obs, J_H, chirality, and both RS projectors
# =============================================================================


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for factor in factors:
        out = np.kron(out, factor)
    return out


def euclidean_jw_gammas(n_pairs: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    gammas: list[np.ndarray] = []
    for index in range(n_pairs):
        left = [sigma_3] * index
        right = [identity] * (n_pairs - 1 - index)
        gammas.append(kron_all(left + [sigma_1] + right))
        gammas.append(kron_all(left + [sigma_2] + right))
    return gammas


def signed_gammas(
    positive: int, negative: int
) -> tuple[list[np.ndarray], np.ndarray]:
    euclidean = euclidean_jw_gammas((positive + negative) // 2)
    metric = np.array([1.0] * positive + [-1.0] * negative)
    gammas = [
        gamma if metric[index] > 0 else 1j * gamma
        for index, gamma in enumerate(euclidean)
    ]
    return gammas, metric


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    chirality = matrix_product(gammas)
    square = complex(np.trace(chirality @ chirality) / chirality.shape[0])
    if abs(square - 1.0) < TOL:
        return chirality
    if abs(square + 1.0) < TOL:
        return 1j * chirality
    raise AssertionError("chirality square is not scalar +/-1")


def commuting_real_structure(gammas: list[np.ndarray]) -> np.ndarray:
    """Unitary part of an antilinear Clifford real/quaternionic structure."""
    real_gammas = [
        gamma
        for gamma in gammas
        if max_abs(gamma.conj() - gamma) < TOL
    ]
    unitary_part = matrix_product(real_gammas)
    norm_square = unitary_part @ unitary_part.conj().T
    scale = float(np.max(np.abs(np.diag(norm_square))))
    return unitary_part / np.sqrt(scale)


def returned_antilinear(
    unitary_part: np.ndarray, linear_lift: np.ndarray
) -> np.ndarray:
    """Unitary part of L (U o conjugation) L^-1."""
    return (
        linear_lift
        @ unitary_part
        @ np.linalg.inv(linear_lift.conj())
    )


def gamma_trace_projector(
    gammas: list[np.ndarray], metric: np.ndarray
) -> np.ndarray:
    vector_dimension = len(gammas)
    spinor_dimension = gammas[0].shape[0]
    gamma_trace = np.hstack(gammas)
    injection = (
        np.vstack(
            [
                metric[index] * gammas[index]
                for index in range(vector_dimension)
            ]
        )
        / vector_dimension
    )
    return (
        np.eye(vector_dimension * spinor_dimension, dtype=complex)
        - injection @ gamma_trace
    )


def diagonalize_return(block: np.ndarray) -> np.ndarray:
    diagonal = np.where(np.diag(block).real < 0.0, -1.0, 1.0)
    rounded = np.diag(diagonal)
    if max_abs(block - rounded) >= TOL:
        raise AssertionError("return block is not diagonal +/-1 in the chosen frame")
    return rounded


def spin_lift(
    orthogonal_return: np.ndarray, gammas: list[np.ndarray]
) -> tuple[np.ndarray, list[int]]:
    flipped = [
        index
        for index, sign in enumerate(np.diag(orthogonal_return))
        if sign < 0
    ]
    if not flipped:
        return np.eye(gammas[0].shape[0], dtype=complex), flipped
    return matrix_product([gammas[index] for index in flipped]), flipped


def adjoint_action_error(
    linear_lift: np.ndarray,
    gammas: list[np.ndarray],
    orthogonal_return: np.ndarray,
) -> float:
    inverse = np.linalg.inv(linear_lift)
    return max(
        max_abs(
            linear_lift @ gamma @ inverse
            - orthogonal_return[index, index] * gamma
        )
        for index, gamma in enumerate(gammas)
    )


print("\n" + "=" * 92)
print("B. REFERENCE CLIFFORD LIFT (not yet the missing 20-slot connection)")
print("=" * 92)

return_4 = diagonalize_return(return_map[:4, :4])
return_10 = diagonalize_return(return_map[4:, 4:])
gammas_4, eta_4 = signed_gammas(3, 1)
gammas_10, eta_10 = signed_gammas(6, 4)
lift_4, flipped_4 = spin_lift(return_4, gammas_4)
lift_10, flipped_10 = spin_lift(return_10, gammas_10)
lift_14 = np.kron(lift_4, lift_10)

lift_error_4 = adjoint_action_error(lift_4, gammas_4, return_4)
lift_error_10 = adjoint_action_error(lift_10, gammas_10, return_10)
check(
    "reference Clifford lifts cover the computed base and Sym^2 returns",
    lift_error_4 < TOL and lift_error_10 < TOL,
    f"Ad defects 4D={lift_error_4:.2e}, 10D={lift_error_10:.2e}",
)
check(
    "actual endpoint lift reverses 2 base and 4 DeWitt legs",
    len(flipped_4) == 2 and len(flipped_10) == 4,
    f"flipped sets {flipped_4}, {flipped_10}",
)

chirality_4 = normalized_chirality(gammas_4)
chirality_10 = normalized_chirality(gammas_10)
check(
    "reference frame return preserves base and internal chirality separately",
    max_abs(
        lift_4 @ chirality_4 @ np.linalg.inv(lift_4) - chirality_4
    )
    < TOL
    and max_abs(
        lift_10 @ chirality_10 @ np.linalg.inv(lift_10) - chirality_10
    )
    < TOL,
)

projector_4 = gamma_trace_projector(gammas_4, eta_4)
projector_10 = gamma_trace_projector(gammas_10, eta_10)
rs_return_4 = np.kron(return_4, lift_4)
rs_return_10 = np.kron(return_10, lift_10)
projector_return_error_4 = max_abs(
    rs_return_4 @ projector_4 @ np.linalg.inv(rs_return_4) - projector_4
)
projector_return_error_10 = max_abs(
    rs_return_10 @ projector_10 @ np.linalg.inv(rs_return_10)
    - projector_10
)
check(
    "reference lift preserves both gamma-traceless RS projectors",
    projector_return_error_4 < TOL and projector_return_error_10 < TOL,
    (
        f"RS4 defect {projector_return_error_4:.2e}, "
        f"RS10 defect {projector_return_error_10:.2e}"
    ),
)
check(
    "RS projector ranks remain 12 and 288",
    int(round(np.trace(projector_4).real)) == 12
    and int(round(np.trace(projector_10).real)) == 288,
)

observer_real_4 = commuting_real_structure(gammas_4)
observer_real_10 = commuting_real_structure(gammas_10)
observer_reality = np.kron(observer_real_4, observer_real_10)

# Factorized Cl(9,5) gammas are needed only to type J_H independently of
# J_obs.  J_obs^2=+1; the GU quaternionic J_H has square -1.
identity_4_spinor = np.eye(gammas_4[0].shape[0], dtype=complex)
identity_10_spinor = np.eye(gammas_10[0].shape[0], dtype=complex)
factorized_gammas_14 = [
    np.kron(gamma, identity_10_spinor) for gamma in gammas_4
] + [
    np.kron(chirality_4, gamma) for gamma in gammas_10
]
quaternionic_reality = commuting_real_structure(factorized_gammas_14)
identity_128 = np.eye(128, dtype=complex)
check(
    "Layer-0 type split: J_obs^2=+1 while J_H^2=-1",
    max_abs(
        observer_reality @ observer_reality.conj() - identity_128
    )
    < TOL
    and max_abs(
        quaternionic_reality @ quaternionic_reality.conj() + identity_128
    )
    < TOL,
)

observer_return = returned_antilinear(observer_reality, lift_14)
quaternionic_return = returned_antilinear(quaternionic_reality, lift_14)
check(
    "the reference lift returns both J_obs and J_H exactly",
    max_abs(observer_return - observer_reality) < TOL
    and max_abs(quaternionic_return - quaternionic_reality) < TOL,
)

krein_4 = matrix_product(
    [gamma for gamma, sign in zip(gammas_4, eta_4) if sign > 0]
)
krein_10 = matrix_product(
    [gamma for gamma, sign in zip(gammas_10, eta_10) if sign > 0]
)
krein = np.kron(krein_4, krein_10)
krein_return = lift_14 @ krein @ np.linalg.inv(lift_14)
check(
    "reference Clifford transport realizes the actual Krein-line sign K1=-K0",
    max_abs(krein_return + krein) < TOL,
)

# C_perp is K J_obs, not K J_H.  Store only the unitary part of each
# antilinear map.  For A o conjugation, C0^-1 C1 has linear matrix
# conjugate(A0)^-1 conjugate(A1).
cperp_0 = krein @ observer_reality
cperp_1 = krein_return @ observer_return
cperp_mismatch = (
    np.linalg.inv(cperp_0.conj()) @ cperp_1.conj()
)
cperp_scalar = complex(np.trace(cperp_mismatch) / cperp_mismatch.shape[0])
cperp_centrality_defect = max_abs(
    cperp_mismatch - cperp_scalar * identity_128
)
check(
    "on the reference irreducible spinor lift, C0^-1 C1 is the central scalar -1",
    abs(cperp_scalar + 1.0) < TOL and cperp_centrality_defect < TOL,
    (
        f"scalar {cperp_scalar.real:+.0f}, "
        f"centrality defect {cperp_centrality_defect:.2e}"
    ),
)


# =============================================================================
# C. All 20 B5 slots: support preservation does not normalize their returns
# =============================================================================


def b5_cells() -> set[tuple[str, str]]:
    return {
        (source.name, target.name)
        for source in b5_matrix.SLOTS
        for target in b5_matrix.SLOTS
        if b5_matrix.symbol_multiplicity(
            b5_matrix.TYPES[source.h_type],
            b5_matrix.TYPES[target.h_type],
        )
    }


def mirror_cell(cell: tuple[str, str]) -> tuple[str, str]:
    source, target = cell
    return (
        b5_matrix.SLOT_BY_NAME[source].mirror,
        b5_matrix.SLOT_BY_NAME[target].mirror,
    )


def phase_extension(
    pair_signs: tuple[int, ...],
    mirror_pairs: list[tuple[str, str]],
) -> dict[str, int]:
    phases: dict[str, int] = {}
    for sign, pair in zip(pair_signs, mirror_pairs):
        for slot_name in pair:
            phases[slot_name] = sign
    return phases


def permissive_support_matcher(
    phases: dict[str, int],
    cells: set[tuple[str, str]],
) -> bool:
    """Deliberately insufficient: support, mirror, dimension, provenance only."""
    if set(phases) != set(b5_matrix.SLOT_BY_NAME):
        return False
    for slot in b5_matrix.SLOTS:
        mirror = b5_matrix.SLOT_BY_NAME[slot.mirror]
        if slot.dimension != mirror.dimension:
            return False
        if phases[slot.name] != phases[slot.mirror]:
            return False
    for source, target in cells:
        factor = phases[target] / phases[source]
        mirror_source, mirror_target = mirror_cell((source, target))
        mirror_factor = phases[mirror_target] / phases[mirror_source]
        if factor == 0 or factor != mirror_factor:
            return False
        if (mirror_source, mirror_target) not in cells:
            return False
    return True


def is_central_slot_return(phases: dict[str, int]) -> bool:
    return len(set(phases.values())) == 1


print("\n" + "=" * 92)
print("C. ALL 20 B5 PROVENANCE SLOTS: CENTRALITY IS NOT SUPPORT DATA")
print("=" * 92)

slots = b5_matrix.SLOTS
slot_names = {slot.name for slot in slots}
mirror_pairs = sorted(
    {
        tuple(sorted((slot.name, slot.mirror)))
        for slot in slots
    }
)
cells = b5_cells()
special_directed = {
    cell
    for cell in cells
    if (cell[1], cell[0]) == mirror_cell(cell)
}
special_edges = {
    tuple(sorted(cell)) for cell in special_directed
}
check(
    "complete B5 ledger has 20 slots, 10 mirror pairs, 136 cells, and 10 special edges",
    len(slot_names) == 20
    and len(mirror_pairs) == 10
    and len(cells) == 136
    and len(special_edges) == 10,
)

all_sign_extensions = [
    phase_extension(signs, mirror_pairs)
    for signs in cartesian_product((-1, 1), repeat=len(mirror_pairs))
]
permissive_count = sum(
    permissive_support_matcher(extension, cells)
    for extension in all_sign_extensions
)
central_count = sum(is_central_slot_return(extension) for extension in all_sign_extensions)
check(
    "support/mirror constraints admit all 2^10 pair-sign extensions",
    permissive_count == 2**10,
    f"admitted {permissive_count}",
)
check(
    "only two of those extensions are central; modulo global sign, 2^9 relative classes remain",
    central_count == 2,
    f"central {central_count}, relative classes {2**9}",
)

uniform_central = phase_extension(
    tuple([-1] * len(mirror_pairs)), mirror_pairs
)
planted_noncentral = dict(uniform_central)
for slot_name in mirror_pairs[0]:
    planted_noncentral[slot_name] = 1
check(
    "uniform -1 extension matches the reference spinor central return",
    permissive_support_matcher(uniform_central, cells)
    and is_central_slot_return(uniform_central),
)
check(
    "planted noncentral lift passes the permissive support matcher",
    permissive_support_matcher(planted_noncentral, cells),
)
check(
    "strict centrality rejects the planted noncentral lift",
    not is_central_slot_return(planted_noncentral),
)


print("\n" + "=" * 92)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID")
    sys.exit(1)

print("VERDICT: K-LINE-MONODROMY-EXACT-C_PERP-ASSOCIATED-MAP-OPEN")
print("=" * 92)
print(
    "\nPASS.  On the actual TX + Sym^2 T*X DeWitt carrier, the generator loop\n"
    "has a nontrivial induced Sym^2 return and exact Krein-line monodromy -1;\n"
    "its square has monodromy +1.  A reference Clifford lift returns J_obs\n"
    "and the distinct quaternionic J_H, preserves base/internal chirality and\n"
    "both RS projectors, and gives C0^-1 C1=-I at irreducible spinor grade.\n"
    "\nKILL (support-only inference).  The 20-slot support ledger does not lift\n"
    "that scalar uniquely: even its sign-only commutant subfamily has 2^9\n"
    "relative classes after quotienting the global sign.  A planted\n"
    "noncentral return preserves every checked support/mirror/dimension fact.\n"
    "\nOPEN AT NAMED MAP.  Build the source-owned associated-bundle transport on\n"
    "the 20 normalized provenance slots, covering the computed DeWitt frame\n"
    "loop and intertwining C_perp and the written RS symbol.  Its endpoint\n"
    "ratios, not the Krein line or support permutation alone, decide whether\n"
    "all slot phases equal the central -1."
)
