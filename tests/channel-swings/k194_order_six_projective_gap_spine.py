#!/usr/bin/env python3
"""K194 correlated projective-gap spine for K186 regularizers.

K193 proved outward boxes around the finite face bank, but independently
ranging every gap discards the physical correlation between ordered nodes.
This certificate keeps the K193 shifted Hermite--Genocchi entries and writes

    r0=t/32, r1=t/64, c0=t/40, c1=t/80.

One common interval cell for ``t`` supplies every matrix entry and the Cauchy
normalization before the complete interval determinant is evaluated.  The
determinant enclosure is outward and does not claim affine dependency between
its entry balls.  Contiguous scale and radial cells then certify the size-two
and size-three regularizers on a projective spine.  This is a one-dimensional
shape ray, not a transverse ordered-gap atlas or a Duffy/Jacobi cubature
remainder.
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
K193_PATH = ROOT / "tests/channel-swings/k193_order_six_shifted_face_entry.py"
K193_MANIFEST = ROOT / "lab/process/k193-order-six-shifted-face-entry-wave.json"
OUTPUT = ROOT / "lab/process/k194-order-six-projective-gap-spine-wave.json"

T = sp.symbols("t")
T_MIN = Fraction(1)
T_MAX = Fraction(8)
SUBDIVISIONS = {
    2: {"scale_cells": 64, "radial_cells": 16},
    3: {"scale_cells": 256, "radial_cells": 16},
}
PROJECTIVE_GAPS = {
    "r0": Fraction(1, 32),
    "r1": Fraction(1, 64),
    "c0": Fraction(1, 40),
    "c1": Fraction(1, 80),
}
POINT_SCALES = (Fraction(1), Fraction(4), Fraction(8))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K193 = load_module("k193_for_k194", K193_PATH)
K191 = K193.K191
ctx.dps = K193.ARB_DIGITS
ctx.threads = 1


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def interval(lower: Fraction, upper: Fraction) -> arb:
    return K191.interval_from_bounds(lower, upper)


def projective_nodes(size: int) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    if size == 2:
        return (PROJECTIVE_GAPS["r0"], Fraction(0)), (
            PROJECTIVE_GAPS["c0"], Fraction(0)
        )
    if size == 3:
        return (
            PROJECTIVE_GAPS["r0"], PROJECTIVE_GAPS["r1"], Fraction(0)
        ), (
            PROJECTIVE_GAPS["c0"], PROJECTIVE_GAPS["c1"], Fraction(0)
        )
    raise ValueError("K194 admits only sizes two and three")


def projective_substitution(size: int) -> dict[sp.Symbol, sp.Expr]:
    substitution = {
        K191.R0: sp.Rational(PROJECTIVE_GAPS["r0"].numerator, PROJECTIVE_GAPS["r0"].denominator) * T,
        K191.C0: sp.Rational(PROJECTIVE_GAPS["c0"].numerator, PROJECTIVE_GAPS["c0"].denominator) * T,
        K191.R1: sp.Integer(0),
        K191.C1: sp.Integer(0),
    }
    if size == 3:
        substitution[K191.R1] = sp.Rational(
            PROJECTIVE_GAPS["r1"].numerator, PROJECTIVE_GAPS["r1"].denominator
        ) * T
        substitution[K191.C1] = sp.Rational(
            PROJECTIVE_GAPS["c1"].numerator, PROJECTIVE_GAPS["c1"].denominator
        ) * T
    return substitution


@lru_cache(maxsize=None)
def projective_monomial(power: int, size: int, row: int, column: int) -> sp.Expr:
    return sp.expand(
        K191.monomial_dd_matrix(power, size)[row][column].subs(
            projective_substitution(size)
        )
    )


@lru_cache(maxsize=None)
def projective_cauchy(size: int, row: int, column: int) -> sp.Expr:
    return sp.factor(
        K191.cauchy_dd_matrix(size)[row][column].subs(projective_substitution(size))
    )


@lru_cache(maxsize=None)
def projective_normalization(size: int) -> sp.Expr:
    expression = sp.prod(
        1 + K191.W + row + column
        for row in K191.row_nodes(size)
        for column in K191.column_nodes(size)
    )
    return sp.factor(expression.subs(projective_substitution(size)))


@lru_cache(maxsize=None)
def shifted_coefficients(shift: Fraction) -> tuple[arb, ...]:
    return K193.shifted_coefficients(shift, K193.TAYLOR_ORDER)


def entry_argument_bounds(
    size: int,
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[Fraction, Fraction]:
    row_nodes, column_nodes = projective_nodes(size)
    row_prefix = row_nodes[: row + 1]
    column_prefix = column_nodes[: column + 1]
    return (
        w_lower + min(row_prefix) * t_lower + min(column_prefix) * t_lower,
        w_upper + max(row_prefix) * t_upper + max(column_prefix) * t_upper,
    )


def shifted_entry_enclosure(
    size: int,
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[arb, arb]:
    lower, upper = entry_argument_bounds(
        size, row, column, t_lower, t_upper, w_lower, w_upper
    )
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = {
        K191.W: interval(w_lower - shift, w_upper - shift),
        T: interval(t_lower, t_upper),
    }
    coefficients = shifted_coefficients(shift)
    polynomial = arb(0)
    for power in range(row + column, K193.TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * K191.evaluate_sympy_interval(
            projective_monomial(power, size, row, column), values
        )

    derivative_order = row + column
    tail_order = K193.TAYLOR_ORDER + 1
    f_sup = K193.derivative_abs_at_base(lower, tail_order)
    g_sup = arb(math.factorial(tail_order)) / K193.ball(1 + lower) ** (tail_order + 1)
    combinatorial = Fraction(
        math.factorial(tail_order),
        math.factorial(tail_order - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (f_sup + g_sup)
        / math.factorial(tail_order)
        * K193.ball(combinatorial)
        * K193.ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + arb(0, tail), tail


def projective_cell(
    size: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[arb, float]:
    values = {
        K191.W: interval(w_lower, w_upper),
        T: interval(t_lower, t_upper),
    }
    matrix = []
    maximum_tail = 0.0
    for row in range(size):
        result_row = []
        for column in range(size):
            residual, tail = shifted_entry_enclosure(
                size, row, column, t_lower, t_upper, w_lower, w_upper
            )
            cauchy = K191.evaluate_sympy_interval(
                projective_cauchy(size, row, column), values
            )
            result_row.append(cauchy + residual)
            maximum_tail = max(maximum_tail, float(tail))
        matrix.append(result_row)
    normalization = K191.evaluate_sympy_interval(projective_normalization(size), values)
    return normalization * K191.determinant(matrix), maximum_tail


def exact_translated_evaluation_checks() -> dict[str, Any]:
    shift = Fraction(7, 64)
    substitution = {
        K191.W: K191.W - sp.Rational(shift.numerator, shift.denominator)
    }
    values = {
        K191.W: interval(Fraction(-3, 64), Fraction(-1, 64)),
        K191.R0: interval(Fraction(1, 64), Fraction(1, 32)),
        K191.R1: interval(Fraction(1, 128), Fraction(1, 64)),
        K191.C0: interval(Fraction(1, 80), Fraction(1, 40)),
        K191.C1: interval(Fraction(1, 160), Fraction(1, 80)),
    }
    checked = 0
    overlapping = 0
    for size in (2, 3):
        for power in range(K193.TAYLOR_ORDER + 1):
            original = K191.monomial_dd_matrix(power, size)
            shifted = K193.shifted_monomial_dd_matrix(power, size, shift)
            for row in range(size):
                for column in range(size):
                    exact = sp.expand(original[row][column].subs(substitution) - shifted[row][column])
                    if exact != 0:
                        raise AssertionError("translated polynomial identity failed")
                    slow = K191.evaluate_sympy_interval(shifted[row][column], values)
                    translated_values = dict(values)
                    translated_values[K191.W] = values[K191.W] - K193.ball(shift)
                    fast = K191.evaluate_sympy_interval(
                        original[row][column], translated_values
                    )
                    if slow.upper() < fast.lower() or fast.upper() < slow.lower():
                        raise AssertionError("fast translated interval escaped exact shifted evaluation")
                    checked += 1
                    overlapping += 1
    return {
        "rational_shift": ftext(shift),
        "matrix_entries_checked": checked,
        "symbolic_identities_exact": True,
        "interval_evaluations_overlap": overlapping,
        "fast_rule": "evaluate the original exact monomial divided-difference polynomial with w replaced by the translated interval w-a; no per-chart symbolic re-expansion",
    }


def build_spine(size: int) -> dict[str, Any]:
    scale_cells = SUBDIVISIONS[size]["scale_cells"]
    radial_cells = SUBDIVISIONS[size]["radial_cells"]
    rows = []
    all_lowers: list[float] = []
    all_uppers: list[float] = []
    all_tails: list[float] = []
    radial_bounds = [
        (
            K193.RADIAL_WIDTH * radial_index / radial_cells,
            K193.RADIAL_WIDTH * (radial_index + 1) / radial_cells,
        )
        for radial_index in range(radial_cells)
    ]
    radial_interval_contiguous = (
        radial_bounds[0][0] == 0
        and radial_bounds[-1][1] == K193.RADIAL_WIDTH
        and all(
            radial_bounds[index][1] == radial_bounds[index + 1][0]
            for index in range(len(radial_bounds) - 1)
        )
    )
    if not radial_interval_contiguous:
        raise AssertionError("radial subdivision is not a contiguous partition")
    for scale_index in range(scale_cells):
        t_lower = T_MIN + (T_MAX - T_MIN) * scale_index / scale_cells
        t_upper = T_MIN + (T_MAX - T_MIN) * (scale_index + 1) / scale_cells
        lowers = []
        uppers = []
        tails = []
        for w_lower, w_upper in radial_bounds:
            regularizer, tail = projective_cell(
                size, t_lower, t_upper, w_lower, w_upper
            )
            lower = float(regularizer.lower())
            upper = float(regularizer.upper())
            if not lower > 0:
                raise AssertionError(
                    f"projective cell lost positivity size={size} t={t_lower}:{t_upper} w={w_lower}:{w_upper}: {regularizer}"
                )
            lowers.append(lower)
            uppers.append(upper)
            tails.append(tail)
        rows.append(
            {
                "scale_cell": scale_index,
                "t_bounds": [ftext(t_lower), ftext(t_upper)],
                "radial_subcells": radial_cells,
                "minimum_R_lower": min(lowers),
                "maximum_R_upper": max(uppers),
                "maximum_entry_tail": max(tails),
                "strictly_positive": True,
            }
        )
        all_lowers.extend(lowers)
        all_uppers.extend(uppers)
        all_tails.extend(tails)
    return {
        "scale_cells": scale_cells,
        "radial_cells_per_scale_cell": radial_cells,
        "total_cells": scale_cells * radial_cells,
        "cells": rows,
        "minimum_R_lower": min(all_lowers),
        "maximum_R_upper": max(all_uppers),
        "maximum_entry_tail": max(all_tails),
        "all_cells_strictly_positive": True,
        "scale_interval_contiguous": all(
            rows[index]["t_bounds"][1] == rows[index + 1]["t_bounds"][0]
            for index in range(len(rows) - 1)
        ),
        "radial_interval_contiguous": radial_interval_contiguous,
    }


def generic_shifted_entry(
    size: int,
    row: int,
    column: int,
    bounds: dict[sp.Symbol, tuple[Fraction, Fraction]],
) -> arb:
    lower, upper = K193.entry_argument_bounds(size, row, column, bounds)
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = K193.interval_values(bounds)
    values[K191.W] = values[K191.W] - K193.ball(shift)
    coefficients = shifted_coefficients(shift)
    polynomial = arb(0)
    for power in range(row + column, K193.TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * K191.evaluate_sympy_interval(
            K191.monomial_dd_matrix(power, size)[row][column], values
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
    return polynomial + arb(0, tail)


def uncorrelated_hull_control() -> dict[str, Any]:
    bounds = {
        K191.W: (Fraction(0), K193.RADIAL_WIDTH),
        K191.R0: (PROJECTIVE_GAPS["r0"] * T_MIN, PROJECTIVE_GAPS["r0"] * T_MAX),
        K191.R1: (PROJECTIVE_GAPS["r1"] * T_MIN, PROJECTIVE_GAPS["r1"] * T_MAX),
        K191.C0: (PROJECTIVE_GAPS["c0"] * T_MIN, PROJECTIVE_GAPS["c0"] * T_MAX),
        K191.C1: (PROJECTIVE_GAPS["c1"] * T_MIN, PROJECTIVE_GAPS["c1"] * T_MAX),
    }
    values = K193.interval_values(bounds)
    matrix = []
    for row in range(3):
        matrix.append(
            [
                K191.evaluate_sympy_interval(K191.cauchy_dd_matrix(3)[row][column], values)
                + generic_shifted_entry(3, row, column, bounds)
                for column in range(3)
            ]
        )
    normalization = K191.evaluate_sympy_interval(
        sp.prod(
            1 + K191.W + row + column
            for row in K191.row_nodes(3)
            for column in K191.column_nodes(3)
        ),
        values,
    )
    regularizer = normalization * K191.determinant(matrix)
    if regularizer.lower() > 0:
        raise AssertionError("uncorrelated projective hull unexpectedly certified")
    return {
        "independent_coordinate_hull": {
            str(symbol): [ftext(lower), ftext(upper)]
            for symbol, (lower, upper) in bounds.items()
        },
        "R_lower": float(regularizer.lower()),
        "R_upper": float(regularizer.upper()),
        "strict_positive_certificate_rejected": True,
        "role": "baseline dependency-loss control only; the independent hull contains shapes outside the correlated ray and says nothing negative about the physical regularizer",
    }


def point_controls(spines: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    with localcontext() as context:
        context.prec = 220
        base = Decimal(K193.BASE_X.numerator) / Decimal(K193.BASE_X.denominator)
        w = Decimal(K193.RADIAL_WIDTH.numerator) / Decimal(K193.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + w)
        for size in (2, 3):
            for scale in POINT_SCALES:
                scale_decimal = Decimal(scale.numerator) / Decimal(scale.denominator)
                row_coefficients, column_coefficients = projective_nodes(size)
                left = [
                    minimum_sum * Decimal(2) / Decimal(5)
                    + base * scale_decimal * Decimal(value.numerator) / Decimal(value.denominator)
                    for value in row_coefficients
                ]
                right = [
                    minimum_sum * Decimal(3) / Decimal(5)
                    + base * scale_decimal * Decimal(value.numerator) / Decimal(value.denominator)
                    for value in column_coefficients
                ]
                value = K191.K186.divided_difference_regularizer(left, right, 200)
                global_lower = Decimal(str(spines[str(size)]["minimum_R_lower"]))
                global_upper = Decimal(str(spines[str(size)]["maximum_R_upper"]))
                contained = global_lower <= value <= global_upper
                if not contained:
                    raise AssertionError("independent projective point escaped the certified spine range")
                rows.append(
                    {
                        "size": size,
                        "scale": ftext(scale),
                        "regularizer": format(value, ".24E"),
                        "contained_in_global_spine_range": True,
                    }
                )
    return {
        "precision_decimal_digits": 200,
        "rows": rows,
        "all_contained": True,
        "role": "independent convergent-series divided-difference controls; directed Arb cells carry the proof",
    }


def build() -> dict[str, Any]:
    predecessor = json.loads(K193_MANIFEST.read_text())
    translated = exact_translated_evaluation_checks()
    spines = {str(size): build_spine(size) for size in (2, 3)}
    controls = point_controls(spines)
    uncorrelated = uncorrelated_hull_control()
    face_center = predecessor["outward_face_charts"]["sizes"]["3"][-1]["center"]
    projective_face_center = {
        key: ftext(value) for key, value in PROJECTIVE_GAPS.items()
    }
    exact_coordinate_match = face_center == projective_face_center
    expected_radial_cell = f"{ftext(K193.BASE_X)}<=x<={ftext(K193.UPPER_X)}"
    radial_cell_equal = (
        predecessor["fixed_control"]["radial_cell"] == expected_radial_cell
        and predecessor["fixed_control"]["relative_radial_width"]
        == ftext(K193.RADIAL_WIDTH)
    )
    join_proved = exact_coordinate_match and radial_cell_equal
    if not join_proved:
        raise AssertionError("K194 does not exactly join the declared K193 face cell")
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k193-order-six-shifted-face-entry-wave.json",
            "source_manifest": predecessor["fixed_control"]["source_manifest"],
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "relative_radial_width": predecessor["fixed_control"]["relative_radial_width"],
            "projective_scale_range": f"{ftext(T_MIN)}<=t<={ftext(T_MAX)}",
            "projective_gap_ray": {key: f"t*{ftext(value)}" for key, value in PROJECTIVE_GAPS.items()},
            "maximum_gap_ratios": {key: ftext(value * T_MAX) for key, value in PROJECTIVE_GAPS.items()},
            "taylor_order": K193.TAYLOR_ORDER,
            "arb_decimal_digits": K193.ARB_DIGITS,
            "threads": 1,
            "source_patterns": predecessor["fixed_control"]["source_patterns"],
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "translated_interval_operator": translated,
        "correlated_projective_spine": {
            "sizes": spines,
            "total_outward_cells": sum(row["total_cells"] for row in spines.values()),
            "all_cells_strictly_positive": all(
                row["all_cells_strictly_positive"] for row in spines.values()
            ),
            "ordered_shape": "r0>r1>0 and c0>c1>0 for every t>0",
            "all_scale_and_radial_cells_contiguous": all(
                row["scale_interval_contiguous"] and row["radial_interval_contiguous"]
                for row in spines.values()
            ),
            "k193_fully_active_face_center_join": {
                "t": "1/1",
                "center": face_center,
                "exact_coordinate_match": exact_coordinate_match,
                "radial_cell_equal": radial_cell_equal,
                "join_proved": join_proved,
            },
        },
        "dependency_loss_control": uncorrelated,
        "independent_controls": controls,
        "complete_family_propagation": {
            "operator_applies_to_every_size_two_and_three_regularizer": True,
            "all_53_patterns_retain_the_same_formula": predecessor["fixed_control"]["source_patterns"] == 53,
            "all_468_occurrences_retain_the_same_formula": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "all_234_entries_and_18_groups_remain_in_scope": True,
            "new_outward_domain_propagates_only_when_the_normalized_gap_tuple_lies_on_the_declared_projective_ray": True,
        },
        "decision": {
            "fast_translated_interval_evaluator_serialized": True,
            "correlated_ordered_gap_spine_serialized": True,
            "contiguous_overlap_and_k193_join_proved": True,
            "independent_coordinate_dependency_loss_exposed": True,
            "transverse_ordered_gap_atlas_complete": False,
            "duffy_jacobi_composition_released": False,
            "next_exact_input": "introduce ordered projective shape variables around and beyond the certified ray, supplying every entry from one common scale cell before the outward complete-determinant enclosure; tile that transverse shape domain before differentiating the common-chart model for Duffy/Jacobi remainder bounds",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_projective_scale_cell_before_complete_determinant_enclosure": True,
            "size_two_and_size_three_projective_spines_outwardly_certified": True,
            "k193_face_center_join_proved": True,
            "transverse_arbitrary_gap_ratio_domain_covered": False,
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
        "translated_interval_operator": result["translated_interval_operator"],
        "correlated_projective_spine": {
            "total_outward_cells": result["correlated_projective_spine"]["total_outward_cells"],
            "all_cells_strictly_positive": result["correlated_projective_spine"]["all_cells_strictly_positive"],
            "ordered_shape": result["correlated_projective_spine"]["ordered_shape"],
            "all_scale_and_radial_cells_contiguous": result["correlated_projective_spine"]["all_scale_and_radial_cells_contiguous"],
            "k193_fully_active_face_center_join": result["correlated_projective_spine"]["k193_fully_active_face_center_join"],
            "sizes": {
                size: {key: value for key, value in row.items() if key != "cells"}
                for size, row in result["correlated_projective_spine"]["sizes"].items()
            },
        },
        "dependency_loss_control": result["dependency_loss_control"],
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
