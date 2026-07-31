#!/usr/bin/env python3
r"""RB3c: typed curvature vertex, Krein completion, and finite Green/Q join.

Layer 0
-------
The W125 gamma-traceless construction is a map

    T_b : S -> R = ker(Gamma) subset V* tensor S,

for each adjoint-valued curvature two-form coefficient ``b``.  It is not an
endomorphism of ``R``.  Consequently, the N1 display ``P_R T_b P_R`` is not
dimensionally meaningful for this owned construction: the right ``P_R`` has
domain ``V* tensor S``, while ``T_b`` has domain ``S``.

This probe keeps that type and constructs one honest finite full-carrier
completion on

    E_20 = S plus (V* tensor S) = S plus I plus R.

It uses the diagonal member ``G2=diag(1,1/14)`` of the already-written
full-20 Krein family and closes ``T_b`` with its Krein adjoint.  This proves
existence of one nondegenerate K-polarized S/R completion; it does not select
that member of the G2 family or identify it with a physical source term.

The bounded current/Green fixture below is conditional on that typed vertex.
One scalar Q_F amplitude is evaluated from the actual 128/1792-dimensional
Cl(9,5) matrices.  It is synchronized with a finite A0-induced reductive
connection realization and a planted abelianized one-dimensional
1/12/13-form polynomial profile.  The exterior reorder signs are the genuine
14-dimensional signs, but no full Q_F form, D_A^coad current, common
epsilon_IG map, Y14 domain/boundary, or density/Hodge variation is built.

The probe also keeps the native trace-reversed DeWitt fibre separate from the
raw Frobenius comparator as an independent compatibility check.  Its Hodge
operator is not applied in the polynomial Green fixture.  It makes no
stationarity, CME, domain, mass, index, generation-count, cosmological-value,
physical field-embedding, full-current, full-Sp-covariance, or
JD-versus-TOTAL selection claim.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import actual_sym2_c14_orbit_probe as sym2  # noqa: E402


TOL = 1.0e-8
FD_TOL = 3.0e-6
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def info(message: str) -> None:
    print(f"INFO: {message}")


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def matrix_product(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result @ matrix
    return result


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def spin_generator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return 0.25 * commutator(left, right)


def close(left: complex, right: complex, tolerance: float = TOL) -> bool:
    scale = max(1.0, abs(left), abs(right))
    return abs(left - right) <= tolerance * scale


print("=" * 104)
print("RB3c TYPED CURVATURE VERTEX / KREIN COMPLETION / FINITE GREEN-Q JOIN")
print("=" * 104)


# ---------------------------------------------------------------------------
# A. W125/N4a S -> R map and one finite full-20 K-polarized completion
# ---------------------------------------------------------------------------


print("\nA. Native W125/N4a type and S <-> R completion")

gammas, eta14 = sym2.native_gammas()
dimension_v = len(gammas)
dimension_s = gammas[0].shape[0]
dimension_vs = dimension_v * dimension_s
identity_s = np.eye(dimension_s, dtype=complex)

krein_s = matrix_product(gammas[:9])
j_quat = matrix_product(
    [gammas[index] for index in (1, 3, 5, 7, 10, 12)]
)
gamma_matrix = np.hstack(gammas)
j_matrix = np.vstack(
    [eta14[index] * gammas[index] for index in range(dimension_v)]
) / dimension_v


def gamma_operator(gamma_basis: list[np.ndarray]) -> np.ndarray:
    return np.hstack(gamma_basis)


def j_operator(gamma_basis: list[np.ndarray]) -> np.ndarray:
    return np.vstack(
        [
            eta14[index] * gamma_basis[index]
            for index in range(dimension_v)
        ]
    ) / dimension_v


def project_r(
    value: np.ndarray,
    gamma_basis: list[np.ndarray] = gammas,
) -> np.ndarray:
    """Apply P_R=1-j Gamma without materializing a 1792-square matrix."""
    gamma = gamma_operator(gamma_basis)
    j_map = j_operator(gamma_basis)
    return value - j_map @ (gamma @ value)


def krein_vs_apply(value: np.ndarray) -> np.ndarray:
    """Apply diag(eta_14) tensor K_S to a vector or column matrix."""
    was_vector = value.ndim == 1
    columns = 1 if was_vector else value.shape[1]
    reshaped = value.reshape(dimension_v, dimension_s, columns)
    result = np.stack(
        [
            eta14[index] * krein_s @ reshaped[index]
            for index in range(dimension_v)
        ]
    )
    flattened = result.reshape(dimension_vs, columns)
    return flattened[:, 0] if was_vector else flattened


def pair_s(left: np.ndarray, right: np.ndarray) -> complex:
    return complex(np.vdot(left, krein_s @ right))


def pair_vs(left: np.ndarray, right: np.ndarray) -> complex:
    return complex(np.vdot(left, krein_vs_apply(right)))


def pair_full(
    left_s: np.ndarray,
    left_vs: np.ndarray,
    right_s: np.ndarray,
    right_vs: np.ndarray,
) -> complex:
    return pair_s(left_s, right_s) + pair_vs(left_vs, right_vs)


def krein_adjoint_s_to_vs(operator: np.ndarray) -> np.ndarray:
    """K_S^{-1} T^dagger K_VS; K_S^{-1}=K_S in this basis."""
    return krein_s @ krein_vs_apply(operator).conj().T


def channel_parts(
    gamma_basis: list[np.ndarray],
    adjoint_generator: np.ndarray,
    pair: tuple[int, int] = (3, 4),
) -> tuple[np.ndarray, np.ndarray]:
    """The exact W125 contract/wedge maps for one two-form coefficient."""
    left, right = pair
    gamma_two = gamma_basis[left] @ gamma_basis[right]
    contract_blocks = []
    wedge_blocks = []
    for vector_index in range(dimension_v):
        if vector_index == left:
            contract = gamma_basis[right]
        elif vector_index == right:
            contract = -gamma_basis[left]
        else:
            contract = np.zeros_like(gamma_basis[0])
        wedge = (
            eta14[vector_index]
            * 0.5
            * (
                gamma_basis[vector_index] @ gamma_two
                + gamma_two @ gamma_basis[vector_index]
            )
        )
        # The fixed adjoint coefficient acts on S.  Keeping it on the
        # right preserves the W125 gamma-trace identity term by term.
        contract_blocks.append(contract @ adjoint_generator)
        wedge_blocks.append(wedge @ adjoint_generator)
    return np.vstack(contract_blocks), np.vstack(wedge_blocks)


rho_h = spin_generator(gammas[0], gammas[1])
rho_m1 = spin_generator(gammas[0], gammas[2])
rho_m2 = spin_generator(gammas[1], gammas[2])

check(
    "the native spinor data are Cl(9,5), Hermitian Krein, and quaternionic",
    sym2.clifford_defect(gammas, eta14) < TOL
    and max_abs(krein_s - krein_s.conj().T) < TOL
    and max_abs(krein_s @ krein_s - identity_s) < TOL
    and max_abs(j_quat @ j_quat.conj() + identity_s) < TOL,
)
check(
    "the selected adjoint direction is right-H linear and Krein-skew",
    max_abs(rho_h @ j_quat - j_quat @ rho_h.conj()) < TOL
    and max_abs(rho_h.conj().T @ krein_s + krein_s @ rho_h) < TOL,
)
check(
    "the native h/m spin generators close the same so(3) brackets",
    max_abs(commutator(rho_h, rho_m1) + rho_m2) < TOL
    and max_abs(commutator(rho_h, rho_m2) - rho_m1) < TOL
    and max_abs(commutator(rho_m1, rho_m2) + rho_h) < TOL,
)

contract_map, wedge_map = channel_parts(gammas, rho_h)
gamma_contract = gamma_matrix @ contract_map
gamma_wedge = gamma_matrix @ wedge_map
least_squares_coefficient = complex(
    -np.vdot(gamma_wedge, gamma_contract)
    / np.vdot(gamma_wedge, gamma_wedge)
)
typed_raw = contract_map - wedge_map / 6.0
wrong_raw = contract_map
typed_map = project_r(typed_raw)
wrong_projected = project_r(wrong_raw)

check(
    "the unique gamma-trace coefficient is exactly -1/6",
    abs(least_squares_coefficient + 1.0 / 6.0) < 1.0e-12,
    f"t*={least_squares_coefficient.real:.12f}",
)
check(
    "contract-(1/6)wedge lands in R before projection",
    np.linalg.norm(gamma_matrix @ typed_raw) < TOL
    and np.linalg.norm(typed_map - typed_raw) < TOL,
    (
        f"gamma leak={np.linalg.norm(gamma_matrix @ typed_raw):.2e}, "
        f"projection shift={np.linalg.norm(typed_map - typed_raw):.2e}"
    ),
)
check(
    "the wrong coefficient is gamma-traceful and needs a nontrivial projection",
    np.linalg.norm(gamma_matrix @ wrong_raw) > 1.0
    and np.linalg.norm(wrong_projected - wrong_raw) > 1.0,
    (
        f"wrong leak={np.linalg.norm(gamma_matrix @ wrong_raw):.6f}, "
        f"wrong shift={np.linalg.norm(wrong_projected - wrong_raw):.6f}"
    ),
)

rng = np.random.default_rng(20260730)
projector_seed = (
    rng.standard_normal((dimension_vs, 3))
    + 1j * rng.standard_normal((dimension_vs, 3))
)
projected_seed = project_r(projector_seed)
left_seed = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
right_seed = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
check(
    "P_R is an idempotent gamma-trace projector and Gamma j=1",
    np.linalg.norm(project_r(projected_seed) - projected_seed) < 2.0e-8
    and np.linalg.norm(gamma_matrix @ projected_seed) < 2.0e-8
    and max_abs(gamma_matrix @ j_matrix - identity_s) < TOL,
)
check(
    "P_R is self-adjoint for the native vector-spinor Krein pairing",
    close(
        pair_vs(left_seed, project_r(right_seed[:, None])[:, 0]),
        pair_vs(project_r(left_seed[:, None])[:, 0], right_seed),
        2.0e-8,
    ),
)

right_sandwich_rejected = False
try:
    _ = typed_map @ np.zeros((dimension_vs, 1), dtype=complex)
except ValueError:
    right_sandwich_rejected = True
check(
    "Layer-0 rejects the dimensionally invalid P_R T_b P_R sandwich",
    typed_map.shape == (dimension_vs, dimension_s)
    and right_sandwich_rejected,
    f"T_b shape={typed_map.shape}, right P_R domain={dimension_vs}",
)
check(
    "the typed S -> R map is nonzero and full column rank",
    np.linalg.norm(typed_map) > 1.0
    and np.linalg.matrix_rank(typed_map, tol=TOL) == dimension_s,
)
completion_rank = 2 * np.linalg.matrix_rank(typed_map, tol=TOL)
completion_kernel = dimension_s + dimension_vs - completion_rank
check(
    "the off-diagonal completion is rank 256 with kernel 1664, not a nondegenerate operator",
    completion_rank == 256 and completion_kernel == 1664,
    f"rank={completion_rank}, kernel={completion_kernel}",
)

right_h_defect_t = max(
    max_abs(
        typed_map[
            index * dimension_s : (index + 1) * dimension_s
        ]
        @ j_quat
        - j_quat
        @ typed_map[
            index * dimension_s : (index + 1) * dimension_s
        ].conj()
    )
    for index in range(dimension_v)
)
typed_reverse = krein_adjoint_s_to_vs(typed_map)
right_h_defect_reverse = max(
    max_abs(
        typed_reverse[
            :, index * dimension_s : (index + 1) * dimension_s
        ]
        @ j_quat
        - j_quat
        @ typed_reverse[
            :, index * dimension_s : (index + 1) * dimension_s
        ].conj()
    )
    for index in range(dimension_v)
)
check(
    "T_b and its Krein reverse are both right-H linear",
    right_h_defect_t < TOL and right_h_defect_reverse < TOL,
    f"T={right_h_defect_t:.2e}, T-cross={right_h_defect_reverse:.2e}",
)

spinor_seed = (
    rng.standard_normal(dimension_s)
    + 1j * rng.standard_normal(dimension_s)
)
vector_spinor_seed = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
check(
    "T-cross is the exact native Krein adjoint of T",
    close(
        pair_vs(vector_spinor_seed, typed_map @ spinor_seed),
        pair_s(typed_reverse @ vector_spinor_seed, spinor_seed),
        2.0e-8,
    ),
)
hilbert_reverse = typed_map.conj().T
krein_eigenvalues = np.linalg.eigvalsh(krein_s)
spin_positive = int(np.sum(krein_eigenvalues > 0.5))
spin_negative = int(np.sum(krein_eigenvalues < -0.5))
negative_gamma_hilbert_defect = max(
    max_abs(gamma.conj().T - gamma)
    for gamma, sign in zip(gammas, eta14)
    if sign < 0
)
check(
    "the T-reverse coincidence does not replace the indefinite Krein form",
    np.linalg.norm(hilbert_reverse - typed_reverse) < TOL
    and spin_positive == 64
    and spin_negative == 64
    and negative_gamma_hilbert_defect > 1.0,
    (
        "T-cross=T-dagger on this channel, while "
        f"K signature=(64,64) and negative-gamma Hilbert defect="
        f"{negative_gamma_hilbert_defect:.2f}"
    ),
)


def apply_full20_vertex(
    forward: np.ndarray,
    reverse: np.ndarray,
    spinor: np.ndarray,
    vector_spinor: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    return reverse @ vector_spinor, forward @ spinor


left_s = (
    rng.standard_normal(dimension_s)
    + 1j * rng.standard_normal(dimension_s)
)
left_vs = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
right_s = (
    rng.standard_normal(dimension_s)
    + 1j * rng.standard_normal(dimension_s)
)
right_vs = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
v_right_s, v_right_vs = apply_full20_vertex(
    typed_map, typed_reverse, right_s, right_vs
)
v_left_s, v_left_vs = apply_full20_vertex(
    typed_map, typed_reverse, left_s, left_vs
)
check(
    "the off-diagonal S/R completion is K-self-adjoint on full E20",
    close(
        pair_full(left_s, left_vs, v_right_s, v_right_vs),
        pair_full(v_left_s, v_left_vs, right_s, right_vs),
        2.0e-8,
    ),
)
i_seed = j_matrix @ spinor_seed
check(
    "the completion has only S <-> R blocks and annihilates I in reverse",
    np.linalg.norm(gamma_matrix @ (typed_map @ spinor_seed)) < TOL
    and np.linalg.norm(typed_reverse @ i_seed) < TOL,
)

# The vector-spinor form induces K/14 on I, so this is exactly the
# alpha=beta=1, zeta=0 member of the written G2 family.
g2_diagonal = np.array([[1.0, 0.0], [0.0, 1.0 / 14.0]])
vector_spinor_positive = (
    int(np.sum(eta14 > 0)) * spin_positive
    + int(np.sum(eta14 < 0)) * spin_negative
)
vector_spinor_negative = (
    int(np.sum(eta14 > 0)) * spin_negative
    + int(np.sum(eta14 < 0)) * spin_positive
)
i_positive, i_negative = spin_positive, spin_negative
r_positive = vector_spinor_positive - i_positive
r_negative = vector_spinor_negative - i_negative
e20_positive = spin_positive + vector_spinor_positive
e20_negative = spin_negative + vector_spinor_negative
check(
    "the chosen diagonal G2 member is nondegenerate and the full signatures close",
    abs(np.linalg.det(g2_diagonal) - 1.0 / 14.0) < TOL
    and (i_positive, i_negative) == (64, 64)
    and (r_positive, r_negative) == (832, 832)
    and (e20_positive, e20_negative) == (960, 960),
    (
        f"S=({spin_positive},{spin_negative}), "
        f"I=({i_positive},{i_negative}), "
        f"R=({r_positive},{r_negative}), "
        f"E20=({e20_positive},{e20_negative})"
    ),
)
info(
    "constructed one diagonal-G2 S<->R completion; the four-real-parameter "
    "G2 family and the overall lambda_F remain charged"
)


# ---------------------------------------------------------------------------
# B. Native DeWitt geometry and the raw-Frobenius hostile comparator
# ---------------------------------------------------------------------------


print("\nB. DeWitt trace reversal and Hodge-sign control")


def raw_frobenius(h: np.ndarray, k: np.ndarray) -> float:
    eta4 = sym2.ETA4
    return float(np.trace(eta4 @ h @ eta4 @ k))


def signature(matrix: np.ndarray) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(matrix)
    return (
        int(np.sum(eigenvalues > TOL)),
        int(np.sum(eigenvalues < -TOL)),
        int(np.sum(np.abs(eigenvalues) <= TOL)),
    )


def star_square(dimension: int, degree: int, negative: int) -> int:
    return -1 if (degree * (dimension - degree) + negative) % 2 else 1


dewitt_gram = np.array(
    [
        [sym2.dewitt(left, right) for right in sym2.DEWITT_FRAME]
        for left in sym2.DEWITT_FRAME
    ]
)
frobenius_gram = np.array(
    [
        [raw_frobenius(left, right) for right in sym2.DEWITT_FRAME]
        for left in sym2.DEWITT_FRAME
    ]
)
check(
    "actual Sym2 DeWitt fibre has signature (6,4), hence ambient (9,5)",
    signature(dewitt_gram) == (6, 4, 0)
    and (3 + 6, 1 + 4) == (9, 5),
)
check(
    "raw Frobenius instead has fibre (7,3), hence hostile ambient (10,4)",
    signature(frobenius_gram) == (7, 3, 0)
    and (3 + 7, 1 + 3) == (10, 4),
)
check(
    "native (9,5) Hodge signs are + on 1/13 and - on 2/12",
    star_square(14, 1, 5) == 1
    and star_square(14, 13, 5) == 1
    and star_square(14, 2, 5) == -1
    and star_square(14, 12, 5) == -1,
)
check(
    "raw-Frobenius (10,4) reverses both relevant Hodge-sign classes",
    star_square(14, 1, 4) == -1
    and star_square(14, 13, 4) == -1
    and star_square(14, 2, 4) == 1
    and star_square(14, 12, 4) == 1,
)

eta4 = sym2.ETA4
h_trace = -eta4 / 4.0
trace_test = np.array(
    [
        [0.7, 0.2, 0.0, -0.1],
        [0.2, -0.3, 0.4, 0.0],
        [0.0, 0.4, 0.9, 0.3],
        [-0.1, 0.0, 0.3, -0.2],
    ]
)
tau_test = float(np.trace(eta4 @ trace_test) / 4.0)
check(
    "h_trace=-g/4 is the DeWitt dual of tau=tr_g/4",
    abs(sym2.dewitt(h_trace, trace_test) - tau_test) < TOL,
)
check(
    "the raw Frobenius musical gives -tau and is rejected linearly",
    abs(raw_frobenius(h_trace, trace_test) + tau_test) < TOL
    and abs(tau_test) > 0.1,
    f"tau={tau_test:.6f}",
)


# ---------------------------------------------------------------------------
# C. A0-induced connection: L, formal adjoint, and Green boundary owner
# ---------------------------------------------------------------------------


print("\nC. A0-induced reductive connection and its Green formula")


def so_generator(left: int, right: int) -> np.ndarray:
    result = np.zeros((3, 3))
    result[left, right] = 1.0
    result[right, left] = -1.0
    return result


h_generator = so_generator(0, 1)
m1_generator = so_generator(0, 2)
m2_generator = so_generator(1, 2)


def kappa(left: np.ndarray, right: np.ndarray) -> float:
    return float(-0.5 * np.trace(left @ right))


def project_h(matrix: np.ndarray) -> np.ndarray:
    return kappa(h_generator, matrix) * h_generator


def project_m(matrix: np.ndarray) -> np.ndarray:
    return matrix - project_h(matrix)


check(
    "the finite A0 h/m basis has the same brackets as its native spin lift",
    max_abs(commutator(h_generator, m1_generator) + m2_generator) < TOL
    and max_abs(commutator(h_generator, m2_generator) - m1_generator) < TOL
    and max_abs(commutator(m1_generator, m2_generator) + h_generator) < TOL,
)


def omega_coefficient(x: float) -> float:
    return 0.31 + 0.17 * x


def beta_coefficient(x: float) -> float:
    return 0.43 - 0.11 * x + 0.07 * x * x


def xi_coefficient(x: float) -> float:
    return 0.23 + 0.71 * x + 0.19 * x * x


def xi_coefficient_prime(x: float) -> float:
    return 0.71 + 0.38 * x


def omega_at(x: float) -> np.ndarray:
    return omega_coefficient(x) * h_generator


def beta_at(x: float) -> np.ndarray:
    return beta_coefficient(x) * m1_generator


def xi_at(x: float) -> np.ndarray:
    return xi_coefficient(x) * m2_generator


def xi_prime_at(x: float) -> np.ndarray:
    return xi_coefficient_prime(x) * m2_generator


def l_a0(x: float) -> np.ndarray:
    """L_A0 xi=-D_omega xi+pr_h[beta,xi] at the identity lift."""
    return (
        -xi_prime_at(x)
        - commutator(omega_at(x), xi_at(x))
        + project_h(commutator(beta_at(x), xi_at(x)))
    )


def exp_m2(angle: float) -> np.ndarray:
    return (
        np.eye(3)
        + np.sin(angle) * m2_generator
        + (1.0 - np.cos(angle)) * (m2_generator @ m2_generator)
    )


def gamma_a0(parameter: float, x: float) -> np.ndarray:
    """Gamma=A0-g pr_m(g^-1 A0 g+g^-1 dg)g^-1."""
    f_value = xi_coefficient(x)
    f_prime = xi_coefficient_prime(x)
    group = exp_m2(parameter * f_value)
    inverse = group.T
    group_prime = group @ (parameter * f_prime * m2_generator)
    a_zero = omega_at(x) + beta_at(x)
    b_zero = inverse @ a_zero @ group + inverse @ group_prime
    return a_zero - group @ project_m(b_zero) @ inverse


connection_step = 1.0e-6
connection_grid = np.linspace(0.0, 1.0, 17)
connection_fd_defect = max(
    max_abs(
        (
            gamma_a0(connection_step, x)
            - gamma_a0(-connection_step, x)
        )
        / (2.0 * connection_step)
        - l_a0(x)
    )
    for x in connection_grid
)
check(
    "finite-differencing the literal A0 connection reproduces L_A0",
    connection_fd_defect < 2.0e-8,
    f"max defect={connection_fd_defect:.2e}",
)


def eta_m_at(x: float) -> np.ndarray:
    return (
        (0.19 + 0.13 * x * x) * m1_generator
        + (-0.17 + 0.61 * x + 0.29 * x * x) * m2_generator
    )


def eta_m_prime_at(x: float) -> np.ndarray:
    return (
        (0.26 * x) * m1_generator
        + (0.61 + 0.58 * x) * m2_generator
    )


def eta_h_at(x: float) -> np.ndarray:
    return (0.37 - 0.23 * x + 0.17 * x * x) * h_generator


def l_a0_adjoint(x: float) -> np.ndarray:
    """D_omega eta_m + ad_beta^! eta_h in this invariant pairing."""
    return project_m(
        eta_m_prime_at(x)
        + commutator(omega_at(x), eta_m_at(x))
        + commutator(eta_h_at(x), beta_at(x))
    )


quadrature_nodes_raw, quadrature_weights_raw = np.polynomial.legendre.leggauss(48)
quadrature_nodes = (quadrature_nodes_raw + 1.0) / 2.0
quadrature_weights = quadrature_weights_raw / 2.0


def integrate_numeric(function) -> float:
    return float(
        sum(
            weight * float(function(float(x)))
            for x, weight in zip(quadrature_nodes, quadrature_weights)
        )
    )


green_left = integrate_numeric(
    lambda x: kappa(eta_m_at(x) + eta_h_at(x), l_a0(x))
)
green_bulk = integrate_numeric(
    lambda x: kappa(l_a0_adjoint(x), xi_at(x))
)
green_boundary = (
    kappa(eta_m_at(0.0), xi_at(0.0))
    - kappa(eta_m_at(1.0), xi_at(1.0))
)
wrong_adjoint_bulk = integrate_numeric(
    lambda x: kappa(
        project_m(
            eta_m_prime_at(x)
            + commutator(omega_at(x), eta_m_at(x))
        ),
        xi_at(x),
    )
)
check(
    "L_A0 and L_A0-adjoint satisfy the finite Green identity",
    abs(green_left - green_bulk - green_boundary) < 2.0e-12,
    (
        f"left={green_left:.9f}, bulk={green_bulk:.9f}, "
        f"boundary={green_boundary:.9f}"
    ),
)
check(
    "the beta-adjoint term and boundary term are both load-bearing",
    abs(green_left - wrong_adjoint_bulk - green_boundary) > 1.0e-3
    and abs(green_left - green_bulk) > 1.0e-3
    and abs(green_boundary) > 1.0e-3,
)


# ---------------------------------------------------------------------------
# D. One typed Q_F amplitude and a planted 14D Green-algebra fixture
# ---------------------------------------------------------------------------


print("\nD. One Q_F amplitude and synchronized finite Green/chain-rule fixture")

x_mover = gammas[0] @ gammas[1] @ gammas[2]
check(
    "the moving-Clifford generator is K-skew and right-H linear",
    max_abs(x_mover.conj().T @ krein_s + krein_s @ x_mover) < TOL
    and max_abs(x_mover @ j_quat - j_quat @ x_mover.conj()) < TOL
    and max_abs(x_mover @ x_mover + identity_s) < TOL,
)


def mover(parameter: float) -> np.ndarray:
    return (
        np.cos(parameter) * identity_s
        + np.sin(parameter) * x_mover
    )


def moved_gammas(parameter: float) -> list[np.ndarray]:
    group = mover(parameter)
    inverse = mover(-parameter)
    return [group @ gamma @ inverse for gamma in gammas]


@lru_cache(maxsize=None)
def typed_map_at(parameter: float) -> np.ndarray:
    gamma_basis = moved_gammas(parameter)
    contract, wedge = channel_parts(gamma_basis, rho_h)
    raw = contract - wedge / 6.0
    # P_R is kept literally in the construction even though the 1/6
    # identity makes this projection numerically inert on the base stratum.
    return project_r(raw, gamma_basis)


z_spinor = (
    rng.standard_normal(dimension_s)
    + 1j * rng.standard_normal(dimension_s)
)
z_vector_spinor = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
z_spinor /= np.linalg.norm(z_spinor)
z_vector_spinor /= np.linalg.norm(z_vector_spinor)


@lru_cache(maxsize=None)
def typed_q_coefficient(parameter: float) -> float:
    forward = typed_map_at(parameter)
    reverse = krein_adjoint_s_to_vs(forward)
    out_s, out_vs = apply_full20_vertex(
        forward, reverse, z_spinor, z_vector_spinor
    )
    # lambda_F=1 and the ambient density is the fixed unit density in this
    # finite local frame.  Both K_E and V_b are therefore present literally.
    return 0.5 * float(
        pair_full(
            z_spinor,
            z_vector_spinor,
            out_s,
            out_vs,
        ).real
    )


vertex_step = 2.0e-6
q_zero = typed_q_coefficient(0.0)
q_derivative = (
    typed_q_coefficient(vertex_step)
    - typed_q_coefficient(-vertex_step)
) / (2.0 * vertex_step)
check(
    "the typed full-20 completion emits one nonzero Q_F scalar amplitude",
    abs(q_zero) > 1.0e-5,
    f"q(0)={q_zero:.9f}",
)
check(
    "the moved raw typed map gives a live amplitude response at fixed K_E/Z/b/density",
    abs(q_derivative) > 1.0e-5
    and np.linalg.norm(typed_map_at(vertex_step) - typed_map_at(-vertex_step))
    / (2.0 * vertex_step)
    > 1.0,
    f"q-dot={q_derivative:.9f}",
)
check(
    "the moved typed map remains gamma-traceless and right-H linear",
    np.linalg.norm(
        gamma_operator(moved_gammas(vertex_step))
        @ typed_map_at(vertex_step)
    )
    < 2.0e-8
    and max(
        max_abs(
            typed_map_at(vertex_step)[
                index * dimension_s : (index + 1) * dimension_s
            ]
            @ j_quat
            - j_quat
            @ typed_map_at(vertex_step)[
                index * dimension_s : (index + 1) * dimension_s
            ].conj()
        )
        for index in range(dimension_v)
    )
    < TOL,
)
moving_projector_seed = (
    rng.standard_normal(dimension_vs)
    + 1j * rng.standard_normal(dimension_vs)
)
moving_projector_response = (
    project_r(
        moving_projector_seed[:, None],
        moved_gammas(vertex_step),
    )
    - project_r(
        moving_projector_seed[:, None],
        moved_gammas(-vertex_step),
    )
) / (2.0 * vertex_step)
raw_plus = (
    channel_parts(moved_gammas(vertex_step), rho_h)[0]
    - channel_parts(moved_gammas(vertex_step), rho_h)[1] / 6.0
)
raw_minus = (
    channel_parts(moved_gammas(-vertex_step), rho_h)[0]
    - channel_parts(moved_gammas(-vertex_step), rho_h)[1] / 6.0
)
projector_channel_derivative = (
    (typed_map_at(vertex_step) - raw_plus)
    - (typed_map_at(-vertex_step) - raw_minus)
) / (2.0 * vertex_step)
check(
    "generic P_R moves but delta(P_R) T_b=0 on the exact 1/6 family",
    np.linalg.norm(moving_projector_response) > 1.0
    and np.linalg.norm(projector_channel_derivative) < TOL
    and np.linalg.norm(
        typed_map_at(vertex_step)
        - raw_plus
    )
    < 2.0e-8,
    (
        f"||P_R-dot seed||={np.linalg.norm(moving_projector_response):.6f}; "
        f"||delta(P_R)T_b||={np.linalg.norm(projector_channel_derivative):.2e}"
    ),
)


def polynomial_derivative(
    coefficients: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        Fraction(power) * coefficient
        for power, coefficient in enumerate(coefficients)
        if power > 0
    )


def polynomial_product(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return tuple(result)


def integrate_unit(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        (
            coefficient / Fraction(power + 1)
            for power, coefficient in enumerate(coefficients)
        ),
        Fraction(0),
    )


def evaluate_polynomial(
    coefficients: tuple[Fraction, ...],
    value: Fraction,
) -> Fraction:
    return sum(
        (
            coefficient * value**power
            for power, coefficient in enumerate(coefficients)
        ),
        Fraction(0),
    )


def evaluate_polynomial_float(
    coefficients: tuple[Fraction, ...],
    value: float,
) -> float:
    return float(
        sum(
            float(coefficient) * value**power
            for power, coefficient in enumerate(coefficients)
        )
    )


def exterior_reorder_sign(indices: tuple[int, ...]) -> int:
    if len(indices) != len(set(indices)):
        return 0
    inversions = sum(
        indices[left] > indices[right]
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


theta_poly = (Fraction(1), Fraction(0), Fraction(1))
q_poly = (Fraction(0), Fraction(2), Fraction(0), Fraction(1))
theta_prime_poly = polynomial_derivative(theta_poly)
q_prime_poly = polynomial_derivative(q_poly)
sign_dtheta_q = exterior_reorder_sign(
    (13, 0) + tuple(range(1, 13))
)
sign_theta_dq = exterior_reorder_sign(
    (0, 13) + tuple(range(1, 13))
)
sign_boundary = exterior_reorder_sign((13,) + tuple(range(13)))

base_bulk = sign_dtheta_q * integrate_unit(
    polynomial_product(theta_prime_poly, q_poly)
)
base_interior = sign_theta_dq * integrate_unit(
    polynomial_product(theta_poly, q_prime_poly)
)
base_boundary = sign_boundary * (
    evaluate_polynomial(theta_poly, Fraction(1))
    * evaluate_polynomial(q_poly, Fraction(1))
    - evaluate_polynomial(theta_poly, Fraction(0))
    * evaluate_polynomial(q_poly, Fraction(0))
)
check(
    "the planted 14D wedge order gives signs (-1,+1,-1)",
    (sign_dtheta_q, sign_theta_dq, sign_boundary) == (-1, 1, -1),
)
check(
    "the planted 1/12/13-form polynomial Green identity retains its endpoint term",
    base_bulk == base_boundary + base_interior
    and base_boundary != 0,
)


def theta_coefficient(parameter: float, x: float) -> float:
    """theta(t)=theta(0)-(Gamma(t)-Gamma(0)) in the H direction."""
    return evaluate_polynomial_float(theta_poly, x) - kappa(
        h_generator,
        gamma_a0(parameter, x) - gamma_a0(0.0, x),
    )


def delta_action(parameter: float) -> float:
    """Delta S=-J_F[theta]=-integral theta wedge D Q_F."""
    # This is the literal fixed-H, A=0 sub-stratum, so D_A on the H*
    # coefficient reduces to the exterior derivative.  The non-Abelian A0
    # dependence remains in Gamma(epsilon,A0) and hence in theta.
    q_value = typed_q_coefficient(parameter)
    return -sign_theta_dq * integrate_numeric(
        lambda x: theta_coefficient(parameter, x)
        * q_value
        * evaluate_polynomial_float(q_prime_poly, x)
    )


bridge_step = vertex_step
delta_action_fd = (
    delta_action(bridge_step) - delta_action(-bridge_step)
) / (2.0 * bridge_step)
connection_response = sign_theta_dq * integrate_numeric(
    lambda x: kappa(h_generator, l_a0(x))
    * q_zero
    * evaluate_polynomial_float(q_prime_poly, x)
)
moving_current_response = -sign_theta_dq * integrate_numeric(
    lambda x: evaluate_polynomial_float(theta_poly, x)
    * q_derivative
    * evaluate_polynomial_float(q_prime_poly, x)
)
delta_epsilon_literal = connection_response + moving_current_response
check(
    "the synchronized one-parameter fixture obeys the candidate chain rule",
    abs(delta_action_fd - delta_epsilon_literal)
    < FD_TOL * max(1.0, abs(delta_action_fd)),
    (
        f"finite={delta_action_fd:.9f}, "
        f"L/J_F + moving-Q={delta_epsilon_literal:.9f}"
    ),
)
check(
    "freezing the matrix-derived amplitude loses a nonzero response",
    abs(delta_action_fd - connection_response) > 1.0e-4,
    (
        f"full={delta_action_fd:.9f}, "
        f"frozen-current={connection_response:.9f}"
    ),
)

moving_bulk = float(base_bulk) * q_derivative
moving_interior = float(base_interior) * q_derivative
moving_boundary = float(base_boundary) * q_derivative
moving_direct = -moving_interior
moving_green = -moving_bulk + moving_boundary
check(
    "the moving-amplitude term agrees in direct and Green-expanded form",
    abs(moving_direct - moving_green) < 1.0e-12
    and abs(
        delta_epsilon_literal
        - (connection_response + moving_green)
    )
    < 1.0e-12,
)
check(
    "dropping the planted endpoint term changes the finite comparator response",
    abs(moving_boundary) > 1.0e-5
    and abs(moving_direct - (-moving_bulk)) > 1.0e-5,
    f"boundary contribution={moving_boundary:.9f}",
)
info(
    "the scalar amplitude used final P_R, the typed V_b, diagonal K_E, "
    "fixed Z/b/rho_h, and fixed unit density; no full Q_F form, common "
    "epsilon_IG mover, D_A current, or density variation was constructed"
)


# ---------------------------------------------------------------------------
# Verdict
# ---------------------------------------------------------------------------


print("\n" + "=" * 104)
if FAILURES:
    print(f"EARLIEST EXECUTABLE OBSTRUCTION: {FAILURES[0]}")
    print(f"FAILED CHECKS ({len(FAILURES)}):")
    for failure in FAILURES:
        print(f"  - {failure}")
    raise SystemExit(1)

print("VERDICT: W125/N4a IS S->R, NOT AN R->R ENDOMORPHISM")
print(
    "CONSTRUCTED: ONE DIAGONAL-G2 S<->R KREIN-ADJOINT COMPLETION; "
    "THE G2-PLUS-R PAIRING, NOT THE RANK-256 VERTEX, IS NONDEGENERATE"
)
print(
    "CONSTRUCTED: ONE MATRIX Q_F AMPLITUDE + ONE 1D A0 "
    "L/L-ADJOINT/GREEN + SYNCHRONIZED CHAIN-RULE FIXTURE"
)
print(
    "NONCLAIM: NO PHYSICAL S+R EMBEDDING, FULL Q_F/D_A CURRENT, COMMON "
    "EPSILON_IG, Y14 DOMAIN/BOUNDARY, DENSITY VARIATION, FULL-SP COVARIANCE, "
    "UNIQUE POLARIZATION, JD/TOTAL SELECTION, VEV/MASS, STATIONARITY/CME, "
    "INDEX/COUNT, OR COSMOLOGICAL VALUE"
)
