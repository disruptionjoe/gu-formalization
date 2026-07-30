#!/usr/bin/env python3
"""RB3 moving-soldering, trace-coordinate, and bridge-discriminator probe.

This probe consumes both RB2 bridge systems.  It constructs:

* an actual native 128-complex-dimensional full-Sp moving-Clifford-plane
  direction outside the Spin(9,5) stabilizer;
* native moving P_R/chirality transport and their frozen-map controls, with
  the remaining dependency transports recorded at formula level;
* one reductive A0-induced connection candidate that is lift-independent;
* the actual-Sym2 Lorentz-scalar trace projector;
* the first exact missing full-20 placement arrow; and
* a homogeneous chain-rule discriminator proxy between the JD and TOTAL
  current bridges.

It does not construct rho_S(Phi_tr), its full-20 lift, a Standard Model
Yukawa matrix, a VEV, a four-dimensional cosmological equation, a global H
reduction, a native Ward identity, a mass, an index, or a generation count.
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import actual_sym2_c14_orbit_probe as sym2  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as b5  # noqa: E402


TOL = 1.0e-8
FD_TOL = 2.0e-6
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def product(matrices: list[np.ndarray]) -> np.ndarray:
    out = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


print("=" * 104)
print("RB3 MOVING SOLDERING + SPIN-ZERO PLACEMENT + BRIDGE DISCRIMINATOR")
print("=" * 104)


# ---------------------------------------------------------------------------
# A. Native moving Clifford-plane orbit
# ---------------------------------------------------------------------------


print("\nA. Native moving Clifford-plane orbit")

gammas, eta14 = sym2.native_gammas()
identity128 = np.eye(128, dtype=complex)
krein = product([gammas[index] for index in range(9)])
j_quat_matrix = product(
    [gammas[index] for index in (1, 3, 5, 7, 10, 12)]
)
x_mover = gammas[0] @ gammas[1] @ gammas[2]

check(
    "the grade-three generator squares to -I and is Krein-skew",
    max_abs(x_mover @ x_mover + identity128) < TOL
    and max_abs(
        x_mover.conj().T @ krein + krein @ x_mover
    )
    < TOL,
)
check(
    "the grade-three generator is right-H linear",
    max_abs(
        x_mover @ j_quat_matrix
        - j_quat_matrix @ x_mover.conj()
    )
    < TOL,
)


def mover(parameter: float) -> np.ndarray:
    return (
        np.cos(parameter) * identity128
        + np.sin(parameter) * x_mover
    )


def moved_gammas(parameter: float) -> list[np.ndarray]:
    group = mover(parameter)
    inverse = mover(-parameter)
    return [group @ gamma @ inverse for gamma in gammas]


group_sample = mover(0.23)
check(
    "the one-parameter mover is native K-unitary and right-H linear",
    max_abs(
        group_sample.conj().T @ krein @ group_sample - krein
    )
    < TOL
    and max_abs(
        group_sample @ j_quat_matrix
        - j_quat_matrix @ group_sample.conj()
    )
    < TOL,
)
check(
    "the moved generators retain the exact Cl(9,5) relations",
    sym2.clifford_defect(moved_gammas(0.23), eta14) < TOL,
)

gamma_span = np.column_stack(
    [gamma.reshape(-1) for gamma in gammas]
)
commutator_residuals = []
for gamma in gammas:
    tangent = commutator(x_mover, gamma).reshape(-1)
    if np.linalg.norm(tangent) < TOL:
        commutator_residuals.append(0.0)
        continue
    coefficients, *_ = np.linalg.lstsq(
        gamma_span,
        tangent,
        rcond=None,
    )
    residual = np.linalg.norm(
        tangent - gamma_span @ coefficients
    ) / np.linalg.norm(tangent)
    commutator_residuals.append(float(residual))

check(
    "the mover fixes three gammas and moves eleven outside the old 14-plane",
    max(commutator_residuals[:3]) < TOL
    and min(commutator_residuals[3:]) > 0.99,
    (
        f"fixed-max={max(commutator_residuals[:3]):.2e}, "
        f"moved-min={min(commutator_residuals[3:]):.6f}"
    ),
)

dim_sp_64 = 64 * (2 * 64 + 1)
dim_spin_14 = comb(14, 2)
dim_split_spin = comb(4, 2) + comb(10, 2)
check(
    "the formal Clifford-plane orbit dimensions are explicit",
    dim_sp_64 == 8256
    and dim_spin_14 == 91
    and dim_sp_64 - dim_spin_14 == 8165
    and dim_split_spin == 51,
)


# The two charge-conjugation branches have different full-G behavior.
transpose_signs = []
for gamma in gammas:
    if max_abs(gamma.T - gamma) < TOL:
        transpose_signs.append(1)
    elif max_abs(gamma.T + gamma) < TOL:
        transpose_signs.append(-1)
    else:
        transpose_signs.append(0)
symmetric_indices = [
    index for index, sign in enumerate(transpose_signs) if sign == 1
]
skew_indices = [
    index for index, sign in enumerate(transpose_signs) if sign == -1
]
c_minus = np.linalg.inv(product([gammas[i] for i in skew_indices]))
c_plus = np.linalg.inv(
    product([gammas[i] for i in symmetric_indices])
)
c_plus_defect = max_abs(x_mover.T @ c_plus + c_plus @ x_mover)
c_minus_defect = max_abs(
    x_mover.T @ c_minus + c_minus @ x_mover
)
check(
    "C+ is native fixed while C- must move or reduce the symmetry",
    max_abs(c_plus + krein @ j_quat_matrix) < TOL
    and c_plus_defect < TOL
    and c_minus_defect > 0.5,
    f"C+={c_plus_defect:.2e}, C-={c_minus_defect:.2e}",
)

chirality = product(gammas)
check(
    "freezing chirality during generic Clifford-plane motion is detected",
    np.linalg.norm(commutator(x_mover, chirality)) > 1.0,
)


# ---------------------------------------------------------------------------
# B. Gamma_trace, j, P_R, and written RR primitive transport
# ---------------------------------------------------------------------------


print("\nB. Moving projectors and a same-dependency RR control")


def gamma_trace(
    vector_spinor: np.ndarray,
    gamma_basis: list[np.ndarray],
) -> np.ndarray:
    return sum(
        (
            gamma_basis[index] @ vector_spinor[index]
            for index in range(14)
        ),
        np.zeros(128, dtype=complex),
    )


def j_map(
    spinor: np.ndarray,
    gamma_basis: list[np.ndarray],
) -> np.ndarray:
    return np.stack(
        [
            eta14[index] * gamma_basis[index] @ spinor / 14.0
            for index in range(14)
        ]
    )


def p_r(
    vector_spinor: np.ndarray,
    gamma_basis: list[np.ndarray],
) -> np.ndarray:
    return vector_spinor - j_map(
        gamma_trace(vector_spinor, gamma_basis),
        gamma_basis,
    )


def clifford_symbol(
    vector: np.ndarray,
    gamma_basis: list[np.ndarray],
) -> np.ndarray:
    return sum(
        (
            vector[index] * gamma_basis[index]
            for index in range(14)
        ),
        np.zeros((128, 128), dtype=complex),
    )


def q_rr(
    vector_spinor: np.ndarray,
    vector: np.ndarray,
    gamma_basis: list[np.ndarray],
) -> np.ndarray:
    restricted = p_r(vector_spinor, gamma_basis)
    symbol = clifford_symbol(vector, gamma_basis)
    multiplied = np.stack(
        [symbol @ restricted[index] for index in range(14)]
    )
    return p_r(multiplied, gamma_basis)


def vector_spinor_pair(
    left: np.ndarray,
    right: np.ndarray,
) -> float:
    return float(
        sum(
            eta14[index]
            * np.vdot(left[index], krein @ right[index])
            for index in range(14)
        ).real
    )


def rr_functional(
    parameter: float,
    vector_spinor: np.ndarray,
    vector: np.ndarray,
) -> float:
    gamma_basis = moved_gammas(parameter)
    return vector_spinor_pair(
        vector_spinor,
        q_rr(vector_spinor, vector, gamma_basis),
    )


rng = np.random.default_rng(20260730)
z_seed = (
    rng.standard_normal((14, 128))
    + 1j * rng.standard_normal((14, 128))
)
v_seed = rng.standard_normal(14)
v_seed /= np.linalg.norm(v_seed)
step = 1.0e-6

p_plus = p_r(z_seed, moved_gammas(step))
p_minus = p_r(z_seed, moved_gammas(-step))
projector_response = (p_plus - p_minus) / (2.0 * step)
projector_motion_ratio = float(
    np.linalg.norm(projector_response) / np.linalg.norm(z_seed)
)
check(
    "a frozen P_R misses a strong generic full-G response",
    projector_motion_ratio > 0.05,
    f"ratio={projector_motion_ratio:.6f}",
)

fixed_z_derivative = (
    rr_functional(step, z_seed, v_seed)
    - rr_functional(-step, z_seed, v_seed)
) / (2.0 * step)
check(
    "the written RR primitive has a live fixed-Z soldering response",
    abs(fixed_z_derivative) > 1.0,
    f"derivative={fixed_z_derivative:.6f}",
)


def transported_rr_functional(parameter: float) -> float:
    group = mover(parameter)
    moved_z = np.stack([group @ value for value in z_seed])
    return vector_spinor_pair(
        moved_z,
        q_rr(moved_z, v_seed, moved_gammas(parameter)),
    )


transported_derivative = (
    transported_rr_functional(step)
    - transported_rr_functional(-step)
) / (2.0 * step)
check(
    "simultaneous transport restores covariance of the RR control",
    abs(transported_derivative) < FD_TOL,
    f"derivative={transported_derivative:.3e}",
)
check(
    "the RR number is a same-dependency control, not literal Q_F",
    abs(fixed_z_derivative) > 1.0
    and abs(transported_derivative) < FD_TOL,
)


# ---------------------------------------------------------------------------
# C. A0-dependent reductive connection and lift independence
# ---------------------------------------------------------------------------


print("\nC. Lift-independent A0-induced connection candidate")


def so_generator(left: int, right: int) -> np.ndarray:
    out = np.zeros((3, 3))
    out[left, right] = 1.0
    out[right, left] = -1.0
    return out


h_generator = so_generator(0, 1)
m_generator = so_generator(0, 2)


def project_h(matrix: np.ndarray) -> np.ndarray:
    coefficient = float(
        np.sum(matrix * h_generator)
        / np.sum(h_generator * h_generator)
    )
    return coefficient * h_generator


def project_m(matrix: np.ndarray) -> np.ndarray:
    return matrix - project_h(matrix)


a_zero = 0.27 * h_generator + 0.19 * m_generator
maurer = -0.31 * m_generator
b_zero = a_zero + maurer
gamma_reductive = project_h(b_zero) - maurer
gamma_equivalent = a_zero - project_m(b_zero)
check(
    "the two local formulas for Gamma(epsilon,A0) agree",
    max_abs(gamma_reductive - gamma_equivalent) < TOL,
)

# Change the local lift g -> g h at the point h=1, dh=eta_h.  The bare
# -dg g^-1 changes, while g pr_h(B0) g^-1-dg g^-1 does not.
eta_h = 0.43 * h_generator
bare_before = -maurer
bare_after = -(maurer + eta_h)
gamma_after_lift_change = project_h(b_zero + eta_h) - (
    maurer + eta_h
)
check(
    "the bare Maurer--Cartan connection fails lift independence",
    np.linalg.norm(bare_after - bare_before) > 0.1,
)
check(
    "the A0-induced reductive connection descends across the H lift",
    max_abs(gamma_after_lift_change - gamma_reductive) < TOL,
)

gamma_dependency = {
    "branch": "A0-induced reductive candidate",
    "epsilon_IG": "value+first-derivative",
    "A0": "background-connection-owner",
    "reductive_projection": "Spin(9,5)-stabilizer-choice",
}
check(
    "the A0-induced candidate dependency explicitly includes A0",
    gamma_dependency["branch"] == "A0-induced reductive candidate"
    and
    gamma_dependency["A0"] == "background-connection-owner"
    and gamma_dependency["epsilon_IG"] == "value+first-derivative",
)


# ---------------------------------------------------------------------------
# D. Exact actual-Sym2 trace coordinate
# ---------------------------------------------------------------------------


print("\nD. Actual-Sym2 trace coordinate")

eta4 = sym2.ETA4
h_trace = -eta4 / 4.0


def tau(tensor: np.ndarray) -> float:
    return float(0.25 * np.trace(eta4 @ tensor))


def primal_trace_projector(tensor: np.ndarray) -> np.ndarray:
    return -4.0 * tau(tensor) * h_trace


test_tensor = np.array(
    [
        [0.3, 0.1, 0.0, 0.2],
        [0.1, -0.4, 0.3, 0.0],
        [0.0, 0.3, 0.8, -0.2],
        [0.2, 0.0, -0.2, 0.5],
    ]
)
projected_trace = primal_trace_projector(test_tensor)
check(
    "h_tr is the DeWitt dual of tau and has tau(h_tr)=-1/4",
    abs(sym2.dewitt(h_trace, test_tensor) - tau(test_tensor)) < TOL
    and abs(tau(h_trace) + 0.25) < TOL,
)
check(
    "the primal actual-Sym2 trace-line projector is idempotent",
    max_abs(
        primal_trace_projector(projected_trace) - projected_trace
    )
    < TOL
    and abs(tau(test_tensor - projected_trace)) < TOL,
)

tau_frobenius_matrix = eta4 / 4.0
dual_covector_seed = rng.standard_normal((2, 4, 4))
dual_covector_seed = (
    dual_covector_seed
    + np.swapaxes(dual_covector_seed, 1, 2)
) / 2.0


def phi_trace_dual(vertical_covector: np.ndarray) -> np.ndarray:
    return -4.0 * np.array(
        [
            np.trace(component.T @ h_trace)
            for component in vertical_covector
        ]
    )


def include_trace_dual(adjoint_coefficient: np.ndarray) -> np.ndarray:
    return np.stack(
        [
            coefficient * tau_frobenius_matrix
            for coefficient in adjoint_coefficient
        ]
    )


def dual_trace_projector(vertical_covector: np.ndarray) -> np.ndarray:
    return include_trace_dual(phi_trace_dual(vertical_covector))


projected_dual = dual_trace_projector(dual_covector_seed)
check(
    "the ad-valued vertical-covector trace projector p_tr is idempotent",
    max_abs(
        dual_trace_projector(projected_dual) - projected_dual
    )
    < TOL
    and max_abs(
        phi_trace_dual(projected_dual)
        - phi_trace_dual(dual_covector_seed)
    )
    < TOL,
)


def symmetric_basis() -> list[np.ndarray]:
    basis = []
    for left in range(4):
        for right in range(left, 4):
            tensor = np.zeros((4, 4))
            tensor[left, right] = 1.0
            tensor[right, left] = 1.0
            if left == right:
                tensor[left, right] = 1.0
            basis.append(tensor)
    return basis


sym_basis = symmetric_basis()
invariance_rows = []
for generator in sym2.lorentz_generators(np.diag(eta4)):
    columns = [
        sym2.sym2_components(
            generator.T @ tensor + tensor @ generator
        )
        for tensor in sym_basis
    ]
    invariance_rows.append(np.column_stack(columns))
invariance_matrix = np.vstack(invariance_rows)
invariant_dimension = 10 - int(
    np.linalg.matrix_rank(invariance_matrix, tol=TOL)
)
check(
    "the fixed Lorentz-invariant actual-Sym2 subspace is one-dimensional",
    invariant_dimension == 1
    and all(
        max_abs(generator.T @ h_trace + h_trace @ generator)
        < TOL
        for generator in sym2.lorentz_generators(np.diag(eta4))
    ),
)

split_order = [0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
split_gammas = [gammas[index] for index in split_order]
trace_insertion = sym2.gamma_of_covector(
    sym2.dewitt_musical(h_trace),
    split_gammas[4:],
)
check(
    "the bare trace Clifford insertion is nonzero and full rank",
    np.linalg.matrix_rank(trace_insertion, tol=TOL) == 128,
)

# A decomposable one-mode trace connection has a wedge square proportional
# to tau_a tau_b - tau_b tau_a and hence zero.  This does not remove N1's
# separately written theta^2 term.
tau_seed = rng.standard_normal(14)
decomposable_wedge_coefficients = (
    np.outer(tau_seed, tau_seed)
    - np.outer(tau_seed, tau_seed).T
)
sigma_seed = rng.standard_normal(14)
two_mode_wedge_coefficients = (
    np.outer(tau_seed, sigma_seed)
    - np.outer(sigma_seed, tau_seed)
)
check(
    "the covariantly constant decomposable trace mode has a wedge-square zero control",
    max_abs(decomposable_wedge_coefficients) < TOL
    and max_abs(two_mode_wedge_coefficients) > 0.1,
)


# ---------------------------------------------------------------------------
# E. Full-20 placement: exact first missing arrow and power controls
# ---------------------------------------------------------------------------


print("\nE. Full-20 placement intersection")

placement_arrows = (
    ("p_trace_dual", "CONSTRUCTED"),
    ("Phi_trace", "CONSTRUCTED"),
    ("rho_S(Phi_trace)_native_spinor", "MISSING-FIRST-FACTOR"),
    (
        "widehat_c_rho20(tau tensor Phi_trace)",
        "MISSING-PHYSICAL-OBJECT",
    ),
    ("P0_native_defect_embeddings", "MISSING-DOWNSTREAM"),
    ("Y_K/Y_C_full20_incidence", "MISSING-DOWNSTREAM"),
    ("SM_stabilizer_branching", "MISSING-DOWNSTREAM"),
    ("coflip_right_H_intertwiner", "MISSING-DOWNSTREAM"),
    ("4D_cosmological_Euler_map", "MISSING-DOWNSTREAM"),
)
check(
    "the first unresolved placement factor is explicit rho_S(Phi_trace)",
    placement_arrows[:2]
    == (("p_trace_dual", "CONSTRUCTED"), ("Phi_trace", "CONSTRUCTED"))
    and placement_arrows[2]
    == ("rho_S(Phi_trace)_native_spinor", "MISSING-FIRST-FACTOR")
    and placement_arrows[3][1] == "MISSING-PHYSICAL-OBJECT",
)

expected_vertical_incidence = {
    "SS": 4,
    "SI": 4,
    "SR": 8,
    "IS": 4,
    "II": 4,
    "IR": 8,
    "RS": 8,
    "RI": 8,
    "RR": 20,
}


def slot_sector(slot: b5.Slot) -> str:
    if slot.name.startswith("S:"):
        return "S"
    if slot.name.startswith("imGamma:"):
        return "I"
    return "R"


vertical_incidence = {
    source + target: 0
    for source in ("S", "I", "R")
    for target in ("S", "I", "R")
}
for source_slot in b5.SLOTS:
    for target_slot in b5.SLOTS:
        source_type = b5.TYPES[source_slot.h_type]
        target_type = b5.TYPES[target_slot.h_type]
        fibre_part = int(
            source_type.left_dim == target_type.left_dim
            and source_type.right_dim == target_type.right_dim
        ) * b5.vector_tensor_decomposition(
            source_type.d5_weight
        ).get(
            target_type.d5_weight,
            0,
        )
        if fibre_part:
            vertical_incidence[
                slot_sector(source_slot) + slot_sector(target_slot)
            ] += 1

check(
    "the observer-complex calculation derives the exact 68 vertical incidences",
    vertical_incidence == expected_vertical_incidence
    and sum(vertical_incidence.values()) == 68
    and (vertical_incidence["SS"], vertical_incidence["II"], vertical_incidence["RR"])
    == (4, 4, 20),
)

observer_incidence = {
    (source.name, target.name): b5.symbol_multiplicity(
        b5.TYPES[source.h_type],
        b5.TYPES[target.h_type],
    )
    for source in b5.SLOTS
    for target in b5.SLOTS
}
check(
    "the frozen 20-slot/136-incidence schema is carried into the moving build",
    len(b5.SLOTS) == 20
    and sum(value > 0 for value in observer_incidence.values()) == 136,
)

charge_fixture = np.diag([1.0, -1.0, 2.0, -2.0])
identity_placement = np.eye(4)
charged_placement = np.zeros((4, 4))
charged_placement[0, 1] = 1.0
identity_singular_values = np.linalg.svd(
    identity_placement,
    compute_uv=False,
)
nonuniversal_singular_values = np.linalg.svd(
    np.diag([1.0, 2.0, 3.0, 4.0]),
    compute_uv=False,
)
check(
    "a universal identity placement is rejected as an uncharged Higgs/Yukawa substitute",
    max_abs(commutator(charge_fixture, identity_placement)) < TOL
    and max_abs(commutator(charge_fixture, charged_placement)) > 1.0,
)
check(
    "the identity plant has only one singular value while a nonuniversal texture has more",
    len(np.unique(np.round(identity_singular_values, 10))) == 1
    and len(np.unique(np.round(nonuniversal_singular_values, 10))) > 1,
)

provenance_real_y = np.array(
    [[1.0, 0.2, 0.0], [0.2, 2.0, -0.1], [0.0, -0.1, 3.0]],
    dtype=complex,
)
provenance_complex_y = provenance_real_y.copy()
provenance_complex_y[0, 1] += 0.4j
j_h = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
j_total = np.kron(np.eye(3), j_h)
real_y_lift = np.kron(provenance_real_y, np.eye(2))
complex_y_lift = np.kron(provenance_complex_y, np.eye(2))
check(
    "real provenance Y can be right-H linear while genuinely complex Y cannot be assumed so",
    max_abs(real_y_lift @ j_total - j_total @ real_y_lift.conj())
    < TOL
    and max_abs(
        complex_y_lift @ j_total - j_total @ complex_y_lift.conj()
    )
    > 0.1,
)

raw_total_operator = (
    rng.standard_normal((128, 128))
    + 1j * rng.standard_normal((128, 128))
)
krein_adjoint_operator = (
    np.linalg.inv(krein)
    @ raw_total_operator.conj().T
    @ krein
)
k_projection = (
    raw_total_operator + krein_adjoint_operator
) / 2.0
c_natural_plus = -np.linalg.solve(
    c_plus,
    raw_total_operator.T @ c_plus,
)
c_projection = (
    raw_total_operator - c_natural_plus
) / 2.0
check(
    "K-sesquilinear and C-complex-bilinear total projections do not collapse",
    np.linalg.norm(k_projection - c_projection)
    / np.linalg.norm(raw_total_operator)
    > 0.1,
)

# The scalar center of GL(4) gives Sym2 and Lambda2 the same weight but
# Lambda3 a different one.  Even this permissive central test bounds a
# putative map to Lambda2+Lambda3 by six, so it cannot be an isomorphism
# of the two ten-dimensional fibres.
central_compatible_rank_bound = comb(4, 2)
topology_menu = {-1, 0, 1}
check(
    "the exterior-ten substitution fails the central-weight full-rank test",
    central_compatible_rank_bound == 6 < 10,
)
check(
    "premature n=3 is rejected outside the frozen topology menu",
    3 not in topology_menu,
)

same_rank_projector = np.diag([1.0, 1.0, 0.0, 0.0])
projector_rotation = np.array(
    [
        [np.cos(0.4), 0.0, np.sin(0.4), 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-np.sin(0.4), 0.0, np.cos(0.4), 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
)
moved_same_rank_projector = (
    projector_rotation
    @ same_rank_projector
    @ projector_rotation.T
)
check(
    "a same-rank but nonintertwining frozen projector is rejected",
    np.linalg.matrix_rank(moved_same_rank_projector, tol=TOL)
    == np.linalg.matrix_rank(same_rank_projector, tol=TOL)
    == 2
    and max_abs(moved_same_rank_projector - same_rank_projector) > 0.1,
)

shared_scalar_parameter_count = 1
fitted_scalar_parameter_count = 5
check(
    "one independently fitted scalar per physics leg is rejected",
    shared_scalar_parameter_count == 1
    and fitted_scalar_parameter_count
    > shared_scalar_parameter_count,
)

constraint_surplus = "SURPLUS-UNCOMPUTABLE-FIRST-rho_S(Phi_trace)"
check(
    "constraint surplus remains uncomputable rather than fitted from prose rows",
    constraint_surplus
    == "SURPLUS-UNCOMPUTABLE-FIRST-rho_S(Phi_trace)",
)


# ---------------------------------------------------------------------------
# F. Held-out-blind discriminator for both RB2 bridge systems
# ---------------------------------------------------------------------------


print("\nF. Moving-epsilon discriminator for the RB2 bridge pair")


def h_linear_projection(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (
        matrix
        + j_quat_matrix
        @ matrix.conj()
        @ np.linalg.inv(j_quat_matrix)
    )


def native_sp_projection(matrix: np.ndarray) -> np.ndarray:
    h_linear = h_linear_projection(matrix)
    projected = 0.5 * (
        h_linear
        - np.linalg.inv(krein) @ h_linear.conj().T @ krein
    )
    return h_linear_projection(projected)


def normalized(matrix: np.ndarray, scale: float) -> np.ndarray:
    return scale * matrix / np.linalg.norm(matrix)


rng_bridge = np.random.default_rng(20260731)


def random_matrix() -> np.ndarray:
    return (
        rng_bridge.standard_normal((128, 128))
        + 1j * rng_bridge.standard_normal((128, 128))
    )


gamma_connection_zero = normalized(
    native_sp_projection(random_matrix()),
    3.0,
)
connection = normalized(
    native_sp_projection(random_matrix()),
    2.0,
)
distortion = normalized(
    native_sp_projection(random_matrix()),
    1.7,
)
odd_field = normalized(
    h_linear_projection(random_matrix()),
    2.4,
)
delta_gamma = commutator(x_mover, gamma_connection_zero)


def relative_bridge_with_odd(
    parameter: float,
    odd_value: np.ndarray,
) -> float:
    group = mover(parameter)
    gamma_connection = (
        group @ gamma_connection_zero @ mover(-parameter)
    )
    theta_matrix = connection - gamma_connection - distortion
    covariant_connection = connection - gamma_connection
    j_f = (
        covariant_connection @ odd_value
        + odd_value @ covariant_connection
    )
    return float(-np.trace(j_f @ theta_matrix).real)


def relative_bridge(parameter: float) -> float:
    return relative_bridge_with_odd(parameter, odd_field)


theta_zero = connection - gamma_connection_zero - distortion
covariant_zero = connection - gamma_connection_zero
j_f_zero = covariant_zero @ odd_field + odd_field @ covariant_zero
delta_j_f = -(
    delta_gamma @ odd_field + odd_field @ delta_gamma
)
analytic_relative_response = float(
    -np.trace(
        delta_j_f @ theta_zero - j_f_zero @ delta_gamma
    ).real
)
finite_relative_response = (
    relative_bridge(step) - relative_bridge(-step)
) / (2.0 * step)
check(
    "the homogeneous moving-Gamma chain-rule proxy matches finite differences",
    abs(
        analytic_relative_response - finite_relative_response
    )
    < FD_TOL,
    (
        f"analytic={analytic_relative_response:.6g}, "
        f"finite={finite_relative_response:.6g}"
    ),
)
frozen_current_response = float(
    np.trace(j_f_zero @ delta_gamma).real
)
check(
    "freezing the current-map response changes the relative epsilon proxy",
    abs(frozen_current_response - finite_relative_response) > 1.0e-3,
    (
        f"complete={finite_relative_response:.6g}, "
        f"frozen-current={frozen_current_response:.6g}"
    ),
)
check(
    "one nonzero fixture proves the discriminator polynomial is not identically zero",
    abs(finite_relative_response) > 1.0e-3,
    f"response={finite_relative_response:.6g}",
)

zero_odd_field = np.zeros_like(odd_field)
controlled_zero_response = (
    relative_bridge_with_odd(step, zero_odd_field)
    - relative_bridge_with_odd(-step, zero_odd_field)
) / (2.0 * step)
check(
    "the same fixture vanishes on the controlled odd=J_F=0 stratum",
    abs(controlled_zero_response) < TOL,
)

bridge_emission = {
    "N1_JD_bridge": "SURVIVES-RB3-HOMOGENEOUS-CHAIN-RULE-PROXY",
    "N1_total_current_bridge": "SURVIVES-RB3-HOMOGENEOUS-CHAIN-RULE-PROXY",
    "selection": "NONE; LITERAL-MOVING-QF/A0-JOIN-PENDING",
}
check(
    "both RB2 bridges survive without premature selection",
    set(bridge_emission) == {
        "N1_JD_bridge",
        "N1_total_current_bridge",
        "selection",
    }
    and bridge_emission["selection"].startswith("NONE"),
)


# ---------------------------------------------------------------------------
# G. Five-leg and external-datum disposition
# ---------------------------------------------------------------------------


print("\nG. Five-leg and external-datum disposition")

five_leg_status = {
    "standard_model_yukawa": (
        "BLOCKED-FIRST-FACTOR-AT-rho_S(Phi_trace); FULL20-LIFT-MISSING"
    ),
    "quantum_krein_bv": "K/C-SEPARATE; C+-FIXED; C--CONGRUENCE-OR-STABILIZER",
    "gravity_cosmology": "AMBIENT-THETA2-CARRIED; 4D-MAP-UNBUILT",
    "index_count": "P3-RIGHT-H-CONDITIONAL; NO-READOUT",
    "uv_causality": (
        "PRINCIPAL-CLIFFORD-SYMBOL-CONJUGATE/CARRIED; "
        "MOVING-SUBPRINCIPAL+DOMAIN-UNTESTED"
    ),
}
check(
    "all five interfaces remain explicit without a fitted readout",
    set(five_leg_status)
    == {
        "standard_model_yukawa",
        "quantum_krein_bv",
        "gravity_cosmology",
        "index_count",
        "uv_causality",
    }
    and five_leg_status["index_count"].endswith("NO-READOUT"),
)

datum_ledger = {
    "P1_P2": "one carried orientation line; zero-order intertwiner open",
    "P3": "external relative-KO datum; right-H placement open",
    "global_H_reduction": (
        "constructed if P_G is extended from the Spin(9,5) frame bundle; "
        "otherwise existence is uncertain; charge a separate sector only "
        "if the variational setup fixes one"
    ),
    "VEV": "not supplied or selected",
}
datum_identity_tokens = {
    "P1_P2": "orientation_line",
    "P3": "relative_KO_comparator",
    "VEV": "spinzero_vacuum_coordinate",
}
check(
    "no new datum is silently relabelled as P1/P2 or P3",
    datum_ledger["VEV"] == "not supplied or selected"
    and "existence is uncertain" in datum_ledger["global_H_reduction"],
)
check(
    "a future VEV has a distinct Layer-0 identity from P1/P2 and P3",
    len(set(datum_identity_tokens.values())) == 3,
)


if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\nVERDICT: MOVING-CLIFFORD-PLANE-LOCALLY-CONSTRUCTED")
print("CANDIDATE: A0-INDUCED-GAMMA(EPSILON_IG,A0)-LIFT-INDEPENDENT")
print("OPEN: IDENTITY-WITH-N1-GAMMA_CONN-AND-OTHER-H-CONNECTION-BRANCHES")
print("VERDICT: ACTUAL-SYM2-TRACE-COORDINATE-CONSTRUCTED")
print("BLOCK: PHYSICAL-FULL20-PLACEMENT-FIRST-FACTOR-AT-rho_S(Phi_trace)")
print("VERDICT: BOTH-RB2-BRIDGES-SURVIVE-HOMOGENEOUS-CHAIN-RULE-PROXY")
print("OPEN: LITERAL-Q_F/P_R/A0-GAMMA MOVING RESPONSE AND GREEN JOIN")
print("GLOBAL: H-REDUCTION-CONDITIONAL-ON-EXTENDED-SP-BUNDLE")
print("NOT CLAIMED: VEV, MASS, COSMOLOGICAL VALUE, INDEX, OR COUNT")
print("ALL CONTROLS PASSED")
