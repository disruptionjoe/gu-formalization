#!/usr/bin/env python3
"""K283 correlated size-four projective-gap follow-through.

K282 certifies a local outward neighborhood of every size-four face center.
This successor keeps the fully active gap ratios on one common projective
scale ``t`` and extends that chart along ``1 <= t <= 5/4``.  Every cell is
preconditioned by its confluent center matrix before the determinant is
enclosed.  The result is a one-dimensional correlated spine, not a transverse
gap atlas or a mixed-Duffy/Jacobi error.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K282_PATH = Path(__file__).with_name("k282_order_seven_shifted_face_center_calculus.py")
K282_MANIFEST = ROOT / "lab/process/k282-order-seven-shifted-face-center-calculus.json"
OUTPUT = ROOT / "lab/process/k283-order-seven-projective-gap-followthrough.json"

T_MIN = Fraction(1)
T_MAX = Fraction(5, 4)
SCALE_CELLS = 32
RADIAL_CELLS = 48
PROJECTIVE_GAPS = {
    "r0": Fraction(1, 32),
    "r1": Fraction(1, 64),
    "r2": Fraction(1, 128),
    "c0": Fraction(1, 40),
    "c1": Fraction(1, 80),
    "c2": Fraction(1, 160),
}


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K280 = load_module("k280_for_k283", K280_PATH)
K282 = load_module("k282_for_k283", K282_PATH)
ctx.dps = K282.ARB_DIGITS
ctx.threads = 1


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def interval(lower: Fraction, upper: Fraction) -> arb:
    return K282.interval(lower, upper)


def projective_values(
    t_lower: Fraction, t_upper: Fraction, w_lower: Fraction, w_upper: Fraction
) -> dict[Any, arb]:
    t = interval(t_lower, t_upper)
    return {
        K282.W: interval(w_lower, w_upper),
        K282.R0: K282.ball(PROJECTIVE_GAPS["r0"]) * t,
        K282.R1: K282.ball(PROJECTIVE_GAPS["r1"]) * t,
        K282.R2: K282.ball(PROJECTIVE_GAPS["r2"]) * t,
        K282.C0: K282.ball(PROJECTIVE_GAPS["c0"]) * t,
        K282.C1: K282.ball(PROJECTIVE_GAPS["c1"]) * t,
        K282.C2: K282.ball(PROJECTIVE_GAPS["c2"]) * t,
    }


def argument_bounds(
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[Fraction, Fraction]:
    row_coefficients = (
        PROJECTIVE_GAPS["r0"], PROJECTIVE_GAPS["r1"],
        PROJECTIVE_GAPS["r2"], Fraction(0),
    )[: row + 1]
    column_coefficients = (
        PROJECTIVE_GAPS["c0"], PROJECTIVE_GAPS["c1"],
        PROJECTIVE_GAPS["c2"], Fraction(0),
    )[: column + 1]
    return (
        w_lower + min(row_coefficients) * t_lower + min(column_coefficients) * t_lower,
        w_upper + max(row_coefficients) * t_upper + max(column_coefficients) * t_upper,
    )


def shifted_entry(
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[arb, float]:
    lower, upper = argument_bounds(row, column, t_lower, t_upper, w_lower, w_upper)
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = projective_values(t_lower, t_upper, w_lower, w_upper)
    values[K282.W] -= K282.ball(shift)
    coefficients = K282.shifted_coefficients(shift)
    monomials = K282.numeric_monomial_dd_series(
        K282.TAYLOR_ORDER, row, column, values
    )
    polynomial = arb(0)
    for power in range(row + column, K282.TAYLOR_ORDER + 1):
        polynomial += coefficients[power] * monomials[power]
    derivative_order = row + column
    tail_order = K282.TAYLOR_ORDER + 1
    f_sup = K282.K193.derivative_abs_at_base(lower, tail_order)
    g_sup = arb(math.factorial(tail_order)) / K282.ball(1 + lower) ** (tail_order + 1)
    combinatorial = Fraction(
        math.factorial(tail_order),
        math.factorial(tail_order - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (f_sup + g_sup)
        / math.factorial(tail_order)
        * K282.ball(combinatorial)
        * K282.ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + arb(0, tail), float(tail)


def exact_cauchy_entry(row: int, column: int, values: dict[Any, arb]) -> arb:
    splits = itertools.combinations_with_replacement(range(column + 1), row)
    total = arb(0)
    for split in splits:
        starts = (0,) + split
        ends = split + (column,)
        term = arb(1)
        for factor, (start, end) in enumerate(zip(starts, ends)):
            row_node = K282.ROW_NODES[factor]
            row_value = arb(0) if row_node == 0 else values[row_node]
            for node_index in range(start, end + 1):
                column_node = K282.COLUMN_NODES[node_index]
                column_value = arb(0) if column_node == 0 else values[column_node]
                term /= 1 + values[K282.W] + row_value + column_value
        total += term
    return -total if (row + column) % 2 else total


def complete_matrix(
    t_lower: Fraction, t_upper: Fraction, w_lower: Fraction, w_upper: Fraction
) -> tuple[list[list[arb]], float]:
    values = projective_values(t_lower, t_upper, w_lower, w_upper)
    maximum_tail = 0.0
    matrix = []
    for row in range(4):
        result_row = []
        for column in range(4):
            residual, tail = shifted_entry(
                row, column, t_lower, t_upper, w_lower, w_upper
            )
            result_row.append(exact_cauchy_entry(row, column, values) + residual)
            maximum_tail = max(maximum_tail, tail)
        matrix.append(result_row)
    return matrix, maximum_tail


def normalization(values: dict[Any, arb]) -> arb:
    result = arb(1)
    for row_node in K282.ROW_NODES:
        row_value = arb(0) if row_node == 0 else values[row_node]
        for column_node in K282.COLUMN_NODES:
            column_value = arb(0) if column_node == 0 else values[column_node]
            result *= 1 + values[K282.W] + row_value + column_value
    return result


def projective_cell(
    t_lower: Fraction, t_upper: Fraction, w_lower: Fraction, w_upper: Fraction
) -> tuple[arb, float]:
    matrix, maximum_tail = complete_matrix(t_lower, t_upper, w_lower, w_upper)
    t_mid = (t_lower + t_upper) / 2
    w_mid = (w_lower + w_upper) / 2
    center, _ = complete_matrix(t_mid, t_mid, w_mid, w_mid)
    inverse, center_determinant = K282.matrix_inverse(center)
    delta = [
        [matrix[row][column] - center[row][column] for column in range(4)]
        for row in range(4)
    ]
    correction = K282.matrix_multiply(inverse, delta)
    identity_plus = [
        [correction[row][column] + (1 if row == column else 0) for column in range(4)]
        for row in range(4)
    ]
    values = projective_values(t_lower, t_upper, w_lower, w_upper)
    regularizer = normalization(values) * center_determinant * K282.determinant(identity_plus)
    if not regularizer.lower() > 0:
        raise AssertionError(
            f"projective cell lost positivity t={ftext(t_lower)}:{ftext(t_upper)} "
            f"w={ftext(w_lower)}:{ftext(w_upper)} value={regularizer}"
        )
    return regularizer, maximum_tail


def build_spine() -> dict[str, Any]:
    scale_step = (T_MAX - T_MIN) / SCALE_CELLS
    radial_step = K282.RADIAL_WIDTH / RADIAL_CELLS
    rows = []
    global_lowers = []
    global_uppers = []
    global_tails = []
    for scale_index in range(SCALE_CELLS):
        t_lower = T_MIN + scale_index * scale_step
        t_upper = t_lower + scale_step
        lowers = []
        uppers = []
        tails = []
        for radial_index in range(RADIAL_CELLS):
            w_lower = radial_index * radial_step
            w_upper = w_lower + radial_step
            regularizer, tail = projective_cell(t_lower, t_upper, w_lower, w_upper)
            lowers.append(float(regularizer.lower()))
            uppers.append(float(regularizer.upper()))
            tails.append(tail)
        rows.append(
            {
                "scale_cell": scale_index,
                "t_bounds": [ftext(t_lower), ftext(t_upper)],
                "radial_subcells": RADIAL_CELLS,
                "minimum_R_lower": min(lowers),
                "maximum_R_upper": max(uppers),
                "maximum_entry_tail": max(tails),
                "strictly_positive": True,
            }
        )
        global_lowers.extend(lowers)
        global_uppers.extend(uppers)
        global_tails.extend(tails)
    return {
        "scale_cells": SCALE_CELLS,
        "radial_cells_per_scale_cell": RADIAL_CELLS,
        "total_cells": SCALE_CELLS * RADIAL_CELLS,
        "cells": rows,
        "minimum_R_lower": min(global_lowers),
        "maximum_R_upper": max(global_uppers),
        "maximum_entry_tail": max(global_tails),
        "all_cells_strictly_positive": True,
        "scale_interval_contiguous": all(
            rows[index]["t_bounds"][1] == rows[index + 1]["t_bounds"][0]
            for index in range(len(rows) - 1)
        ),
        "radial_interval_contiguous": True,
    }


def point_controls(spine: dict[str, Any]) -> dict[str, Any]:
    rows = []
    with localcontext() as context:
        context.prec = 320
        base = Decimal(K282.BASE_X.numerator) / Decimal(K282.BASE_X.denominator)
        w = Decimal(K282.RADIAL_WIDTH.numerator) / Decimal(K282.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base * (Decimal(1) + w)
        for scale in (Fraction(1), Fraction(9, 8), Fraction(5, 4)):
            t = Decimal(scale.numerator) / Decimal(scale.denominator)
            left = [
                Decimal(minimum_sum * Decimal(2) / Decimal(5))
                + base * t * Decimal(PROJECTIVE_GAPS[label].numerator) / Decimal(PROJECTIVE_GAPS[label].denominator)
                for label in ("r0", "r1", "r2")
            ] + [Decimal(minimum_sum * Decimal(2) / Decimal(5))]
            right = [
                Decimal(minimum_sum * Decimal(3) / Decimal(5))
                + base * t * Decimal(PROJECTIVE_GAPS[label].numerator) / Decimal(PROJECTIVE_GAPS[label].denominator)
                for label in ("c0", "c1", "c2")
            ] + [Decimal(minimum_sum * Decimal(3) / Decimal(5))]
            value = K280.divided_regularizer(left, right, 300)
            if not Decimal(str(spine["minimum_R_lower"])) <= value <= Decimal(
                str(spine["maximum_R_upper"])
            ):
                raise AssertionError("projective point escaped certified spine range")
            rows.append(
                {
                    "scale": ftext(scale),
                    "regularizer": format(value, ".30E"),
                    "contained_in_global_spine_range": True,
                }
            )
    return {"precision_decimal_digits": 300, "rows": rows, "all_contained": True}


def build() -> dict[str, Any]:
    predecessor = json.loads(K282_MANIFEST.read_text())
    fully_active = predecessor["size_four_outward_face_charts"]["fully_active_chart"]
    expected_center = {key: ftext(value) for key, value in PROJECTIVE_GAPS.items()}
    exact_join = fully_active["center"] == expected_center
    if not exact_join:
        raise AssertionError("K283 projective ray does not join K282 fully active center")
    spine = build_spine()
    return {
        "schema_version": "1.0",
        "result_id": "K283-ORDER-SEVEN-PROJECTIVE-GAP-FOLLOWTHROUGH",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k282-order-seven-shifted-face-center-calculus.json",
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "relative_radial_width": predecessor["fixed_control"]["relative_radial_width"],
            "projective_scale_range": f"{ftext(T_MIN)}<=t<={ftext(T_MAX)}",
            "projective_gap_ray": {key: f"t*{ftext(value)}" for key, value in PROJECTIVE_GAPS.items()},
            "patterns": predecessor["fixed_control"]["nontrivial_patterns"],
            "occurrences": predecessor["fixed_control"]["nontrivial_occurrences"],
            "gram_entries": predecessor["fixed_control"]["gram_entries"],
            "groups": predecessor["fixed_control"]["groups"],
            "arb_decimal_digits": K282.ARB_DIGITS,
            "threads": 1,
        },
        "correlated_projective_spine": {
            **spine,
            "ordered_shape": "r0>r1>r2>0 and c0>c1>c2>0 for every t>0",
            "k282_fully_active_face_center_join": {
                "t": "1/1",
                "center": fully_active["center"],
                "exact_coordinate_match": exact_join,
                "radial_cell_equal": predecessor["fixed_control"]["radial_cell"]
                == f"{ftext(K282.BASE_X)}<=x<={ftext(K282.UPPER_X)}",
                "join_proved": exact_join,
            },
        },
        "independent_controls": point_controls(spine),
        "complete_family_propagation": {
            "size_four_pattern_occurrences": predecessor["fixed_control"]["occurrences_by_size"]["4"],
            "all_24_size_four_occurrences_retain_the_same_formula": predecessor["fixed_control"]["occurrences_by_size"]["4"] == 24,
            "all_408_entries_and_16_groups_remain_in_scope": True,
            "new_outward_domain_propagates_only_when_the_normalized_gap_tuple_lies_on_the_declared_projective_ray": True,
        },
        "decision": {
            "correlated_size_four_projective_spine_serialized": True,
            "contiguous_t1_to_t5_over_4_and_radial_coverage_proved": True,
            "k282_face_center_join_proved": True,
            "transverse_ordered_gap_atlas_complete": False,
            "mixed_duffy_derivatives_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "next_exact_input": "introduce transverse ordered size-four shape variables around the certified t in [1,5/4] spine, preserving one common chart before differentiating for mixed Duffy/Jacobi remainder bounds",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_entries_use_one_shared_projective_scale_cell_before_complete_determinant_enclosure": True,
            "size_four_projective_t1_t5_over_4_spine_outwardly_certified": True,
            "k282_face_center_join_proved": True,
            "transverse_arbitrary_gap_ratio_domain_covered": False,
            "mixed_duffy_derivative_envelopes_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": predecessor["ledger_effect"],
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Outward size-four projective gap spine on 1<=t<=5/4 joined to K282 and propagated to the 24 size-four occurrences only; no transverse arbitrary-gap atlas, mixed-Duffy/Jacobi error, action-column value, residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    spine = result["correlated_projective_spine"]
    return {
        "fixed_control": result["fixed_control"],
        "correlated_projective_spine": {
            key: value for key, value in spine.items() if key != "cells"
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
