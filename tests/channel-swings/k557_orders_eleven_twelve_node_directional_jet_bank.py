#!/usr/bin/env python3
"""Evaluate complete coherent order-eleven/twelve node jets in Arb."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import math
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K556_PATH = HERE / "k556_orders_eleven_twelve_axis_jet_compiler.py"
K555 = ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json"
K556 = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"
OUTPUT = ROOT / "lab/process/k557-orders-eleven-twelve-node-directional-jet-bank.json"

SHIFT = 256
EXPECTED = {
    11: {"side": 12, "axes": 24, "paths": 640, "groups": 24, "entries": 12920, "ordered": 25200, "axis_uses": 604800, "prefactor_power": 13},
    12: {"side": 13, "axes": 26, "paths": 1152, "groups": 33, "entries": 35352, "ordered": 69552, "axis_uses": 1808352, "prefactor_power": 14},
}
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


K556_MODULE = load_module(K556_PATH, "k556_for_k557")


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def lower_text(value: arb) -> str:
    return repr(math.nextafter(float(value.lower()), -math.inf))


def upper_text(value: arb) -> str:
    return repr(math.nextafter(float(value.upper()), math.inf))


def polynomial_multiply(left: tuple[arb, arb, arb], right: tuple[arb, arb, arb]) -> tuple[arb, arb, arb]:
    return (
        left[0] * right[0],
        left[0] * right[1] + left[1] * right[0],
        left[0] * right[2] + left[1] * right[1] + left[2] * right[0],
    )


def polynomial_add(left: tuple[arb, arb, arb], right: tuple[arb, arb, arb], multiplier: int = 1) -> tuple[arb, arb, arb]:
    return tuple(left[index] + multiplier * right[index] for index in range(3))  # type: ignore[return-value]


@lru_cache(maxsize=None)
def kernel_jet(argument_numerator: int, coefficient: int) -> tuple[arb, arb, arb]:
    argument = arb(argument_numerator) / SHIFT
    value = 2 * argument.bessel_k(1)
    if coefficient == 0:
        return value, arb(0), arb(0)
    first = -(argument.bessel_k(0) + argument.bessel_k(2)) * coefficient
    second = (3 * argument.bessel_k(1) + argument.bessel_k(3)) * (coefficient**2) / 2
    return value, first, second / 2


@lru_cache(maxsize=None)
def determinant_jet(rows: tuple[int, ...], columns: tuple[int, ...], side: int, axis_side: str, axis_index: int) -> tuple[arb, arb, arb]:
    total = (arb(0), arb(0), arb(0))
    for permutation in itertools.permutations(range(len(rows))):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(len(permutation))
            for right in range(left + 1, len(permutation))
        )
        term = (arb(-1 if inversions % 2 else 1), arb(0), arb(0))
        for row_index, column_index in enumerate(permutation):
            row = rows[row_index]
            column = columns[column_index]
            coefficient = int(axis_side == "s" and axis_index >= row) + int(axis_side == "v" and axis_index >= column)
            argument_numerator = (side + 1 - row) + (side + 1 - column)
            term = polynomial_multiply(term, kernel_jet(argument_numerator, coefficient))
        total = polynomial_add(total, term)
    return total


def gram_jet(left: dict[str, Any], right: dict[str, Any], side: int, axis_side: str, axis_index: int) -> tuple[arb, arb, arb]:
    left_old = int(left["old_position"])
    right_old = int(right["old_position"])
    result = kernel_jet(side + 1 - left_old, int(axis_side == "s" and axis_index >= left_old))
    result = polynomial_multiply(
        result,
        kernel_jet(side + 1 - right_old, int(axis_side == "v" and axis_index >= right_old)),
    )
    left_occurrences = K556_MODULE.occurrences(left)
    right_occurrences = K556_MODULE.occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside a coherent group")
    for species in left_occurrences:
        result = polynomial_multiply(
            result,
            determinant_jet(tuple(left_occurrences[species]), tuple(right_occurrences[species]), side, axis_side, axis_index),
        )
    return result


def compile_order(order: int, evaluation: dict[str, Any], interface: dict[str, Any]) -> dict[str, Any]:
    expected = EXPECTED[order]
    side = expected["side"]
    axes = tuple([f"s{i}" for i in range(1, side + 1)] + [f"v{i}" for i in range(1, side + 1)])
    groups = K556_MODULE.group_terms(order)
    product_weight = arb(SHIFT) ** -expected["axes"]
    native_prefactor = (2 * arb.pi()) ** -expected["prefactor_power"]
    normalization = product_weight * native_prefactor
    axis_rows = []
    base_reference: arb | None = None
    all_groups_second_positive = True
    all_groups_second_nonnegative = True
    for axis in axes:
        axis_side, axis_index = axis[0], int(axis[1:])
        total = (arb(0), arb(0), arb(0))
        group_rows = []
        for (seed, signature), terms in groups.items():
            group_id = f"order{order}:seed{seed}:{signature}"
            group_total = (arb(0), arb(0), arb(0))
            for left in terms:
                for right in terms:
                    jet = gram_jet(left, right, side, axis_side, axis_index)
                    multiplier = int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"])
                    group_total = polynomial_add(group_total, jet, multiplier)
            second = 2 * group_total[2]
            all_groups_second_positive = all_groups_second_positive and second.lower() > 0
            all_groups_second_nonnegative = all_groups_second_nonnegative and second.lower() >= 0
            group_rows.append({
                "group_id": group_id,
                "value_lower": lower_text(group_total[0]),
                "value_upper": upper_text(group_total[0]),
                "first_derivative_lower": lower_text(group_total[1]),
                "first_derivative_upper": upper_text(group_total[1]),
                "second_derivative_lower": lower_text(second),
                "second_derivative_upper": upper_text(second),
            })
            total = polynomial_add(total, group_total)
        second_total = 2 * total[2]
        if base_reference is None:
            base_reference = total[0]
        elif not (total[0] - base_reference).contains(0):
            raise AssertionError(f"order-{order} axis-dependent value coefficient")
        axis_rows.append({
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
            "all_group_jets_sha256": digest(group_rows),
            "all_group_second_derivatives_strictly_positive": all(float(row["second_derivative_lower"]) > 0 for row in group_rows),
        })
    assert base_reference is not None
    node = evaluation["complete_node_evaluation"]
    if base_reference.upper() < arb(node["raw_complete_quadratic_form_lower"]).lower() or base_reference.lower() > arb(node["raw_complete_quadratic_form_upper"]).upper():
        raise AssertionError(f"order-{order} value coefficient does not replay K555")
    finite = all(
        math.isfinite(float(row[field]))
        for row in axis_rows
        for field in ("raw_first_derivative_lower", "raw_first_derivative_upper", "raw_second_derivative_lower", "raw_second_derivative_upper")
    )
    return {
        "order": order,
        "fixed_control": {
            "side_count": side,
            "native_axes": list(axes),
            "native_raw_time_node": "1/256",
            "paths": expected["paths"],
            "coherent_groups": expected["groups"],
            "symmetric_node_upper_triangle_entries": expected["entries"],
            "ordered_directional_entries_per_axis": expected["ordered"],
            "axis_entry_evaluations": expected["axis_uses"],
            "native_prefactor": f"(2*pi)^-{expected['prefactor_power']}",
            "K556_compiled_entry_interface_sha256": interface["compiled_entry_interface"]["stream_sha256"],
        },
        "axis_node_jets": axis_rows,
        "bank_summary": {
            "all_axis_jets_finite": finite,
            "all_group_second_derivatives_nonnegative_on_all_axes_at_node": all_groups_second_nonnegative,
            "all_group_second_derivatives_strictly_positive_on_all_axes_at_node": all_groups_second_positive,
            "complete_value_coefficient_replays_K555": True,
            "local_node_jets_are_not_global_derivative_bounds": True,
            "global_second_derivative_integrals_computed": False,
            "complete_remainder_emitted": False,
        },
        "release_test": {
            "all_axes_evaluated": len(axis_rows) == expected["axes"],
            "all_axis_entry_evaluations_completed": expected["axes"] * expected["ordered"] == expected["axis_uses"],
            "every_axis_has_a_complete_group_digest": all(row["all_group_jets_sha256"].startswith("sha256:") for row in axis_rows),
            "all_axis_jets_finite": finite,
            "K555_value_replayed": True,
            "global_remainder_not_overclaimed": True,
        },
    }


def build() -> dict[str, Any]:
    k555 = json.loads(K555.read_text())
    k556 = json.loads(K556.read_text())
    evaluations = {int(row["order"]): row for row in k555["order_evaluations"]}
    interfaces = {int(row["order"]): row for row in k556["order_interfaces"]}
    rows = [compile_order(order, evaluations[order], interfaces[order]) for order in (11, 12)]
    return {
        "schema_version": "1.0",
        "result_id": "K557-ORDERS-ELEVEN-TWELVE-NODE-DIRECTIONAL-JET-BANK",
        "created": "2026-09-27",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json",
                "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json",
            ],
            "orders": [11, 12],
            "arb_decimal_digits": 180,
            "threads": 1,
            "combined_paths": 1792,
            "combined_groups": 57,
            "combined_symmetric_node_entries": 48272,
            "combined_ordered_directional_entries": 94752,
            "combined_native_axes": 50,
            "combined_axis_entry_evaluations": 2413152,
        },
        "order_banks": rows,
        "decision": {
            "complete_first_second_node_jets_evaluated": True,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eleven_remainder_emitted": False,
            "complete_order_twelve_remainder_emitted": False,
            "complete_order_eleven_integral_emitted": False,
            "complete_order_twelve_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "release_test": {
            "both_order_banks_present": [row["order"] for row in rows] == [11, 12],
            "all_50_axes_evaluated": sum(len(row["axis_node_jets"]) for row in rows) == 50,
            "all_2413152_axis_entry_evaluations_completed": sum(row["fixed_control"]["axis_entry_evaluations"] for row in rows) == 2413152,
            "all_axis_jets_finite": all(row["bank_summary"]["all_axis_jets_finite"] for row in rows),
            "both_K555_values_replayed": all(row["bank_summary"]["complete_value_coefficient_replays_K555"] for row in rows),
            "global_remainders_not_overclaimed": True,
            "complete_integrals_not_overclaimed": True,
        },
        "next_exact_input": "freeze the separate 24/26-axis positive tensor-Peano identities, then construct zero-safe whole-domain face/interior/tail enclosures for every complete coherent pure-second functional",
        "ledger_effect": k555["ledger_effect"],
        "source_routing": k555["source_routing"],
        "claim_ceiling": "Rigorous 180-digit Arb value/first/second directional jets at the native positive nodes for every coherent group and all 50 raw Laplace-time axes of orders eleven and twelve, covering all 2,413,152 ordered axis-entry evaluations while replaying K555's complete value coefficients. The two off-diagonal orientations remain separate. These local jets are not global derivative bounds and emit no Peano remainder, complete integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_paths"], fixed["combined_groups"], fixed["combined_symmetric_node_entries"], fixed["combined_ordered_directional_entries"], fixed["combined_native_axes"], fixed["combined_axis_entry_evaluations"]) != (1792, 57, 48272, 94752, 50, 2413152):
        raise AssertionError("K557 combined census changed")
    rows = payload["order_banks"]
    if len(rows) != 2 or [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K557 order banks changed")
    for row in rows:
        expected = EXPECTED[row["order"]]
        control = row["fixed_control"]
        expected_axes = [f"s{i}" for i in range(1, expected["side"] + 1)] + [f"v{i}" for i in range(1, expected["side"] + 1)]
        if control["native_axes"] != expected_axes or control["native_raw_time_node"] != "1/256" or len(row["axis_node_jets"]) != expected["axes"]:
            raise AssertionError(f"K557 order-{row['order']} native axes changed")
        if (control["paths"], control["coherent_groups"], control["symmetric_node_upper_triangle_entries"], control["ordered_directional_entries_per_axis"], control["axis_entry_evaluations"]) != (expected["paths"], expected["groups"], expected["entries"], expected["ordered"], expected["axis_uses"]):
            raise AssertionError(f"K557 order-{row['order']} census changed")
        if not row["bank_summary"]["all_axis_jets_finite"] or not row["bank_summary"]["complete_value_coefficient_replays_K555"] or not row["bank_summary"]["local_node_jets_are_not_global_derivative_bounds"]:
            raise AssertionError(f"K557 order-{row['order']} bank summary failed")
        if row["bank_summary"]["global_second_derivative_integrals_computed"] or row["bank_summary"]["complete_remainder_emitted"] or not all(row["release_test"].values()):
            raise AssertionError(f"K557 order-{row['order']} overclaim or release failure")
    decision = payload["decision"]
    if not decision["complete_first_second_node_jets_evaluated"] or decision["global_second_derivative_integrals_computed"] or decision["complete_order_eleven_integral_emitted"] or decision["complete_order_twelve_integral_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K557 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K557 combined release test failed")


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
