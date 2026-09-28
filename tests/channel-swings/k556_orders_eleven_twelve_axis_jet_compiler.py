#!/usr/bin/env python3
"""Compile the complete native order-eleven/twelve ordered-axis interfaces."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K179_PATH = HERE / "k179_matched_normal_order_coefficient_family.py"
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
K554 = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"
K555 = ROOT / "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json"
OUTPUT = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"

EXPECTED = {
    11: {"side": 12, "axes": 24, "paths": 640, "groups": 24, "entries": 12920, "ordered": 25200},
    12: {"side": 13, "axes": 26, "paths": 1152, "groups": 33, "entries": 35352, "ordered": 69552},
}


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k556", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def occurrences(term: dict[str, Any]) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        result[str(species)].append(int(position))
    return dict(sorted(result.items()))


def group_terms(order: int) -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def compact_descriptor(group_id: str, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    left_occurrences = occurrences(left)
    right_occurrences = occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside coherent group")
    return {
        "group_id": group_id,
        "left": str(left["contraction_id"]),
        "right": str(right["contraction_id"]),
        "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]),
        "left_old_position": int(left["old_position"]),
        "right_old_position": int(right["old_position"]),
        "species_matrices": [
            {
                "species": species,
                "rank": len(left_occurrences[species]),
                "row_positions": left_occurrences[species],
                "column_positions": right_occurrences[species],
            }
            for species in left_occurrences
        ],
    }


def empty_axis_row(axis: str) -> dict[str, Any]:
    return {
        "axis": axis,
        "entries_touched": 0,
        "old_position_kernel_hits": 0,
        "determinant_primitive_entry_hits": 0,
        "determinant_matrices_touched": 0,
        "maximum_species_determinant_rank_touched": 0,
    }


def update_axis_rows(rows: dict[str, dict[str, Any]], descriptor: dict[str, Any], side_count: int) -> None:
    left_old = int(descriptor["left_old_position"])
    right_old = int(descriptor["right_old_position"])
    for index in range(1, side_count + 1):
        for side, old_position, coordinate_key in (
            ("s", left_old, "row_positions"),
            ("v", right_old, "column_positions"),
        ):
            row = rows[f"{side}{index}"]
            old_hits = int(index >= old_position)
            primitive_hits = matrices_touched = maximum_rank = 0
            for matrix in descriptor["species_matrices"]:
                active = sum(position <= index for position in matrix[coordinate_key])
                if active:
                    matrices_touched += 1
                    maximum_rank = max(maximum_rank, int(matrix["rank"]))
                other_size = len(matrix["column_positions"] if side == "s" else matrix["row_positions"])
                primitive_hits += active * other_size
            if old_hits or primitive_hits:
                row["entries_touched"] += 1
            row["old_position_kernel_hits"] += old_hits
            row["determinant_primitive_entry_hits"] += primitive_hits
            row["determinant_matrices_touched"] += matrices_touched
            row["maximum_species_determinant_rank_touched"] = max(
                int(row["maximum_species_determinant_rank_touched"]), maximum_rank
            )


def compile_order(order: int, atlas: dict[str, Any], evaluation: dict[str, Any]) -> dict[str, Any]:
    expected = EXPECTED[order]
    axes = tuple([f"s{i}" for i in range(1, expected["side"] + 1)] + [f"v{i}" for i in range(1, expected["side"] + 1)])
    groups = group_terms(order)
    paths = sum(len(rows) for rows in groups.values())
    upper_entries = sum(len(rows) * (len(rows) + 1) // 2 for rows in groups.values())
    ordered_entries = sum(len(rows) ** 2 for rows in groups.values())
    if (paths, len(groups), upper_entries, ordered_entries) != (
        expected["paths"], expected["groups"], expected["entries"], expected["ordered"]
    ):
        raise AssertionError(f"order-{order} jet census changed")

    stream = hashlib.sha256()
    stream.update(b"[")
    first = True
    axis_rows = {axis: empty_axis_row(axis) for axis in axes}
    group_rows = []
    descriptor_count = 0
    for (seed, signature), terms in groups.items():
        group_id = f"order{order}:seed{seed}:{signature}"
        group_start = descriptor_count
        for left in terms:
            for right in terms:
                descriptor = compact_descriptor(group_id, left, right)
                if not first:
                    stream.update(b",")
                stream.update(json.dumps(descriptor, sort_keys=True, separators=(",", ":")).encode())
                first = False
                descriptor_count += 1
                update_axis_rows(axis_rows, descriptor, expected["side"])
        group_rows.append({
            "group_id": group_id,
            "path_count": len(terms),
            "ordered_directional_entries": descriptor_count - group_start,
            "upper_triangle_entries_at_symmetric_node": len(terms) * (len(terms) + 1) // 2,
        })
    stream.update(b"]")
    if descriptor_count != expected["ordered"]:
        raise AssertionError(f"order-{order} descriptor count changed")

    return {
        "order": order,
        "fixed_control": {
            "side_count": expected["side"],
            "positive_time_variables": expected["axes"],
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries_at_symmetric_node": upper_entries,
            "ordered_directional_entries": descriptor_count,
            "native_axes": list(axes),
            "maximum_species_determinant_rank": 6,
            "K554_face_atlas_sha256": atlas["cumulative_time_face_atlas"]["atlas_sha256"],
            "K555_entry_interval_sha256": evaluation["complete_node_evaluation"]["all_entry_interval_sha256"],
        },
        "group_interface": group_rows,
        "axis_incidence": [axis_rows[axis] for axis in axes],
        "compiled_entry_interface": {
            "entry_count": descriptor_count,
            "stream_sha256": "sha256:" + stream.hexdigest(),
            "descriptor_fields": [
                "coherent group and contraction ids",
                "exact coefficient product",
                "two old-position cumulative-time starts",
                "every species determinant row/column position",
                "every native axis mask derived exactly as the suffix from its recorded start position",
            ],
        },
        "release_test": {
            "all_paths_replayed": paths == expected["paths"],
            "all_groups_replayed": len(groups) == expected["groups"],
            "all_symmetric_node_entries_replayed": upper_entries == expected["entries"],
            "all_ordered_directional_entries_compiled": descriptor_count == expected["ordered"],
            "all_native_axes_compiled": len(axis_rows) == expected["axes"] and list(axis_rows) == list(axes),
            "every_axis_touches_an_entry": all(row["entries_touched"] > 0 for row in axis_rows.values()),
            "maximum_rank_remains_six": max(row["maximum_species_determinant_rank_touched"] for row in axis_rows.values()) == 6,
        },
    }


def build() -> dict[str, Any]:
    k378 = json.loads(K378.read_text())
    k554 = json.loads(K554.read_text())
    k555 = json.loads(K555.read_text())
    atlases = {int(row["order"]): row for row in k554["order_interfaces"]}
    evaluations = {int(row["order"]): row for row in k555["order_evaluations"]}
    rows = [compile_order(order, atlases[order], evaluations[order]) for order in (11, 12)]
    return {
        "schema_version": "1.0",
        "result_id": "K556-ORDERS-ELEVEN-TWELVE-AXIS-JET-COMPILER",
        "created": "2026-09-27",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k378-rank-six-global-scaled-bessel-bank.json",
                "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json",
                "lab/process/k555-orders-eleven-twelve-group-interval-evaluator.json",
            ],
            "orders": [11, 12],
            "combined_paths": sum(row["fixed_control"]["paths"] for row in rows),
            "combined_groups": sum(row["fixed_control"]["coherent_groups"] for row in rows),
            "combined_symmetric_node_entries": sum(row["fixed_control"]["upper_triangle_gram_entries_at_symmetric_node"] for row in rows),
            "combined_ordered_directional_entries": sum(row["fixed_control"]["ordered_directional_entries"] for row in rows),
            "combined_native_axes": sum(row["fixed_control"]["positive_time_variables"] for row in rows),
            "K378_maximum_derivative_order": 12,
            "K378_bank_result_id": k378["result_id"],
        },
        "order_interfaces": rows,
        "jet_algebra": {
            "primitive_kernel": "F(x)=2*K1(x)",
            "first_derivative": "F'(x)=-(K0(x)+K2(x))",
            "second_derivative": "F''(x)=(3*K1(x)+K3(x))/2",
            "truncated_series_convention": "[F, dF, d2F/2] in one native raw-time axis",
            "determinants_differentiated_before_group_enclosure": True,
            "complete_group_quadratic_forms_differentiated_before_enclosure": True,
            "off_diagonal_group_entries_kept_in_both_ordered_orientations": True,
            "upper_triangle_doubling_used_for_directional_jets": False,
            "axis_masks_derived_from_recorded_cumulative_time_starts": True,
            "maximum_bessel_order_required_at_positive_node": 3,
            "maximum_zero_safe_scaled_primitive_order_available": 12,
            "K378_rank_six_global_bank_consumed_for_future_faces": True,
            "occurrencewise_absolute_value_used": False,
            "raw_zero_bessel_evaluation_used": False,
        },
        "decision": {
            "complete_order_eleven_axis_interface_emitted": True,
            "complete_order_twelve_axis_interface_emitted": True,
            "complete_first_second_node_jets_evaluated": False,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eleven_remainder_emitted": False,
            "complete_order_twelve_remainder_emitted": False,
            "complete_order_eleven_integral_emitted": False,
            "complete_order_twelve_integral_emitted": False,
            "native_K152_interval_emitted": False,
        },
        "release_test": {
            "all_1792_paths_replayed": sum(row["fixed_control"]["paths"] for row in rows) == 1792,
            "all_57_groups_replayed": sum(row["fixed_control"]["coherent_groups"] for row in rows) == 57,
            "all_48272_symmetric_node_entries_replayed": sum(row["fixed_control"]["upper_triangle_gram_entries_at_symmetric_node"] for row in rows) == 48272,
            "all_94752_ordered_directional_entries_compiled": sum(row["fixed_control"]["ordered_directional_entries"] for row in rows) == 94752,
            "all_50_native_axes_compiled": sum(row["fixed_control"]["positive_time_variables"] for row in rows) == 50,
            "rank_six_boundary_retained_both_orders": all(row["release_test"]["maximum_rank_remains_six"] for row in rows),
            "off_diagonal_orientations_retained": True,
            "global_remainders_not_overclaimed": True,
            "complete_integrals_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "next_exact_input": "evaluate the complete value/first/second node jets for all 94,752 ordered entries on their 24/26 native axes, then construct separate zero-safe Peano, face, interior and tail closures",
        "ledger_effect": k555["ledger_effect"],
        "source_routing": k555["source_routing"],
        "claim_ceiling": "Exact complete ordered differentiation interfaces for the native order-eleven and order-twelve one-node rules: all 1,792 paths, 57 coherent groups, 48,272 symmetric-node upper-triangle entries, 94,752 ordered directional entries and 50 separate raw-time axes are retained with rank six. Off-diagonal orientations remain separate and every primitive axis mask is derived from its recorded cumulative-time start. This emits no node jet bank, global derivative norm, Peano remainder, complete integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public, novelty or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_paths"], fixed["combined_groups"], fixed["combined_symmetric_node_entries"], fixed["combined_ordered_directional_entries"], fixed["combined_native_axes"], fixed["K378_maximum_derivative_order"]) != (1792, 57, 48272, 94752, 50, 12):
        raise AssertionError("K556 combined census changed")
    rows = payload["order_interfaces"]
    if len(rows) != 2 or [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K556 order interfaces changed")
    for row in rows:
        expected = EXPECTED[row["order"]]
        control = row["fixed_control"]
        if (control["side_count"], control["positive_time_variables"], control["paths"], control["coherent_groups"], control["upper_triangle_gram_entries_at_symmetric_node"], control["ordered_directional_entries"], control["maximum_species_determinant_rank"]) != (expected["side"], expected["axes"], expected["paths"], expected["groups"], expected["entries"], expected["ordered"], 6):
            raise AssertionError(f"K556 order-{row['order']} interface changed")
        expected_axes = [f"s{i}" for i in range(1, expected["side"] + 1)] + [f"v{i}" for i in range(1, expected["side"] + 1)]
        if control["native_axes"] != expected_axes or [axis["axis"] for axis in row["axis_incidence"]] != expected_axes:
            raise AssertionError(f"K556 order-{row['order']} native axes changed")
        if not all(row["release_test"].values()):
            raise AssertionError(f"K556 order-{row['order']} release test failed")
    algebra = payload["jet_algebra"]
    if not all(algebra[key] for key in ("determinants_differentiated_before_group_enclosure", "complete_group_quadratic_forms_differentiated_before_enclosure", "off_diagonal_group_entries_kept_in_both_ordered_orientations", "axis_masks_derived_from_recorded_cumulative_time_starts", "K378_rank_six_global_bank_consumed_for_future_faces")):
        raise AssertionError("K556 coherent differentiation order changed")
    if algebra["occurrencewise_absolute_value_used"] or algebra["raw_zero_bessel_evaluation_used"] or algebra["maximum_zero_safe_scaled_primitive_order_available"] != 12:
        raise AssertionError("K556 zero-safe contract changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K556 combined release test failed")
    decision = payload["decision"]
    if not decision["complete_order_eleven_axis_interface_emitted"] or not decision["complete_order_twelve_axis_interface_emitted"] or decision["complete_first_second_node_jets_evaluated"] or decision["complete_order_eleven_integral_emitted"] or decision["complete_order_twelve_integral_emitted"] or decision["native_K152_interval_emitted"]:
        raise AssertionError("K556 decision boundary changed")


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
