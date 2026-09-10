#!/usr/bin/env python3
"""K193 shifted noncoalescent face-entry certificates for K186 regularizers.

K192 banked the finite active-gap topology but stopped before an outward
shifted Taylor operator.  This module constructs that operator.  Every matrix
entry expands ``F_x(y)-(1+y)^-1`` about the midpoint of the Hermite--Genocchi
argument range induced by one common face chart.  Exact translated monomial
divided differences retain the shared chart variables, and complete Cauchy
minor determinants carry the linear determinant perturbation.

The present certificate is intentionally local: it covers rational boxes
around every K192 face center on the radial cell ``31/256 <= x <= 1/8``.  It
does not claim that those boxes cover the residual gap simplex or release a
Duffy/Jacobi remainder.
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
K191_PATH = ROOT / "tests/channel-swings/k191_order_six_near_coalescent_taylor_box.py"
K192_PATH = ROOT / "tests/channel-swings/k192_order_six_radially_stratified_wide_gap.py"
K192_MANIFEST = ROOT / "lab/process/k192-order-six-radially-stratified-wide-gap-wave.json"
OUTPUT = ROOT / "lab/process/k193-order-six-shifted-face-entry-wave.json"

BASE_X = Fraction(31, 256)
UPPER_X = Fraction(1, 8)
RADIAL_WIDTH = UPPER_X / BASE_X - 1
ACTIVE_HALF_WIDTH = Fraction(1, 512)
INACTIVE_UPPER = Fraction(1, 512)
TAYLOR_ORDER = 16
ARB_DIGITS = 120

ctx.dps = ARB_DIGITS
ctx.threads = 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K191 = load_module("k191_for_k193", K191_PATH)
K192 = load_module("k192_for_k193", K192_PATH)
VARIABLES = K191.VARIABLES
GAP_VARIABLES = (K191.R0, K191.R1, K191.C0, K191.C1)
LABELS = ("r0", "r1", "c0", "c1")
SYMBOL_BY_LABEL = dict(zip(LABELS, GAP_VARIABLES))


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def ball(value: Fraction) -> arb:
    return arb(ftext(value))


def interval(lower: Fraction, upper: Fraction) -> arb:
    return K191.interval_from_bounds(lower, upper)


def chart_bounds(center: dict[str, str], size: int) -> dict[sp.Symbol, tuple[Fraction, Fraction]]:
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]] = {
        K191.W: (Fraction(0), RADIAL_WIDTH),
    }
    relevant = {"r0", "c0"} if size == 2 else set(LABELS)
    for label in LABELS:
        symbol = SYMBOL_BY_LABEL[label]
        if label not in relevant:
            bounds[symbol] = (Fraction(0), Fraction(0))
            continue
        value = Fraction(center[label])
        if value:
            bounds[symbol] = (value - ACTIVE_HALF_WIDTH, value + ACTIVE_HALF_WIDTH)
        else:
            bounds[symbol] = (Fraction(0), INACTIVE_UPPER)
    return bounds


def interval_values(bounds: dict[sp.Symbol, tuple[Fraction, Fraction]]) -> dict[sp.Symbol, arb]:
    return {symbol: interval(*bounds[symbol]) for symbol in VARIABLES}


@lru_cache(maxsize=None)
def shifted_monomial_dd_matrix(power: int, size: int, shift: Fraction):
    substitution = {
        K191.W: K191.W - sp.Rational(shift.numerator, shift.denominator)
    }
    return tuple(
        tuple(value.subs(substitution) for value in row)
        for row in K191.monomial_dd_matrix(power, size)
    )


@lru_cache(maxsize=None)
def derivative_abs_at_base(y: Fraction, order: int) -> arb:
    """Absolute y-derivative of F_x(y)=x*K1(x*(1+y))."""

    x = ball(BASE_X)
    argument = x * ball(1 + y)
    bessel = tuple(argument.bessel_k(index) for index in range(order + 2))
    result = arb(0)
    for index in range(order + 1):
        result += math.comb(order, index) * bessel[abs(1 - order + 2 * index)]
    result *= arb(2) ** (-order)
    return x ** (order + 1) * result


def shifted_coefficients(shift: Fraction, maximum_order: int) -> tuple[arb, ...]:
    coefficients = []
    for order in range(maximum_order + 1):
        value = derivative_abs_at_base(shift, order) / math.factorial(order)
        if order % 2:
            value = -value
        cauchy = ball(Fraction(-1 if order % 2 else 1, 1)) / ball(1 + shift) ** (order + 1)
        coefficients.append(value - cauchy)
    return tuple(coefficients)


def entry_argument_bounds(
    size: int,
    row: int,
    column: int,
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]],
) -> tuple[Fraction, Fraction]:
    rows = K191.row_nodes(size)[: row + 1]
    columns = K191.column_nodes(size)[: column + 1]

    def node_bounds(node: sp.Expr) -> tuple[Fraction, Fraction]:
        if node == 0:
            return Fraction(0), Fraction(0)
        return bounds[node]

    row_bounds = [node_bounds(node) for node in rows]
    column_bounds = [node_bounds(node) for node in columns]
    return (
        bounds[K191.W][0] + min(value[0] for value in row_bounds) + min(value[0] for value in column_bounds),
        bounds[K191.W][1] + max(value[1] for value in row_bounds) + max(value[1] for value in column_bounds),
    )


def shifted_entry_enclosure(
    x: arb,
    size: int,
    row: int,
    column: int,
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]],
) -> tuple[arb, arb, Fraction, Fraction]:
    lower, upper = entry_argument_bounds(size, row, column, bounds)
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = interval_values(bounds)
    coefficients = shifted_coefficients(shift, TAYLOR_ORDER)
    polynomial = arb(0)
    for power in range(row + column, TAYLOR_ORDER + 1):
        monomial = shifted_monomial_dd_matrix(power, size, shift)[row][column]
        polynomial += coefficients[power] * K191.evaluate_sympy_interval(monomial, values)

    derivative_order = row + column
    tail_order = TAYLOR_ORDER + 1
    f_sup = derivative_abs_at_base(lower, tail_order)
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


def determinant_radius(
    size: int,
    residual: list[list[arb]],
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]],
) -> arb:
    values = interval_values(bounds)
    residual_bounds = [[value.abs_upper() for value in row] for row in residual]
    cauchy = [
        [K191.evaluate_sympy_interval(value, values) for value in row]
        for row in K191.cauchy_dd_matrix(size)
    ]
    q_expression = sp.prod(
        1 + K191.W + row + column
        for row in K191.row_nodes(size)
        for column in K191.column_nodes(size)
    )
    q_upper = K191.evaluate_sympy_interval(q_expression, values).abs_upper()
    radius = arb(0)
    for row in range(size):
        for column in range(size):
            minor = [
                [cauchy[i][j] for j in range(size) if j != column]
                for i in range(size) if i != row
            ]
            coefficient = (q_upper * K191.determinant(minor)).abs_upper()
            radius += coefficient * residual_bounds[row][column]
    if size == 2:
        radius += q_upper * (
            residual_bounds[0][0] * residual_bounds[1][1]
            + residual_bounds[0][1] * residual_bounds[1][0]
        )
        return radius.upper()
    for permutation in itertools.permutations(range(size)):
        for selected_rows in itertools.combinations(range(size), 2):
            selected = set(selected_rows)
            term = q_upper
            for row, column in enumerate(permutation):
                term *= residual_bounds[row][column] if row in selected else cauchy[row][column].abs_upper()
            radius += term
        cubic = q_upper
        for row, column in enumerate(permutation):
            cubic *= residual_bounds[row][column]
        radius += cubic
    return radius.upper()


def exact_translation_checks() -> dict[str, Any]:
    checked = 0
    shift = Fraction(7, 64)
    a = sp.Rational(shift.numerator, shift.denominator)
    for size in (2, 3):
        for power in range(TAYLOR_ORDER + 1):
            original = K191.monomial_dd_matrix(power, size)
            reconstructed = [[sp.Integer(0) for _ in range(size)] for _ in range(size)]
            for shifted_power in range(power + 1):
                translated = shifted_monomial_dd_matrix(shifted_power, size, shift)
                coefficient = sp.binomial(power, shifted_power) * a ** (power - shifted_power)
                for row in range(size):
                    for column in range(size):
                        reconstructed[row][column] += coefficient * translated[row][column]
            for row in range(size):
                for column in range(size):
                    if sp.expand(original[row][column] - reconstructed[row][column]) != 0:
                        raise AssertionError("shifted divided-difference translation identity failed")
                    checked += 1
    return {
        "rational_shift": ftext(shift),
        "matrix_entries_checked": checked,
        "all_exact": True,
    }


def chart_certificate(size: int, face: dict[str, Any]) -> dict[str, Any]:
    bounds = chart_bounds(face["center"], size)
    x = ball(BASE_X)
    residual: list[list[arb]] = []
    tails = []
    shifts = []
    radii = []
    for row in range(size):
        residual_row = []
        for column in range(size):
            value, tail, shift, radius = shifted_entry_enclosure(x, size, row, column, bounds)
            residual_row.append(value)
            tails.append(float(tail))
            shifts.append(ftext(shift))
            radii.append(ftext(radius))
        residual.append(residual_row)
    perturbation = determinant_radius(size, residual, bounds)
    regularizer = arb(1, perturbation)
    if not regularizer.lower() > 0:
        raise AssertionError(
            f"shifted face chart lost positivity for size {size} active={face['active']}: {regularizer}"
        )
    return {
        "active": face["active"],
        "center": face["center"],
        "bounds": {
            str(symbol): [ftext(lower), ftext(upper)]
            for symbol, (lower, upper) in bounds.items()
        },
        "entry_shifts": shifts,
        "entry_radii": radii,
        "maximum_entry_tail": max(tails),
        "determinant_perturbation_upper": float(perturbation),
        "R_lower": float(regularizer.lower()),
        "R_upper": float(regularizer.upper()),
        "strictly_positive": True,
    }


def point_controls(charts: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    rows = []
    for size in (2, 3):
        chart = charts[str(size)][-1]
        center = chart["center"]
        w = RADIAL_WIDTH / 2
        argument = BASE_X * (1 + w)
        left_minimum = argument * Fraction(2, 5)
        right_minimum = argument * Fraction(3, 5)
        row_labels = ("r0",) if size == 2 else ("r0", "r1")
        column_labels = ("c0",) if size == 2 else ("c0", "c1")
        row_offsets = [Fraction(center[label]) for label in row_labels] + [Fraction(0)]
        column_offsets = [Fraction(center[label]) for label in column_labels] + [Fraction(0)]
        with localcontext() as context:
            context.prec = 220
            base_decimal = Decimal(BASE_X.numerator) / Decimal(BASE_X.denominator)
            left = [
                Decimal(left_minimum.numerator) / Decimal(left_minimum.denominator)
                + base_decimal * Decimal(offset.numerator) / Decimal(offset.denominator)
                for offset in row_offsets
            ]
            right = [
                Decimal(right_minimum.numerator) / Decimal(right_minimum.denominator)
                + base_decimal * Decimal(offset.numerator) / Decimal(offset.denominator)
                for offset in column_offsets
            ]
            value = K191.K186.divided_difference_regularizer(left, right, 200)
        contained = Decimal(str(chart["R_lower"])) <= value <= Decimal(str(chart["R_upper"]))
        if not contained:
            raise AssertionError("independent face-center value escaped its outward chart")
        rows.append({
            "size": size,
            "active": chart["active"],
            "minimum_cross_argument": ftext(argument),
            "regularizer": format(value, ".24E"),
            "certified_lower": chart["R_lower"],
            "certified_upper": chart["R_upper"],
            "contained": True,
        })
    return {"precision_decimal_digits": 200, "rows": rows, "all_contained": True}


def build() -> dict[str, Any]:
    predecessor = json.loads(K192_MANIFEST.read_text())
    masks = predecessor["noncoalescent_face_scaffold"]["size_three_nonempty_active_gap_masks"]
    faces_by_size = {
        "2": [face for face in masks if set(face["active"]) <= {"r0", "c0"}],
        "3": masks,
    }
    charts = {
        size: [chart_certificate(int(size), face) for face in faces]
        for size, faces in faces_by_size.items()
    }
    controls = point_controls(charts)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k192-order-six-radially-stratified-wide-gap-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": f"{ftext(BASE_X)}<=x<={ftext(UPPER_X)}",
            "relative_radial_width": ftext(RADIAL_WIDTH),
            "active_coordinate_half_width": ftext(ACTIVE_HALF_WIDTH),
            "inactive_coordinate_upper": ftext(INACTIVE_UPPER),
            "taylor_order": TAYLOR_ORDER,
            "arb_decimal_digits": ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "shifted_operator": {
            "entry_identity": "[r_0,...,r_i][c_0,...,c_j](F_x-G)=sum_n (F_x^(n)(a)-G^(n)(a))/n! * [r_0,...,r_i][c_0,...,c_j](w+r+c-a)^n",
            "center_rule": "entrywise midpoint of the Hermite--Genocchi argument range induced by one shared rational face box",
            "tail_rule": "complete monotonicity bounds the (N+1)st derivative at the common argument lower endpoint; the shifted Hermite--Genocchi radius is half the declared argument range",
            "linear_determinant_rule": "evaluate each complete signed Cauchy minor determinant before absolute bounding, then multiply by a separately outward common normalization-product bound and the shifted residual-entry radius",
            "shared_face_center_dependencies_retained": True,
            "determinant_level_cauchy_cofactors_retained": True,
            "exact_translation_checks": exact_translation_checks(),
        },
        "outward_face_charts": {
            "sizes": charts,
            "size_two_chart_count": len(charts["2"]),
            "size_three_chart_count": len(charts["3"]),
            "all_18_charts_strictly_positive": all(
                chart["strictly_positive"] for rows in charts.values() for chart in rows
            ),
            "minimum_R_lower_by_size": {
                size: min(chart["R_lower"] for chart in rows) for size, rows in charts.items()
            },
            "maximum_R_upper_by_size": {
                size: max(chart["R_upper"] for chart in rows) for size, rows in charts.items()
            },
        },
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_two_and_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "outward_domain_propagates_only_when_a_pattern_lies_in_a_declared_chart": True,
        },
        "decision": {
            "shifted_face_entry_operator_serialized": True,
            "shared_center_and_cauchy_cofactor_requirements_closed": True,
            "all_k192_face_centers_have_a_strict_outward_neighborhood_on_the_rejected_high_radial_cell": True,
            "residual_gap_simplex_union_complete": False,
            "duffy_jacobi_composition_released": False,
            "next_exact_input": "tile the ordered physical gap-ratio domain with adaptive shifted charts, prove overlap with the K192 coalescent union, and only then differentiate the common chart model for Duffy/Jacobi remainder bounds",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_serialized": True,
            "shared_face_center_dependencies_serialized": True,
            "determinant_level_cauchy_cofactors_serialized": True,
            "all_15_size_three_face_centers_outwardly_certified": True,
            "all_3_size_two_face_centers_outwardly_certified": True,
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
            "LT-GR6b": "NEEDS_UNCHANGED",
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
        "shifted_operator": result["shifted_operator"],
        "outward_face_charts": {
            key: value for key, value in result["outward_face_charts"].items() if key != "sizes"
        },
        "independent_controls": result["independent_controls"],
        "complete_family_propagation": result["complete_family_propagation"],
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
