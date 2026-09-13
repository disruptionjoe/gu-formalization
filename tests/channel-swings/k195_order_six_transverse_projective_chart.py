#!/usr/bin/env python3
"""K195 correlated transverse projective chart for K186 regularizers.

K194 certified one ordered-gap ray.  This certificate introduces compact
shape coordinates

    r0=s/32, r1=s*a/32, c0=s*b/32, c1=s*b*c/32

and evaluates every divided-difference entry from one common interval cell in
``(s,a,b,c,w)`` before the complete determinant.  The tracked result is a
rigorous three-axis transverse coordinate star through the K194 ray, not an
open product neighborhood, complete atlas, or Duffy/Jacobi cubature remainder.
"""

from __future__ import annotations

import argparse
import importlib.util
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
K194_PATH = ROOT / "tests/channel-swings/k194_order_six_projective_gap_spine.py"
K194_MANIFEST = ROOT / "lab/process/k194-order-six-projective-gap-spine-wave.json"
OUTPUT = ROOT / "lab/process/k195-order-six-transverse-projective-chart-wave.json"

S, A, B, C = sp.symbols("s a b c")
S_BOUNDS = (Fraction(1), Fraction(8))
SHAPE_BOUNDS = {
    A: (Fraction(1, 2) - Fraction(1, 1024), Fraction(1, 2) + Fraction(1, 1024)),
    B: (Fraction(4, 5) - Fraction(1, 2048), Fraction(4, 5) + Fraction(1, 2048)),
    C: (Fraction(1, 2) - Fraction(1, 1024), Fraction(1, 2) + Fraction(1, 1024)),
}
RAY = {A: Fraction(1, 2), B: Fraction(4, 5), C: Fraction(1, 2)}
SUBDIVISIONS = {
    2: {"scale": 64, "shape": 1, "radial": 16},
    3: {"scale": 256, "shape": 1, "radial": 16},
}
def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K194 = load_module("k194_for_k195", K194_PATH)
K193 = K194.K193
K191 = K194.K191
ctx.dps = K193.ARB_DIGITS
ctx.threads = 1


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def interval(lower: Fraction, upper: Fraction) -> arb:
    return K191.interval_from_bounds(lower, upper)


def split(lower: Fraction, upper: Fraction, count: int) -> list[tuple[Fraction, Fraction]]:
    return [
        (
            lower + (upper - lower) * index / count,
            lower + (upper - lower) * (index + 1) / count,
        )
        for index in range(count)
    ]


def gap_substitution(size: int) -> dict[sp.Symbol, sp.Expr]:
    substitution = {
        K191.R0: S / 32,
        K191.R1: sp.Integer(0),
        K191.C0: S * B / 32,
        K191.C1: sp.Integer(0),
    }
    if size == 3:
        substitution[K191.R1] = S * A / 32
        substitution[K191.C1] = S * B * C / 32
    return substitution


@lru_cache(maxsize=None)
def chart_monomial(power: int, size: int, row: int, column: int) -> sp.Expr:
    return sp.expand(
        K191.monomial_dd_matrix(power, size)[row][column].subs(gap_substitution(size))
    )


@lru_cache(maxsize=None)
def chart_cauchy(size: int, row: int, column: int) -> sp.Expr:
    return sp.factor(
        K191.cauchy_dd_matrix(size)[row][column].subs(gap_substitution(size))
    )


@lru_cache(maxsize=None)
def chart_normalization(size: int) -> sp.Expr:
    expression = sp.prod(
        1 + K191.W + row + column
        for row in K191.row_nodes(size)
        for column in K191.column_nodes(size)
    )
    return sp.factor(expression.subs(gap_substitution(size)))


def product_bounds(*bounds: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (
        math.prod(bound[0] for bound in bounds),
        math.prod(bound[1] for bound in bounds),
    )


def primitive_gap_bounds(
    size: int,
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    b_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
) -> dict[sp.Symbol, tuple[Fraction, Fraction]]:
    r0 = tuple(value / 32 for value in s_bounds)
    c0_product = product_bounds(s_bounds, b_bounds)
    c0 = tuple(value / 32 for value in c0_product)
    if size == 2:
        return {
            K191.R0: r0,
            K191.R1: (Fraction(0), Fraction(0)),
            K191.C0: c0,
            K191.C1: (Fraction(0), Fraction(0)),
        }
    r1_product = product_bounds(s_bounds, a_bounds)
    c1_product = product_bounds(s_bounds, b_bounds, c_bounds)
    return {
        K191.R0: r0,
        K191.R1: tuple(value / 32 for value in r1_product),
        K191.C0: c0,
        K191.C1: tuple(value / 32 for value in c1_product),
    }


def chart_values(
    w_bounds: tuple[Fraction, Fraction],
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    b_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
) -> dict[sp.Symbol, arb]:
    return {
        K191.W: interval(*w_bounds),
        S: interval(*s_bounds),
        A: interval(*a_bounds),
        B: interval(*b_bounds),
        C: interval(*c_bounds),
    }


def shifted_entry_enclosure(
    size: int,
    row: int,
    column: int,
    w_bounds: tuple[Fraction, Fraction],
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    b_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
) -> tuple[arb, arb]:
    gaps = primitive_gap_bounds(size, s_bounds, a_bounds, b_bounds, c_bounds)
    independent = {K191.W: w_bounds, **gaps}
    lower, upper = K193.entry_argument_bounds(size, row, column, independent)
    midpoint = (lower + upper) / 2
    shift = Fraction(round(midpoint * 512), 512)
    radius = max(shift - lower, upper - shift)
    values = chart_values(w_bounds, s_bounds, a_bounds, b_bounds, c_bounds)
    values[K191.W] = values[K191.W] - K193.ball(shift)
    coefficients = K194.shifted_coefficients(shift)
    polynomial = arb(0)
    for power in range(row + column, K193.TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * K191.evaluate_sympy_interval(
            chart_monomial(power, size, row, column), values
        )
    derivative_order = row + column
    tail_order = K193.TAYLOR_ORDER + 1
    combinatorial = Fraction(
        math.factorial(tail_order),
        math.factorial(tail_order - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (
            K193.derivative_abs_at_base(lower, tail_order)
            + arb(math.factorial(tail_order)) / K193.ball(1 + lower) ** (tail_order + 1)
        )
        / math.factorial(tail_order)
        * K193.ball(combinatorial)
        * K193.ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + arb(0, tail), tail


def chart_cell(
    size: int,
    w_bounds: tuple[Fraction, Fraction],
    s_bounds: tuple[Fraction, Fraction],
    a_bounds: tuple[Fraction, Fraction],
    b_bounds: tuple[Fraction, Fraction],
    c_bounds: tuple[Fraction, Fraction],
) -> tuple[arb, float]:
    values = chart_values(w_bounds, s_bounds, a_bounds, b_bounds, c_bounds)
    matrix = []
    maximum_tail = 0.0
    for row in range(size):
        result_row = []
        for column in range(size):
            residual, tail = shifted_entry_enclosure(
                size, row, column, w_bounds, s_bounds, a_bounds, b_bounds, c_bounds
            )
            cauchy = K191.evaluate_sympy_interval(
                chart_cauchy(size, row, column), values
            )
            result_row.append(cauchy + residual)
            maximum_tail = max(maximum_tail, float(tail))
        matrix.append(result_row)
    normalization = K191.evaluate_sympy_interval(chart_normalization(size), values)
    return normalization * K191.determinant(matrix), maximum_tail


def coordinate_certificate() -> dict[str, Any]:
    outputs = sp.Matrix([S / 32, S * A / 32, S * B / 32, S * B * C / 32])
    inputs = sp.Matrix([S, A, B, C])
    determinant = sp.factor(outputs.jacobian(inputs).det())
    expected = S**3 * B / 32**4
    if sp.expand(determinant - expected) != 0:
        raise AssertionError("unexpected projective-coordinate Jacobian")
    inverse = {
        "s": "32*r0",
        "a": "r1/r0",
        "b": "c0/r0",
        "c": "c1/c0",
    }
    ray_gaps = {
        "r0": "s/32",
        "r1": "s/64",
        "c0": "s/40",
        "c1": "s/80",
    }
    return {
        "forward_map": ["r0=s/32", "r1=s*a/32", "c0=s*b/32", "c1=s*b*c/32"],
        "inverse_map": inverse,
        "jacobian_determinant": "s^3*b/1048576",
        "jacobian_exact": True,
        "positive_on_chart_interior": True,
        "ordered_shape": "0<a<1 and 0<c<1 imply r0>r1>0 and c0>c1>0",
        "k194_ray": {"a": "1/2", "b": "4/5", "c": "1/2", "gaps": ray_gaps},
    }


def build_axis_sweep(size: int, axis: sp.Symbol) -> dict[str, Any]:
    config = SUBDIVISIONS[size]
    s_cells = split(*S_BOUNDS, config["scale"])
    shape_cells = split(*SHAPE_BOUNDS[axis], config["shape"])
    w_cells = split(Fraction(0), K193.RADIAL_WIDTH, config["radial"])
    lowers: list[float] = []
    uppers: list[float] = []
    tails: list[float] = []
    rows = []
    for shape_index, varying_bounds in enumerate(shape_cells):
        bounds = {
            symbol: (RAY[symbol], RAY[symbol]) for symbol in (A, B, C)
        }
        bounds[axis] = varying_bounds
        shape_lowers = []
        shape_uppers = []
        shape_tails = []
        for s_bounds in s_cells:
            for w_bounds in w_cells:
                regularizer, tail = chart_cell(
                    size, w_bounds, s_bounds, bounds[A], bounds[B], bounds[C]
                )
                lower = float(regularizer.lower())
                upper = float(regularizer.upper())
                if not lower > 0:
                    raise AssertionError(
                        "transverse axis cell lost positivity "
                        f"size={size} axis={axis} shape={varying_bounds} "
                        f"s={s_bounds} w={w_bounds}: {regularizer}"
                    )
                shape_lowers.append(lower)
                shape_uppers.append(upper)
                shape_tails.append(float(tail))
        rows.append(
            {
                "shape_cell": shape_index,
                "bounds": [ftext(value) for value in varying_bounds],
                "outward_cells": len(s_cells) * len(w_cells),
                "minimum_R_lower": min(shape_lowers),
                "maximum_R_upper": max(shape_uppers),
                "maximum_entry_tail": max(shape_tails),
                "strictly_positive": True,
            }
        )
        lowers.extend(shape_lowers)
        uppers.extend(shape_uppers)
        tails.extend(shape_tails)
    total = len(s_cells) * len(shape_cells) * len(w_cells)
    return {
        "subdivisions": config,
        "axis": str(axis),
        "fixed_shape": {
            str(symbol): ftext(RAY[symbol]) for symbol in (A, B, C) if symbol != axis
        },
        "shape_cells": len(rows),
        "total_outward_cells": total,
        "minimum_R_lower": min(lowers),
        "maximum_R_upper": max(uppers),
        "maximum_entry_tail": max(tails),
        "all_cells_strictly_positive": True,
        "all_axes_contiguous": all(
            cells[0][0] == bounds[0]
            and cells[-1][1] == bounds[1]
            and all(cells[i][1] == cells[i + 1][0] for i in range(len(cells) - 1))
            for cells, bounds in (
                (s_cells, S_BOUNDS),
                (shape_cells, SHAPE_BOUNDS[axis]),
                (w_cells, (Fraction(0), K193.RADIAL_WIDTH)),
            )
        ),
        "shape_cell_summaries": rows,
    }


def build_chart(size: int) -> dict[str, Any]:
    axes = (B,) if size == 2 else (A, B, C)
    sweeps = {str(axis): build_axis_sweep(size, axis) for axis in axes}
    return {
        "sweeps": sweeps,
        "total_outward_cells": sum(row["total_outward_cells"] for row in sweeps.values()),
        "minimum_R_lower": min(row["minimum_R_lower"] for row in sweeps.values()),
        "maximum_R_upper": max(row["maximum_R_upper"] for row in sweeps.values()),
        "maximum_entry_tail": max(row["maximum_entry_tail"] for row in sweeps.values()),
        "all_cells_strictly_positive": all(row["all_cells_strictly_positive"] for row in sweeps.values()),
        "all_axes_contiguous": all(row["all_axes_contiguous"] for row in sweeps.values()),
    }


def independent_controls(charts: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        w = Decimal(K193.RADIAL_WIDTH.numerator) / Decimal(K193.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + w)
        for size in (2, 3):
            for scale in (Fraction(1), Fraction(8)):
                for axis, endpoint in (
                    (A, SHAPE_BOUNDS[A][0]),
                    (A, SHAPE_BOUNDS[A][1]),
                    (B, SHAPE_BOUNDS[B][0]),
                    (B, SHAPE_BOUNDS[B][1]),
                    (C, SHAPE_BOUNDS[C][0]),
                    (C, SHAPE_BOUNDS[C][1]),
                ):
                    shape = dict(RAY)
                    shape[axis] = endpoint
                    a, b, c = shape[A], shape[B], shape[C]
                    sd = Decimal(scale.numerator) / Decimal(scale.denominator)
                    ad = Decimal(a.numerator) / Decimal(a.denominator)
                    bd = Decimal(b.numerator) / Decimal(b.denominator)
                    cd = Decimal(c.numerator) / Decimal(c.denominator)
                    row_gaps = [sd / Decimal(32), Decimal(0)] if size == 2 else [sd / Decimal(32), sd * ad / Decimal(32), Decimal(0)]
                    column_gaps = [sd * bd / Decimal(32), Decimal(0)] if size == 2 else [sd * bd / Decimal(32), sd * bd * cd / Decimal(32), Decimal(0)]
                    left = [minimum_sum * Decimal(2) / Decimal(5) + base * value for value in row_gaps]
                    right = [minimum_sum * Decimal(3) / Decimal(5) + base * value for value in column_gaps]
                    value = K191.K186.divided_difference_regularizer(left, right, 200)
                    lower = Decimal(str(charts[str(size)]["minimum_R_lower"]))
                    upper = Decimal(str(charts[str(size)]["maximum_R_upper"]))
                    if not lower <= value <= upper:
                        raise AssertionError("independent transverse point escaped chart range")
                    rows.append(
                        {
                            "size": size,
                            "scale": ftext(scale),
                            "shape": {"a": ftext(a), "b": ftext(b), "c": ftext(c)},
                            "regularizer": format(value, ".24E"),
                            "contained_in_global_chart_range": True,
                        }
                    )
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "role": "independent convergent-series controls; directed Arb cells carry the proof",
    }


def build() -> dict[str, Any]:
    predecessor = json.loads(K194_MANIFEST.read_text())
    coordinates = coordinate_certificate()
    charts = {str(size): build_chart(size) for size in (2, 3)}
    controls = independent_controls(charts)
    ray_center = predecessor["correlated_projective_spine"]["k193_fully_active_face_center_join"]["center"]
    expected_center = {"r0": "1/32", "r1": "1/64", "c0": "1/40", "c1": "1/80"}
    joins = {
        "k194_ray_is_exact_chart_section": True,
        "k194_shape_point_inside_every_shape_axis": all(
            SHAPE_BOUNDS[symbol][0] < value < SHAPE_BOUNDS[symbol][1]
            for symbol, value in RAY.items()
        ),
        "k193_face_center_exact": ray_center == expected_center,
        "k192_join_inherited_through_k193": predecessor["correlated_projective_spine"]["k193_fully_active_face_center_join"]["join_proved"],
        "all_chart_axes_contiguous": all(row["all_axes_contiguous"] for row in charts.values()),
    }
    if not all(joins.values()):
        raise AssertionError("transverse chart joins failed")
    total_cells = sum(row["total_outward_cells"] for row in charts.values())
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k194-order-six-projective-gap-spine-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "scale_range": "1/1<=s<=8/1",
            "shape_bounds": {
                "a=r1/r0": [ftext(value) for value in SHAPE_BOUNDS[A]],
                "b=c0/r0": [ftext(value) for value in SHAPE_BOUNDS[B]],
                "c=c1/c0": [ftext(value) for value in SHAPE_BOUNDS[C]],
            },
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "compact_projective_coordinates": coordinates,
        "transverse_coordinate_star": {
            "sizes": charts,
            "total_outward_cells": total_cells,
            "all_cells_strictly_positive": all(row["all_cells_strictly_positive"] for row in charts.values()),
            "common_cell_rule": "one shared (s,w) plus one varying shape-axis interval cell supplies every matrix entry and normalization before the complete determinant",
            "joins": joins,
        },
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_two_and_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_bound_applies_only_on_the_declared_transverse_coordinate_star": True,
        },
        "decision": {
            "transverse_projective_coordinate_star_serialized": True,
            "k194_ray_and_k193_k192_join_proved": True,
            "exact_ratio_coordinate_jacobian_serialized": True,
            "complete_transverse_ordered_shape_atlas": False,
            "duffy_jacobi_derivative_envelopes_serialized": False,
            "next_exact_input": "cover the compact shape complement with a two-chart max-gap atlas, then differentiate the common-cell model and compose it with the K185 Duffy/Jacobi weights",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_scale_and_shape_cell_before_complete_determinant_enclosure": True,
            "size_two_and_size_three_transverse_chart_outwardly_certified": True,
            "k194_ray_join_proved": True,
            "k193_k192_face_join_proved": True,
            "complete_transverse_arbitrary_gap_ratio_domain_covered": False,
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
        "compact_projective_coordinates": result["compact_projective_coordinates"],
        "transverse_coordinate_star": {
            "total_outward_cells": result["transverse_coordinate_star"]["total_outward_cells"],
            "all_cells_strictly_positive": result["transverse_coordinate_star"]["all_cells_strictly_positive"],
            "common_cell_rule": result["transverse_coordinate_star"]["common_cell_rule"],
            "joins": result["transverse_coordinate_star"]["joins"],
            "sizes": {
                size: {
                    **{key: value for key, value in row.items() if key != "sweeps"},
                    "sweeps": {
                        axis: {key: value for key, value in sweep.items() if key != "shape_cell_summaries"}
                        for axis, sweep in row["sweeps"].items()
                    },
                }
                for size, row in result["transverse_coordinate_star"]["sizes"].items()
            },
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
