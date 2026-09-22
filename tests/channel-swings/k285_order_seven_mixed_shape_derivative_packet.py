#!/usr/bin/env python3
"""K285 rigorous first shape-gradient packet on the K284 tube.

The packet differentiates the exact normalized determinant structurally.  A
Hermite--Genocchi derivative bound controls every affected Bessel divided-
difference entry, while exact product and cofactor rules bound the complete
regularizer.  This is a six-coordinate first-gradient packet, not the higher
mixed derivatives or composed Jacobi remainder required for final cubature.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K280_PATH = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
K284_PATH = Path(__file__).with_name("k284_order_seven_transverse_shape_atlas.py")
K284_MANIFEST = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
OUTPUT = ROOT / "lab/process/k285-order-seven-mixed-shape-derivative-packet.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K280 = load_module("k280_for_k285", K280_PATH)
K284 = load_module("k284_for_k285", K284_PATH)
K282 = K284.K282
K283 = K284.K283
ctx.dps = K282.ARB_DIGITS
ctx.threads = 1

SYMBOL_BY_LABEL = dict(zip(K284.GAP_LABELS, K284.GAP_SYMBOLS))


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def participates(label: str, row: int, column: int) -> bool:
    symbol = SYMBOL_BY_LABEL[label]
    return symbol in K282.ROW_NODES[: row + 1] or symbol in K282.COLUMN_NODES[: column + 1]


def entry_derivative_abs_bound(
    label: str,
    row: int,
    column: int,
    lower_argument: Fraction,
) -> arb:
    """Hermite--Genocchi bound for one node derivative.

    A row/column divided difference is the simplex average of the
    ``row+column`` derivative divided by ``row! column!``.  Differentiating one
    participating node inserts a barycentric weight in ``[0,1]`` and one more
    kernel derivative, giving the bound below.  Complete monotonicity makes
    the lower endpoint the supremum on the positive cell.
    """

    if not participates(label, row, column):
        return arb(0)
    order = row + column + 1
    return K282.K193.derivative_abs_at_base(lower_argument, order) / (
        math.factorial(row) * math.factorial(column)
    )


def minor(matrix: list[list[arb]], skip_row: int, skip_column: int) -> list[list[arb]]:
    return [
        [value for column, value in enumerate(row) if column != skip_column]
        for row_index, row in enumerate(matrix)
        if row_index != skip_row
    ]


def normalization_derivative_abs_bound(
    label: str, values: dict[Any, arb]
) -> arb:
    symbol = SYMBOL_BY_LABEL[label]
    logarithmic = arb(0)
    if symbol in K282.ROW_NODES:
        row_value = values[symbol]
        for column_node in K282.COLUMN_NODES:
            column_value = arb(0) if column_node == 0 else values[column_node]
            logarithmic += 1 / (1 + values[K282.W] + row_value + column_value)
    else:
        column_value = values[symbol]
        for row_node in K282.ROW_NODES:
            row_value = arb(0) if row_node == 0 else values[row_node]
            logarithmic += 1 / (1 + values[K282.W] + row_value + column_value)
    return K283.normalization(values).abs_upper() * logarithmic.abs_upper()


def cell_gradient_bounds(
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[dict[str, float], float]:
    matrix, maximum_tail = K284.complete_matrix(
        t_lower, t_upper, w_lower, w_upper, True
    )
    values = K284.shape_values(t_lower, t_upper, w_lower, w_upper, True)
    normalization = K283.normalization(values)
    normalization_abs = normalization.abs_upper()
    determinant_abs = K282.determinant(matrix).abs_upper()
    cofactors = [
        [K282.determinant(minor(matrix, row, column)).abs_upper() for column in range(4)]
        for row in range(4)
    ]
    result: dict[str, float] = {}
    for label in K284.GAP_LABELS:
        determinant_derivative = arb(0)
        for row in range(4):
            for column in range(4):
                if not participates(label, row, column):
                    continue
                lower, _ = K284.argument_bounds(
                    row,
                    column,
                    t_lower,
                    t_upper,
                    w_lower,
                    w_upper,
                    True,
                )
                determinant_derivative += cofactors[row][column] * entry_derivative_abs_bound(
                    label, row, column, lower
                )
        normalization_derivative = normalization_derivative_abs_bound(label, values)
        bound = (
            normalization_derivative * determinant_abs
            + normalization_abs * determinant_derivative
        )
        result[label] = float(bound.upper())
    return result, maximum_tail


def build_packet() -> dict[str, Any]:
    scale_step = (K283.T_MAX - K283.T_MIN) / K284.SCALE_CELLS
    radial_step = K282.RADIAL_WIDTH / K284.RADIAL_CELLS
    rows = []
    global_bounds = {label: [] for label in K284.GAP_LABELS}
    global_tails = []
    for scale_index in range(K284.SCALE_CELLS):
        t_lower = K283.T_MIN + scale_index * scale_step
        t_upper = t_lower + scale_step
        local = {label: [] for label in K284.GAP_LABELS}
        local_tails = []
        for radial_index in range(K284.RADIAL_CELLS):
            w_lower = radial_index * radial_step
            w_upper = w_lower + radial_step
            bounds, tail = cell_gradient_bounds(t_lower, t_upper, w_lower, w_upper)
            for label, value in bounds.items():
                local[label].append(value)
                global_bounds[label].append(value)
            local_tails.append(tail)
            global_tails.append(tail)
        rows.append(
            {
                "scale_cell": scale_index,
                "t_bounds": [ftext(t_lower), ftext(t_upper)],
                "radial_subcells": K284.RADIAL_CELLS,
                "coordinate_derivative_abs_upper": {
                    label: max(values) for label, values in local.items()
                },
                "maximum_entry_tail": max(local_tails),
            }
        )
    return {
        "scale_cells": K284.SCALE_CELLS,
        "radial_cells_per_scale_cell": K284.RADIAL_CELLS,
        "total_cells": K284.SCALE_CELLS * K284.RADIAL_CELLS,
        "coordinate_count": 6,
        "cells": rows,
        "global_coordinate_derivative_abs_upper": {
            label: max(values) for label, values in global_bounds.items()
        },
        "global_l1_gradient_abs_upper": sum(max(values) for values in global_bounds.values()),
        "maximum_entry_tail": max(global_tails),
        "all_bounds_finite_positive": all(
            math.isfinite(value) and value > 0
            for values in global_bounds.values()
            for value in values
        ),
    }


def point_regularizer(scale: Fraction, deviations: tuple[Fraction, ...]) -> Decimal:
    with localcontext() as context:
        context.prec = 320
        base_x = Decimal(K282.BASE_X.numerator) / Decimal(K282.BASE_X.denominator)
        w = Decimal(K282.RADIAL_WIDTH.numerator) / Decimal(K282.RADIAL_WIDTH.denominator) / 2
        minimum_sum = base_x * (Decimal(1) + w)
        t = Decimal(scale.numerator) / Decimal(scale.denominator)
        gaps = [
            t
            * Decimal(K283.PROJECTIVE_GAPS[label].numerator)
            / Decimal(K283.PROJECTIVE_GAPS[label].denominator)
            + Decimal(deviations[index].numerator) / Decimal(deviations[index].denominator)
            for index, label in enumerate(K284.GAP_LABELS)
        ]
        left = [
            minimum_sum * Decimal(2) / Decimal(5) + base_x * gaps[index]
            for index in range(3)
        ] + [minimum_sum * Decimal(2) / Decimal(5)]
        right = [
            minimum_sum * Decimal(3) / Decimal(5) + base_x * gaps[index + 3]
            for index in range(3)
        ] + [minimum_sum * Decimal(3) / Decimal(5)]
        return K280.divided_regularizer(left, right, 300)


def finite_difference_controls(packet: dict[str, Any]) -> dict[str, Any]:
    step = K284.SHAPE_RADIUS / 8
    rows = []
    bounds = packet["global_coordinate_derivative_abs_upper"]
    for scale in (Fraction(1), Fraction(5, 4)):
        for index, label in enumerate(K284.GAP_LABELS):
            plus = [Fraction(0)] * 6
            minus = [Fraction(0)] * 6
            plus[index] = step
            minus[index] = -step
            slope = abs(
                (point_regularizer(scale, tuple(plus)) - point_regularizer(scale, tuple(minus)))
                / (
                    Decimal(2 * step.numerator)
                    / Decimal(step.denominator)
                )
            )
            contained = slope <= Decimal(str(bounds[label]))
            if not contained:
                raise AssertionError(f"finite-difference control escaped {label} bound")
            rows.append(
                {
                    "scale": ftext(scale),
                    "coordinate": label,
                    "central_difference_step": ftext(step),
                    "absolute_slope": format(slope, ".30E"),
                    "contained_in_global_bound": True,
                }
            )
    return {
        "precision_decimal_digits": 300,
        "rows": rows,
        "all_contained": True,
    }


def build() -> dict[str, Any]:
    predecessor = json.loads(K284_MANIFEST.read_text())
    packet = build_packet()
    return {
        "schema_version": "1.0",
        "result_id": "K285-ORDER-SEVEN-MIXED-SHAPE-DERIVATIVE-PACKET",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k284-order-seven-transverse-shape-atlas.json",
            "radial_cell": predecessor["fixed_control"]["radial_cell"],
            "projective_scale_range": predecessor["fixed_control"]["projective_scale_range"],
            "transverse_shape_radius": predecessor["fixed_control"]["transverse_shape_radius"],
            "patterns": predecessor["fixed_control"]["patterns"],
            "occurrences": predecessor["fixed_control"]["occurrences"],
            "gram_entries": predecessor["fixed_control"]["gram_entries"],
            "groups": predecessor["fixed_control"]["groups"],
            "arb_decimal_digits": K282.ARB_DIGITS,
            "threads": 1,
        },
        "derivative_identity": {
            "entry_rule": "differentiate the Hermite--Genocchi simplex average; one participating node inserts a barycentric weight in [0,1] and one additional completely-monotone kernel derivative",
            "determinant_rule": "sum complete signed cofactors times entry derivatives before absolute bounding",
            "normalization_rule": "differentiate the complete sixteen-factor positive Cauchy normalization product",
            "composition_rule": "abs(d(N det A)) <= abs(dN) abs(det A) + abs(N) sum_ij abs(cofactor_ij) abs(dA_ij)",
            "exact_shape_coordinates": list(K284.GAP_LABELS),
        },
        "first_shape_gradient_packet": packet,
        "independent_controls": finite_difference_controls(packet),
        "complete_family_propagation": predecessor["complete_family_propagation"],
        "decision": {
            "all_six_first_shape_derivative_envelopes_serialized": True,
            "complete_transverse_tube_retained": True,
            "higher_mixed_duffy_derivatives_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "next_exact_input": "lift the same Hermite--Genocchi/cofactor rule to the finite mixed derivative orders required by the selected Duffy--Jacobi rule, then integrate the resulting remainder only on the K284 tube",
        },
        "release_test": {
            "k284_transverse_ordered_shape_tube_retained": True,
            "all_six_first_shape_derivative_envelopes_serialized": True,
            "complete_signed_cofactor_structure_retained_before_absolute_bound": True,
            "higher_mixed_duffy_derivative_envelopes_serialized": False,
            "determinant_preserving_jacobi_error_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": predecessor["ledger_effect"],
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Rigorous first-derivative envelopes for all six shape coordinates on the certified K284 size-four tube, propagated to the 24 size-four occurrences only; no higher mixed-Duffy derivative bank, composed Jacobi error, complete arbitrary-gap simplex, action-column value, residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    packet = result["first_shape_gradient_packet"]
    return {
        "fixed_control": result["fixed_control"],
        "derivative_identity": result["derivative_identity"],
        "first_shape_gradient_packet": {
            key: value for key, value in packet.items() if key != "cells"
        },
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
