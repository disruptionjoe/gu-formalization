"""Anchor-scale A-door fork for the source-action buildbench.

This module tests the cheap full-scale fork named by the 2026-07-10 hourly
plan. It does not rebuild the exact toy B1 super-Jacobi calculation at
128-by-128 scale. Instead it checks the anchor-scale necessary conditions that
the source-action build must satisfy before a BV-closure attempt is worth doing:

* the Cl(9,5) representation and RS anchors reproduce;
* scalar-spinor component shifts are real full-scale maps into the RS
  vector-spinor carrier;
* non-null component shifts are not tangent to ``ker Gamma``;
* the shifts are compatible with the quaternionic/H-linear and Krein anchors;
* null directions expose the derivative-level tau caveat, so this is not a
  closed source action.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math
from typing import Mapping

import numpy as np

from lib import gu_bridge
from lib.loss_channels import EXPECTED_BARE_COMMUTATOR, EXPECTED_C2


TOL = 1e-8
ANCHOR_TOL = 1e-2
ETA = np.array([1.0] * 9 + [-1.0] * 5)


class ADoorVerdict(str, Enum):
    """Classification for the anchor-scale fork."""

    PARTIAL_PASS_BV_TAU_BLOCKED = "partial_pass_bv_tau_blocked"
    FAILED_ANCHOR_SCALE = "failed_anchor_scale"


@dataclass(frozen=True)
class ADoorReport:
    """Executable report for the anchor-scale A-door fork."""

    verdict: ADoorVerdict
    metrics: Mapping[str, object]
    next_action: str

    def passed_non_null_anchor(self) -> bool:
        return self.verdict == ADoorVerdict.PARTIAL_PASS_BV_TAU_BLOCKED


def _signature(matrix: np.ndarray, tol: float = 1e-8) -> tuple[int, int, int]:
    vals = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    scale = max(float(np.max(np.abs(vals))), 1.0)
    eps = tol * scale
    return (
        int(np.sum(vals > eps)),
        int(np.sum(vals < -eps)),
        int(np.sum(np.abs(vals) <= eps)),
    )


def _component_injection(component: int, n: int = gu_bridge.N, dim: int = gu_bridge.DIM) -> np.ndarray:
    injection = np.zeros((n * dim, dim), dtype=complex)
    injection[component * dim : (component + 1) * dim, :] = np.eye(dim, dtype=complex)
    return injection


def _linear_combination_injection(coefficients: Mapping[int, complex]) -> np.ndarray:
    out = np.zeros((gu_bridge.N * gu_bridge.DIM, gu_bridge.DIM), dtype=complex)
    for component, coefficient in coefficients.items():
        out += coefficient * _component_injection(component)
    return out


def quaternionic_J(e128: list[np.ndarray], seed: int = 1) -> np.ndarray:
    """Build the phase-unique quaternionic structure used by the parity checks."""

    def phi(unitary: np.ndarray) -> np.ndarray:
        out = np.zeros_like(unitary)
        for a in range(gu_bridge.N):
            out += ETA[a] * (e128[a] @ unitary @ e128[a].conj())
        return out / gu_bridge.N

    rng = np.random.default_rng(seed)
    unitary = rng.standard_normal((gu_bridge.DIM, gu_bridge.DIM)) + 1j * rng.standard_normal(
        (gu_bridge.DIM, gu_bridge.DIM)
    )
    for _ in range(400):
        unitary = 0.5 * (unitary + phi(unitary))
        unitary /= np.linalg.norm(unitary)
    left, _, right = np.linalg.svd(unitary)
    unitary = left @ right
    return unitary / np.sqrt(abs(np.trace(unitary @ unitary.conj()) / gu_bridge.DIM))


def spinor_krein_metric(e128: list[np.ndarray]) -> np.ndarray:
    """Spinor Krein metric beta_S from the repo's ghost-parity convention."""

    beta = np.eye(gu_bridge.DIM, dtype=complex)
    for spacelike in range(9):
        beta = beta @ e128[spacelike]
    if np.linalg.norm(beta.conj().T + beta) < 1e-9:
        beta = 1j * beta
    beta = beta / np.sqrt(abs((beta @ beta)[0, 0].real))
    return beta


def _rank(matrix: np.ndarray, tol: float = 1e-8) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def run_anchor_scale_a_door() -> ADoorReport:
    """Run the anchor-scale necessary-condition fork."""

    e, Gamma, Pi_RS, M_D = gu_bridge.constraint_objects()
    dim = gu_bridge.DIM
    total_dim = gu_bridge.N * dim
    identity_total = np.eye(total_dim, dtype=complex)
    Q = identity_total - Pi_RS

    bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
    c2 = float(np.linalg.norm(Gamma @ M_D @ Pi_RS))
    anchor_ok = (
        abs(bare - EXPECTED_BARE_COMMUTATOR) < ANCHOR_TOL
        and abs(c2 - EXPECTED_C2) < ANCHOR_TOL
    )

    gamma_rank = _rank(Gamma)
    ker_gamma_dim = total_dim - gamma_rank
    gamma_surjective = gamma_rank == dim

    # Non-null component shifts S -> V tensor S.
    basis_trace_ranks: dict[int, int] = {}
    basis_q_ranks: dict[int, int] = {}
    basis_kernel_projection_ranks: dict[int, int] = {}
    for component in range(gu_bridge.N):
        injection = _component_injection(component)
        basis_trace_ranks[component] = _rank(Gamma @ injection)
        basis_q_ranks[component] = _rank(Q @ injection)
        basis_kernel_projection_ranks[component] = _rank(Pi_RS @ injection)

    non_null_components_not_tangent = all(rank == dim for rank in basis_trace_ranks.values())
    non_null_components_have_normal_part = all(rank == dim for rank in basis_q_ranks.values())
    non_null_components_have_kernel_part = all(
        rank == dim for rank in basis_kernel_projection_ranks.values()
    )

    # Null direction control: e_0 + e_9 is null for (9,5). This is the derivative tau caveat.
    null_injection = _linear_combination_injection({0: 1.0, 9: 1.0})
    null_trace = Gamma @ null_injection
    null_trace_rank = _rank(null_trace)
    null_kernel_dim = dim - null_trace_rank
    null_square_norm = float(np.linalg.norm(null_trace @ null_trace))
    null_direction_has_tangent_spinors = null_kernel_dim > 0

    # Quaternionic/H-linear compatibility of component shifts.
    U = quaternionic_J(e, seed=1)
    J_vector_spinor = np.kron(np.eye(gu_bridge.N, dtype=complex), U)
    h_defects: dict[int, float] = {}
    trace_h_defects: dict[int, float] = {}
    for component in range(gu_bridge.N):
        injection = _component_injection(component)
        h_defects[component] = float(np.linalg.norm(J_vector_spinor @ injection.conj() - injection @ U))
        trace_map = Gamma @ injection
        trace_h_defects[component] = float(np.linalg.norm(U @ trace_map.conj() - trace_map @ U))
    h_linear_component_shifts = max(h_defects.values()) < 1e-7
    h_linear_gamma_traces = max(trace_h_defects.values()) < 1e-7

    # Krein compatibility: component pullback remains the spinor Krein form up to vector sign.
    beta = spinor_krein_metric(e)
    beta_signature = _signature(beta)
    beta_pseudo_residual = 0.0
    for i in range(gu_bridge.N):
        for j in range(i + 1, gu_bridge.N):
            sigma = 0.25 * (e[i] @ e[j] - e[j] @ e[i])
            beta_pseudo_residual = max(
                beta_pseudo_residual,
                float(np.linalg.norm(beta @ sigma + sigma.conj().T @ beta)),
            )
    K = np.kron(np.diag(ETA).astype(complex), beta)
    pullback_spacelike = _component_injection(0).conj().T @ K @ _component_injection(0)
    pullback_timelike = _component_injection(9).conj().T @ K @ _component_injection(9)
    krein_component_compatible = (
        beta_signature == (64, 64, 0)
        and _signature(pullback_spacelike) == (64, 64, 0)
        and _signature(pullback_timelike) == (64, 64, 0)
        and beta_pseudo_residual < 1e-7
    )

    partial_pass = all(
        [
            anchor_ok,
            gamma_surjective,
            ker_gamma_dim == 1664,
            non_null_components_not_tangent,
            non_null_components_have_normal_part,
            non_null_components_have_kernel_part,
            h_linear_component_shifts,
            h_linear_gamma_traces,
            krein_component_compatible,
            null_direction_has_tangent_spinors,
            math.isclose(null_square_norm, 0.0, abs_tol=1e-7),
        ]
    )

    metrics: dict[str, object] = {
        "bare_commutator": bare,
        "C2": c2,
        "anchor_ok": anchor_ok,
        "gamma_rank": gamma_rank,
        "ker_gamma_dim": ker_gamma_dim,
        "basis_trace_ranks": basis_trace_ranks,
        "basis_q_ranks": basis_q_ranks,
        "basis_kernel_projection_ranks": basis_kernel_projection_ranks,
        "non_null_components_not_tangent": non_null_components_not_tangent,
        "non_null_components_have_normal_part": non_null_components_have_normal_part,
        "non_null_components_have_kernel_part": non_null_components_have_kernel_part,
        "null_trace_rank": null_trace_rank,
        "null_kernel_dim": null_kernel_dim,
        "null_square_norm": null_square_norm,
        "null_direction_has_tangent_spinors": null_direction_has_tangent_spinors,
        "max_component_h_defect": max(h_defects.values()),
        "max_trace_h_defect": max(trace_h_defects.values()),
        "h_linear_component_shifts": h_linear_component_shifts,
        "h_linear_gamma_traces": h_linear_gamma_traces,
        "spinor_krein_signature": beta_signature,
        "beta_pseudo_antihermitian_residual": beta_pseudo_residual,
        "component_krein_compatible": krein_component_compatible,
    }

    if partial_pass:
        return ADoorReport(
            verdict=ADoorVerdict.PARTIAL_PASS_BV_TAU_BLOCKED,
            metrics=metrics,
            next_action=(
                "attempt minimal BV/Koszul-Tate closure, with the null-direction tau caveat "
                "kept as an explicit failure condition"
            ),
        )

    return ADoorReport(
        verdict=ADoorVerdict.FAILED_ANCHOR_SCALE,
        metrics=metrics,
        next_action="record A-door failure and pivot back to the carrier-B/ker-Gamma declaration",
    )
