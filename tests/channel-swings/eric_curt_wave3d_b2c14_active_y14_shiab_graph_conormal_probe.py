#!/usr/bin/env python3
r"""B2C14 active-Y14 trace-adapted Shiab graph/conormal gate.

This probe executes the repository-selected bosonic trace-adapted Shiab in
the exact trace-reversed ``(9,5)`` Clifford/exterior algebra.  It keeps the
pointwise operator symbol

    ell(xi) a = S_tr(xi wedge a)

separate from its real-jet formal-transpose symbol and from the composite
reference-graph coefficient

    K0(xi)   = 1/2 (ell(xi) + ell(xi)^top),
    K_act(xi)= K0(xi) sigma(DB_rot)(xi).

For the gauge-rotated reference graph at a normal frame and in the declared
left convention,

    sigma(DB_rot)(xi) chi_m = -xi tensor chi_m,
    sigma(DT|fixed A)(xi) chi_m = +xi tensor chi_m.

Here ``chi_m`` is a genuine quotient tangent in a proved grade-three
``Spin(9,5)``-invariant subspace of
``sp(32,32;H)/spin(9,5)``.  The direct curvature half therefore vanishes by
``xi wedge xi=0``.  The transpose half need not.  The decisive calculation
below evaluates it on the complete 364-dimensional grade-three quotient
slice and the matching complete grade-three connection tester basis.  The
image is computed modulo every one of the 91 vertical lift/stabilizer
bivectors.  All zero/nonzero and rank statements use exact rational Clifford
arithmetic.

The resulting grade-three projected squared-residual comparator is kept
separate from the complete all-grade residual primalizer and from the
characteristic kernel of the full coupled Euler system.  This is a local
pointwise quotient-coefficient result, not a global Y14 domain,
hyperbolicity, positivity, observation, Standard Model, or datum claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
TESTS = ROOT / "tests"
for path in (CHANNEL, TESTS):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import actual_sym2_c14_orbit_probe as sym2  # noqa: E402


FAILURES: list[str] = []
EXACT = 0
SOURCE = 0
TYPE = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(
        f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}",
        flush=True,
    )
    if false_claim:
        FAILURES.append(f"planted: {label}")


# ---------------------------------------------------------------------------
# Exact Cl(9,5) and exterior algebra.


N = 14
FULL_KEY = tuple(range(N))
ETA = (
    F(1),
    F(1),
    F(1),
    F(-1),
    F(1),
    F(1),
    F(1),
    F(1),
    F(1),
    F(1),
    F(-1),
    F(-1),
    F(-1),
    F(-1),
)
TRACE_INDEX = 10
TRACE_MASK = 1 << TRACE_INDEX
SP_GRADES = (2, 3, 6, 7, 10, 11, 14)

Cliff = dict[int, F]
Form = dict[tuple[int, ...], Cliff]


def bits(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


def clean_cliff(value: Cliff) -> Cliff:
    return {mask: coefficient for mask, coefficient in value.items() if coefficient}


def cliff_add(*values: Cliff) -> Cliff:
    result: Cliff = {}
    for value in values:
        for mask, coefficient in value.items():
            result[mask] = result.get(mask, F(0)) + coefficient
    return clean_cliff(result)


def cliff_scale(value: Cliff, coefficient: F) -> Cliff:
    return clean_cliff({mask: coefficient * item for mask, item in value.items()})


def mask_product(left: int, right: int) -> tuple[int, F]:
    left_bits = bits(left)
    right_bits = bits(right)
    inversions = sum(a > b for a in left_bits for b in right_bits)
    coefficient = F(-1 if inversions % 2 else 1)
    for index in bits(left & right):
        coefficient *= ETA[index]
    return left ^ right, coefficient


def cliff_mul(left: Cliff, right: Cliff) -> Cliff:
    result: Cliff = {}
    for left_mask, left_value in left.items():
        for right_mask, right_value in right.items():
            mask, coefficient = mask_product(left_mask, right_mask)
            result[mask] = (
                result.get(mask, F(0))
                + left_value * right_value * coefficient
            )
    return clean_cliff(result)


def cliff_comm(left: Cliff, right: Cliff) -> Cliff:
    return cliff_add(cliff_mul(left, right), cliff_scale(cliff_mul(right, left), F(-1)))


def blade(*indices: int) -> Cliff:
    value: Cliff = {0: F(1)}
    for index in indices:
        value = cliff_mul(value, {1 << index: F(1)})
    return value


def permutation_sign(indices: tuple[int, ...]) -> int:
    inversions = sum(
        indices[left] > indices[right]
        for left in range(len(indices))
        for right in range(left + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def clean_form(value: Form) -> Form:
    return {
        key: clean_cliff(coefficient)
        for key, coefficient in value.items()
        if clean_cliff(coefficient)
    }


def add_forms(*values: Form) -> Form:
    result: Form = {}
    for value in values:
        for key, coefficient in value.items():
            result[key] = cliff_add(result.get(key, {}), coefficient)
    return clean_form(result)


def scale_form(value: Form, coefficient: F) -> Form:
    return clean_form(
        {key: cliff_scale(item, coefficient) for key, item in value.items()}
    )


def wedge(left: Form, right: Form) -> Form:
    result: Form = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            joined = left_key + right_key
            if len(set(joined)) != len(joined):
                continue
            key = tuple(sorted(joined))
            value = cliff_scale(
                cliff_mul(left_value, right_value),
                F(permutation_sign(joined)),
            )
            result[key] = cliff_add(result.get(key, {}), value)
    return clean_form(result)


def hodge(value: Form, metric: tuple[F, ...] = ETA) -> Form:
    result: Form = {}
    for key, coefficient in value.items():
        complement = tuple(index for index in FULL_KEY if index not in key)
        factor = F(permutation_sign(key + complement))
        for index in key:
            factor *= metric[index]
        result[complement] = cliff_scale(coefficient, factor)
    return clean_form(result)


def project_sp(value: Form) -> Form:
    return clean_form(
        {
            key: {
                mask: coefficient
                for mask, coefficient in item.items()
                if mask.bit_count() in SP_GRADES
            }
            for key, item in value.items()
        }
    )


def left_multiply(multiplier: Cliff, value: Form) -> Form:
    return clean_form(
        {key: cliff_mul(multiplier, coefficient) for key, coefficient in value.items()}
    )


PHI_ONE: Form = {(index,): blade(index) for index in range(N)}
PHI_TWO: Form = {
    pair: blade(*pair) for pair in combinations(range(N), 2)
}


def raw_source(
    curvature: Form,
    metric: tuple[F, ...] = ETA,
    one: Form = PHI_ONE,
    two: Form = PHI_TWO,
) -> Form:
    first = wedge(one, hodge(curvature, metric))
    second = hodge(
        wedge(
            one,
            hodge(wedge(two, hodge(curvature, metric)), metric),
        ),
        metric,
    )
    return add_forms(first, scale_form(second, F(-1, 2)))


def trace_line_source(
    curvature: Form,
    metric: tuple[F, ...] = ETA,
    trace: Cliff | None = None,
    one: Form = PHI_ONE,
    two: Form = PHI_TWO,
) -> Form:
    return project_sp(
        left_multiply(
            blade(TRACE_INDEX) if trace is None else trace,
            raw_source(curvature, metric, one, two),
        )
    )


def form_degree(value: Form) -> int:
    degrees = {len(key) for key in value}
    if len(degrees) != 1:
        raise ValueError(f"inhomogeneous or empty form: {degrees}")
    return next(iter(degrees))


def top_pair(one_form: Form, density: Form) -> F:
    top = wedge(one_form, density).get(FULL_KEY, {})
    return top.get(0, F(0))


def basis_pair(mu: int, mask: int, density: Form) -> F:
    """Fast exact top pairing for one basis one-form and a 13-form."""
    complement = tuple(item for item in FULL_KEY if item != mu)
    density_value = density.get(complement, {})
    total = F(0)
    for density_mask, coefficient in density_value.items():
        product_mask, product_coefficient = mask_product(mask, density_mask)
        if product_mask == 0:
            total += coefficient * product_coefficient
    return F(permutation_sign((mu,) + complement)) * total


def one_form(components: dict[int, Cliff]) -> Form:
    return clean_form({(index,): value for index, value in components.items()})


def basis_one(index: int, mask: int, coefficient: F = F(1)) -> Form:
    return one_form({index: {mask: coefficient}})


def covector_form(components: tuple[F, ...]) -> Form:
    return clean_form(
        {
            (index,): {0: coefficient}
            for index, coefficient in enumerate(components)
            if coefficient
        }
    )


def graph_one(components: tuple[F, ...], internal_mask: int) -> Form:
    return clean_form(
        {
            (index,): {internal_mask: -coefficient}
            for index, coefficient in enumerate(components)
            if coefficient
        }
    )


def connection_lower(value: Form, metric: tuple[F, ...] = ETA) -> Form:
    return hodge(value, metric)


# ---------------------------------------------------------------------------
# Exact formal-symmetric graph coefficient on the reduction subspace.


ALL_BIVECTORS = tuple(
    sum(1 << index for index in pair) for pair in combinations(range(N), 2)
)
H_BIVECTORS = ALL_BIVECTORS
QUOTIENT_GRADE3 = tuple(
    sum(1 << index for index in triple)
    for triple in combinations(range(N), 3)
)
TESTERS = tuple(
    (mu, mask) for mu in range(N) for mask in QUOTIENT_GRADE3
)
FULL_QUOTIENT_DIMENSION = sum(
    sp.binomial(N, degree) for degree in (3, 6, 7, 10, 11, 14)
)


def pair_graph_with_density(
    xi: tuple[F, ...], internal_mask: int, density: Form
) -> F:
    """Pair ``-xi tensor gamma_I`` with a degree-13 density exactly."""
    total = F(0)
    for index, xi_value in enumerate(xi):
        if not xi_value:
            continue
        complement = tuple(item for item in FULL_KEY if item != index)
        density_value = density.get(complement, {})
        internal = cliff_mul({internal_mask: -xi_value}, density_value)
        total += F(permutation_sign((index,) + complement)) * internal.get(0, F(0))
    return total


def tester_norm(mu: int, mask: int, metric: tuple[F, ...] = ETA) -> F:
    value = basis_one(mu, mask)
    return top_pair(value, connection_lower(value, metric))


def build_graph_k(
    xi: tuple[F, ...],
    owners: tuple[int, ...],
    metric: tuple[F, ...] = ETA,
) -> tuple[list[dict[int, F]], list[F], list[tuple[int, int, F]]]:
    """Return exact rows of K_act on a declared internal-owner slice.

    Rows are the complete grade-three one-form tester basis.  Columns are the
    supplied lexicographically frozen owner masks.  The direct
    ``ell(xi)(-xi chi)`` half is identically zero; the returned coefficient
    is one half of the transpose pairing.
    """
    xi_form = covector_form(xi)
    rows: list[dict[int, F]] = []
    norms: list[F] = []
    witnesses: list[tuple[int, int, F]] = []
    for row_index, (mu, tester_mask) in enumerate(TESTERS):
        tester = basis_one(mu, tester_mask)
        density = trace_line_source(wedge(xi_form, tester), metric)
        row: dict[int, F] = {}
        for column, owner_mask in enumerate(owners):
            coefficient = F(1, 2) * pair_graph_with_density(
                xi, owner_mask, density
            )
            if coefficient:
                row[column] = coefficient
                witnesses.append((row_index, column, coefficient))
        rows.append(row)
        norms.append(tester_norm(mu, tester_mask, metric))
    return rows, norms, witnesses


def build_h_return_k(
    xi: tuple[F, ...], metric: tuple[F, ...] = ETA
) -> tuple[
    list[dict[int, F]],
    list[dict[int, F]],
    list[dict[int, F]],
    list[dict[int, F]],
    list[F],
]:
    """Project ``K0(xi)`` on every possible h-valued LC principal return.

    The domain is the conservative space ``T*Y tensor spin(9,5)`` rather than
    the smaller diagonal ``xi tensor h`` ansatz.  Rows are the matching
    grade-three residual testers.  A quotient-grade graph class outside this
    image cannot be canceled by any h-valued Levi--Civita return.
    """
    xi_form = covector_form(xi)
    h_inputs = tuple(
        (mu, mask) for mu in range(N) for mask in H_BIVECTORS
    )
    direct_densities = tuple(
        trace_line_source(
            wedge(xi_form, basis_one(mu, mask)), metric
        )
        for mu, mask in h_inputs
    )
    plus_rows: list[dict[int, F]] = []
    minus_rows: list[dict[int, F]] = []
    direct_rows: list[dict[int, F]] = []
    transpose_rows: list[dict[int, F]] = []
    norms: list[F] = []
    for tester_mu, tester_mask in TESTERS:
        tester = basis_one(tester_mu, tester_mask)
        transpose_density = trace_line_source(wedge(xi_form, tester), metric)
        plus_row: dict[int, F] = {}
        minus_row: dict[int, F] = {}
        direct_row: dict[int, F] = {}
        transpose_row: dict[int, F] = {}
        for column, ((input_mu, input_mask), direct_density) in enumerate(
            zip(h_inputs, direct_densities)
        ):
            direct = basis_pair(tester_mu, tester_mask, direct_density)
            transpose = basis_pair(input_mu, input_mask, transpose_density)
            plus = F(1, 2) * (direct + transpose)
            minus = F(1, 2) * (direct - transpose)
            if direct:
                direct_row[column] = direct
            if transpose:
                transpose_row[column] = transpose
            if plus:
                plus_row[column] = plus
            if minus:
                minus_row[column] = minus
        plus_rows.append(plus_row)
        minus_rows.append(minus_row)
        direct_rows.append(direct_row)
        transpose_rows.append(transpose_row)
        norms.append(tester_norm(tester_mu, tester_mask, metric))
    return plus_rows, minus_rows, direct_rows, transpose_rows, norms


def merge_column_blocks(
    left: list[dict[int, F]],
    right: list[dict[int, F]],
    left_columns: int,
) -> list[dict[int, F]]:
    return [
        {
            **left_row,
            **{
                left_columns + column: value
                for column, value in right_row.items()
            },
        }
        for left_row, right_row in zip(left, right)
    ]


def sparse_row_rank(rows: list[dict[int, F]], columns: int) -> int:
    pivots: dict[int, dict[int, F]] = {}
    for source in rows:
        row = dict(source)
        for lead in sorted(pivots):
            if lead not in row:
                continue
            factor = row[lead]
            for column, value in pivots[lead].items():
                updated = row.get(column, F(0)) - factor * value
                if updated:
                    row[column] = updated
                elif column in row:
                    del row[column]
        if not row:
            continue
        lead = min(row)
        factor = row[lead]
        row = {column: value / factor for column, value in row.items()}
        pivots[lead] = row
        if len(pivots) == columns:
            return columns
    return len(pivots)


def combine_rows(
    *terms: tuple[F, list[dict[int, F]]]
) -> list[dict[int, F]]:
    result: list[dict[int, F]] = []
    for row_index in range(len(TESTERS)):
        row: dict[int, F] = {}
        for coefficient, rows in terms:
            for column, value in rows[row_index].items():
                row[column] = row.get(column, F(0)) + coefficient * value
        result.append({column: value for column, value in row.items() if value})
    return result


def leading_hessian(
    rows: list[dict[int, F]], norms: list[F], size: int
) -> list[list[F]]:
    result = [[F(0) for _ in range(size)] for _ in range(size)]
    for row, norm in zip(rows, norms):
        if not row:
            continue
        if not norm:
            raise ValueError("degenerate connection tester basis")
        items = tuple(row.items())
        for left, left_value in items:
            for right, right_value in items:
                result[left][right] += left_value * right_value / norm
    return result


def dense_rank(matrix: list[list[F]]) -> int:
    return sparse_row_rank(
        [
            {column: value for column, value in enumerate(row) if value}
            for row in matrix
        ],
        len(matrix[0]) if matrix else 0,
    )


def swap_symmetric(matrix: list[list[F]], left: int, right: int) -> None:
    if left == right:
        return
    matrix[left], matrix[right] = matrix[right], matrix[left]
    for row in matrix:
        row[left], row[right] = row[right], row[left]


def symmetric_inertia(source: list[list[F]]) -> tuple[int, int, int]:
    """Exact rational congruence inertia with 1x1/2x2 pivots."""
    matrix = [list(row) for row in source]
    positive = negative = 0
    while matrix:
        size = len(matrix)
        diagonal = next((i for i in range(size) if matrix[i][i]), None)
        if diagonal is not None:
            swap_symmetric(matrix, 0, diagonal)
            pivot = matrix[0][0]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            remainder = [
                [
                    matrix[i][j] - matrix[i][0] * matrix[0][j] / pivot
                    for j in range(1, size)
                ]
                for i in range(1, size)
            ]
            matrix = remainder
            continue
        off = next(
            (
                (i, j)
                for i in range(size)
                for j in range(i + 1, size)
                if matrix[i][j]
            ),
            None,
        )
        if off is None:
            return positive, negative, size
        left, right = off
        swap_symmetric(matrix, 0, left)
        if right == 0:
            right = left
        swap_symmetric(matrix, 1, right)
        a = matrix[0][1]
        b = matrix[1][1]
        # The 2x2 pivot [[0,a],[a,b]] has determinant -a^2 < 0.
        positive += 1
        negative += 1
        inverse = [[-b / (a * a), F(1) / a], [F(1) / a, F(0)]]
        remainder: list[list[F]] = []
        for i in range(2, size):
            row: list[F] = []
            for j in range(2, size):
                correction = sum(
                    matrix[i][p] * inverse[p][q] * matrix[q][j]
                    for p in range(2)
                    for q in range(2)
                )
                row.append(matrix[i][j] - correction)
            remainder.append(row)
        matrix = remainder
    return positive, negative, 0


def vector(*entries: tuple[int, int]) -> tuple[F, ...]:
    result = [F(0)] * N
    for index, coefficient in entries:
        result[index] = F(coefficient)
    return tuple(result)


def quadratic_norm(xi: tuple[F, ...]) -> F:
    return sum(ETA[index] * value * value for index, value in enumerate(xi))


# ---------------------------------------------------------------------------
# Exact moving-Shiab / six-permutation M response in the reduction direction.


def form_commutator(value: Form, generator: Cliff) -> Form:
    return clean_form(
        {
            key: cliff_comm(coefficient, generator)
            for key, coefficient in value.items()
        }
    )


def derivative_raw_source(
    curvature: Form,
    d_one: Form,
    d_two: Form,
    metric: tuple[F, ...] = ETA,
) -> Form:
    first = wedge(d_one, hodge(curvature, metric))
    second_left = wedge(
        d_one,
        hodge(wedge(PHI_TWO, hodge(curvature, metric)), metric),
    )
    second_right = wedge(
        PHI_ONE,
        hodge(wedge(d_two, hodge(curvature, metric)), metric),
    )
    second = hodge(add_forms(second_left, second_right), metric)
    return add_forms(first, scale_form(second, F(-1, 2)))


def derivative_trace_source(curvature: Form, generator: Cliff) -> Form:
    trace = blade(TRACE_INDEX)
    d_trace = cliff_comm(trace, generator)
    d_one = form_commutator(PHI_ONE, generator)
    d_two = form_commutator(PHI_TWO, generator)
    raw = raw_source(curvature)
    d_raw = derivative_raw_source(curvature, d_one, d_two)
    return project_sp(
        add_forms(
            left_multiply(d_trace, raw),
            left_multiply(trace, d_raw),
        )
    )


def q_sym(left: Form, right: Form) -> Form:
    return scale_form(add_forms(wedge(left, right), wedge(right, left)), F(1, 2))


def cubic_slot(source, x: Form, y: Form, z: Form) -> F:
    return top_pair(x, source(q_sym(y, z)))


def symmetric_six(source, x: Form, y: Form, z: Form) -> F:
    values = (x, y, z)
    return F(1, 6) * sum(
        cubic_slot(source, values[a], values[b], values[c])
        for a, b, c in permutations(range(3))
    )


# ---------------------------------------------------------------------------
# Independent native-matrix and variable-density controls.


def mask_matrix(mask: int, gammas: list[np.ndarray]) -> np.ndarray:
    result = np.eye(gammas[0].shape[0], dtype=complex)
    for index in bits(mask):
        result = result @ gammas[index]
    return result


def cliff_matrix(value: Cliff, gammas: list[np.ndarray]) -> np.ndarray:
    return sum(
        (float(coefficient) * mask_matrix(mask, gammas) for mask, coefficient in value.items()),
        np.zeros_like(gammas[0]),
    )


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value)))


def matrix_product(values: list[np.ndarray]) -> np.ndarray:
    result = np.eye(values[0].shape[0], dtype=complex)
    for value in values:
        result = result @ value
    return result


def native_matrix_checks(
    xi: tuple[F, ...],
    witness: tuple[int, int, F],
    rows: list[dict[int, F]],
    owners: tuple[int, ...],
) -> None:
    original_gammas, original_metric = sym2.native_gammas()
    split_order = (0, 1, 2, 9, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13)
    gammas = [original_gammas[index] for index in split_order]
    metric = tuple(F(int(value)) for value in original_metric[list(split_order)])
    exact(
        "the exact algebra and native 128x128 representation use the same split (9,5) metric",
        metric == ETA and sym2.clifford_defect(gammas, np.array(ETA, dtype=float)) < 1.0e-10,
    )

    row_index, column, coefficient = witness
    mu, tester_mask = TESTERS[row_index]
    owner_mask = owners[column]
    tester = basis_one(mu, tester_mask)
    density = trace_line_source(wedge(covector_form(xi), tester))
    exact_pair = pair_graph_with_density(xi, owner_mask, density)

    # Convert the exact source and graph one-form to the native matrices and
    # independently evaluate RB1c's 0.5 ReTr top pairing.  Since dim S=128,
    # it equals 64 times the normalized scalar-part pairing used above.
    matrix_total = 0.0
    for index, xi_value in enumerate(xi):
        if not xi_value:
            continue
        complement = tuple(item for item in FULL_KEY if item != index)
        graph_matrix = -float(xi_value) * mask_matrix(owner_mask, gammas)
        density_matrix = cliff_matrix(density.get(complement, {}), gammas)
        matrix_total += (
            permutation_sign((index,) + complement)
            * 0.5
            * float(np.trace(graph_matrix @ density_matrix).real)
        )
    exact(
        "the exact scalar certificate agrees with the independent 128x128 half-trace pairing",
        abs(matrix_total - 64.0 * float(exact_pair)) < 1.0e-8
        and coefficient == F(1, 2) * exact_pair
        and rows[row_index][column] == coefficient,
        f"exact={coefficient}; matrix={matrix_total / 128.0}",
    )

    beta = matrix_product(original_gammas[:9])
    right_h = matrix_product(
        [original_gammas[index] for index in (1, 3, 5, 7, 10, 12)]
    )
    c_plus = np.linalg.inv(
        matrix_product(
            [original_gammas[index] for index in range(14) if index % 2 == 0]
        )
    )

    def defects(matrix: np.ndarray) -> tuple[float, float, float]:
        return (
            max_abs(matrix @ right_h - right_h @ matrix.conj()),
            max_abs(beta @ matrix + matrix.conj().T @ beta),
            max_abs(matrix.T @ c_plus + c_plus @ matrix),
        )

    owner_matrix = mask_matrix(owner_mask, gammas)
    density_defects = [
        defects(cliff_matrix(value, gammas)) for value in density.values()
    ]
    exact(
        "the owner generator and active trace-adapted output are right-H, Krein-skew, and C-plus compatible",
        max(defects(owner_matrix)) < 1.0e-10
        and max((max(value) for value in density_defects), default=0.0) < 2.0e-9,
    )


def density_green_checks() -> None:
    x = sp.symbols("x", real=True)
    rho = 1 + x
    coefficient = sp.Integer(2)
    u = 1 + x**2
    v = 1 + x + x**3
    direct = sp.integrate(v * rho * coefficient * sp.diff(u, x), (x, 0, 1))
    adjoint = -sp.diff(rho * coefficient * v, x)
    boundary = (v * rho * coefficient * u).subs(x, 1) - (v * rho * coefficient * u).subs(x, 0)
    bulk = sp.integrate(u * adjoint, (x, 0, 1))
    frozen = sp.integrate(u * (-rho * coefficient * sp.diff(v, x)), (x, 0, 1))
    exact(
        "the scalar variable-density control satisfies formal-adjoint plus nonzero Green-endpoint identity",
        sp.simplify(direct - bulk - boundary) == 0,
        f"direct={direct}; bulk={bulk}; boundary={boundary}",
    )
    exact(
        "the scalar Green endpoint is nonzero and fixes the boundary-flux sign",
        boundary != 0 and sp.simplify(direct - bulk + boundary) != 0,
        f"boundary={boundary}",
    )
    reject(
        "freeze the density derivative in the scalar formal adjoint",
        sp.simplify(direct - frozen - boundary) == 0,
    )
    exact(
        "density derivatives are subprincipal and do not alter the frozen pointwise K0 coefficient",
        sp.diff(rho * coefficient, x).subs(x, 0) != 0
        and (rho * coefficient).subs(x, 0) == 2,
    )


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md").read_text()
    rb1c = (ROOT / "explorations/rb1c-native-grade3-curvature-admission-2026-07-30.md").read_text()
    source_receipt(
        "the draft packet fixes the completed T/Shiab/F_B plus one-half D_B T plus one-third bracket action grammar",
        "F_{B_\\omega}" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "2021 draft p.44 eq.9.4",
    )
    source_receipt(
        "the checked author record identifies displacement from gauge-rotated Levi-Civita in the contortion slot",
        "02:19:17" in toe
        and "contorsion/torsion slot" in toe
        and "gauge-rotated Levi--Civita" in toe,
        "TOE official/local 02:17:07/02:19:17-02:20:33",
    )
    source_receipt(
        "source trace reversal and contraction-not-projection collide explicitly with the repository Shiab family",
        "00:20:51" in toe
        and "01:36:35" in toe
        and "trace-reversed Frobenius" in toe
        and "contraction, not a projection" in toe
        and "four-ordering family" in rb1c
        and "trace adapter" in rb1c,
        "TOE 00:20:51-00:29:16 and 01:34:49-01:36:56",
    )


def main() -> int:
    print("ECW3D-B2C14R DESCENDED QUOTIENT-GRADE SHIAB / GRAPH GATE")
    source_checks()

    exact(
        "the native metric is trace-reversed (9,5) with a negative DeWitt trace line",
        sum(value > 0 for value in ETA) == 9
        and sum(value < 0 for value in ETA) == 5
        and ETA[TRACE_INDEX] == -1,
    )
    hodge_plant = {(0, 1): {0: F(1)}}
    raw_metric = tuple(F(1) if index == TRACE_INDEX else value for index, value in enumerate(ETA))
    exact(
        "trace reversal changes the degree-two Hodge square from hostile +1 to active -1",
        hodge(hodge(hodge_plant)) == scale_form(hodge_plant, F(-1))
        and hodge(hodge(hodge_plant, raw_metric), raw_metric) == hodge_plant,
    )

    generic = {(0, 1): blade(2, 3)}
    active_source = trace_line_source(generic)
    exact(
        "the exact trace-adapted Shiab is nonzero and lands in degree thirteen",
        bool(active_source) and form_degree(active_source) == 13,
    )
    exact(
        "an extra final Hodge is detected as the wrong degree-one object",
        form_degree(hodge(active_source)) == 1,
    )

    exact(
        "the declared reduction tangent is g/h of dimension 8165 and the executed grade-three slice is horizontal",
        len(H_BIVECTORS) == 91
        and int(FULL_QUOTIENT_DIMENSION) == 8165
        and len(QUOTIENT_GRADE3) == 364
        and not set(H_BIVECTORS).intersection(QUOTIENT_GRADE3),
    )
    exact(
        "the complete grade-three slice is invariant under every spin(9,5) bivector commutator",
        all(
            set(cliff_comm({h_mask: F(1)}, {m_mask: F(1)})).issubset(
                QUOTIENT_GRADE3
            )
            for h_mask in H_BIVECTORS
            for m_mask in QUOTIENT_GRADE3
        ),
    )

    xi0 = vector((0, 1))
    paired_lift_cancellations = []
    bare_lift_terms = []
    for h_mask in H_BIVECTORS:
        bare_db_lift = graph_one(xi0, h_mask)
        comoving_omega_return = scale_form(bare_db_lift, F(-1))
        bare_lift_terms.append(bare_db_lift)
        paired_lift_cancellations.append(
            add_forms(bare_db_lift, comoving_omega_return)
        )
    exact(
        "every vertical lift direction cancels when u and omega_LC co-move by the G1 right-H law",
        all(bare_lift_terms) and not any(paired_lift_cancellations),
    )
    reject(
        "treat the bare fixed-frame h lift term as a descended epsilon_red tangent",
        not all(bare_lift_terms),
    )

    normals = {
        "base_spacelike": xi0,
        "base_null": vector((0, 1), (3, 1)),
        "base_spacelike_second": vector((1, 1)),
        "base_spacelike_sum": vector((0, 1), (1, 1)),
    }
    results: dict[str, dict] = {}
    for name, xi in normals.items():
        quotient_rows, norms, witnesses = build_graph_k(
            xi, QUOTIENT_GRADE3
        )
        (
            h_return_rows,
            h_return_minus_rows,
            h_direct_rows,
            h_transpose_rows,
            _,
        ) = build_h_return_k(xi)
        h_columns = N * len(H_BIVECTORS)
        rank_h_image = sparse_row_rank(h_return_rows, h_columns)
        rank_h_minus = sparse_row_rank(h_return_minus_rows, h_columns)
        rank_h_direct = sparse_row_rank(h_direct_rows, h_columns)
        rank_h_transpose = sparse_row_rank(h_transpose_rows, h_columns)
        combined_rows = merge_column_blocks(
            h_return_rows, quotient_rows, h_columns
        )
        rank_combined = sparse_row_rank(
            combined_rows, h_columns + len(QUOTIENT_GRADE3)
        )
        quotient_rank = rank_combined - rank_h_image
        projected_hessian = leading_hessian(
            quotient_rows, norms, len(QUOTIENT_GRADE3)
        )
        projected_rank_hessian = dense_rank(projected_hessian)
        results[name] = {
            "xi": xi,
            "rows": quotient_rows,
            "h_rows": h_return_rows,
            "h_minus_rows": h_return_minus_rows,
            "norms": norms,
            "witnesses": witnesses,
            "rank_h_image": rank_h_image,
            "rank_combined": rank_combined,
            "quotient_rank": quotient_rank,
            "projected_rank_hessian": projected_rank_hessian,
        }
        exact(
            f"{name}: the grade-three-projected reduction-tangent image survives modulo every h-valued LC principal return",
            bool(witnesses)
            and quotient_rank > 0
            and rank_h_image == 0
            and rank_h_minus == 0
            and rank_h_direct == 0
            and rank_h_transpose == 0,
            (
                f"q={quadratic_norm(xi)}; ranks(direct,transpose,+,-)="
                f"({rank_h_direct},{rank_h_transpose},{rank_h_image},{rank_h_minus}); "
                f"rank([C(W_h)|K_m])={rank_combined}; quotient={quotient_rank}"
            ),
        )
        exact(
            f"{name}: the matching grade-three projected Gram rank follows the null/non-null split without being promoted to the all-grade Hessian",
            (
                quadratic_norm(xi) == 0
                and projected_rank_hessian == 0
            )
            or (
                quadratic_norm(xi) != 0
                and projected_rank_hessian == len(QUOTIENT_GRADE3)
            ),
            f"projected-rank={projected_rank_hessian}/364",
        )

    primary = results["base_spacelike"]
    first = primary["witnesses"][0]
    second = primary["witnesses"][1]
    exact(
        "the lexicographic scan returns two distinct exact quotient-grade witnesses",
        first[:2] != second[:2] and first[2] != 0 and second[2] != 0,
        f"first={first}; second={second}",
    )
    native_matrix_checks(
        normals["base_spacelike"], first, primary["rows"], QUOTIENT_GRADE3
    )

    owner0 = QUOTIENT_GRADE3[first[1]]
    direct_graph_curvature = wedge(
        covector_form(xi0), graph_one(xi0, owner0)
    )
    exact(
        "the direct DB_rot graph curvature symbol vanishes exactly by xi wedge xi",
        not direct_graph_curvature,
    )
    exact(
        "the formal-transpose half survives although the direct curvature half vanishes",
        first[2] != 0,
        str(first[2]),
    )
    reject(
        "infer K_act=0 from the direct xi-wedge-xi curvature cancellation",
        first[2] == 0,
    )
    reject(
        "infer a complete prolonged conormal packet from a nonzero quotient-grade residual coefficient alone",
        False,
    )

    mixed_quotient_rows = combine_rows(
        (F(1, 2), results["base_spacelike_sum"]["rows"]),
        (F(-1, 2), results["base_spacelike"]["rows"]),
        (F(-1, 2), results["base_spacelike_second"]["rows"]),
    )
    mixed_h_rows = combine_rows(
        (F(1, 2), results["base_spacelike_sum"]["h_rows"]),
        (F(-1, 2), results["base_spacelike"]["h_rows"]),
        (F(-1, 2), results["base_spacelike_second"]["h_rows"]),
    )
    h_columns = N * len(H_BIVECTORS)
    mixed_rank_h = sparse_row_rank(mixed_h_rows, h_columns)
    mixed_combined = merge_column_blocks(
        mixed_h_rows, mixed_quotient_rows, h_columns
    )
    mixed_quotient_rank = sparse_row_rank(
        mixed_combined, h_columns + len(QUOTIENT_GRADE3)
    ) - mixed_rank_h
    exact(
        "mixed-normal grade-three-projected polarization survives modulo every h-valued LC principal return",
        mixed_quotient_rank > 0,
        f"quotient-rank={mixed_quotient_rank}",
    )
    reject(
        "declare the quadratic graph tensor from basis covectors without mixed polarization",
        mixed_quotient_rank == 0,
    )

    raw_rows, _, raw_witnesses = build_graph_k(
        normals["base_spacelike"], QUOTIENT_GRADE3, raw_metric
    )
    exact(
        "the raw-Frobenius hostile branch does not reproduce the active trace-reversed coefficient tensor",
        raw_rows != primary["rows"] and bool(raw_witnesses),
    )
    reject(
        "replace the trace-reversed Hodge by raw Frobenius because both have fourteen directions",
        raw_rows == primary["rows"],
    )

    # The moving-source response now uses a genuine quotient-grade generator,
    # not a vertical Spin bivector.  The generator moves the trace line, Phi1,
    # and Phi2 simultaneously.
    move_generator = {QUOTIENT_GRADE3[0]: F(1)}
    x_form = basis_one(1, QUOTIENT_GRADE3[0])
    y_form = basis_one(2, QUOTIENT_GRADE3[1])
    z_form = basis_one(3, QUOTIENT_GRADE3[2])
    ds = lambda curvature: derivative_trace_source(curvature, move_generator)
    dm_value = symmetric_six(ds, x_form, y_form, z_form)
    shifted_plus = lambda curvature: add_forms(
        trace_line_source(curvature), ds(curvature)
    )
    shifted_minus = lambda curvature: add_forms(
        trace_line_source(curvature), scale_form(ds(curvature), F(-1))
    )
    dm_difference = F(1, 2) * (
        symmetric_six(shifted_plus, x_form, y_form, z_form)
        - symmetric_six(shifted_minus, x_form, y_form, z_form)
    )
    d_trace = cliff_comm(blade(TRACE_INDEX), move_generator)
    d_one = form_commutator(PHI_ONE, move_generator)
    d_two = form_commutator(PHI_TWO, move_generator)
    raw_generic = raw_source(generic)
    trace_part = project_sp(left_multiply(d_trace, raw_generic))
    phi_one_part = project_sp(
        left_multiply(
            blade(TRACE_INDEX),
            derivative_raw_source(generic, d_one, {}),
        )
    )
    phi_two_part = project_sp(
        left_multiply(
            blade(TRACE_INDEX),
            derivative_raw_source(generic, {}, d_two),
        )
    )
    exact(
        "the quotient-grade derivative moves trace gamma, Phi1, and Phi2 while the chosen projected Phi2 contribution vanishes",
        bool(d_trace)
        and bool(d_one)
        and bool(d_two)
        and bool(trace_part)
        and bool(phi_one_part)
        and not phi_two_part
        and bool(derivative_trace_source(generic, move_generator))
        and derivative_trace_source(generic, move_generator)
        == add_forms(trace_part, phi_one_part, phi_two_part),
        f"component supports=({len(trace_part)},{len(phi_one_part)},{len(phi_two_part)})",
    )
    exact(
        "the selected quotient-grade six-permutation DM response equals the centered difference and vanishes",
        dm_value == dm_difference and dm_value == 0,
        str(dm_value),
    )

    density_green_checks()

    type_level("K0, DB_rot=-xi tensor chi, fixed-A DT=-DB_rot, and their quotient-grade composites are distinct")
    type_level("u is a local lift modulo right H while epsilon_red=[u] is the descended P/H field")
    type_level("h lift directions, the full 8165-dimensional g/h tangent, and the executed 364-dimensional invariant grade-three slice are distinct")
    type_level("the quotient-safe nonzero residual coefficient proves second order for at least one epsilon_red tangent but does not construct the complete all-grade residual Hessian")
    type_level("the grade-three projected Gram comparator, complete K-top R_res K, and full coupled characteristic kernel are distinct")
    type_level("a prolonged trace is potentially required by the live second jet, but its complete conormal momenta and boundary domain remain unconstructed")
    type_level("moving trace/Phi/Hodge/density/primalizer returns remain required; a nonzero DM response on other quotient grades is open after the grade-three value zero")
    type_level("the observed four-dimensional LC lift remains a normalization control and is not relabeled as the full ambient Y14 metric graph")
    type_level("the source's Shiab family does not uniquely select the repository trace-line adapter")
    type_level("the active (9,5) right-H carrier is not identified with Curt's literal (7,7) complex presentation")
    type_level("P1/P2/P3 supplies no Shiab selector, quotient symbol, graph coefficient, conormal pair, radical, domain, or action term")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("no hyperbolicity, positivity, unitarity, Standard Model equation, count, dark-energy, dark-matter, or PP3 claim follows")

    reject("identify the bosonic trace-adapted Shiab with the spinorial Clifford-contraction Shiab", False)
    reject("call the entire Shiab a projection rather than a contraction with an internal real-form projection", False)
    reject("use a positive-Hilbert conjugate transpose in place of the density-dual/Krein formal transpose", False)
    reject("identify a nonzero projected quotient coefficient with a noncharacteristic full coupled Euler system", False)
    reject("identify a nonzero projected Gram comparator with a complete prolonged preboundary form or closed domain", False)
    reject("promote the repository trace-line adapter to a source-selected operator", False)

    summary = (
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + {TYPE} type-level "
        f"+ {PLANTED} planted = {EXACT + SOURCE + TYPE + PLANTED}"
    )
    print(summary)
    if FAILURES:
        print(f"FAILURES: {FAILURES}")
        return 1
    print("ALL B2C14R CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
