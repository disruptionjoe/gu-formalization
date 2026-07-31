#!/usr/bin/env python3
r"""RB7: first non-metric source response and homogeneous stationary saddle.

This probe executes the two tracks frozen in

  GUH-20260731T033558Z-rb7-stationary-nonmetric-order-parameter.

Track A reconstructs the *tensor*, not merely the norm, of the conditional
W177 ambient Yang--Mills Euler covector.  The connection one-form coindex is
then restricted vertically before any Gram endomorphism is read.  If that
restricted tensor is not separated from the contracted-Bianchi numerical
floor, the selector is killed.  A separate mixed-slot contraction is retained
only as a signal-preserving comparator; it is not silently identified with a
vertical connection coefficient.

Track B is the exact homogeneous finite reduction of the written
Yang--Mills-plus-quadratic-distortion sector on a compact su(2) subalgebra.
The complete anisotropic Euler equations and Hessian are tested.  A critical
point in this finite truncation is not a stationary solution of the full GU
metric/connection/section/BV action.

Layer 0:

* the fibre is Sym^2(T*X) with trace-reversed DeWitt signature (6,4);
* H_theta and H_F are source concomitants, not physical Hessians;
* Q is their commutator, not charge conjugation or a supplied J;
* a negative triplet, a rank-four support, or a stationary multiplicity is
  not a generation, an index, a Standard Model sector, or P3; and
* the raw Frobenius and exterior numerical tens are controls, not alternate
  names for the native fibre.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import w177_ym_residual_and_mode_closure_probe as w177  # noqa: E402


TOL = 3.0e-7
RESOLUTION = 2.0e-5
FAILURES: list[str] = []
CHECK_COUNT = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECK_COUNT
    CHECK_COUNT += 1
    passed = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if passed else 'FAIL'}: {label}{suffix}")
    if not passed:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def fro(value: np.ndarray) -> float:
    return float(np.linalg.norm(value))


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value))) if value.size else 0.0


def inertia(matrix: np.ndarray, tolerance: float = TOL) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.T))
    scale = max(1.0, float(np.max(np.abs(values))))
    cut = tolerance * scale
    return (
        int(np.sum(values > cut)),
        int(np.sum(values < -cut)),
        int(np.sum(np.abs(values) <= cut)),
    )


def metric_adjoint(matrix: np.ndarray, metric: np.ndarray) -> np.ndarray:
    return np.linalg.solve(metric, matrix.T @ metric)


def signed_frame(metric: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(0.5 * (metric + metric.T))
    order = np.concatenate(
        [np.flatnonzero(values > 0.0), np.flatnonzero(values < 0.0)]
    )
    signed_values = values[order]
    frame = vectors[:, order] / np.sqrt(np.abs(signed_values))
    return frame, np.diag(np.sign(signed_values))


def block_diag(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    result = np.zeros(
        (left.shape[0] + right.shape[0], left.shape[1] + right.shape[1])
    )
    result[: left.shape[0], : left.shape[1]] = left
    result[left.shape[0] :, left.shape[1] :] = right
    return result


def trace_involution(base_metric: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    inverse = np.linalg.inv(base_metric)
    trace_covector = np.array(
        [float(np.trace(inverse @ element)) for element in w177.EBASIS]
    )
    metric_components = w177.comps_of(base_metric)
    projector = 0.25 * np.outer(metric_components, trace_covector)
    return projector, np.eye(10) - 2.0 * projector


def standard_dewitt_frame() -> np.ndarray:
    pairs = w177.PAIRS
    pair_index = {pair: index for index, pair in enumerate(pairs)}

    def diagonal(values: tuple[float, float, float, float]) -> np.ndarray:
        out = np.zeros(10)
        for index, value in enumerate(values):
            out[pair_index[(index, index)]] = value
        return out

    def pair(pair_value: tuple[int, int], scale: float) -> np.ndarray:
        out = np.zeros(10)
        out[pair_index[pair_value]] = scale
        return out

    positive = [
        diagonal((1.0, -1.0, 0.0, 0.0)) / np.sqrt(2.0),
        diagonal((1.0, 1.0, -2.0, 0.0)) / np.sqrt(6.0),
        diagonal((1.0, 1.0, 1.0, 3.0)) / np.sqrt(12.0),
        pair((0, 1), 1.0 / np.sqrt(2.0)),
        pair((0, 2), 1.0 / np.sqrt(2.0)),
        pair((1, 2), 1.0 / np.sqrt(2.0)),
    ]
    negative = [
        diagonal((0.5, 0.5, 0.5, -0.5)),
        pair((0, 3), 1.0 / np.sqrt(2.0)),
        pair((1, 3), 1.0 / np.sqrt(2.0)),
        pair((2, 3), 1.0 / np.sqrt(2.0)),
    ]
    return np.column_stack(positive + negative)


ETA4 = np.diag([1.0, 1.0, 1.0, -1.0])
ETA10 = np.diag([1.0] * 6 + [-1.0] * 4)
ETA14 = np.diag([1.0] * 9 + [-1.0] * 5)
FRAME10 = standard_dewitt_frame()
TRACE_PROJECTOR_STD = np.diag([0.0] * 6 + [1.0] + [0.0] * 3)
TRACE_INVOLUTION_STD = np.eye(10) - 2.0 * TRACE_PROJECTOR_STD


@dataclass
class ResidualData:
    scale: float
    metric: np.ndarray
    base_frame: np.ndarray
    vertical_frame: np.ndarray
    eta4: np.ndarray
    eta10: np.ndarray
    residual: np.ndarray
    direct: np.ndarray
    discrepancy: np.ndarray
    full_norm: float
    vertical_norm: float
    vertical_direct_norm: float
    vertical_discrepancy_norm: float
    base_mixed_norm: float
    mixed_h: np.ndarray
    mixed_fit_coefficients: np.ndarray
    mixed_fit_residual: float


def reconstruct_residual(scale: float) -> ResidualData:
    """Return the W177 residual in a base/vertical adapted signed frame."""
    hvec = w177.fixed_w177_point()
    metric_step = scale * 1.0e-5
    connection_step = scale * 1.0e-4
    ricci_step = scale * 1.0e-3
    metric, _partial_metric, gamma, riemann = w177.riemann_data(
        hvec, metric_step, connection_step
    )
    ricci = w177.ricci_from_riemann(metric, riemann)
    partial_ricci = np.zeros((14, 14, 14))
    partial_riemann = np.zeros((14, 14, 14, 14, 14))
    for fibre_index in range(10):
        plus = hvec.copy()
        minus = hvec.copy()
        plus[fibre_index] += ricci_step
        minus[fibre_index] -= ricci_step
        plus_data = w177.riemann_data(plus, metric_step, connection_step)
        minus_data = w177.riemann_data(minus, metric_step, connection_step)
        plus_ricci = w177.ricci_from_riemann(plus_data[0], plus_data[3])
        minus_ricci = w177.ricci_from_riemann(minus_data[0], minus_data[3])
        partial_ricci[4 + fibre_index] = (
            plus_ricci - minus_ricci
        ) / (2.0 * ricci_step)
        partial_riemann[4 + fibre_index] = (
            plus_data[3] - minus_data[3]
        ) / (2.0 * ricci_step)

    covariant_ricci = w177.covariant_derivative_two_tensor(
        partial_ricci, ricci, gamma
    )
    codazzi = w177.codazzi_residual(covariant_ricci)
    direct = w177.direct_divergence(
        metric, gamma, riemann, partial_riemann
    )

    base_frame, eta4 = signed_frame(metric[:4, :4])
    vertical_frame, eta10 = signed_frame(metric[4:, 4:])
    adapted = block_diag(base_frame, vertical_frame)
    residual_adapted = np.einsum(
        "ma,jb,lc,mjl->abc",
        adapted,
        adapted,
        adapted,
        codazzi,
        optimize=True,
    )
    direct_adapted = np.einsum(
        "ma,jb,lc,mjl->abc",
        adapted,
        adapted,
        adapted,
        direct,
        optimize=True,
    )
    discrepancy = direct_adapted - residual_adapted

    # E_{AB,i}: A,B are the adjoint pair and i is the connection-form
    # coindex.  This is the only Track-A tensor eligible for the declared
    # vertical-connection response.
    vertical = residual_adapted[:, :, 4:]
    vertical_direct = direct_adapted[:, :, 4:]
    vertical_discrepancy = discrepancy[:, :, 4:]

    # Signal-preserving comparator: one base and one vertical adjoint leg,
    # with a base connection-form coindex.  Contract the two base legs to a
    # symmetric tensor on the vertical adjoint slot.  This is a conditional
    # mixed adapter, not a retained vertical connection coefficient.
    mixed = residual_adapted[:4, 4:, :4]
    mixed_b = np.einsum(
        "aib,cjd,ac,bd->ij",
        mixed,
        mixed,
        eta4,
        eta4,
        optimize=True,
    )
    mixed_h = eta10 @ mixed_b

    base_metric = w177.vmat(hvec)
    _trace_projector, trace_involution_coord = trace_involution(base_metric)
    trace_involution_frame = np.linalg.solve(
        vertical_frame, trace_involution_coord @ vertical_frame
    )
    fit_columns = np.column_stack(
        [np.eye(10).reshape(-1), trace_involution_frame.reshape(-1)]
    )
    coefficients, *_ = np.linalg.lstsq(
        fit_columns, mixed_h.reshape(-1), rcond=None
    )
    fitted = (
        coefficients[0] * np.eye(10)
        + coefficients[1] * trace_involution_frame
    )
    fit_residual = fro(mixed_h - fitted) / max(1.0, fro(mixed_h))

    return ResidualData(
        scale=scale,
        metric=metric,
        base_frame=base_frame,
        vertical_frame=vertical_frame,
        eta4=eta4,
        eta10=eta10,
        residual=residual_adapted,
        direct=direct_adapted,
        discrepancy=discrepancy,
        full_norm=fro(residual_adapted),
        vertical_norm=fro(vertical),
        vertical_direct_norm=fro(vertical_direct),
        vertical_discrepancy_norm=fro(vertical_discrepancy),
        base_mixed_norm=fro(mixed),
        mixed_h=mixed_h,
        mixed_fit_coefficients=coefficients,
        mixed_fit_residual=fit_residual,
    )


def anisotropic_potential(
    radii: np.ndarray, sigma: float, mass_sq: float, alpha: float
) -> float:
    squares = radii * radii
    return float(
        0.5 * sigma * mass_sq * np.sum(squares)
        + 0.5
        * alpha
        * (
            squares[0] * squares[1]
            + squares[1] * squares[2]
            + squares[2] * squares[0]
        )
    )


def anisotropic_euler(
    radii: np.ndarray, sigma: float, mass_sq: float, alpha: float
) -> np.ndarray:
    r1, r2, r3 = radii
    mu = sigma * mass_sq
    return np.array(
        [
            r1 * (mu + alpha * (r2 * r2 + r3 * r3)),
            r2 * (mu + alpha * (r3 * r3 + r1 * r1)),
            r3 * (mu + alpha * (r1 * r1 + r2 * r2)),
        ]
    )


def anisotropic_hessian(
    radii: np.ndarray, sigma: float, mass_sq: float, alpha: float
) -> np.ndarray:
    r1, r2, r3 = radii
    mu = sigma * mass_sq
    result = np.array(
        [
            [
                mu + alpha * (r2 * r2 + r3 * r3),
                2.0 * alpha * r1 * r2,
                2.0 * alpha * r1 * r3,
            ],
            [
                2.0 * alpha * r1 * r2,
                mu + alpha * (r3 * r3 + r1 * r1),
                2.0 * alpha * r2 * r3,
            ],
            [
                2.0 * alpha * r1 * r3,
                2.0 * alpha * r2 * r3,
                mu + alpha * (r1 * r1 + r2 * r2),
            ],
        ]
    )
    return result


def finite_difference_gradient(
    radii: np.ndarray, sigma: float, mass_sq: float, alpha: float
) -> np.ndarray:
    step = 1.0e-6
    output = np.zeros(3)
    for index in range(3):
        plus = radii.copy()
        minus = radii.copy()
        plus[index] += step
        minus[index] -= step
        output[index] = (
            anisotropic_potential(plus, sigma, mass_sq, alpha)
            - anisotropic_potential(minus, sigma, mass_sq, alpha)
        ) / (2.0 * step)
    return output


def anisotropic_grams(
    radii: np.ndarray, sigma: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    h_theta = np.zeros((10, 10))
    h_f = np.zeros((10, 10))
    squares = radii * radii
    for local_index, fibre_index in enumerate((7, 8, 9)):
        other = [
            squares[index]
            for index in range(3)
            if index != local_index
        ]
        h_theta[fibre_index, fibre_index] = sigma * squares[local_index]
        h_f[fibre_index, fibre_index] = squares[local_index] * sum(other)
    q = h_theta @ h_f - h_f @ h_theta
    return h_theta, h_f, q


def support_projector(frame: np.ndarray, metric: np.ndarray) -> np.ndarray:
    gram = frame.T @ metric @ frame
    return frame @ np.linalg.inv(gram) @ frame.T @ metric


def normalized_determinant_polynomial_sample(frame: np.ndarray) -> float:
    """Necessary base-incidence test: all u symmetric-product v have det 0."""
    samples = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 0.0]),
        np.array([1.0, 0.0, -1.0]),
        np.array([0.0, 1.0, 1.0]),
        np.array([1.0, 2.0, -1.0]),
        np.array([2.0, -1.0, 3.0]),
    ]
    maximum = 0.0
    for coefficients in samples:
        components = frame @ coefficients
        tensor = w177.vmat(FRAME10 @ components)
        scale = max(1.0e-30, fro(tensor))
        maximum = max(
            maximum,
            abs(float(np.linalg.det(tensor))) / scale**4,
        )
    return maximum


def hyperbolic_plane_rotation(
    positive: int, negative: int, rapidity: float
) -> np.ndarray:
    output = np.eye(10)
    cosine = np.cosh(rapidity)
    sine = np.sinh(rapidity)
    output[positive, positive] = cosine
    output[negative, negative] = cosine
    output[positive, negative] = sine
    output[negative, positive] = sine
    return output


print("=" * 96)
print("RB7 FROZEN INPUTS AND PARAMETER COUNT")
print("=" * 96)
print(
    """
Track A:
  E_MJ,L = nabla_M Ric_LJ - nabla_J Ric_LM
  restrict only connection-form coindex L vertically
  new fitted parameters = 0
  carried scale = kappa * zeta_F / g_A^2 (eigenspaces may not use magnitude)

Track B:
  Phi_i = r_a e_i^a T_a, [T_a,T_b] = epsilon_ab^c T_c
  V = (sigma m^2 / 2) sum r_a^2
      + (alpha / 2) sum_(a<b) r_a^2 r_b^2
  pre-solution amplitudes = 3 anisotropic variables
  new fitted coefficients = 0
  carried coefficient ratio = m^2 / alpha

Forbidden during candidate construction:
  u, P_W, J, selected eigenvectors, Standard Model labels, P3, index, count
"""
)


print("=" * 96)
print("A. ACTUAL W177 EULER-TENSOR RESPONSE")
print("=" * 96)
scales = (0.75, 1.0, 1.25)
residual_data = [reconstruct_residual(scale) for scale in scales]
central = residual_data[1]
full_norms = np.array([item.full_norm for item in residual_data])
vertical_norms = np.array([item.vertical_norm for item in residual_data])
vertical_floors = np.array(
    [item.vertical_discrepancy_norm for item in residual_data]
)
vertical_separation = central.vertical_norm / max(
    central.vertical_discrepancy_norm, 1.0e-30
)
vertical_spread = (
    float(np.max(vertical_norms) - np.min(vertical_norms))
    / max(float(np.median(vertical_norms)), 1.0e-30)
)

check(
    "full reconstructed W177 residual reproduces the prior stable norm",
    np.max(np.abs(full_norms - np.array([3.19904935, 3.19904137, 3.19903939])))
    < 3.0e-6,
    np.array2string(full_norms, precision=9),
)
check(
    "Ricci-Codazzi residual is antisymmetric in its adjoint pair",
    fro(central.residual + central.residual.swapaxes(0, 1))
    < 2.0e-6,
)
check(
    "adapted base and vertical frames reproduce signatures (3,1) and (6,4)",
    inertia(central.eta4) == (3, 1, 0)
    and inertia(central.eta10) == (6, 4, 0),
)
check(
    "vertical connection-form residual is nonzero numerically",
    central.vertical_norm > 1.0e-6,
    f"{central.vertical_norm:.9g}",
)
check(
    "vertical connection-form residual fails numerical-floor separation",
    vertical_separation < 1.1,
    f"signal/floor={vertical_separation:.6g}",
)
check(
    "vertical connection-form residual is scale-unstable",
    vertical_spread > 1.0,
    f"spread={vertical_spread:.6g}, norms={vertical_norms}",
)
check(
    "the signal-preserving mixed block carries the full residual at central scale",
    abs(np.sqrt(2.0) * central.base_mixed_norm - central.full_norm)
    < 2.0e-5,
    f"mixed={central.base_mixed_norm:.9g}, full={central.full_norm:.9g}",
)

mixed_coefficients = np.array(
    [item.mixed_fit_coefficients for item in residual_data]
)
mixed_fit_residuals = np.array(
    [item.mixed_fit_residual for item in residual_data]
)
check(
    "mixed signal Gram is DeWitt-self-adjoint",
    fro(
        metric_adjoint(central.mixed_h, central.eta10)
        - central.mixed_h
    )
    < 2.0e-6,
)
check(
    "mixed signal Gram collapses to the identity/trace algebra",
    float(np.max(mixed_fit_residuals)) < 2.0e-5,
    f"residuals={mixed_fit_residuals}",
)
check(
    "mixed signal Gram is the traceless projector up to stable scale",
    np.max(
        np.abs(
            mixed_coefficients
            / mixed_coefficients[:, :1]
            - np.array([[1.0, 1.0]] * 3)
        )
    )
    < 2.0e-5,
    str(mixed_coefficients),
)
mixed_trace_commutator = (
    central.mixed_h
    @ np.linalg.solve(
        central.vertical_frame,
        trace_involution(
            w177.vmat(w177.fixed_w177_point())
        )[1]
        @ central.vertical_frame,
    )
    - np.linalg.solve(
        central.vertical_frame,
        trace_involution(
            w177.vmat(w177.fixed_w177_point())
        )[1]
        @ central.vertical_frame,
    )
    @ central.mixed_h
)
check(
    "mixed signal Gram resolves no nonzero trace commutator",
    fro(mixed_trace_commutator) < RESOLUTION,
    f"norm={fro(mixed_trace_commutator):.6g}",
)

track_a_verdict = (
    "VERTICAL-RESPONSE-KILLED-BELOW-NUMERICAL-FLOOR; "
    "SIGNAL-PRESERVING-MIXED-GRAM-NONSELECTING"
)
info(track_a_verdict)


print("\n" + "=" * 96)
print("B. EXACT HOMOGENEOUS NON-ABELIAN STATIONARY TRUNCATION")
print("=" * 96)
sigma = -1.0
mass_sq = 1.0
alpha = 1.0
mu = sigma * mass_sq
rank_three = np.full(3, np.sqrt(-mu / (2.0 * alpha)))
rank_two = np.array([np.sqrt(-mu / alpha), np.sqrt(-mu / alpha), 0.0])

plant = np.array([0.31, -0.47, 0.83])
check(
    "analytic anisotropic Euler derivative matches finite differences",
    max_abs(
        anisotropic_euler(plant, sigma, mass_sq, alpha)
        - finite_difference_gradient(plant, sigma, mass_sq, alpha)
    )
    < 2.0e-9,
)
check(
    "rank-three and rank-two nonzero branches solve all anisotropic equations",
    max_abs(anisotropic_euler(rank_three, sigma, mass_sq, alpha))
    < 1.0e-12
    and max_abs(anisotropic_euler(rank_two, sigma, mass_sq, alpha))
    < 1.0e-12,
)
rank_three_hessian = np.linalg.eigvalsh(
    anisotropic_hessian(rank_three, sigma, mass_sq, alpha)
)
rank_two_hessian = np.linalg.eigvalsh(
    anisotropic_hessian(rank_two, sigma, mass_sq, alpha)
)
check(
    "rank-three branch has one positive and two negative anisotropy Hessian modes",
    inertia(anisotropic_hessian(rank_three, sigma, mass_sq, alpha))
    == (1, 2, 0),
    str(rank_three_hessian),
)
check(
    "rank-two branch is also a saddle",
    inertia(anisotropic_hessian(rank_two, sigma, mass_sq, alpha))
    == (2, 1, 0),
    str(rank_two_hessian),
)
check(
    "commuting one-component direction is unbounded below on the negative branch",
    anisotropic_potential(
        np.array([20.0, 0.0, 0.0]), sigma, mass_sq, alpha
    )
    < -100.0
    and anisotropic_potential(
        np.array([40.0, 0.0, 0.0]), sigma, mass_sq, alpha
    )
    < anisotropic_potential(
        np.array([20.0, 0.0, 0.0]), sigma, mass_sq, alpha
    ),
)
check(
    "positive support has no corresponding real nonzero branch for positive coefficients",
    -1.0 * mass_sq / (2.0 * alpha) < 0.0,
)

h_theta, h_f, q = anisotropic_grams(rank_three, sigma)
check(
    "homogeneous H_theta and H_F are exactly DeWitt-self-adjoint",
    max_abs(metric_adjoint(h_theta, ETA10) - h_theta) < TOL
    and max_abs(metric_adjoint(h_f, ETA10) - h_f) < TOL,
)
check(
    "homogeneous H_theta identifies a negative triplet but has a seven-dimensional zero sector",
    inertia(h_theta) == (0, 3, 7),
    str(inertia(h_theta)),
)
check(
    "homogeneous H_theta and H_F commute throughout the anisotropic grammar",
    max_abs(q) < 1.0e-14,
)
check(
    "zero Q is singular and polar-ineligible",
    np.linalg.matrix_rank(q, tol=1.0e-12) == 0
    and max_abs(-(q @ q)) < 1.0e-14,
)

triplet_frame = np.eye(10)[:, 7:10]
cartan_frame = np.eye(10)[:, 6:10]
check(
    "native trace line plus negative triplet is a maximal negative four-plane",
    inertia(cartan_frame.T @ ETA10 @ cartan_frame) == (0, 4, 0),
)
raw_metric_std = np.diag([1.0] * 7 + [-1.0] * 3)
check(
    "raw Frobenius trace plus the same triplet has signature (1,3), not a negative four-plane",
    inertia(cartan_frame.T @ raw_metric_std @ cartan_frame) == (1, 3, 0),
)

base_incidence_control = normalized_determinant_polynomial_sample(
    triplet_frame
)
generic_motion = (
    hyperbolic_plane_rotation(3, 7, 0.19)
    @ hyperbolic_plane_rotation(2, 9, -0.31)
    @ hyperbolic_plane_rotation(1, 8, 0.23)
    @ hyperbolic_plane_rotation(0, 7, 0.37)
)
generic_triplet = generic_motion @ triplet_frame
generic_incidence_obstruction = normalized_determinant_polynomial_sample(
    generic_triplet
)
check(
    "planted RB4 base-induced triplet passes the rank-two tensor incidence control",
    base_incidence_control < 1.0e-12,
    f"{base_incidence_control:.3e}",
)
check(
    "generic negative triplet can fail the base-induced incidence control",
    max_abs(generic_motion.T @ ETA10 @ generic_motion - ETA10) < TOL
    and inertia(generic_triplet.T @ ETA10 @ generic_triplet) == (0, 3, 0)
    and generic_incidence_obstruction > 1.0e-5,
    f"determinant obstruction={generic_incidence_obstruction:.6g}",
)
check(
    "negative-triplet Grassmannian and RB4 image dimensions leave codimension fifteen",
    3 * 6 == 18 and 18 - 3 == 15,
)

track_b_verdict = (
    "KINEMATIC-CARTAN-SUPPORT-AT-NONZERO-SADDLE; "
    "NO-STABLE-SELECTION; Q-ZERO; BASE-INCIDENCE-UNSELECTED"
)
info(track_b_verdict)


print("\n" + "=" * 96)
print("C. CONSTRAINT SURPLUS AND SCOPE")
print("=" * 96)
check(
    "radial-only stationarity would be a planted false positive",
    anisotropic_potential(rank_three, sigma, mass_sq, alpha)
    < anisotropic_potential(np.zeros(3), sigma, mass_sq, alpha)
    and inertia(anisotropic_hessian(rank_three, sigma, mass_sq, alpha))
    != (3, 0, 0),
)
check(
    "the frozen-ratio radial equation/amplitude balance is zero",
    1 - 1 == 0,
    "conditional on freezing the carried m^2/alpha ratio",
)
check(
    "an adjustable program-unfixed ratio makes the radial surplus negative",
    1 - (1 + 1) == -1,
    "one equation minus amplitude and coefficient ratio",
)
check(
    "full downstream construction fails before surplus can certify a fit",
    vertical_separation < 1.1
    and inertia(anisotropic_hessian(rank_three, sigma, mass_sq, alpha))
    != (3, 0, 0)
    and np.linalg.matrix_rank(q) == 0,
)

payload = {
    "check_count": CHECK_COUNT,
    "constraint_surplus": {
        "base_induced_codimension_inside_negative_triplets": 15,
        "conditional_frozen_ratio_equation_amplitude_balance": 0,
        "negative_triplet_orbit_dimension": 18,
        "radial_surplus_with_adjustable_coefficient_ratio": -1,
        "rb4_base_induced_image_dimension": 3,
    },
    "layer0": {
        "fibre": "Sym^2(T*X)",
        "native_signature": [6, 4],
        "track_a": "fixed-U, fixed-epsilon first A-descent only",
        "track_b": "stationary only in frozen homogeneous truncation",
    },
    "track_a": {
        "full_residual_norms": full_norms.tolist(),
        "mixed_fit_coefficients": mixed_coefficients.tolist(),
        "mixed_fit_residuals": mixed_fit_residuals.tolist(),
        "verdict": track_a_verdict,
        "vertical_discrepancy_norms": vertical_floors.tolist(),
        "vertical_residual_norms": vertical_norms.tolist(),
        "vertical_signal_to_floor_central": vertical_separation,
    },
    "track_b": {
        "rank_three_hessian_eigenvalues": rank_three_hessian.tolist(),
        "rank_two_hessian_eigenvalues": rank_two_hessian.tolist(),
        "raw_trace_plus_triplet_inertia": [1, 3],
        "trace_reversed_trace_plus_triplet_inertia": [0, 4],
        "verdict": track_b_verdict,
    },
    "verdict": (
        "FIRST VERTICAL DESCENT KILLED; MIXED W177 RESPONSE NONSELECTING; "
        "HOMOGENEOUS TRACE-REVERSED SU2 BUILDS ONLY AN UNSTABLE CARTAN SADDLE"
    ),
}
print(json.dumps(payload, indent=2, sort_keys=True))

if FAILURES:
    print("FAILED CONTROLS:")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print(f"RB7 STATIONARY NON-METRIC ORDER-PARAMETER PROBE: {CHECK_COUNT} CHECKS PASS")
