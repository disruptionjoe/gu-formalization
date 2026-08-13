#!/usr/bin/env python3
"""W177 ambient Yang--Mills stationarity and mode-closure gate.

Layer 0
-------
This probe does *not* identify the displayed X4 Seiberg--Witten connection
with the W131/W177 connection.  It tests the explicit conditional ambient
candidate

    A0 = spin-lift(nabla^gimmel) on Y14 = Met(X4)

inside the assumed Yang--Mills sector

    S_YM[A] = alpha integral_Y <F_A,F_A>.

For a Levi--Civita connection, the Yang--Mills residual is the represented
divergence of Riemann curvature.  With all indices lowered, contracted Bianchi
gives

    (D_A0^* F_A0)_{MJ,L}
      = +/- (nabla_M Ric_{LJ} - nabla_J Ric_{LM}).

The overall sign depends on the codifferential convention; zero versus
nonzero does not.  The test evaluates this tensor at the exact deterministic
W177 point over three nested finite-difference scales.

Predeclared numerical verdict
-----------------------------
NONSTATIONARY only when:
  * every scale has a nonzero residual above 1e-6;
  * the three residual norms have relative spread below 12%; and
  * the median signal is at least 20 times the larger of the contracted-
    Bianchi comparison defect and the parallel-Ricci zero-control residual.

STATIONARY only when the maximum residual is below both 1e-6 and twenty times
that numerical floor.  Every other return is OPEN-NUMERICALLY.

Controls
--------
  * W177 point, signature, and nonzero-curvature anchors.
  * Metric compatibility and Ricci symmetry.
  * Direct covariant divergence of Riemann agrees with the Ricci-Codazzi form.
  * A planted parallel tensor Ric=lambda*g has zero residual.
  * A planted non-Codazzi symmetric tensor has nonzero residual.
  * No physical Hessian or retained-mode spectrum is read unless STATIONARY.

This is a local finite-difference construction check, not a global theorem,
vacuum claim, X4 reduction, physical spectrum, or B5 phase selection.
"""
from __future__ import annotations

import json
from dataclasses import dataclass

import numpy as np


N = 14
NF = 10
ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])
ETA14 = np.diag([1.0] * 9 + [-1.0] * 5)
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]
EBASIS: list[np.ndarray] = []
for pair in PAIRS:
    matrix = np.zeros((4, 4))
    a, b = pair
    matrix[a, b] = 1.0
    matrix[b, a] = 1.0
    EBASIS.append(matrix)
CHECKS: list[tuple[str, bool]] = []


def fro(value: np.ndarray) -> float:
    return float(np.linalg.norm(value))


def check(name: str, condition: bool, detail: str = "") -> None:
    passed = bool(condition)
    CHECKS.append((name, passed))
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if passed else 'FAIL'}: {name}{suffix}")


def vmat(components: np.ndarray) -> np.ndarray:
    matrix = np.zeros((4, 4))
    for component, (a, b) in zip(components, PAIRS, strict=True):
        matrix[a, b] = component
        matrix[b, a] = component
    return matrix


def comps_of(matrix: np.ndarray) -> np.ndarray:
    return np.array([matrix[a, b] for a, b in PAIRS])


def fibre_metric(base_metric: np.ndarray) -> np.ndarray:
    inverse = np.linalg.inv(base_metric)
    raised = [inverse @ element for element in EBASIS]
    result = np.zeros((NF, NF))
    for i in range(NF):
        for j in range(NF):
            result[i, j] = (
                np.trace(raised[i] @ raised[j])
                - 0.5 * np.trace(raised[i]) * np.trace(raised[j])
            )
    return result


def gimmel(hvec: np.ndarray) -> np.ndarray:
    base_metric = vmat(hvec)
    result = np.zeros((N, N))
    result[:4, :4] = base_metric
    result[4:, 4:] = fibre_metric(base_metric)
    return result


def orthonormal_frame(metric: np.ndarray) -> np.ndarray:
    """Columns E satisfy E.T G E = diag(+^9,-^5), as in W177."""
    eigenvalues, eigenvectors = np.linalg.eigh(metric)
    order = np.argsort(-np.sign(eigenvalues))
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]
    return eigenvectors / np.sqrt(np.abs(eigenvalues))


def fixed_w177_point() -> np.ndarray:
    """Reproduce W177's exact seeded curved Lorentzian fibre point."""
    rng = np.random.default_rng(20260714)
    seed = rng.normal(size=(4, 4))
    seed = 0.5 * (seed + seed.T)
    return comps_of(ETA4 + 0.12 * seed)


def metric_derivative(hvec: np.ndarray, step: float) -> np.ndarray:
    """Coordinate partial_Q G_MN; base derivatives are exactly zero."""
    partial = np.zeros((N, N, N))
    for fibre_index in range(NF):
        plus = hvec.copy()
        minus = hvec.copy()
        plus[fibre_index] += step
        minus[fibre_index] -= step
        partial[4 + fibre_index] = (
            gimmel(plus) - gimmel(minus)
        ) / (2.0 * step)
    return partial


def christoffel(hvec: np.ndarray, metric_step: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return G, partial G, and Gamma^I_JK for the explicit gimmel metric."""
    metric = gimmel(hvec)
    inverse = np.linalg.inv(metric)
    partial = metric_derivative(hvec, metric_step)
    gamma = np.zeros((N, N, N))
    for j in range(N):
        for k in range(N):
            covector = 0.5 * (
                partial[j, :, k] + partial[k, :, j] - partial[:, j, k]
            )
            gamma[:, j, k] = inverse @ covector
    return metric, partial, gamma


def riemann_data(
    hvec: np.ndarray,
    metric_step: float,
    connection_step: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return G, partial G, Gamma, and R_IJKL with W177's convention."""
    metric, partial_metric, gamma = christoffel(hvec, metric_step)
    partial_gamma = np.zeros((N, N, N, N))
    for fibre_index in range(NF):
        plus = hvec.copy()
        minus = hvec.copy()
        plus[fibre_index] += connection_step
        minus[fibre_index] -= connection_step
        gamma_plus = christoffel(plus, metric_step)[2]
        gamma_minus = christoffel(minus, metric_step)[2]
        partial_gamma[4 + fibre_index] = (
            gamma_plus - gamma_minus
        ) / (2.0 * connection_step)

    # R^I_JKL = partial_K Gamma^I_JL - partial_L Gamma^I_JK
    #          + Gamma^I_KP Gamma^P_JL - Gamma^I_LP Gamma^P_JK.
    riemann_up = (
        partial_gamma.transpose(1, 2, 0, 3)
        - partial_gamma.transpose(1, 2, 3, 0)
        + np.einsum("ikp,pjl->ijkl", gamma, gamma)
        - np.einsum("ilp,pjk->ijkl", gamma, gamma)
    )
    riemann_low = np.einsum("im,mjkl->ijkl", metric, riemann_up)
    return metric, partial_metric, gamma, riemann_low


def ricci_from_riemann(metric: np.ndarray, riemann_low: np.ndarray) -> np.ndarray:
    """Ric_JL = G^IM R_MJIL."""
    inverse = np.linalg.inv(metric)
    return np.einsum("im,mjil->jl", inverse, riemann_low)


def covariant_derivative_two_tensor(
    partial_tensor: np.ndarray,
    tensor: np.ndarray,
    gamma: np.ndarray,
) -> np.ndarray:
    """nabla_Q T_AB for a covariant two-tensor."""
    return (
        partial_tensor
        - np.einsum("pqa,pb->qab", gamma, tensor)
        - np.einsum("pqb,ap->qab", gamma, tensor)
    )


def codazzi_residual(nabla_ricci: np.ndarray) -> np.ndarray:
    """Y_MJL = nabla_M Ric_LJ - nabla_J Ric_LM."""
    first = np.einsum("mlj->mjl", nabla_ricci)
    second = np.einsum("jlm->mjl", nabla_ricci)
    return first - second


def frame_three_tensor(tensor: np.ndarray, frame: np.ndarray) -> np.ndarray:
    """Transform a fully covariant three-tensor to the W177 orthonormal frame."""
    return np.einsum("ma,jb,lc,mjl->abc", frame, frame, frame, tensor)


def direct_divergence(
    metric: np.ndarray,
    gamma: np.ndarray,
    riemann_low: np.ndarray,
    partial_riemann: np.ndarray,
) -> np.ndarray:
    """G^KQ nabla_Q R_MJKL, retaining all four connection-index terms."""
    nabla = (
        partial_riemann
        - np.einsum("pqm,pjkl->qmjkl", gamma, riemann_low)
        - np.einsum("pqj,mpkl->qmjkl", gamma, riemann_low)
        - np.einsum("pqk,mjpl->qmjkl", gamma, riemann_low)
        - np.einsum("pql,mjkp->qmjkl", gamma, riemann_low)
    )
    return np.einsum("kq,qmjkl->mjl", np.linalg.inv(metric), nabla)


@dataclass
class ScaleResult:
    scale: float
    residual_norm: float
    curvature_norm: float
    ricci_symmetry_defect: float
    metric_compatibility_defect: float
    bianchi_defect: float
    parallel_control: float
    noncodazzi_control: float


def evaluate_scale(hvec: np.ndarray, scale: float) -> ScaleResult:
    metric_step = scale * 1.0e-5
    connection_step = scale * 1.0e-4
    ricci_step = scale * 1.0e-3

    metric, partial_metric, gamma, riemann_low = riemann_data(
        hvec, metric_step, connection_step
    )
    inverse = np.linalg.inv(metric)
    frame = orthonormal_frame(metric)
    ricci = ricci_from_riemann(metric, riemann_low)

    partial_ricci = np.zeros((N, N, N))
    partial_riemann = np.zeros((N, N, N, N, N))
    for fibre_index in range(NF):
        plus = hvec.copy()
        minus = hvec.copy()
        plus[fibre_index] += ricci_step
        minus[fibre_index] -= ricci_step
        data_plus = riemann_data(plus, metric_step, connection_step)
        data_minus = riemann_data(minus, metric_step, connection_step)
        ricci_plus = ricci_from_riemann(data_plus[0], data_plus[3])
        ricci_minus = ricci_from_riemann(data_minus[0], data_minus[3])
        partial_ricci[4 + fibre_index] = (
            ricci_plus - ricci_minus
        ) / (2.0 * ricci_step)
        partial_riemann[4 + fibre_index] = (
            data_plus[3] - data_minus[3]
        ) / (2.0 * ricci_step)

    nabla_ricci = covariant_derivative_two_tensor(partial_ricci, ricci, gamma)
    codazzi = codazzi_residual(nabla_ricci)
    codazzi_frame = frame_three_tensor(codazzi, frame)

    direct = direct_divergence(metric, gamma, riemann_low, partial_riemann)
    direct_frame = frame_three_tensor(direct, frame)
    bianchi_defect = fro(direct_frame - codazzi_frame)

    # Metric compatibility and the planted Ric=lambda*G parallel control.
    nabla_metric = covariant_derivative_two_tensor(
        partial_metric, metric, gamma
    )
    parallel_codazzi = codazzi_residual(1.7 * nabla_metric)
    parallel_frame = frame_three_tensor(parallel_codazzi, frame)

    # A planted symmetric tensor T=f u(x)u(x), f=H_00, is not Codazzi.
    u = np.linspace(0.25, 1.55, N)
    planted = hvec[0] * np.outer(u, u)
    partial_planted = np.zeros((N, N, N))
    partial_planted[4] = np.outer(u, u)
    nabla_planted = covariant_derivative_two_tensor(
        partial_planted, planted, gamma
    )
    planted_codazzi = codazzi_residual(nabla_planted)
    planted_frame = frame_three_tensor(planted_codazzi, frame)

    # Curvature norm in W177's orthonormal frame.
    curvature_frame = np.einsum(
        "ia,jb,kc,ld,ijkl->abcd",
        frame,
        frame,
        frame,
        frame,
        riemann_low,
    )

    # Sanity: inverse is used so a silent singularity cannot pass.
    assert np.all(np.isfinite(inverse))
    return ScaleResult(
        scale=scale,
        residual_norm=fro(codazzi_frame),
        curvature_norm=fro(curvature_frame),
        ricci_symmetry_defect=fro(ricci - ricci.T),
        metric_compatibility_defect=fro(nabla_metric),
        bianchi_defect=bianchi_defect,
        parallel_control=fro(parallel_frame),
        noncodazzi_control=fro(planted_frame),
    )


def main() -> int:
    hvec = fixed_w177_point()
    metric = gimmel(hvec)
    eigenvalues = np.linalg.eigvalsh(metric)
    signature = (
        int(np.sum(eigenvalues > 0.0)),
        int(np.sum(eigenvalues < 0.0)),
    )
    check("W177 deterministic point has gimmel signature (9,5)", signature == (9, 5), str(signature))

    scales = (0.75, 1.0, 1.25)
    results = [evaluate_scale(hvec, scale) for scale in scales]

    curvature_norms = np.array([item.curvature_norm for item in results])
    residual_norms = np.array([item.residual_norm for item in results])
    median_residual = float(np.median(residual_norms))
    relative_spread = float(
        (np.max(residual_norms) - np.min(residual_norms))
        / max(median_residual, 1.0e-30)
    )

    central = results[1]
    floor = max(central.bianchi_defect, central.parallel_control, 1.0e-12)
    separation = median_residual / floor

    check(
        "W177 curvature remains nonzero across derivative scales",
        bool(np.min(curvature_norms) > 1.0),
        np.array2string(curvature_norms, precision=6),
    )
    check(
        "Ricci tensor is symmetric at every scale",
        max(item.ricci_symmetry_defect for item in results) < 2.0e-4,
        f"max defect={max(item.ricci_symmetry_defect for item in results):.3e}",
    )
    check(
        "Levi--Civita metric compatibility survives the numerical derivative",
        max(item.metric_compatibility_defect for item in results) < 1.0e-7,
        f"max defect={max(item.metric_compatibility_defect for item in results):.3e}",
    )
    check(
        "contracted-Bianchi direct divergence agrees with the Ricci-Codazzi form",
        central.bianchi_defect
        / max(central.residual_norm, fro(ETA14), 1.0e-30)
        < 2.0e-2,
        f"absolute={central.bianchi_defect:.3e}, residual={central.residual_norm:.6g}",
    )
    check(
        "planted parallel Ricci=lambda*g has zero Yang--Mills residual",
        central.parallel_control < 1.0e-7,
        f"residual={central.parallel_control:.3e}",
    )
    check(
        "planted non-Codazzi symmetric tensor has nonzero residual",
        central.noncodazzi_control > 1.0e-2,
        f"residual={central.noncodazzi_control:.6g}",
    )

    nonstationary = (
        bool(np.min(residual_norms) > 1.0e-6)
        and relative_spread < 0.12
        and separation > 20.0
    )
    stationary = (
        bool(np.max(residual_norms) < 1.0e-6)
        and bool(np.max(residual_norms) < 20.0 * floor)
    )
    if nonstationary:
        verdict = "W177-AMBIENT-YM-NONSTATIONARY"
        hessian_disposition = "PHYSICAL-HESSIAN-KILLED-AT-W177-BACKGROUND"
        mode_closure_disposition = "NOT-historical-investigation"
    elif stationary:
        verdict = "W177-AMBIENT-YM-STATIONARY-LOCAL-NUMERIC"
        hessian_disposition = "PHYSICAL-HESSIAN-ADMISSIBLE-FOR-NEXT-GAUGE-DOMAIN-GATE"
        mode_closure_disposition = "NEXT-COMPUTE-FULL-OFF-DIAGONAL-BLOCK"
    else:
        verdict = "W177-AMBIENT-YM-STATIONARITY-OPEN-NUMERICALLY"
        hessian_disposition = "PHYSICAL-HESSIAN-NOT-ADMITTED"
        mode_closure_disposition = "NOT-historical-investigation"

    check(
        "stationarity classifier returned one predeclared typed verdict",
        verdict
        in {
            "W177-AMBIENT-YM-NONSTATIONARY",
            "W177-AMBIENT-YM-STATIONARY-LOCAL-NUMERIC",
            "W177-AMBIENT-YM-STATIONARITY-OPEN-NUMERICALLY",
        },
        verdict,
    )

    payload = {
        "action_arena": "conditional ambient Y14 Yang--Mills branch",
        "background": "A0 = spin-lift(nabla^gimmel), deterministic W177 point",
        "b5_transport_computed": False,
        "hessian_disposition": hessian_disposition,
        "mode_closure_disposition": mode_closure_disposition,
        "numerical_floor": floor,
        "residual_norms": residual_norms.tolist(),
        "residual_relative_spread": relative_spread,
        "signal_to_numerical_floor": separation,
        "scales": list(scales),
        "verdict": verdict,
        "x4_reduction_built": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))

    failed = [name for name, passed in CHECKS if not passed]
    if failed:
        print("FAILED CONTROLS:")
        for name in failed:
            print(f"  - {name}")
        return 1
    print("W177 AMBIENT YM RESIDUAL / MODE-CLOSURE GATE: ALL CONTROLS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
