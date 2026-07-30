#!/usr/bin/env python3
r"""Independent observer-complex support rederivation with thin embeddings.

This probe constructs the twenty labelled observer summands of

    S + im(Gamma_14) + ker(Gamma_14)

inside a factorized *complex/compact computational realization*

    Cl_14(C) = Cl_4(C) hat-tensor Cl_10(C).

It then applies the nine written first-order block formulas directly to those
embeddings and measures every source/target projection for a generic base
covector and a generic fibre covector.  The held-out 136-cell representation
ledger is imported only after the construction has emitted its supports.

Scope firewall
---------------
The matrices here are observer-complex coordinate embeddings.  They are not
the still-open program-native Lorentzian/Krein projectors, normalized
associated-bundle transport, formal adjoints, Green forms, closed domains,
Noether identities, or BV differentials.  A positive Euclidean coordinate
norm is used only to detect whether a complex intertwiner block is zero.

Efficiency
----------
No dense 1792 x 1792 vector-spinor projector or operator is formed.  The
largest carrier matrix is one thin slot embedding, at most 1792 x 288.
Support is witnessed by four deterministic generic source vectors per slot.
Because every allowed observer Hom multiplicity is zero or one, a nonzero
coordinate projection certifies the cell; the held-out exact ledger and a
reported numerical zero/nonzero gap audit the generic-witness step.

Deterministic, numpy only, no writes, no network.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
import sys
from typing import Callable

import numpy as np


TOL = 2.0e-9
WITNESSES = 4
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1.0 + 0.0j]])
    for factor in factors:
        out = np.kron(out, factor)
    return out


def euclidean_gammas(n_pairs: int) -> list[np.ndarray]:
    """Jordan-Wigner Euclidean gamma matrices, all Hermitian and square +1."""
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


def normalized_chirality(gammas: list[np.ndarray]) -> np.ndarray:
    raw = np.eye(gammas[0].shape[0], dtype=complex)
    for gamma in gammas:
        raw = raw @ gamma
    square = complex(np.trace(raw @ raw) / raw.shape[0])
    if abs(square - 1.0) < 1.0e-10:
        omega = raw
    elif abs(square + 1.0) < 1.0e-10:
        omega = 1j * raw
    else:
        raise AssertionError(f"chirality square is not scalar +/-1: {square}")
    omega = 0.5 * (omega + omega.conj().T)
    return omega


def chirality_bases(omega: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(omega)
    plus = eigenvectors[:, eigenvalues > 0.5]
    minus = eigenvectors[:, eigenvalues < -0.5]
    return plus, minus


def clifford_defect(gammas: list[np.ndarray]) -> float:
    identity = np.eye(gammas[0].shape[0], dtype=complex)
    defect = 0.0
    for left, gamma_left in enumerate(gammas):
        for right, gamma_right in enumerate(gammas):
            expected = (
                2.0 * identity if left == right else np.zeros_like(identity)
            )
            observed = gamma_left @ gamma_right + gamma_right @ gamma_left
            defect = max(defect, float(np.max(np.abs(observed - expected))))
    return defect


def gamma_trace_matrix(gammas: list[np.ndarray]) -> np.ndarray:
    return np.hstack(gammas)


def rs_factor_basis(
    gammas: list[np.ndarray], spin_chirality_basis: np.ndarray
) -> np.ndarray:
    """Orthonormal basis of ker(Gamma_d) in V_d tensor S_d^{+/-}."""
    vector_dimension = len(gammas)
    spinor_dimension = gammas[0].shape[0]
    domain = np.kron(np.eye(vector_dimension), spin_chirality_basis)
    restricted_trace = gamma_trace_matrix(gammas) @ domain
    _left, singular_values, right_h = np.linalg.svd(
        restricted_trace, full_matrices=True
    )
    scale = max(1.0, float(singular_values[0]))
    rank = int(np.sum(singular_values > 1.0e-11 * scale))
    null_coordinates = right_h.conj().T[:, rank:]
    basis = domain @ null_coordinates
    expected = (
        vector_dimension * spin_chirality_basis.shape[1] - spinor_dimension // 2
    )
    if basis.shape[1] != expected:
        raise AssertionError(
            f"unexpected RS factor dimension {basis.shape[1]} != {expected}"
        )
    return basis


def factor_gram_defect(basis: np.ndarray) -> float:
    identity = np.eye(basis.shape[1], dtype=complex)
    return float(np.max(np.abs(basis.conj().T @ basis - identity)))


def embed_base_vector_factor(
    rs4_basis: np.ndarray, internal_spin_basis: np.ndarray
) -> np.ndarray:
    """Embed RS4 tensor S10 in the base-vector part of V14 tensor S14."""
    rs_dimension = rs4_basis.shape[1]
    internal_dimension = internal_spin_basis.shape[1]
    reshaped = rs4_basis.reshape(4, 4, rs_dimension)
    out = np.zeros(
        (14, 128, rs_dimension * internal_dimension), dtype=complex
    )
    for vector_index in range(4):
        out[vector_index] = np.kron(
            reshaped[vector_index], internal_spin_basis
        )
    return out.reshape(14 * 128, -1)


def embed_fibre_vector_factor(
    base_spin_basis: np.ndarray, rs10_basis: np.ndarray
) -> np.ndarray:
    """Embed S4 tensor RS10 in the fibre-vector part of V14 tensor S14."""
    base_dimension = base_spin_basis.shape[1]
    rs_dimension = rs10_basis.shape[1]
    reshaped = rs10_basis.reshape(10, 32, rs_dimension)
    out = np.zeros(
        (14, 128, base_dimension * rs_dimension), dtype=complex
    )
    for vector_index in range(10):
        out[4 + vector_index] = np.kron(
            base_spin_basis, reshaped[vector_index]
        )
    return out.reshape(14 * 128, -1)


@dataclass(frozen=True)
class SlotBasis:
    name: str
    sector: str
    basis: np.ndarray

    @property
    def dimension(self) -> int:
        return self.basis.shape[1]


Cell = tuple[str, str]


print("=" * 92)
print("FULL-20 OBSERVER-COMPLEX THIN-EMBEDDING SUPPORT REDERIVATION")
print("=" * 92)
print("construction: Cl4(C) x Cl10(C), compact coordinate norm, geometric ker(Gamma)")
print("not claimed: native Krein projectors, transport, formal adjoint, domain, or BV closure")


# ---------------------------------------------------------------------------
# A. Factorized complex Clifford substrate and twenty independent embeddings.
# ---------------------------------------------------------------------------
print("\nA. Factorized Clifford substrate and thin slot embeddings")

gamma_4 = euclidean_gammas(2)
gamma_10 = euclidean_gammas(5)
omega_4 = normalized_chirality(gamma_4)
omega_10 = normalized_chirality(gamma_10)
spin4_plus, spin4_minus = chirality_bases(omega_4)
spin10_plus, spin10_minus = chirality_bases(omega_10)

identity_4 = np.eye(4, dtype=complex)
identity_32 = np.eye(32, dtype=complex)
base_gammas = [np.kron(gamma, identity_32) for gamma in gamma_4]
fibre_gammas = [np.kron(omega_4, gamma) for gamma in gamma_10]
gamma_14 = base_gammas + fibre_gammas

check(
    "factor Clifford relations hold in dimensions 4, 10, and 14",
    max(
        clifford_defect(gamma_4),
        clifford_defect(gamma_10),
        clifford_defect(gamma_14),
    )
    < 1.0e-10,
)
check(
    "factor chirality dimensions are 2+2 and 16+16",
    spin4_plus.shape[1] == spin4_minus.shape[1] == 2
    and spin10_plus.shape[1] == spin10_minus.shape[1] == 16,
)

# Four spinor observer irreps.  The names are constructed from the factor
# chiralities, not imported from the held-out multiplicity ledger.
spin_irreps: list[tuple[str, np.ndarray]] = [
    ("E+:L16+", np.kron(spin4_plus, spin10_plus)),
    ("E+:R16-", np.kron(spin4_minus, spin10_minus)),
    ("E-:L16-", np.kron(spin4_plus, spin10_minus)),
    ("E-:R16+", np.kron(spin4_minus, spin10_plus)),
]

spin_concat = np.hstack([basis for _label, basis in spin_irreps])
check(
    "the four factor-spinor embeddings are orthonormal and complete",
    spin_concat.shape == (128, 128)
    and np.max(
        np.abs(
            spin_concat.conj().T @ spin_concat
            - np.eye(128, dtype=complex)
        )
    )
    < 1.0e-10,
)


def normalized_full_injection(spin_basis: np.ndarray) -> np.ndarray:
    """Normalized span-equivalent version of Gamma^sharp/14."""
    return np.vstack([gamma @ spin_basis for gamma in gamma_14]) / np.sqrt(14.0)


def normalized_partial_injection(
    spin_basis: np.ndarray, indices: range | list[int]
) -> np.ndarray:
    out = np.zeros((14, 128, spin_basis.shape[1]), dtype=complex)
    index_list = list(indices)
    for index in index_list:
        out[index] = gamma_14[index] @ spin_basis / np.sqrt(len(index_list))
    return out.reshape(14 * 128, -1)


def low_r_embedding(spin_basis: np.ndarray, wrong_sign: bool = False) -> np.ndarray:
    """The unique S4 tensor S10 combination in ker(Gamma_14)."""
    base_part = normalized_partial_injection(spin_basis, range(4))
    fibre_part = normalized_partial_injection(spin_basis, range(4, 14))
    sign = 1.0 if wrong_sign else -1.0
    return (
        np.sqrt(10.0 / 14.0) * base_part
        + sign * np.sqrt(4.0 / 14.0) * fibre_part
    )


rs4_plus = rs_factor_basis(gamma_4, spin4_plus)
rs4_minus = rs_factor_basis(gamma_4, spin4_minus)
rs10_plus = rs_factor_basis(gamma_10, spin10_plus)
rs10_minus = rs_factor_basis(gamma_10, spin10_minus)

factor_rs_checks = [
    (
        rs4_plus,
        gamma_trace_matrix(gamma_4),
        6,
    ),
    (
        rs4_minus,
        gamma_trace_matrix(gamma_4),
        6,
    ),
    (
        rs10_plus,
        gamma_trace_matrix(gamma_10),
        144,
    ),
    (
        rs10_minus,
        gamma_trace_matrix(gamma_10),
        144,
    ),
]
check(
    "RS4/RS10 factor kernels have dimensions 6,6,144,144",
    all(basis.shape[1] == expected for basis, _trace, expected in factor_rs_checks),
)
check(
    "RS factor bases are orthonormal and gamma-traceless",
    max(
        max(
            factor_gram_defect(basis),
            float(np.max(np.abs(trace @ basis))),
        )
        for basis, trace, _expected in factor_rs_checks
    )
    < 1.0e-10,
)

slots: list[SlotBasis] = []

# S provenance.
for label, basis in spin_irreps:
    slots.append(SlotBasis(f"S:{label}", "S", basis))

# im(Gamma) provenance.
for label, basis in spin_irreps:
    slots.append(
        SlotBasis(f"imGamma:{label}", "I", normalized_full_injection(basis))
    )

# Low ker(Gamma) provenance.
for label, basis in spin_irreps:
    slots.append(SlotBasis(f"kerGamma:{label}", "R", low_r_embedding(basis)))

# The two product-rule X families, split into their eight observer irreps.
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
    slots.append(SlotBasis(name, "R", basis))

slot_by_name = {slot.name: slot for slot in slots}
slots_by_sector = {
    sector: [slot for slot in slots if slot.sector == sector]
    for sector in ("S", "I", "R")
}

check("twenty provenance-labelled embeddings are constructed", len(slots) == 20)
check(
    "slot dimensions close as S=128, I=128, R=1664, total=1920",
    sum(slot.dimension for slot in slots_by_sector["S"]) == 128
    and sum(slot.dimension for slot in slots_by_sector["I"]) == 128
    and sum(slot.dimension for slot in slots_by_sector["R"]) == 1664
    and sum(slot.dimension for slot in slots) == 1920,
)
check(
    "largest thin embedding is 1792 x 288 (no dense vector-spinor projector)",
    max(slot.basis.shape[0] for slot in slots) == 1792
    and max(slot.dimension for slot in slots) == 288,
)


def gamma_trace(vector_spinors: np.ndarray) -> np.ndarray:
    """Gamma trace on shape (1792,k) or (14,128,k)."""
    if vector_spinors.ndim == 2:
        reshaped = vector_spinors.reshape(14, 128, -1)
    else:
        reshaped = vector_spinors
    out = np.zeros((128, reshaped.shape[2]), dtype=complex)
    for index, gamma in enumerate(gamma_14):
        out += gamma @ reshaped[index]
    return out


r_trace_defect = max(
    float(np.max(np.abs(gamma_trace(slot.basis))))
    for slot in slots_by_sector["R"]
)
check(
    "all twelve R embeddings are in ker(Gamma_14)",
    r_trace_defect < 1.0e-10,
    f"max defect {r_trace_defect:.2e}",
)

# A planted wrong sign must fail the same predicate.
wrong_low = low_r_embedding(spin_irreps[0][1], wrong_sign=True)
wrong_low_trace = float(np.linalg.norm(gamma_trace(wrong_low)))
check(
    "wrong-sign low-R embedding is rejected by gamma trace",
    wrong_low_trace > 1.0,
    f"trace norm {wrong_low_trace:.2e}",
)


# ---------------------------------------------------------------------------
# B. Intrinsic primitive formulas and generic coordinate support.
# ---------------------------------------------------------------------------
print("\nB. Apply the nine block formulas before opening the held-out ledger")


def j_map(spinors: np.ndarray) -> np.ndarray:
    return np.vstack([gamma @ spinors for gamma in gamma_14]) / 14.0


def p_i(vector_spinors: np.ndarray) -> np.ndarray:
    return j_map(gamma_trace(vector_spinors))


def p_r(vector_spinors: np.ndarray) -> np.ndarray:
    return vector_spinors - p_i(vector_spinors)


def clifford_symbol(xi: np.ndarray) -> np.ndarray:
    return sum(xi[index] * gamma_14[index] for index in range(14))


def l_map(spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    out = np.zeros((14, 128, spinors.shape[1]), dtype=complex)
    for index in range(14):
        out[index] = xi[index] * spinors
    return out.reshape(14 * 128, -1)


def contraction(vector_spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    reshaped = vector_spinors.reshape(14, 128, -1)
    out = np.zeros((128, reshaped.shape[2]), dtype=complex)
    for index in range(14):
        out += xi[index] * reshaped[index]
    return out


def delta_map(vector_spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return -contraction(vector_spinors, xi)


def m_map(vector_spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    reshaped = vector_spinors.reshape(14, 128, -1)
    cxi = clifford_symbol(xi)
    out = np.empty_like(reshaped)
    for index in range(14):
        out[index] = cxi @ reshaped[index]
    return out.reshape(14 * 128, -1)


def t_map(spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return p_r(l_map(spinors, xi))


def q_map(vector_spinors: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return p_r(m_map(p_r(vector_spinors), xi))


BlockOperator = Callable[[np.ndarray, np.ndarray], np.ndarray]


def op_ss(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return clifford_symbol(xi) @ source


def op_si(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return clifford_symbol(xi) @ gamma_trace(source)


def op_sr(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return delta_map(source, xi)


def op_is(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return j_map(clifford_symbol(xi) @ source)


def op_ii(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return j_map(clifford_symbol(xi) @ gamma_trace(source))


def op_ir(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return j_map(delta_map(source, xi))


def op_rs(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return t_map(source, xi)


def op_ri(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return t_map(gamma_trace(source), xi)


def op_rr(source: np.ndarray, xi: np.ndarray) -> np.ndarray:
    return q_map(source, xi)


# Block label: (source sector, target sector, intrinsic primitive).
block_operators: dict[str, tuple[str, str, BlockOperator]] = {
    "SS": ("S", "S", op_ss),
    "SI": ("I", "S", op_si),
    "SR": ("R", "S", op_sr),
    "IS": ("S", "I", op_is),
    "II": ("I", "I", op_ii),
    "IR": ("R", "I", op_ir),
    "RS": ("S", "R", op_rs),
    "RI": ("I", "R", op_ri),
    "RR": ("R", "R", op_rr),
}

base_xi = np.zeros(14, dtype=complex)
base_xi[:4] = np.array([1.0, 2.0, 3.0, 5.0])
base_xi /= np.linalg.norm(base_xi)
fibre_xi = np.zeros(14, dtype=complex)
fibre_xi[4:] = np.array([1.0, 2.0, 4.0, 7.0, 11.0, 16.0, 22.0, 29.0, 37.0, 46.0])
fibre_xi /= np.linalg.norm(fibre_xi)

rng = np.random.default_rng(20260730)
witnesses: dict[str, np.ndarray] = {}
for slot in slots:
    coordinates = (
        rng.standard_normal((slot.dimension, WITNESSES))
        + 1j * rng.standard_normal((slot.dimension, WITNESSES))
    )
    coordinates, _triangular = np.linalg.qr(coordinates)
    witnesses[slot.name] = slot.basis @ coordinates[:, :WITNESSES]


def compute_block_support(
    source_sector: str,
    target_sector: str,
    operator: BlockOperator,
    xi: np.ndarray,
) -> tuple[set[Cell], dict[Cell, float]]:
    support: set[Cell] = set()
    amplitudes: dict[Cell, float] = {}
    for source_slot in slots_by_sector[source_sector]:
        output = operator(witnesses[source_slot.name], xi)
        output_norm = max(1.0, float(np.linalg.norm(output)))
        for target_slot in slots_by_sector[target_sector]:
            projection = target_slot.basis.conj().T @ output
            amplitude = float(np.linalg.norm(projection)) / output_norm
            cell = (source_slot.name, target_slot.name)
            amplitudes[cell] = amplitude
            if amplitude > TOL:
                support.add(cell)
    return support, amplitudes


constructed_support: dict[tuple[str, str], set[Cell]] = {}
constructed_amplitudes: dict[tuple[str, str], dict[Cell, float]] = {}
for branch, xi in (("base", base_xi), ("fibre", fibre_xi)):
    for block_name, (source_sector, target_sector, operator) in block_operators.items():
        support, amplitudes = compute_block_support(
            source_sector, target_sector, operator, xi
        )
        constructed_support[(branch, block_name)] = support
        constructed_amplitudes[(branch, block_name)] = amplitudes

constructed_base = set().union(
    *(constructed_support[("base", block)] for block in block_operators)
)
constructed_fibre = set().union(
    *(constructed_support[("fibre", block)] for block in block_operators)
)
constructed_full = constructed_base | constructed_fibre

info(
    "constructed supports before held-out import: "
    f"base={len(constructed_base)}, fibre={len(constructed_fibre)}, "
    f"union={len(constructed_full)}"
)
info(
    "constructed per-block union counts: "
    + str(
        {
            block: len(
                constructed_support[("base", block)]
                | constructed_support[("fibre", block)]
            )
            for block in block_operators
        }
    )
)


# ---------------------------------------------------------------------------
# C. Held-out comparison.  Only now import the independent exact ledger.
# ---------------------------------------------------------------------------
print("\nC. Open the held-out exact representation ledger")

HERE = os.path.dirname(os.path.abspath(__file__))
TESTS_ROOT = os.path.abspath(os.path.join(HERE, ".."))
if TESTS_ROOT not in sys.path:
    sys.path.insert(0, TESTS_ROOT)

import shiab_b5_krein_mirror_orbit_reduction as heldout_reduction  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as heldout_ledger  # noqa: E402


def sector_from_name(name: str) -> str:
    if name.startswith("S:"):
        return "S"
    if name.startswith("imGamma:"):
        return "I"
    if name.startswith(("kerGamma:", "X:")):
        return "R"
    raise ValueError(f"unknown observer slot {name}")


def heldout_parts(cell: Cell) -> tuple[int, int]:
    source_name, target_name = cell
    source = heldout_ledger.TYPES[
        heldout_ledger.SLOT_BY_NAME[source_name].h_type
    ]
    target = heldout_ledger.TYPES[
        heldout_ledger.SLOT_BY_NAME[target_name].h_type
    ]
    base_part = int(
        source.d5_weight == target.d5_weight
        and target.left_dim
        in heldout_ledger.su2_vector_targets(source.left_dim)
        and target.right_dim
        in heldout_ledger.su2_vector_targets(source.right_dim)
    )
    fibre_part = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * heldout_ledger.vector_tensor_decomposition(source.d5_weight).get(
        target.d5_weight, 0
    )
    return base_part, fibre_part


heldout_allowed = heldout_reduction.nonzero_cells()
heldout_base = {
    cell for cell in heldout_allowed if heldout_parts(cell) == (1, 0)
}
heldout_fibre = {
    cell for cell in heldout_allowed if heldout_parts(cell) == (0, 1)
}

check(
    "independently constructed labels and dimensions match the frozen ledger",
    set(slot_by_name) == set(heldout_ledger.SLOT_BY_NAME)
    and all(
        slot_by_name[name].dimension
        == heldout_ledger.SLOT_BY_NAME[name].dimension
        for name in slot_by_name
    ),
)
check(
    "held-out envelope is 136 = 68 base + 68 fibre",
    len(heldout_allowed) == 136
    and len(heldout_base) == len(heldout_fibre) == 68
    and heldout_base.isdisjoint(heldout_fibre),
)

for block_name, (source_sector, target_sector, _operator) in block_operators.items():
    expected = {
        cell
        for cell in heldout_allowed
        if sector_from_name(cell[0]) == source_sector
        and sector_from_name(cell[1]) == target_sector
    }
    expected_base = expected & heldout_base
    expected_fibre = expected & heldout_fibre
    observed_base = constructed_support[("base", block_name)]
    observed_fibre = constructed_support[("fibre", block_name)]
    check(
        f"{block_name}: coordinate base support equals held-out sector envelope",
        observed_base == expected_base,
        f"{len(observed_base)}/{len(expected_base)} cells",
    )
    check(
        f"{block_name}: coordinate fibre support equals held-out sector envelope",
        observed_fibre == expected_fibre,
        f"{len(observed_fibre)}/{len(expected_fibre)} cells",
    )

check(
    "all nine coordinate formulas reproduce exactly all 136 held-out cells",
    constructed_base == heldout_base
    and constructed_fibre == heldout_fibre
    and constructed_full == heldout_allowed,
)

# Audit the generic-witness inference with the ledger now visible.
nonzero_amplitudes: list[float] = []
zero_amplitudes: list[float] = []
for branch, expected_branch in (
    ("base", heldout_base),
    ("fibre", heldout_fibre),
):
    for block_name in block_operators:
        amplitudes = constructed_amplitudes[(branch, block_name)]
        for cell, amplitude in amplitudes.items():
            if cell in expected_branch:
                nonzero_amplitudes.append(amplitude)
            else:
                zero_amplitudes.append(amplitude)

min_nonzero = min(nonzero_amplitudes)
max_zero = max(zero_amplitudes)
gap_ratio = min_nonzero / max(max_zero, np.finfo(float).tiny)
check(
    "generic coordinate witnesses have a decisive zero/nonzero gap",
    min_nonzero > 1.0e-4
    and max_zero < 1.0e-10
    and gap_ratio > 1.0e6,
    (
        f"min nonzero={min_nonzero:.2e}, max zero={max_zero:.2e}, "
        f"gap={gap_ratio:.2e}"
    ),
)


# ---------------------------------------------------------------------------
# D. Hostile/planted controls.
# ---------------------------------------------------------------------------
print("\nD. Hostile controls")

x_names = {slot.name for slot in slots if slot.name.startswith("X:")}
without_x = {
    cell
    for cell in constructed_full
    if cell[0] not in x_names and cell[1] not in x_names
}
check(
    "omitting the X family destroys full support and slot coverage",
    len(without_x) < len(constructed_full)
    and {
        endpoint for cell in without_x for endpoint in cell
    }
    != set(slot_by_name),
)

plus_names = {
    "S:E+:L16+",
    "S:E+:R16-",
    "imGamma:E+:L16+",
    "imGamma:E+:R16-",
    "kerGamma:E+:L16+",
    "kerGamma:E+:R16-",
    "X:X32p",
    "X:X23m",
    "X:X2Tp",
    "X:X1Tm",
}
one_chirality = {
    cell
    for cell in constructed_full
    if cell[0] in plus_names and cell[1] in plus_names
}
check(
    "preprojecting to one total chirality loses the full-20 result",
    one_chirality != constructed_full
    and {
        endpoint for cell in one_chirality for endpoint in cell
    }
    <= plus_names,
)

q_base = constructed_support[("base", "RR")]
q_fibre = constructed_support[("fibre", "RR")]
check(
    "base-only and fibre-only Q are distinct 20-cell halves, not the full Q",
    len(q_base) == len(q_fibre) == 20
    and q_base.isdisjoint(q_fibre)
    and len(q_base | q_fibre) == 40,
)


def collapse_provenance(name: str) -> str:
    if name.startswith(("S:", "imGamma:", "kerGamma:")):
        return "E:" + name.split(":", 1)[1]
    return name


collapsed = {
    (collapse_provenance(source), collapse_provenance(target))
    for source, target in constructed_full
}
check(
    "collapsing S/imGamma/low-R provenance changes the manifest",
    len(collapsed) < len(constructed_full),
)

victim = min(constructed_full)
deleted = set(constructed_full)
deleted.remove(victim)
check(
    "deleting one planted coordinate cell fails exact held-out equality",
    deleted != heldout_allowed and constructed_full == heldout_allowed,
    f"deleted {victim}",
)

try:
    _unknown = slot_by_name["S"]
except KeyError:
    unknown_rejected = True
else:
    unknown_rejected = False
check(
    "formula-blind single-character label is rejected by typed slot lookup",
    unknown_rejected,
)

# A zero primitive is a direct planted matcher test: names and sector types are
# all still present, but coordinate projections must return the empty support.
def zero_ss(source: np.ndarray, _xi: np.ndarray) -> np.ndarray:
    return np.zeros_like(source)


zero_support, zero_amplitudes_map = compute_block_support(
    "S", "S", zero_ss, base_xi
)
check(
    "zero-formula planted control yields no support despite valid labels",
    not zero_support
    and max(zero_amplitudes_map.values(), default=0.0) == 0.0,
)


print("\n" + "=" * 92)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    sys.exit(1)

print("VERDICT: OBSERVER-COMPLEX-20-EMBEDDING-SUPPORT-REDERIVED")
print("=" * 92)
print(
    "\nThe factorized complex Clifford construction independently builds all twenty\n"
    "provenance-labelled thin embeddings and recomputes all nine written block\n"
    "supports.  For generic base and symmetric-fibre covectors it reproduces the\n"
    "held-out exact ledger cell-for-cell: 68 base + 68 fibre = 136.  The result\n"
    "survives omission, chirality, provenance, deleted-cell, zero-formula, and\n"
    "wrong-low-embedding controls, with a large numerical zero/nonzero gap.\n"
    "\nThis upgrades the prior hand-entered analytic manifest to an independent\n"
    "observer-complex coordinate rederivation.  It does NOT construct native\n"
    "Krein-normalized physical projectors, associated-bundle transport around\n"
    "the DeWitt loop, a formal adjoint/Green packet, a closed domain, a Noether\n"
    "identity, BV nilpotency, cohomology, or a generation count."
)
