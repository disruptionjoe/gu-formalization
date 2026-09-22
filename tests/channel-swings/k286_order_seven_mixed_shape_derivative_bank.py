#!/usr/bin/env python3
"""K286 conservative mixed shape-derivative bank through order four.

The certificate stays on K284's complete common determinant chart.  It bounds
the full Bessel divided-difference entries by Hermite--Genocchi derivatives,
the determinant by its complete 24-term Leibniz expansion, and the positive
sixteen-factor Cauchy normalization by its product rule.  The result is a
componentwise bank for every mixed shape derivative of total order at most
four, not an operator-norm identity and not a native action-column error.
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
K285_PATH = Path(__file__).with_name("k285_order_seven_mixed_shape_derivative_packet.py")
K285_MANIFEST = ROOT / "lab/process/k285-order-seven-mixed-shape-derivative-packet.json"
OUTPUT = ROOT / "lab/process/k286-order-seven-mixed-shape-derivative-bank.json"
MAX_ORDER = 4


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K285 = load_module("k285_for_k286", K285_PATH)
K284 = K285.K284
K283 = K285.K283
K282 = K285.K282
ctx.dps = K282.ARB_DIGITS
ctx.threads = 1


def ftext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def falling(value: int, order: int) -> int:
    return math.prod(range(value - order + 1, value + 1)) if order else 1


def determinant_product_bound(entry_bounds: list[arb], order: int) -> arb:
    """Labelled product rule for four determinant-row factors and 24 terms."""

    total = arb(0)
    for assignment in itertools.product(range(4), repeat=order):
        counts = [assignment.count(slot) for slot in range(4)]
        term = arb(1)
        for count in counts:
            term *= entry_bounds[count]
        total += term
    return 24 * total


def cell_bank(
    t_lower: Fraction,
    t_upper: Fraction,
    w_lower: Fraction,
    w_upper: Fraction,
) -> tuple[dict[int, float], float]:
    matrix, maximum_tail = K284.complete_matrix(
        t_lower, t_upper, w_lower, w_upper, True
    )
    values = K284.shape_values(t_lower, t_upper, w_lower, w_upper, True)

    entry_bounds = [
        max(value.abs_upper() for row in matrix for value in row)
    ]
    for order in range(1, MAX_ORDER + 1):
        candidates = []
        for row in range(4):
            for column in range(4):
                lower, _ = K284.argument_bounds(
                    row,
                    column,
                    t_lower,
                    t_upper,
                    w_lower,
                    w_upper,
                    True,
                )
                candidates.append(
                    K282.K193.derivative_abs_at_base(
                        lower, row + column + order
                    )
                    / (math.factorial(row) * math.factorial(column))
                )
        entry_bounds.append(max(candidates))

    factor_uppers = []
    for row_node in K282.ROW_NODES:
        row_value = arb(0) if row_node == 0 else values[row_node]
        for column_node in K282.COLUMN_NODES:
            column_value = arb(0) if column_node == 0 else values[column_node]
            factor_uppers.append(
                (1 + values[K282.W] + row_value + column_value).abs_upper()
            )
    maximum_factor = max(factor_uppers)
    normalization_bounds = [K283.normalization(values).abs_upper()]
    for order in range(1, MAX_ORDER + 1):
        # Every factor is affine in every shape coordinate it contains.  A
        # nonzero order-m product derivative assigns its labelled slots to m
        # distinct factors; P(16,m) and the largest remaining factor product
        # bound every repeated or mixed coordinate pattern.
        normalization_bounds.append(
            falling(16, order) * maximum_factor ** (16 - order)
        )

    determinant_bounds = [
        determinant_product_bound(entry_bounds, order)
        for order in range(MAX_ORDER + 1)
    ]
    regularizer_bounds: dict[int, float] = {}
    for order in range(1, MAX_ORDER + 1):
        total = arb(0)
        for split in range(order + 1):
            total += (
                math.comb(order, split)
                * normalization_bounds[split]
                * determinant_bounds[order - split]
            )
        regularizer_bounds[order] = float(total.upper())
    return regularizer_bounds, maximum_tail


def build_bank() -> dict[str, Any]:
    scale_step = (K283.T_MAX - K283.T_MIN) / K284.SCALE_CELLS
    radial_step = K282.RADIAL_WIDTH / K284.RADIAL_CELLS
    rows = []
    global_bounds = {order: [] for order in range(1, MAX_ORDER + 1)}
    global_tails = []
    for scale_index in range(K284.SCALE_CELLS):
        t_lower = K283.T_MIN + scale_index * scale_step
        t_upper = t_lower + scale_step
        local = {order: [] for order in range(1, MAX_ORDER + 1)}
        local_tails = []
        for radial_index in range(K284.RADIAL_CELLS):
            w_lower = radial_index * radial_step
            w_upper = w_lower + radial_step
            bounds, tail = cell_bank(t_lower, t_upper, w_lower, w_upper)
            for order, value in bounds.items():
                local[order].append(value)
                global_bounds[order].append(value)
            local_tails.append(tail)
            global_tails.append(tail)
        rows.append(
            {
                "scale_cell": scale_index,
                "t_bounds": [ftext(t_lower), ftext(t_upper)],
                "radial_subcells": K284.RADIAL_CELLS,
                "componentwise_mixed_derivative_abs_upper": {
                    str(order): max(values) for order, values in local.items()
                },
                "maximum_entry_tail": max(local_tails),
            }
        )
    componentwise = {
        str(order): max(values) for order, values in global_bounds.items()
    }
    operator = {
        str(order): (6 ** (order / 2)) * componentwise[str(order)]
        for order in range(1, MAX_ORDER + 1)
    }
    return {
        "scale_cells": K284.SCALE_CELLS,
        "radial_cells_per_scale_cell": K284.RADIAL_CELLS,
        "total_cells": K284.SCALE_CELLS * K284.RADIAL_CELLS,
        "shape_coordinate_count": 6,
        "maximum_derivative_order": MAX_ORDER,
        "cells": rows,
        "global_componentwise_mixed_derivative_abs_upper": componentwise,
        "global_euclidean_operator_norm_upper": operator,
        "maximum_entry_tail": max(global_tails),
        "all_bounds_finite_positive": all(
            math.isfinite(value) and value > 0
            for values in global_bounds.values()
            for value in values
        ),
    }


def point_regularizer(scale: Fraction, deviations: tuple[Fraction, ...]) -> Decimal:
    return K285.point_regularizer(scale, deviations)


def central_mixed_difference(
    scale: Fraction, labels: tuple[str, ...], step: Fraction
) -> Decimal:
    indices = [K284.GAP_LABELS.index(label) for label in labels]
    total = Decimal(0)
    for signs in itertools.product((-1, 1), repeat=len(labels)):
        deviations = [Fraction(0)] * 6
        coefficient = 1
        for index, sign in zip(indices, signs):
            deviations[index] += sign * step
            coefficient *= sign
        total += coefficient * point_regularizer(scale, tuple(deviations))
    with localcontext() as context:
        context.prec = 300
        denominator = (
            Decimal(2 * step.numerator) / Decimal(step.denominator)
        ) ** len(labels)
        return abs(total / denominator)


def finite_difference_controls(bank: dict[str, Any]) -> dict[str, Any]:
    step = K284.SHAPE_RADIUS / 16
    patterns = (
        ("r0",),
        ("c2", "c2"),
        ("r0", "r1", "c0"),
        ("r0", "r1", "c0", "c1"),
        ("r2", "r2", "c2", "c2"),
    )
    bounds = bank["global_componentwise_mixed_derivative_abs_upper"]
    rows = []
    for scale in (Fraction(1), Fraction(5, 4)):
        for pattern in patterns:
            value = central_mixed_difference(scale, pattern, step)
            bound = Decimal(str(bounds[str(len(pattern))]))
            if value > bound:
                raise AssertionError(f"mixed control escaped order {len(pattern)} bound")
            rows.append(
                {
                    "scale": ftext(scale),
                    "pattern": list(pattern),
                    "central_difference_step": ftext(step),
                    "absolute_difference_quotient": format(value, ".30E"),
                    "contained_in_componentwise_bound": True,
                }
            )
    return {"precision_decimal_digits": 300, "rows": rows, "all_contained": True}


def build() -> dict[str, Any]:
    predecessor = json.loads(K285_MANIFEST.read_text())
    bank = build_bank()
    return {
        "schema_version": "1.0",
        "result_id": "K286-ORDER-SEVEN-MIXED-SHAPE-DERIVATIVE-BANK",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            **predecessor["fixed_control"],
            "predecessor_manifest": "lab/process/k285-order-seven-mixed-shape-derivative-packet.json",
            "maximum_derivative_order": MAX_ORDER,
        },
        "derivative_identity": {
            "entry_rule": "an order-m derivative of a participating Hermite--Genocchi node list is bounded by the (row+column+m)-th completely-monotone Bessel derivative divided by row! column!",
            "determinant_rule": "all 24 determinant terms and all 4^m labelled derivative-to-row assignments are retained before absolute bounding",
            "normalization_rule": "an order-m derivative of the sixteen-factor positive normalization assigns its labelled slots to distinct affine factors and is bounded by P(16,m) times the largest remaining factor product",
            "regularizer_rule": "D^m(N det A) uses the complete binomial product rule for m=1..4",
            "componentwise_to_operator_rule": "for six coordinates, Frobenius domination gives ||D^m R||_2 <= 6^(m/2) times the componentwise bound",
        },
        "mixed_shape_derivative_bank": bank,
        "independent_controls": finite_difference_controls(bank),
        "complete_family_propagation": predecessor["complete_family_propagation"],
        "decision": {
            "mixed_shape_derivatives_through_order_four_serialized": True,
            "complete_transverse_tube_retained": True,
            "tensor_jacobi_remainder_released": True,
            "native_occurrence_measure_serialized": False,
            "next_exact_input": "compose the fourth-order bank with a positive determinant-preserving Jacobi rule on the K284 tube, then keep the normalized tube proxy separate from the missing native K179 occurrence measure",
        },
        "release_test": {
            "k284_transverse_ordered_shape_tube_retained": True,
            "all_mixed_shape_derivative_components_through_order_four_bounded": True,
            "complete_determinant_leibniz_assignments_retained": True,
            "complete_normalization_product_rule_retained": True,
            "tensor_jacobi_remainder_serialized": False,
            "native_K179_occurrence_measure_serialized": False,
            "complete_arbitrary_gap_ratio_domain_covered": False,
            "complete_base_action_column_evaluated": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": predecessor["ledger_effect"],
        "physical_or_source_selection": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Componentwise and Euclidean-operator derivative envelopes through total order four for the six K284 shape coordinates on the certified size-four tube, propagated to the 24 size-four occurrences only; no native occurrence measure, composed Jacobi error, complete arbitrary-gap simplex, action-column value, residual, exterior gap, native K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    bank = result["mixed_shape_derivative_bank"]
    return {
        "fixed_control": result["fixed_control"],
        "derivative_identity": result["derivative_identity"],
        "mixed_shape_derivative_bank": {
            key: value for key, value in bank.items() if key != "cells"
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
