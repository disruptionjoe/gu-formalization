#!/usr/bin/env python3
"""Finite-dimensional Cl(4,0) RS gamma-trace/projector model.

This is a concrete matrix sanity check for the K3 pulled-back
Rarita-Schwinger symbol pieces.  It deliberately computes only raw complex
finite-dimensional ranks.  It does not compute a K-theory symbol class, an
Atiyah-Singer/APS index, or the GU generation count.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import json
import math
import sys
from typing import Iterable, Sequence

import numpy as np


TOL = 1.0e-10
INTERNAL_RANK_C = 16
SAMPLE_XI = (1.0, 2.0, 3.0, 4.0)


Matrix = np.ndarray


@dataclass(frozen=True)
class RawRankSummary:
    base_vector_spinor_dim_C: int
    base_gamma_trace_target_dim_C: int
    base_gamma_trace_rank_C: int
    base_kernel_rank_C: int
    internal_rank_C: int
    vector_spinor_dim_C: int
    gamma_trace_target_dim_C: int
    gamma_trace_rank_C: int
    gamma_trace_kernel_rank_C: int
    naive_kernel_rank_H_if_halvable: float
    internal_half_kernel_rank_C: int
    internal_half_naive_rank_H_if_halvable: float


@dataclass(frozen=True)
class ProjectorSummary:
    rank_C: int
    idempotent_error: float
    hermitian_error: float
    gamma_trace_error: float


@dataclass(frozen=True)
class RawSymbolSummary:
    xi: tuple[float, float, float, float]
    xi_norm: float
    base_restricted_shape: tuple[int, int]
    base_restricted_rank_C: int
    base_restricted_singular_values: tuple[float, ...]
    with_internal_rank_C: int
    with_internal_shape: tuple[int, int]
    projected_gauge_rank_C: int
    raw_symbol_on_projected_gauge_rank_C: int
    raw_symbol_on_projected_gauge_norm: float


def pauli_matrices() -> tuple[Matrix, Matrix, Matrix, Matrix]:
    ident = np.eye(2, dtype=complex)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=complex)
    return ident, sigma_1, sigma_2, sigma_3


def euclidean_gamma_matrices() -> list[Matrix]:
    """Return Hermitian 4x4 gamma matrices for Cl(4,0).

    gamma_1 = sigma_1 tensor sigma_1
    gamma_2 = sigma_1 tensor sigma_2
    gamma_3 = sigma_1 tensor sigma_3
    gamma_4 = sigma_2 tensor I

    Their product is diag(-1, -1, +1, +1), so the positive chiral
    subspace is spanned by the last two standard basis vectors.
    """

    ident, sigma_1, sigma_2, sigma_3 = pauli_matrices()
    return [
        np.kron(sigma_1, sigma_1),
        np.kron(sigma_1, sigma_2),
        np.kron(sigma_1, sigma_3),
        np.kron(sigma_2, ident),
    ]


def chirality(gammas: Sequence[Matrix]) -> Matrix:
    out = np.eye(gammas[0].shape[0], dtype=complex)
    for gamma in gammas:
        out = out @ gamma
    return out


def max_abs(matrix: Matrix) -> float:
    return float(np.max(np.abs(matrix)))


def matrix_rank(matrix: Matrix, tol: float = TOL) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def assert_close_matrix(left: Matrix, right: Matrix, label: str, tol: float = TOL) -> None:
    diff = max_abs(left - right)
    assert diff <= tol, f"{label}: max difference {diff:.3e} exceeds {tol:.3e}"


def assert_clifford_relations(gammas: Sequence[Matrix]) -> float:
    ident = np.eye(gammas[0].shape[0], dtype=complex)
    max_error = 0.0
    for i, gamma_i in enumerate(gammas):
        assert_close_matrix(gamma_i, gamma_i.conj().T, f"gamma_{i + 1} Hermitian")
        for j, gamma_j in enumerate(gammas):
            expected = 2.0 * ident if i == j else np.zeros_like(ident)
            error = max_abs(gamma_i @ gamma_j + gamma_j @ gamma_i - expected)
            max_error = max(max_error, error)
    assert max_error <= TOL, f"Clifford relation error {max_error:.3e}"
    return max_error


def chiral_bases() -> tuple[Matrix, Matrix]:
    """Return standard-basis isometries B_plus, B_minus for this gamma choice."""

    basis_plus = np.array(
        [
            [0, 0],
            [0, 0],
            [1, 0],
            [0, 1],
        ],
        dtype=complex,
    )
    basis_minus = np.array(
        [
            [1, 0],
            [0, 1],
            [0, 0],
            [0, 0],
        ],
        dtype=complex,
    )
    return basis_plus, basis_minus


def gamma_blocks(gammas: Sequence[Matrix]) -> tuple[list[Matrix], list[Matrix]]:
    basis_plus, basis_minus = chiral_bases()
    plus_to_minus = [basis_minus.conj().T @ gamma @ basis_plus for gamma in gammas]
    minus_to_plus = [basis_plus.conj().T @ gamma @ basis_minus for gamma in gammas]
    return plus_to_minus, minus_to_plus


def gamma_trace_map(blocks: Sequence[Matrix], internal_rank: int = 1) -> Matrix:
    """Build G: C^4 tensor S^pm tensor F -> S^mp tensor F."""

    ident_f = np.eye(internal_rank, dtype=complex)
    block_terms = [np.kron(block, ident_f) for block in blocks]
    return np.hstack(block_terms)


def kernel_projector(gamma_trace: Matrix) -> Matrix:
    """Orthogonal projector onto ker(gamma_trace)."""

    gram = gamma_trace @ gamma_trace.conj().T
    return np.eye(gamma_trace.shape[1], dtype=complex) - gamma_trace.conj().T @ np.linalg.inv(gram) @ gamma_trace


def projector_summary(projector: Matrix, gamma_trace: Matrix) -> ProjectorSummary:
    return ProjectorSummary(
        rank_C=matrix_rank(projector),
        idempotent_error=max_abs(projector @ projector - projector),
        hermitian_error=max_abs(projector - projector.conj().T),
        gamma_trace_error=max_abs(gamma_trace @ projector),
    )


def assert_projector_summary(summary: ProjectorSummary, expected_rank: int, label: str) -> None:
    assert summary.rank_C == expected_rank, f"{label}: rank {summary.rank_C} != {expected_rank}"
    assert summary.idempotent_error <= TOL, f"{label}: idempotent error {summary.idempotent_error:.3e}"
    assert summary.hermitian_error <= TOL, f"{label}: Hermitian error {summary.hermitian_error:.3e}"
    assert summary.gamma_trace_error <= TOL, f"{label}: gamma-trace error {summary.gamma_trace_error:.3e}"


def range_basis_from_projector(projector: Matrix) -> Matrix:
    hermitian_part = 0.5 * (projector + projector.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian_part)
    return eigenvectors[:, eigenvalues > 0.5]


def vector_spinor_symbol(block: Matrix, internal_rank: int = 1) -> Matrix:
    """Componentwise Clifford symbol on vector-spinors."""

    return np.kron(np.eye(4, dtype=complex), np.kron(block, np.eye(internal_rank, dtype=complex)))


def c_xi_block(blocks: Sequence[Matrix], xi: Sequence[float]) -> Matrix:
    out = np.zeros_like(blocks[0])
    for coefficient, block in zip(xi, blocks):
        out = out + coefficient * block
    return out


def gauge_symbol(xi: Sequence[float], spinor_rank: int, internal_rank: int = 1) -> Matrix:
    """Pointwise principal gauge map epsilon -> xi tensor epsilon."""

    ident = np.eye(spinor_rank * internal_rank, dtype=complex)
    return np.vstack([coefficient * ident for coefficient in xi])


def singular_values_desc(matrix: Matrix) -> tuple[float, ...]:
    values = np.linalg.svd(matrix, compute_uv=False)
    return tuple(float(value) for value in values)


def raw_symbol_summary(
    plus_to_minus: Sequence[Matrix],
    minus_to_plus: Sequence[Matrix],
    xi: Sequence[float],
    internal_rank: int,
) -> RawSymbolSummary:
    base_g_plus = gamma_trace_map(plus_to_minus)
    base_g_minus = gamma_trace_map(minus_to_plus)
    base_p_plus = kernel_projector(base_g_plus)
    base_p_minus = kernel_projector(base_g_minus)
    base_kernel_plus = range_basis_from_projector(base_p_plus)
    base_kernel_minus = range_basis_from_projector(base_p_minus)

    base_c_xi = c_xi_block(plus_to_minus, xi)
    base_symbol = base_p_minus @ vector_spinor_symbol(base_c_xi) @ base_p_plus
    base_restricted = base_kernel_minus.conj().T @ base_symbol @ base_kernel_plus
    base_rank = matrix_rank(base_restricted)
    assert base_rank == base_restricted.shape[0] == base_restricted.shape[1]

    full_g_plus = gamma_trace_map(plus_to_minus, internal_rank)
    full_g_minus = gamma_trace_map(minus_to_plus, internal_rank)
    full_p_plus = kernel_projector(full_g_plus)
    full_p_minus = kernel_projector(full_g_minus)
    full_kernel_plus = range_basis_from_projector(full_p_plus)
    full_kernel_minus = range_basis_from_projector(full_p_minus)
    full_c_xi = c_xi_block(plus_to_minus, xi)
    full_symbol = full_p_minus @ vector_spinor_symbol(full_c_xi, internal_rank) @ full_p_plus
    full_restricted = full_kernel_minus.conj().T @ full_symbol @ full_kernel_plus
    full_rank = matrix_rank(full_restricted)
    assert full_rank == full_restricted.shape[0] == full_restricted.shape[1]

    projected_gauge = full_p_plus @ gauge_symbol(xi, spinor_rank=2, internal_rank=internal_rank)
    symbol_on_projected_gauge = full_symbol @ projected_gauge

    return RawSymbolSummary(
        xi=tuple(float(value) for value in xi),
        xi_norm=float(math.sqrt(sum(value * value for value in xi))),
        base_restricted_shape=base_restricted.shape,
        base_restricted_rank_C=base_rank,
        base_restricted_singular_values=singular_values_desc(base_restricted),
        with_internal_rank_C=full_rank,
        with_internal_shape=full_restricted.shape,
        projected_gauge_rank_C=matrix_rank(projected_gauge),
        raw_symbol_on_projected_gauge_rank_C=matrix_rank(symbol_on_projected_gauge),
        raw_symbol_on_projected_gauge_norm=float(np.linalg.norm(symbol_on_projected_gauge)),
    )


def raw_rank_summary(plus_to_minus: Sequence[Matrix], internal_rank: int) -> RawRankSummary:
    base_g_plus = gamma_trace_map(plus_to_minus)
    full_g_plus = gamma_trace_map(plus_to_minus, internal_rank)
    base_rank = matrix_rank(base_g_plus)
    full_rank = matrix_rank(full_g_plus)
    base_kernel_rank = base_g_plus.shape[1] - base_rank
    full_kernel_rank = full_g_plus.shape[1] - full_rank
    internal_half_kernel_rank = base_kernel_rank * (internal_rank // 2)
    return RawRankSummary(
        base_vector_spinor_dim_C=base_g_plus.shape[1],
        base_gamma_trace_target_dim_C=base_g_plus.shape[0],
        base_gamma_trace_rank_C=base_rank,
        base_kernel_rank_C=base_kernel_rank,
        internal_rank_C=internal_rank,
        vector_spinor_dim_C=full_g_plus.shape[1],
        gamma_trace_target_dim_C=full_g_plus.shape[0],
        gamma_trace_rank_C=full_rank,
        gamma_trace_kernel_rank_C=full_kernel_rank,
        naive_kernel_rank_H_if_halvable=full_kernel_rank / 2.0,
        internal_half_kernel_rank_C=internal_half_kernel_rank,
        internal_half_naive_rank_H_if_halvable=internal_half_kernel_rank / 2.0,
    )


def rounded(values: Iterable[float], digits: int = 12) -> list[float]:
    return [round(value, digits) for value in values]


def compute_model(internal_rank: int = INTERNAL_RANK_C, xi: Sequence[float] = SAMPLE_XI) -> dict[str, object]:
    gammas = euclidean_gamma_matrices()
    clifford_error = assert_clifford_relations(gammas)
    chi = chirality(gammas)
    expected_chi = np.diag([-1, -1, 1, 1]).astype(complex)
    assert_close_matrix(chi, expected_chi, "chirality")
    assert_close_matrix(chi @ chi, np.eye(4, dtype=complex), "chirality square")
    for index, gamma in enumerate(gammas, start=1):
        assert_close_matrix(chi @ gamma + gamma @ chi, np.zeros((4, 4), dtype=complex), f"chirality anticommutes with gamma_{index}")

    plus_to_minus, minus_to_plus = gamma_blocks(gammas)
    base_g_plus = gamma_trace_map(plus_to_minus)
    base_g_minus = gamma_trace_map(minus_to_plus)
    full_g_plus = gamma_trace_map(plus_to_minus, internal_rank)
    full_g_minus = gamma_trace_map(minus_to_plus, internal_rank)

    base_p_plus = kernel_projector(base_g_plus)
    base_p_minus = kernel_projector(base_g_minus)
    full_p_plus = kernel_projector(full_g_plus)
    full_p_minus = kernel_projector(full_g_minus)

    base_projector_plus = projector_summary(base_p_plus, base_g_plus)
    base_projector_minus = projector_summary(base_p_minus, base_g_minus)
    full_projector_plus = projector_summary(full_p_plus, full_g_plus)
    full_projector_minus = projector_summary(full_p_minus, full_g_minus)

    assert_projector_summary(base_projector_plus, 6, "base P_+")
    assert_projector_summary(base_projector_minus, 6, "base P_-")
    assert_projector_summary(full_projector_plus, 6 * internal_rank, "P_+ tensor F")
    assert_projector_summary(full_projector_minus, 6 * internal_rank, "P_- tensor F")

    ranks = raw_rank_summary(plus_to_minus, internal_rank)
    raw_symbol = raw_symbol_summary(plus_to_minus, minus_to_plus, xi, internal_rank)

    return {
        "not_index_computation": True,
        "computed_object": "raw_complex_Cl4_gamma_trace_projectors_and_sample_projected_symbol",
        "clifford_relations_ok": True,
        "clifford_max_error": clifford_error,
        "chirality_matrix": [[int(round(value.real)) for value in row] for row in chi],
        "chirality_squared_ok": True,
        "spinor_ranks_C": {"S4": 4, "S4_plus": 2, "S4_minus": 2},
        "raw_rank_summary": ranks.__dict__,
        "projectors": {
            "base_P_plus": base_projector_plus.__dict__,
            "base_P_minus": base_projector_minus.__dict__,
            "with_F_P_plus": full_projector_plus.__dict__,
            "with_F_P_minus": full_projector_minus.__dict__,
        },
        "sample_raw_projected_symbol": {
            **raw_symbol.__dict__,
            "base_restricted_singular_values": rounded(raw_symbol.base_restricted_singular_values),
        },
        "rank_interpretation": {
            "candidate_A_effective_rank_H": 4,
            "candidate_B_effective_rank_H": 8,
            "raw_kernel_rank_C_with_F": ranks.gamma_trace_kernel_rank_C,
            "naive_H_halving_if_an_H_structure_were_verified": ranks.naive_kernel_rank_H_if_halvable,
            "why_not_decisive": (
                "The raw finite rank is the gamma-trace-free vector-spinor rank. "
                "The APS/GU gate needs a gauge-fixed elliptic symbol class and "
                "characteristic-class evaluation, not this raw rank."
            ),
        },
    }


def print_human(summary: dict[str, object]) -> None:
    ranks = summary["raw_rank_summary"]
    projectors = summary["projectors"]
    symbol = summary["sample_raw_projected_symbol"]
    interpretation = summary["rank_interpretation"]

    print("=" * 76)
    print("RS Cl(4,0) gamma-trace/projector finite model")
    print("=" * 76)
    print("Scope: raw complex finite-dimensional matrix ranks only; NOT a K-theory index.")
    print()
    print("Clifford sanity:")
    print(f"  Clifford relations ok: {summary['clifford_relations_ok']} (max error {summary['clifford_max_error']:.3e})")
    print(f"  chirality gamma_1...gamma_4 = {summary['chirality_matrix']}")
    print(f"  spinor ranks over C: {summary['spinor_ranks_C']}")
    print()
    print("Gamma-trace ranks:")
    print(
        "  base G_+: C^{base_vector_spinor_dim_C} -> C^{base_gamma_trace_target_dim_C}, "
        "rank_C={base_gamma_trace_rank_C}, ker_C={base_kernel_rank_C}".format(**ranks)
    )
    print(
        "  with F=C^{internal_rank_C}: C^{vector_spinor_dim_C} -> C^{gamma_trace_target_dim_C}, "
        "rank_C={gamma_trace_rank_C}, ker_C={gamma_trace_kernel_rank_C}".format(**ranks)
    )
    print(
        "  naive H-halving of ker_C={gamma_trace_kernel_rank_C} would be {naive_kernel_rank_H_if_halvable}; "
        "this is only a rank comparison, not an H-index certificate.".format(**ranks)
    )
    print(
        "  if an extra internal C^8 half is imposed externally: ker_C={internal_half_kernel_rank_C}, "
        "naive H={internal_half_naive_rank_H_if_halvable}; still raw, not effective rank.".format(**ranks)
    )
    print()
    print("Projector checks:")
    for label, data in projectors.items():
        print(
            f"  {label}: rank_C={data['rank_C']}, "
            f"P^2-P={data['idempotent_error']:.3e}, "
            f"P-P*={data['hermitian_error']:.3e}, "
            f"G P={data['gamma_trace_error']:.3e}"
        )
    print()
    print("Sample raw projected symbol:")
    print(f"  xi={symbol['xi']}, |xi|={symbol['xi_norm']:.12f}")
    print(
        f"  base ker-to-ker matrix shape={symbol['base_restricted_shape']}, "
        f"rank_C={symbol['base_restricted_rank_C']}"
    )
    print(f"  base singular values={symbol['base_restricted_singular_values']}")
    print(
        f"  with F matrix shape={symbol['with_internal_shape']}, "
        f"rank_C={symbol['with_internal_rank_C']}"
    )
    print(
        "  projected gauge image rank_C={projected_gauge_rank_C}; "
        "raw symbol on it rank_C={raw_symbol_on_projected_gauge_rank_C}, "
        "norm={raw_symbol_on_projected_gauge_norm:.12f}".format(**symbol)
    )
    print()
    print("Verdict:")
    print("  RAW_SYMBOL_ONLY / NOT_INDEX_COMPUTATION")
    print(
        "  candidate effective H-ranks are "
        f"{interpretation['candidate_A_effective_rank_H']} and {interpretation['candidate_B_effective_rank_H']}; "
        f"the computed raw ker_C is {interpretation['raw_kernel_rank_C_with_F']}."
    )
    print(f"  {interpretation['why_not_decisive']}")
    print("=" * 76)


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Compute explicit Cl(4,0) RS gamma-trace projectors and raw symbol ranks."
    )
    parser.add_argument("--json", action="store_true", help="Print the result summary as JSON.")
    args = parser.parse_args(argv)

    summary = compute_model()
    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print_human(summary)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except AssertionError as exc:
        print("=" * 76)
        print(f"FAIL: {exc}")
        print("=" * 76)
        raise SystemExit(1)
