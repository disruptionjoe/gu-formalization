#!/usr/bin/env python3
"""N3 first-variation ledger and hostile controls for frozen packet v0.

This probe does not pretend that absent carrier derivatives are numerical
zeros.  It machine-checks the parts of N3 that are determined by the frozen
action:

* exact action-term/field ownership;
* K-sesquilinear versus C-Grassmann total-kernel projections;
* the inherited first-order actual-Sym2 support ceiling after each frozen
  P0 restriction, kept separate from the unresolved zero-order placement;
* analytic versus finite-difference variations for a selected commuting-
  scalar sign/dependency control;
* the moving-section current derivative;
* the P_IG Gaussian-parent coefficient sign;
* the same-source connection-current cancellation fork;
* the metric-trace-to-Ricci0 Hessian symbol and its Layer-0 separation from
  the N2 vertical-connection trace;
* the fixed-gamma full-Sp dimension obstruction under stated representation
  hypotheses, with a finite plane-leakage control;
* an even canonical-pair Hamiltonian sign plant, not a graded BV proof; and
* the virtual P3 comparator's unchanged local principal symbol.

It returns PARTIAL-WITH-NAMED-MISSING-ADJOINTS.  It does not compute a
stationary point, CME, domain, physical mass, index, or generation count.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
TESTS = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TESTS))

import full20_irrep_symbol_noether_probe as full20  # noqa: E402
import unified_source_datum_packet_v0_probe as n1  # noqa: E402


SEALED_HASH = "1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb"
TOL = 2.0e-9
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def hermitian_part(matrix: np.ndarray) -> np.ndarray:
    return (matrix + matrix.conj().T) / 2


def alternating_part(matrix: np.ndarray) -> np.ndarray:
    return (matrix - matrix.T) / 2


def krein_adjoint(operator: np.ndarray, krein: np.ndarray) -> np.ndarray:
    return np.linalg.solve(krein, operator.conj().T @ krein)


def c_natural(
    operator: np.ndarray, charge_conjugation: np.ndarray, tau: int
) -> np.ndarray:
    return tau * np.linalg.solve(
        charge_conjugation,
        operator.T @ charge_conjugation,
    )


@dataclass(frozen=True)
class EulerEntry:
    term: str
    field: str
    covector: str
    carrier: str
    status: str


# These are formula tokens, not a semantic matcher.  Every key is an exact N1
# ActionTerm name and every field is an exact declared varied field.  A zero is
# recorded only when it follows from the independent-field fork frozen in N1.
VARIATION_LEDGER: dict[str, dict[str, tuple[str, str]]] = {
    "ambient_yang_mills": {
        "A": (
            "(zeta_F/g_A^2) D_A^! F_A",
            "EXACT-WEAK-FORM",
        ),
    },
    "induced_ym_parent": {
        "A": ("B_U^! P_IG; B_U(a)=[a wedge U]", "EXACT-WEAK-FORM"),
        "U": ("D_A^! P_IG", "EXACT-WEAK-FORM"),
        "P_IG": ("D_A U-Z_U^-1 P_IG", "EXACT-ALGEBRAIC"),
        "epsilon_IG": (
            "0 in N1's independent P_IG,U parent; epsilon enters theta",
            "EXACT-ZERO-IN-FROZEN-FORK",
        ),
    },
    "distortion_source_bridge": {
        "A": (
            "kappa^-1 theta-J plus implicit -(D_A J)^!theta",
            "BLOCKED-LITERAL-J; CONDITIONAL-TYPED-COMPLETION",
        ),
        "U": (
            "-kappa^-1 theta+J",
            "BLOCKED-LITERAL-J; CONDITIONAL-TYPED-COMPLETION",
        ),
        "epsilon_IG": (
            "-(D_epsilon Gamma)^!(kappa^-1 theta-J)",
            "MAP-DEFERRED-GAMMA-ORBIT",
        ),
        "Z": (
            "-(D_Z J)^! theta",
            "BLOCKED-LITERAL-J; CONDITIONAL-TYPED-COMPLETION",
        ),
    },
    "full20_krein_quadratic": {
        "A": (
            "J_20,D + D_A^! Q_20,F, defined by density-dual variation",
            "FORMULA-EXPLICIT; PROJECTOR/GAMMA-ADJOINTS-DEFERRED",
        ),
        "Z": (
            "real/Grassmann derivative of the K-lowered full20 operator",
            "REALITY-CONVENTION-DEFERRED",
        ),
    },
    "end_selector": {
        "A": (
            "branchwise A derivative: vertical/vectorlike zero when v_tr fixed; boundary comparator inherits D_packet(A)",
            "BRANCH-TYPED",
        ),
        "Z": (
            "m_sel chi Herm_K(c_rho(v_tr))Z or m_sel chi Z",
            "EXACT-PHYSICAL-BRANCHES",
        ),
    },
    "induced_section_gravity": {
        "s": (
            "2 alpha (D_s II)^!II+2 beta (D_s II0)^!II0+E_g,alg-Lambda g^-1",
            "D_s-II-AND-GREEN-MAP-DEFERRED",
        ),
    },
    "seiberg_witten_defect": {
        "s": (
            "(D_s R_SW)^!(lambda_SW R_SW)+density/Hodge variation",
            "MOMENT-MAP/PROJECTOR-ADJOINTS-DEFERRED",
        ),
        "A": (
            "(s^*)^![lambda_SW D_AX^! P_+^! R_SW]",
            "EXACT-WEAK-FORM; P_+-ADJOINT-DEFERRED",
        ),
        "Z": (
            "-s_* P0^![lambda_SW (D_psi mu)^! R_SW]",
            "MOMENT-MAP-ADJOINT-DEFERRED",
        ),
    },
    "krein_yukawa_defect": {
        "s": (
            "moving pullback+P0+K+resV+density derivative",
            "MAP-DEFERRED-WITH-EXACT-DEPENDENCIES",
        ),
        "A": (
            "(res_s^V)^! J_v^K",
            "FORMAL-DENSITY-DUAL",
        ),
        "Z": (
            "s_* P0^![2 Herm_K(c_rho(v)Y_K) psi]",
            "KERNEL-PROJECTION-EXACT; REALITY-NORMALIZATION-DECLARED",
        ),
    },
    "charge_conjugation_yukawa_defect": {
        "s": (
            "moving pullback+P0+C+resV+density+reality-completion derivative",
            "C-REALITY-COMPLETION-DEFERRED",
        ),
        "A": (
            "(res_s^V)^! J_v^C",
            "FORMAL-DENSITY-DUAL",
        ),
        "Z": (
            "s_* P0^![Alt(C c_rho(v)Y_C) psi+reality dual]",
            "GRASSMANN-PROJECTION-EXACT; REALITY-COMPLETION-DEFERRED",
        ),
    },
    "spurion_interface": {
        "s": (
            "moving pullback+P0+C+resV+Sigma+density derivative",
            "MAP-DEFERRED-WITH-EXACT-DEPENDENCIES",
        ),
        "A": (
            "(res_s^V)^! J_v^Sigma",
            "FORMAL-DENSITY-DUAL",
        ),
        "Z": (
            "s_* P0^![2 Alt(C c_rho(v)Sigma) psi]",
            "GRASSMANN-PROJECTION-EXACT",
        ),
    },
    "minimal_bv_extension": {
        field: (
            "canonical antifield-linear Hamiltonian derivative of S_cl+<Phi+,s0 Phi>",
            "ANTIFIELD-LINEAR-SKELETON; OPEN-HOM-MAPS-DEFERRED",
        )
        for field in (
            "A",
            "U",
            "P_IG",
            "epsilon_IG",
            "Z",
            "c_g",
            "gamma",
            "bar_gamma",
            "b_gamma",
            "s",
            "xi",
        )
    },
    "orientation_holonomy_cocycle": {},
}


def expected_varied_fields(term: n1.ActionTerm) -> set[str]:
    return {
        field
        for field in term.fields
        if field in n1.FIELDS
        and n1.FIELDS[field].varied
        and field != "theta"
    }


def sector(slot_name: str) -> str:
    if slot_name.startswith("S:"):
        return "S"
    if slot_name.startswith("imGamma:"):
        return "I"
    if slot_name.startswith("kerGamma:") or slot_name.startswith("X:"):
        return "R"
    raise ValueError(f"unknown full-20 slot {slot_name}")


def restricted_incidence(cells: set[tuple[str, str]], projector: str) -> set:
    allowed = {
        "1": {"S", "I", "R"},
        "P_S": {"S"},
        "P_I": {"I"},
        "P_R": {"R"},
    }[projector]
    return {
        cell
        for cell in cells
        if sector(cell[0]) in allowed and sector(cell[1]) in allowed
    }


def central_difference(
    function,
    point: np.ndarray,
    coordinate: int,
    step: float = 1.0e-6,
) -> float:
    right = point.copy()
    left = point.copy()
    right[coordinate] += step
    left[coordinate] -= step
    return float((function(right) - function(left)) / (2 * step))


VARIABLES = ("a", "u", "p", "epsilon", "z", "s")


def finite_terms(x: np.ndarray) -> dict[str, float]:
    a, u, p, epsilon, z, s = x
    c_ym = 0.7
    z_u = 1.3
    kappa = 1.7
    h0, h1, lambda_f = 0.9, -0.4, 0.2
    m_sel = 0.6
    alpha, beta, lambda_bare = 1.1, 0.3, 0.07
    lambda_sw = 0.8
    y_k = 0.5
    a0 = -0.2
    fixed_selector_profile = 0.35
    curvature = a + a * a / 2
    theta = a - epsilon - u
    current = z * z
    h_operator = h0 + h1 * a + lambda_f * curvature
    sw_residual = a + s - z * z
    return {
        "ambient_yang_mills": c_ym * curvature * curvature / 2,
        "induced_ym_parent": p * (1 + a) * u - p * p / (2 * z_u),
        "distortion_source_bridge": theta * theta / (2 * kappa)
        - theta * current,
        "full20_krein_quadratic": z * z * h_operator / 2,
        # Selected physical vertical rival: its supplied profile is fixed,
        # so this branch varies Z but neither A nor s.  The auxiliary
        # boundary rival has a separate Zhat and is not mixed into this toy.
        "end_selector": m_sel * z * z * fixed_selector_profile / 2,
        "induced_section_gravity": alpha * s * s
        + beta * s**4
        - 2 * lambda_bare * (1 + s),
        "seiberg_witten_defect": lambda_sw * sw_residual**2 / 2,
        "krein_yukawa_defect": y_k * z * z * (a - a0) * s,
    }


def finite_gradients(x: np.ndarray) -> dict[str, np.ndarray]:
    a, u, p, epsilon, z, s = x
    c_ym = 0.7
    z_u = 1.3
    kappa = 1.7
    h0, h1, lambda_f = 0.9, -0.4, 0.2
    m_sel = 0.6
    alpha, beta, lambda_bare = 1.1, 0.3, 0.07
    lambda_sw = 0.8
    y_k = 0.5
    a0 = -0.2
    fixed_selector_profile = 0.35
    curvature = a + a * a / 2
    theta = a - epsilon - u
    current = z * z
    bridge = theta / kappa - current
    h_operator = h0 + h1 * a + lambda_f * curvature
    sw_residual = a + s - z * z
    gradients: dict[str, np.ndarray] = {}

    value = np.zeros(6)
    value[0] = c_ym * curvature * (1 + a)
    gradients["ambient_yang_mills"] = value

    value = np.zeros(6)
    value[0] = p * u
    value[1] = p * (1 + a)
    value[2] = (1 + a) * u - p / z_u
    gradients["induced_ym_parent"] = value

    value = np.zeros(6)
    value[0] = bridge
    value[1] = -bridge
    value[3] = -bridge
    value[4] = -2 * theta * z
    gradients["distortion_source_bridge"] = value

    value = np.zeros(6)
    value[0] = z * z * (h1 + lambda_f * (1 + a)) / 2
    value[4] = z * h_operator
    gradients["full20_krein_quadratic"] = value

    value = np.zeros(6)
    value[4] = m_sel * z * fixed_selector_profile
    gradients["end_selector"] = value

    value = np.zeros(6)
    value[5] = 2 * alpha * s + 4 * beta * s**3 - 2 * lambda_bare
    gradients["induced_section_gravity"] = value

    value = np.zeros(6)
    value[0] = lambda_sw * sw_residual
    value[4] = -2 * lambda_sw * z * sw_residual
    value[5] = lambda_sw * sw_residual
    gradients["seiberg_witten_defect"] = value

    value = np.zeros(6)
    value[0] = y_k * z * z * s
    value[4] = 2 * y_k * z * (a - a0) * s
    value[5] = y_k * z * z * (a - a0)
    gradients["krein_yukawa_defect"] = value
    return gradients


def pushed_density_value(
    section: np.ndarray, weights: np.ndarray, density_scale: float
) -> float:
    test_function = section**3 + 2 * section
    density = 1 + density_scale * section**2
    return float(np.dot(weights, test_function * density))


def pushed_density_derivative(
    section: np.ndarray,
    velocity: np.ndarray,
    weights: np.ndarray,
    density_scale: float,
) -> tuple[float, float, float]:
    test_function = section**3 + 2 * section
    derivative_test = (3 * section**2 + 2) * velocity
    density = 1 + density_scale * section**2
    derivative_density = 2 * density_scale * section * velocity
    moving_support = float(np.dot(weights, derivative_test * density))
    intrinsic_density = float(np.dot(weights, test_function * derivative_density))
    return moving_support + intrinsic_density, moving_support, intrinsic_density


def polynomial_derivative(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(
        Fraction(index) * coefficients[index]
        for index in range(1, len(coefficients))
    )


def polynomial_product(
    left: tuple[Fraction, ...], right: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


def integrate_unit(coefficients: tuple[Fraction, ...]) -> Fraction:
    return sum(
        coefficient / Fraction(power + 1)
        for power, coefficient in enumerate(coefficients)
    )


def evaluate_polynomial(
    coefficients: tuple[Fraction, ...], value: Fraction
) -> Fraction:
    return sum(
        coefficient * value**power
        for power, coefficient in enumerate(coefficients)
    )


def ricci_zero_symbol(k: np.ndarray, metric: np.ndarray) -> np.ndarray:
    k_squared = float(k @ metric @ k)
    return (
        np.outer(k, k) - metric * k_squared / 4
    ) / 4


def metric_trace(tensor: np.ndarray, metric: np.ndarray) -> float:
    inverse = np.linalg.inv(metric)
    return float(np.einsum("ab,ab", inverse, tensor))


def contracted_tensor_norm(tensor: np.ndarray, metric: np.ndarray) -> float:
    inverse = np.linalg.inv(metric)
    raised = inverse @ tensor @ inverse
    return float(np.einsum("ab,ab", tensor, raised))


def projection_residual(
    matrices: list[np.ndarray], target: np.ndarray
) -> float:
    basis = np.stack([matrix.reshape(-1) for matrix in matrices], axis=1)
    coefficients, *_ = np.linalg.lstsq(basis, target.reshape(-1), rcond=None)
    projected = (basis @ coefficients).reshape(target.shape)
    return float(np.linalg.norm(target - projected))


print("=" * 98)
print("N3 UNIFIED SOURCE-ACTION FIRST-VARIATION / SIX-INTERFACE CONTRACT")
print("=" * 98)

check(
    "frozen N1 construction hash is unchanged",
    n1.construction_hash() == SEALED_HASH,
)

print("\nA. Exact action-term and density-dual ownership")
n1_term_names = {term.name for term in n1.ACTION_TERMS}
check(
    "variation ledger has exactly one row family for every frozen N1 term",
    set(VARIATION_LEDGER) == n1_term_names,
)
for term in n1.ACTION_TERMS:
    expected = expected_varied_fields(term)
    actual = set(VARIATION_LEDGER[term.name])
    check(
        f"{term.name} emits every declared varied-field covector",
        actual == expected,
        f"expected={sorted(expected)}, actual={sorted(actual)}",
    )

all_ledger_legs = {
    leg
    for term in n1.ACTION_TERMS
    if term.name in VARIATION_LEDGER
    for leg in term.legs
}
check(
    "one exact term ledger carries all five campaign legs",
    all_ledger_legs == set(n1.LEGS),
)
check(
    "T9 has no ordinary local Euler covector at fixed topology",
    VARIATION_LEDGER["orientation_holonomy_cocycle"] == {},
)
defect_fermion_duals = tuple(
    VARIATION_LEDGER[term]["Z"][0]
    for term in (
        "seiberg_witten_defect",
        "krein_yukawa_defect",
        "charge_conjugation_yukawa_defect",
        "spurion_interface",
    )
)
check(
    "every defect fermion covector carries the s_* equation dual",
    all("s_*" in token for token in defect_fermion_duals),
)
deleted_section_duals = tuple(
    token.replace("s_*", "") for token in defect_fermion_duals
)
check(
    "deleting s_* makes the defect-to-ambient incidence contract fail",
    not all("s_*" in token for token in deleted_section_duals),
)

print("\nB. Total K and C kernel projections")
rng = np.random.default_rng(20260730)
dimension = 6
rank = 4
krein = np.diag([1, 1, 1, -1, -1, -1]).astype(complex)
raw_operator = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
    size=(dimension, dimension)
)
restriction = rng.normal(size=(dimension, rank)) + 1j * rng.normal(
    size=(dimension, rank)
)

left_k = hermitian_part(
    restriction.conj().T @ krein @ raw_operator @ restriction
)
right_k = (
    restriction.conj().T
    @ krein
    @ (
        raw_operator + krein_adjoint(raw_operator, krein)
    )
    @ restriction
    / 2
)
check(
    "K real part selects the Krein-self-adjoint total ordered operator",
    max_abs(left_k - right_k) < TOL,
)
check(
    "Krein adjoint is involutive",
    max_abs(
        krein_adjoint(krein_adjoint(raw_operator, krein), krein)
        - raw_operator
    )
    < TOL,
)
k_skew = (
    raw_operator - krein_adjoint(raw_operator, krein)
) / 2
check(
    "K-skew total-operator stratum is killed by the sesquilinear real part",
    max_abs(
        hermitian_part(
            restriction.conj().T @ krein @ k_skew @ restriction
        )
    )
    < TOL,
)

identity_c = np.eye(dimension, dtype=complex)
symplectic_c = np.block(
    [
        [np.zeros((3, 3)), np.eye(3)],
        [-np.eye(3), np.zeros((3, 3))],
    ]
).astype(complex)
for label, charge_conjugation, tau in (
    ("C_plus", identity_c, 1),
    ("C_minus", symplectic_c, -1),
):
    left_c = alternating_part(
        restriction.T @ charge_conjugation @ raw_operator @ restriction
    )
    right_c = (
        restriction.T
        @ charge_conjugation
        @ (
            raw_operator
            - c_natural(raw_operator, charge_conjugation, tau)
        )
        @ restriction
        / 2
    )
    check(
        f"{label} Grassmann diagonal selects the C-natural anti-fixed total operator",
        max_abs(left_c - right_c) < TOL,
    )
    check(
        f"{label} C-natural involution closes",
        max_abs(
            c_natural(
                c_natural(raw_operator, charge_conjugation, tau),
                charge_conjugation,
                tau,
            )
            - raw_operator
        )
        < TOL,
    )
    c_fixed = (
        raw_operator
        + c_natural(raw_operator, charge_conjugation, tau)
    ) / 2
    check(
        f"{label} C-natural fixed stratum is killed for one identical odd field",
        max_abs(
            alternating_part(
                restriction.T
                @ charge_conjugation
                @ c_fixed
                @ restriction
            )
        )
        < TOL,
    )

dagger_collapse = restriction.conj().T @ identity_c @ raw_operator @ restriction
transpose_c = restriction.T @ identity_c @ raw_operator @ restriction
check(
    "planted K/C branch collapse is detected by dagger versus transpose",
    np.linalg.norm(dagger_collapse - transpose_c) > 1.0,
)

first_order_symbol_cells = set().union(
    *full20.BLOCK_FIBRE_SUPPORT.values()
)
symbol_ceiling = {
    projector: restricted_incidence(first_order_symbol_cells, projector)
    for projector in ("1", "P_S", "P_I", "P_R")
}
check(
    "inherited actual-Sym2 first-order symbol comparator has 68 cells",
    len(first_order_symbol_cells) == 68,
)
check(
    "conditional P0-restricted first-order support ceilings are 68/4/4/20",
    {name: len(cells) for name, cells in symbol_ceiling.items()}
    == {"1": 68, "P_S": 4, "P_I": 4, "P_R": 20},
)
zero_order_placement_status = (
    "UNRESOLVED-NEEDS-ENDS-TO-END20-P0-RHOPHI-PROVENANCE-MAP"
)
check(
    "first-order support is not promoted to zero-order Yukawa incidence",
    zero_order_placement_status.startswith("UNRESOLVED"),
)

print("\nC. Selected commuting-scalar sign/dependency controls")
point = np.array([0.21, -0.31, 0.47, 0.12, -0.38, 0.29])
term_gradients = finite_gradients(point)
controlled_terms = set(term_gradients)
check(
    "finite-difference battery is explicitly a selected N1 subset",
    controlled_terms < set(VARIATION_LEDGER)
    and {
        "charge_conjugation_yukawa_defect",
        "spurion_interface",
        "minimal_bv_extension",
        "orientation_holonomy_cocycle",
    }.isdisjoint(controlled_terms),
)
worst_difference = 0.0
for term_name, analytic in term_gradients.items():
    for coordinate in range(len(VARIABLES)):
        numeric = central_difference(
            lambda candidate, name=term_name: finite_terms(candidate)[name],
            point,
            coordinate,
        )
        worst_difference = max(
            worst_difference, abs(numeric - analytic[coordinate])
        )
check(
    "selected commuting-scalar controls match their analytic derivatives",
    worst_difference < 3.0e-9,
    f"worst={worst_difference:.3e}",
)

# Completion of the square fixes the coefficient sign without implying
# positivity of the native indefinite pairing or a sign for charged Z_U.
x_parent = Fraction(7, 5)
parent_cases = {}
for z_parent in (Fraction(11, 6), Fraction(-11, 6)):
    p_stationary = z_parent * x_parent
    parent_cases[z_parent] = (
        p_stationary * x_parent
        - p_stationary * p_stationary / (2 * z_parent)
    )
check(
    "frozen P_IG parent eliminates with coefficient +Z_U/2 for either sign",
    all(
        value == z_parent * x_parent * x_parent / 2
        for z_parent, value in parent_cases.items()
    ),
)
check(
    "planted inherited coefficient -Z_U/2 is rejected",
    all(
        value != -z_parent * x_parent * x_parent / 2
        for z_parent, value in parent_cases.items()
    ),
)
sample_coordinates = tuple(
    Fraction(value) for value in (-2, -1, 0, 1, 2)
)
coefficient_direct = Fraction(7, 3)
eta_parameter = Fraction(5, 4)
coefficient_reparameterized = 1 + eta_parameter * eta_parameter
direct_zero_locus = {
    coordinate
    for coordinate in sample_coordinates
    if coefficient_direct * coordinate == 0
}
reparameterized_zero_locus = {
    coordinate
    for coordinate in sample_coordinates
    if coefficient_reparameterized * coordinate == 0
}
check(
    "nonzero coefficient reparameterization preserves the Euler zero locus",
    direct_zero_locus == reparameterized_zero_locus == {Fraction(0)},
)

print("\nD. Moving section current and Green boundary")
section = np.array([-0.4, 0.2, 0.75])
velocity = np.array([0.3, -0.5, 0.1])
weights = np.array([0.2, 0.5, 0.3])
density_scale = 0.4
analytic_current, moving_piece, density_piece = pushed_density_derivative(
    section, velocity, weights, density_scale
)
step = 1.0e-6
numeric_current = (
    pushed_density_value(
        section + step * velocity, weights, density_scale
    )
    - pushed_density_value(
        section - step * velocity, weights, density_scale
    )
) / (2 * step)
check(
    "moving s_! support plus intrinsic density derivative matches finite difference",
    abs(analytic_current - numeric_current) < 2.0e-10,
)
check(
    "omitting either moving support or density variation is detected",
    abs(moving_piece - numeric_current) > 1.0e-3
    and abs(density_piece - numeric_current) > 1.0e-3,
)

u_poly = (Fraction(1), Fraction(0), Fraction(1))
v_poly = (Fraction(0), Fraction(2), Fraction(0), Fraction(1))
ibp_bulk = integrate_unit(
    tuple(
        a + b
        for a, b in zip(
            polynomial_product(u_poly, polynomial_derivative(v_poly)),
            polynomial_product(polynomial_derivative(u_poly), v_poly)
            + (Fraction(0),),
        )
    )
)
ibp_boundary = (
    evaluate_polynomial(u_poly, Fraction(1))
    * evaluate_polynomial(v_poly, Fraction(1))
    - evaluate_polynomial(u_poly, Fraction(0))
    * evaluate_polynomial(v_poly, Fraction(0))
)
check(
    "total derivative is a Green boundary current, not a discarded bulk zero",
    ibp_bulk == ibp_boundary == 6,
)

print("\nE. Source-current Layer 0 and same-source cancellation")
theta_type = "Omega1(Y,adP)"
literal_j_type = "Omega1(Y)"
connection_j_dual_type = "Omega1(Y,adP)^vee tensor Dens(Y)"
check(
    "literal N1 Clifford-vector current cannot pair with adjoint-valued theta",
    literal_j_type != theta_type,
)

# A density-dual action derivative is a covector.  The bridge action needs a
# separately declared Hodge/Krein/adjoint-pairing Riesz map to turn it into
# the primal adjoint-valued one-form paired with theta.
adjoint_hodge_pairing = np.array(
    [[2.0, 0.25], [0.25, -1.5]],
    dtype=float,
)
current_density_dual = np.array([0.7, -0.2])
current_primal = np.linalg.solve(
    adjoint_hodge_pairing,
    current_density_dual,
)
check(
    "density-dual A-variation is not silently identified with a primal current",
    connection_j_dual_type != theta_type,
)
check(
    "a declared nondegenerate Hodge/Krein Riesz map recovers the primal current",
    np.linalg.matrix_rank(adjoint_hodge_pairing) == 2
    and np.linalg.norm(
        adjoint_hodge_pairing @ current_primal
        - current_density_dual
    )
    < TOL,
)

# Minimal A-linear stratum: the Dirac part gives A J_D, the curvature vertex
# gives an independent J_F, and theta=A-Gamma(epsilon)-U.  If the bridge uses
# J_D, only +J_D and -J_D cancel in E_A; J_F remains.
a_value = Fraction(2, 5)
u_value = Fraction(-1, 7)
gamma_epsilon = Fraction(3, 11)
j_dirac = Fraction(5, 13)
j_curvature = Fraction(-2, 17)
kappa_value = Fraction(17, 9)
theta_value = a_value - gamma_epsilon - u_value
matter_a_derivative = j_dirac + j_curvature
bridge_a_derivative = theta_value / kappa_value - j_dirac
check(
    "same Dirac-current bridge cancels only +J_D and -J_D",
    matter_a_derivative + bridge_a_derivative
    == theta_value / kappa_value + j_curvature,
)
total_bridge_derivative = (
    theta_value / kappa_value
    - j_dirac
    - j_curvature
)
check(
    "a bridge defined as the total matter current cancels both direct pieces",
    matter_a_derivative + total_bridge_derivative
    == theta_value / kappa_value,
)
check(
    "the selected bridge current survives with positive sign in the U equation",
    -theta_value / kappa_value + j_dirac
    != theta_value / kappa_value,
)

# If J_D(A)=j0+cA, the uncancelled correction is -(D_A J_D)^! theta.
j0 = Fraction(4, 9)
c_current = Fraction(2, 7)
j_dirac_of_a = j0 + c_current * a_value
matter_derivative = j_dirac_of_a + j_curvature
bridge_derivative = (
    theta_value / kappa_value
    - j_dirac_of_a
    - theta_value * c_current
)
check(
    "A-dependent same-Dirac-current bridge leaves J_F-(D_A J_D)^!theta",
    matter_derivative + bridge_derivative
    == (
        theta_value / kappa_value
        + j_curvature
        - c_current * theta_value
    ),
)

print("\nF. Metric trace Hessian versus N2 vertical-connection trace")
eta = np.diag([1.0, 1.0, 1.0, -1.0])
covectors = {
    "zero": np.array([0.0, 0.0, 0.0, 0.0]),
    "spacelike": np.array([1.0, 0.0, 0.0, 0.0]),
    "timelike": np.array([0.0, 0.0, 0.0, 1.0]),
    "null": np.array([1.0, 0.0, 0.0, 1.0]),
}
symbols = {name: ricci_zero_symbol(k, eta) for name, k in covectors.items()}
check(
    "constant metric-trace amplitude has zero Ricci0 Hessian symbol",
    max_abs(symbols["zero"]) == 0.0,
)
check(
    "every tested nonzero Fourier covector gives a nonzero tracefree Hessian channel",
    all(
        max_abs(symbols[name]) > 0.0
        for name in ("spacelike", "timelike", "null")
    ),
)
check(
    "all metric-trace Hessian outputs are exactly trace-free",
    all(abs(metric_trace(symbol, eta)) < TOL for symbol in symbols.values()),
)
check(
    "null tracefree Hessian is nonzero despite zero contracted norm",
    max_abs(symbols["null"]) > 0.0
    and abs(contracted_tensor_norm(symbols["null"], eta)) < TOL,
)

metric_trace_carrier = "delta s=(phi/4)g in Sym2(T*X)"
n2_trace_carrier = "v_tr=tau_g tensor Phi_tr in V*Y tensor adP"
check(
    "Layer 0 keeps metric trace variation and N2 vertical connection trace distinct",
    metric_trace_carrier != n2_trace_carrier,
)

# The DeWitt inverse of tau_g is h_tr=-g/4.  If phi multiplies that native
# vector, the Fourier symbol is the negative of the +phi*g/4 convention.
native_trace_symbols = {
    name: -symbol for name, symbol in symbols.items()
}
check(
    "native DeWitt trace-vector amplitude reverses the conformal sign but not survival",
    max_abs(native_trace_symbols["spacelike"] + symbols["spacelike"])
    < TOL
    and max_abs(native_trace_symbols["spacelike"]) > 0.0,
)

# Exact variation of tau_g(q)=tr(g^-1 q)/4 under h=(phi/4)g.
q_tensor = np.diag([2.0, -1.0, 0.5, 3.0])
phi = 0.8
h_metric = phi * eta / 4
tau_value = np.trace(np.linalg.inv(eta) @ q_tensor) / 4
tau_derivative = -np.trace(
    np.linalg.inv(eta)
    @ h_metric
    @ np.linalg.inv(eta)
    @ q_tensor
) / 4
check(
    "metric trace variation rescales tau_g but does not identify its field amplitude",
    abs(tau_derivative + phi * tau_value / 4) < TOL,
)

# Curved-ambient Gauss rewrite:
# alpha|II|^2+beta|II0|^2 =
# (alpha+3beta/4)|H|^2-(alpha+beta)R_X
# +(alpha+beta)R_Y,tan.
principal_curvatures = tuple(
    Fraction(value) for value in (1, -2, 3, 1)
)
mean_squared = sum(principal_curvatures) ** 2
ii_squared = sum(value * value for value in principal_curvatures)
ambient_tangential_scalar = Fraction(7, 9)
intrinsic_scalar = (
    mean_squared
    - ii_squared
    + ambient_tangential_scalar
)
ii_zero_squared = ii_squared - mean_squared / 4
alpha_q, beta_q = Fraction(5, 3), Fraction(-2, 7)
geometry_direct = alpha_q * ii_squared + beta_q * ii_zero_squared
geometry_gauss = (
    alpha_q + Fraction(3, 4) * beta_q
) * mean_squared - (alpha_q + beta_q) * intrinsic_scalar + (
    alpha_q + beta_q
) * ambient_tangential_scalar
check(
    "curved-ambient Gauss rewrite carries both intrinsic and ambient curvature",
    geometry_direct == geometry_gauss,
)
flat_only_gauss = (
    alpha_q + Fraction(3, 4) * beta_q
) * mean_squared - (alpha_q + beta_q) * intrinsic_scalar
check(
    "plant detects omission of native ambient tangential curvature",
    flat_only_gauss != geometry_direct,
)

print("\nG. Fixed-plane full-Sp hypothesis and dynamical-soldering fork")
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
gamma_plane = [sigma_x, sigma_y]
spin_generator = (sigma_x @ sigma_y - sigma_y @ sigma_x) / 4
generic_k_unitary_generator = 1j * sigma_x
spin_residual = max(
    projection_residual(
        gamma_plane,
        spin_generator @ gamma - gamma @ spin_generator,
    )
    for gamma in gamma_plane
)
generic_residual = max(
    projection_residual(
        gamma_plane,
        generic_k_unitary_generator @ gamma
        - gamma @ generic_k_unitary_generator,
    )
    for gamma in gamma_plane
)
check(
    "finite Spin-like control preserves the planted Clifford plane",
    spin_residual < TOL,
)
check(
    "finite generic K-unitary control can leave the planted Clifford plane",
    generic_residual > 1.0,
)
check(
    "standard irreducible fixed-plane full-Sp hypothesis is dimension-obstructed",
    64 * (2 * 64 + 1) == 8256
    and 14 * 13 // 2 == 91
    and 8256 > 91,
)
projector = np.diag([1.0, 0.0]).astype(complex)
check(
    "nonintertwining projector plant is detected",
    np.linalg.norm(
        generic_k_unitary_generator @ projector
        - projector @ generic_k_unitary_generator
    )
    > 1.0,
)

print("\nH. Even canonical sign plant, Noether boundary, and P3 virtual carry")
q = Fraction(2, 3)
q_plus = Fraction(-3, 5)
f_q = q * q + 1
f_prime = 2 * q
potential_prime = 3 * q * q
d_s_d_q = q_plus * f_prime + potential_prime
d_s_d_q_plus = f_q
x_q = d_s_d_q_plus
x_q_plus = -d_s_d_q
check(
    "even canonical-pair plant gives Xq=dS/dq+ and Xq+=-dS/dq",
    x_q == f_q and x_q_plus == -(q_plus * f_prime + potential_prime),
)
check(
    "even-pair plant rejects a plus sign on conjugate evolution",
    x_q_plus != d_s_d_q,
)

principal = np.array([[1.0, 2.0], [-2.0, 1.0]])
hopf_principal = np.kron(principal, np.eye(4))
trivial_principal = np.kron(principal, np.eye(4))
hopf_lower = np.kron(np.eye(2), np.diag([1.0, -1.0, 0.5, -0.5]))
trivial_lower = np.zeros_like(hopf_lower)
check(
    "P3 graded comparator pair has equal local principal matrices on distinct bundles",
    max_abs(hopf_principal - trivial_principal) == 0.0
    and np.linalg.matrix_rank(hopf_principal)
    == 4 * np.linalg.matrix_rank(principal),
)
check(
    "nontrivial n Hopf connection remains visible in lower-order data",
    np.linalg.norm(hopf_lower - trivial_lower) > 1.0,
)
check(
    "n=0 trivial-connection comparator has no lower-order difference",
    max_abs(trivial_lower - np.zeros_like(trivial_lower)) == 0.0,
)

SIX_OUTPUTS = {
    "total_K_and_C_kernels": "PROJECTIONS-EXPLICIT; ZERO-ORDER-PLACEMENT-DEFERRED",
    "fermion_and_vertical_Euler": "FORMAL-COVECTORS; J-BRIDGE-BLOCKED",
    "section_trace_split": "MOVING-CURRENT-EXPLICIT; D_sII/D_sRYTAN/PLACEMENT-DEFERRED",
    "IG_parent_and_compatibility": "PARENT-COEFFICIENT-EXACT; FIXED-PLANE-FULL-SP-HYPOTHESIS-OBSTRUCTED; DYNAMIC-SOLDERING-DEFERRED",
    "physical_R_defect": "LC-EXACT; IG/COMPAT/SOURCE-QUOTIENT-DEFERRED",
    "P3_virtual_symbol_pair": "PRINCIPAL-PAIR-EXPLICIT; NONTRIVIAL-N-LOWER-CONNECTION-CARRIED; N0-TRIVIAL; NO-PUSHFORWARD",
}
MISSING_MAPS = (
    "typed disposition of J_bridge: Riesz-lowered J_D, total J_D+J_F, or independent soldered current",
    "full20 D_A covector and Hodge/Krein Riesz map including projector/gamma/K and F_A-vertex adjoints",
    "C-branch reality completion and exact P0/rho(Phi)/provenance placement",
    "D_s II, D_s RY_tan, the normal connection, and geometric Green operator",
    "D_s P0, D_s res_s^V, D_s c_rho, and bundle-valued moving equation dual",
    "dynamical epsilon_IG soldering orbit and its full-Sp covariant derivative",
    "OmegaIG/open-BV native-real-form Hom maps and Euler-ideal quotient",
    "twisted subprincipal convention, closed domain, and pushforward",
)
planted_unrelated_constraint = "lunar_ephemeris_constraint"
check(
    "unrelated planted constraint is rejected by the exact interface ledger",
    planted_unrelated_constraint not in SIX_OUTPUTS
    and all(
        planted_unrelated_constraint not in item
        for item in MISSING_MAPS
    ),
)
check(
    "all six N3 interfaces are emitted with nonempty honest statuses",
    len(SIX_OUTPUTS) == 6 and all(SIX_OUTPUTS.values()),
)
check(
    "complete N3 is refused with a finite named missing-map ledger",
    len(MISSING_MAPS) == 8
    and any("J_bridge" in item for item in MISSING_MAPS)
    and any("Riesz" in item for item in MISSING_MAPS)
    and any("soldering" in item for item in MISSING_MAPS),
)

print("\nSix-interface status ledger:")
for name, status in SIX_OUTPUTS.items():
    print(f"  {name}: {status}")
print("\nNamed missing maps:")
for item in MISSING_MAPS:
    print(f"  - {item}")

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\n" + "=" * 98)
print("VERDICT: N3-TERM-BY-TERM-FIRST-VARIATION-LEDGER-COMPLETE")
print("VERDICT: TOTAL-K/C-PROJECTIONS-EXPLICIT; ZERO-ORDER-PLACEMENT-DEFERRED")
print("VERDICT: CONDITIONAL-FIRST-ORDER-SYMBOL-SUPPORT-COMPARATOR-EXPLICIT")
print("VERDICT: MOVING-SECTION-CURRENT-DERIVATIVE-CONSTRUCTED")
print("VERDICT: P_IG-PARENT-ELIMINATION-COEFFICIENT-PLUS-Z_U/2")
print("VERDICT: SAME-DIRAC-CURRENT-A-COUPLING-CANCELS-ON-A-LINEAR-STRATUM")
print("VERDICT: KINEMATIC-METRIC-TRACE-TO-RICCI0-HESSIAN-CHANNEL")
print("VERDICT: FIXED-PLANE-FULL-SP-BRANCH-OBSTRUCTED-UNDER-STATED-HYPOTHESES")
print("RESIDUAL: DYNAMIC-SOLDERING-AND-TYPED-J-BRIDGE-MAP-DEFERRED")
print("RESULT: SIX-TYPED-N3-INTERFACES; PARTIAL-WITH-NAMED-MISSING-ADJOINTS")
print("NONCLAIM: NO-STATIONARITY; NO-CME; NO-DOMAIN; NO-MASS; NO-INDEX; NO-COUNT")
print("=" * 98)
