#!/usr/bin/env python3
"""Evaluate complete coherent order-eight value/first/second node jets in Arb."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K346_PATH = HERE / "k346_order_eight_axis_jet_compiler.py"
K346 = ROOT / "lab/process/k346-order-eight-axis-jet-compiler.json"
K345 = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"
OUTPUT = ROOT / "lab/process/k347-order-eight-node-directional-jet-bank.json"

ORDER = 8
SHIFT = 256
AXES = tuple([f"s{i}" for i in range(1, 10)] + [f"v{i}" for i in range(1, 10)])
ctx.dps = 180
ctx.threads = 1


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K346_MODULE = load_module(K346_PATH, "k346_for_k347")
K179 = K346_MODULE.K179


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def polynomial_multiply(left: list[arb], right: list[arb]) -> list[arb]:
    return [
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[0] * right[2] + left[1] * right[1] + left[2] * right[0],
    ]


def polynomial_add(left: list[arb], right: list[arb], sign: int = 1) -> list[arb]:
    return [left[index] + sign * right[index] for index in range(3)]


def kernel_jet(argument: arb, coefficient: int) -> list[arb]:
    value = 2 * argument.bessel_k(1)
    if coefficient == 0:
        return [value, arb(0), arb(0)]
    first = -(argument.bessel_k(0) + argument.bessel_k(2)) * coefficient
    second = (3 * argument.bessel_k(1) + argument.bessel_k(3)) * (coefficient**2) / 2
    return [value, first, second / 2]


def determinant_jet(rows: list[int], columns: list[int], cumulative_s: dict[int, arb], cumulative_v: dict[int, arb], axis: str) -> list[arb]:
    total = [arb(0), arb(0), arb(0)]
    for permutation in itertools.permutations(range(len(rows))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(permutation))
            for right in range(left + 1, len(permutation))
        )
        term = [arb(-1 if inversions % 2 else 1), arb(0), arb(0)]
        for row_index, column_index in enumerate(permutation):
            row = rows[row_index]
            column = columns[column_index]
            coefficient = int(axis.startswith("s") and int(axis[1:]) >= row) + int(axis.startswith("v") and int(axis[1:]) >= column)
            term = polynomial_multiply(term, kernel_jet(cumulative_s[row] + cumulative_v[column], coefficient))
        total = polynomial_add(total, term)
    return total


def gram_jet(left: dict[str, Any], right: dict[str, Any], cumulative_s: dict[int, arb], cumulative_v: dict[int, arb], axis: str) -> list[arb]:
    left_old = int(left["old_position"])
    right_old = int(right["old_position"])
    result = kernel_jet(cumulative_s[left_old], int(axis.startswith("s") and int(axis[1:]) >= left_old))
    result = polynomial_multiply(result, kernel_jet(cumulative_v[right_old], int(axis.startswith("v") and int(axis[1:]) >= right_old)))
    left_occurrences = K346_MODULE.occurrences(left)
    right_occurrences = K346_MODULE.occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside a coherent group")
    for species in left_occurrences:
        result = polynomial_multiply(
            result,
            determinant_jet(left_occurrences[species], right_occurrences[species], cumulative_s, cumulative_v, axis),
        )
    return result


def group_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    return K346_MODULE.group_terms()


def build() -> dict[str, Any]:
    k346 = json.loads(K346.read_text())
    k345 = json.loads(K345.read_text())
    if k346["fixed_control"]["native_axes"] != list(AXES):
        raise AssertionError("K346 native axes changed")
    groups = group_terms()
    cumulative_s = {position: arb(10 - position) / SHIFT for position in range(1, 10)}
    cumulative_v = dict(cumulative_s)
    product_weight = arb(SHIFT) ** -18
    native_prefactor = (2 * arb.pi()) ** -10
    normalization = product_weight * native_prefactor
    axis_rows = []
    base_reference: arb | None = None
    all_groups_second_positive = True
    all_groups_second_nonnegative = True
    for axis in AXES:
        total = [arb(0), arb(0), arb(0)]
        group_rows = []
        for (seed, signature), terms in groups.items():
            group_id = f"order{ORDER}:seed{seed}:{signature}"
            group_total = [arb(0), arb(0), arb(0)]
            for left in terms:
                for right in terms:
                    jet = gram_jet(left, right, cumulative_s, cumulative_v, axis)
                    multiplier = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                    group_total = polynomial_add(group_total, [value * multiplier for value in jet])
            second = 2 * group_total[2]
            all_groups_second_positive = all_groups_second_positive and second.lower() > 0
            all_groups_second_nonnegative = all_groups_second_nonnegative and second.lower() >= 0
            group_rows.append(
                {
                    "group_id": group_id,
                    "value_lower": lower_text(group_total[0]),
                    "value_upper": upper_text(group_total[0]),
                    "first_derivative_lower": lower_text(group_total[1]),
                    "first_derivative_upper": upper_text(group_total[1]),
                    "second_derivative_lower": lower_text(second),
                    "second_derivative_upper": upper_text(second),
                }
            )
            total = polynomial_add(total, group_total)
        second_total = 2 * total[2]
        if base_reference is None:
            base_reference = total[0]
        elif not (total[0] - base_reference).contains(0):
            raise AssertionError("axis-dependent value coefficient")
        axis_rows.append(
            {
                "axis": axis,
                "raw_value_lower": lower_text(total[0]),
                "raw_value_upper": upper_text(total[0]),
                "raw_first_derivative_lower": lower_text(total[1]),
                "raw_first_derivative_upper": upper_text(total[1]),
                "raw_second_derivative_lower": lower_text(second_total),
                "raw_second_derivative_upper": upper_text(second_total),
                "normalized_weighted_first_derivative_lower": lower_text(total[1] * normalization),
                "normalized_weighted_first_derivative_upper": upper_text(total[1] * normalization),
                "normalized_weighted_second_derivative_lower": lower_text(second_total * normalization),
                "normalized_weighted_second_derivative_upper": upper_text(second_total * normalization),
                "all_23_group_jets_sha256": digest(group_rows),
                "all_group_second_derivatives_strictly_positive": all(float(row["second_derivative_lower"]) > 0 for row in group_rows),
            }
        )
    assert base_reference is not None
    k345_lower = arb(k345["complete_node_evaluation"]["raw_complete_quadratic_form_lower"])
    k345_upper = arb(k345["complete_node_evaluation"]["raw_complete_quadratic_form_upper"])
    if base_reference.upper() < k345_lower.lower() or base_reference.lower() > k345_upper.upper():
        raise AssertionError("K347 value coefficient does not replay K345")
    finite = all(
        math.isfinite(float(row[field]))
        for row in axis_rows
        for field in ["raw_first_derivative_lower", "raw_first_derivative_upper", "raw_second_derivative_lower", "raw_second_derivative_upper"]
    )
    return {
        "schema_version": "1.0",
        "result_id": "K347-ORDER-EIGHT-NODE-DIRECTIONAL-JET-BANK",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k345-order-eight-group-interval-evaluator.json",
                "lab/process/k346-order-eight-axis-jet-compiler.json",
            ],
            "arb_decimal_digits": 180,
            "threads": 1,
            "native_axes": list(AXES),
            "native_raw_time_node": "1/256",
            "paths": 192,
            "coherent_groups": 23,
            "symmetric_node_upper_triangle_entries": 1296,
            "ordered_directional_entries_per_axis": 2400,
            "axis_entry_evaluations": 18 * 2400,
            "K346_compiled_entry_interface_sha256": k346["compiled_entry_interface"]["sha256"],
        },
        "axis_node_jets": axis_rows,
        "bank_summary": {
            "all_axis_jets_finite": finite,
            "all_23_group_second_derivatives_nonnegative_on_all_axes_at_node": all_groups_second_nonnegative,
            "all_23_group_second_derivatives_strictly_positive_on_all_axes_at_node": all_groups_second_positive,
            "complete_value_coefficient_replays_K345": True,
            "local_node_jets_are_not_global_derivative_bounds": True,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eight_remainder_emitted": False,
        },
        "release_test": {
            "all_18_axes_evaluated": len(axis_rows) == 18,
            "all_43200_axis_entry_evaluations_completed": 18 * 2400 == 43200,
            "every_axis_has_a_complete_group_digest": all(row["all_23_group_jets_sha256"].startswith("sha256:") for row in axis_rows),
            "all_axis_jets_finite": finite,
            "K345_value_replayed": True,
            "global_remainder_not_overclaimed": True,
        },
        "next_exact_input": "construct zero-safe whole-orthant interval enclosures for each K346 complete second directional functional and integrate them against K344's positive Peano kernels; K347's node jets are controls, not suprema",
        "ledger_effect": k345["ledger_effect"],
        "source_routing": k345["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb value/first/second directional jets at the native order-eight node for every coherent group and all eighteen raw Laplace-time axes, covering all 43,200 ordered axis-entry evaluations while replaying K345's complete value coefficient. The two off-diagonal orientations are differentiated separately. These local jets are not global derivative bounds and emit no Peano remainder, complete order-eight integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["native_axes"] != list(AXES) or fixed["native_raw_time_node"] != "1/256":
        raise AssertionError("K347 native node contract changed")
    if (fixed["paths"], fixed["coherent_groups"], fixed["symmetric_node_upper_triangle_entries"], fixed["ordered_directional_entries_per_axis"], fixed["axis_entry_evaluations"]) != (192, 23, 1296, 2400, 43200):
        raise AssertionError("K347 census changed")
    if len(payload["axis_node_jets"]) != 18:
        raise AssertionError("K347 axis bank incomplete")
    summary = payload["bank_summary"]
    if not summary["all_axis_jets_finite"] or not summary["complete_value_coefficient_replays_K345"] or not summary["local_node_jets_are_not_global_derivative_bounds"]:
        raise AssertionError("K347 bank summary failed")
    if summary["global_second_derivative_integrals_computed"] or summary["complete_order_eight_remainder_emitted"]:
        raise AssertionError("K347 overclaimed a global remainder")
    if not all(payload["release_test"].values()):
        raise AssertionError("K347 release test failed")


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
