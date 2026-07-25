#!/usr/bin/env python3
"""Finite spectral stress tests for standard OS reflection positivity.

For positive Euclidean times t_i, this script constructs

    K_ij = sum_a w_a exp(-omega_a (t_i+t_j)) / (2 omega_a).

Positive spectral weights make K a positive sum of rank-one Gram matrices.
Seeded finite tests stress that prediction, while a planted signed spectral
measure supplies a negative control.  The reflection geometry is then held
fixed while the spectral data change, demonstrating that a bare reflection
matrix does not determine positivity without covariance/action data.

MANDATORY GU FORK GUARD
-----------------------
These are standard OS controls, not a GU transfer.  Standard OS positivity
constructs a positive Hilbert space, not the GU Krein physical quotient.  A
signature real slice is not the GU 192/384 carrier without a typed map.  The
determinant Minkowski metric is not the gimmel/DeWitt metric.  Nothing here
proves GU soldering, gauge dynamics, or physicality.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

try:
    import numpy as np
except ModuleNotFoundError:
    np = None  # type: ignore[assignment]


RANDOM_SEED = 20260725


@dataclass(frozen=True)
class SpectralReport:
    hermitian: bool
    positive_semidefinite: bool
    rank: int
    positive_index: int
    negative_index: int
    dimension: int
    minimum_eigenvalue: float
    maximum_eigenvalue: float
    tolerance: float


def os_kernel(times, frequencies, weights):
    """Construct the finite reflected two-point kernel."""

    decay = np.exp(-np.outer(times, frequencies))
    coefficients = weights / (2.0 * frequencies)
    return (decay * coefficients) @ decay.conj().T


def spectral_report(matrix) -> SpectralReport:
    hermitian_residual = float(np.max(np.abs(matrix - matrix.conj().T)))
    hermitian_part = (matrix + matrix.conj().T) / 2.0
    eigenvalues = np.linalg.eigvalsh(hermitian_part)
    # Use a matrix-relative threshold.  An absolute floor at 1 would make the
    # positivity and rank verdict change under harmless rescaling and could
    # hide a small but genuinely negative spectral direction.
    scale = max(
        float(np.max(np.abs(eigenvalues))),
        float(np.finfo(float).tiny),
    )
    tolerance = 256.0 * matrix.shape[0] * np.finfo(float).eps * scale
    rank = int(np.count_nonzero(np.abs(eigenvalues) > tolerance))
    positive_index = int(np.count_nonzero(eigenvalues > tolerance))
    negative_index = int(np.count_nonzero(eigenvalues < -tolerance))
    return SpectralReport(
        hermitian=hermitian_residual <= tolerance,
        positive_semidefinite=float(eigenvalues[0]) >= -tolerance,
        rank=rank,
        positive_index=positive_index,
        negative_index=negative_index,
        dimension=matrix.shape[0],
        minimum_eigenvalue=float(eigenvalues[0]),
        maximum_eigenvalue=float(eigenvalues[-1]),
        tolerance=tolerance,
    )


def reflection_geometry(positive_times):
    """Return a doubled time set and the permutation implementing t -> -t."""

    full_times = np.concatenate((-positive_times[::-1], positive_times))
    reflection = np.fliplr(np.eye(full_times.size))
    return full_times, reflection


def check(name: str, condition: bool, detail: str) -> bool:
    print(f"[{'PASS' if condition else 'FAIL'}] {name}: {detail}")
    return condition


def main() -> int:
    if np is None:
        print(
            "[FAIL] NumPy dependency missing: install NumPy to run the "
            "finite spectral/reflection-positivity stress test.",
            file=sys.stderr,
        )
        return 2

    times = np.array([0.2, 0.55, 1.1, 1.9, 2.8], dtype=float)
    frequencies = np.array([0.45, 1.3, 3.1], dtype=float)
    positive_weights = np.array([1.5, 0.7, 2.2], dtype=float)
    deterministic_kernel = os_kernel(times, frequencies, positive_weights)
    deterministic_report = spectral_report(deterministic_kernel)
    single_mode_report = spectral_report(
        os_kernel(times, frequencies[:1], positive_weights[:1])
    )

    rng = np.random.default_rng(RANDOM_SEED)
    random_reports: list[SpectralReport] = []
    random_rank_bounds: list[int] = []
    for _ in range(16):
        dimension = int(rng.integers(3, 9))
        mode_count = int(rng.integers(1, 9))
        planted_times = np.sort(rng.uniform(0.03, 3.5, size=dimension))
        planted_frequencies = np.sort(rng.uniform(0.08, 4.5, size=mode_count))
        planted_weights = rng.lognormal(mean=0.0, sigma=0.9, size=mode_count)
        report = spectral_report(
            os_kernel(planted_times, planted_frequencies, planted_weights)
        )
        random_reports.append(report)
        random_rank_bounds.append(min(dimension, mode_count))

    # Hold both times and frequencies fixed.  Replacing one positive spectral
    # weight by a sufficiently negative weight makes the reflected kernel
    # indefinite.  The negative trace already forces a negative eigenvalue;
    # eigvalsh supplies a quantitative finite witness.
    contrast_times = np.array([0.15, 0.5, 1.0, 1.7], dtype=float)
    contrast_frequencies = np.array([0.55, 2.2], dtype=float)
    contrast_positive_weights = np.array([1.0, 0.8], dtype=float)
    contrast_signed_weights = np.array([1.0, -40.0], dtype=float)
    positive_contrast_matrix = os_kernel(
        contrast_times,
        contrast_frequencies,
        contrast_positive_weights,
    )
    positive_contrast = spectral_report(positive_contrast_matrix)
    signed_kernel = os_kernel(
        contrast_times,
        contrast_frequencies,
        contrast_signed_weights,
    )
    signed_contrast = spectral_report(signed_kernel)
    scale_factor = 1.0e-15
    scaled_positive_contrast = spectral_report(scale_factor * positive_contrast_matrix)
    scaled_signed_contrast = spectral_report(scale_factor * signed_kernel)

    full_times, reflection = reflection_geometry(contrast_times)
    reflected_times = reflection @ full_times
    reflection_is_fixed = (
        np.array_equal(reflected_times, -full_times)
        and np.array_equal(reflection @ reflection, np.eye(full_times.size))
        and np.array_equal(reflection.conj().T @ reflection, np.eye(full_times.size))
    )

    all_random_psd = all(
        report.hermitian
        and report.positive_semidefinite
        and report.rank <= rank_bound
        for report, rank_bound in zip(random_reports, random_rank_bounds)
    )
    random_minimum = min(report.minimum_eigenvalue for report in random_reports)
    random_largest_tolerance = max(report.tolerance for report in random_reports)
    observed_ranks = sorted({report.rank for report in random_reports})

    checks = [
        check(
            "deterministic positive spectral kernel",
            deterministic_report.hermitian
            and deterministic_report.positive_semidefinite
            and deterministic_report.rank == len(frequencies),
            (
                f"rank={deterministic_report.rank}/{deterministic_report.dimension}, "
                f"lambda_min={deterministic_report.minimum_eigenvalue:.3e}, "
                f"tol={deterministic_report.tolerance:.3e}"
            ),
        ),
        check(
            "finite OS quotient rank depends on spectral data",
            single_mode_report.positive_semidefinite
            and single_mode_report.rank == 1
            and deterministic_report.rank == 3,
            (
                "same positive-time geometry gives quotient ranks "
                f"{single_mode_report.rank} and {deterministic_report.rank} "
                "for one versus three positive spectral atoms"
            ),
        ),
        check(
            "seeded-random positive spectra",
            all_random_psd,
            (
                f"seed={RANDOM_SEED}, trials={len(random_reports)}, "
                f"ranks={observed_ranks}, worst_lambda_min={random_minimum:.3e}, "
                f"max_tol={random_largest_tolerance:.3e}"
            ),
        ),
        check(
            "planted negative spectral weight",
            signed_contrast.hermitian
            and signed_contrast.negative_index >= 1
            and signed_contrast.minimum_eigenvalue
            < -10.0 * signed_contrast.tolerance,
            (
                f"weight=-40 gives lambda_min="
                f"{signed_contrast.minimum_eigenvalue:.3e}, "
                f"tol={signed_contrast.tolerance:.3e}, "
                f"inertia=(+{signed_contrast.positive_index},"
                f"-{signed_contrast.negative_index})"
            ),
        ),
        check(
            "spectral classification is scale covariant",
            scaled_positive_contrast.positive_semidefinite
            and scaled_positive_contrast.rank == positive_contrast.rank
            and not scaled_signed_contrast.positive_semidefinite
            and scaled_signed_contrast.rank == signed_contrast.rank
            and scaled_signed_contrast.positive_index
            == signed_contrast.positive_index
            and scaled_signed_contrast.negative_index
            == signed_contrast.negative_index,
            (
                f"rescaling by {scale_factor:.0e} preserves positive ranks "
                f"{positive_contrast.rank}/{scaled_positive_contrast.rank} "
                "and signed negativity "
                f"{signed_contrast.minimum_eigenvalue:.3e}/"
                f"{scaled_signed_contrast.minimum_eigenvalue:.3e}"
            ),
        ),
        check(
            "reflection matrix alone does not determine positivity",
            reflection_is_fixed
            and positive_contrast.positive_semidefinite
            and not signed_contrast.positive_semidefinite,
            (
                "same t->-t involution and frequencies: positive weights give "
                f"lambda_min={positive_contrast.minimum_eigenvalue:.3e}; "
                "signed weights give "
                f"lambda_min={signed_contrast.minimum_eigenvalue:.3e}"
            ),
        ),
    ]

    print()
    print("GU fork guard:")
    print("  STANDARD CONTROL ONLY: no GU transfer is proved here.")
    print("  Standard OS positive Hilbert space is not the GU Krein physical quotient.")
    print("  Signature real slices are not the GU 192/384 carrier without a typed map.")
    print("  The determinant Minkowski metric is not the gimmel/DeWitt metric.")
    print("  No check proves GU soldering, gauge dynamics, or physicality.")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
