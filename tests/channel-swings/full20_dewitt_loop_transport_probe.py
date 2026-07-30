#!/usr/bin/env python3
r"""Full-20 associated transport around the actual DeWitt metric-fibre loop.

This probe closes the exact finite-dimensional residual shared by:

* ``actual_fibre_cperp_b5_naturality_probe.py`` (actual Sym^2 loop, but no
  normalized twenty-slot map);
* ``full20_observer_projector_support_probe.py`` (twenty thin embeddings, but
  no transport); and
* ``vertical_krein_weld_probe.py`` (spinor C_perp=K J_obs, but no full
  Gamma-natural vector-spinor extension).

Layer 0 is load-bearing.  Three different matrices are kept separate:

1. the raw, generally non-scalar representation matrix of the endpoint frame
   return inside each observer irrep;
2. the multiplicity-space matrix after that common representation motion is
   factored from the isomorphic S/imGamma/low-kerGamma copies; and
3. the linear returned mismatch C_0^{-1} C_1 of an antilinear coflip.

The naive pairing-induced extension eta_(9,5) tensor C_perp is computed as a
hostile near-miss.  It mixes imGamma and the low kerGamma copy and therefore
does not define the declared B5 provenance coflip.  Requiring Gamma and j to
intertwine determines the vector factor, up to one common phase, as

    (normal grading) * eta_(9,5)
      = diag(+1 on TX, -1 on Sym^2 T*X) * eta_(9,5).

That correction is derived before endpoint mismatches are read.

The corrected map is then tested on all twenty thin summands, on all nine
written first-order primitive formulas, and on every one of the 136
independently certified nonzero observer cells.  An independent mirror-pair
phase twist is required to preserve static support and fail the actual
coefficient-level intertwiner equations.

Scope: exact finite matrices on the actual real DeWitt frame return, with a
complexified observer-coordinate decomposition of the fibres.  This does not
construct a Green domain, nonlinear BV differential, stationary vacuum,
four-dimensional spectrum, physical index, generation count, or P3 map.
Deterministic, numpy only, no writes, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import os
import sys
from typing import Callable

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
TESTS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
if TESTS_ROOT not in sys.path:
    sys.path.insert(0, TESTS_ROOT)

import shiab_b5_krein_mirror_orbit_reduction as b5_reduction  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as b5_matrix  # noqa: E402


TOL = 3.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


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


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for factor in factors:
        out = np.kron(out, factor)
    return out


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


# =============================================================================
# A. Recompute the actual TX + Sym^2(T*X) DeWitt-loop return
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
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    change = mixed_rotation(turns * np.pi * parameter, positive_leg)
    metric = change.T @ ETA4_MATRIX @ change
    induced = induced_sym2_frame(change)
    coordinate_frame = block_diag(np.linalg.inv(change), induced)
    orthonormal_frame = coordinate_frame @ REFERENCE_FRAME
    return metric, induced, orthonormal_frame


def rounded_diagonal_return(matrix: np.ndarray) -> np.ndarray:
    signs = np.where(np.diag(matrix).real < 0.0, -1.0, 1.0)
    rounded = np.diag(signs)
    if max_abs(matrix - rounded) >= TOL:
        raise AssertionError("endpoint return is not diagonal +/-1")
    return rounded


print("=" * 96)
print("A. ACTUAL SYM^2 DEWITT LOOP; NO EXTERIOR-TEN SUBSTITUTION")
print("=" * 96)

reference_defect = max_abs(
    REFERENCE_FRAME.T
    @ gimmel_metric(ETA4_MATRIX)
    @ REFERENCE_FRAME
    - REFERENCE_METRIC
)
frame_defects: list[float] = []
for parameter in np.linspace(0.0, 1.0, 17):
    metric_t, _induced_t, frame_t = actual_frame_data(parameter)
    frame_defects.append(
        max_abs(frame_t.T @ gimmel_metric(metric_t) @ frame_t - REFERENCE_METRIC)
    )

metric_end, induced_end, frame_end = actual_frame_data(1.0)
return_14 = np.linalg.inv(REFERENCE_FRAME) @ frame_end
return_14[np.abs(return_14) < 1.0e-12] = 0.0
return_4 = rounded_diagonal_return(return_14[:4, :4])
return_10 = rounded_diagonal_return(return_14[4:, 4:])

metric_double, _induced_double, frame_double = actual_frame_data(1.0, turns=2)
return_double = np.linalg.inv(REFERENCE_FRAME) @ frame_double

check(
    "explicit frame is DeWitt-orthonormal with actual fibre signature (6,4)",
    reference_defect < TOL,
    f"defect {reference_defect:.2e}",
)
check(
    "actual B_t^-1 plus E -> B_t^T E B_t frame is isometric along the loop",
    max(frame_defects) < TOL,
    f"max defect {max(frame_defects):.2e}",
)
check(
    "generator closes the metric and reverses two base plus four Sym^2 legs",
    max_abs(metric_end - ETA4_MATRIX) < TOL
    and int(np.sum(np.diag(return_4) < 0)) == 2
    and int(np.sum(np.diag(return_10) < 0)) == 4
    and int(np.sum(np.linalg.eigvalsh(induced_end) < -0.5)) == 4,
)
check(
    "doubled loop returns the full actual frame to identity",
    max_abs(metric_double - ETA4_MATRIX) < TOL
    and max_abs(return_double - np.eye(14)) < TOL,
)


# =============================================================================
# B. Program-native signed Clifford substrate and all twenty thin summands
# =============================================================================


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


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    chirality = matrix_product(gammas)
    square = complex(np.trace(chirality @ chirality) / chirality.shape[0])
    if abs(square - 1.0) < TOL:
        return chirality
    if abs(square + 1.0) < TOL:
        return 1j * chirality
    raise AssertionError("chirality square is not scalar +/-1")


def chirality_bases(omega: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    hermitian_defect = max_abs(omega.conj().T - omega)
    if hermitian_defect >= TOL:
        raise AssertionError(f"chirality is not Hermitian: {hermitian_defect}")
    eigenvalues, eigenvectors = np.linalg.eigh(omega)
    return (
        eigenvectors[:, eigenvalues > 0.5],
        eigenvectors[:, eigenvalues < -0.5],
    )


def clifford_defect(gammas: list[np.ndarray], metric: np.ndarray) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    defect = 0.0
    for left, gamma_left in enumerate(gammas):
        for right, gamma_right in enumerate(gammas):
            expected = (
                2.0 * metric[left] * identity
                if left == right
                else np.zeros_like(identity)
            )
            defect = max(
                defect,
                max_abs(
                    gamma_left @ gamma_right
                    + gamma_right @ gamma_left
                    - expected
                ),
            )
    return defect


def gamma_trace_matrix(gammas: list[np.ndarray]) -> np.ndarray:
    return np.hstack(gammas)


def rs_factor_basis(
    gammas: list[np.ndarray], spin_chirality_basis: np.ndarray
) -> np.ndarray:
    vector_dimension = len(gammas)
    domain = np.kron(np.eye(vector_dimension), spin_chirality_basis)
    restricted_trace = gamma_trace_matrix(gammas) @ domain
    _left, singular_values, right_h = np.linalg.svd(
        restricted_trace, full_matrices=True
    )
    scale = max(1.0, float(singular_values[0]))
    rank = int(np.sum(singular_values > 1.0e-11 * scale))
    return domain @ right_h.conj().T[:, rank:]


def embed_base_vector_factor(
    rs4_basis: np.ndarray, internal_spin_basis: np.ndarray
) -> np.ndarray:
    rs_dimension = rs4_basis.shape[1]
    internal_dimension = internal_spin_basis.shape[1]
    reshaped = rs4_basis.reshape(4, 4, rs_dimension)
    out = np.zeros((14, 128, rs_dimension * internal_dimension), dtype=complex)
    for vector_index in range(4):
        out[vector_index] = np.kron(
            reshaped[vector_index], internal_spin_basis
        )
    return out.reshape(14 * 128, -1)


def embed_fibre_vector_factor(
    base_spin_basis: np.ndarray, rs10_basis: np.ndarray
) -> np.ndarray:
    base_dimension = base_spin_basis.shape[1]
    rs_dimension = rs10_basis.shape[1]
    reshaped = rs10_basis.reshape(10, 32, rs_dimension)
    out = np.zeros((14, 128, base_dimension * rs_dimension), dtype=complex)
    for vector_index in range(10):
        out[4 + vector_index] = np.kron(
            base_spin_basis, reshaped[vector_index]
        )
    return out.reshape(14 * 128, -1)


@dataclass(frozen=True)
class SlotBasis:
    name: str
    sector: str
    carrier: str
    basis: np.ndarray

    @property
    def dimension(self) -> int:
        return self.basis.shape[1]


print("\n" + "=" * 96)
print("B. SIGNED Cl(9,5) AND TWENTY PROVENANCE-LABELLED THIN SUMMANDS")
print("=" * 96)

gamma_4, eta_4 = signed_gammas(3, 1)
gamma_10, eta_10 = signed_gammas(6, 4)
omega_4 = normalized_chirality(gamma_4)
omega_10 = normalized_chirality(gamma_10)
spin4_plus, spin4_minus = chirality_bases(omega_4)
spin10_plus, spin10_minus = chirality_bases(omega_10)

identity_4_spin = np.eye(4, dtype=complex)
identity_10_spin = np.eye(32, dtype=complex)
gamma_14 = [
    np.kron(gamma, identity_10_spin) for gamma in gamma_4
] + [
    np.kron(omega_4, gamma) for gamma in gamma_10
]
eta_14 = np.concatenate((eta_4, eta_10))
identity_128 = np.eye(128, dtype=complex)

spin_irreps: list[tuple[str, np.ndarray]] = [
    ("E+:L16+", np.kron(spin4_plus, spin10_plus)),
    ("E+:R16-", np.kron(spin4_minus, spin10_minus)),
    ("E-:L16-", np.kron(spin4_plus, spin10_minus)),
    ("E-:R16+", np.kron(spin4_minus, spin10_plus)),
]


def normalized_partial_injection(
    spin_basis: np.ndarray, indices: range | list[int]
) -> np.ndarray:
    out = np.zeros((14, 128, spin_basis.shape[1]), dtype=complex)
    index_list = list(indices)
    for index in index_list:
        out[index] = (
            eta_14[index] * gamma_14[index] @ spin_basis
            / np.sqrt(len(index_list))
        )
    return out.reshape(14 * 128, -1)


def normalized_full_injection(spin_basis: np.ndarray) -> np.ndarray:
    base = normalized_partial_injection(spin_basis, range(4))
    fibre = normalized_partial_injection(spin_basis, range(4, 14))
    return (
        np.sqrt(4.0 / 14.0) * base
        + np.sqrt(10.0 / 14.0) * fibre
    )


def low_r_embedding(spin_basis: np.ndarray) -> np.ndarray:
    base = normalized_partial_injection(spin_basis, range(4))
    fibre = normalized_partial_injection(spin_basis, range(4, 14))
    return (
        np.sqrt(10.0 / 14.0) * base
        - np.sqrt(4.0 / 14.0) * fibre
    )


rs4_plus = rs_factor_basis(gamma_4, spin4_plus)
rs4_minus = rs_factor_basis(gamma_4, spin4_minus)
rs10_plus = rs_factor_basis(gamma_10, spin10_plus)
rs10_minus = rs_factor_basis(gamma_10, spin10_minus)

slots: list[SlotBasis] = []
for label, basis in spin_irreps:
    slots.append(SlotBasis(f"S:{label}", "S", "S", basis))
for label, basis in spin_irreps:
    slots.append(
        SlotBasis(
            f"imGamma:{label}",
            "I",
            "VS",
            normalized_full_injection(basis),
        )
    )
for label, basis in spin_irreps:
    slots.append(
        SlotBasis(
            f"kerGamma:{label}",
            "R",
            "VS",
            low_r_embedding(basis),
        )
    )

x_embeddings = [
    ("X:X32p", embed_base_vector_factor(rs4_plus, spin10_plus)),
    ("X:X23m", embed_base_vector_factor(rs4_minus, spin10_minus)),
    ("X:X2Tp", embed_fibre_vector_factor(spin4_plus, rs10_plus)),
    ("X:X1Tm", embed_fibre_vector_factor(spin4_minus, rs10_minus)),
    ("X:X32m", embed_base_vector_factor(rs4_plus, spin10_minus)),
    ("X:X23p", embed_base_vector_factor(rs4_minus, spin10_plus)),
    ("X:X2Tm", embed_fibre_vector_factor(spin4_plus, rs10_minus)),
    ("X:X1Tp", embed_fibre_vector_factor(spin4_minus, rs10_plus)),
]
for name, basis in x_embeddings:
    slots.append(SlotBasis(name, "R", "VS", basis))

slot_by_name = {slot.name: slot for slot in slots}
slots_by_sector = {
    sector: [slot for slot in slots if slot.sector == sector]
    for sector in ("S", "I", "R")
}


def gamma_trace(vector_spinors: np.ndarray) -> np.ndarray:
    reshaped = vector_spinors.reshape(14, 128, -1)
    out = np.zeros((128, reshaped.shape[2]), dtype=complex)
    for index, gamma in enumerate(gamma_14):
        out += gamma @ reshaped[index]
    return out


gram_defect = max(
    max_abs(slot.basis.conj().T @ slot.basis - np.eye(slot.dimension))
    for slot in slots
)
r_trace_defect = max(
    max_abs(gamma_trace(slot.basis))
    for slot in slots_by_sector["R"]
)

check(
    "factorized matrices satisfy the signed Cl(9,5) relations",
    clifford_defect(gamma_14, eta_14) < TOL,
)
check(
    "factor RS kernels have dimensions 6,6,144,144",
    [basis.shape[1] for basis in (rs4_plus, rs4_minus, rs10_plus, rs10_minus)]
    == [6, 6, 144, 144],
)
check(
    "all twenty signed-coordinate embeddings are orthonormal",
    len(slots) == 20 and gram_defect < TOL,
    f"max Gram defect {gram_defect:.2e}",
)
check(
    "the twelve R embeddings are gamma-traceless and dimensions close to 1920",
    r_trace_defect < TOL
    and sum(slot.dimension for slot in slots) == 1920,
    f"trace defect {r_trace_defect:.2e}",
)
check(
    "constructed labels and dimensions match the independent exact ledger",
    set(slot_by_name) == set(b5_matrix.SLOT_BY_NAME)
    and all(
        slot_by_name[name].dimension
        == b5_matrix.SLOT_BY_NAME[name].dimension
        for name in slot_by_name
    ),
)


# =============================================================================
# C. Raw endpoint representation motion and multiplicity matrices
# =============================================================================


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


lift_4, flipped_4 = spin_lift(return_4, gamma_4)
lift_10, flipped_10 = spin_lift(return_10, gamma_10)
lift_14 = np.kron(lift_4, lift_10)


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


def apply_vs_linear(
    vector_return: np.ndarray,
    spin_return: np.ndarray,
    vectors: np.ndarray,
) -> np.ndarray:
    reshaped = vectors.reshape(14, 128, -1)
    out = np.zeros_like(reshaped)
    for target_index in range(14):
        for source_index in range(14):
            coefficient = vector_return[target_index, source_index]
            if abs(coefficient) > 0.0:
                out[target_index] += (
                    coefficient * spin_return @ reshaped[source_index]
                )
    return out.reshape(14 * 128, -1)


def apply_slot_return(slot: SlotBasis, vectors: np.ndarray) -> np.ndarray:
    if slot.carrier == "S":
        return lift_14 @ vectors
    return apply_vs_linear(return_14, lift_14, vectors)


def slot_projection(slot: SlotBasis, vectors: np.ndarray) -> np.ndarray:
    return slot.basis.conj().T @ vectors


print("\n" + "=" * 96)
print("C. RAW RETURN MATRICES FIRST; MULTIPLICITY BEFORE SCHUR SCALARS")
print("=" * 96)

lift_cover_defect = max(
    adjoint_action_error(lift_4, gamma_4, return_4),
    adjoint_action_error(lift_10, gamma_10, return_10),
)
check(
    "reference Clifford lift covers the recomputed two-plus-four leg return",
    lift_cover_defect < TOL
    and len(flipped_4) == 2
    and len(flipped_10) == 4,
    f"cover defect {lift_cover_defect:.2e}",
)

raw_slot_return: dict[str, np.ndarray] = {}
raw_leakage: dict[str, float] = {}
raw_centrality: dict[str, float] = {}
for slot in slots:
    returned_basis = apply_slot_return(slot, slot.basis)
    coordinates = slot_projection(slot, returned_basis)
    residual = returned_basis - slot.basis @ coordinates
    scalar = complex(np.trace(coordinates) / slot.dimension)
    raw_slot_return[slot.name] = coordinates
    raw_leakage[slot.name] = float(np.linalg.norm(residual))
    raw_centrality[slot.name] = max_abs(
        coordinates - scalar * np.eye(slot.dimension)
    )

check(
    "actual linear endpoint transport preserves every one of the twenty summands",
    max(raw_leakage.values()) < TOL,
    f"max leakage {max(raw_leakage.values()):.2e}",
)
check(
    "raw observer-irrep return is non-scalar, so it is not a Schur phase",
    max(raw_centrality.values()) > 0.5,
    f"max centrality defect {max(raw_centrality.values()):.2e}",
)

e_labels = [label for label, _basis in spin_irreps]
raw_multiplicity_defect = 0.0
raw_multiplicity_matrices: dict[str, np.ndarray] = {}
for label in e_labels:
    names = [
        f"S:{label}",
        f"imGamma:{label}",
        f"kerGamma:{label}",
    ]
    common_irrep_return = raw_slot_return[names[0]]
    raw_multiplicity_defect = max(
        raw_multiplicity_defect,
        *(max_abs(raw_slot_return[name] - common_irrep_return) for name in names),
    )
    raw_multiplicity_matrices[label] = np.eye(3, dtype=complex)

check(
    "factoring the common irrep motion gives identity on all four three-copy multiplicities",
    raw_multiplicity_defect < TOL
    and all(
        max_abs(matrix - np.eye(3)) < TOL
        for matrix in raw_multiplicity_matrices.values()
    ),
    f"factorization defect {raw_multiplicity_defect:.2e}",
)
info(
    "raw multiplicity matrices for "
    + ", ".join(f"{label}: I_3" for label in e_labels)
)


# =============================================================================
# D. Layer 0: pairing extension versus Gamma-natural extension
# =============================================================================


def commuting_real_structure(gammas: list[np.ndarray]) -> np.ndarray:
    real_gammas = [
        gamma for gamma in gammas if max_abs(gamma.conj() - gamma) < TOL
    ]
    unitary = matrix_product(real_gammas)
    norm_square = unitary @ unitary.conj().T
    scale = float(np.max(np.abs(np.diag(norm_square))))
    return unitary / np.sqrt(scale)


observer_reality = np.kron(
    commuting_real_structure(gamma_4),
    commuting_real_structure(gamma_10),
)
krein = matrix_product(
    [gamma for gamma, sign in zip(gamma_14, eta_14) if sign > 0]
)
cperp_spin = krein @ observer_reality

# The sign q is derived independently from the spinor coflip's action on each
# gamma.  It is + on TX and - on the actual Sym^2 fibre.
normal_grading = np.array([1.0] * 4 + [-1.0] * 10)
gamma_duality_defect = 0.0
derived_normal_signs: list[int] = []
inverse_cperp = np.linalg.inv(cperp_spin)
for index, gamma in enumerate(gamma_14):
    transformed = (
        cperp_spin @ gamma.conj() @ inverse_cperp
        / eta_14[index]
    )
    plus_defect = max_abs(transformed - gamma)
    minus_defect = max_abs(transformed + gamma)
    derived_normal_signs.append(1 if plus_defect < minus_defect else -1)
    gamma_duality_defect = max(
        gamma_duality_defect, min(plus_defect, minus_defect)
    )
derived_normal_grading = np.array(derived_normal_signs, dtype=float)

# Pairing-only vector duality and the Gamma-natural extension.  The latter is
# also solved from Gamma C_V = C_S Gamma rather than merely asserted.
pairing_vector_factor = eta_14.copy()
solved_vector_factor = np.empty(14, dtype=complex)
gamma_naturality_solve_defect = 0.0
for index, gamma in enumerate(gamma_14):
    left_basis = gamma @ cperp_spin
    target = cperp_spin @ gamma.conj()
    scalar = np.vdot(left_basis, target) / np.vdot(left_basis, left_basis)
    solved_vector_factor[index] = scalar
    gamma_naturality_solve_defect = max(
        gamma_naturality_solve_defect,
        max_abs(target - scalar * left_basis),
    )
natural_vector_factor = normal_grading * eta_14


def apply_coflip_unitary(
    slot: SlotBasis,
    basis: np.ndarray,
    spin_unitary: np.ndarray,
    vector_factor: np.ndarray,
) -> np.ndarray:
    """Apply the unitary part A to conjugate(basis): C=A o conjugation."""
    if slot.carrier == "S":
        return spin_unitary @ basis.conj()
    reshaped = basis.conj().reshape(14, 128, -1)
    out = np.zeros_like(reshaped)
    for index in range(14):
        out[index] = vector_factor[index] * spin_unitary @ reshaped[index]
    return out.reshape(14 * 128, -1)


def coflip_coordinate_map(
    slot: SlotBasis,
    spin_unitary: np.ndarray,
    vector_factor: np.ndarray,
) -> tuple[np.ndarray, float]:
    mirror = slot_by_name[b5_matrix.SLOT_BY_NAME[slot.name].mirror]
    image = apply_coflip_unitary(
        slot, slot.basis, spin_unitary, vector_factor
    )
    coordinates = mirror.basis.conj().T @ image
    residual = image - mirror.basis @ coordinates
    return coordinates, float(np.linalg.norm(residual))


print("\n" + "=" * 96)
print("D. LAYER 0: WHICH C_perp EXTENSION ACTUALLY MEANS THE B5 COFLIP?")
print("=" * 96)

check(
    "spinor C_perp is an antilinear involution",
    max_abs(cperp_spin @ cperp_spin.conj() - identity_128) < TOL,
)
check(
    "its Clifford action independently recovers the +4/-10 normal grading",
    gamma_duality_defect < TOL
    and np.array_equal(derived_normal_grading, normal_grading),
    f"defect {gamma_duality_defect:.2e}",
)
check(
    "Gamma-naturality solves all fourteen vector phases up to one common phase",
    gamma_naturality_solve_defect < TOL
    and max_abs(solved_vector_factor - natural_vector_factor) < TOL,
    (
        f"solve defect {gamma_naturality_solve_defect:.2e}, "
        f"phase defect {max_abs(solved_vector_factor - natural_vector_factor):.2e}"
    ),
)

pairing_maps: dict[str, np.ndarray] = {}
pairing_leakage: dict[str, float] = {}
natural_maps: dict[str, np.ndarray] = {}
natural_leakage: dict[str, float] = {}
for slot in slots:
    pairing_maps[slot.name], pairing_leakage[slot.name] = coflip_coordinate_map(
        slot, cperp_spin, pairing_vector_factor
    )
    natural_maps[slot.name], natural_leakage[slot.name] = coflip_coordinate_map(
        slot, cperp_spin, natural_vector_factor
    )


def multiplicity_coeff(
    common_duality: np.ndarray, block: np.ndarray
) -> tuple[complex, float]:
    coefficient = np.vdot(common_duality, block) / np.vdot(
        common_duality, common_duality
    )
    return coefficient, max_abs(block - coefficient * common_duality)


pairing_multiplicity_matrices: dict[str, np.ndarray] = {}
pairing_factor_defect = 0.0
natural_multiplicity_matrices: dict[str, np.ndarray] = {}
natural_factor_defect = 0.0
for label in e_labels:
    provenance = ("S", "imGamma", "kerGamma")
    source_names = [f"{name}:{label}" for name in provenance]
    mirror_label = b5_matrix.SLOT_BY_NAME[source_names[0]].mirror.split(":", 1)[1]
    mirror_names = [f"{name}:{mirror_label}" for name in provenance]
    common_duality = natural_maps[source_names[0]]

    pairing_matrix = np.zeros((3, 3), dtype=complex)
    natural_matrix = np.zeros((3, 3), dtype=complex)
    for source_index, source_name in enumerate(source_names):
        source_slot = slot_by_name[source_name]
        pairing_image = apply_coflip_unitary(
            source_slot,
            source_slot.basis,
            cperp_spin,
            pairing_vector_factor,
        )
        natural_image = apply_coflip_unitary(
            source_slot,
            source_slot.basis,
            cperp_spin,
            natural_vector_factor,
        )
        for target_index, target_name in enumerate(mirror_names):
            target_slot = slot_by_name[target_name]
            if target_slot.carrier != source_slot.carrier:
                pairing_block = np.zeros_like(common_duality)
                natural_block = np.zeros_like(common_duality)
            else:
                target_basis = target_slot.basis
                pairing_block = target_basis.conj().T @ pairing_image
                natural_block = target_basis.conj().T @ natural_image
            pairing_coefficient, pairing_defect = multiplicity_coeff(
                common_duality, pairing_block
            )
            natural_coefficient, natural_defect = multiplicity_coeff(
                common_duality, natural_block
            )
            pairing_matrix[target_index, source_index] = pairing_coefficient
            natural_matrix[target_index, source_index] = natural_coefficient
            pairing_factor_defect = max(pairing_factor_defect, pairing_defect)
            natural_factor_defect = max(natural_factor_defect, natural_defect)

    pairing_multiplicity_matrices[label] = pairing_matrix
    natural_multiplicity_matrices[label] = natural_matrix

expected_pairing_two_copy = np.array(
    [
        [-3.0 / 7.0, 2.0 * np.sqrt(10.0) / 7.0],
        [2.0 * np.sqrt(10.0) / 7.0, 3.0 / 7.0],
    ],
    dtype=complex,
)
expected_pairing_three_copy = block_diag(
    np.ones((1, 1), dtype=complex),
    expected_pairing_two_copy,
)

check(
    "pairing-only extension mixes imGamma and low kerGamma with the exact 2x2 involution",
    pairing_factor_defect < TOL
    and all(
        max_abs(matrix - expected_pairing_three_copy) < TOL
        for matrix in pairing_multiplicity_matrices.values()
    ),
    f"factor defect {pairing_factor_defect:.2e}",
)
info(
    "pairing-only (I,low-R) multiplicity matrix = "
    "[[-3/7, 2*sqrt(10)/7], [2*sqrt(10)/7, 3/7]]"
)
check(
    "the pairing-only extension therefore fails the declared provenance-slot map",
    max(pairing_leakage.values()) > 0.5
    and any(
        abs(matrix[1, 2]) > 0.5 and abs(matrix[2, 1]) > 0.5
        for matrix in pairing_multiplicity_matrices.values()
    ),
    f"max declared-slot leakage {max(pairing_leakage.values()):.2e}",
)
check(
    "the Gamma-natural +4/-10 correction maps every slot to its declared mirror",
    natural_factor_defect < TOL
    and max(natural_leakage.values()) < TOL
    and all(
        max_abs(matrix - np.eye(3)) < TOL
        for matrix in natural_multiplicity_matrices.values()
    ),
    (
        f"factor defect {natural_factor_defect:.2e}, "
        f"max leakage {max(natural_leakage.values()):.2e}"
    ),
)

natural_involution_defect = 0.0
for slot in slots:
    mirror_name = b5_matrix.SLOT_BY_NAME[slot.name].mirror
    natural_involution_defect = max(
        natural_involution_defect,
        max_abs(
            natural_maps[mirror_name]
            @ natural_maps[slot.name].conj()
            - np.eye(slot.dimension)
        ),
    )
check(
    "the corrected twenty-slot map is an antilinear involution pair by pair",
    natural_involution_defect < TOL,
    f"defect {natural_involution_defect:.2e}",
)


# =============================================================================
# E. Transport the corrected coflip and compute endpoint mismatches
# =============================================================================


def returned_antilinear(
    unitary_part: np.ndarray, linear_lift: np.ndarray
) -> np.ndarray:
    return (
        linear_lift
        @ unitary_part
        @ np.linalg.inv(linear_lift.conj())
    )


print("\n" + "=" * 96)
print("E. ENDPOINT MISMATCHES AFTER MULTIPLICITY NORMALIZATION")
print("=" * 96)

cperp_spin_returned = returned_antilinear(cperp_spin, lift_14)
spin_return_scalar = complex(
    np.trace(
        np.linalg.inv(cperp_spin.conj())
        @ cperp_spin_returned.conj()
    )
    / 128
)
check(
    "actual Clifford lift returns the spinor coflip with one minus sign",
    max_abs(cperp_spin_returned + cperp_spin) < TOL
    and abs(spin_return_scalar + 1.0) < TOL,
    f"scalar {spin_return_scalar.real:+.0f}",
)

returned_maps: dict[str, np.ndarray] = {}
returned_leakage: dict[str, float] = {}
endpoint_mismatch: dict[str, np.ndarray] = {}
endpoint_scalars: dict[str, complex] = {}
endpoint_centrality: dict[str, float] = {}
for slot in slots:
    returned_maps[slot.name], returned_leakage[slot.name] = coflip_coordinate_map(
        slot, cperp_spin_returned, natural_vector_factor
    )
    mismatch = (
        np.linalg.inv(natural_maps[slot.name].conj())
        @ returned_maps[slot.name].conj()
    )
    scalar = complex(np.trace(mismatch) / slot.dimension)
    endpoint_mismatch[slot.name] = mismatch
    endpoint_scalars[slot.name] = scalar
    endpoint_centrality[slot.name] = max_abs(
        mismatch - scalar * np.eye(slot.dimension)
    )

check(
    "returned corrected coflip still lands in every declared mirror slot",
    max(returned_leakage.values()) < TOL,
    f"max leakage {max(returned_leakage.values()):.2e}",
)
check(
    "all twenty linear mismatches are central -I",
    max(endpoint_centrality.values()) < TOL
    and max(abs(value + 1.0) for value in endpoint_scalars.values()) < TOL,
    (
        f"centrality {max(endpoint_centrality.values()):.2e}, "
        f"scalar spread {max(abs(value + 1.0) for value in endpoint_scalars.values()):.2e}"
    ),
)

endpoint_multiplicity_matrices: dict[str, np.ndarray] = {}
for label in e_labels:
    names = [
        f"S:{label}",
        f"imGamma:{label}",
        f"kerGamma:{label}",
    ]
    matrix = np.zeros((3, 3), dtype=complex)
    for index, name in enumerate(names):
        matrix[index, index] = endpoint_scalars[name]
    endpoint_multiplicity_matrices[label] = matrix

check(
    "each three-copy endpoint multiplicity matrix is -I_3 before slotwise reading",
    all(
        max_abs(matrix + np.eye(3)) < TOL
        for matrix in endpoint_multiplicity_matrices.values()
    ),
)
info(
    "endpoint multiplicity matrices for "
    + ", ".join(f"{label}: -I_3" for label in e_labels)
)

lift_double = lift_14 @ lift_14
cperp_spin_double = returned_antilinear(cperp_spin, lift_double)
double_maps: dict[str, np.ndarray] = {}
double_mismatch_defect = 0.0
for slot in slots:
    double_map, double_leakage = coflip_coordinate_map(
        slot, cperp_spin_double, natural_vector_factor
    )
    mismatch = (
        np.linalg.inv(natural_maps[slot.name].conj())
        @ double_map.conj()
    )
    double_maps[slot.name] = mismatch
    double_mismatch_defect = max(
        double_mismatch_defect,
        double_leakage,
        max_abs(mismatch - np.eye(slot.dimension)),
    )
check(
    "doubled actual loop has +I mismatch on every slot",
    max_abs(return_double - np.eye(14)) < TOL
    and max_abs(lift_double - np.eye(128)) < TOL
    and max_abs(cperp_spin_double - cperp_spin) < TOL
    and double_mismatch_defect < TOL,
    f"defect {double_mismatch_defect:.2e}",
)


# =============================================================================
# F. Written Gamma, j, P_R, and all nine first-order primitives
# =============================================================================


def j_map(spinors: np.ndarray) -> np.ndarray:
    out = np.zeros((14, 128, spinors.shape[1]), dtype=complex)
    for index in range(14):
        out[index] = eta_14[index] * gamma_14[index] @ spinors / 14.0
    return out.reshape(14 * 128, -1)


def p_i(vector_spinors: np.ndarray) -> np.ndarray:
    return j_map(gamma_trace(vector_spinors))


def p_r(vector_spinors: np.ndarray) -> np.ndarray:
    return vector_spinors - p_i(vector_spinors)


def clifford_symbol(vector: np.ndarray) -> np.ndarray:
    return sum(vector[index] * gamma_14[index] for index in range(14))


def l_map(spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    out = np.zeros((14, 128, spinors.shape[1]), dtype=complex)
    for index in range(14):
        out[index] = vector[index] * spinors
    return out.reshape(14 * 128, -1)


def contraction(vector_spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    reshaped = vector_spinors.reshape(14, 128, -1)
    out = np.zeros((128, reshaped.shape[2]), dtype=complex)
    for index in range(14):
        out += eta_14[index] * vector[index] * reshaped[index]
    return out


def delta_map(vector_spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return -contraction(vector_spinors, vector)


def m_map(vector_spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    reshaped = vector_spinors.reshape(14, 128, -1)
    symbol = clifford_symbol(vector)
    out = np.empty_like(reshaped)
    for index in range(14):
        out[index] = symbol @ reshaped[index]
    return out.reshape(14 * 128, -1)


def t_map(spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return p_r(l_map(spinors, vector))


def q_map(vector_spinors: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return p_r(m_map(p_r(vector_spinors), vector))


BlockOperator = Callable[[np.ndarray, np.ndarray], np.ndarray]


def op_ss(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return clifford_symbol(vector) @ source


def op_si(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return clifford_symbol(vector) @ gamma_trace(source)


def op_sr(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return delta_map(source, vector)


def op_is(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return j_map(clifford_symbol(vector) @ source)


def op_ii(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return j_map(clifford_symbol(vector) @ gamma_trace(source))


def op_ir(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return j_map(delta_map(source, vector))


def op_rs(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return t_map(source, vector)


def op_ri(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return t_map(gamma_trace(source), vector)


def op_rr(source: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return q_map(source, vector)


block_operators: dict[tuple[str, str], tuple[str, BlockOperator]] = {
    ("S", "S"): ("SS", op_ss),
    ("I", "S"): ("SI", op_si),
    ("R", "S"): ("SR", op_sr),
    ("S", "I"): ("IS", op_is),
    ("I", "I"): ("II", op_ii),
    ("R", "I"): ("IR", op_ir),
    ("S", "R"): ("RS", op_rs),
    ("I", "R"): ("RI", op_ri),
    ("R", "R"): ("RR", op_rr),
}


def apply_carrier_return(
    sector: str, vectors: np.ndarray
) -> np.ndarray:
    if sector == "S":
        return lift_14 @ vectors
    return apply_vs_linear(return_14, lift_14, vectors)


print("\n" + "=" * 96)
print("F. WRITTEN INTERTWINERS AND THE NINE FIRST-ORDER FORMULAS")
print("=" * 96)

rng = np.random.default_rng(20260730)
random_spinors = (
    rng.standard_normal((128, 3)) + 1j * rng.standard_normal((128, 3))
)
random_vs = (
    rng.standard_normal((14 * 128, 3))
    + 1j * rng.standard_normal((14 * 128, 3))
)

gamma_covariance_defect = max_abs(
    gamma_trace(apply_vs_linear(return_14, lift_14, random_vs))
    - lift_14 @ gamma_trace(random_vs)
)
j_covariance_defect = max_abs(
    apply_vs_linear(return_14, lift_14, j_map(random_spinors))
    - j_map(lift_14 @ random_spinors)
)
pr_covariance_defect = max_abs(
    p_r(apply_vs_linear(return_14, lift_14, random_vs))
    - apply_vs_linear(return_14, lift_14, p_r(random_vs))
)
check(
    "actual loop transport intertwines Gamma, j, and P_R",
    max(gamma_covariance_defect, j_covariance_defect, pr_covariance_defect)
    < TOL,
    (
        f"defects Gamma={gamma_covariance_defect:.2e}, "
        f"j={j_covariance_defect:.2e}, P_R={pr_covariance_defect:.2e}"
    ),
)

generic_vector = np.array(
    [1.0, 2.0, 3.0, 5.0, 1.0, 2.0, 4.0, 7.0, 11.0, 16.0, 22.0, 29.0, 37.0, 46.0],
    dtype=complex,
)
generic_vector /= np.linalg.norm(generic_vector)

operator_transport_defects: dict[str, float] = {}
for (source_sector, target_sector), (name, operator) in block_operators.items():
    source_slot = slots_by_sector[source_sector][0]
    coordinates = (
        rng.standard_normal((source_slot.dimension, 2))
        + 1j * rng.standard_normal((source_slot.dimension, 2))
    )
    source = source_slot.basis @ coordinates
    source_returned = apply_carrier_return(source_sector, source)
    left = apply_carrier_return(
        target_sector, operator(source, generic_vector)
    )
    right = operator(source_returned, return_14 @ generic_vector)
    scale = max(1.0, float(np.linalg.norm(left)), float(np.linalg.norm(right)))
    operator_transport_defects[name] = float(np.linalg.norm(left - right)) / scale

check(
    "all nine written primitives are covariant under the actual loop return",
    max(operator_transport_defects.values()) < TOL,
    f"max defect {max(operator_transport_defects.values()):.2e}",
)


# =============================================================================
# G. All 136 coefficient cells and a planted independent slot phase
# =============================================================================


def sector_from_name(name: str) -> str:
    if name.startswith("S:"):
        return "S"
    if name.startswith("imGamma:"):
        return "I"
    if name.startswith(("kerGamma:", "X:")):
        return "R"
    raise ValueError(f"unknown slot {name}")


def heldout_parts(cell: tuple[str, str]) -> tuple[int, int]:
    source_name, target_name = cell
    source = b5_matrix.TYPES[b5_matrix.SLOT_BY_NAME[source_name].h_type]
    target = b5_matrix.TYPES[b5_matrix.SLOT_BY_NAME[target_name].h_type]
    base_part = int(
        source.d5_weight == target.d5_weight
        and target.left_dim in b5_matrix.su2_vector_targets(source.left_dim)
        and target.right_dim in b5_matrix.su2_vector_targets(source.right_dim)
    )
    fibre_part = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * b5_matrix.vector_tensor_decomposition(source.d5_weight).get(
        target.d5_weight, 0
    )
    return base_part, fibre_part


def static_phase_matcher(
    phases: dict[str, int], cells: set[tuple[str, str]]
) -> bool:
    if set(phases) != set(slot_by_name):
        return False
    for slot in b5_matrix.SLOTS:
        if phases[slot.name] != phases[slot.mirror]:
            return False
    for source, target in cells:
        mirror_cell = (
            b5_matrix.SLOT_BY_NAME[source].mirror,
            b5_matrix.SLOT_BY_NAME[target].mirror,
        )
        if mirror_cell not in cells:
            return False
        if phases[target] / phases[source] != (
            phases[mirror_cell[1]] / phases[mirror_cell[0]]
        ):
            return False
    return True


print("\n" + "=" * 96)
print("G. COEFFICIENT-LEVEL COFLIP COVARIANCE ON ALL 136 CELLS")
print("=" * 96)

base_vector = np.zeros(14, dtype=complex)
base_vector[:4] = np.array([1.0, 2.0, 3.0, 5.0])
base_vector /= np.linalg.norm(base_vector)
fibre_vector = np.zeros(14, dtype=complex)
fibre_vector[4:] = np.array(
    [1.0, 2.0, 4.0, 7.0, 11.0, 16.0, 22.0, 29.0, 37.0, 46.0]
)
fibre_vector /= np.linalg.norm(fibre_vector)

all_cells = b5_reduction.nonzero_cells()
check(
    "independent exact ledger supplies 136 cells split 68 base plus 68 fibre",
    len(all_cells) == 136
    and sum(heldout_parts(cell) == (1, 0) for cell in all_cells) == 68
    and sum(heldout_parts(cell) == (0, 1) for cell in all_cells) == 68,
)

witness_coordinates: dict[str, np.ndarray] = {}
for slot in slots:
    coordinates = (
        rng.standard_normal((slot.dimension, 2))
        + 1j * rng.standard_normal((slot.dimension, 2))
    )
    coordinates, _triangular = np.linalg.qr(coordinates)
    witness_coordinates[slot.name] = coordinates[:, :2]

canonical_cell_residuals: dict[tuple[str, str], float] = {}
cell_amplitudes: dict[tuple[str, str], float] = {}
cell_cache: dict[
    tuple[str, str],
    tuple[np.ndarray, np.ndarray],
] = {}
for cell in sorted(all_cells):
    source_name, target_name = cell
    source = slot_by_name[source_name]
    target = slot_by_name[target_name]
    mirror_source_name = b5_matrix.SLOT_BY_NAME[source_name].mirror
    mirror_target_name = b5_matrix.SLOT_BY_NAME[target_name].mirror
    mirror_source = slot_by_name[mirror_source_name]
    mirror_target = slot_by_name[mirror_target_name]
    source_sector = sector_from_name(source_name)
    target_sector = sector_from_name(target_name)
    _block_name, operator = block_operators[(source_sector, target_sector)]
    parts = heldout_parts(cell)
    vector = base_vector if parts == (1, 0) else fibre_vector
    transformed_vector = natural_vector_factor * vector

    coordinates = witness_coordinates[source_name]
    source_vectors = source.basis @ coordinates
    output = operator(source_vectors, vector)
    projected_output = target.basis.conj().T @ output

    mirror_coordinates = natural_maps[source_name] @ coordinates.conj()
    mirror_vectors = mirror_source.basis @ mirror_coordinates
    mirror_output = operator(mirror_vectors, transformed_vector)
    projected_mirror_output = (
        mirror_target.basis.conj().T @ mirror_output
    )

    left = natural_maps[target_name] @ projected_output.conj()
    right = projected_mirror_output
    scale = max(
        1.0e-14,
        float(np.linalg.norm(left)),
        float(np.linalg.norm(right)),
    )
    canonical_cell_residuals[cell] = float(np.linalg.norm(left - right)) / scale
    cell_amplitudes[cell] = float(np.linalg.norm(projected_output))
    cell_cache[cell] = (left, right)

check(
    "generic witnesses make every independently allowed written coefficient cell nonzero",
    min(cell_amplitudes.values()) > 1.0e-7,
    f"minimum amplitude {min(cell_amplitudes.values()):.2e}",
)
check(
    "Gamma-natural coflip intertwines every one of the 136 actual formula projections",
    max(canonical_cell_residuals.values()) < TOL,
    f"max residual {max(canonical_cell_residuals.values()):.2e}",
)

mirror_pairs = sorted(
    {
        tuple(sorted((slot.name, slot.mirror)))
        for slot in b5_matrix.SLOTS
    }
)
twisted_pair = mirror_pairs[0]
twist_phases = {name: 1 for name in slot_by_name}
for name in twisted_pair:
    twist_phases[name] = -1

twisted_maps = {
    name: twist_phases[name] * natural_maps[name] for name in natural_maps
}
twisted_involution_defect = max(
    max_abs(
        twisted_maps[b5_matrix.SLOT_BY_NAME[name].mirror]
        @ twisted_maps[name].conj()
        - np.eye(slot_by_name[name].dimension)
    )
    for name in slot_by_name
)

twisted_cell_residuals: dict[tuple[str, str], float] = {}
for cell, (canonical_left, canonical_right) in cell_cache.items():
    source_name, target_name = cell
    left = twist_phases[target_name] * canonical_left
    right = twist_phases[source_name] * canonical_right
    scale = max(
        1.0e-14,
        float(np.linalg.norm(left)),
        float(np.linalg.norm(right)),
    )
    twisted_cell_residuals[cell] = float(np.linalg.norm(left - right)) / scale

twisted_failures = {
    cell: residual
    for cell, residual in twisted_cell_residuals.items()
    if residual > 1.0e-6
}
check(
    "planted independent pair phase preserves involution and the static support matcher",
    twisted_involution_defect < TOL
    and static_phase_matcher(twist_phases, all_cells),
    f"twisted pair {twisted_pair}",
)
check(
    "the same planted phase fails the actual written differential intertwiners",
    bool(twisted_failures)
    and max(twisted_cell_residuals.values()) > 1.0,
    (
        f"{len(twisted_failures)} failing cells, "
        f"max residual {max(twisted_cell_residuals.values()):.2e}"
    ),
)

all_pair_phase_assignments: list[dict[str, int]] = []
for signs in product((-1, 1), repeat=len(mirror_pairs)):
    assignment: dict[str, int] = {}
    for sign, pair in zip(signs, mirror_pairs):
        for name in pair:
            assignment[name] = sign
    all_pair_phase_assignments.append(assignment)

static_admissible_count = sum(
    static_phase_matcher(assignment, all_cells)
    for assignment in all_pair_phase_assignments
)
coefficient_admissible = [
    assignment
    for assignment in all_pair_phase_assignments
    if all(
        assignment[source] == assignment[target]
        for source, target in all_cells
    )
]
check(
    "actual nonzero coefficient equations reduce 2^10 static phases to one global class",
    static_admissible_count == 2**10
    and len(coefficient_admissible) == 2
    and all(len(set(assignment.values())) == 1 for assignment in coefficient_admissible),
    (
        f"static {static_admissible_count}, "
        f"coefficient-level {len(coefficient_admissible)} absolute"
    ),
)


print("\n" + "=" * 96)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print(
    "VERDICT: FULL20-GAMMA-NATURAL-DEWITT-TRANSPORT-CENTRAL-MINUS-ONE"
)
print("=" * 96)
print(
    "\nLAYER 0 CORRECTION.  Extending the spinor coflip by the Krein pairing\n"
    "alone asks the wrong full-carrier question: eta_(9,5) tensor C_perp mixes\n"
    "imGamma with the low kerGamma copy by the exact involution\n"
    "[[-3/7,2sqrt(10)/7],[2sqrt(10)/7,3/7]].  It therefore has no declared\n"
    "twenty-slot scalar table.  Requiring the already-written Gamma and j maps\n"
    "to intertwine uniquely supplies the missing normal grading (+ on TX, - on\n"
    "the actual Sym^2 fibre), up to one common phase.  This corrected map\n"
    "preserves P_I, P_R, and every declared mirror slot.\n"
    "\nTRANSPORT.  The raw endpoint matrices are non-scalar observer-group\n"
    "motions, as they should be.  After factoring those motions, all four\n"
    "S/imGamma/low-R multiplicity returns are I_3.  The transported corrected\n"
    "coflip has C0^-1 C1=-I on every one of the twenty summands, including\n"
    "-I_3 on every repeated E-type multiplicity space; the doubled loop gives\n"
    "+I.  There is no residual X, provenance, or multiplicity phase at this\n"
    "finite associated-bundle grade.\n"
    "\nDIFFERENTIAL.  Gamma, j, P_R, and all nine written first-order primitives\n"
    "are covariant under the actual loop.  The corrected coflip intertwines all\n"
    "136 nonzero coefficient projections.  A planted independent mirror-pair\n"
    "phase preserves the static support and involution but fails those actual\n"
    "intertwiner equations.  Thus the coefficient construction leaves one\n"
    "global orientation phase, and the DeWitt loop fixes its nontrivial return.\n"
    "\nBOUNDARY.  This closes the P1/P2 weld at exact finite associated-bundle and\n"
    "formal first-order-expression grade.  It does not freeze a common closed\n"
    "domain, nonlinear BV completion, physical index, generation count, or P3."
)
