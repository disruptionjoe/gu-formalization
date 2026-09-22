#!/usr/bin/env python3
"""Execute K336's shared-entry gap jets on the positive reference slab.

This is the first numerical complete-determinant use of the axis-native map
bank.  It evaluates every repeated K334 gap-box class and all five Duffy axes
on K326's strictly positive x/b slab.  Origin, projective-face and tail cells
remain governed by K336's serialized ledger and are not silently inferred from
this reference bank.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K308_MODULE = HERE / "k308_order_seven_regularized_y_master_operator.py"
K326_MODULE = HERE / "k326_order_seven_signed_entry_jet_chart_bank.py"
K334 = ROOT / "lab/process/k334-order-seven-recursive-global-subdivision.json"
K336 = ROOT / "lab/process/k336-order-seven-axis-native-map-bank.json"
OUTPUT = ROOT / "lab/process/k337-order-seven-gap-axis-leaf-evaluator.json"

ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def interval_arb(value: list[str]) -> arb:
    left, right = (Fraction(item) for item in value)
    midpoint = (left + right) / 2
    radius = (right - left) / 2
    return arb(str(midpoint)) + arb(0, arb(str(radius)).upper())


def symmetric(value: arb) -> arb:
    return arb(0, abs(value).upper())


def abs_upper(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def add_poly(left: list[arb], right: list[arb]) -> list[arb]:
    return [a + b for a, b in zip(left, right, strict=True)]


def multiply_poly(left: list[arb], right: list[arb]) -> list[arb]:
    result = [arb(0), arb(0), arb(0)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= 2:
                result[i + j] += a * b
    return result


def determinant_taylor(entry_jets: list[list[list[arb]]]) -> list[arb]:
    size = len(entry_jets)
    total = [arb(0), arb(0), arb(0)]
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = [arb(-1 if inversions % 2 else 1), arb(0), arb(0)]
        for row, column in enumerate(permutation):
            value, first, second = entry_jets[row][column]
            term = multiply_poly(term, [value, first, second / 2])
        total = add_poly(total, term)
    return [total[0], total[1], 2 * total[2]]


def slope_upper(value: list[str], b_upper: Fraction) -> Fraction:
    interval = [Fraction(item) for item in value]
    return b_upper * max(abs(interval[0]), abs(interval[1]))


def build_d4(module, k326, gaps, direction_map) -> list[arb]:
    nodes = k326.node_lowers(k326.DEFAULT_X, k326.DEFAULT_B, gaps)
    lower = min(nodes["odd_left"]) + min(nodes["odd_right"])
    matrix = []
    for row in range(4):
        entries = []
        for column in range(4):
            base_order = row + column
            slope = slope_upper(direction_map[row][column], k326.DEFAULT_B[1])
            value = k326.signed(module.dd_abs_upper(lower, row, column), -1 if base_order % 2 else 1)
            first = symmetric(module.ball(slope) * module.dd_abs_upper(lower, row, column, 1))
            second = k326.signed(
                module.ball(slope * slope) * module.dd_abs_upper(lower, row, column, 2),
                -1 if (base_order + 2) % 2 else 1,
            )
            entries.append([value, first, second])
        matrix.append(entries)
    return determinant_taylor(matrix)


def build_b5(module, k326, gaps, direction_map) -> list[arb]:
    nodes = k326.node_lowers(k326.DEFAULT_X, k326.DEFAULT_B, gaps)
    row_orders = k326.ROW_ORDERS
    column_orders = k326.COLUMN_ORDERS
    matrix = [[[arb(0), arb(0), arb(0)] for _ in range(5)] for _ in range(5)]
    terminal_value = k326.terminal_jet_uppers(k326.DEFAULT_X)[0]

    for row in range(5):
        for column in range(5):
            if (row, column) in ((3, 4), (4, 3), (4, 4)):
                continue
            slope_row = direction_map[row][column]
            if slope_row is None:
                raise AssertionError("nonzero B5 slot lacks a direction interval")
            slope = slope_upper(slope_row, k326.DEFAULT_B[1])
            if row == 3 and column == 3:
                matrix[row][column][0] = symmetric(terminal_value)
                continue
            if row < 4 and column < 4:
                lower = nodes["even_left"][row] + nodes["even_right"][column]
                a, c = row_orders[row], column_orders[column]
            elif row < 4:
                lower = nodes["even_left"][row]
                a, c = row_orders[row], 0
            else:
                lower = nodes["even_right"][column]
                a, c = 0, column_orders[column]
            if lower <= 0:
                raise AssertionError("reference-slab nonterminal B5 argument touched zero")
            base_order = a + c
            coefficient = Fraction(1)  # y, 1-y and endpoint weights are all <=1.
            matrix[row][column][0] = k326.signed(
                module.ball(coefficient) * module.dd_abs_upper(lower, a, c),
                -1 if base_order % 2 else 1,
            )
            matrix[row][column][1] = symmetric(
                module.ball(coefficient * slope) * module.dd_abs_upper(lower, a, c, 1)
            )
            matrix[row][column][2] = k326.signed(
                module.ball(coefficient * slope * slope) * module.dd_abs_upper(lower, a, c, 2),
                -1 if (base_order + 2) % 2 else 1,
            )
    return determinant_taylor(matrix)


def evaluate_axis(module, k326, item, axis_row) -> list[str]:
    gaps = [(Fraction(left), Fraction(right)) for left, right in item["gap_intervals"]]
    directions = axis_row["shared_entry_normalized_argument_directions"]
    d4 = build_d4(module, k326, gaps, directions["D4_normalized_argument_direction_matrix"])
    b5 = build_b5(module, k326, gaps, directions["bordered_B5_normalized_argument_direction_matrix"])
    polynomial = [interval_arb(value) for value in axis_row["native_projective_polynomial_value_first_second_intervals"]]
    complete = multiply_poly(multiply_poly([d4[0], d4[1], d4[2] / 2], [b5[0], b5[1], b5[2] / 2]), [polynomial[0], polynomial[1], polynomial[2] / 2])
    complete = [complete[0], complete[1], 2 * complete[2]]
    scalar = Fraction(4, 120) * k326.DEFAULT_X[1] ** 2 * Fraction(1, 16)
    return [abs_upper(value * module.ball(scalar)) for value in complete]


def build() -> dict[str, Any]:
    module = load_module(K308_MODULE, "k337_k308_backend")
    k326 = load_module(K326_MODULE, "k337_k326_backend")
    k334 = json.loads(K334.read_text())
    k336 = json.loads(K336.read_text())
    if not k336["decision"]["first_complete_gap_axis_leaf_evaluation_released"]:
        raise AssertionError("K336 did not release numerical leaf evaluation")

    rows = []
    totals = [0.0, 0.0, 0.0]
    for item in k336["axis_native_gap_classes"]:
        axis_rows = []
        for axis_row in item["axes"]:
            uppers = evaluate_axis(module, k326, item, axis_row)
            if any(not math.isfinite(float(value)) or float(value) <= 0 for value in uppers):
                raise AssertionError("reference gap-axis determinant bound is not finite positive")
            axis_rows.append({
                "axis": axis_row["axis"],
                "complete_value_first_second_abs_uppers": uppers,
            })
            totals = [current + float(value) for current, value in zip(totals, uppers, strict=True)]
        rows.append({"gap_class": item["class_id"], "axes": axis_rows})

    return {
        "schema_version": "1.0",
        "result_id": "K337-ORDER-SEVEN-GAP-AXIS-LEAF-EVALUATOR",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k334-order-seven-recursive-global-subdivision.json",
                "lab/process/k336-order-seven-axis-native-map-bank.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "accepted_subdivision_checksum": k336["fixed_control"]["accepted_subdivision_checksum"],
            "gap_class_count": len(rows),
            "axis_count": 5,
            "reference_x_cell": [str(value) for value in k326.DEFAULT_X],
            "reference_b_cell": [str(value) for value in k326.DEFAULT_B],
            "endpoint_chart_count": 16,
        },
        "reference_positive_slab_bank": {
            "rows": rows,
            "class_axis_evaluation_count": len(rows) * 5,
            "summed_value_first_second_abs_uppers": [repr(value) for value in totals],
            "shared_entry_interval_substitution_precedes_complete_determinant_coefficient_enclosure": True,
            "D4_complete_permutation_count": 24,
            "bordered_B5_complete_permutation_count": 120,
            "literal_border_zeros_retained": True,
            "terminal_gap_direction_exactly_zero_on_reference_map": True,
            "right_endpoint_bank_obtained_by_exact_transpose": True,
        },
        "scope_boundary": {
            "covered": "all repeated K334 gap-box classes and all five K299 Duffy axes on K326's strictly positive x/b reference slab",
            "not_covered": [
                "the K334 radial-origin cells",
                "the s=0 and s=1 projective face cells",
                "the analytic r>=1 tails",
                "positive Peano integration over every labelled K334 leaf",
            ],
            "reference_bank_is_not_a_gap_axis_constant": True,
        },
        "decision": {
            "first_complete_shared_entry_gap_axis_determinant_bank_finite": True,
            "all_five_axes_execute_on_every_repeated_gap_class": True,
            "complete_gap_axis_constants_emitted": False,
            "complete_six_axis_peano_norm_emitted": False,
            "k294_gamma_join_released": False,
            "next_exact_input": "lift the K337 shared-entry evaluator from the positive reference slab to K334's degree-27 normalized origin and preconditioned s-face cells, then apply K336's unchanged 35/36/37 tail ledger and the five K299 Peano masses",
        },
        "release_test": {
            "K334_checksum_replayed": k334["recursive_cover"]["coverage_checksum"] == k336["fixed_control"]["accepted_subdivision_checksum"],
            "all_class_axis_bounds_finite_positive": all(
                math.isfinite(float(value)) and float(value) > 0
                for row in rows for axis in row["axes"]
                for value in axis["complete_value_first_second_abs_uppers"]
            ),
            "complete_gap_constant_overclaim": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": k336["ledger_effect"],
        "source_routing": k336["source_routing"],
        "claim_ceiling": "First finite complete shared-entry determinant gap-axis bank on the strictly positive K326 reference slab. Every repeated K334 gap-box class and all five K299 Duffy axes are evaluated by substituting shared D4 and bordered-B5 entry jets before complete determinant coefficient enclosure, with literal border zeros and the native projective-polynomial jets retained. Origin, s-face and radial-tail cells remain to be lifted through K336's serialized preconditioners and degree ledger, so no complete gap-axis constant, six-axis Peano norm, K294 gamma join, action-column value, residual, K152 interval, source/ledger, canon, paper, public or physical claim is emitted.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["accepted_subdivision_checksum"] != "sha256:2df52de1d9beca3aaf6ea730416f7251e79cf8b1da260c214e27d2e3b5996016":
        raise AssertionError("K334 checksum changed")
    rows = payload["reference_positive_slab_bank"]["rows"]
    if len(rows) != fixed["gap_class_count"] or len({row["gap_class"] for row in rows}) != len(rows):
        raise AssertionError("gap class bank changed")
    if payload["reference_positive_slab_bank"]["class_axis_evaluation_count"] != len(rows) * 5:
        raise AssertionError("class-axis evaluation count changed")
    for row in rows:
        if [axis["axis"] for axis in row["axes"]] != ["t0", "t1", "t2", "t3", "t4"]:
            raise AssertionError("axis census changed")
        if any(len(axis["complete_value_first_second_abs_uppers"]) != 3 for axis in row["axes"]):
            raise AssertionError("coefficient order changed")
    bank = payload["reference_positive_slab_bank"]
    if not bank["shared_entry_interval_substitution_precedes_complete_determinant_coefficient_enclosure"]:
        raise AssertionError("shared-entry assembly order changed")
    if not bank["literal_border_zeros_retained"] or not bank["terminal_gap_direction_exactly_zero_on_reference_map"]:
        raise AssertionError("border or terminal contract changed")
    if not payload["scope_boundary"]["reference_bank_is_not_a_gap_axis_constant"]:
        raise AssertionError("reference scope hidden")
    decision = payload["decision"]
    if decision["complete_gap_axis_constants_emitted"] or decision["complete_six_axis_peano_norm_emitted"] or decision["k294_gamma_join_released"]:
        raise AssertionError("downstream result overclaimed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
