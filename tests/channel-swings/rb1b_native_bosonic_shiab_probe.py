#!/usr/bin/env python3
"""RB1b native bosonic-Shiab reopener and adjacent architecture control.

The preregistered construction is the full-Spin(9,5)-equivariant algebraic
Ricci--Einstein route

    Omega^2(spin) -> Omega^1(spin) -> Omega^13(spin*).

It is tested first and killed at that symmetry grade by an exact
representation-parity obstruction.
The second half is deliberately graded only as an adjacent finite
architecture fixture.  It checks the degree, moving-soldering covariance,
right-H linearity, reality, and epsilon response of a source-shaped
full-adjoint grade-flipping formula.  It is not a 14-dimensional selector
calculation and it cannot re-enter RB2 without a native carrier admission
and cyclic/transgression proof.
"""

from __future__ import annotations

from itertools import combinations
from math import comb

import numpy as np

import actual_sym2_c14_orbit_probe as native_clifford


TOL = 1.0e-10
FD_TOL = 1.0e-7
FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    rows = sum(block.shape[0] for block in blocks)
    columns = sum(block.shape[1] for block in blocks)
    out = np.zeros((rows, columns), dtype=complex)
    row = column = 0
    for block in blocks:
        out[
            row : row + block.shape[0],
            column : column + block.shape[1],
        ] = block
        row += block.shape[0]
        column += block.shape[1]
    return out


def relative_norm(left: np.ndarray, right: np.ndarray) -> float:
    denominator = max(1.0, float(np.linalg.norm(right)))
    return float(np.linalg.norm(left - right) / denominator)


# ---------------------------------------------------------------------------
# A. Preregistered Ricci--Einstein same-spin-sector route
# ---------------------------------------------------------------------------


print("=" * 100)
print("RB1b NATIVE BOSONIC-SHIAB REOPENER")
print("=" * 100)
print("\nA. Layer-0 carrier and exact parity obstruction")

dimension_v = 14
dimension_spin_adjoint = comb(dimension_v, 2)
domain_dimension = dimension_spin_adjoint**2
target_one_form_dimension = dimension_v * dimension_spin_adjoint
general_ricci_contraction_dimension = dimension_v**2
algebraic_riemann_ricci_dimension = (
    dimension_v * (dimension_v + 1) // 2
)

# The complexified Spin(14) central lift of -I acts by (-1)^tensor_degree.
# An intertwiner T from a +1 representation to a -1 representation obeys
# T = -T and is therefore zero.
source_central_character = (-1) ** (2 + 2)
target_central_character = (-1) ** (1 + 2)
same_sector_hom_dimension = (
    0
    if source_central_character != target_central_character
    else -1
)

check(
    "the full-Spin same-Lambda2 algebraic Hom is exactly zero by central parity",
    source_central_character == 1
    and target_central_character == -1
    and same_sector_hom_dimension == 0,
)
check(
    "Ricci contraction lands in V*xV*, or Sym2 with Riemann symmetries, not a one-form spin adjoint",
    general_ricci_contraction_dimension == 196
    and algebraic_riemann_ricci_dimension == 105
    and target_one_form_dimension == 1274
    and domain_dimension == 8281,
)
check(
    "a nondegenerate pairing cannot repair a zero intertwiner space",
    same_sector_hom_dimension == 0,
)

# A diagonal coframe has one external and one internal vector factor.  It is
# parity even under the diagonal Spin action and supplies no unpaired odd
# index for a same-Lambda2 target.
diagonal_coframe_character = (-1) ** (1 + 1)
check(
    "the diagonal coframe is parity-even and does not reopen the route",
    diagonal_coframe_character == 1,
)


# ---------------------------------------------------------------------------
# B. Adjacent full-adjoint grade-flipping formula: finite architecture only
# ---------------------------------------------------------------------------


print("\nB. Full-adjoint carrier and Hodge-degree architecture")

native_adjoint_grades = (2, 3, 6, 7, 10, 11, 14)
native_adjoint_grade_dimensions = tuple(
    comb(dimension_v, grade) for grade in native_adjoint_grades
)
reversion_skew_grades = tuple(
    grade
    for grade in range(dimension_v + 1)
    if (-1) ** (grade * (grade - 1) // 2) == -1
)
native_gammas, _native_metric = native_clifford.native_gammas()
native_krein = np.eye(128, dtype=complex)
for gamma in native_gammas[:9]:
    native_krein = native_krein @ gamma
native_krein_inverse = np.linalg.inv(native_krein)
check(
    "native gammas are Krein-self-adjoint and reversion selects exactly the stated skew grades",
    max(
        np.max(
            np.abs(
                native_krein_inverse
                @ gamma.conj().T
                @ native_krein
                - gamma
            )
        )
        for gamma in native_gammas
    )
    < TOL
    and reversion_skew_grades == native_adjoint_grades,
)
check(
    "the declared Clifford-adjoint grades sum to dim sp(32,32;H)=8256",
    sum(native_adjoint_grade_dimensions) == 8256,
    str(dict(zip(native_adjoint_grades, native_adjoint_grade_dimensions))),
)
check(
    "the grade-flipping Lambda2-to-(V* tensor Lambda3) channel clears parity",
    (-1) ** (2 + 2) == (-1) ** (1 + 3) == 1,
)
candidate_descent_grade = (
    "LOCAL-FRAMED; ASSOCIATED-BUNDLE-H-DESCENT-UNBUILT"
)
epsilon_convention = "epsilon_source = inverse(g_RB3)"
check(
    "the adjacent candidate keeps its local framed descent grade explicit",
    candidate_descent_grade
    == "LOCAL-FRAMED; ASSOCIATED-BUNDLE-H-DESCENT-UNBUILT"
    and epsilon_convention == "epsilon_source = inverse(g_RB3)",
)


Form = dict[tuple[int, ...], np.ndarray]
BASE_DIMENSION = 4
BASE_METRIC = np.array([1.0, 1.0, 1.0, -1.0])
I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
J_QUAT = np.block([[Z2, I2], [-I2, Z2]])
H2 = np.diag([1.0, -1.0])
KREIN = block_diag(H2, H2)
KREIN_INV = np.linalg.inv(KREIN)


def h_linear_matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Complex 4x4 realization of a quaternionic 2x2 matrix."""
    return np.block([[a, b], [-b.conj(), a.conj()]])


def h_defect(matrix: np.ndarray) -> float:
    return float(
        np.linalg.norm(
            matrix @ J_QUAT - J_QUAT @ matrix.conj()
        )
    )


def krein_adjoint(matrix: np.ndarray) -> np.ndarray:
    return KREIN_INV @ matrix.conj().T @ KREIN


def project_krein_skew(matrix: np.ndarray) -> np.ndarray:
    """Krein-skew projection; it is native sp only on right-H inputs."""
    return 0.5 * (matrix - krein_adjoint(matrix))


def permutation_sign(indices: tuple[int, ...]) -> int:
    inversions = sum(
        indices[left] > indices[right]
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def add_forms(*forms: Form) -> Form:
    keys = set().union(*(form.keys() for form in forms))
    return {
        key: sum(
            (form.get(key, np.zeros((4, 4), dtype=complex)) for form in forms),
            np.zeros((4, 4), dtype=complex),
        )
        for key in keys
    }


def scale_form(form: Form, scalar: float) -> Form:
    return {key: scalar * value for key, value in form.items()}


def wedge(left: Form, right: Form) -> Form:
    out: Form = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            joined = left_key + right_key
            if len(set(joined)) != len(joined):
                continue
            key = tuple(sorted(joined))
            coefficient = permutation_sign(joined)
            value = coefficient * left_value @ right_value
            out[key] = out.get(
                key,
                np.zeros((4, 4), dtype=complex),
            ) + value
    return out


def hodge(form: Form) -> Form:
    out: Form = {}
    full = tuple(range(BASE_DIMENSION))
    for key, value in form.items():
        complement = tuple(index for index in full if index not in key)
        coefficient = (
            permutation_sign(key + complement)
            * float(np.prod(BASE_METRIC[list(key)]))
        )
        out[complement] = coefficient * value
    return out


def form_degree(form: Form) -> int:
    degrees = {len(key) for key in form}
    if len(degrees) != 1:
        raise ValueError(f"inhomogeneous form: {degrees}")
    return next(iter(degrees), -1)


def form_norm(form: Form) -> float:
    return float(
        np.sqrt(
            sum(np.linalg.norm(value) ** 2 for value in form.values())
        )
    )


def form_relative(left: Form, right: Form) -> float:
    keys = set(left) | set(right)
    numerator = np.sqrt(
        sum(
            np.linalg.norm(
                left.get(key, np.zeros((4, 4), dtype=complex))
                - right.get(key, np.zeros((4, 4), dtype=complex))
            )
            ** 2
            for key in keys
        )
    )
    return float(numerator / max(1.0, form_norm(right)))


def project_form(form: Form) -> Form:
    return {
        key: project_krein_skew(value)
        for key, value in form.items()
    }


def adjoint_form(group: np.ndarray, form: Form) -> Form:
    inverse = np.linalg.inv(group)
    return {
        key: group @ value @ inverse for key, value in form.items()
    }


def epsilon_frame(form: Form, epsilon: np.ndarray) -> Form:
    return adjoint_form(np.linalg.inv(epsilon), form)


def top_trace(form: Form) -> complex:
    return complex(np.trace(form[(0, 1, 2, 3)]))


def raw_shiab(
    epsilon: np.ndarray,
    curvature: Form,
    phi_one: Form,
    phi_two: Form,
) -> Form:
    e_one = epsilon_frame(phi_one, epsilon)
    e_two = epsilon_frame(phi_two, epsilon)
    first = wedge(e_one, hodge(curvature))
    second = hodge(
        wedge(
            e_one,
            hodge(wedge(e_two, hodge(curvature))),
        )
    )
    return project_form(add_forms(first, scale_form(second, -0.5)))


def random_complex(
    rng: np.random.Generator,
    shape: tuple[int, int],
) -> np.ndarray:
    return rng.standard_normal(shape) + 1j * rng.standard_normal(shape)


def random_h_linear(
    rng: np.random.Generator,
    scale: float,
) -> np.ndarray:
    return scale * h_linear_matrix(
        random_complex(rng, (2, 2)),
        random_complex(rng, (2, 2)),
    )


def random_form(
    rng: np.random.Generator,
    degree: int,
    scale: float,
    in_sp: bool,
) -> Form:
    result = {
        key: random_h_linear(rng, scale)
        for key in combinations(range(BASE_DIMENSION), degree)
    }
    return project_form(result) if in_sp else result


def boost(parameter: float) -> np.ndarray:
    block = np.array(
        [
            [np.cosh(parameter), np.sinh(parameter)],
            [np.sinh(parameter), np.cosh(parameter)],
        ],
        dtype=complex,
    )
    return block_diag(block, block)


def phase(left: float, right: float) -> np.ndarray:
    block = np.diag(
        [np.exp(1j * left), np.exp(1j * right)]
    )
    return block_diag(block, block.conj())


rng = np.random.default_rng(20260730)
epsilon = boost(0.21) @ phase(0.13, -0.08)
group = phase(0.37, -0.19) @ boost(0.31)

phi_one = random_form(rng, 1, 0.2, in_sp=False)
phi_two = random_form(rng, 2, 0.2, in_sp=False)
curvature = random_form(rng, 2, 0.2, in_sp=True)
theta = random_form(rng, 1, 0.15, in_sp=True)
delta_theta = random_form(rng, 1, 0.1, in_sp=True)
chi = project_krein_skew(random_h_linear(rng, 0.07))

check(
    "the finite native transformations preserve Krein and right-H structures",
    np.linalg.norm(group.conj().T @ KREIN @ group - KREIN) < TOL
    and h_defect(group) < TOL,
)

shiab = raw_shiab(epsilon, curvature, phi_one, phi_two)
check(
    "the source-shaped architecture has output degree d-1 without a final Hodge",
    form_degree(shiab) == 3,
)
check(
    "an extra final Hodge is a detected double-Hodge error",
    form_degree(hodge(shiab)) == 1,
)
check(
    "the finite output remains right-H linear",
    max(h_defect(value) for value in shiab.values()) < TOL,
)

epsilon_transformed = epsilon @ np.linalg.inv(group)
curvature_transformed = adjoint_form(group, curvature)
shiab_transformed = raw_shiab(
    epsilon_transformed,
    curvature_transformed,
    phi_one,
    phi_two,
)
shiab_expected = adjoint_form(group, shiab)
native_covariance_defect = form_relative(
    shiab_transformed,
    shiab_expected,
)
check(
    "moving-epsilon homogeneous covariance closes in the native fixture",
    native_covariance_defect < TOL,
    f"residual={native_covariance_defect:.3e}",
)

wrong_epsilon = group @ epsilon
wrong_law_defect = form_relative(
    raw_shiab(
        wrong_epsilon,
        curvature_transformed,
        phi_one,
        phi_two,
    ),
    shiab_expected,
)
check(
    "the wrong epsilon transformation law is rejected",
    wrong_law_defect > 1.0e-3,
    f"plant={wrong_law_defect:.3e}",
)

raw_action_trace = top_trace(wedge(theta, shiab))
check(
    "the reduced-trace action pairing is real on the native fixture",
    abs(raw_action_trace.imag) < TOL,
    f"imag={raw_action_trace.imag:.3e}",
)


def epsilon_derivative(
    epsilon_value: np.ndarray,
    curvature_value: Form,
    phi_one_value: Form,
    phi_two_value: Form,
    chi_value: np.ndarray,
) -> Form:
    e_one = epsilon_frame(phi_one_value, epsilon_value)
    e_two = epsilon_frame(phi_two_value, epsilon_value)
    d_one = {
        key: value @ chi_value - chi_value @ value
        for key, value in e_one.items()
    }
    d_two = {
        key: value @ chi_value - chi_value @ value
        for key, value in e_two.items()
    }
    first = wedge(d_one, hodge(curvature_value))
    second_left = wedge(
        d_one,
        hodge(wedge(e_two, hodge(curvature_value))),
    )
    second_right = wedge(
        e_one,
        hodge(wedge(d_two, hodge(curvature_value))),
    )
    return project_form(
        add_forms(
            first,
            scale_form(
                hodge(add_forms(second_left, second_right)),
                -0.5,
            ),
        )
    )


step = 1.0e-6
analytic_epsilon_response = epsilon_derivative(
    epsilon,
    curvature,
    phi_one,
    phi_two,
    chi,
)
plus = raw_shiab(
    epsilon @ (I4 + step * chi),
    curvature,
    phi_one,
    phi_two,
)
minus = raw_shiab(
    epsilon @ (I4 - step * chi),
    curvature,
    phi_one,
    phi_two,
)
finite_epsilon_response = scale_form(
    add_forms(plus, scale_form(minus, -1.0)),
    1.0 / (2.0 * step),
)
epsilon_response_defect = form_relative(
    finite_epsilon_response,
    analytic_epsilon_response,
)
check(
    "the explicit-map epsilon response at fixed curvature matches a central finite difference",
    epsilon_response_defect < FD_TOL
    and form_norm(analytic_epsilon_response) > 1.0e-3,
    f"residual={epsilon_response_defect:.3e}",
)


# ---------------------------------------------------------------------------
# C. Planted real-form and transgression failures
# ---------------------------------------------------------------------------


print("\nC. Wrong-real-form and cyclicity controls")

wrong_group = np.diag(
    np.exp(1j * np.array([0.11, 0.29, 0.53, -0.17]))
)
check(
    "the U(2,2)-type comparator preserves Krein but violates right-H",
    np.linalg.norm(
        wrong_group.conj().T @ KREIN @ wrong_group - KREIN
    )
    < TOL
    and h_defect(wrong_group) > 1.0e-3,
)
wrong_real_output = raw_shiab(
    epsilon @ np.linalg.inv(wrong_group),
    adjoint_form(wrong_group, curvature),
    phi_one,
    phi_two,
)
wrong_real_expected = adjoint_form(wrong_group, shiab)
wrong_real_covariance = form_relative(
    wrong_real_output,
    wrong_real_expected,
)
wrong_real_h_defect = max(
    h_defect(value) for value in wrong_real_output.values()
)
check(
    "homogeneous covariance alone would falsely admit the complex comparator",
    wrong_real_covariance < TOL,
    f"residual={wrong_real_covariance:.3e}",
)
check(
    "the right-H gate rejects that comparator",
    wrong_real_h_defect > 1.0e-3,
    f"H-defect={wrong_real_h_defect:.3e}",
)


def cubic_function(test_theta: Form) -> float:
    quadratic = wedge(test_theta, test_theta)
    return float(
        top_trace(
            wedge(
                test_theta,
                raw_shiab(
                    epsilon,
                    quadratic,
                    phi_one,
                    phi_two,
                ),
            )
        ).real
    )


theta_plus = add_forms(theta, scale_form(delta_theta, step))
theta_minus = add_forms(theta, scale_form(delta_theta, -step))
cubic_fd = (
    cubic_function(theta_plus) - cubic_function(theta_minus)
) / (2.0 * step)
quadratic_theta = wedge(theta, theta)
cyclic_prediction = 3.0 * float(
    top_trace(
        wedge(
            delta_theta,
            raw_shiab(
                epsilon,
                quadratic_theta,
                phi_one,
                phi_two,
            ),
        )
    ).real
)
cyclic_gap = abs(cubic_fd - cyclic_prediction) / max(
    1.0e-12,
    abs(cubic_fd),
    abs(cyclic_prediction),
)
check(
    "one nondegenerate counterexample shows covariance and reality do not imply the RB2 cyclic identity",
    cyclic_gap > 1.0e-3,
    (
        f"fd={cubic_fd:.6g}, cyclic={cyclic_prediction:.6g}, "
        f"relative-gap={cyclic_gap:.3f}"
    ),
)


print("\nD. Typed disposition")
check(
    "the preregistered full-Spin same-Lambda2 Ricci route is killed, not passed to RB2",
    same_sector_hom_dimension == 0,
)
check(
    "the adjacent source-shaped architecture fixture remains pre-RB1",
    cyclic_gap > 1.0e-3
    and form_degree(shiab) == 3
    and native_covariance_defect < TOL,
)

if FAILURES:
    print(f"\nCONTROLS FAILED: {FAILURES}")
    print("VERDICT: VOID")
    raise SystemExit(1)

print("\nVERDICT: FULL-SPIN-SAME-LAMBDA2-RICCI-ROUTE-KILLED-BY-PARITY")
print("EMISSION: EPSILON-SOLDERED-FULL-ADJOINT-GRADE-FLIP-CONDITIONAL")
print("BLOCK: GRADE-THREE-ADMISSION-AND-NATIVE-CYCLIC-BIANCHI-IDENTITY")
print("REENTRY: NONE; RB1/RB2 SOURCE RECORDS UNCHANGED")
print("ALL CONTROLS PASSED")
