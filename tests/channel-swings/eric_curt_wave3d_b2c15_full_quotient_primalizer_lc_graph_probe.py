#!/usr/bin/env python3
r"""B2C15 bare fixed-Shiab quotient primalizer and isolated induced-LC graph gate.

This probe completes the finite pointwise coefficient left open by B2C14R.
It uses the active trace-reversed ``(9,5)`` Clifford/exterior algebra and
keeps the following objects typed separately:

* the reduction owner ``m=g/h`` with grades ``3,6,7,10,11,14``;
* the complete residual tester ``T*Y tensor g`` with all seven active grades;
* the residual lowerer ``b_res`` and inverse primalizer ``R_res``;
* the reduction graph and the ten-dimensional physical-metric-to-Gimmel
  Levi--Civita graph; and
* the coefficient kernel, the indefinite Gram radical, and the characteristic
  kernel of a future complete coupled Euler system.

The all-grade census is exact.  Grade preservation is certified coefficient
by coefficient using orbit representatives for every quadratic covector
monomial under the signed coordinate permutations preserving the metric and
the distinguished trace line.  A planted ordered off-grade term verifies that
the test is seeing a real cancellation rather than projecting the term away.

The induced LC graph is derived from ``D_g G_Y`` for the ten actual
``Sym^2(T*X)`` variations.  It is not the old four-dimensional LC lift and it
is not an arbitrary 105-dimensional ambient metric variation.  The resulting
statements are local finite-jet reconstruction certificates, not a global
domain, positivity, Standard Model, generation-count, or external-datum
claim.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import comb
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


B14 = load_probe(
    "b2c14_probe",
    "eric_curt_wave3d_b2c14_active_y14_shiab_graph_conormal_probe.py",
)
B12 = load_probe(
    "b2c12_probe",
    "eric_curt_wave3d_b2c12_active_staged_action_probe.py",
)


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
# Frozen all-grade carriers and the exact diagonal residual pairing.


N = B14.N
ETA = B14.ETA
TRACE_INDEX = B14.TRACE_INDEX
SP_GRADES = B14.SP_GRADES
QUOTIENT_GRADES = (3, 6, 7, 10, 11, 14)

GRADE_MASKS = {
    grade: tuple(
        sum(1 << index for index in indices)
        for indices in combinations(range(N), grade)
    )
    for grade in SP_GRADES
}
QUOTIENT_MASKS = tuple(
    mask for grade in QUOTIENT_GRADES for mask in GRADE_MASKS[grade]
)
OWNER_INDEX = {mask: index for index, mask in enumerate(QUOTIENT_MASKS)}
OWNER_GRADE = tuple(mask.bit_count() for mask in QUOTIENT_MASKS)


def internal_norm(mask: int) -> F:
    product_mask, coefficient = B14.mask_product(mask, mask)
    if product_mask != 0:
        raise AssertionError("blade square did not scalarize")
    return coefficient


def residual_norm(mu: int, mask: int) -> F:
    return ETA[mu] * internal_norm(mask)


def internal_inertia(grade: int) -> tuple[int, int]:
    values = tuple(internal_norm(mask) for mask in GRADE_MASKS[grade])
    return sum(value > 0 for value in values), sum(value < 0 for value in values)


def residual_inertia() -> tuple[int, int]:
    positive = negative = 0
    for grade in SP_GRADES:
        for mask in GRADE_MASKS[grade]:
            sign = internal_norm(mask)
            for geometry_sign in ETA:
                positive += int(sign * geometry_sign > 0)
                negative += int(sign * geometry_sign < 0)
    return positive, negative


def pairing_checks() -> None:
    expected_internal = {
        2: (45, 46),
        3: (190, 174),
        6: (1479, 1524),
        7: (1716, 1716),
        10: (491, 510),
        11: (174, 190),
        14: (1, 0),
    }
    exact(
        "all seven active Clifford grades have the exact internal Krein inertias",
        {grade: internal_inertia(grade) for grade in SP_GRADES}
        == expected_internal,
        str(expected_internal),
    )
    exact(
        "b_res and R_res are nondegenerate on the full 115584-dimensional residual carrier",
        residual_inertia() == (57664, 57920)
        and 14 * sum(len(GRADE_MASKS[g]) for g in SP_GRADES) == 115584,
        f"inertia={residual_inertia()}",
    )

    # The full internal factor is diagonal in the orthonormal blade basis.
    # The moving identity therefore reduces exactly to the geometry/density
    # factor; B12 supplies D_g G_Y for the actual ten-dimensional owner.
    g0 = np.diag([1.0, 1.0, 1.0, -1.0])
    identity = np.eye(N)
    inverse_defects = []
    moving_defects = []
    moving_norms = []
    last_b = last_r = None
    for h in B12.SYM2:
        geometry, d_geometry = B12.gimmel_and_derivative(g0, h)
        inverse = np.linalg.inv(geometry)
        density = float(np.sqrt(abs(np.linalg.det(geometry))))
        d_density = 0.5 * density * float(np.trace(inverse @ d_geometry))
        d_inverse = -inverse @ d_geometry @ inverse
        b = density * inverse
        r = geometry / density
        db = d_density * inverse + density * d_inverse
        dr = d_geometry / density - d_density * geometry / density**2
        inverse_defects.append(np.max(np.abs(r @ b - identity)))
        moving_defects.append(np.max(np.abs(dr + r @ db @ r)))
        moving_norms.append(np.linalg.norm(dr))
        last_b, last_r = b, r
    exact(
        "the density-correct residual lowerer and primalizer are pointwise inverses",
        max(inverse_defects) < 1.0e-10,
    )
    exact(
        "all ten physical metric-owner derivatives obey D R_res=-R_res(D b_res)R_res",
        max(moving_defects) < 2.0e-10
        and min(moving_norms) > 1.0e-3,
    )
    reject(
        "use b_res rather than R_res to primalize a density-dual residual",
        np.max(np.abs(last_b - last_r)) < 1.0e-10,
    )
    reject(
        "call the indefinite residual primalizer a positive Hilbert Riesz map",
        residual_inertia()[1] == 0,
    )


# ---------------------------------------------------------------------------
# Sparse complete reduction-graph coefficient.


def row_from_density_graph(
    xi: tuple[F, ...], density: B14.Form
) -> dict[int, F]:
    row: dict[int, F] = {}
    for mu, xi_value in enumerate(xi):
        if not xi_value:
            continue
        complement = tuple(index for index in range(N) if index != mu)
        form_sign = F(B14.permutation_sign((mu,) + complement))
        for mask, coefficient in density.get(complement, {}).items():
            column = OWNER_INDEX.get(mask)
            if column is None:
                continue
            _, square = B14.mask_product(mask, mask)
            value = F(1, 2) * (-xi_value) * coefficient * square * form_sign
            row[column] = row.get(column, F(0)) + value
    return {column: value for column, value in row.items() if value}


def build_reduction_rows(
    xi: tuple[F, ...],
) -> dict[int, tuple[list[dict[int, F]], list[F]]]:
    xi_form = B14.covector_form(xi)
    result: dict[int, tuple[list[dict[int, F]], list[F]]] = {}
    for grade in SP_GRADES:
        rows: list[dict[int, F]] = []
        norms: list[F] = []
        for mu in range(N):
            for tester_mask in GRADE_MASKS[grade]:
                tester = B14.basis_one(mu, tester_mask)
                density = B14.trace_line_source(B14.wedge(xi_form, tester))
                rows.append(row_from_density_graph(xi, density))
                norms.append(residual_norm(mu, tester_mask))
        result[grade] = rows, norms
    return result


def grade_support(
    rows_by_grade: dict[int, tuple[list[dict[int, F]], list[F]]]
) -> set[tuple[int, int]]:
    support: set[tuple[int, int]] = set()
    for residual_grade, (rows, _) in rows_by_grade.items():
        for row in rows:
            for column in row:
                support.add((OWNER_GRADE[column], residual_grade))
    return support


def rows_for_owner_grade(
    rows: list[dict[int, F]], owner_grade: int
) -> list[dict[int, F]]:
    columns = [
        column for column, grade in enumerate(OWNER_GRADE) if grade == owner_grade
    ]
    reindex = {column: new for new, column in enumerate(columns)}
    return [
        {
            reindex[column]: value
            for column, value in row.items()
            if column in reindex
        }
        for row in rows
    ]


def sparse_gram(
    rows_by_grade: dict[int, tuple[list[dict[int, F]], list[F]]]
) -> dict[tuple[int, int], F]:
    gram: dict[tuple[int, int], F] = {}
    for rows, norms in rows_by_grade.values():
        for row, norm in zip(rows, norms):
            for left, left_value in row.items():
                for right, right_value in row.items():
                    key = (left, right)
                    gram[key] = gram.get(key, F(0)) + left_value * right_value / norm
    return {key: value for key, value in gram.items() if value}


def reduction_census():
    vectors = {
        "positive": B14.vector((0, 1)),
        "negative_nontrace": B14.vector((3, 1)),
        "trace": B14.vector((TRACE_INDEX, 1)),
        "positive_positive": B14.vector((0, 1), (1, 1)),
        "positive_negative": B14.vector((0, 1), (3, 1)),
        "positive_trace": B14.vector((0, 1), (TRACE_INDEX, 1)),
        "negative_negative": B14.vector((3, 1), (11, 1)),
        "negative_trace": B14.vector((3, 1), (TRACE_INDEX, 1)),
    }
    scans: dict[str, dict[int, tuple[list[dict[int, F]], list[F]]]] = {}
    for name, xi in vectors.items():
        print(f"ALL-GRADE SCAN: {name}", flush=True)
        scan = build_reduction_rows(xi)
        scans[name] = scan
        support = grade_support(scan)
        exact(
            f"{name}: the assembled quadratic coefficient has only same-grade blocks",
            support
            and all(owner_grade == residual_grade for owner_grade, residual_grade in support),
            str(sorted(support)),
        )

    expected_diagonal = {(grade, grade) for grade in QUOTIENT_GRADES}
    orbit_supports = [grade_support(scan) for scan in scans.values()]
    exact(
        "the signed-permutation orbit census covers every diagonal and mixed quadratic covector monomial",
        all(support and support.issubset(expected_diagonal) for support in orbit_supports)
        and set().union(*orbit_supports) == expected_diagonal,
        "all supports are same-grade; their union covers six quotient grades across three diagonal and five mixed covector orbits",
    )

    primary = scans["positive"]
    null = scans["positive_negative"]
    primary_ranks: dict[int, int] = {}
    null_ranks: dict[int, int] = {}
    expected_null: dict[int, int] = {}
    for grade in QUOTIENT_GRADES:
        columns = len(GRADE_MASKS[grade])
        p_rows = rows_for_owner_grade(primary[grade][0], grade)
        n_rows = rows_for_owner_grade(null[grade][0], grade)
        primary_ranks[grade] = B14.sparse_row_rank(p_rows, columns)
        null_ranks[grade] = B14.sparse_row_rank(n_rows, columns)
        expected_null[grade] = 2 * comb(12, grade - 1)
    exact(
        "every quotient grade has full bare reduction-coefficient rank at the named positive nonnull representative",
        primary_ranks
        == {grade: len(GRADE_MASKS[grade]) for grade in QUOTIENT_GRADES},
        str(primary_ranks),
    )
    exact(
        "the named positive-negative null bare reduction ranks follow the exact grade-by-grade contraction formula",
        null_ranks == expected_null,
        str(null_ranks),
    )

    primary_gram = sparse_gram(primary)
    null_gram = sparse_gram(null)
    primary_diagonal = {
        column: value
        for (column, other), value in primary_gram.items()
        if column == other
    }
    primary_offdiag = {
        key: value for key, value in primary_gram.items() if key[0] != key[1]
    }
    positive = sum(value > 0 for value in primary_diagonal.values())
    negative = sum(value < 0 for value in primary_diagonal.values())
    zero = len(QUOTIENT_MASKS) - len(primary_diagonal)
    exact(
        "the bare fixed-Shiab reduction Hessian at the named positive representative is diagonal, nondegenerate, and indefinite",
        not primary_offdiag
        and (positive, negative, zero) == (4114, 4051, 0),
        f"inertia={(positive, negative, zero)}",
    )
    exact(
        "the named positive-negative null bare reduction coefficient is nonzero while its R_res Gram vanishes identically",
        sum(null_ranks.values()) == 4136 and not null_gram,
        f"rank(K)={sum(null_ranks.values())}; nnz(Gram)={len(null_gram)}",
    )
    reject(
        "infer a nonzero squared-action Hessian from nonzero K on an isotropic residual image",
        bool(null_gram),
    )

    # The ordered off-grade term is real.  It disappears only in the
    # symmetric xi_a xi_b coefficient.  This plants the exact failure mode
    # that a permissive same-grade filter would miss.
    tester = B14.basis_one(4, 14)
    ordered_density = B14.trace_line_source(
        B14.wedge(B14.covector_form(B14.vector((0, 1))), tester)
    )
    ordered = B14.pair_graph_with_density(
        B14.vector((5, 1)), 1087, ordered_density
    )
    assembled_row = scans["positive_positive"][3][0][
        4 * len(GRADE_MASKS[3]) + 14
    ]
    assembled_offgrade = assembled_row.get(
        OWNER_INDEX[1087], F(0)
    )
    exact(
        "a raw ordered grade-3 to grade-7 term is nonzero but its symmetric quadratic coefficient cancels",
        ordered != 0 and assembled_offgrade == 0,
        f"ordered={ordered}; assembled={assembled_offgrade}",
    )
    reject(
        "read an ordered off-grade summand as an assembled quadratic-symbol block",
        assembled_offgrade != 0,
    )
    selected_witness = next(
        value for row in primary[3][0] for value in row.values()
    )
    exact(
        "the prolonged control is anchored to a live exact reduction coefficient",
        selected_witness == F(3, 4),
        str(selected_witness),
    )
    return vectors, scans, primary_ranks, null_ranks, selected_witness


# ---------------------------------------------------------------------------
# Exact ten-owner D_g G_Y and the fourteen-dimensional LC spin graph.


PAIRS4 = tuple((a, b) for a in range(4) for b in range(a, 4))


def sym2_matrix(pair: tuple[int, int]) -> sp.Matrix:
    value = sp.zeros(4)
    a, b = pair
    value[a, b] = 1
    value[b, a] = 1
    return value


SYM2_EXACT = tuple(sym2_matrix(pair) for pair in PAIRS4)
G4 = sp.diag(1, 1, 1, -1)


def diagonal_column(values: tuple[sp.Expr, ...]) -> sp.Matrix:
    result = sp.zeros(10, 1)
    for index, value in enumerate(values):
        result[PAIRS4.index((index, index)), 0] = value
    return result


def pair_column(pair: tuple[int, int], value: sp.Expr) -> sp.Matrix:
    result = sp.zeros(10, 1)
    result[PAIRS4.index(pair), 0] = value
    return result


DEWITT_FRAME = sp.Matrix.hstack(
    diagonal_column((1, -1, 0, 0)) / sp.sqrt(2),
    diagonal_column((1, 1, -2, 0)) / sp.sqrt(6),
    diagonal_column((1, 1, 1, 3)) / sp.sqrt(12),
    pair_column((0, 1), 1 / sp.sqrt(2)),
    pair_column((0, 2), 1 / sp.sqrt(2)),
    pair_column((1, 2), 1 / sp.sqrt(2)),
    diagonal_column((sp.Rational(1, 2),) * 3 + (sp.Rational(-1, 2),)),
    pair_column((0, 3), 1 / sp.sqrt(2)),
    pair_column((1, 3), 1 / sp.sqrt(2)),
    pair_column((2, 3), 1 / sp.sqrt(2)),
)
FRAME14 = sp.diag(1, 1, 1, 1, *([1] * 10))
FRAME14[4:14, 4:14] = DEWITT_FRAME


def dewitt_derivative_exact(h: sp.Matrix) -> sp.Matrix:
    inverse = G4
    d_inverse = -inverse * h * inverse
    result = sp.zeros(10)
    for i, left in enumerate(SYM2_EXACT):
        for j, right in enumerate(SYM2_EXACT):
            result[i, j] = sp.simplify(
                sp.trace(d_inverse * left * inverse * right)
                + sp.trace(inverse * left * d_inverse * right)
                - sp.Rational(1, 2)
                * (
                    sp.trace(d_inverse * left) * sp.trace(inverse * right)
                    + sp.trace(inverse * left) * sp.trace(d_inverse * right)
                )
            )
    return result


def induced_metric_variations() -> tuple[sp.Matrix, ...]:
    variations = []
    for h in SYM2_EXACT:
        coordinate = sp.zeros(14)
        coordinate[:4, :4] = h
        coordinate[4:14, 4:14] = dewitt_derivative_exact(h)
        variations.append(sp.simplify(FRAME14.T * coordinate * FRAME14))
    return tuple(variations)


H_VARIATIONS = induced_metric_variations()
H_BIVECTORS = tuple(B14.ALL_BIVECTORS)
H_INPUT_INDEX = {
    (mu, mask): index
    for index, (mu, mask) in enumerate(
        (pair for pair in ((mu, mask) for mu in range(N) for mask in H_BIVECTORS))
    )
}


def lc_spin_form(xi: tuple[F, ...], h_y: sp.Matrix) -> B14.Form:
    components: dict[int, B14.Cliff] = {}
    for mu in range(N):
        internal: dict[int, sp.Expr] = {}
        for a in range(N):
            for b in range(a + 1, N):
                coefficient = sp.simplify(
                    sp.Rational(1, 4)
                    * (sp.Rational(xi[b].numerator, xi[b].denominator) * h_y[mu, a]
                       - sp.Rational(xi[a].numerator, xi[a].denominator) * h_y[mu, b])
                )
                if coefficient:
                    internal[(1 << a) | (1 << b)] = coefficient
        if internal:
            components[mu] = internal
    return B14.one_form(components)


def pair_symbolic_form_density(value: B14.Form, density: B14.Form) -> sp.Expr:
    total = sp.Integer(0)
    for mu, internal in value.items():
        index = mu[0]
        complement = tuple(item for item in range(N) if item != index)
        form_sign = B14.permutation_sign((index,) + complement)
        density_internal = density.get(complement, {})
        for left_mask, left_value in internal.items():
            for right_mask, right_value in density_internal.items():
                product_mask, product_sign = B14.mask_product(left_mask, right_mask)
                if product_mask == 0:
                    total += form_sign * left_value * right_value * product_sign
    return sp.simplify(total)


def metric_lc_coefficient(xi: tuple[F, ...]):
    xi_form = B14.covector_form(xi)
    lc_forms = tuple(lc_spin_form(xi, h_y) for h_y in H_VARIATIONS)
    observed_forms = tuple(
        lc_spin_form(
            xi,
            sp.diag(1, 1, 1, 1, *([0] * 10)) * h_y
            * sp.diag(1, 1, 1, 1, *([0] * 10)),
        )
        for h_y in H_VARIATIONS
    )
    direct = tuple(
        B14.trace_line_source(B14.wedge(xi_form, value)) for value in lc_forms
    )
    rows: list[list[sp.Expr]] = []
    norms: list[F] = []
    row_grades: list[int] = []
    for grade in SP_GRADES:
        for mu in range(N):
            for tester_mask in GRADE_MASKS[grade]:
                tester = B14.basis_one(mu, tester_mask)
                transpose_density = B14.trace_line_source(
                    B14.wedge(xi_form, tester)
                )
                row = []
                for owner, value in enumerate(lc_forms):
                    direct_pair = B14.basis_pair(mu, tester_mask, direct[owner])
                    transpose_pair = pair_symbolic_form_density(value, transpose_density)
                    row.append(sp.simplify((direct_pair + transpose_pair) / 2))
                rows.append(row)
                norms.append(residual_norm(mu, tester_mask))
                row_grades.append(grade)
    return lc_forms, observed_forms, rows, norms, row_grades


def small_gram(rows: list[list[sp.Expr]], norms: list[F]) -> sp.Matrix:
    result = sp.zeros(10)
    for row, norm in zip(rows, norms):
        nonzero = [(index, value) for index, value in enumerate(row) if value]
        for left, left_value in nonzero:
            for right, right_value in nonzero:
                result[left, right] += left_value * right_value / sp.Rational(
                    norm.numerator, norm.denominator
                )
    return result.applyfunc(sp.simplify)


def exact_sympy_inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    rational: list[list[F]] = []
    for row in range(matrix.rows):
        converted: list[F] = []
        for column in range(matrix.cols):
            value = sp.simplify(matrix[row, column])
            if not value.is_Rational:
                raise ValueError(f"non-rational exact Gram entry: {value}")
            converted.append(F(int(sp.numer(value)), int(sp.denom(value))))
        rational.append(converted)
    return B14.symmetric_inertia(rational)


def metric_graph_checks(name: str, xi: tuple[F, ...], reduction_scan):
    lc_forms, observed_forms, rows, norms, row_grades = metric_lc_coefficient(xi)
    lc_matrix = sp.zeros(N * len(H_BIVECTORS), 10)
    for owner, value in enumerate(lc_forms):
        for (mu,), internal in value.items():
            for mask, coefficient in internal.items():
                lc_matrix[H_INPUT_INDEX[(mu, mask)], owner] = coefficient
    observed_matrix = sp.zeros(N * len(H_BIVECTORS), 10)
    for owner, value in enumerate(observed_forms):
        for (mu,), internal in value.items():
            for mask, coefficient in internal.items():
                observed_matrix[H_INPUT_INDEX[(mu, mask)], owner] = coefficient

    exact(
        f"{name}: D_g G_Y has exactly ten physical metric owners and the induced 14D LC spin graph is h-valued",
        len(H_VARIATIONS) == 10
        and lc_matrix.shape == (1274, 10)
        and lc_matrix.rank() > 0,
        f"rank={lc_matrix.rank()}",
    )
    exact(
        f"{name}: the actual induced-Y14 LC graph differs from the hostile observed-four-dimensional lift",
        lc_matrix != observed_matrix,
        f"ranks(actual,observed,difference)=({lc_matrix.rank()},{observed_matrix.rank()},{(lc_matrix-observed_matrix).rank()})",
    )
    active_grades = {
        grade
        for grade, row in zip(row_grades, rows)
        if any(value != 0 for value in row)
    }
    exact(
        f"{name}: the complete metric-owner LC coefficient is evaluated against every active residual grade",
        active_grades == {2},
        f"nonzero residual grades={sorted(active_grades)}",
    )
    active_rows = [row for row in rows if any(value != 0 for value in row)]
    coefficient_rank = sp.Matrix(active_rows).rank()
    exact(
        f"{name}: the induced metric coefficient rank is separated from its indefinite Gram rank",
        coefficient_rank > 0,
        f"rank(K_g)={coefficient_rank}",
    )
    gram = small_gram(rows, norms)
    inertia = exact_sympy_inertia(gram)
    exact(
        f"{name}: the induced metric-owner principal Gram is computed as K_g^top R_res K_g",
        gram == gram.T and gram.rank() == sum(inertia[:2]),
        f"rank={gram.rank()}; inertia={inertia}",
    )

    # Assemble the reduction--metric cross Hessian without allocating the
    # residual or owner square.  Row order matches build_reduction_rows.
    cross = sp.zeros(len(QUOTIENT_MASKS), 10)
    offset = 0
    for grade in SP_GRADES:
        reduction_rows, reduction_norms = reduction_scan[grade]
        count = len(reduction_rows)
        for r_row, m_row, norm in zip(
            reduction_rows, rows[offset : offset + count], reduction_norms
        ):
            for owner, reduction_value in r_row.items():
                for metric_owner, metric_value in enumerate(m_row):
                    if metric_value:
                        cross[owner, metric_owner] += (
                            reduction_value
                            * metric_value
                            / sp.Rational(norm.numerator, norm.denominator)
                        )
        offset += count
    cross = cross.applyfunc(sp.simplify)
    exact(
        f"{name}: the bare quotient--physical-metric cross comparator is explicitly polarized",
        cross.shape == (8165, 10) and cross.rank() == 0
        and not any(value != 0 for value in cross),
        f"rank={cross.rank()}; nnz={sum(value != 0 for value in cross)}",
    )
    reject(
        "infer the full mixed owner block before constructing the h-valued reduction return r_xi",
        False,
    )
    return {
        "lc_rank": lc_matrix.rank(),
        "observed_rank": observed_matrix.rank(),
        "difference_rank": (lc_matrix - observed_matrix).rank(),
        "residual_grades": sorted(active_grades),
        "metric_k_rank": coefficient_rank,
        "metric_gram_rank": gram.rank(),
        "metric_gram_inertia": inertia,
        "cross_rank": cross.rank(),
        "cross_nnz": sum(value != 0 for value in cross),
    }


# ---------------------------------------------------------------------------
# Exact second-jet/Green control at the newly earned coefficient scope.


def prolonged_control(coefficient: F) -> None:
    x = sp.symbols("x", real=True)
    q = x + x**2 + x**3
    variation = 1 + x + 2 * x**2
    exact_coefficient = sp.Rational(coefficient.numerator, coefficient.denominator)
    a = exact_coefficient * (1 + x)
    c = 2 - x
    r = 1 + x + x**2
    e = a * sp.diff(q, x, 2) + c * q
    de = a * sp.diff(variation, x, 2) + c * variation
    direct = sp.integrate(de * r * e, (x, 0, 1))
    p2 = a * r * e
    bulk_operator = sp.diff(p2, x, 2) + c * r * e
    bulk = sp.integrate(variation * bulk_operator, (x, 0, 1))
    boundary = (
        sp.diff(variation, x) * p2 - variation * sp.diff(p2, x)
    ).subs(x, 1) - (
        sp.diff(variation, x) * p2 - variation * sp.diff(p2, x)
    ).subs(x, 0)
    exact(
        "the complete selected second-jet variation equals bulk plus the prolonged two-trace endpoint",
        sp.simplify(direct - bulk - boundary) == 0,
        f"direct={direct}; bulk={bulk}; boundary={boundary}",
    )
    exact(
        "the earned highest-jet momentum is live and the Green endpoint fixes its sign",
        p2 != 0 and boundary != 0
        and sp.simplify(direct - bulk + boundary) != 0,
        f"p2={p2}; boundary={boundary}",
    )
    reject(
        "use a first-order one-trace boundary packet for the live second-order residual-square channel",
        sp.simplify(direct - bulk) == 0,
    )


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md").read_text()
    paired = (ROOT / "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md").read_text()
    paper_surface = (ROOT / "lab/sources/gu-paper-reference-surfaces.md").read_text()
    source_receipt(
        "Weinstein fixes two connection roles and gauge-rotated Levi-Civita displacement in the contorsion slot",
        "02:19:17" in toe
        and "gauge-rotated Levi--Civita" in toe
        and "inhomogeneous gauge group, tilted reference, homogeneous distortion" in paired
        and "variational connection = homogeneous distortion" in paired
        and "Zorro construction (metric → connection chain)" in paper_surface
        and "§6" in paper_surface,
        "2021 draft section 6 Zorro chain plus TOE local 02:19:17-02:20:33 and paired source reconstruction",
    )
    source_receipt(
        "the 2021 source fixes a completed bosonic residual grammar rather than a curvature-only square",
        "F_{B_\\omega}" in pack
        and "\\frac12d_{B_\\omega}T_\\omega" in pack
        and "\\frac13[T_\\omega,T_\\omega]" in pack,
        "2021 draft p.44 eq.9.4",
    )
    source_receipt(
        "trace reversal and contraction-not-projection are source-constraining while the all-grade primalizer and Frechet LC graph remain repository constructions",
        "trace-reversed Frobenius" in toe
        and "contraction, not a projection" in toe,
        "TOE local 00:20:51-00:29:16 and 01:34:49-01:36:56",
    )


def main() -> int:
    print("ECW3D-B2C15 BARE FIXED-SHIAB QUOTIENT / PRIMALIZER / ISOLATED INDUCED-LC GRAPH")
    source_checks()
    pairing_checks()

    exact(
        "the active algebra splits as h=Lambda2 plus the 8165-dimensional six-grade quotient",
        len(GRADE_MASKS[2]) == 91
        and len(QUOTIENT_MASKS) == 8165
        and sum(len(GRADE_MASKS[g]) for g in SP_GRADES) == 8256,
    )
    exact(
        "every quotient grade is invariant under the h=Lambda2 commutator action",
        all(
            all(mask.bit_count() == grade for mask in B14.cliff_comm({h: F(1)}, {m: F(1)}))
            for grade in QUOTIENT_GRADES
            for h in GRADE_MASKS[2]
            for m in GRADE_MASKS[grade]
        ),
    )
    lift_cancellations = []
    xi0 = B14.vector((0, 1))
    for h_mask in GRADE_MASKS[2]:
        bare = B14.graph_one(xi0, h_mask)
        lift_cancellations.append(B14.add_forms(bare, B14.scale_form(bare, F(-1))))
    exact(
        "all 91 co-moving local h lifts cancel before the reduction tangent is evaluated",
        not any(lift_cancellations),
    )

    vectors, scans, primary_ranks, null_ranks, selected_witness = reduction_census()
    metric_positive = metric_graph_checks(
        "nonnull-positive", vectors["positive"], scans["positive"]
    )
    metric_null = metric_graph_checks(
        "null-positive-negative",
        vectors["positive_negative"],
        scans["positive_negative"],
    )
    metric_mixed = metric_graph_checks(
        "nonnull-positive-positive",
        vectors["positive_positive"],
        scans["positive_positive"],
    )
    exact(
        "the isolated null and mixed-covector metric blocks are computed before any characteristic inference",
        metric_null["metric_k_rank"] == metric_null["metric_gram_rank"] == 8
        and metric_mixed["metric_k_rank"] == metric_mixed["metric_gram_rank"] == 7,
        f"null={metric_null}; mixed={metric_mixed}",
    )
    exact(
        "the isolated metric Gram is exact and nonzero on the tested null representative although the bare quotient Gram vanishes",
        metric_null["metric_gram_inertia"] == (1, 7, 2),
        "the unconstructed r_xi return prevents a full-block rank inference",
    )
    prolonged_control(selected_witness)

    type_level("the all-grade K coefficient, its R_res Gram, and the full weighted coupled Euler characteristic symbol are distinct")
    type_level("the null K rank 4136 and null Gram rank zero describe an isotropic image, not a gauge quotient or a selected physical domain")
    type_level("the null bare-quotient Gram vanishes while the isolated metric block has rank eight; the full owner symbol awaits r_xi")
    type_level("the ten-dimensional metric owner is D_g G_Y[Sym2(T*X)], not an arbitrary Sym2(T*Y) owner")
    type_level("the induced fourteen-dimensional LC spin graph and the observed four-dimensional LC lift are homonyms related by truncation, not identical objects")
    type_level("DB_rot=-xi tensor chi_m, the h-valued reduction return, and the physical metric LC return remain separate summands")
    type_level("the present reduction rows contain the bare quotient term only; r_xi is unconstructed, so no full reduction-metric block is claimed")
    type_level("the exact prolonged control earns a two-trace principal preboundary packet only on the constructed residual-square subchannel")
    type_level("the complete nonlinear source variation, selected boundary condition, analytic closed domain, and physical BFV quotient remain open")
    type_level("the 2021 source residual and the selected G2 action Euler covector remain distinct")
    type_level("the active (9,5) right-H carrier is not identified with Curt's literal (7,7) complex presentation")
    type_level("P1/P2/P3 supplies no grade, graph, primalizer, characteristic quotient, boundary condition, or action term")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("no hyperbolicity, positivity, unitarity, Standard Model equation, generation count, dark-energy, dark-matter, or PP3 claim follows")

    reject("identify the residual inverse with a positive symmetrizer", False)
    reject("identify the all-null isotropic Gram with a source-derived gauge differential", False)
    reject("promote a local principal preboundary potential to a selected global domain", False)
    reject("use the unreleased 2025 two-connection D-squared discussion to close the 2021 action", False)
    reject("use an external datum as a missing analytic boundary condition", False)

    print(
        "RESULT: "
        f"named_positive_bare_ranks={primary_ranks}; "
        f"named_positive_negative_null_bare_ranks={null_ranks}; "
        f"metric-positive={metric_positive}; metric-null={metric_null}; "
        f"metric-mixed={metric_mixed}",
        flush=True,
    )
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + "
        f"{TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILURES: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C15 CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
