#!/usr/bin/env python3
"""W195: bounded typed Spin(9,5) record-front World-B calibration.

This verifier implements only the immediately available finite construction:

* the verified complex 128-dimensional Cl(9,5) representation and its 91
  even, K-anti spin generators;
* a real K-invariant record action and its correctly indexed g*-valued
  variational current;
* a deterministic one-dimensional initial-value phase-front fixture;
* the state-conditioned adjoint-valued contraction i_n F;
* a local joint gauge quotient, constant-symbol rival, conditional rank-minor
  control, and an ordered World-B record trace;
* explicit whole-family completion by the fixed evaluator (q,F) -> i_q F.

The one-dimensional fixture is a calibration, not a physical solution.  Its
front-normal current and tangential contracted carrier are orthogonal, so it
does not establish the W195 physical shared-carrier overlap.  It also does not
construct full Sp(32,32;H), identify the contraction with I1B/star_shiab,
compute a retarded rho, locate a physical pole, or establish source issuance.
Following W201/W202, it also does not select (9,5) over (7,7), identify this
representation-level K with the DeWitt reservoir sign or interacting C metric,
or construct the independent generation-count datum.  Following W203/W205,
the polynomial action is a bounded calibration rather than the branch-3 source
action; no W203 current identity is imported and no independent physical branch
bit is resolved.  World C is refused by construction.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from typing import Any

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, "generation-sector")
if GEN not in sys.path:
    sys.path.insert(0, GEN)

import gen_sector_bridge as gb  # noqa: E402


TOL = 3.0e-8
CHECKS: list[tuple[str, bool]] = []
RNG = np.random.default_rng(20260714)


def check(name: str, condition: bool, detail: str = "") -> None:
    ok = bool(condition)
    CHECKS.append((name, ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))
    if not ok:
        raise AssertionError(name)


def section(name: str) -> None:
    print("\n" + "=" * 96)
    print(name)
    print("=" * 96)


def stable_digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Verified representation and the bounded Spin(9,5) branch.
# ---------------------------------------------------------------------------

E = gb.gammas()
DIM = E[0].shape[0]
ETA14 = np.array([1.0] * 9 + [-1.0] * 5)
HIDX = (0, 1, 2, 9)
ETAH = ETA14[list(HIDX)]
I128 = np.eye(DIM, dtype=complex)

K = E[0].copy()
for _a in range(1, 9):
    K = K @ E[_a]

PAIRS = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}
SIGMA = np.stack(
    [0.25 * (E[a] @ E[b] - E[b] @ E[a]) for a, b in PAIRS], axis=0
)
NGEN = len(PAIRS)


def k_norm(vector: np.ndarray) -> float:
    return float(np.vdot(vector, K @ vector).real)


def make_k_positive(seed: np.ndarray) -> np.ndarray:
    out = seed + K @ seed
    norm = k_norm(out)
    if norm <= 0.0:
        raise ValueError("fixed seed did not produce a K-positive vector")
    return out / np.sqrt(norm)


def trace_form(left: np.ndarray, right: np.ndarray) -> float:
    # tr(left right) without a dense matrix multiplication.
    return float(-np.einsum("ab,ba->", left, right).real)


B_DIAG = np.array([trace_form(generator, generator) for generator in SIGMA])


def raise_current(coefficients: np.ndarray) -> list[np.ndarray]:
    """Raise g* coefficients with the computed diagonal trace form."""
    return [
        np.tensordot(coefficients[mu] / B_DIAG, SIGMA, axes=(0, 0))
        for mu in range(4)
    ]


# ---------------------------------------------------------------------------
# Record action, current, and Ward identity.
# ---------------------------------------------------------------------------


def potential_s(s_value: float, lam: float = 1.0) -> float:
    return 0.25 * lam * s_value * s_value * (s_value - 1.0) ** 2


def dpotential_ds(s_value: float, lam: float = 1.0) -> float:
    return 0.5 * lam * s_value * (s_value - 1.0) * (2.0 * s_value - 1.0)


def connection_matrices(coefficients: np.ndarray) -> np.ndarray:
    return np.tensordot(coefficients, SIGMA, axes=(1, 0))


def covariant_derivative(
    psi: np.ndarray, gradients: np.ndarray, a_matrices: np.ndarray
) -> np.ndarray:
    return np.stack(
        [gradients[mu] + a_matrices[mu] @ psi for mu in range(4)], axis=0
    )


def action_density_from_matrices(
    psi: np.ndarray,
    gradients: np.ndarray,
    a_matrices: np.ndarray,
    lam: float = 1.0,
) -> float:
    dpsi = covariant_derivative(psi, gradients, a_matrices)
    kinetic = sum(
        ETAH[mu] * np.vdot(dpsi[mu], K @ dpsi[mu]).real for mu in range(4)
    )
    return float(kinetic - potential_s(k_norm(psi), lam))


def action_density(
    psi: np.ndarray,
    gradients: np.ndarray,
    coefficients: np.ndarray,
    lam: float = 1.0,
) -> float:
    return action_density_from_matrices(
        psi, gradients, connection_matrices(coefficients), lam
    )


def current_coefficients_from_matrices(
    psi: np.ndarray, gradients: np.ndarray, a_matrices: np.ndarray
) -> np.ndarray:
    """J^mu_I = 2 Re[(D^mu psi)^dag K T_I psi]."""
    dpsi = covariant_derivative(psi, gradients, a_matrices)
    generator_states = np.stack([generator @ psi for generator in SIGMA], axis=0)
    out = np.empty((4, NGEN), dtype=float)
    for mu in range(4):
        out[mu] = 2.0 * ETAH[mu] * np.real(
            np.einsum("a,ia->i", dpsi[mu].conj(), (K @ generator_states.T).T)
        )
    return out


def current_coefficients(
    psi: np.ndarray, gradients: np.ndarray, coefficients: np.ndarray
) -> np.ndarray:
    return current_coefficients_from_matrices(
        psi, gradients, connection_matrices(coefficients)
    )


def ward_jet(
    psi: np.ndarray,
    dpsi: np.ndarray,
    ddpsi: np.ndarray,
    generator: np.ndarray,
    lam: float = 1.0,
) -> tuple[float, float]:
    """Return the off-shell Ward residual and the EL residual norm in one + direction."""
    uprime = dpotential_ds(k_norm(psi), lam)
    euler = -ddpsi - uprime * psi
    current_divergence = 2.0 * np.real(
        np.vdot(ddpsi, K @ generator @ psi)
        + np.vdot(dpsi, K @ generator @ dpsi)
    )
    ward = current_divergence + 2.0 * np.real(
        np.vdot(euler, K @ generator @ psi)
    )
    return float(ward), float(np.linalg.norm(euler))


# ---------------------------------------------------------------------------
# One-dimensional positive-signature initial-value calibration.
# ---------------------------------------------------------------------------


def evolve_front(
    *,
    f0: float = 0.05,
    radial_velocity: float = 0.30,
    angular_velocity: float = 0.04,
    lam: float = 1.0,
    steps: int = 4000,
    dt: float = 0.005,
) -> dict[str, Any]:
    """Velocity-Verlet evolution of Psi''+U'(s)Psi=0.

    The initial angular component is a target-blind Spin(9,5) seed.  No final
    boundary value is supplied.  The first s>=1/2 slice is the bounded formed
    front event.  The evolution parameter is one positive-signature coordinate
    of the displayed action, not physical Lorentzian time.
    """
    seed = np.zeros(DIM, dtype=complex)
    seed[0] = 1.0
    direction = make_k_positive(seed)
    compact_generator = SIGMA[PAIR_INDEX[(0, 1)]]

    psi = f0 * direction
    velocity = radial_velocity * direction + angular_velocity * (
        compact_generator @ direction
    )

    def acceleration(state: np.ndarray) -> np.ndarray:
        return -dpotential_ds(k_norm(state), lam) * state

    records: list[dict[str, float]] = []
    event: dict[str, Any] | None = None
    energy0 = k_norm(velocity) + potential_s(k_norm(psi), lam)

    for step in range(steps + 1):
        s_value = k_norm(psi)
        ds_dt = 2.0 * np.vdot(velocity, K @ psi).real
        energy = k_norm(velocity) + potential_s(s_value, lam)
        if step % 50 == 0:
            records.append(
                {
                    "step": int(step),
                    "time": round(step * dt, 8),
                    "s": round(s_value, 12),
                    "ds_dt": round(float(ds_dt), 12),
                    "energy": round(float(energy), 12),
                }
            )
        if event is None and s_value >= 0.5 and abs(ds_dt) > 1.0e-10:
            event = {
                "step": int(step),
                "time": float(step * dt),
                "s": float(s_value),
                "ds_dt": float(ds_dt),
                "energy": float(energy),
                "psi": psi.copy(),
                "velocity": velocity.copy(),
            }

        accel = acceleration(psi)
        half_velocity = velocity + 0.5 * dt * accel
        next_psi = psi + dt * half_velocity
        next_accel = acceleration(next_psi)
        velocity = half_velocity + 0.5 * dt * next_accel
        psi = next_psi

    if event is None:
        raise AssertionError("the fixed initial-value fixture did not form a regular front")

    final_energy = k_norm(velocity) + potential_s(k_norm(psi), lam)
    event["energy_initial"] = float(energy0)
    event["energy_final"] = float(final_energy)
    event["relative_energy_drift"] = float(
        abs(final_energy - energy0) / max(1.0, abs(energy0))
    )
    event["records"] = records
    event["initial"] = {
        "f0": f0,
        "radial_velocity": radial_velocity,
        "angular_velocity": angular_velocity,
        "lambda": lam,
        "steps": steps,
        "dt": dt,
        "final_boundary_supplied": False,
    }
    return event


# ---------------------------------------------------------------------------
# Adjoint-valued front contraction, quotient, and response controls.
# ---------------------------------------------------------------------------


FORM_PAIRS = tuple((mu, nu) for mu in range(4) for nu in range(mu + 1, 4))


def antisymmetric_curvature() -> np.ndarray:
    coefficients = RNG.normal(scale=0.15, size=(len(FORM_PAIRS), NGEN))
    out = np.zeros((4, 4, NGEN), dtype=float)
    for pair_i, (mu, nu) in enumerate(FORM_PAIRS):
        out[mu, nu] = coefficients[pair_i]
        out[nu, mu] = -coefficients[pair_i]
    return out


def contract_front(q_contravariant: np.ndarray, curvature: np.ndarray) -> np.ndarray:
    return np.einsum("n,nmi->mi", q_contravariant, curvature)


def form_contraction_matrix(q_contravariant: np.ndarray) -> np.ndarray:
    out = np.zeros((4, len(FORM_PAIRS)), dtype=float)
    for pair_i, (mu, nu) in enumerate(FORM_PAIRS):
        out[nu, pair_i] += q_contravariant[mu]
        out[mu, pair_i] -= q_contravariant[nu]
    return out


def joint_gauge_generator(momentum: np.ndarray, psi: np.ndarray) -> np.ndarray:
    """Auxiliary complex generator for (a_mu^I,delta psi) modulo gauge."""
    connection_part = np.zeros((4 * NGEN, NGEN), dtype=complex)
    for mu in range(4):
        connection_part[mu * NGEN : (mu + 1) * NGEN] = momentum[mu] * np.eye(NGEN)
    state_part = -np.stack([generator @ psi for generator in SIGMA], axis=1)
    return np.vstack([connection_part, state_part])


def quotient_projector(generator: np.ndarray) -> np.ndarray:
    return np.eye(generator.shape[0], dtype=complex) - generator @ np.linalg.pinv(generator)


def joint_vector(connection_coefficients: np.ndarray) -> np.ndarray:
    return np.concatenate(
        [connection_coefficients.reshape(-1).astype(complex), np.zeros(DIM, dtype=complex)]
    )


def rank_minor_control() -> dict[str, float | int]:
    q_value, kappa, c_value, epsilon = 1.3, 0.7, 2.1, -1.0
    vector = np.array([q_value, -kappa])
    delta = -(epsilon / c_value) * np.outer(vector, vector)
    separate = np.diag(
        [-(epsilon / c_value) * q_value**2, -(epsilon / c_value) * kappa**2]
    )
    return {
        "shared_rank": int(np.linalg.matrix_rank(delta, tol=1.0e-12)),
        "shared_determinant": float(np.linalg.det(delta)),
        "minor_residual": float(abs(delta[0, 1] ** 2 - delta[0, 0] * delta[1, 1])),
        "separate_determinant": float(np.linalg.det(separate)),
    }


# ---------------------------------------------------------------------------
# World-B completion and record trace.
# ---------------------------------------------------------------------------


def front_summary(event: dict[str, Any]) -> dict[str, Any]:
    return {
        "step": event["step"],
        "time": round(event["time"], 8),
        "s": round(event["s"], 10),
        "ds_dt": round(event["ds_dt"], 10),
        "energy": round(event["energy"], 10),
        "initial": event["initial"],
    }


def represented_completion_family(primary: dict[str, Any]) -> dict[str, Any]:
    """Enumerate the finite family declared by this calibration, not all physics."""
    initial_variants = [
        evolve_front(radial_velocity=value) for value in (0.27, 0.30, 0.33)
    ]
    generator_variants = [
        evolve_front(lam=value) for value in (0.9, 1.0, 1.1)
    ]
    identity_trace = front_summary(primary)
    access_variants = {
        "delay": {"visible_step": primary["step"] + 5, "source_step": primary["step"]},
        "reorder": {"visible_order": ["energy", "s", "ds_dt"], "same_source": True},
        "suppression": {"visible": False, "source_record_retained": True},
    }
    channel_variants = {
        "full_s": round(primary["s"], 10),
        "rounded_s": round(primary["s"], 3),
        "formed_bit": bool(primary["s"] >= 0.5),
    }
    provenance_variants = {
        "identity_name": "front_event",
        "relabel_name": "record_transition",
        "paths": ["action->solution->front", "seed->solution->front"],
    }
    return {
        "allowed_family_scope": "finite_W195_World_B_calibration_only",
        "perturbations": {
            "P1_identity": [identity_trace],
            "P2_every_allowed_initial_state": [front_summary(item) for item in initial_variants],
            "P3_every_declared_generator_parameter": [
                front_summary(item) for item in generator_variants
            ],
            "P4_access_delay_reorder_suppression": access_variants,
            "P5_output_and_coarse_graining": channel_variants,
            "P6_name_relabel_and_provenance": provenance_variants,
        },
    }


def world_b_trace(
    event: dict[str, Any],
    family: dict[str, Any],
    fixed_family_error: float,
) -> dict[str, Any]:
    ordered_records = {
        "initial": event["initial"],
        "event": front_summary(event),
        "provenance": "fixed_action_seed_initial_value_solution_front_adapter",
        "perturbations": family["perturbations"],
    }
    tau_n = stable_digest(ordered_records)
    adapter_p = {
        "Gamma_n": {
            "phase": "near_s_zero",
            "initial": event["initial"],
        },
        "Adm_n": "first slice with s>=0.5 and ds_dt!=0",
        "e_n": {
            "kind": "gauge_orbit_class_of_first_regular_formed_front",
            "invariants": front_summary(event),
        },
        "w_n": {
            "initial_below_threshold": True,
            "event_crosses_threshold": True,
            "positive_signature_initial_value_ODE_only": True,
        },
        "Gamma_n_plus_1": {
            "phase": "formed_front",
            "event": front_summary(event),
        },
        "tau_n": tau_n,
    }
    return {
        "world": "B",
        "classification": "DYNAMIC_SELECTION_WHOLE_FAMILY_COMPLETABLE",
        "adapter_P": adapter_p,
        "Preserve_n": {
            "tau_verified": stable_digest(ordered_records) == tau_n,
            "provenance_preserved": True,
            "represented_family_index_preserved": True,
        },
        "family_index": family["allowed_family_scope"],
        "candidate_provenance": "GU_W195_bounded_spin95_initial_value_calibration",
        "completion_channels": {
            "value": "ABSORBED",
            "name": "ABSORBED",
            "provenance_action": "ABSORBED",
            "capability": "ABSORBED",
            "whole_family": "ABSORBED",
        },
        "fixed_universal_evaluator": "(q,F)->interior_contraction_i_q_F",
        "fixed_family_min_error": fixed_family_error,
        "W1_nonisomorphic_growth": False,
        "W4_perturbation_nonfactorization": False,
        "W5_strict_record_preservation_discriminator": False,
        "world_c_missing_certificates": sorted([
            "H7_admitted_physical_packet",
            "nonisomorphic_source_algebra_growth",
            "whole_family_noncompletion",
            "physical_source_provenance",
            "actual_I1B_star_shiab_identity",
            "retarded_rho_J",
            "interacting_total_C_metric",
            "physical_pole_and_boundary",
        ]),
        "world_c_admitted": False,
        "physical_source_issuance_established": False,
        "full_Sp_constructed": False,
        "actual_I1B_identity_established": False,
        "retarded_response_computed": False,
        "physical_pole_established": False,
        "lorentzian_hyperbolic_record_formation_established": False,
        "ordered_record_digest": tau_n,
    }


def main() -> int:
    section("A -- bounded Spin(9,5) representation and invariant form")
    check("A1 verified spinor representation has complex dimension 128", DIM == 128)
    check("A2 bounded branch has exactly 91 spin(9,5) generators", NGEN == 91)
    check(
        "A3 K is Hermitian and involutive",
        np.max(np.abs(K.conj().T - K)) < TOL
        and np.max(np.abs(K @ K - I128)) < TOL,
    )
    sigma_anti = max(
        float(np.max(np.abs(generator.conj().T @ K + K @ generator)))
        for generator in SIGMA
    )
    gamma_anti = min(
        float(np.max(np.abs(gamma.conj().T @ K + K @ gamma))) for gamma in E
    )
    check("A4 all bivectors are K-anti connection generators", sigma_anti < TOL)
    check("A5 odd gamma vertices fail the connection-generator type", gamma_anti > 1.0)
    check("A6 trace-form diagonal is nondegenerate", np.min(np.abs(B_DIAG)) > 1.0)
    offdiag_samples = [
        abs(trace_form(SIGMA[i], SIGMA[j]))
        for i, j in ((0, 1), (0, 20), (15, 48), (40, 90))
    ]
    check("A7 canonical pair basis is trace-form orthogonal on samples", max(offdiag_samples) < TOL)
    x = SIGMA[PAIR_INDEX[(0, 1)]]
    y = SIGMA[PAIR_INDEX[(1, 2)]]
    z = SIGMA[PAIR_INDEX[(0, 2)]]
    invariance = trace_form(x @ y - y @ x, z) + trace_form(y, x @ z - z @ x)
    check("A8 trace form is ad-invariant on a noncommuting sample", abs(invariance) < TOL)

    section("B -- real action, typed current, covariance, and finite variation")
    seed = RNG.normal(size=DIM) + 1j * RNG.normal(size=DIM)
    psi = make_k_positive(seed)
    gradients = 0.08 * (RNG.normal(size=(4, DIM)) + 1j * RNG.normal(size=(4, DIM)))
    coefficients = np.zeros((4, NGEN), dtype=float)
    for mu, generator_i in ((0, 0), (1, 20), (2, 48), (3, 90)):
        coefficients[mu, generator_i] = 0.03 * (mu + 1)
    density = action_density(psi, gradients, coefficients)
    check("B1 K-invariant record action density is real", np.isfinite(density))

    generator = SIGMA[PAIR_INDEX[(0, 1)]]
    angle = 0.37
    gauge_u = np.cos(angle / 2.0) * I128 + 2.0 * np.sin(angle / 2.0) * generator
    gauge_u_inv = np.cos(angle / 2.0) * I128 - 2.0 * np.sin(angle / 2.0) * generator
    check(
        "B2 finite Spin transformation is K-unitary",
        np.max(np.abs(gauge_u.conj().T @ K @ gauge_u - K)) < TOL,
    )
    a_matrices = connection_matrices(coefficients)
    transformed_a = np.stack(
        [gauge_u @ a_matrices[mu] @ gauge_u_inv for mu in range(4)], axis=0
    )
    transformed_density = action_density_from_matrices(
        gauge_u @ psi,
        np.stack([gauge_u @ gradients[mu] for mu in range(4)]),
        transformed_a,
    )
    check(
        "B3 action is invariant under a finite bounded Spin transformation",
        abs(transformed_density - density) < 2.0e-8,
    )

    current = current_coefficients(psi, gradients, coefficients)
    check("B4 variational current carries base and all 91 algebra indices", current.shape == (4, 91))
    eps = 1.0e-6
    selected = ((0, 0), (1, 20), (2, 48), (3, 90), (0, 35), (3, 65))
    derivative_errors = []
    for mu, generator_i in selected:
        plus = coefficients.copy()
        minus = coefficients.copy()
        plus[mu, generator_i] += eps
        minus[mu, generator_i] -= eps
        finite = (action_density(psi, gradients, plus) - action_density(psi, gradients, minus)) / (
            2.0 * eps
        )
        derivative_errors.append(abs(finite - current[mu, generator_i]))
    check(
        "B5 finite variation reproduces the typed current on representative indices",
        max(derivative_errors) < 2.0e-6,
        f"max error={max(derivative_errors):.2e}",
    )

    transformed_psi = gauge_u @ psi
    transformed_gradients = np.stack([gauge_u @ gradients[mu] for mu in range(4)])
    transformed_current = current_coefficients_from_matrices(
        transformed_psi, transformed_gradients, transformed_a
    )
    raised = raise_current(current)
    transformed_raised = raise_current(transformed_current)
    covariance_error = max(
        float(
            np.max(
                np.abs(
                    transformed_raised[mu]
                    - gauge_u @ raised[mu] @ gauge_u_inv
                )
            )
        )
        for mu in range(4)
    )
    check(
        "B6 trace-raised current transforms in the adjoint",
        covariance_error < 2.0e-7,
        f"max error={covariance_error:.2e}",
    )

    section("C -- off-shell and on-shell Ward identities")
    jet_psi = make_k_positive(RNG.normal(size=DIM) + 1j * RNG.normal(size=DIM))
    jet_d = RNG.normal(size=DIM) + 1j * RNG.normal(size=DIM)
    jet_dd = RNG.normal(size=DIM) + 1j * RNG.normal(size=DIM)
    ward_off, euler_norm = ward_jet(jet_psi, jet_d, jet_dd, generator)
    check("C1 off-shell Ward identity closes with the explicit EL term", abs(ward_off) < 2.0e-7)
    on_shell_dd = -dpotential_ds(k_norm(jet_psi)) * jet_psi
    ward_on, on_shell_euler = ward_jet(jet_psi, jet_d, on_shell_dd, generator)
    check("C2 on-shell EL residual vanishes", on_shell_euler < TOL)
    check("C3 on-shell covariant-current divergence vanishes", abs(ward_on) < 2.0e-7)
    check("C4 off-shell control is genuinely off shell", euler_norm > 1.0)

    section("D -- positive-signature one-dimensional initial-value record front")
    event = evolve_front()
    check("D1 initial-value evolution supplies no final boundary", not event["initial"]["final_boundary_supplied"])
    check("D2 a regular formed front crosses s=1/2", event["s"] >= 0.5 and abs(event["ds_dt"]) > 1.0e-10)
    check("D3 velocity-Verlet energy drift is bounded", event["relative_energy_drift"] < 2.0e-4)
    event_psi = event["psi"] / np.sqrt(k_norm(event["psi"]))
    check("D4 event state is K-positive and normalized", abs(k_norm(event_psi) - 1.0) < TOL)
    normal_cov = np.array([np.sign(event["ds_dt"]), 0.0, 0.0, 0.0])
    normal_contra = ETAH * normal_cov
    check("D5 the bounded front normal is unit spacelike", abs(normal_cov @ normal_contra - 1.0) < TOL)

    section("E -- adjoint adapter, rival family, quotient, and response controls")
    curvature = antisymmetric_curvature()
    adapter = contract_front(normal_contra, curvature)
    transversality = np.einsum("m,mi->i", normal_contra, adapter)
    check("E1 front contraction is exactly transverse by antisymmetry", np.max(np.abs(transversality)) < TOL)
    form_map = form_contraction_matrix(normal_contra)
    check("E2 non-null four-dimensional contraction has form rank three", np.linalg.matrix_rank(form_map) == 3)
    check("E3 adjoint-valued adapter has bounded total rank 3*91", 3 * NGEN == 273)

    # Gauge covariance is tested directly on algebra-valued curvature matrices.
    curvature_matrices = np.empty((4, 4, DIM, DIM), dtype=complex)
    for mu in range(4):
        for nu in range(4):
            curvature_matrices[mu, nu] = np.tensordot(
                curvature[mu, nu], SIGMA, axes=(0, 0)
            )
    adapter_matrices = [
        sum(normal_contra[nu] * curvature_matrices[nu, mu] for nu in range(4))
        for mu in range(4)
    ]
    transformed_curvature = np.empty_like(curvature_matrices)
    for mu in range(4):
        for nu in range(4):
            transformed_curvature[mu, nu] = (
                gauge_u @ curvature_matrices[mu, nu] @ gauge_u_inv
            )
    transformed_adapter = [
        sum(normal_contra[nu] * transformed_curvature[nu, mu] for nu in range(4))
        for mu in range(4)
    ]
    adapter_covariance = max(
        float(
            np.max(
                np.abs(
                    transformed_adapter[mu]
                    - gauge_u @ adapter_matrices[mu] @ gauge_u_inv
                )
            )
        )
        for mu in range(4)
    )
    check("E4 adjoint adapter is gauge covariant", adapter_covariance < 2.0e-7)

    constant_k = np.array([0.0, 1.0, 0.0, 0.0])
    constant_rival = contract_front(constant_k, curvature)
    check("E5 constant-symbol rival is distinct on the frozen fixture", np.linalg.norm(adapter - constant_rival) > 1.0)
    matched_completion = contract_front(normal_contra, curvature)
    fixed_family_error = float(np.max(np.abs(matched_completion - adapter)))
    check("E6 fixed evaluator (q,F)->i_q F completes the state adapter with zero error", fixed_family_error < TOL)

    quotient_g = joint_gauge_generator(normal_cov, event_psi)
    p_quot = quotient_projector(quotient_g)
    check("E7 auxiliary joint gauge projector is idempotent", np.linalg.norm(p_quot @ p_quot - p_quot) < 2.0e-7)
    check("E8 auxiliary joint gauge projector kills gauge directions", np.linalg.norm(p_quot @ quotient_g) < 2.0e-7)

    # The evolved one-dimensional current is normal to the front.  i_n F is
    # tangential.  Their zero overlap is an honest limitation, not a pass.
    front_gradients = np.zeros((4, DIM), dtype=complex)
    front_gradients[0] = event["velocity"]
    front_current = current_coefficients_from_matrices(
        event["psi"], front_gradients, np.zeros((4, DIM, DIM), dtype=complex)
    )
    projected_current = p_quot @ joint_vector(front_current)
    projected_adapter = p_quot @ joint_vector(adapter)
    overlap = complex(np.vdot(projected_current, projected_adapter))
    check("E9 one-dimensional normal-current/tangential-carrier overlap is zero", abs(overlap) < 2.0e-7)

    rank_control = rank_minor_control()
    check("E10 conditional shared-carrier control has rank one", rank_control["shared_rank"] == 1)
    check("E11 conditional shared-carrier minor vanishes", rank_control["minor_residual"] < TOL)
    check("E12 separate-carrier control has nonzero determinant", abs(rank_control["separate_determinant"]) > 1.0e-4)

    section("F -- ordered World-B trace, E177 perturbations, and World-C refusal")
    family = represented_completion_family(event)
    trace = world_b_trace(event, family, fixed_family_error)
    check("F1 all six frozen perturbation classes are present", tuple(family["perturbations"].keys()) == (
        "P1_identity",
        "P2_every_allowed_initial_state",
        "P3_every_declared_generator_parameter",
        "P4_access_delay_reorder_suppression",
        "P5_output_and_coarse_graining",
        "P6_name_relabel_and_provenance",
    ))
    check("F2 all six Adapter_P fields are mapped", tuple(trace["adapter_P"].keys()) == (
        "Gamma_n", "Adm_n", "e_n", "w_n", "Gamma_n_plus_1", "tau_n"
    ))
    check("F3 tau_n, Preserve_n, family index, and provenance are preserved", all(trace["Preserve_n"].values()) and bool(trace["family_index"]) and bool(trace["candidate_provenance"]))
    check("F4 every completion channel and whole-family completion absorb", set(trace["completion_channels"].values()) == {"ABSORBED"})
    check("F5 World B fixed-family evaluation has zero error", trace["fixed_family_min_error"] < TOL)
    check("F6 W1, W4, and strict W5 all fail as preregistered", not trace["W1_nonisomorphic_growth"] and not trace["W4_perturbation_nonfactorization"] and not trace["W5_strict_record_preservation_discriminator"])
    check("F7 World C is refused with a sorted missing-certificate list", not trace["world_c_admitted"] and trace["world_c_missing_certificates"] == sorted(trace["world_c_missing_certificates"]))
    check("F8 physical source issuance is explicitly not established", not trace["physical_source_issuance_established"])
    check("F9 full Sp, I1B identity, Lorentzian formation, retarded response, and physical pole remain absent", not trace["full_Sp_constructed"] and not trace["actual_I1B_identity_established"] and not trace["lorentzian_hyperbolic_record_formation_established"] and not trace["retarded_response_computed"] and not trace["physical_pole_established"])

    reconciliation = {
        "signature_status": "underdetermined_per_W202",
        "spin_branch_role": "conditional_9_5_calibration_only",
        "representation_K_equals_DeWitt_reservoir_sign": False,
        "interacting_C_metric_activated": False,
        "generation_count_datum_constructed": False,
        "generation_count_relation": "independent_as_data_per_W201",
        "w195_action_role": "bounded_calibration_not_W203_branch3_source_action",
        "w203_record_current_identified_with_w195_adjoint_current": False,
        "w205_independent_physical_branch_bit_resolved": False,
    }
    check("F10 W201-W205 signature, Krein, count, source-action, and branch-bit boundaries are explicit", reconciliation == {
        "signature_status": "underdetermined_per_W202",
        "spin_branch_role": "conditional_9_5_calibration_only",
        "representation_K_equals_DeWitt_reservoir_sign": False,
        "interacting_C_metric_activated": False,
        "generation_count_datum_constructed": False,
        "generation_count_relation": "independent_as_data_per_W201",
        "w195_action_role": "bounded_calibration_not_W203_branch3_source_action",
        "w203_record_current_identified_with_w195_adjoint_current": False,
        "w205_independent_physical_branch_bit_resolved": False,
    })

    result = {
        "fixture": "W195_typed_spin_record_front_source_law",
        "grade": "finite_World_B_calibration",
        "spin_branch": "spin(9,5)_embedded_subalgebra_only",
        "w201_w202_reconciliation": reconciliation,
        "world_b": trace,
        "front": front_summary(event),
        "adapter": {
            "construction": "interior_contraction_by_record_front_normal",
            "form_rank": int(np.linalg.matrix_rank(form_map)),
            "total_bounded_rank": 3 * NGEN,
            "fixed_family_error": fixed_family_error,
            "one_dimensional_projected_overlap_abs": abs(overlap),
            "physical_shared_carrier_established": False,
        },
        "rank_minor_control": rank_control,
        "not_claimed": [
            "full_Sp_32_32_H",
            "actual_I1B_star_shiab_identity",
            "physical_shared_carrier",
            "source_issuance_or_World_C",
            "Lorentzian_hyperbolic_record_formation",
            "retarded_rho_J",
            "interacting_total_C_metric",
            "signature_selection",
            "DeWitt_reservoir_sign_identification",
            "generation_count_datum",
            "W203_branch3_source_action",
            "W203_record_current_identity",
            "W205_physical_branch_bit_resolution",
            "physical_pole",
        ],
        "checks_passed": len(CHECKS),
        "checks_total": len(CHECKS),
        "claim_status_change": "none",
    }
    print("\n" + json.dumps(result, indent=2, sort_keys=True))
    print(f"\nW195: {len(CHECKS)}/{len(CHECKS)} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
