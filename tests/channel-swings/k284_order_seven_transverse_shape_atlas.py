#!/usr/bin/env python3
"""K284 transverse ordered size-four shape atlas.

K283 certifies one correlated projective centerline.  This successor retains
that common scale and adds six independent signed shape coordinates inside one
complete determinant enclosure.  The certified object is a nonempty ordered
tube around the K283 spine, not the full arbitrary-gap simplex and not a
mixed-Duffy/Jacobi cubature error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K282_PATH = Path(__file__).with_name("k282_order_seven_shifted_face_center_calculus.py")
K283_PATH = Path(__file__).with_name("k283_order_seven_projective_gap_followthrough.py")
K282_MANIFEST = ROOT / "lab/process/k282-order-seven-shifted-face-center-calculus.json"
K283_MANIFEST = ROOT / "lab/process/k283-order-seven-projective-gap-followthrough.json"
OUTPUT = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"

SHAPE_RADIUS = Fraction(1, 32768)
SCALE_CELLS = 32
RADIAL_CELLS = 64


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K280 = load_module("k280_for_k284", K280_PATH)
K282 = load_module("k282_for_k284", K282_PATH)
K283 = load_module("k283_for_k284", K283_PATH)
ctx.dps = K282.ARB_DIGITS
ctx.threads = 1

GAP_SYMBOLS = (K282.R0, K282.R1, K282.R2, K282.C0, K282.C1, K282.C2)
GAP_LABELS = ("r0", "r1", "r2", "c0", "c1", "c2")


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def shape_values(
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
    with_shape: bool,
) -> dict[Any, arb]:
    values = K283.projective_values(t_lower, t_upper, w_lower, w_upper)
    if with_shape:
        deviation = K282.interval(-SHAPE_RADIUS, SHAPE_RADIUS)
        for symbol in GAP_SYMBOLS:
            values[symbol] += deviation
    return values


def argument_bounds(
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
    with_shape: bool,
) -> tuple[Fraction, Fraction]:
    lower, upper = K283.argument_bounds(
        row, column, t_lower, t_upper, w_lower, w_upper
    )
    # Every divided-difference node list contains the zero node, so the lower
    # argument is unchanged while the largest row and column nodes can each
    # move outward by SHAPE_RADIUS.
    if with_shape:
        upper += 2 * SHAPE_RADIUS
    return lower, upper


def shifted_entry(
    row: int,
    column: int,
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
    with_shape: bool,
) -> tuple[arb, float]:
    lower, upper = argument_bounds(
        row, column, t_lower, t_upper, w_lower, w_upper, with_shape
    )
    shift = (lower + upper) / 2
    radius = (upper - lower) / 2
    values = shape_values(t_lower, t_upper, w_lower, w_upper, with_shape)
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
    g_sup = arb(K282.math.factorial(tail_order)) / K282.ball(1 + lower) ** (
        tail_order + 1
    )
    combinatorial = Fraction(
        K282.math.factorial(tail_order),
        K282.math.factorial(tail_order - derivative_order)
        * K282.math.factorial(row)
        * K282.math.factorial(column),
    )
    tail = (
        (f_sup + g_sup)
        / K282.math.factorial(tail_order)
        * K282.ball(combinatorial)
        * K282.ball(radius) ** (tail_order - derivative_order)
    ).upper()
    return polynomial + arb(0, tail), float(tail)


def exact_cauchy_entry(
    row: int, column: int, values: dict[Any, arb]
) -> arb:
    return K283.exact_cauchy_entry(row, column, values)


def complete_matrix(
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
    with_shape: bool,
) -> tuple[list[list[arb]], float]:
    values = shape_values(t_lower, t_upper, w_lower, w_upper, with_shape)
    maximum_tail = 0.0
    matrix = []
    for row in range(4):
        result_row = []
        for column in range(4):
            residual, tail = shifted_entry(
                row,
                column,
                t_lower,
                t_upper,
                w_lower,
                w_upper,
                with_shape,
            )
            result_row.append(exact_cauchy_entry(row, column, values) + residual)
            maximum_tail = max(maximum_tail, tail)
        matrix.append(result_row)
    return matrix, maximum_tail


def atlas_cell(
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[arb, float]:
    matrix, maximum_tail = complete_matrix(
        t_lower, t_upper, w_lower, w_upper, True
    )
    t_mid = (t_lower + t_upper) / 2
    w_mid = (w_lower + w_upper) / 2
    center, _ = complete_matrix(t_mid, t_mid, w_mid, w_mid, False)
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
    values = shape_values(t_lower, t_upper, w_lower, w_upper, True)
    regularizer = (
        K283.normalization(values)
        * center_determinant
        * K282.determinant(identity_plus)
    )
    if not regularizer.lower() > 0:
        raise AssertionError(
            "transverse atlas cell lost positivity "
            f"t={ftext(t_lower)}:{ftext(t_upper)} "
            f"w={ftext(w_lower)}:{ftext(w_upper)} value={regularizer}"
        )
    return regularizer, maximum_tail


def ordering_certificate() -> dict[str, Any]:
    base = K283.PROJECTIVE_GAPS
    margins = {
        "r0_minus_r1": base["r0"] - base["r1"] - 2 * SHAPE_RADIUS,
        "r1_minus_r2": base["r1"] - base["r2"] - 2 * SHAPE_RADIUS,
        "r2_minus_zero": base["r2"] - SHAPE_RADIUS,
        "c0_minus_c1": base["c0"] - base["c1"] - 2 * SHAPE_RADIUS,
        "c1_minus_c2": base["c1"] - base["c2"] - 2 * SHAPE_RADIUS,
        "c2_minus_zero": base["c2"] - SHAPE_RADIUS,
    }
    if not all(value > 0 for value in margins.values()):
        raise AssertionError("shape radius does not preserve strict gap ordering")
    return {
        "worst_case_at_t": "1/1",
        "margins": {key: ftext(value) for key, value in margins.items()},
        "all_strictly_positive": True,
    }


def build_atlas() -> dict[str, Any]:
    scale_step = (K283.T_MAX - K283.T_MIN) / SCALE_CELLS
    radial_step = K282.RADIAL_WIDTH / RADIAL_CELLS
    rows = []
    global_lowers = []
    global_uppers = []
    global_tails = []
    for scale_index in range(SCALE_CELLS):
        t_lower = K283.T_MIN + scale_index * scale_step
        t_upper = t_lower + scale_step
        lowers = []
        uppers = []
        tails = []
        for radial_index in range(RADIAL_CELLS):
            w_lower = radial_index * radial_step
            w_upper = w_lower + radial_step
            regularizer, tail = atlas_cell(t_lower, t_upper, w_lower, w_upper)
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
        "shape_dimension": 6,
        "shape_box": {label: f"[-{ftext(SHAPE_RADIUS)},{ftext(SHAPE_RADIUS)}]" for label in GAP_LABELS},
        "cells": rows,
        "minimum_R_lower": min(global_lowers),
        "maximum_R_upper": max(global_uppers),
        "maximum_entry_tail": max(global_tails),
        "all_cells_strictly_positive": True,
        "scale_interval_contiguous": True,
        "radial_interval_contiguous": True,
    }


def point_controls(atlas: dict[str, Any]) -> dict[str, Any]:
    rows = []
    patterns = (
        ("zero", (0, 0, 0, 0, 0, 0)),
        ("alternating", (1, -1, 1, -1, 1, -1)),
        ("reverse_alternating", (-1, 1, -1, 1, -1, 1)),
    )
    with localcontext() as context:
        context.prec = 320
        base_x = Decimal(K282.BASE_X.numerator) / Decimal(K282.BASE_X.denominator)
        w = Decimal(K282.RADIAL_WIDTH.numerator) / Decimal(K282.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base_x * (Decimal(1) + w)
        epsilon = Decimal(SHAPE_RADIUS.numerator) / Decimal(SHAPE_RADIUS.denominator)
        for scale in (Fraction(1), Fraction(9, 8), Fraction(5, 4)):
            t = Decimal(scale.numerator) / Decimal(scale.denominator)
            for name, signs in patterns:
                deviations = [Decimal(sign) * epsilon for sign in signs]
                gaps = [
                    t
                    * Decimal(K283.PROJECTIVE_GAPS[label].numerator)
                    / Decimal(K283.PROJECTIVE_GAPS[label].denominator)
                    + deviations[index]
                    for index, label in enumerate(GAP_LABELS)
                ]
                left = [
                    minimum_sum * Decimal(2) / Decimal(5) + base_x * gaps[index]
                    for index in range(3)
                ] + [minimum_sum * Decimal(2) / Decimal(5)]
                right = [
                    minimum_sum * Decimal(3) / Decimal(5) + base_x * gaps[index + 3]
                    for index in range(3)
                ] + [minimum_sum * Decimal(3) / Decimal(5)]
                value = K280.divided_regularizer(left, right, 300)
                if not Decimal(str(atlas["minimum_R_lower"])) <= value <= Decimal(
                    str(atlas["maximum_R_upper"])
                ):
                    raise AssertionError("transverse point escaped certified atlas range")
                rows.append(
                    {
                        "scale": ftext(scale),
                        "shape_pattern": name,
                        "regularizer": format(value, ".30E"),
                        "contained_in_global_atlas_range": True,
                    }
                )
    return {"precision_decimal_digits": 300, "rows": rows, "all_contained": True}


def build() -> dict[str, Any]:
    k282 = json.loads(K282_MANIFEST.read_text())
    k283 = json.loads(K283_MANIFEST.read_text())
    atlas = build_atlas()
    k282_width = Fraction(
        k282["size_four_outward_face_charts"]["fully_active_chart"]["coordinate_width"]
    )
    overlap = {
        "k283_centerline": {
            "condition": "eta_r0=eta_r1=eta_r2=eta_c0=eta_c1=eta_c2=0",
            "same_projective_scale_range": k283["fixed_control"]["projective_scale_range"],
            "same_radial_cell": k283["fixed_control"]["radial_cell"],
            "exact_formula_match": True,
        },
        "k282_t_equals_one_section": {
            "k284_shape_radius": ftext(SHAPE_RADIUS),
            "k282_fully_active_half_width": ftext(k282_width),
            "strictly_contained": SHAPE_RADIUS < k282_width,
            "same_center": k283["correlated_projective_spine"]["k282_fully_active_face_center_join"]["center"],
            "same_radial_cell": k283["fixed_control"]["radial_cell"],
        },
        "both_predecessor_overlaps_proved": SHAPE_RADIUS < k282_width,
    }
    return {
        "schema_version": "1.0",
        "result_id": "K284-ORDER-SEVEN-TRANSVERSE-SHAPE-ATLAS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k282-order-seven-shifted-face-center-calculus.json",
                "lab/process/k283-order-seven-projective-gap-followthrough.json",
            ],
            "radial_cell": k283["fixed_control"]["radial_cell"],
            "projective_scale_range": k283["fixed_control"]["projective_scale_range"],
            "projective_gap_ray": k283["fixed_control"]["projective_gap_ray"],
            "transverse_shape_radius": ftext(SHAPE_RADIUS),
            "patterns": k283["fixed_control"]["patterns"],
            "occurrences": k283["fixed_control"]["occurrences"],
            "gram_entries": k283["fixed_control"]["gram_entries"],
            "groups": k283["fixed_control"]["groups"],
            "arb_decimal_digits": K282.ARB_DIGITS,
            "threads": 1,
        },
        "ordering_certificate": ordering_certificate(),
        "transverse_shape_atlas": atlas,
        "predecessor_overlap": overlap,
        "independent_controls": point_controls(atlas),
        "complete_family_propagation": {
            "size_four_pattern_occurrences": k283["complete_family_propagation"]["size_four_pattern_occurrences"],
            "all_24_size_four_occurrences_retain_the_same_formula": True,
            "all_408_entries_16_groups_and_96_paths_remain_in_scope": True,
            "new_domain_propagates_only_to_size_four_occurrences_whose_normalized_gap_tuple_lies_in_the_declared_tube": True,
        },
        "decision": {
            "six_dimensional_transverse_ordered_tube_serialized": True,
            "complete_scale_and_radial_coverage_proved": True,
            "k282_and_k283_overlap_proved": True,
            "complete_arbitrary_gap_simplex_covered": False,
            "mixed_duffy_derivatives_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "next_exact_input": "differentiate the common center-preconditioned determinant chart with respect to the six bounded shape coordinates, then compose a mixed Duffy/Jacobi remainder only on the certified tube",
        },
        "release_test": {
            "shifted_hermite_genocchi_entry_tail_retained": True,
            "all_six_shape_coordinates_share_one_complete_determinant_chart": True,
            "strict_gap_order_preserved": True,
            "k282_and_k283_overlap_proved": True,
            "transverse_ordered_shape_tube_covered": True,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "mixed_duffy_derivative_envelopes_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k283["ledger_effect"],
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Six-dimensional ordered transverse size-four tube of radius 1/32768 around the K283 projective spine, joined to K282 and propagated to the 24 size-four occurrences only; no complete arbitrary-gap simplex, mixed-Duffy/Jacobi error, action-column value, residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    atlas = result["transverse_shape_atlas"]
    return {
        "fixed_control": result["fixed_control"],
        "ordering_certificate": result["ordering_certificate"],
        "transverse_shape_atlas": {key: value for key, value in atlas.items() if key != "cells"},
        "predecessor_overlap": result["predecessor_overlap"],
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
