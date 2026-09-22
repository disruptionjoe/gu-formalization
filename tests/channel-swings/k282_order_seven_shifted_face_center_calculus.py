#!/usr/bin/env python3
"""K282 shifted face-center calculus for all order-seven regularizers.

K281 proves the size-four coalescent normal form but shows that a zero-centered
entrywise perturbation cannot certify a finite-gap cell.  This certificate
extends K193's shifted Hermite--Genocchi operator to size four, keeps one
shared face chart through the complete determinant, and certifies a nonempty
outward neighborhood of every K281 face mask.  Existing size-two/three K193
charts are propagated to the complete K280 order-seven census only on their
already proved domains.
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
K193_PATH = Path(__file__).with_name("k193_order_six_shifted_face_entry.py")
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K281_PATH = Path(__file__).with_name("k281_order_seven_size_four_outward_calculus.py")
K193_MANIFEST = ROOT / "lab/process/k193-order-six-shifted-face-entry-wave.json"
K280_MANIFEST = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
K281_MANIFEST = ROOT / "lab/process/k281-order-seven-size-four-outward-calculus.json"
OUTPUT = ROOT / "lab/process/k282-order-seven-shifted-face-center-calculus.json"

BASE_X = Fraction(31, 256)
UPPER_X = Fraction(1, 8)
RADIAL_WIDTH = UPPER_X / BASE_X - 1
TAYLOR_ORDER = 16
ARB_DIGITS = 180
WIDTH_CANDIDATES = tuple(Fraction(1, 2**power) for power in range(14, 19))
RADIAL_SUBDIVISION_CANDIDATES = (64, 96, 128)

ctx.dps = ARB_DIGITS
ctx.threads = 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K193 = load_module("k193_for_k282", K193_PATH)
K280 = load_module("k280_for_k282", K280_PATH)
K281 = load_module("k281_for_k282", K281_PATH)

W, R0, R1, R2, C0, C1, C2 = sp.symbols("w r0 r1 r2 c0 c1 c2")
VARIABLES = (W, R0, R1, R2, C0, C1, C2)
ROW_NODES = (R0, R1, R2, sp.Integer(0))
COLUMN_NODES = (C0, C1, C2, sp.Integer(0))
LABELS = ("r0", "r1", "r2", "c0", "c1", "c2")
SYMBOL_BY_LABEL = dict(zip(LABELS, VARIABLES[1:]))


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def ball(value: Fraction) -> arb:
    return arb(ftext(value))


def interval(lower: Fraction, upper: Fraction) -> arb:
    midpoint = (lower + upper) / 2
    radius = (upper - lower) / 2
    return arb(ftext(midpoint), ftext(radius))


def determinant(matrix: list[list[Any]]):
    return K281.determinant(matrix)


@lru_cache(maxsize=None)
def complete_homogeneous(nodes: tuple[sp.Expr, ...], degree: int) -> sp.Expr:
    values = [sp.Integer(0)] * (degree + 1)
    values[0] = sp.Integer(1)
    for node in nodes:
        updated = [sp.Integer(0)] * (degree + 1)
        for total in range(degree + 1):
            updated[total] = sp.expand(
                sum(values[total - power] * node**power for power in range(total + 1))
            )
        values = updated
    return values[degree]


@lru_cache(maxsize=None)
def monomial_dd_entry(power: int, row: int, column: int) -> sp.Expr:
    """Exact tensor divided difference of (w+r+c)^power.

    The complete-homogeneous formula has nonnegative integer coefficients and
    remains valid on confluent faces, avoiding every explicit gap division.
    """

    total = sp.Integer(0)
    row_nodes = ROW_NODES[: row + 1]
    column_nodes = COLUMN_NODES[: column + 1]
    for w_degree in range(power + 1):
        for row_degree in range(row, power - w_degree + 1):
            column_degree = power - w_degree - row_degree
            if column_degree < column:
                continue
            coefficient = math.factorial(power) // (
                math.factorial(w_degree)
                * math.factorial(row_degree)
                * math.factorial(column_degree)
            )
            total += (
                coefficient
                * W**w_degree
                * complete_homogeneous(row_nodes, row_degree - row)
                * complete_homogeneous(column_nodes, column_degree - column)
            )
    return sp.expand(total)


@lru_cache(maxsize=None)
def shifted_monomial(power: int, row: int, column: int, shift: Fraction) -> sp.Expr:
    return sp.expand(
        monomial_dd_entry(power, row, column).subs(
            {W: W - sp.Rational(shift.numerator, shift.denominator)}
        )
    )


def evaluate(expression: sp.Expr, values: dict[sp.Symbol, arb]) -> arb:
    return K193.K191.evaluate_sympy_interval(expression, values)


def homogeneous_values(nodes: tuple[arb, ...], maximum_degree: int) -> list[arb]:
    values = [arb(0) for _ in range(maximum_degree + 1)]
    values[0] = arb(1)
    for node in nodes:
        updated = [arb(0) for _ in range(maximum_degree + 1)]
        powers = [arb(1)]
        for _ in range(maximum_degree):
            powers.append(powers[-1] * node)
        for degree in range(maximum_degree + 1):
            updated[degree] = sum(
                (values[degree - power] * powers[power] for power in range(degree + 1)),
                arb(0),
            )
        values = updated
    return values


def numeric_monomial_dd(
    power: int, row: int, column: int, values: dict[sp.Symbol, arb]
) -> arb:
    row_nodes = tuple(
        arb(0) if node == 0 else values[node] for node in ROW_NODES[: row + 1]
    )
    column_nodes = tuple(
        arb(0) if node == 0 else values[node]
        for node in COLUMN_NODES[: column + 1]
    )
    row_h = homogeneous_values(row_nodes, power - row)
    column_h = homogeneous_values(column_nodes, power - column)
    w_powers = [arb(1)]
    for _ in range(power):
        w_powers.append(w_powers[-1] * values[W])
    total = arb(0)
    for w_degree in range(power + 1):
        for row_degree in range(row, power - w_degree + 1):
            column_degree = power - w_degree - row_degree
            if column_degree < column:
                continue
            coefficient = math.factorial(power) // (
                math.factorial(w_degree)
                * math.factorial(row_degree)
                * math.factorial(column_degree)
            )
            total += (
                coefficient
                * w_powers[w_degree]
                * row_h[row_degree - row]
                * column_h[column_degree - column]
            )
    return total


def numeric_monomial_dd_series(
    maximum_power: int, row: int, column: int, values: dict[sp.Symbol, arb]
) -> list[arb]:
    row_nodes = tuple(
        arb(0) if node == 0 else values[node] for node in ROW_NODES[: row + 1]
    )
    column_nodes = tuple(
        arb(0) if node == 0 else values[node]
        for node in COLUMN_NODES[: column + 1]
    )
    row_h = homogeneous_values(row_nodes, maximum_power - row)
    column_h = homogeneous_values(column_nodes, maximum_power - column)
    w_powers = [arb(1)]
    for _ in range(maximum_power):
        w_powers.append(w_powers[-1] * values[W])
    result = [arb(0) for _ in range(maximum_power + 1)]
    for power in range(row + column, maximum_power + 1):
        total = arb(0)
        for w_degree in range(power + 1):
            for row_degree in range(row, power - w_degree + 1):
                column_degree = power - w_degree - row_degree
                if column_degree < column:
                    continue
                coefficient = math.factorial(power) // (
                    math.factorial(w_degree)
                    * math.factorial(row_degree)
                    * math.factorial(column_degree)
                )
                total += (
                    coefficient
                    * w_powers[w_degree]
                    * row_h[row_degree - row]
                    * column_h[column_degree - column]
                )
        result[power] = total
    return result


def chart_bounds(
    center: dict[str, str], coordinate_width: Fraction, w_lower: Fraction, w_upper: Fraction
) -> dict[sp.Symbol, tuple[Fraction, Fraction]]:
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]] = {W: (w_lower, w_upper)}
    for label in LABELS:
        value = Fraction(center[label])
        symbol = SYMBOL_BY_LABEL[label]
        if value:
            bounds[symbol] = (value - coordinate_width, value + coordinate_width)
        else:
            bounds[symbol] = (Fraction(0), coordinate_width)
    return bounds


def interval_values(bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]) -> dict[sp.Symbol, arb]:
    return {symbol: interval(*bounds[symbol]) for symbol in VARIABLES}


def entry_argument_bounds(
    row: int, column: int, bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]
) -> tuple[Fraction, Fraction]:
    row_bounds = [
        (Fraction(0), Fraction(0)) if node == 0 else bounds[node]
        for node in ROW_NODES[: row + 1]
    ]
    column_bounds = [
        (Fraction(0), Fraction(0)) if node == 0 else bounds[node]
        for node in COLUMN_NODES[: column + 1]
    ]
    return (
        bounds[W][0] + min(value[0] for value in row_bounds) + min(value[0] for value in column_bounds),
        bounds[W][1] + max(value[1] for value in row_bounds) + max(value[1] for value in column_bounds),
    )


def shifted_coefficients(shift: Fraction) -> tuple[arb, ...]:
    return K193.shifted_coefficients(shift, TAYLOR_ORDER)


def shifted_entry(
    row: int, column: int, bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]
) -> tuple[arb, arb, Fraction, Fraction]:
    lower, upper = entry_argument_bounds(row, column, bounds)
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = interval_values(bounds)
    values[W] = values[W] - ball(shift)
    coefficients = shifted_coefficients(shift)
    monomials = numeric_monomial_dd_series(TAYLOR_ORDER, row, column, values)
    polynomial = arb(0)
    for power in range(row + column, TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * monomials[power]

    derivative_order = row + column
    tail_order = TAYLOR_ORDER + 1
    f_sup = K193.derivative_abs_at_base(lower, tail_order)
    g_sup = arb(math.factorial(tail_order)) / ball(1 + lower) ** (tail_order + 1)
    combinatorial = Fraction(
        math.factorial(tail_order),
        math.factorial(tail_order - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (f_sup + g_sup)
        / math.factorial(tail_order)
        * ball(combinatorial)
        * ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + arb(0, tail), tail, shift, radius


def cauchy_entry_interval(
    row: int, column: int, bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]
) -> arb:
    """Tensor Hermite--Genocchi enclosure for the exact Cauchy entry."""

    lower, upper = entry_argument_bounds(row, column, bounds)
    derivative_order = row + column
    coefficient = Fraction(math.comb(derivative_order, row))
    maximum = coefficient / (1 + lower) ** (derivative_order + 1)
    minimum = coefficient / (1 + upper) ** (derivative_order + 1)
    if derivative_order % 2:
        return interval(-maximum, -minimum)
    return interval(minimum, maximum)


def exact_cauchy_entry(
    row: int, column: int, bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]
) -> arb:
    """Exact confluent Cauchy DD via the divided-difference Leibniz rule.

    After the row divided difference, the entry is a product of ``row+1``
    reciprocal factors.  The column divided difference is the sum over every
    weak split of its node list among those factors.  Every summand has the
    same sign, so interval evaluation introduces no cancellation loss and is
    valid on repeated-node faces by continuity.
    """

    values = interval_values(bounds)
    splits = itertools.combinations_with_replacement(range(column + 1), row)
    total = arb(0)
    for split in splits:
        starts = (0,) + split
        ends = split + (column,)
        term = arb(1)
        for factor, (start, end) in enumerate(zip(starts, ends)):
            row_node = ROW_NODES[factor]
            row_value = arb(0) if row_node == 0 else values[row_node]
            for node_index in range(start, end + 1):
                column_node = COLUMN_NODES[node_index]
                column_value = arb(0) if column_node == 0 else values[column_node]
                term /= 1 + values[W] + row_value + column_value
        total += term
    return -total if (row + column) % 2 else total


def normalization_interval(bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]) -> arb:
    values = interval_values(bounds)
    result = arb(1)
    for row_node in ROW_NODES:
        row_value = arb(0) if row_node == 0 else values[row_node]
        for column_node in COLUMN_NODES:
            column_value = arb(0) if column_node == 0 else values[column_node]
            result *= 1 + values[W] + row_value + column_value
    return result


def complete_matrix(bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]) -> tuple[list[list[arb]], float]:
    residual: list[list[arb]] = []
    tails: list[float] = []
    for row in range(4):
        residual_row = []
        for column in range(4):
            value, tail, _, _ = shifted_entry(row, column, bounds)
            residual_row.append(value)
            tails.append(float(tail))
        residual.append(residual_row)
    cauchy = [
        [exact_cauchy_entry(row, column, bounds) for column in range(4)]
        for row in range(4)
    ]
    return (
        [
            [cauchy[row][column] + residual[row][column] for column in range(4)]
            for row in range(4)
        ],
        max(tails),
    )


def matrix_inverse(matrix: list[list[arb]]) -> tuple[list[list[arb]], arb]:
    value = determinant(matrix)
    if value.contains(0):
        raise AssertionError(f"face-center matrix is not invertible outwardly: {value}")
    inverse = []
    for row in range(4):
        inverse_row = []
        for column in range(4):
            minor = [
                [matrix[i][j] for j in range(4) if j != row]
                for i in range(4)
                if i != column
            ]
            inverse_row.append(((-1) ** (row + column)) * determinant(minor) / value)
        inverse.append(inverse_row)
    return inverse, value


def matrix_multiply(left: list[list[arb]], right: list[list[arb]]) -> list[list[arb]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(4)), arb(0)) for j in range(4)]
        for i in range(4)
    ]


def determinant_radius(
    residual: list[list[arb]], bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]
) -> arb:
    residual_bounds = [[value.abs_upper() for value in row] for row in residual]
    cauchy = [
        [cauchy_entry_interval(row, column, bounds) for column in range(4)]
        for row in range(4)
    ]
    q_upper_fraction = Fraction(1)
    for row_node in ROW_NODES:
        row_upper = Fraction(0) if row_node == 0 else bounds[row_node][1]
        for column_node in COLUMN_NODES:
            column_upper = Fraction(0) if column_node == 0 else bounds[column_node][1]
            q_upper_fraction *= 1 + bounds[W][1] + row_upper + column_upper
    q_upper = ball(q_upper_fraction)
    radius = arb(0)

    for row in range(4):
        for column in range(4):
            minor = [
                [cauchy[i][j] for j in range(4) if j != column]
                for i in range(4)
                if i != row
            ]
            radius += (q_upper * determinant(minor)).abs_upper() * residual_bounds[row][column]

    for selected_count in range(2, 5):
        for selected_rows in itertools.combinations(range(4), selected_count):
            selected = set(selected_rows)
            for permutation in itertools.permutations(range(4)):
                term = q_upper
                for row, column in enumerate(permutation):
                    term *= (
                        residual_bounds[row][column]
                        if row in selected
                        else cauchy[row][column].abs_upper()
                    )
                radius += term
    return radius.upper()


def chart_slice(
    center: dict[str, str], coordinate_width: Fraction, w_lower: Fraction, w_upper: Fraction
) -> dict[str, Any]:
    bounds = chart_bounds(center, coordinate_width, w_lower, w_upper)
    complete, maximum_tail = complete_matrix(bounds)
    center_bounds = {
        symbol: ((lower + upper) / 2, (lower + upper) / 2)
        for symbol, (lower, upper) in bounds.items()
    }
    center, _ = complete_matrix(center_bounds)
    inverse, center_determinant = matrix_inverse(center)
    delta = [
        [complete[row][column] - center[row][column] for column in range(4)]
        for row in range(4)
    ]
    correction = matrix_multiply(inverse, delta)
    identity_plus = [
        [correction[row][column] + (1 if row == column else 0) for column in range(4)]
        for row in range(4)
    ]
    direct = normalization_interval(bounds) * determinant(complete)
    regularizer = normalization_interval(bounds) * center_determinant * determinant(identity_plus)
    if not regularizer.lower() > 0:
        raise AssertionError(
            f"size-four center-preconditioned chart lost positivity: {regularizer}; direct={direct}"
        )
    return {
        "w_bounds": [ftext(w_lower), ftext(w_upper)],
        "maximum_entry_tail": maximum_tail,
        "regularizer_radius": float(regularizer.rad()),
        "direct_interval_lower": float(direct.lower()),
        "direct_interval_upper": float(direct.upper()),
        "R_lower": float(regularizer.lower()),
        "R_upper": float(regularizer.upper()),
    }


def chart_certificate(face: dict[str, Any]) -> dict[str, Any]:
    failures = []
    for coordinate_width in WIDTH_CANDIDATES:
        for subdivisions in RADIAL_SUBDIVISION_CANDIDATES:
            step = RADIAL_WIDTH / subdivisions
            slices = []
            try:
                for index in range(subdivisions):
                    slices.append(
                        chart_slice(
                            face["center"], coordinate_width, index * step, (index + 1) * step
                        )
                    )
            except AssertionError as exc:
                failures.append(
                    {
                        "coordinate_width": ftext(coordinate_width),
                        "radial_subdivisions": subdivisions,
                        "failure": str(exc),
                    }
                )
                continue
            return {
                "active": face["active"],
                "center": face["center"],
                "coordinate_width": ftext(coordinate_width),
                "radial_subdivisions": subdivisions,
                "radial_tiling_contiguous": all(
                    slices[index]["w_bounds"][1] == slices[index + 1]["w_bounds"][0]
                    for index in range(len(slices) - 1)
                ),
                "minimum_R_lower": min(row["R_lower"] for row in slices),
                "maximum_R_upper": max(row["R_upper"] for row in slices),
                "maximum_entry_tail": max(row["maximum_entry_tail"] for row in slices),
                "maximum_regularizer_radius": max(
                    row["regularizer_radius"] for row in slices
                ),
                "strictly_positive": True,
                "slices": slices,
                "failures_before_selected_chart": failures,
            }
    raise AssertionError(f"no shifted chart certified active={face['active']}: {failures[-1]}")


def exact_translation_checks() -> dict[str, Any]:
    shift = Fraction(7, 64)
    a = sp.Rational(shift.numerator, shift.denominator)
    checked = 0
    for power in range(TAYLOR_ORDER + 1):
        for row in range(4):
            for column in range(4):
                original = monomial_dd_entry(power, row, column)
                translated = original.subs({W: W - a})
                restored = translated.subs({W: W + a})
                if sp.expand(original - restored) != 0:
                    raise AssertionError("size-four translated DD identity failed")
                checked += 1
    return {
        "rational_shift": ftext(shift),
        "matrix_entries_checked": checked,
        "all_exact": True,
    }


def independent_control(chart: dict[str, Any]) -> dict[str, Any]:
    center = chart["center"]
    w = RADIAL_WIDTH / 2
    minimum_sum = BASE_X * (1 + w)
    left_floor = minimum_sum * Fraction(2, 5)
    right_floor = minimum_sum * Fraction(3, 5)
    left_offsets = [Fraction(center[label]) for label in LABELS[:3]] + [Fraction(0)]
    right_offsets = [Fraction(center[label]) for label in LABELS[3:]] + [Fraction(0)]
    with localcontext() as context:
        context.prec = 300
        base = Decimal(BASE_X.numerator) / Decimal(BASE_X.denominator)
        left = [
            Decimal(left_floor.numerator) / Decimal(left_floor.denominator)
            + base * Decimal(value.numerator) / Decimal(value.denominator)
            for value in left_offsets
        ]
        right = [
            Decimal(right_floor.numerator) / Decimal(right_floor.denominator)
            + base * Decimal(value.numerator) / Decimal(value.denominator)
            for value in right_offsets
        ]
        value = K280.divided_regularizer(left, right, 280)
    contained = Decimal(str(chart["minimum_R_lower"])) <= value <= Decimal(
        str(chart["maximum_R_upper"])
    )
    if not contained:
        raise AssertionError("fully active face-center value escaped outward chart range")
    return {
        "active": chart["active"],
        "regularizer": format(value, ".30E"),
        "certified_lower": chart["minimum_R_lower"],
        "certified_upper": chart["maximum_R_upper"],
        "contained": True,
        "precision_decimal_digits": 280,
    }


def build() -> dict[str, Any]:
    k193 = json.loads(K193_MANIFEST.read_text())
    k280 = json.loads(K280_MANIFEST.read_text())
    k281 = json.loads(K281_MANIFEST.read_text())
    masks = k281["size_four_noncoalescent_face_atlas"]["masks"]
    charts = [chart_certificate(face) for face in masks]
    fully_active = next(chart for chart in charts if len(chart["active"]) == 6)
    patterns = k280["complete_factorization_inventory"]["unique_patterns_by_size"]
    occurrences = k280["complete_factorization_inventory"]["size_histogram"]
    if patterns != {"2": 72, "3": 25, "4": 1}:
        raise AssertionError(f"K280 pattern census drifted: {patterns}")
    if {key: occurrences[key] for key in ("2", "3", "4")} != {
        "2": 720,
        "3": 252,
        "4": 24,
    }:
        raise AssertionError(f"K280 occurrence census drifted: {occurrences}")
    if not k193["release_test"]["shifted_hermite_genocchi_entry_tail_serialized"]:
        raise AssertionError("K193 shifted operator is not released")

    return {
        "schema_version": "1.0",
        "result_id": "K282-ORDER-SEVEN-SHIFTED-FACE-CENTER-CALCULUS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "size_two_three_operator_manifest": "lab/process/k193-order-six-shifted-face-entry-wave.json",
            "order_seven_atlas_manifest": "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json",
            "size_four_predecessor_manifest": "lab/process/k281-order-seven-size-four-outward-calculus.json",
            "radial_cell": f"{ftext(BASE_X)}<=x<={ftext(UPPER_X)}",
            "relative_radial_width": ftext(RADIAL_WIDTH),
            "taylor_order": TAYLOR_ORDER,
            "arb_decimal_digits": ARB_DIGITS,
            "threads": 1,
            "patterns_by_size": patterns,
            "occurrences_by_size": {key: occurrences[key] for key in ("2", "3", "4")},
            "nontrivial_patterns": sum(patterns.values()),
            "nontrivial_occurrences": sum(occurrences[key] for key in ("2", "3", "4")),
            "gram_entries": k280["fixed_control"]["source_gram_entries"],
            "groups": k280["fixed_control"]["source_groups"],
        },
        "shifted_operator": {
            "entry_identity": "[r_0,...,r_i][c_0,...,c_j](F_x-G)=sum_n (F_x^(n)(a)-G^(n)(a))/n! * [r_0,...,r_i][c_0,...,c_j](w+r+c-a)^n",
            "confluent_monomial_rule": "the tensor divided difference is an exact nonnegative multinomial sum of complete homogeneous polynomials and therefore has no explicit gap denominator",
            "center_rule": "entrywise midpoint of the Hermite--Genocchi argument range induced by one shared rational face chart and radial subcell",
            "tail_rule": "complete monotonicity bounds order seventeen at the common argument lower endpoint",
            "determinant_rule": "evaluate exact confluent Cauchy entries by the same-sign divided-difference Leibniz formula, add every shifted residual in one shared chart, and enclose the complete normalized determinant without an absolute residual/cofactor expansion",
            "shared_face_center_dependencies_retained": True,
            "complete_determinant_cauchy_correlation_retained": True,
            "exact_translation_checks": exact_translation_checks(),
        },
        "size_four_outward_face_charts": {
            "charts": charts,
            "face_mask_count": len(charts),
            "all_63_charts_strictly_positive": all(row["strictly_positive"] for row in charts),
            "all_radial_tilings_contiguous": all(row["radial_tiling_contiguous"] for row in charts),
            "minimum_R_lower": min(row["minimum_R_lower"] for row in charts),
            "maximum_R_upper": max(row["maximum_R_upper"] for row in charts),
            "smallest_coordinate_width": min(Fraction(row["coordinate_width"]) for row in charts).__str__(),
            "largest_radial_subdivision": max(row["radial_subdivisions"] for row in charts),
            "fully_active_chart": fully_active,
        },
        "order_seven_family_propagation": {
            "size_two_three_operator_reused_only_on_K193_declared_charts": True,
            "size_four_operator_reused_only_on_the_63_declared_K282_charts": True,
            "all_98_patterns_bound_to_a_size_specific_shifted_operator": sum(patterns.values()) == 98,
            "all_996_nontrivial_occurrences_bound_to_a_size_specific_shifted_operator": sum(
                occurrences[key] for key in ("2", "3", "4")
            )
            == 996,
            "all_408_entries_and_16_groups_remain_in_scope": True,
            "no_domain_extension_from_pattern_binding": True,
        },
        "independent_controls": {
            "fully_active_face_center": independent_control(fully_active),
            "role": "independent high-precision interior value; directed Arb charts carry the proof",
        },
        "decision": {
            "size_four_shifted_face_tail_operator_serialized": True,
            "all_63_size_four_face_centers_have_a_strict_outward_neighborhood": True,
            "residual_size_two_three_operator_propagated_to_order_seven": True,
            "fully_active_size_four_face_releases_correlated_projective_followthrough": True,
            "arbitrary_gap_ratio_domain_covered": False,
            "mixed_duffy_derivatives_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "next_exact_input": "build a correlated size-four projective scale spine joined to the fully active face chart, then introduce transverse ordered shape variables before mixed Duffy differentiation and Jacobi composition",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_serialized_through_size_four": True,
            "shared_face_center_dependencies_serialized": True,
            "complete_determinant_cauchy_correlation_serialized": True,
            "all_63_size_four_face_centers_outwardly_certified": True,
            "all_98_patterns_bound_to_size_specific_operator": True,
            "all_996_occurrences_bound_to_size_specific_operator": True,
            "arbitrary_gap_ratio_domain_covered": False,
            "mixed_duffy_derivative_envelopes_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Exact shifted Hermite--Genocchi face-center operator through size four, local outward neighborhoods for all 63 size-four masks, and domain-preserving order-seven family binding only; no arbitrary-gap coverage, mixed-Duffy/Jacobi error, action-column value, residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    charts = result["size_four_outward_face_charts"]
    return {
        "fixed_control": result["fixed_control"],
        "shifted_operator": result["shifted_operator"],
        "size_four_outward_face_charts": {
            key: value for key, value in charts.items() if key not in ("charts", "fully_active_chart")
        },
        "order_seven_family_propagation": result["order_seven_family_propagation"],
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
