#!/usr/bin/env python3
"""Minimal counterexample to a construction-wide scattering pairing claim.

This probe is deliberately source-independent.  It keeps the exact algebraic
scaffold used by ``operator_grade_face_probe.py``:

* doubled generator ``A = -sigma1 (x) H - E i sigma2 (x) I``;
* native Krein current ``X = sigma2 (x) K``;
* kinematic mover split by the sign of ``Im spectrum(A)``;
* absolute-flux channel normalization; and
* the same left-incidence scattering solve.

The internal matrices are otherwise generic deterministic K-self-adjoint
matrices ``H = K G`` with ``G`` Hermitian.  Hence ``A^dag X + X A = 0`` is an
exact positive control.  If the doubled/Krein/channel construction itself
forced

    Tr(t^dag E_R t) = 0

or an exactly +/- paired spectrum for ``Q = t^dag E_R t``, those properties
would survive these cases.  They do not.  A PASS therefore means the claimed
construction-wide identity is falsified; it says nothing against an additional
symmetry that may exist in the frozen 128-dimensional Clifford fixture.

Deterministic; numpy + scipy only; no repository model imports.
"""
from __future__ import annotations

import sys

import numpy as np
from scipy.linalg import expm


S1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
S2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)

CURRENT_TOL = 1.0e-12
INVOLUTION_TOL = 1.0e-10
COUNTEREXAMPLE_FLOOR = 1.0e-3


def hermitian_sample(rng: np.random.Generator, n: int) -> np.ndarray:
    raw = rng.standard_normal((n, n)) + 1.0j * rng.standard_normal((n, n))
    return 0.5 * (raw + raw.conj().T)


def modes(generator: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Match modes_gen: spectral projectors, then orthonormal range bases."""
    ident = np.eye(2 * n, dtype=complex)
    eigenvalues, eigenvectors = np.linalg.eig(generator)
    inverse = np.linalg.inv(eigenvectors)
    plus = np.imag(eigenvalues) > 0.0
    if int(np.sum(plus)) != n:
        raise RuntimeError(
            f"kinematic split has {int(np.sum(plus))} plus modes, expected {n}"
        )
    projector = eigenvectors[:, plus] @ inverse[plus, :]
    basis_plus = np.linalg.svd(projector)[0][:, :n]
    basis_minus = np.linalg.svd(ident - projector)[0][:, :n]
    return basis_plus, basis_minus


def channels(basis: np.ndarray, current: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Match chan: normalize by absolute flux and retain its sign grading."""
    gram = basis.conj().T @ current @ basis
    gram = 0.5 * (gram + gram.conj().T)
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    if float(np.min(np.abs(eigenvalues))) < 1.0e-8:
        raise RuntimeError("flux Gram is numerically degenerate")
    inverse_sqrt = (
        eigenvectors
        @ np.diag(1.0 / np.sqrt(np.abs(eigenvalues)))
        @ eigenvectors.conj().T
    )
    channel_basis = basis @ inverse_sqrt
    grading = channel_basis.conj().T @ current @ channel_basis
    grading = 0.5 * (grading + grading.conj().T)
    return channel_basis, grading


def run_case(n: int, seed: int) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    half = n // 2
    krein = np.diag([1.0] * half + [-1.0] * half).astype(complex)
    ident_n = np.eye(n, dtype=complex)
    ident_2n = np.eye(2 * n, dtype=complex)
    current = np.kron(S2, krein)
    gamma = 1.0j * np.kron(S2, ident_n)
    energy = 20.0

    def internal() -> np.ndarray:
        # H^dag K = K H exactly up to floating arithmetic.
        return krein @ hermitian_sample(rng, n)

    def generator(hmat: np.ndarray) -> np.ndarray:
        return -np.kron(S1, hmat) - energy * gamma

    h_left = internal()
    h_right = internal()
    h_segments = [internal() for _ in range(5)]

    transfer = ident_2n.copy()
    current_defect = 0.0
    for hmat in h_segments:
        amat = generator(hmat)
        current_defect = max(
            current_defect,
            float(np.max(np.abs(amat.conj().T @ current + current @ amat))),
        )
        transfer = expm(0.05 * amat) @ transfer

    left_plus, left_minus = modes(generator(h_left), n)
    right_plus, _right_minus = modes(generator(h_right), n)
    channel_left_plus, grading_left_plus = channels(left_plus, current)
    channel_left_minus, _grading_left_minus = channels(left_minus, current)
    channel_right_plus, grading_right_plus = channels(right_plus, current)

    solution = np.linalg.solve(
        np.hstack([channel_right_plus, -transfer @ channel_left_minus]),
        transfer @ channel_left_plus,
    )
    transmission = solution[:n, :]
    qmat = transmission.conj().T @ grading_right_plus @ transmission
    qmat = 0.5 * (qmat + qmat.conj().T)

    eigenvalues, eigenvectors = np.linalg.eigh(qmat)
    order = np.argsort(eigenvalues)
    values = eigenvalues[order]
    vectors = eigenvectors[:, order]
    pair_defect = float(np.max(np.abs(values + values[::-1])))

    # This is the exact post-hoc construction used by the 128-dimensional
    # probe.  It anticommutes only when the spectrum was already +/- paired.
    reversal = np.fliplr(np.eye(n, dtype=complex))
    sigma = vectors @ reversal @ vectors.conj().T
    sigma_involution_defect = float(
        np.max(np.abs(sigma @ sigma - np.eye(n, dtype=complex)))
    )
    sigma_anticommutator_defect = float(
        np.max(np.abs(sigma @ qmat @ sigma + qmat))
    )

    grading_defect = float(
        np.max(
            np.abs(
                grading_right_plus @ grading_right_plus
                - np.eye(n, dtype=complex)
            )
        )
    )
    grading_trace = float(abs(np.trace(grading_right_plus)))

    return {
        "current_defect": current_defect,
        "grading_defect": grading_defect,
        "grading_trace": grading_trace,
        "trace_q": float(abs(np.trace(qmat))),
        "pair_defect": pair_defect,
        "sigma_involution_defect": sigma_involution_defect,
        "sigma_anticommutator_defect": sigma_anticommutator_defect,
    }


def main() -> int:
    cases = ((2, 7), (2, 19), (4, 31))
    all_pass = True
    print("=== OPERATOR-GRADE SIGMA COUNTEREXAMPLE ===")
    for n, seed in cases:
        result = run_case(n, seed)
        controls = (
            result["current_defect"] < CURRENT_TOL
            and result["grading_defect"] < INVOLUTION_TOL
            and result["grading_trace"] < INVOLUTION_TOL
            and result["sigma_involution_defect"] < INVOLUTION_TOL
        )
        counterexample = (
            result["trace_q"] > COUNTEREXAMPLE_FLOOR
            and result["pair_defect"] > COUNTEREXAMPLE_FLOOR
            and result["sigma_anticommutator_defect"] > COUNTEREXAMPLE_FLOOR
        )
        passed = controls and counterexample
        all_pass &= passed
        print(
            f"[{'PASS' if passed else 'FAIL'}] n={n} seed={seed}: "
            f"current={result['current_defect']:.2e} "
            f"E^2-I={result['grading_defect']:.2e} "
            f"|Tr E|={result['grading_trace']:.2e} |Tr Q|={result['trace_q']:.6f} "
            f"pair={result['pair_defect']:.6f} "
            f"posthoc-sigma-anti={result['sigma_anticommutator_defect']:.6f}"
        )

    if all_pass:
        print(
            "OUTCOME: SIG-IDENTITY-ARTIFACT -- the general graded-scattering "
            "scaffold preserves the Krein current but does not force trace "
            "zero, +/- pairing, or a post-hoc anticommuting sigma."
        )
        return 0
    print("OUTCOME: CONTROL OR COUNTEREXAMPLE FAILURE")
    return 1


if __name__ == "__main__":
    sys.exit(main())
