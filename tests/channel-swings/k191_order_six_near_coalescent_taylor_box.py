#!/usr/bin/env python3
"""K191 outward near-coalescent Taylor boxes for K186 regularizers.

For a positive base argument ``x`` write

    F_x(y) = x K_1(x(1+y)).

After row and column Newton transforms, the K186 regularizer is exactly

    R_m = det([r_0,...,r_i][c_0,...,c_j] F_x(w+r+c))
          * product_(a,b) (1+w+r_a+c_b).

The common radial scale has disappeared before interval evaluation.  This
module expands the complete divided-difference matrix in a Taylor polynomial,
bounds its tail from complete monotonicity of K_1, and certifies a finite
radial/gap-ratio neighbourhood of the K190 coalescent spine with Arb.

The certificate is deliberately local in relative row/column spread.  It does
not cover arbitrary gap ratios or serialize the Duffy/Jacobi cubature error.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

import sympy as sp
from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K186_PATH = ROOT / "tests/channel-swings/k186_order_six_bessel_vandermonde.py"
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
K190_PATH = ROOT / "tests/channel-swings/k190_order_six_coalescent_scaled_jet.py"
K190_MANIFEST = ROOT / "lab/process/k190-order-six-coalescent-scaled-jet-wave.json"
OUTPUT = ROOT / "lab/process/k191-order-six-near-coalescent-taylor-box-wave.json"

ARB_DIGITS = 120
TAYLOR_ORDER = 16
RADIAL_SUBDIVISION_CANDIDATES = (8, 16, 32, 64, 128, 256)
GAP_RELATIVE_RADIUS = Fraction(1, 512)
RADIAL_LOW_POWER = 200
RADIAL_HIGH_POWER = 2

ctx.dps = ARB_DIGITS
ctx.threads = 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K186 = load_module("k186", K186_PATH)
K190 = load_module("k190", K190_PATH)

W, R0, R1, C0, C1 = sp.symbols("w r0 r1 c0 c1")
VARIABLES = (W, R0, R1, C0, C1)


def determinant(matrix: list[list[Any]]):
    if len(matrix) == 1:
        return matrix[0][0]
    return K190.determinant(matrix)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def rational_ball(value: Fraction) -> arb:
    return arb(fraction_text(value))


def interval_from_bounds(lower: Fraction, upper: Fraction) -> arb:
    midpoint = (lower + upper) / 2
    radius = (upper - lower) / 2
    return arb(fraction_text(midpoint), fraction_text(radius))


def row_nodes(size: int) -> tuple[sp.Expr, ...]:
    if size == 2:
        return (R0, sp.Integer(0))
    if size == 3:
        return (R0, R1, sp.Integer(0))
    raise ValueError("K191 admits only sizes two and three")


def column_nodes(size: int) -> tuple[sp.Expr, ...]:
    if size == 2:
        return (C0, sp.Integer(0))
    if size == 3:
        return (C0, C1, sp.Integer(0))
    raise ValueError("K191 admits only sizes two and three")


@lru_cache(maxsize=None)
def monomial_dd_matrix(power: int, size: int) -> tuple[tuple[sp.Expr, ...], ...]:
    """Exact sequential row/column divided differences of z**power."""

    rows = row_nodes(size)
    columns = column_nodes(size)
    matrix = [
        [sp.expand((W + rows[i] + columns[j]) ** power) for j in range(size)]
        for i in range(size)
    ]
    for order in range(1, size):
        for row in range(size - 1, order - 1, -1):
            divisor = rows[row] - rows[row - order]
            for column in range(size):
                matrix[row][column] = sp.cancel(
                    (matrix[row][column] - matrix[row - 1][column]) / divisor
                )
    for order in range(1, size):
        for column in range(size - 1, order - 1, -1):
            divisor = columns[column] - columns[column - order]
            for row in range(size):
                matrix[row][column] = sp.cancel(
                    (matrix[row][column] - matrix[row][column - 1]) / divisor
                )
    return tuple(tuple(sp.expand(value) for value in row) for row in matrix)


@lru_cache(maxsize=None)
def monomial_dd_bounds(
    power: int, size: int, radial_width_bound: Fraction
) -> tuple[tuple[tuple[Fraction, Fraction], ...], ...]:
    """Range each nonnegative-coefficient monomial DD on the admitted box."""

    matrix = monomial_dd_matrix(power, size)
    upper_substitution = {
        W: sp.Rational(radial_width_bound.numerator, radial_width_bound.denominator),
        R0: sp.Rational(GAP_RELATIVE_RADIUS.numerator, GAP_RELATIVE_RADIUS.denominator),
        R1: sp.Rational(GAP_RELATIVE_RADIUS.numerator, GAP_RELATIVE_RADIUS.denominator),
        C0: sp.Rational(GAP_RELATIVE_RADIUS.numerator, GAP_RELATIVE_RADIUS.denominator),
        C1: sp.Rational(GAP_RELATIVE_RADIUS.numerator, GAP_RELATIVE_RADIUS.denominator),
    }
    zero_substitution = {variable: 0 for variable in VARIABLES}
    result = []
    for row in matrix:
        result_row = []
        for value in row:
            polynomial = sp.Poly(value, *VARIABLES)
            if any(coefficient < 0 for coefficient in polynomial.coeffs()):
                raise AssertionError("monomial divided difference lost coefficient positivity")
            lower = sp.Rational(value.subs(zero_substitution))
            upper = sp.Rational(value.subs(upper_substitution))
            result_row.append(
                (
                    Fraction(int(lower.p), int(lower.q)),
                    Fraction(int(upper.p), int(upper.q)),
                )
            )
        result.append(tuple(result_row))
    return tuple(result)


def bessel_k_cache(x: arb, maximum_order: int) -> tuple[arb, ...]:
    return tuple(x.bessel_k(order) for order in range(maximum_order + 1))


def scaled_taylor_coefficients(x: arb, maximum_order: int) -> tuple[arb, ...]:
    """Coefficients of F_x(y)=x*K1(x*(1+y)) about y=0."""

    bessel = bessel_k_cache(x, maximum_order + 1)
    coefficients = []
    for order in range(maximum_order + 1):
        derivative_abs = arb(0)
        for index in range(order + 1):
            bessel_order = abs(1 - order + 2 * index)
            derivative_abs += math.comb(order, index) * bessel[bessel_order]
        derivative_abs *= arb(2) ** (-order)
        coefficient = x ** (order + 1) * derivative_abs / math.factorial(order)
        if order % 2:
            coefficient = -coefficient
        if (order % 2 == 0 and not coefficient.lower() > 0) or (
            order % 2 == 1 and not coefficient.upper() < 0
        ):
            raise AssertionError(f"Taylor coefficient sign lost at order {order}")
        coefficients.append(coefficient)
    return tuple(coefficients)


def dd_entry_enclosure(
    coefficients: tuple[arb, ...], size: int, row: int, column: int,
    radial_width_bound: Fraction,
) -> tuple[arb, arb]:
    """Enclose H_x=F_x-(1+y)^-1 in divided-difference coordinates."""

    polynomial = arb(0)
    for power in range(row + column, TAYLOR_ORDER + 1):
        lower, upper = monomial_dd_bounds(
            power, size, radial_width_bound
        )[row][column]
        cauchy_coefficient = arb(-1 if power % 2 else 1)
        polynomial += (coefficients[power] - cauchy_coefficient) * interval_from_bounds(lower, upper)

    derivative_order = row + column
    maximum_argument = radial_width_bound + 2 * GAP_RELATIVE_RADIUS
    combinatorial = Fraction(
        math.factorial(TAYLOR_ORDER + 1),
        math.factorial(TAYLOR_ORDER + 1 - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (abs(coefficients[TAYLOR_ORDER + 1]).upper() + 1)
        * rational_ball(combinatorial)
        * rational_ball(maximum_argument) ** (TAYLOR_ORDER + 1 - derivative_order)
    ).upper()
    return polynomial, tail


@lru_cache(maxsize=None)
def cauchy_dd_matrix(size: int) -> tuple[tuple[sp.Expr, ...], ...]:
    """Exact row/column DD matrix of G(y)=(1+y)^-1."""

    rows = row_nodes(size)
    columns = column_nodes(size)
    matrix = [
        [1 / (1 + W + rows[i] + columns[j]) for j in range(size)]
        for i in range(size)
    ]
    for order in range(1, size):
        for row in range(size - 1, order - 1, -1):
            divisor = rows[row] - rows[row - order]
            for column in range(size):
                matrix[row][column] = sp.factor(
                    (matrix[row][column] - matrix[row - 1][column]) / divisor
                )
    for order in range(1, size):
        for column in range(size - 1, order - 1, -1):
            divisor = columns[column] - columns[column - order]
            for row in range(size):
                matrix[row][column] = sp.factor(
                    (matrix[row][column] - matrix[row][column - 1]) / divisor
                )
    return tuple(tuple(value for value in row) for row in matrix)


def evaluate_sympy_interval(expression: sp.Expr, values: dict[sp.Symbol, arb]) -> arb:
    if expression.is_Number:
        return arb(str(expression))
    if expression.is_Symbol:
        return values[expression]
    if expression.is_Add:
        total = arb(0)
        for argument in expression.args:
            total += evaluate_sympy_interval(argument, values)
        return total
    if expression.is_Mul:
        total = arb(1)
        for argument in expression.args:
            total *= evaluate_sympy_interval(argument, values)
        return total
    if expression.is_Pow:
        base, exponent = expression.args
        if not exponent.is_Integer:
            raise ValueError("only integer powers occur in K191 Cauchy coefficients")
        return evaluate_sympy_interval(base, values) ** int(exponent)
    raise TypeError(f"unsupported SymPy node {type(expression).__name__}")


@lru_cache(maxsize=None)
def cauchy_linear_coefficients(size: int) -> tuple[tuple[sp.Expr, ...], ...]:
    """Return Q times the cofactor matrix of the exact Cauchy DD matrix."""

    matrix = sp.Matrix(cauchy_dd_matrix(size))
    rows = row_nodes(size)
    columns = column_nodes(size)
    product = sp.prod(1 + W + row + column for row in rows for column in columns)
    result = []
    for row in range(size):
        result_row = []
        for column in range(size):
            minor = matrix.minor_submatrix(row, column).det()
            result_row.append(sp.factor(product * (-1) ** (row + column) * minor))
        result.append(tuple(result_row))
    return tuple(result)


def determinant_residual_radius(
    size: int, residual_bounds: list[list[arb]], radial_width: Fraction
) -> arb:
    """Bound Q*(det(A+H)-det(A)), retaining all linear cofactors."""

    rows = row_nodes(size)
    columns = column_nodes(size)
    interval_values = {
        W: interval_from_bounds(Fraction(0), radial_width),
        R0: interval_from_bounds(Fraction(0), GAP_RELATIVE_RADIUS),
        R1: interval_from_bounds(Fraction(0), GAP_RELATIVE_RADIUS),
        C0: interval_from_bounds(Fraction(0), GAP_RELATIVE_RADIUS),
        C1: interval_from_bounds(Fraction(0), GAP_RELATIVE_RADIUS),
    }
    cauchy = cauchy_dd_matrix(size)
    product_upper = Fraction(1)
    for row in rows:
        for column in columns:
            row_upper = GAP_RELATIVE_RADIUS if row != 0 else Fraction(0)
            column_upper = GAP_RELATIVE_RADIUS if column != 0 else Fraction(0)
            product_upper *= 1 + radial_width + row_upper + column_upper
    q_upper = rational_ball(product_upper)

    radius = arb(0)
    cauchy_intervals = [
        [evaluate_sympy_interval(value, interval_values) for value in row]
        for row in cauchy
    ]
    # Linear H terms use the full Cauchy cofactor before absolute bounding;
    # this retains the determinant cancellation that the K189 route lacked.
    for row in range(size):
        for column in range(size):
            minor = [
                [
                    cauchy_intervals[i][j]
                    for j in range(size)
                    if j != column
                ]
                for i in range(size)
                if i != row
            ]
            coefficient = (q_upper * determinant(minor)).abs_upper()
            radius += coefficient * residual_bounds[row][column]

    if size == 2:
        radius += q_upper * (
            residual_bounds[0][0] * residual_bounds[1][1]
            + residual_bounds[0][1] * residual_bounds[1][0]
        )
        return radius.upper()

    # Quadratic H terms leave one exact Cauchy entry; cubic terms are det(H).
    for permutation in itertools.permutations(range(size)):
        for selected_rows in itertools.combinations(range(size), 2):
            selected = set(selected_rows)
            term = q_upper
            for row, column in enumerate(permutation):
                if row in selected:
                    term *= residual_bounds[row][column]
                else:
                    term *= cauchy_intervals[row][column].abs_upper()
            radius += term
        cubic = q_upper
        for row, column in enumerate(permutation):
            cubic *= residual_bounds[row][column]
        radius += cubic
    return radius.upper()


def cell_certificate(
    base: Fraction, upper: Fraction, size: int, radial_width_bound: Fraction
) -> dict[str, Any]:
    x = rational_ball(base)
    coefficients = scaled_taylor_coefficients(x, TAYLOR_ORDER + 1)
    residual_matrix = []
    tails = []
    for row in range(size):
        matrix_row = []
        tail_row = []
        for column in range(size):
            polynomial, tail = dd_entry_enclosure(
                coefficients, size, row, column, radial_width_bound
            )
            matrix_row.append(polynomial + arb(0, tail))
            tail_row.append(tail)
        residual_matrix.append(matrix_row)
        tails.append(tail_row)

    residual_bounds = [
        [value.abs_upper() for value in row] for row in residual_matrix
    ]
    radial_width = upper / base - 1
    determinant_perturbation = determinant_residual_radius(
        size, residual_bounds, radial_width
    )
    regularizer = arb(1, determinant_perturbation)
    if not regularizer.lower() > 0:
        raise AssertionError(
            f"positive cell enclosure lost for size {size} at {fraction_text(base)}: {regularizer}"
        )
    return {
        "base_x": fraction_text(base),
        "upper_x": fraction_text(upper),
        "radial_relative_width": fraction_text(radial_width),
        "R_lower": float(regularizer.lower()),
        "R_upper": float(regularizer.upper()),
        "determinant_perturbation_upper": float(determinant_perturbation.upper()),
        "maximum_entry_tail_radius": max(float(value) for row in tails for value in row),
    }


def adaptive_radial_certificates() -> tuple[
    dict[int, list[dict[str, Any]]], list[dict[str, Any]]
]:
    """Choose the coarsest proved linear subdivision in every dyadic band."""

    by_size: dict[int, list[dict[str, Any]]] = {2: [], 3: []}
    bands = []
    raw_cells: list[tuple[Fraction, Fraction]] = []
    for lower_power in range(RADIAL_LOW_POWER, RADIAL_HIGH_POWER, -1):
        lower = Fraction(1, 2**lower_power)
        selected = None
        for subdivisions in RADIAL_SUBDIVISION_CANDIDATES:
            step = lower / subdivisions
            radial_bound = Fraction(1, subdivisions)
            candidate_by_size: dict[int, list[dict[str, Any]]] = {2: [], 3: []}
            try:
                for index in range(subdivisions):
                    base = lower + index * step
                    upper = base + step
                    for size in (2, 3):
                        candidate_by_size[size].append(
                            cell_certificate(base, upper, size, radial_bound)
                        )
            except AssertionError:
                continue
            selected = (subdivisions, candidate_by_size)
            break
        if selected is None:
            raise AssertionError(f"no admitted radial subdivision certified band 2^-{lower_power}")
        subdivisions, candidate_by_size = selected
        by_size[2].extend(candidate_by_size[2])
        by_size[3].extend(candidate_by_size[3])
        raw_cells.extend(
            (Fraction(row["base_x"]), Fraction(row["upper_x"]))
            for row in candidate_by_size[2]
        )
        bands.append(
            {
                "lower": f"2^-{lower_power}",
                "upper": f"2^-{lower_power - 1}",
                "subdivisions": subdivisions,
                "maximum_relative_radial_width": f"1/{subdivisions}",
            }
        )
    if raw_cells[0][0] != Fraction(1, 2**RADIAL_LOW_POWER):
        raise AssertionError("radial floor not covered")
    if raw_cells[-1][1] != Fraction(1, 2**RADIAL_HIGH_POWER):
        raise AssertionError("radial ceiling not covered")
    for first, second in zip(raw_cells, raw_cells[1:]):
        if first[1] != second[0]:
            raise AssertionError("radial tiling has a gap")
    return by_size, bands


def pattern_occurrences(source: dict[str, Any]) -> dict[str, int]:
    result: dict[str, int] = {}
    for entry in source["complete_factorization_inventory"]["entries"]:
        for factor in entry["species_factors"]:
            if factor["size"] <= 1:
                continue
            key = (
                f"m{factor['size']}|"
                f"L{','.join(map(str, factor['left_canonical_positions']))}|"
                f"R{','.join(map(str, factor['right_canonical_positions']))}"
            )
            result[key] = result.get(key, 0) + 1
    return result


def direct_controls(certificate_by_size: dict[int, list[dict[str, Any]]]) -> dict[str, Any]:
    """Independent Decimal finite-gap witnesses contained by certified cells."""

    rows = []
    for size in (2, 3):
        target = Fraction(2, 25)
        matching = next(
            cell
            for cell in certificate_by_size[size]
            if Fraction(cell["base_x"]) <= target < Fraction(cell["upper_x"])
        )
        cell_base_fraction = Fraction(matching["base_x"])
        radial_fraction = target / cell_base_fraction - 1
        base = Decimal(cell_base_fraction.numerator) / Decimal(cell_base_fraction.denominator)
        radial = Decimal(radial_fraction.numerator) / Decimal(radial_fraction.denominator)
        gap_fraction = GAP_RELATIVE_RADIUS / 2
        gap = Decimal(gap_fraction.numerator) / Decimal(gap_fraction.denominator)
        minimum_sum = Decimal(target.numerator) / Decimal(target.denominator)
        left_minimum = minimum_sum * Decimal(2) / 5
        right_minimum = minimum_sum * Decimal(3) / 5
        left = [left_minimum + Decimal(size - 1 - index) * base * gap for index in range(size)]
        right = [right_minimum + Decimal(size - 1 - index) * base * gap for index in range(size)]
        with localcontext() as context:
            context.prec = 220
            value = K186.divided_difference_regularizer(left, right, 200)
        contained = Decimal(str(matching["R_lower"])) <= value <= Decimal(str(matching["R_upper"]))
        if not contained:
            raise AssertionError(f"independent finite-gap control escaped size-{size} enclosure")
        rows.append(
            {
                "size": size,
                "cell_base_argument": matching["base_x"],
                "minimum_cross_argument": "2/25",
                "radial_ratio": str(radial),
                "maximum_row_gap_ratio": str(gap),
                "maximum_column_gap_ratio": str(gap),
                "regularizer": format(value, ".24E"),
                "certified_cell_lower": matching["R_lower"],
                "certified_cell_upper": matching["R_upper"],
                "contained": True,
            }
        )
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_controls_contained": all(row["contained"] for row in rows),
        "role": "independent finite-gap values inside outward generic cells; not the interval proof",
    }


def build() -> dict[str, Any]:
    source = json.loads(K186_MANIFEST.read_text())
    predecessor = json.loads(K190_MANIFEST.read_text())
    by_size, radial_bands = adaptive_radial_certificates()
    occurrences = pattern_occurrences(source)
    patterns_by_size = {
        size: sum(1 for record in source["unique_patterns"].values() if record["size"] == size)
        for size in (2, 3)
    }
    occurrences_by_size = {
        size: sum(
            count
            for pattern, count in occurrences.items()
            if pattern.startswith(f"m{size}|")
        )
        for size in (2, 3)
    }
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k186-order-six-bessel-vandermonde-wave.json",
            "predecessor_manifest": "lab/process/k190-order-six-coalescent-scaled-jet-wave.json",
            "domain": predecessor["fixed_control"]["domain"],
            "radial_argument_range": "2^-200<=x<=1/4",
            "relative_radial_cell_width": "adaptive dyadic-band subdivision from 1/8 through 1/256",
            "maximum_row_spread_over_cell_base": fraction_text(GAP_RELATIVE_RADIUS),
            "maximum_column_spread_over_cell_base": fraction_text(GAP_RELATIVE_RADIUS),
            "maximum_kernel_argument_offset_over_cell_base": fraction_text(
                Fraction(1, min(RADIAL_SUBDIVISION_CANDIDATES))
                + 2 * GAP_RELATIVE_RADIUS
            ),
            "taylor_order": TAYLOR_ORDER,
            "source_patterns": len(source["unique_patterns"]),
            "source_nontrivial_occurrences": sum(occurrences.values()),
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "normalized_identity": {
            "kernel": "F_x(y)=x*K1(x*(1+y))",
            "dimensionless_nodes": "T_i=T_*+x*r_i, U_j=U_*+x*c_j, T_*+U_*=x*(1+w), with x the fixed cell base",
            "matrix_entry": "D_ij=[r_0,...,r_i][c_0,...,c_j]F_x(w+r+c)",
            "regularizer": "R_m=det[D_ij]*product_ab(1+w+r_a+c_b)",
            "coalescent_reduction": "at w=r=c=0 this is K190's scaled-q Hankel normal form",
            "common_radial_scale_cancelled_before_interval_evaluation": True,
            "row_column_correlations_retained_through_complete_divided_difference_entries": True,
        },
        "taylor_theorem": {
            "coefficient": "c_n=x^(n+1)*K1^(n)(x)/n! with sign (-1)^n",
            "monomial_dd": "sequential row/column divided difference of (w+r+c)^n, expanded exactly with nonnegative rational coefficients",
            "entry_tail": "|E_ij|<=|c_(N+1)|*(N+1)!/((N+1-i-j)!*i!*j!)*eta^(N+1-i-j)",
            "tail_basis": "K1 is completely monotone, so the next derivative at y=0 bounds the Lagrange remainder on y>=0",
            "eta": "cell-specific radial width plus twice 1/512; global maximum 33/256",
            "arb_decimal_digits": ARB_DIGITS,
            "threads": 1,
        },
        "outward_certificate": {
            "radial_cells": len(by_size[2]),
            "dyadic_band_subdivisions": radial_bands,
            "radial_tiling_has_no_gaps": True,
            "sizes": {str(size): by_size[size] for size in (2, 3)},
            "all_cells_strictly_positive": True,
            "minimum_R_lower_by_size": {
                str(size): min(row["R_lower"] for row in by_size[size]) for size in (2, 3)
            },
            "maximum_R_upper_by_size": {
                str(size): max(row["R_upper"] for row in by_size[size]) for size in (2, 3)
            },
            "maximum_entry_tail_radius_by_size": {
                str(size): max(row["maximum_entry_tail_radius"] for row in by_size[size])
                for size in (2, 3)
            },
        },
        "complete_family_propagation": {
            "patterns_by_size": {str(key): value for key, value in patterns_by_size.items()},
            "occurrences_by_size": {str(key): value for key, value in occurrences_by_size.items()},
            "all_53_patterns_covered_conditionally_on_spread_box": sum(patterns_by_size.values()) == 53,
            "all_468_occurrences_covered_conditionally_on_spread_box": sum(occurrences_by_size.values()) == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
        },
        "independent_controls": direct_controls(by_size),
        "decision": {
            "nonzero_gap_outward_region_certified": True,
            "arbitrary_gap_ratio_coverage_complete": False,
            "certified_region": "all size-two/three K186 regularizers with 2^-200<=minimum cross argument<=1/4, adaptive radial cell width<=1/8, and each row and column spread<=1/512 of the cell base",
            "residual_region": "row or column spread greater than 1/512 of the local radial base within the K188 positive-radius core",
            "duffy_jacobi_composition_released": False,
            "next_exact_input": "stratify the residual gap-ratio simplex by maximum row/column spread, re-center the normalized divided-difference Taylor model on noncoalescent faces, and compose only after the union of certified cells covers every K186 time-node pattern",
        },
        "release_test": {
            "normalized_divided_difference_identity_banked": True,
            "analytic_entry_tail_bound_banked": True,
            "gap_positive_outward_cells_serialized": True,
            "complete_radial_argument_range_tiled": True,
            "all_53_patterns_propagated_on_certified_cells": True,
            "all_468_occurrences_propagated_on_certified_cells": True,
            "arbitrary_gap_ratio_domain_covered": False,
            "duffy_jacobi_chain_rule_envelopes_serialized": False,
            "determinant_preserving_positive_radius_core_error_serialized": False,
            "complete_outward_order_six_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixed_control": result["fixed_control"],
        "normalized_identity": result["normalized_identity"],
        "taylor_theorem": result["taylor_theorem"],
        "outward_certificate": {
            key: value
            for key, value in result["outward_certificate"].items()
            if key != "sizes"
        },
        "complete_family_propagation": result["complete_family_propagation"],
        "independent_controls": result["independent_controls"],
        "decision": result["decision"],
        "release_test": result["release_test"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
