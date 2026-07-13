"""Source-Noether/tau carrier attempt for the anchor-scale A-door.

The previous BV/Koszul-Tate packet showed that the projected gauge map

    A = Pi_ker(Gamma) d_A

closes the finite-fiber bicomplex.  This module asks the next question: can a
minimal source-level tau/Noether solve derive that projected map instead of
assuming it?

The bounded answer here is conservative.  A finite-fiber KKT/Schur-complement
tau multiplier does derive the projection, but it derives exactly the fixed
orthogonal projector and leaves arbitrary tangent additions in ker(Gamma)
unselected.  That is useful progress, not a source-action proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import sys

import numpy as np


SOURCE_ROOT = Path(__file__).resolve().parents[1]
if str(SOURCE_ROOT) not in sys.path:
    sys.path.insert(0, str(SOURCE_ROOT))

from lib import gu_bridge  # noqa: E402


ANCHOR_BARE_COMMUTATOR = 58.7215
ANCHOR_C2 = 155.3625
TOL = 1.0e-8


class SourceNoetherTauVerdict(str, Enum):
    """Outcome labels for the source-Noether/tau attempt."""

    TAU_SCHUR_PROJECTOR_ONLY_DERIVATIVE_TAU_BLOCKED = (
        "tau_schur_projector_only_derivative_tau_blocked"
    )
    FAILS = "fails"


@dataclass(frozen=True)
class SourceNoetherTauReport:
    """Machine-checkable report for the source-Noether/tau carrier attempt."""

    verdict: SourceNoetherTauVerdict
    right_inverse_residual: float
    kkt_stationarity_residual: float
    tau_noether_residual: float
    projector_identity_residual: float
    correction_normal_residual: float
    raw_noether_rank: int
    tau_multiplier_rank: int
    corrected_gauge_rank: int
    tangent_perturbation_noether_residual: float
    tangent_perturbation_difference_norm: float
    free_tangent_column_dim: int
    free_tangent_matrix_dim: int
    null_raw_noether_rank: int
    null_tau_multiplier_rank: int
    null_corrected_gauge_rank: int
    bare_commutator_norm: float
    c2_norm: float
    source_derived_independent_tau: bool
    next_progress_point: str

    @property
    def finite_fiber_tau_derives_projection(self) -> bool:
        return (
            self.right_inverse_residual < TOL
            and self.kkt_stationarity_residual < TOL
            and self.tau_noether_residual < TOL
            and self.projector_identity_residual < TOL
            and self.correction_normal_residual < TOL
        )

    @property
    def noether_leaves_tangent_freedom(self) -> bool:
        return (
            self.tangent_perturbation_noether_residual < TOL
            and self.tangent_perturbation_difference_norm > 1.0
            and self.free_tangent_matrix_dim > 0
        )


def _rank(matrix: np.ndarray, tol: float = 1.0e-8) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def _vector_spinor_injection(direction: np.ndarray, spin_dim: int) -> np.ndarray:
    """Return spinor -> vector-spinor injection psi |-> direction tensor psi."""

    vector_dim = int(direction.shape[0])
    injection = np.zeros((vector_dim * spin_dim, spin_dim), dtype=complex)
    for vector_index, coeff in enumerate(direction):
        start = vector_index * spin_dim
        injection[start : start + spin_dim, :] = coeff * np.eye(spin_dim)
    return injection


def _tau_schur_solve(
    gamma_trace: np.ndarray,
    pi_rs: np.ndarray,
    raw_gauge: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Solve the finite-fiber KKT system for the minimal tau correction.

    This is the Schur complement of

        minimize ||A - d_A||^2 subject to Gamma A = 0.

    The multiplier is forced to ``(Gamma Gamma^dagger)^-1 Gamma d_A`` and the
    corrected map is exactly the orthogonal projection ``Pi_ker(Gamma) d_A``.
    """

    gamma_dagger = gamma_trace.conj().T
    gamma_gamma_dagger = gamma_trace @ gamma_dagger
    multiplier = np.linalg.solve(gamma_gamma_dagger, gamma_trace @ raw_gauge)
    normal_correction = gamma_dagger @ multiplier
    corrected_gauge = raw_gauge - normal_correction
    right_inverse = gamma_dagger @ np.linalg.inv(gamma_gamma_dagger)

    # Guard the caller's projector against drift: the KKT result should match it.
    projected = pi_rs @ raw_gauge
    if np.linalg.norm(corrected_gauge - projected) > 1.0e-6:
        raise RuntimeError("tau Schur solve no longer matches Pi_ker(Gamma) d_A")

    return multiplier, normal_correction, corrected_gauge, right_inverse


def run_source_noether_tau_carrier(
    xi: np.ndarray | None = None,
) -> SourceNoetherTauReport:
    """Run the finite-fiber source-Noether/tau carrier attempt."""

    _e, gamma_trace, pi_rs, mass_operator = gu_bridge.constraint_objects()
    spin_dim = gu_bridge.DIM
    vector_dim = gu_bridge.N
    total_dim = vector_dim * spin_dim

    if xi is None:
        xi = np.asarray(gu_bridge.XI, dtype=complex)
    else:
        xi = np.asarray(xi, dtype=complex)
    if xi.shape != (vector_dim,):
        raise ValueError(f"xi must have shape ({vector_dim},), got {xi.shape}")

    raw_gauge = _vector_spinor_injection(xi, spin_dim)
    multiplier, correction, corrected_gauge, right_inverse = _tau_schur_solve(
        gamma_trace, pi_rs, raw_gauge
    )
    projected_gauge = pi_rs @ raw_gauge

    right_inverse_residual = float(
        np.linalg.norm(gamma_trace @ right_inverse - np.eye(spin_dim, dtype=complex))
    )
    kkt_stationarity_residual = float(
        np.linalg.norm(corrected_gauge - raw_gauge + gamma_trace.conj().T @ multiplier)
    )
    tau_noether_residual = float(np.linalg.norm(gamma_trace @ corrected_gauge))
    projector_identity_residual = float(np.linalg.norm(corrected_gauge - projected_gauge))
    correction_normal_residual = float(np.linalg.norm(pi_rs @ correction))

    # Noether only kills the normal component.  Any tangent map Z with Gamma Z=0
    # can be added without changing the identity, so finite-fiber tau does not
    # select a unique gauge differential unless a source supplies more data.
    tangent_probe_direction = np.zeros(vector_dim, dtype=complex)
    tangent_probe_direction[1] = 1.0
    tangent_perturbation = pi_rs @ _vector_spinor_injection(
        tangent_probe_direction, spin_dim
    )
    alternative_gauge = corrected_gauge + tangent_perturbation
    tangent_perturbation_noether_residual = float(
        np.linalg.norm(gamma_trace @ alternative_gauge)
    )
    tangent_perturbation_difference_norm = float(np.linalg.norm(tangent_perturbation))

    null_direction = np.zeros(vector_dim, dtype=complex)
    null_direction[0] = 1.0
    null_direction[9] = 1.0
    null_raw = _vector_spinor_injection(null_direction, spin_dim)
    null_multiplier, _null_correction, null_corrected, _null_right_inverse = _tau_schur_solve(
        gamma_trace, pi_rs, null_raw
    )

    raw_noether_rank = _rank(gamma_trace @ raw_gauge)
    tau_multiplier_rank = _rank(multiplier)
    corrected_gauge_rank = _rank(corrected_gauge)
    null_raw_noether_rank = _rank(gamma_trace @ null_raw)
    null_tau_multiplier_rank = _rank(null_multiplier)
    null_corrected_gauge_rank = _rank(null_corrected)

    bare_commutator = pi_rs @ mass_operator - mass_operator @ pi_rs
    c2_operator = gamma_trace @ mass_operator @ pi_rs
    bare_commutator_norm = float(np.linalg.norm(bare_commutator))
    c2_norm = float(np.linalg.norm(c2_operator))

    free_tangent_column_dim = total_dim - _rank(gamma_trace)
    free_tangent_matrix_dim = free_tangent_column_dim * spin_dim

    tau_derives_projection = (
        right_inverse_residual < TOL
        and kkt_stationarity_residual < TOL
        and tau_noether_residual < TOL
        and projector_identity_residual < TOL
        and correction_normal_residual < TOL
    )
    tangent_freedom = (
        tangent_perturbation_noether_residual < TOL
        and tangent_perturbation_difference_norm > 1.0
        and free_tangent_matrix_dim > 0
    )
    anchors_preserved = (
        abs(bare_commutator_norm - ANCHOR_BARE_COMMUTATOR) < 1.0e-4
        and abs(c2_norm - ANCHOR_C2) < 1.0e-4
    )
    null_caveat_preserved = (
        null_raw_noether_rank == 64
        and null_tau_multiplier_rank == 64
        and null_corrected_gauge_rank == 128
    )

    if tau_derives_projection and tangent_freedom and anchors_preserved and null_caveat_preserved:
        verdict = (
            SourceNoetherTauVerdict.TAU_SCHUR_PROJECTOR_ONLY_DERIVATIVE_TAU_BLOCKED
        )
    else:
        verdict = SourceNoetherTauVerdict.FAILS

    return SourceNoetherTauReport(
        verdict=verdict,
        right_inverse_residual=right_inverse_residual,
        kkt_stationarity_residual=kkt_stationarity_residual,
        tau_noether_residual=tau_noether_residual,
        projector_identity_residual=projector_identity_residual,
        correction_normal_residual=correction_normal_residual,
        raw_noether_rank=raw_noether_rank,
        tau_multiplier_rank=tau_multiplier_rank,
        corrected_gauge_rank=corrected_gauge_rank,
        tangent_perturbation_noether_residual=tangent_perturbation_noether_residual,
        tangent_perturbation_difference_norm=tangent_perturbation_difference_norm,
        free_tangent_column_dim=free_tangent_column_dim,
        free_tangent_matrix_dim=free_tangent_matrix_dim,
        null_raw_noether_rank=null_raw_noether_rank,
        null_tau_multiplier_rank=null_tau_multiplier_rank,
        null_corrected_gauge_rank=null_corrected_gauge_rank,
        bare_commutator_norm=bare_commutator_norm,
        c2_norm=c2_norm,
        source_derived_independent_tau=False,
        next_progress_point="DERIVATIVE-TAU-HOMOMORPHISM",
    )


if __name__ == "__main__":
    print(run_source_noether_tau_carrier())
