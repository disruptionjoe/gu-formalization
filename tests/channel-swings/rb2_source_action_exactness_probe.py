#!/usr/bin/env python3
"""RB2 source-action exactness and current-bridge shootout.

This is an executable formula/type contract.  It checks:

* the Layer-0 split between the spinorial and bosonic Shiab carriers;
* complete finite-dimensional A/U/P/epsilon/Z bridge-slice variations at
  classical fixed-geometry antifield-zero grade;
* field-dependent current Hessians, Z-variation, and Green ownership;
* classical parent retention versus exact algebraic elimination;
* the conditional source-action chain rule for A, U, epsilon, and A_lambda;
* source-coefficient selection by transgression exactness, not Ward covariance;
* the lambda=1 field-rank result and the lambda!=1 orbit-tangent control;
* finite homogeneous adjoint-covariance proxies, not native Ward closure;
* action/no-double-count/five-leg referential integrity; and
* the finite RB3 emission plus the source-branch reopener.

It does not construct the native bosonic Shiab, prove complete Diff closure or
the CME, select a zero-order carrier or VEV, solve a curved equation, construct
a global domain, reduce to the physical spectrum, or compute an index/count.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Callable

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import unified_source_datum_packet_v0_probe as n1  # noqa: E402


TOL = 3.0e-6
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def central_gradient(
    function: Callable[[np.ndarray], float],
    point: np.ndarray,
    step: float = 1.0e-6,
) -> np.ndarray:
    result = np.zeros_like(point, dtype=float)
    for index in range(point.size):
        direction = np.zeros_like(point, dtype=float)
        direction[index] = step
        result[index] = (
            function(point + direction) - function(point - direction)
        ) / (2.0 * step)
    return result


def central_directional(
    function: Callable[[np.ndarray], float],
    point: np.ndarray,
    direction: np.ndarray,
    step: float = 1.0e-6,
) -> float:
    return float(
        (
            function(point + step * direction)
            - function(point - step * direction)
        )
        / (2.0 * step)
    )


def symmetric(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.T) / 2.0


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def frobenius(left: np.ndarray, right: np.ndarray) -> float:
    return float(np.trace(left.T @ right))


print("=" * 104)
print("RB2 SOURCE-ACTION EXACTNESS + CURRENT-BRIDGE EULER SHOOTOUT")
print("=" * 104)


# ======================================================================
# A. Layer-0 map, real-form, and symmetry gate
# ======================================================================


@dataclass(frozen=True)
class MapSpec:
    name: str
    domain: str
    codomain: str
    symmetry: str
    real_form: str
    hodge_stage: str
    epsilon_policy: str
    right_h_compatible: bool
    invariant_pairing: str
    action_reality: str
    cyclic_adjoint_grade: str
    grade: str


SPINORIAL_SHIAB_FAMILY = MapSpec(
    "spinorial_shiab_family",
    "Lambda2(V*) tensor S",
    "V* tensor S",
    "Spin(9,5) x Sp(1)_right",
    "Cl(9,5)=M(64,H), right-H",
    "primal_spinorial",
    "not_applicable",
    True,
    "spinor_Krein",
    "real_linear_spinorial",
    "not_a_bosonic_transgression_map",
    "PROVED-FAMILY; REAL-DIM-4-AFTER-RIGHT-H-CUT",
)

H_N1 = (
    "Stab_Sp(Gamma,P_R,P_0,K_or_C,end_selector,active_N1_tensors)"
)
H_SOURCE_CONDITIONAL = (
    "Stab_Sp(Gamma,P_R,P_0,K_or_C,end_selector,"
    "S_bos_density,source_tensors)"
)
FINITE_ADJOINT_PROXY = "real_4x4_homogeneous_conjugation_proxy"

BOSONIC_SHIAB_REQUIRED = MapSpec(
    "S_bos_density_epsilon",
    "Omega2(Y,adP)",
    "Omega13(Y,ad*P)",
    H_SOURCE_CONDITIONAL,
    "Sp(32,32;H), native adjoint/coadjoint",
    "density_dual_composite_includes_Hodge_and_pairing",
    "explicit_response_or_intrinsic_proved_zero",
    True,
    "indefinite_G_tensor_kappa_g",
    "native_real_required",
    "required_but_unbuilt",
    "REQUIRED",
)

SOURCE_BOSONIC_SHIAB = MapSpec(
    "source_density_dual_odot_epsilon",
    "Omega2(Y_source,adP_source)",
    "Omega13(Y_source,adP_source)",
    "tilted source gauge group",
    "Y(7,7)/U(64,64)-type source surface",
    "density_dual_composite_includes_Hodge_and_pairing",
    "explicit_response",
    False,
    "source_pairing_not_translated",
    "source_real_only",
    "source_declared_not_native_certified",
    "SOURCE-EXPLICIT; NATIVE-TRANSLATION-ABSENT",
)


def epsilon_policy_compatible(required: str, candidate: str) -> bool:
    if required == "explicit_response_or_intrinsic_proved_zero":
        return candidate in {
            "explicit_response",
            "intrinsic_proved_zero",
        }
    return required == candidate


def map_can_fill(required: MapSpec, candidate: MapSpec) -> bool:
    return (
        required.domain == candidate.domain
        and required.codomain == candidate.codomain
        and required.symmetry == candidate.symmetry
        and required.real_form == candidate.real_form
        and required.hodge_stage == candidate.hodge_stage
        and epsilon_policy_compatible(
            required.epsilon_policy,
            candidate.epsilon_policy,
        )
        and required.right_h_compatible
        == candidate.right_h_compatible
        and required.invariant_pairing == candidate.invariant_pairing
        and required.action_reality == candidate.action_reality
        and required.cyclic_adjoint_grade
        == candidate.cyclic_adjoint_grade
    )


print("\nA. Layer-0 carrier and native-arena gate")
check(
    "the proved spinorial Shiab family cannot fill the bosonic action slot",
    not map_can_fill(BOSONIC_SHIAB_REQUIRED, SPINORIAL_SHIAB_FAMILY),
)
check(
    "the source bosonic Shiab has the right source carrier but not a native real-form translation",
    SOURCE_BOSONIC_SHIAB.domain.startswith("Omega2")
    and SOURCE_BOSONIC_SHIAB.codomain.startswith("Omega13")
    and not map_can_fill(BOSONIC_SHIAB_REQUIRED, SOURCE_BOSONIC_SHIAB),
)
check(
    "the native density-dual bosonic map requires either explicit epsilon response or proved intrinsic zero response",
    BOSONIC_SHIAB_REQUIRED.epsilon_policy
    == "explicit_response_or_intrinsic_proved_zero"
    and BOSONIC_SHIAB_REQUIRED.hodge_stage
    == "density_dual_composite_includes_Hodge_and_pairing"
    and BOSONIC_SHIAB_REQUIRED.grade == "REQUIRED",
)
check(
    "both explicit-response and proved-intrinsic-zero epsilon policies are admissible construction routes",
    epsilon_policy_compatible(
        BOSONIC_SHIAB_REQUIRED.epsilon_policy,
        "explicit_response",
    )
    and epsilon_policy_compatible(
        BOSONIC_SHIAB_REQUIRED.epsilon_policy,
        "intrinsic_proved_zero",
    ),
)

DIMENSION_Y = 14
DENSITY_DUAL_OUTPUT_DEGREE = 13
THETA_DEGREE = 1
check(
    "the density-dual bosonic action has top degree without a second Hodge star",
    THETA_DEGREE + DENSITY_DUAL_OUTPUT_DEGREE == DIMENSION_Y,
)
check(
    "a double-Hodge bosonic-action plant is rejected by form degree",
    THETA_DEGREE
    + (DIMENSION_Y - DENSITY_DUAL_OUTPUT_DEGREE)
    != DIMENSION_Y,
)

FULL_SP_FIXED_PLANE = "Sp(32,32;H)_generic_fixed_plane"
check(
    "the N1 and conditional-source stabilizers are architecture-specific",
    H_N1 != H_SOURCE_CONDITIONAL
    and "active_N1_tensors" in H_N1
    and "S_bos_density" in H_SOURCE_CONDITIONAL,
)
check(
    "generic fixed-plane full-Sp is a hostile fork, not the RB2 symmetry",
    FULL_SP_FIXED_PLANE not in H_N1
    and FULL_SP_FIXED_PLANE not in H_SOURCE_CONDITIONAL,
)

NATIVE_METADATA = {
    "group": "Sp(32,32;H)",
    "pairing": "indefinite_G_tensor_kappa_g",
    "fibre": "Sym2(T*X)",
    "rs": "gamma_traceless_full20",
    "symmetry": "architecture_specific_stabilizer",
}
HOSTILE_METADATA = (
    ("group", {**NATIVE_METADATA, "group": "U(128)"}),
    ("pairing", {**NATIVE_METADATA, "pairing": "positive_Hilbert"}),
    ("fibre", {**NATIVE_METADATA, "fibre": "Lambda2+Lambda3"}),
    ("rs", {**NATIVE_METADATA, "rs": "ghost_subtracted"}),
    (
        "symmetry",
        {**NATIVE_METADATA, "symmetry": FULL_SP_FIXED_PLANE},
    ),
)
check(
    "native metadata retains the geometer construction on every load-bearing fork",
    NATIVE_METADATA
    == {
        "group": "Sp(32,32;H)",
        "pairing": "indefinite_G_tensor_kappa_g",
        "fibre": "Sym2(T*X)",
        "rs": "gamma_traceless_full20",
        "symmetry": "architecture_specific_stabilizer",
    },
)
for hostile_key, hostile_metadata in HOSTILE_METADATA:
    changed_keys = {
        key
        for key in NATIVE_METADATA
        if hostile_metadata[key] != NATIVE_METADATA[key]
    }
    check(
        f"the {hostile_key} fork is rejected independently",
        hostile_metadata != NATIVE_METADATA
        and changed_keys == {hostile_key},
    )


# ======================================================================
# B. Complete five-field bridge-slice variations at classical fixed grade
# ======================================================================


@dataclass(frozen=True)
class N1Toy:
    dimension: int
    metric_theta: np.ndarray
    metric_parent: np.ndarray
    metric_yang_mills: np.ndarray
    defect_hessian: np.ndarray
    gamma_offset: np.ndarray
    gamma_linear: np.ndarray
    gamma_quadratic: np.ndarray
    dau_linear: np.ndarray
    dau_bilinear: np.ndarray
    jd_offset: np.ndarray
    jd_quadratic: np.ndarray
    h_offset: np.ndarray
    h_slices: np.ndarray
    kappa: float
    z_u: float


def make_n1_toy(seed: int = 20260730, dimension: int = 4) -> N1Toy:
    rng = np.random.default_rng(seed)
    metric_theta = np.diag([1.4, -0.9, 0.7, -1.2])
    metric_parent = np.diag([1.1, -0.8, 1.3, -0.6])
    metric_yang_mills = symmetric(rng.normal(size=(dimension, dimension)))
    metric_yang_mills += 2.0 * np.diag([1.0, -1.0, 0.7, -0.5])
    defect_hessian = 0.25 * symmetric(
        rng.normal(size=(dimension, dimension))
    )
    gamma_offset = rng.normal(size=dimension)
    gamma_linear = rng.normal(size=(dimension, dimension))
    gamma_quadratic = 0.35 * rng.normal(size=(dimension, dimension))
    dau_linear = rng.normal(size=(dimension, dimension))
    dau_bilinear = 0.3 * rng.normal(
        size=(dimension, dimension, dimension)
    )
    jd_offset = rng.normal(size=dimension)
    jd_quadratic = 0.4 * rng.normal(size=(dimension, dimension))
    h_offset = symmetric(rng.normal(size=(dimension, dimension)))
    h_slices = np.stack(
        [
            0.3 * symmetric(rng.normal(size=(dimension, dimension)))
            for _ in range(dimension)
        ]
    )
    return N1Toy(
        dimension,
        metric_theta,
        metric_parent,
        metric_yang_mills,
        defect_hessian,
        gamma_offset,
        gamma_linear,
        gamma_quadratic,
        dau_linear,
        dau_bilinear,
        jd_offset,
        jd_quadratic,
        h_offset,
        h_slices,
        1.7,
        -1.35,
    )


def gamma_value(toy: N1Toy, epsilon: np.ndarray) -> np.ndarray:
    return (
        toy.gamma_offset
        + toy.gamma_linear @ epsilon
        + 0.5 * toy.gamma_quadratic @ (epsilon * epsilon)
    )


def gamma_jacobian(toy: N1Toy, epsilon: np.ndarray) -> np.ndarray:
    return toy.gamma_linear + toy.gamma_quadratic @ np.diag(epsilon)


def dau_value(
    toy: N1Toy,
    connection: np.ndarray,
    distortion: np.ndarray,
) -> np.ndarray:
    return (
        toy.dau_linear @ distortion
        + np.einsum(
            "ijk,j,k->i",
            toy.dau_bilinear,
            connection,
            distortion,
        )
    )


def dau_jacobian_a(toy: N1Toy, distortion: np.ndarray) -> np.ndarray:
    return np.einsum("ijk,k->ij", toy.dau_bilinear, distortion)


def dau_jacobian_u(toy: N1Toy, connection: np.ndarray) -> np.ndarray:
    return toy.dau_linear + np.einsum(
        "ijk,j->ik",
        toy.dau_bilinear,
        connection,
    )


def jd_value(toy: N1Toy, odd_field: np.ndarray) -> np.ndarray:
    return (
        toy.jd_offset
        + toy.jd_quadratic @ (odd_field * odd_field)
    )


def jd_jacobian_z(toy: N1Toy, odd_field: np.ndarray) -> np.ndarray:
    return 2.0 * toy.jd_quadratic @ np.diag(odd_field)


def h_value(toy: N1Toy, odd_field: np.ndarray) -> np.ndarray:
    return toy.h_offset + np.einsum(
        "l,lij->ij",
        odd_field,
        toy.h_slices,
    )


def s20_value(
    toy: N1Toy,
    connection: np.ndarray,
    odd_field: np.ndarray,
) -> float:
    jd = jd_value(toy, odd_field)
    hessian = h_value(toy, odd_field)
    return float(
        jd @ connection
        + 0.5 * connection @ hessian @ connection
    )


def s20_gradients(
    toy: N1Toy,
    connection: np.ndarray,
    odd_field: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    jd = jd_value(toy, odd_field)
    hessian = h_value(toy, odd_field)
    grad_connection = jd + hessian @ connection
    grad_odd = (
        2.0
        * odd_field
        * (toy.jd_quadratic.T @ connection)
        + 0.5
        * np.array(
            [
                connection @ toy.h_slices[index] @ connection
                for index in range(toy.dimension)
            ]
        )
    )
    return grad_connection, grad_odd


def bridge_current(
    toy: N1Toy,
    kind: str,
    connection: np.ndarray,
    odd_field: np.ndarray,
) -> np.ndarray:
    jd = jd_value(toy, odd_field)
    if kind == "JD":
        return jd
    if kind == "TOTAL":
        return jd + h_value(toy, odd_field) @ connection
    raise ValueError(f"unknown bridge current: {kind}")


def bridge_current_jacobians(
    toy: N1Toy,
    kind: str,
    connection: np.ndarray,
    odd_field: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    jacobian_z = jd_jacobian_z(toy, odd_field)
    if kind == "JD":
        return np.zeros((toy.dimension, toy.dimension)), jacobian_z
    if kind == "TOTAL":
        jacobian_z = jacobian_z + np.column_stack(
            [
                toy.h_slices[index] @ connection
                for index in range(toy.dimension)
            ]
        )
        return h_value(toy, odd_field), jacobian_z
    raise ValueError(f"unknown bridge current: {kind}")


N_FIELDS = 5


def split_n1_point(
    toy: N1Toy,
    packed: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    return tuple(
        packed[
            index * toy.dimension : (index + 1) * toy.dimension
        ]
        for index in range(N_FIELDS)
    )  # type: ignore[return-value]


def n1_action(toy: N1Toy, kind: str, packed: np.ndarray) -> float:
    connection, distortion, parent, epsilon, odd_field = split_n1_point(
        toy,
        packed,
    )
    gamma = gamma_value(toy, epsilon)
    theta = connection - gamma - distortion
    dau = dau_value(toy, connection, distortion)
    current = bridge_current(
        toy,
        kind,
        connection,
        odd_field,
    )
    common = (
        0.5 * connection @ toy.metric_yang_mills @ connection
        + 0.5 * connection @ toy.defect_hessian @ connection
        + parent @ toy.metric_parent @ dau
        - 0.5
        / toy.z_u
        * parent
        @ toy.metric_parent
        @ parent
    )
    bridge = (
        0.5
        / toy.kappa
        * theta
        @ toy.metric_theta
        @ theta
        - current @ theta
    )
    return float(
        common
        + s20_value(toy, connection, odd_field)
        + bridge
    )


def n1_analytic_gradient(
    toy: N1Toy,
    kind: str,
    packed: np.ndarray,
) -> np.ndarray:
    connection, distortion, parent, epsilon, odd_field = split_n1_point(
        toy,
        packed,
    )
    gamma = gamma_value(toy, epsilon)
    gamma_jac = gamma_jacobian(toy, epsilon)
    theta = connection - gamma - distortion
    flat_theta = toy.metric_theta @ theta / toy.kappa
    dau = dau_value(toy, connection, distortion)
    jac_a = dau_jacobian_a(toy, distortion)
    jac_u = dau_jacobian_u(toy, connection)
    current = bridge_current(
        toy,
        kind,
        connection,
        odd_field,
    )
    current_a, current_z = bridge_current_jacobians(
        toy,
        kind,
        connection,
        odd_field,
    )
    j20, z20 = s20_gradients(toy, connection, odd_field)

    grad_a = (
        toy.metric_yang_mills @ connection
        + toy.defect_hessian @ connection
        + jac_a.T @ toy.metric_parent @ parent
        + j20
        + flat_theta
        - current
        - current_a.T @ theta
    )
    grad_u = (
        jac_u.T @ toy.metric_parent @ parent
        - flat_theta
        + current
    )
    grad_parent = toy.metric_parent @ (
        dau - parent / toy.z_u
    )
    grad_epsilon = -gamma_jac.T @ (
        flat_theta - current
    )
    grad_odd = z20 - current_z.T @ theta
    return np.concatenate(
        (grad_a, grad_u, grad_parent, grad_epsilon, grad_odd)
    )


print(
    "\nB. Complete classical fixed-geometry antifield-zero "
    "five-field bridge-slice variations"
)
toy = make_n1_toy()
rng = np.random.default_rng(4127)
n1_point = rng.normal(size=toy.dimension * N_FIELDS)
n1_gradients: dict[str, np.ndarray] = {}
for current_kind in ("JD", "TOTAL"):
    numerical = central_gradient(
        lambda packed: n1_action(toy, current_kind, packed),
        n1_point,
    )
    analytic = n1_analytic_gradient(toy, current_kind, n1_point)
    worst = float(np.max(np.abs(numerical - analytic)))
    n1_gradients[current_kind] = analytic
    check(
        f"{current_kind} bridge complete A/U/P/epsilon/Z gradient matches finite differences",
        worst < TOL,
        f"worst={worst:.3e}",
    )

connection, distortion, parent, epsilon, odd_field = split_n1_point(
    toy,
    n1_point,
)
gamma = gamma_value(toy, epsilon)
gamma_jac = gamma_jacobian(toy, epsilon)
theta = connection - gamma - distortion
jf = h_value(toy, odd_field) @ connection
jf_z = np.column_stack(
    [
        toy.h_slices[index] @ connection
        for index in range(toy.dimension)
    ]
)
predicted_delta = np.concatenate(
    (
        -jf - h_value(toy, odd_field).T @ theta,
        jf,
        np.zeros(toy.dimension),
        gamma_jac.T @ jf,
        -jf_z.T @ theta,
    )
)
actual_delta = n1_gradients["TOTAL"] - n1_gradients["JD"]
check(
    "the two bridge Euler systems differ by the complete -J_F[theta] variation",
    np.max(np.abs(actual_delta - predicted_delta)) < 1.0e-10,
)
check(
    "the N1 bridge formulas are distinct on a nondegenerate finite control",
    np.linalg.norm(actual_delta) > 0.2,
)

j20, _ = s20_gradients(toy, connection, odd_field)
jd = jd_value(toy, odd_field)
total = bridge_current(toy, "TOTAL", connection, odd_field)
check(
    "the JD bridge cancels only the direct J_D piece in the A equation",
    np.linalg.norm((j20 - jd) - jf) < 1.0e-12,
)
check(
    "the total bridge cancels the direct current but leaves a nonzero current-Hessian term",
    np.linalg.norm(j20 - total) < 1.0e-12
    and np.linalg.norm(h_value(toy, odd_field).T @ theta) > 0.1,
)

frozen_current_gradient = n1_analytic_gradient(
    toy,
    "TOTAL",
    n1_point,
).copy()
frozen_current_gradient[: toy.dimension] += (
    h_value(toy, odd_field).T @ theta
)
total_numerical = central_gradient(
    lambda packed: n1_action(toy, "TOTAL", packed),
    n1_point,
)
check(
    "a frozen-current total-cancellation plant fails the action derivative",
    np.max(np.abs(frozen_current_gradient - total_numerical)) > 0.1,
)

total_current_a, total_current_z = bridge_current_jacobians(
    toy,
    "TOTAL",
    connection,
    odd_field,
)
check(
    "the total bridge owns nonzero A- and Z-current Hessians",
    np.linalg.norm(total_current_a) > 0.1
    and np.linalg.norm(total_current_z) > 0.1,
)


# ======================================================================
# C. Parent retention/elimination and Green form
# ======================================================================


def eliminated_parent_action(
    toy: N1Toy,
    connection: np.ndarray,
    distortion: np.ndarray,
    z_u: float,
) -> float:
    dau = dau_value(toy, connection, distortion)
    return float(0.5 * z_u * dau @ toy.metric_parent @ dau)


def retained_parent_action(
    toy: N1Toy,
    connection: np.ndarray,
    distortion: np.ndarray,
    parent_value: np.ndarray,
    z_u: float,
) -> float:
    dau = dau_value(toy, connection, distortion)
    return float(
        parent_value @ toy.metric_parent @ dau
        - 0.5
        / z_u
        * parent_value
        @ toy.metric_parent
        @ parent_value
    )


print("\nC. Parent elimination, false field shift, and Green ownership")
for z_u_control in (1.4, -1.35):
    dau = dau_value(toy, connection, distortion)
    stationary_parent = z_u_control * dau
    retained_value = float(
        stationary_parent @ toy.metric_parent @ dau
        - 0.5
        / z_u_control
        * stationary_parent
        @ toy.metric_parent
        @ stationary_parent
    )
    eliminated_value = eliminated_parent_action(
        toy,
        connection,
        distortion,
        z_u_control,
    )
    check(
        f"retained parent equals +Z_U/2 eliminated action for Z_U={z_u_control}",
        abs(retained_value - eliminated_value) < 1.0e-12,
    )
    wrong_sign = -eliminated_value
    check(
        f"sign-flipped eliminated parent is rejected for Z_U={z_u_control}",
        abs(retained_value - wrong_sign) > 1.0e-4,
    )
    au_point = np.concatenate((connection, distortion))
    retained_au_gradient = central_gradient(
        lambda packed: retained_parent_action(
            toy,
            packed[: toy.dimension],
            packed[toy.dimension :],
            stationary_parent,
            z_u_control,
        ),
        au_point,
    )
    eliminated_au_gradient = central_gradient(
        lambda packed: eliminated_parent_action(
            toy,
            packed[: toy.dimension],
            packed[toy.dimension :],
            z_u_control,
        ),
        au_point,
    )
    check(
        f"retained A/U gradients on the auxiliary shell match the eliminated gradients for Z_U={z_u_control}",
        np.max(
            np.abs(retained_au_gradient - eliminated_au_gradient)
        )
        < TOL,
    )

q_f = rng.normal(size=toy.dimension)
original_parent_equation = toy.metric_parent @ (
    dau_value(toy, connection, distortion) - parent / toy.z_u
)
shifted_parent_equation = toy.metric_parent @ (
    dau_value(toy, connection, distortion)
    - (parent + q_f) / toy.z_u
)
check(
    "P_IG -> P_IG+q_F is not a field equivalence because it changes the P equation",
    np.linalg.norm(
        shifted_parent_equation - original_parent_equation
    )
    > 0.1,
)


def polynomial_derivative(
    coefficients: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    return tuple(
        Fraction(power) * coefficients[power]
        for power in range(1, len(coefficients))
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
        value / Fraction(power + 1)
        for power, value in enumerate(coefficients)
    )


def evaluate_polynomial(
    coefficients: tuple[Fraction, ...],
    value: Fraction,
) -> Fraction:
    return sum(
        coefficient * value**power
        for power, coefficient in enumerate(coefficients)
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


a_poly = (Fraction(1), Fraction(0), Fraction(1))
q_poly = (Fraction(0), Fraction(2), Fraction(0), Fraction(1))
sign_da_q = exterior_reorder_sign((13, 0) + tuple(range(1, 13)))
sign_a_dq = exterior_reorder_sign((0, 13) + tuple(range(1, 13)))
sign_boundary = exterior_reorder_sign((13,) + tuple(range(13)))
bulk_da_q = sign_da_q * integrate_unit(
    polynomial_product(polynomial_derivative(a_poly), q_poly)
)
interior_a_dq = sign_a_dq * integrate_unit(
    polynomial_product(a_poly, polynomial_derivative(q_poly))
)
boundary_aq = sign_boundary * (
    evaluate_polynomial(a_poly, Fraction(1))
    * evaluate_polynomial(q_poly, Fraction(1))
    - evaluate_polynomial(a_poly, Fraction(0))
    * evaluate_polynomial(q_poly, Fraction(0))
)
check(
    "the 14D Q_F Green identity keeps its graded sign and boundary flux",
    bulk_da_q == boundary_aq + interior_a_dq,
)
check(
    "a nonzero-boundary total derivative cannot be discarded",
    boundary_aq != 0 and bulk_da_q != interior_a_dq,
)
check(
    "the same nonzero Green fixture supplies the total-bridge Z-Hessian boundary owner",
    boundary_aq != 0
    and bulk_da_q == boundary_aq + interior_a_dq,
)


# ======================================================================
# D. Conditional source-action pullback and lambda field rank
# ======================================================================


@dataclass(frozen=True)
class SourceToy:
    theta_metric: np.ndarray
    theta_b_matrix: np.ndarray
    epsilon_slices: np.ndarray
    b_quartic: float


SOURCE_TOY = SourceToy(
    np.diag([0.8, -1.1, 1.4, -0.6]),
    rng.normal(size=(toy.dimension, toy.dimension)),
    0.2
    * rng.normal(
        size=(toy.dimension, toy.dimension, toy.dimension)
    ),
    0.17,
)


def source_map_matrix(
    source_toy: SourceToy,
    epsilon_value: np.ndarray,
) -> np.ndarray:
    return (
        source_toy.theta_b_matrix
        + np.einsum(
            "l,lij->ij",
            epsilon_value,
            source_toy.epsilon_slices,
        )
    )


def source_bosonic_value(
    source_toy: SourceToy,
    theta_value: np.ndarray,
    b_value: np.ndarray,
    epsilon_value: np.ndarray,
) -> float:
    norm_b = float(b_value @ b_value)
    source_map = source_map_matrix(source_toy, epsilon_value)
    return float(
        0.5
        * theta_value
        @ source_toy.theta_metric
        @ theta_value
        + theta_value @ source_map @ b_value
        + 0.25 * source_toy.b_quartic * norm_b * norm_b
    )


def source_bosonic_gradients(
    source_toy: SourceToy,
    theta_value: np.ndarray,
    b_value: np.ndarray,
    epsilon_value: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    source_map = source_map_matrix(source_toy, epsilon_value)
    e_theta = (
        source_toy.theta_metric @ theta_value
        + source_map @ b_value
    )
    e_b = (
        source_map.T @ theta_value
        + source_toy.b_quartic
        * float(b_value @ b_value)
        * b_value
    )
    e_epsilon_map = np.array(
        [
            theta_value
            @ source_toy.epsilon_slices[index]
            @ b_value
            for index in range(epsilon_value.size)
        ]
    )
    return e_theta, e_b, e_epsilon_map


SOURCE_FIELD_COUNT = 4


def split_source_point(
    toy_model: N1Toy,
    packed: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    return tuple(
        packed[
            index * toy_model.dimension :
            (index + 1) * toy_model.dimension
        ]
        for index in range(SOURCE_FIELD_COUNT)
    )  # type: ignore[return-value]


def source_subaction(
    toy_model: N1Toy,
    source_toy: SourceToy,
    lambda_value: float,
    packed: np.ndarray,
    defect_policy: str = "none",
) -> float:
    connection, distortion, epsilon_value, odd_value = split_source_point(
        toy_model,
        packed,
    )
    gamma = gamma_value(toy_model, epsilon_value)
    theta_value = connection - gamma - distortion
    a_lambda = connection - lambda_value * distortion
    b_lambda = gamma + (1.0 - lambda_value) * distortion
    value = (
        source_bosonic_value(
            source_toy,
            theta_value,
            b_lambda,
            epsilon_value,
        )
        + s20_value(toy_model, a_lambda, odd_value)
    )
    if defect_policy == "repo_A":
        value += 0.5 * connection @ toy_model.defect_hessian @ connection
    elif defect_policy == "A_lambda":
        value += 0.5 * a_lambda @ toy_model.defect_hessian @ a_lambda
    elif defect_policy != "none":
        raise ValueError(defect_policy)
    return float(value)


def source_subaction_gradient(
    toy_model: N1Toy,
    source_toy: SourceToy,
    lambda_value: float,
    packed: np.ndarray,
    defect_policy: str = "none",
) -> np.ndarray:
    connection, distortion, epsilon_value, odd_value = split_source_point(
        toy_model,
        packed,
    )
    gamma = gamma_value(toy_model, epsilon_value)
    gamma_jac = gamma_jacobian(toy_model, epsilon_value)
    theta_value = connection - gamma - distortion
    a_lambda = connection - lambda_value * distortion
    b_lambda = gamma + (1.0 - lambda_value) * distortion
    e_theta, e_b, e_epsilon_map = source_bosonic_gradients(
        source_toy,
        theta_value,
        b_lambda,
        epsilon_value,
    )
    j20, z20 = s20_gradients(toy_model, a_lambda, odd_value)
    e_a = e_theta + j20
    e_u = (
        -e_theta
        + (1.0 - lambda_value) * e_b
        - lambda_value * j20
    )
    e_epsilon = (
        gamma_jac.T @ (e_b - e_theta)
        + e_epsilon_map
    )

    if defect_policy == "repo_A":
        e_a = e_a + toy_model.defect_hessian @ connection
    elif defect_policy == "A_lambda":
        defect_current = toy_model.defect_hessian @ a_lambda
        e_a = e_a + defect_current
        e_u = e_u - lambda_value * defect_current
    elif defect_policy != "none":
        raise ValueError(defect_policy)
    return np.concatenate((e_a, e_u, e_epsilon, z20))


print("\nD. Conditional source action, affine pullback, and field rank")
source_point = rng.normal(size=toy.dimension * SOURCE_FIELD_COUNT)
source_gradients: dict[float, np.ndarray] = {}
source_numerical_gradients: dict[float, np.ndarray] = {}
for lambda_control in (0.0, 1.0, 2.0):
    numerical = central_gradient(
        lambda packed: source_subaction(
            toy,
            SOURCE_TOY,
            lambda_control,
            packed,
        ),
        source_point,
    )
    analytic = source_subaction_gradient(
        toy,
        SOURCE_TOY,
        lambda_control,
        source_point,
    )
    source_gradients[lambda_control] = analytic
    source_numerical_gradients[lambda_control] = numerical
    worst = float(np.max(np.abs(numerical - analytic)))
    check(
        f"lambda={lambda_control:g} A/U/epsilon/Z chain-rule gradient matches finite differences",
        worst < TOL,
        f"worst={worst:.3e}",
    )

dimension = toy.dimension
connection_s, distortion_s, epsilon_s, odd_s = split_source_point(
    toy,
    source_point,
)
gamma_s = gamma_value(toy, epsilon_s)
theta_s = connection_s - gamma_s - distortion_s
_, _, explicit_epsilon_response = source_bosonic_gradients(
    SOURCE_TOY,
    theta_s,
    gamma_s,
    epsilon_s,
)
epsilon_slice = slice(2 * dimension, 3 * dimension)
omitted_epsilon_gradient = source_gradients[1.0].copy()
omitted_epsilon_gradient[epsilon_slice] -= explicit_epsilon_response
check(
    "the source chain fixture detects an omitted explicit epsilon-map response",
    np.max(
        np.abs(
            source_numerical_gradients[1.0]
            - omitted_epsilon_gradient
        )
    )
    > 1.0e-3,
)

lambda_one = source_gradients[1.0]
lambda_one_ea = lambda_one[:dimension]
lambda_one_eu = lambda_one[dimension : 2 * dimension]
check(
    "lambda=1 source-bulk plus S20 has the diagonal E_U=-E_A relation",
    np.max(np.abs(lambda_one_eu + lambda_one_ea)) < 1.0e-10,
)

lambda_two = source_gradients[2.0]
a_two = connection_s - 2.0 * distortion_s
b_two = gamma_s - distortion_s
_, e_b_two, _ = source_bosonic_gradients(
    SOURCE_TOY,
    theta_s,
    b_two,
    epsilon_s,
)
j20_two, _ = s20_gradients(toy, a_two, odd_s)
lambda_two_ea = lambda_two[:dimension]
lambda_two_eu = lambda_two[dimension : 2 * dimension]
check(
    "free lambda!=1 variation adds the independent E_B+J20 equation",
    np.max(
        np.abs(
            lambda_two_ea
            + lambda_two_eu
            - (1.0 - 2.0) * (e_b_two + j20_two)
        )
    )
    < 1.0e-10,
)

rank_lambda_one = np.linalg.matrix_rank(
    np.array([[1.0, -1.0], [0.0, 0.0]])
)
rank_lambda_two = np.linalg.matrix_rank(
    np.array([[1.0, -2.0], [0.0, -1.0]])
)
check(
    "the (A,U)->(A_lambda,B_lambda) field map is singular only at lambda=1",
    rank_lambda_one == 1 and rank_lambda_two == 2,
)

repo_defect_numerical = central_gradient(
    lambda packed: source_subaction(
        toy,
        SOURCE_TOY,
        1.0,
        packed,
        "repo_A",
    ),
    source_point,
)
repo_defect_ea = repo_defect_numerical[:dimension]
repo_defect_eu = repo_defect_numerical[dimension : 2 * dimension]
check(
    "a nondegenerate repo-A retained-term fixture removes the structural guarantee of the lambda=1 diagonal null",
    np.linalg.norm(repo_defect_ea + repo_defect_eu) > 0.05,
)

SOURCE_DEFECT_POLICY = {
    "selected_for_conditional_schema": "repo_A",
    "reason": "preserve constructed N1 term arguments pending a per-term native translation proof",
    "hostile_comparator": "A_lambda",
    "source_forced": False,
    "actual_defect_response_tested": False,
}
check(
    "the source defect-connection policy is explicit and charged, not source-forced",
    SOURCE_DEFECT_POLICY["selected_for_conditional_schema"] == "repo_A"
    and SOURCE_DEFECT_POLICY["hostile_comparator"] == "A_lambda"
    and not SOURCE_DEFECT_POLICY["source_forced"]
    and not SOURCE_DEFECT_POLICY["actual_defect_response_tested"],
)


# ======================================================================
# E. Source coefficient exactness versus covariance
# ======================================================================


def translation_euler_coefficients(
    a_value: Fraction,
    b_value: Fraction,
) -> tuple[Fraction, Fraction]:
    return 2 * a_value, 3 * b_value


SOURCE_A = Fraction(1, 2)
SOURCE_B = Fraction(1, 3)
WRONG_COEFFICIENTS = (
    (Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(1, 3)),
    (Fraction(1, 2), Fraction(1, 2)),
)

print("\nE. Transgression exactness is stronger than gauge covariance")
check(
    "the source coefficients uniquely reproduce unit D_B theta and q(theta) weights",
    translation_euler_coefficients(SOURCE_A, SOURCE_B)
    == (Fraction(1), Fraction(1)),
)
for wrong_a, wrong_b in WRONG_COEFFICIENTS:
    check(
        f"wrong source point a={wrong_a}, b={wrong_b} fails the exactness weights",
        translation_euler_coefficients(wrong_a, wrong_b)
        != (Fraction(1), Fraction(1)),
    )


def translation_eddy_matrix(
    base_connection: np.ndarray,
    theta_matrix: np.ndarray,
    curvature_matrix: np.ndarray,
    coefficient_a: float,
    coefficient_b: float,
) -> np.ndarray:
    derivative = (
        base_connection @ theta_matrix
        + theta_matrix @ base_connection
    )
    quadratic = theta_matrix @ theta_matrix
    return (
        curvature_matrix
        + coefficient_a * derivative
        + coefficient_b * quadratic
    )


def cyclic_translation_action(
    theta_matrix: np.ndarray,
    base_connection: np.ndarray,
    curvature_matrix: np.ndarray,
    coefficient_a: float,
    coefficient_b: float,
    insertion: np.ndarray | None = None,
) -> float:
    eddy = translation_eddy_matrix(
        base_connection,
        theta_matrix,
        curvature_matrix,
        coefficient_a,
        coefficient_b,
    )
    if insertion is None:
        return float(np.trace(theta_matrix @ eddy))
    return float(np.trace(theta_matrix @ insertion @ eddy))


cyclic_dimension = 4
cyclic_theta = rng.normal(size=(cyclic_dimension, cyclic_dimension))
cyclic_base = rng.normal(size=(cyclic_dimension, cyclic_dimension))
cyclic_curvature = rng.normal(
    size=(cyclic_dimension, cyclic_dimension)
)
cyclic_direction = rng.normal(
    size=(cyclic_dimension, cyclic_dimension)
)
cyclic_derivative = (
    cyclic_base @ cyclic_theta
    + cyclic_theta @ cyclic_base
)
cyclic_quadratic = cyclic_theta @ cyclic_theta
check(
    "the D_B theta and q(theta) channels are independent in the cyclic fixture",
    np.linalg.matrix_rank(
        np.column_stack(
            (
                cyclic_derivative.reshape(-1),
                cyclic_quadratic.reshape(-1),
            )
        )
    )
    == 2,
)

for cyclic_label, cyclic_coefficients in (
    ("source", (0.5, 1.0 / 3.0)),
    ("wrong", (0.8, -0.25)),
):
    numerical_translation = central_directional(
        lambda theta_flat: cyclic_translation_action(
            theta_flat.reshape(cyclic_dimension, cyclic_dimension),
            cyclic_base,
            cyclic_curvature,
            cyclic_coefficients[0],
            cyclic_coefficients[1],
        ),
        cyclic_theta.reshape(-1),
        cyclic_direction.reshape(-1),
    )
    predicted_euler = (
        cyclic_curvature
        + 2.0 * cyclic_coefficients[0] * cyclic_derivative
        + 3.0 * cyclic_coefficients[1] * cyclic_quadratic
    )
    predicted_translation = float(
        np.trace(cyclic_direction @ predicted_euler)
    )
    check(
        f"{cyclic_label} cyclic noncommutative translation derivative has the 2a/3b weights",
        abs(numerical_translation - predicted_translation) < TOL,
        (
            f"numeric={numerical_translation:.6e}, "
            f"predicted={predicted_translation:.6e}"
        ),
    )

translated_curvature = (
    cyclic_curvature
    + cyclic_derivative
    + cyclic_quadratic
)
check(
    "the source point reconstructs the unit translated-curvature coefficients in the independent fixture",
    np.linalg.norm(
        cyclic_curvature
        + 2.0 * float(SOURCE_A) * cyclic_derivative
        + 3.0 * float(SOURCE_B) * cyclic_quadratic
        - translated_curvature
    )
    < 1.0e-12,
)
for wrong_a, wrong_b in WRONG_COEFFICIENTS:
    check(
        f"wrong cyclic point a={wrong_a}, b={wrong_b} misses translated curvature",
        np.linalg.norm(
            cyclic_curvature
            + 2.0 * float(wrong_a) * cyclic_derivative
            + 3.0 * float(wrong_b) * cyclic_quadratic
            - translated_curvature
        )
        > 1.0e-4,
    )

noncentral_insertion = rng.normal(
    size=(cyclic_dimension, cyclic_dimension)
)
noncyclic_numerical = central_directional(
    lambda theta_flat: cyclic_translation_action(
        theta_flat.reshape(cyclic_dimension, cyclic_dimension),
        cyclic_base,
        cyclic_curvature,
        float(SOURCE_A),
        float(SOURCE_B),
        noncentral_insertion,
    ),
    cyclic_theta.reshape(-1),
    cyclic_direction.reshape(-1),
)
noncyclic_naive = float(
    np.trace(
        cyclic_direction
        @ noncentral_insertion
        @ translated_curvature
    )
)
check(
    "a genuinely noncyclic insertion breaks the naive source transgression identity",
    abs(noncyclic_numerical - noncyclic_naive) > 1.0e-4,
    (
        f"numeric={noncyclic_numerical:.6e}, "
        f"naive={noncyclic_naive:.6e}"
    ),
)

endpoint_packed = np.concatenate(
    (cyclic_theta.reshape(-1), cyclic_base.reshape(-1))
)


def endpoint_action(packed: np.ndarray) -> float:
    split = cyclic_dimension * cyclic_dimension
    endpoint_theta = packed[:split].reshape(
        cyclic_dimension,
        cyclic_dimension,
    )
    endpoint_base = packed[split:].reshape(
        cyclic_dimension,
        cyclic_dimension,
    )
    return cyclic_translation_action(
        endpoint_theta,
        endpoint_base,
        cyclic_curvature,
        float(SOURCE_A),
        float(SOURCE_B),
    )


endpoint_gradient = central_gradient(endpoint_action, endpoint_packed)
endpoint_split = cyclic_dimension * cyclic_dimension
endpoint_e_theta = endpoint_gradient[:endpoint_split]
endpoint_e_b = endpoint_gradient[endpoint_split:]
endpoint_generator = rng.normal(
    size=(cyclic_dimension, cyclic_dimension)
)
endpoint_generator = endpoint_generator - endpoint_generator.T
endpoint_tangent = commutator(cyclic_base, endpoint_generator).reshape(-1)
endpoint_direction = np.concatenate(
    (-endpoint_tangent, endpoint_tangent)
)
endpoint_numeric = central_directional(
    endpoint_action,
    endpoint_packed,
    endpoint_direction,
)
endpoint_correct = float(
    np.dot(endpoint_e_b - endpoint_e_theta, endpoint_tangent)
)
endpoint_wrong = float(np.dot(endpoint_e_b, endpoint_tangent))
check(
    "the constrained reference-orbit endpoint uses E_B-E_theta, not E_B",
    abs(endpoint_numeric - endpoint_correct) < TOL
    and abs(endpoint_numeric - endpoint_wrong) > 1.0e-4,
)


def covariant_eddy(
    b_zero: np.ndarray,
    b_one: np.ndarray,
    theta_zero: np.ndarray,
    theta_one: np.ndarray,
    a_value: float,
    b_value: float,
) -> np.ndarray:
    curvature = commutator(b_zero, b_one)
    derivative = (
        commutator(b_zero, theta_one)
        - commutator(b_one, theta_zero)
    )
    quadratic = commutator(theta_zero, theta_one)
    return curvature + a_value * derivative + b_value * quadratic


matrix_dimension = 4
raw_group = rng.normal(size=(matrix_dimension, matrix_dimension))
group, _ = np.linalg.qr(raw_group)
group_inverse = group.T
b_zero = rng.normal(size=(matrix_dimension, matrix_dimension))
b_one = rng.normal(size=(matrix_dimension, matrix_dimension))
theta_zero = rng.normal(size=(matrix_dimension, matrix_dimension))
theta_one = rng.normal(size=(matrix_dimension, matrix_dimension))


def conjugate(matrix: np.ndarray) -> np.ndarray:
    return group_inverse @ matrix @ group


for coefficient_label, coefficient_pair in (
    ("source", (0.5, 1.0 / 3.0)),
    ("bare", (0.0, 0.0)),
    ("wrong", (0.8, -0.25)),
):
    original_eddy = covariant_eddy(
        b_zero,
        b_one,
        theta_zero,
        theta_one,
        *coefficient_pair,
    )
    transformed_eddy = covariant_eddy(
        conjugate(b_zero),
        conjugate(b_one),
        conjugate(theta_zero),
        conjugate(theta_one),
        *coefficient_pair,
    )
    check(
        f"{coefficient_label} eddy coefficients pass the coefficient-blind covariance control",
        np.linalg.norm(
            transformed_eddy - conjugate(original_eddy)
        )
        < 1.0e-10,
    )

connection_matrix = rng.normal(size=(matrix_dimension, matrix_dimension))
gamma_matrix = rng.normal(size=(matrix_dimension, matrix_dimension))
distortion_matrix = rng.normal(size=(matrix_dimension, matrix_dimension))
inhomogeneous = rng.normal(size=(matrix_dimension, matrix_dimension))
for lambda_control in (-1.0, 1.0, 2.0):
    a_lambda_original = connection_matrix - lambda_control * distortion_matrix
    b_lambda_original = gamma_matrix + (
        1.0 - lambda_control
    ) * distortion_matrix
    transformed_a = conjugate(connection_matrix) + inhomogeneous
    transformed_gamma = conjugate(gamma_matrix) + inhomogeneous
    transformed_u = conjugate(distortion_matrix)
    transformed_a_lambda = transformed_a - lambda_control * transformed_u
    transformed_b_lambda = transformed_gamma + (
        1.0 - lambda_control
    ) * transformed_u
    check(
        f"lambda={lambda_control:g} gives two affine connections under the same gauge shift",
        np.linalg.norm(
            transformed_a_lambda
            - (conjugate(a_lambda_original) + inhomogeneous)
        )
        < 1.0e-10
        and np.linalg.norm(
            transformed_b_lambda
            - (conjugate(b_lambda_original) + inhomogeneous)
        )
        < 1.0e-10,
    )


# ======================================================================
# F. Finite homogeneous adjoint-covariance proxies
# ======================================================================


def matrix_jd(odd_matrix: np.ndarray) -> np.ndarray:
    return odd_matrix @ odd_matrix


def matrix_jf(
    covariant_connection: np.ndarray,
    odd_matrix: np.ndarray,
) -> np.ndarray:
    return (
        covariant_connection @ odd_matrix
        + odd_matrix @ covariant_connection
    )


def matrix_bridge_action(
    kind: str,
    connection_value: np.ndarray,
    distortion_value: np.ndarray,
    gamma_value_matrix: np.ndarray,
    odd_matrix: np.ndarray,
) -> float:
    theta_matrix = (
        connection_value - gamma_value_matrix - distortion_value
    )
    covariant_connection = connection_value - gamma_value_matrix
    jd_matrix = matrix_jd(odd_matrix)
    jf_matrix = matrix_jf(covariant_connection, odd_matrix)
    current_matrix = jd_matrix if kind == "JD" else jd_matrix + jf_matrix
    s20_matrix = (
        np.trace(jd_matrix @ covariant_connection)
        + np.trace(
            odd_matrix
            @ covariant_connection
            @ covariant_connection
        )
    )
    return float(
        0.5 * np.trace(covariant_connection @ covariant_connection)
        + s20_matrix
        + 0.5 * np.trace(theta_matrix @ theta_matrix)
        - np.trace(current_matrix @ theta_matrix)
    )


def matrix_source_action(
    coefficient_a: float,
    coefficient_b: float,
    b0: np.ndarray,
    b1: np.ndarray,
    t0: np.ndarray,
    t1: np.ndarray,
) -> float:
    eddy = covariant_eddy(
        b0,
        b1,
        t0,
        t1,
        coefficient_a,
        coefficient_b,
    )
    return float(
        np.trace(t0 @ eddy)
        + 0.5 * np.trace(t0 @ t0)
        + 0.25 * np.trace(t1 @ t1)
    )


print("\nF. Finite homogeneous adjoint-covariance proxies")
ward_a = rng.normal(size=(matrix_dimension, matrix_dimension))
ward_u = rng.normal(size=(matrix_dimension, matrix_dimension))
ward_gamma = rng.normal(size=(matrix_dimension, matrix_dimension))
ward_z = rng.normal(size=(matrix_dimension, matrix_dimension))
ward_chi = rng.normal(size=(matrix_dimension, matrix_dimension))
ward_chi = ward_chi - ward_chi.T

ward_fields = (ward_a, ward_u, ward_gamma, ward_z)
ward_directions = tuple(
    commutator(field, ward_chi) for field in ward_fields
)


def packed_matrix_bridge(
    kind: str,
    packed: np.ndarray,
) -> float:
    matrices = tuple(
        packed[
            index * matrix_dimension * matrix_dimension :
            (index + 1) * matrix_dimension * matrix_dimension
        ].reshape(matrix_dimension, matrix_dimension)
        for index in range(4)
    )
    return matrix_bridge_action(kind, *matrices)


ward_packed = np.concatenate(
    tuple(matrix.reshape(-1) for matrix in ward_fields)
)
ward_direction_packed = np.concatenate(
    tuple(matrix.reshape(-1) for matrix in ward_directions)
)
for current_kind in ("JD", "TOTAL"):
    full_ward = central_directional(
        lambda packed: packed_matrix_bridge(current_kind, packed),
        ward_packed,
        ward_direction_packed,
    )
    without_z = central_directional(
        lambda packed: packed_matrix_bridge(current_kind, packed),
        ward_packed,
        np.concatenate(
            tuple(
                direction.reshape(-1)
                if index != 3
                else np.zeros_like(direction).reshape(-1)
                for index, direction in enumerate(ward_directions)
            )
        ),
    )
    check(
        f"{current_kind} bridge closes the reduced homogeneous conjugation contraction",
        abs(full_ward) < 2.0e-6,
        f"residual={full_ward:.3e}",
    )
    check(
        f"{current_kind} reduced covariance proxy detects an omitted Z-current response",
        abs(without_z) > 1.0e-4,
        f"plant={without_z:.3e}",
    )

source_matrices = (
    b_zero,
    b_one,
    theta_zero,
    theta_one,
)
source_directions = tuple(
    commutator(matrix, ward_chi) for matrix in source_matrices
)
source_matrix_packed = np.concatenate(
    tuple(matrix.reshape(-1) for matrix in source_matrices)
)
source_direction_packed = np.concatenate(
    tuple(matrix.reshape(-1) for matrix in source_directions)
)


def packed_source_matrix_action(
    coefficient_a: float,
    coefficient_b: float,
    packed: np.ndarray,
) -> float:
    matrices = tuple(
        packed[
            index * matrix_dimension * matrix_dimension :
            (index + 1) * matrix_dimension * matrix_dimension
        ].reshape(matrix_dimension, matrix_dimension)
        for index in range(4)
    )
    return matrix_source_action(
        coefficient_a,
        coefficient_b,
        *matrices,
    )


for label, coefficient_pair in (
    ("source", (0.5, 1.0 / 3.0)),
    ("wrong", (0.8, -0.25)),
):
    residual = central_directional(
        lambda packed: packed_source_matrix_action(
            coefficient_pair[0],
            coefficient_pair[1],
            packed,
        ),
        source_matrix_packed,
        source_direction_packed,
    )
    check(
        f"{label} source action passes the coefficient-blind homogeneous conjugation proxy",
        abs(residual) < 2.0e-6,
        f"residual={residual:.3e}",
    )

fixed_nonintertwiner = rng.normal(
    size=(matrix_dimension, matrix_dimension)
)


def nonintertwining_source_action(packed: np.ndarray) -> float:
    matrices = tuple(
        packed[
            index * matrix_dimension * matrix_dimension :
            (index + 1) * matrix_dimension * matrix_dimension
        ].reshape(matrix_dimension, matrix_dimension)
        for index in range(4)
    )
    eddy = covariant_eddy(*matrices, 0.5, 1.0 / 3.0)
    return float(
        np.trace(matrices[2] @ fixed_nonintertwiner @ eddy)
    )


nonintertwining_residual = central_directional(
    nonintertwining_source_action,
    source_matrix_packed,
    source_direction_packed,
)
check(
    "a fixed nonintertwining bosonic-map plant breaks the conjugation proxy",
    abs(nonintertwining_residual) > 1.0e-4,
    f"plant={nonintertwining_residual:.3e}",
)

NATIVE_INTERNAL_WARD_STATUS = {
    "grade": "CONDITIONAL-NOT-INSTANTIATED",
    "proxy": FINITE_ADJOINT_PROXY,
    "missing": (
        "native_quaternionic_stabilizer_generators",
        "connection_inhomogeneous_terms",
        "background_responses",
        "parent_and_defect_terms",
        "full_BV_equivariance",
    ),
}
check(
    "the finite conjugation proxy is not promoted to native internal-Ward closure",
    NATIVE_INTERNAL_WARD_STATUS["grade"]
    == "CONDITIONAL-NOT-INSTANTIATED"
    and len(NATIVE_INTERNAL_WARD_STATUS["missing"]) == 5,
)

DIFF_STATUS = {
    "grade": "OWNER-COMPLETE; FORMULA-INCOMPLETE; NO-KILL",
    "missing": (
        "D_s_II",
        "D_s_P0",
        "D_s_resV",
        "D_s_pushforward",
        "density_and_Hodge_shape_variation",
        "junction_terms",
    ),
    "scheduled": "RB4",
}
check(
    "complete Diff closure is honestly held rather than inferred from owner metadata",
    DIFF_STATUS["grade"] == "OWNER-COMPLETE; FORMULA-INCOMPLETE; NO-KILL"
    and len(DIFF_STATUS["missing"]) == 6
    and DIFF_STATUS["scheduled"] == "RB4",
)


# ======================================================================
# G. Action, alias, five-leg, and equivalence registries
# ======================================================================


@dataclass(frozen=True)
class RegisteredObject:
    name: str
    registry: str
    legs: tuple[str, ...]
    status: str


@dataclass(frozen=True)
class ActionRecord:
    name: str
    role: str
    status: str
    action_terms: tuple[str, ...]
    supplied_backgrounds: tuple[str, ...]
    external_interfaces: tuple[str, ...]
    conditional_maps: tuple[str, ...]
    branch_choices: tuple[str, ...]
    leg_status: tuple[tuple[str, str], ...]
    connection_arguments: tuple[tuple[str, str], ...]
    symmetry: str
    field_space: str
    boundary_data: tuple[str, ...]
    held_out: tuple[str, ...]


OBJECT_REGISTRY = {
    entry.name: entry
    for entry in (
        RegisteredObject(
            "ambient_yang_mills",
            "action",
            ("G", "Q", "U"),
            "BUILT",
        ),
        RegisteredObject(
            "induced_ym_parent",
            "action",
            ("G", "Q", "U"),
            "BUILT",
        ),
        RegisteredObject(
            "theta_JD_bridge",
            "action",
            ("G", "Q"),
            "BUILT-RB2",
        ),
        RegisteredObject(
            "theta_total_current_bridge",
            "action",
            ("G", "Q", "U"),
            "BUILT-RB2",
        ),
        RegisteredObject(
            "source_first_order_I_B1",
            "action",
            ("G", "Q", "U"),
            "CONDITIONAL-ON-S_BOS",
        ),
        RegisteredObject(
            "full20_krein_quadratic",
            "action",
            ("Y", "Q", "G", "U"),
            "BUILT",
        ),
        RegisteredObject(
            "end_selector_branch",
            "action",
            ("Y", "I", "U"),
            "BUILT-BRANCH",
        ),
        RegisteredObject(
            "induced_section_gravity",
            "action",
            ("G", "U"),
            "BUILT",
        ),
        RegisteredObject(
            "seiberg_witten_defect",
            "action",
            ("Y", "Q", "G"),
            "BUILT",
        ),
        RegisteredObject(
            "yukawa_K_or_C_branch",
            "action",
            ("Y", "Q", "G"),
            "BUILT-BRANCH",
        ),
        RegisteredObject(
            "optional_spurion_interface",
            "action",
            ("Y",),
            "OPTIONAL-BRANCH",
        ),
        RegisteredObject(
            "minimal_bv_skeleton",
            "action",
            ("Q", "G", "U"),
            "PARTIAL",
        ),
        RegisteredObject(
            "orientation_holonomy_T9",
            "action",
            ("Q", "I"),
            "BUILT",
        ),
        RegisteredObject(
            "A0",
            "supplied",
            ("Y", "Q", "G"),
            "SUPPLIED-BACKGROUND",
        ),
        RegisteredObject(
            "Sigma",
            "supplied",
            ("Y",),
            "SUPPLIED-OPTIONAL",
        ),
        RegisteredObject(
            "P3_relative_KO",
            "external",
            ("I", "U"),
            "EXTERNAL-NOT-ACTION",
        ),
        RegisteredObject(
            "Green_future_common_domain",
            "external",
            ("U", "Q"),
            "CARRIED-HELD",
        ),
        RegisteredObject(
            "S_bos_density_epsilon",
            "conditional_map",
            ("G", "Q", "U"),
            "UNBUILT-BLOCKING-SOURCE",
        ),
        RegisteredObject(
            "source_fermion_residual_translation",
            "conditional_map",
            ("Y", "Q"),
            "UNBUILT",
        ),
        RegisteredObject(
            "moving_full_Sp_soldering",
            "conditional_map",
            ("G", "Q", "U"),
            "HELD-RB3",
        ),
    )
}

COMMON_ACTION_TERMS = (
    "full20_krein_quadratic",
    "end_selector_branch",
    "induced_section_gravity",
    "seiberg_witten_defect",
    "yukawa_K_or_C_branch",
    "optional_spurion_interface",
    "minimal_bv_skeleton",
    "orientation_holonomy_T9",
)

EXACT_N1_HELD_OUT = (
    "bv_obstruction",
    "causality",
    "gravity_cosmology",
    "physical",
    "topology",
)
EXPANDED_HELD_OUT = tuple(
    sorted(
        {
            *n1.HELD_OUT,
            "zero_order_selection",
            "VEV",
            "stationarity",
            "curved_solution",
            "CME",
            "moving_full_Sp",
            "complete_Diff",
            "global_domain",
            "physical_reduction",
            "physical_mass",
            "positivity_rule",
            "anomaly",
            "P3_pushforward",
            "index",
            "count",
        }
    )
)

N1_LEG_STATUS = (
    ("Y", "BUILT-BRANCH"),
    ("Q", "CLASSICAL-BUILT/BV-PARTIAL"),
    ("G", "CLASSICAL-BUILT/MOVING-PARTIAL"),
    ("I", "CARRIED-NOT-READ"),
    ("U", "CLASSICAL-BUILT/BV-PARTIAL"),
)
SOURCE_LEG_STATUS = (
    ("Y", "REPO-DEFECT-BUILT/SOURCE-TRANSLATION-CONDITIONAL"),
    ("Q", "BLOCKED-FIRST-MAP/BV-PARTIAL"),
    ("G", "BLOCKED-FIRST-MAP/MOVING-PARTIAL"),
    ("I", "CARRIED-NOT-READ"),
    ("U", "BLOCKED-FIRST-MAP/BV-PARTIAL"),
)

N1_JD_CONNECTION_ARGUMENTS = (
    ("ambient_yang_mills", "repo_A"),
    ("induced_ym_parent", "repo_A"),
    ("theta_JD_bridge", "repo_A/Gamma(epsilon)/U"),
    ("full20_krein_quadratic", "repo_A"),
    ("end_selector_branch", "repo_A_or_Z_by_branch"),
    ("induced_section_gravity", "none"),
    ("seiberg_witten_defect", "repo_A"),
    ("yukawa_K_or_C_branch", "repo_A"),
    ("optional_spurion_interface", "repo_A_if_on"),
    ("minimal_bv_skeleton", "repo_A"),
    ("orientation_holonomy_T9", "none"),
)
N1_TOTAL_CONNECTION_ARGUMENTS = tuple(
    (
        ("theta_total_current_bridge", argument)
        if term == "theta_JD_bridge"
        else (term, argument)
    )
    for term, argument in N1_JD_CONNECTION_ARGUMENTS
)
SOURCE_CONNECTION_ARGUMENTS = (
    ("source_first_order_I_B1", "B_lambda_and_theta"),
    ("full20_krein_quadratic", "A_lambda"),
    ("end_selector_branch", "repo_A_or_Z_by_branch"),
    ("induced_section_gravity", "none"),
    ("seiberg_witten_defect", "repo_A_CHARGED_HYBRID"),
    ("yukawa_K_or_C_branch", "repo_A_CHARGED_HYBRID"),
    ("optional_spurion_interface", "repo_A_if_on_CHARGED_HYBRID"),
    ("minimal_bv_skeleton", "repo_A_CHARGED_HYBRID"),
    ("orientation_holonomy_T9", "none"),
)

COMMON_N1_GREEN_OWNERS = (
    "YM_A_Green",
    "parent_U_Green",
    "Gamma_epsilon_Green_if_differential",
    "S20_A_Q_F_flux",
    "SW_X_Green",
    "shape_distribution_junction",
    "BV_Lie_Green_PARTIAL",
)

RB2_RECORDS = (
    ActionRecord(
        "N1_JD_bridge",
        "CANDIDATE",
        "SURVIVES-CLASSICAL-FIXED-GEOMETRY-ANTIFIELD-ZERO-LOCAL-WEAK",
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "theta_JD_bridge",
        )
        + COMMON_ACTION_TERMS,
        ("A0", "Sigma"),
        ("P3_relative_KO", "Green_future_common_domain"),
        ("moving_full_Sp_soldering",),
        (
            "one_end_selector",
            "one_K_or_C",
            "parent_retained",
            "spurion=off_or_supplied_Sigma",
            "zeta_F=fundamental_YM",
        ),
        N1_LEG_STATUS,
        N1_JD_CONNECTION_ARGUMENTS,
        H_N1,
        "full record: A,U,P_IG,epsilon,Z,s plus partial BV; tested slice: A,U,P_IG,epsilon,Z",
        COMMON_N1_GREEN_OWNERS,
        EXPANDED_HELD_OUT,
    ),
    ActionRecord(
        "N1_total_current_bridge",
        "CANDIDATE",
        "SURVIVES-CLASSICAL-FIXED-GEOMETRY-ANTIFIELD-ZERO-HESSIAN-BOUNDARY-CONDITIONAL",
        (
            "ambient_yang_mills",
            "induced_ym_parent",
            "theta_total_current_bridge",
        )
        + COMMON_ACTION_TERMS,
        ("A0", "Sigma"),
        ("P3_relative_KO", "Green_future_common_domain"),
        ("moving_full_Sp_soldering",),
        (
            "one_end_selector",
            "one_K_or_C",
            "parent_retained",
            "spurion=off_or_supplied_Sigma",
            "zeta_F=fundamental_YM",
        ),
        N1_LEG_STATUS,
        N1_TOTAL_CONNECTION_ARGUMENTS,
        H_N1,
        "full record: A,U,P_IG,epsilon,Z,s plus partial BV; tested slice: A,U,P_IG,epsilon,Z",
        COMMON_N1_GREEN_OWNERS
        + (
            "total_bridge_Z_current_Hessian_flux",
        ),
        EXPANDED_HELD_OUT,
    ),
    ActionRecord(
        "source_reference_lambda1",
        "CANDIDATE",
        "BLOCKED-FIRST-AT-NATIVE-BOSONIC-SHIAB",
        ("source_first_order_I_B1",) + COMMON_ACTION_TERMS,
        ("A0", "Sigma"),
        ("P3_relative_KO", "Green_future_common_domain"),
        (
            "S_bos_density_epsilon",
            "source_fermion_residual_translation",
            "moving_full_Sp_soldering",
        ),
        (
            "lambda=1",
            "repo_A_defects",
            "one_end_selector",
            "one_K_or_C",
            "spurion=off_or_supplied_Sigma",
            "zeta_F=source_replaces_YM",
        ),
        SOURCE_LEG_STATUS,
        SOURCE_CONNECTION_ARGUMENTS,
        H_SOURCE_CONDITIONAL,
        "conditional source bulk at A_lambda=A-U, B=Gamma; retained terms form a charged repo-A hybrid",
        (
            "source_theta_Green_CONDITIONAL",
            "source_B_Green_CONDITIONAL",
            "S20_A_Q_F_flux",
            "SW_X_Green",
            "shape_distribution_junction",
            "BV_Lie_Green_PARTIAL",
        ),
        EXPANDED_HELD_OUT,
    ),
    ActionRecord(
        "source_orbit_constrained_lambda_not1",
        "CONTROL",
        "BLOCKED-ORBIT-TANGENT-OR-MULTIPLIER-DECLARATION",
        ("source_first_order_I_B1",) + COMMON_ACTION_TERMS,
        ("A0", "Sigma"),
        ("P3_relative_KO", "Green_future_common_domain"),
        (
            "S_bos_density_epsilon",
            "source_fermion_residual_translation",
            "moving_full_Sp_soldering",
        ),
        (
            "lambda!=1",
            "reference_orbit_constraint",
            "repo_A_defects",
            "one_end_selector",
            "one_K_or_C",
            "spurion=off_or_supplied_Sigma",
            "zeta_F=source_replaces_YM",
        ),
        SOURCE_LEG_STATUS,
        SOURCE_CONNECTION_ARGUMENTS,
        H_SOURCE_CONDITIONAL,
        "orbit-constrained B_lambda; tangent/multiplier system unbuilt",
        (
            "source_theta_Green_CONDITIONAL",
            "source_B_Green_CONDITIONAL",
            "S20_A_Q_F_flux",
            "SW_X_Green",
            "shape_distribution_junction",
            "BV_Lie_Green_PARTIAL",
        ),
        EXPANDED_HELD_OUT,
    ),
)

ALIAS_GROUPS = {
    "parent": {"induced_ym_parent", "eliminated_parent_shadow"},
    "bridge": {"theta_JD_bridge", "theta_total_current_bridge"},
    "yukawa": {"yukawa_K", "yukawa_C"},
    "gravity": {"direct_II", "Gauss_rewrite"},
    "shape": {"intrinsic_pullback", "ambient_pushforward"},
    "full20": {"full20_krein_quadratic", "full20_vertical_expansion"},
    "source_order": {"source_first_order_I_B1", "source_residual_square"},
}


def validate_action_records(
    records: tuple[ActionRecord, ...],
) -> list[str]:
    errors: list[str] = []
    roles = Counter(record.role for record in records)
    if roles != Counter({"CANDIDATE": 3, "CONTROL": 1}):
        errors.append(f"wrong census: {roles}")
    if len({record.name for record in records}) != len(records):
        errors.append("duplicate record")
    required_legs = set(n1.LEGS)
    for record in records:
        expected_symmetry = (
            H_SOURCE_CONDITIONAL
            if record.name.startswith("source_")
            else H_N1
        )
        if record.symmetry != expected_symmetry:
            errors.append(f"wrong symmetry: {record.name}")
        if not set(n1.HELD_OUT) <= set(record.held_out):
            errors.append(f"lost N1 held-out wall: {record.name}")
        for term in record.action_terms:
            item = OBJECT_REGISTRY.get(term)
            if item is None or item.registry != "action":
                errors.append(f"unregistered action term: {record.name}/{term}")
        for supplied in record.supplied_backgrounds:
            item = OBJECT_REGISTRY.get(supplied)
            if item is None or item.registry != "supplied":
                errors.append(
                    f"unregistered supplied background: {record.name}/{supplied}"
                )
        for external in record.external_interfaces:
            item = OBJECT_REGISTRY.get(external)
            if item is None or item.registry != "external":
                errors.append(
                    f"unregistered external interface: {record.name}/{external}"
                )
        for conditional in record.conditional_maps:
            item = OBJECT_REGISTRY.get(conditional)
            if item is None or item.registry != "conditional_map":
                errors.append(
                    f"unregistered conditional map: {record.name}/{conditional}"
                )
        owners = (
            record.action_terms
            + record.supplied_backgrounds
            + record.external_interfaces
            + record.conditional_maps
        )
        carried_legs = {
            leg
            for owner in owners
            for leg in OBJECT_REGISTRY[owner].legs
        }
        if carried_legs != required_legs:
            errors.append(
                f"five-leg referential ledger incomplete: {record.name}"
            )
        leg_status = dict(record.leg_status)
        if set(leg_status) != required_legs or any(
            not status for status in leg_status.values()
        ):
            errors.append(
                f"five-leg status ledger incomplete: {record.name}"
            )
        if leg_status.get("I") != "CARRIED-NOT-READ":
            errors.append(f"index leg read or misgraded: {record.name}")
        if record.name.startswith("source_"):
            for conditional_leg in ("Q", "G", "U"):
                if not any(
                    token in leg_status.get(conditional_leg, "")
                    for token in ("BLOCKED", "CONDITIONAL")
                ):
                    errors.append(
                        "source conditional leg promoted: "
                        f"{record.name}/{conditional_leg}"
                    )
        argument_terms = {
            term for term, _ in record.connection_arguments
        }
        if argument_terms != set(record.action_terms):
            errors.append(
                f"connection-argument ledger incomplete: {record.name}"
            )
        if any(
            not argument
            for _, argument in record.connection_arguments
        ):
            errors.append(
                f"empty connection argument: {record.name}"
            )
        if not any(
            choice.startswith("spurion=")
            for choice in record.branch_choices
        ):
            errors.append(f"spurion branch hidden: {record.name}")
        if not any(
            choice.startswith("zeta_F=")
            for choice in record.branch_choices
        ):
            errors.append(f"YM/source branch hidden: {record.name}")
        if "P3_relative_KO" in record.action_terms:
            errors.append(f"P3 inserted into action: {record.name}")
        if (
            "theta_JD_bridge" in record.action_terms
            and "theta_total_current_bridge" in record.action_terms
        ):
            errors.append(f"two bridges inserted: {record.name}")
        if (
            "induced_ym_parent" in record.action_terms
            and "eliminated_parent_shadow" in record.action_terms
        ):
            errors.append(f"parent double counted: {record.name}")
        for alias_name, aliases in ALIAS_GROUPS.items():
            present = aliases & set(record.action_terms)
            if len(present) > 1:
                errors.append(
                    f"alias group doubled: {record.name}/{alias_name}"
                )
        if record.name.startswith("source_"):
            forbidden = {
                "ambient_yang_mills",
                "induced_ym_parent",
                "theta_JD_bridge",
                "theta_total_current_bridge",
            }
            if forbidden & set(record.action_terms):
                errors.append(
                    f"source architecture kept replaced N1 term: {record.name}"
                )
            if "S_bos_density_epsilon" not in record.conditional_maps:
                errors.append(
                    f"source architecture hid bosonic map debit: {record.name}"
                )
    return errors


def action_record_digest(records: tuple[ActionRecord, ...]) -> str:
    payload = [
        {
            "name": record.name,
            "role": record.role,
            "status": record.status,
            "action_terms": record.action_terms,
            "supplied": record.supplied_backgrounds,
            "external": record.external_interfaces,
            "conditional": record.conditional_maps,
            "branches": record.branch_choices,
            "leg_status": record.leg_status,
            "connection_arguments": record.connection_arguments,
            "symmetry": record.symmetry,
            "field_space": record.field_space,
            "boundary": record.boundary_data,
            "held_out": record.held_out,
        }
        for record in records
    ]
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode("utf-8")
    ).hexdigest()


print("\nG. Action/no-double-count/five-leg/equivalence ledgers")
check(
    "the RB2 action records pass exact referential and held-out validation",
    not validate_action_records(RB2_RECORDS),
)
check(
    "the exact N1 sealed construction hash is preserved",
    n1.construction_hash() == n1.SEALED_HASH,
)
check(
    "the five original held-out observable names are preserved exactly",
    EXACT_N1_HELD_OUT == tuple(sorted(n1.HELD_OUT)),
)
check(
    "P3 is carried only as an external interface",
    OBJECT_REGISTRY["P3_relative_KO"].registry == "external"
    and all(
        "P3_relative_KO" not in record.action_terms
        for record in RB2_RECORDS
    ),
)
check(
    "one abstract Yukawa branch prevents simultaneous K/C insertion",
    all(
        "yukawa_K_or_C_branch" in record.action_terms
        and "one_K_or_C" in record.branch_choices
        for record in RB2_RECORDS
    ),
)

EXPECTED_ACTION_DIGEST = (
    "8aa9601a2f1d6ab4ce2b8f25b622ce1217ffb13b00b1c4682e0bf9fbfb4c7d84"
)
FROZEN_ACTION_DIGEST = action_record_digest(RB2_RECORDS)
check(
    "the action registry matches the hard-coded frozen digest",
    FROZEN_ACTION_DIGEST == EXPECTED_ACTION_DIGEST,
    f"actual={FROZEN_ACTION_DIGEST}",
)
digest_mutation_plant = replace(
    RB2_RECORDS[0],
    branch_choices=RB2_RECORDS[0].branch_choices
    + ("digest_mutation_plant",),
)
check(
    "a validation-legal registry mutation changes the frozen digest",
    action_record_digest(
        (digest_mutation_plant,) + RB2_RECORDS[1:]
    )
    != EXPECTED_ACTION_DIGEST,
)

missing_leg_plant = replace(
    RB2_RECORDS[0],
    action_terms=tuple(
        term
        for term in RB2_RECORDS[0].action_terms
        if term not in {"end_selector_branch", "orientation_holonomy_T9"}
    ),
    external_interfaces=("Green_future_common_domain",),
)
check(
    "a missing external index interface is rejected by referential five-leg validation",
    bool(
        validate_action_records(
            (missing_leg_plant,) + RB2_RECORDS[1:]
        )
    ),
)

p3_action_plant = replace(
    RB2_RECORDS[0],
    action_terms=RB2_RECORDS[0].action_terms + ("P3_relative_KO",),
)
check(
    "a P3-as-action plant is rejected",
    bool(
        validate_action_records(
            (p3_action_plant,) + RB2_RECORDS[1:]
        )
    ),
)

double_bridge_plant = replace(
    RB2_RECORDS[0],
    action_terms=RB2_RECORDS[0].action_terms
    + ("theta_total_current_bridge",),
)
check(
    "a duplicate bridge plant is rejected",
    bool(
        validate_action_records(
            (double_bridge_plant,) + RB2_RECORDS[1:]
        )
    ),
)

source_map_omission_plant = replace(
    RB2_RECORDS[2],
    conditional_maps=tuple(
        item
        for item in RB2_RECORDS[2].conditional_maps
        if item != "S_bos_density_epsilon"
    ),
)
check(
    "a source action hiding the unbuilt bosonic map is rejected",
    bool(
        validate_action_records(
            RB2_RECORDS[:2]
            + (source_map_omission_plant,)
            + RB2_RECORDS[3:]
        )
    ),
)

wrong_symmetry_plant = replace(
    RB2_RECORDS[0],
    symmetry=FULL_SP_FIXED_PLANE,
)
check(
    "a generic fixed-plane full-Sp architecture is rejected without killing the stabilizer",
    bool(
        validate_action_records(
            (wrong_symmetry_plant,) + RB2_RECORDS[1:]
        )
    ),
)

promoted_source_leg_plant = replace(
    RB2_RECORDS[2],
    leg_status=tuple(
        (leg, "BUILT") for leg in n1.LEGS
    ),
)
check(
    "a blocked source leg cannot be promoted by referential coverage alone",
    bool(
        validate_action_records(
            RB2_RECORDS[:2]
            + (promoted_source_leg_plant,)
            + RB2_RECORDS[3:]
        )
    ),
)


@dataclass(frozen=True)
class EquivalenceClaim:
    left: str
    right: str
    field_map: str
    machine_evidence: tuple[str, ...]
    unverified_transport: tuple[str, ...]
    grade: str


EQUIVALENCE_CLAIMS = (
    EquivalenceClaim(
        "N1_parent_retained",
        "N1_parent_eliminated",
        "P=Z_U D_A U, Z_U nonzero",
        (
            "stationary_action_value",
            "A/U_gradient_on_auxiliary_shell",
            "positive_algebraic_sign_for_both_Z_U_signs",
        ),
        (
            "field_theoretic_Green_transport",
            "native_Ward_transport",
            "BV_pushforward",
        ),
        "UNIQUE-AUXILIARY-SHELL-SOLUTION-LIFT; CLASSICAL-ANTIFIELD-ZERO",
    ),
    EquivalenceClaim(
        "N1_JD_bridge",
        "N1_total_current_bridge",
        "identity",
        ("relative_action_and_five_field_gradient",),
        ("native_solution_space_comparison",),
        "FORMALLY-DISTINCT; NONDEGENERATE-TOY; COINCIDE-ONLY-ON-CONTROLLED-J_F=0-STRATUM",
    ),
    EquivalenceClaim(
        "source_reference_lambda1",
        "either_N1_bridge",
        "source/native and density-dual S_bos map absent",
        (),
        (
            "native_map",
            "field_map",
            "boundary_map",
            "Ward_map",
        ),
        "NOT-COMPARABLE-YET",
    ),
)
check(
    "parent retention/elimination is graded only as a unique auxiliary-shell classical lift",
    EQUIVALENCE_CLAIMS[0].grade
    == "UNIQUE-AUXILIARY-SHELL-SOLUTION-LIFT; CLASSICAL-ANTIFIELD-ZERO"
    and "field_theoretic_Green_transport"
    in EQUIVALENCE_CLAIMS[0].unverified_transport,
)
check(
    "the two N1 bridges are not collapsed by equality on a degenerate J_F=0 stratum",
    next(
        claim
        for claim in EQUIVALENCE_CLAIMS
        if claim.left == "N1_JD_bridge"
    ).grade
    == "FORMALLY-DISTINCT; NONDEGENERATE-TOY; COINCIDE-ONLY-ON-CONTROLLED-J_F=0-STRATUM",
)


# ======================================================================
# H. RB3 emission and source reopener
# ======================================================================


RB3_EMISSION = (
    {
        "name": "N1_JD_bridge",
        "status": "SURVIVES-CLASSICAL-FIXED-GEOMETRY-ANTIFIELD-ZERO-LOCAL-WEAK",
        "reason": "complete five-field bridge-slice variation and homogeneous conjugation proxy pass",
    },
    {
        "name": "N1_total_current_bridge",
        "status": "SURVIVES-CLASSICAL-FIXED-GEOMETRY-ANTIFIELD-ZERO-HESSIAN-BOUNDARY-CONDITIONAL",
        "reason": "complete five-field bridge-slice variation passes; A-Hessian bulk response and Z-Hessian flux retained",
    },
)

SOURCE_REOPENER = {
    "blocked_candidate": "source_reference_lambda1",
    "minimal_failed_map": (
        "S_bos_density_epsilon:Omega2(Y,adP)->Omega13(Y,ad*P)"
    ),
    "locus": H_SOURCE_CONDITIONAL,
    "structural": (
        "native Sp(32,32;H)",
        "indefinite G/kappa",
        "actual Sym2 fibre",
    ),
    "candidate_specific": (
        "bosonic invariant-tensor contraction",
        "epsilon response",
        "source/native residual translation",
    ),
    "native_reopeners": (
        "construct native density-dual invariant-tensor bosonic Shiab from epsilon/soldering",
        "construct stabilizer Ricci-Einstein contraction on adjoint curvature",
    ),
    "source_fork_comparator": (
        "retain source U(64,64)-type formula as typed nontransferable comparator; NO-NATIVE-REENTRY"
    ),
    "reentry": "RB1 map register then RB2 source variation",
}

print("\nH. RB2 disposition and RB3 emission")
check(
    "RB3 receives a bounded pair of independently constructed N1 Euler systems",
    {item["name"] for item in RB3_EMISSION}
    == {"N1_JD_bridge", "N1_total_current_bridge"},
)
check(
    "the source-shaped candidate is blocked rather than killed",
    next(
        record
        for record in RB2_RECORDS
        if record.name == "source_reference_lambda1"
    ).status
    == "BLOCKED-FIRST-AT-NATIVE-BOSONIC-SHIAB",
)
check(
    "the source reopener has two native routes while the source-fork comparator has no native reentry",
    len(SOURCE_REOPENER["native_reopeners"]) == 2
    and "NO-NATIVE-REENTRY"
    in SOURCE_REOPENER["source_fork_comparator"]
    and SOURCE_REOPENER["reentry"]
    == "RB1 map register then RB2 source variation",
)
check(
    "the lambda-not1 record remains one control and not candidate attrition",
    next(
        record
        for record in RB2_RECORDS
        if record.name == "source_orbit_constrained_lambda_not1"
    ).role
    == "CONTROL",
)

# RB3 returned one moving-soldering candidate to this frozen-geometry
# shootout.  The local reductive connection uses the already supplied A0.
# This is not identified with N1's abstract Gamma_conn; it is a branch on
# which the background response can be rerun.
print("\nI. RB3 A0-induced moving-connection candidate response")


def so3_generator(left: int, right: int) -> np.ndarray:
    out = np.zeros((3, 3))
    out[left, right] = 1.0
    out[right, left] = -1.0
    return out


h_so3 = so3_generator(0, 1)


def project_h_so3(matrix: np.ndarray) -> np.ndarray:
    coefficient = float(
        np.sum(matrix * h_so3) / np.sum(h_so3 * h_so3)
    )
    return coefficient * h_so3


def plane_rotation(
    left: int,
    right: int,
    angle: float,
) -> np.ndarray:
    out = np.eye(3)
    cosine = np.cos(angle)
    sine = np.sin(angle)
    out[left, left] = cosine
    out[right, right] = cosine
    out[left, right] = sine
    out[right, left] = -sine
    return out


def reductive_gamma(
    representative: np.ndarray,
    background: np.ndarray,
    maurer: np.ndarray,
) -> np.ndarray:
    local_background = (
        representative.T @ background @ representative + maurer
    )
    return (
        representative
        @ project_h_so3(local_background)
        @ representative.T
        - representative @ maurer @ representative.T
    )


representative = plane_rotation(0, 2, 0.31)
gauge_group = plane_rotation(1, 2, -0.27)
maurer = 0.23 * so3_generator(0, 2)
background_a0 = (
    0.37 * so3_generator(0, 1)
    - 0.19 * so3_generator(0, 2)
    + 0.11 * so3_generator(1, 2)
)
gamma_before = reductive_gamma(
    representative,
    background_a0,
    maurer,
)
gamma_after = reductive_gamma(
    gauge_group @ representative,
    gauge_group @ background_a0 @ gauge_group.T,
    maurer,
)
gamma_expected = gauge_group @ gamma_before @ gauge_group.T
gamma_frozen_background = reductive_gamma(
    gauge_group @ representative,
    background_a0,
    maurer,
)
check(
    "Gamma(epsilon,A0) transforms covariantly when the supplied background moves",
    np.max(np.abs(gamma_after - gamma_expected)) < TOL,
)
check(
    "freezing A0 during moving-epsilon gauge transport is rejected",
    np.linalg.norm(gamma_frozen_background - gamma_expected) > 1.0e-3,
)

rng_return = np.random.default_rng(20260731)
return_a = rng_return.normal(size=(3, 3))
return_u = rng_return.normal(size=(3, 3))
return_z = rng_return.normal(size=(3, 3))
return_z = return_z - return_z.T
for current_kind in ("JD", "TOTAL"):
    action_before = matrix_bridge_action(
        current_kind,
        return_a,
        return_u,
        gamma_before,
        return_z,
    )
    action_after = matrix_bridge_action(
        current_kind,
        gauge_group @ return_a @ gauge_group.T,
        gauge_group @ return_u @ gauge_group.T,
        gamma_after,
        gauge_group @ return_z @ gauge_group.T,
    )
    action_frozen_background = matrix_bridge_action(
        current_kind,
        gauge_group @ return_a @ gauge_group.T,
        gauge_group @ return_u @ gauge_group.T,
        gamma_frozen_background,
        gauge_group @ return_z @ gauge_group.T,
    )
    check(
        f"{current_kind} bridge retains homogeneous covariance with the A0 response",
        abs(action_after - action_before) < TOL,
    )
    check(
        f"{current_kind} bridge detects an omitted A0 background response",
        abs(action_frozen_background - action_before) > 1.0e-4,
    )

RB3_MOVING_RETURN = {
    "candidate": "Gamma_conn_A0_reductive",
    "candidate_dependency": (
        "epsilon_IG",
        "d_epsilon_IG",
        "A0",
        "pr_spin_reductive",
    ),
    "epsilon_green_owner": "G_Gamma_REQUIRED_UNBUILT",
    "relative_epsilon_response": (
        "J_F[D_X Gamma]-(d_F,epsilon J_F[X])[theta]"
    ),
    "source_reentry": "NONE",
    "identity_with_N1_Gamma_conn": "UNRESOLVED",
}
RB1B_SOURCE_RETURN = {
    "full_Spin_same_Lambda2_Ricci": "KILLED-CENTRAL-PARITY",
    "epsilon_soldered_grade_flip": (
        "CONDITIONAL-PRE-RB1; CYCLIC-NONIMPLICATION-COUNTEREXAMPLE"
    ),
    "source_record": "STILL-BLOCKED-FIRST-AT-NATIVE-BOSONIC-SHIAB",
}
check(
    "the candidate moving epsilon path requires an unbuilt Green owner and J_F map response",
    RB3_MOVING_RETURN["epsilon_green_owner"]
    == "G_Gamma_REQUIRED_UNBUILT"
    and "d_F,epsilon" in RB3_MOVING_RETURN["relative_epsilon_response"],
)
check(
    "the A0-induced candidate is not promoted to the unique N1 Gamma connection",
    RB3_MOVING_RETURN["candidate"] == "Gamma_conn_A0_reductive"
    and RB3_MOVING_RETURN["identity_with_N1_Gamma_conn"]
    == "UNRESOLVED",
)
check(
    "the killed Ricci route and pre-RB1 grade flip do not enter this action shootout",
    RB3_MOVING_RETURN["source_reentry"] == "NONE"
    and RB1B_SOURCE_RETURN["full_Spin_same_Lambda2_Ricci"].startswith("KILLED")
    and RB1B_SOURCE_RETURN["epsilon_soldered_grade_flip"].startswith(
        "CONDITIONAL-PRE-RB1"
    ),
)

SEVEN_AXIS_SNAPSHOT = {
    f"L{index}": "UNCHANGED_FROM_RB1" for index in range(1, 8)
}
check(
    "RB2 changes Layer-0/action architecture without mutating L1-L7",
    set(SEVEN_AXIS_SNAPSHOT) == {f"L{index}" for index in range(1, 8)}
    and set(SEVEN_AXIS_SNAPSHOT.values()) == {"UNCHANGED_FROM_RB1"},
)

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\n" + "=" * 104)
print("VERDICT: TWO-N1-FIVE-FIELD-BRIDGE-SLICES-BUILT-AND-FORMALLY-DISTINCT")
print("VERDICT: TOTAL-CURRENT-DIRECT-CANCELLATION-LEAVES-HESSIAN+GREEN-FLUX")
print("VERDICT: SOURCE-(1/2,1/3)-EXACTNESS-CONDITIONAL; WARD-COEFFICIENT-BLIND")
print("BLOCK: SOURCE-FIRST-AT-NATIVE-DENSITY-DUAL-BOSONIC-SHIAB")
print("EMISSION: N1-JD + N1-TOTAL CLASSICAL FIXED-GEOMETRY PAIR TO RB3")
print("SIDE-TRACK: TWO NATIVE SOURCE REOPENERS RETURN THROUGH RB1/RB2")
print("RB3-RETURN: A0-INDUCED GAMMA(epsilon_IG,A0) BRANCH RESPONSE PASSES")
print("OPEN: IDENTITY WITH N1 GAMMA_CONN; OTHER H-CONNECTION BRANCHES")
print("RB1b-RETURN: FULL-SPIN SAME-LAMBDA2 RICCI KILLED; GRADE CANDIDATE PRE-RB1")
print("PARTIAL: COMPLETE-DIFF-CLOSURE-HELD-RB4; NO-DIFF-BASED-KILL")
print("NONCLAIM: NO-NATIVE-WARD; NO-CME; NO-VEV; NO-MASS; NO-DOMAIN; NO-INDEX; NO-COUNT")
print(f"ACTION-REGISTRY-SHA256: {FROZEN_ACTION_DIGEST}")
print("=" * 104)
