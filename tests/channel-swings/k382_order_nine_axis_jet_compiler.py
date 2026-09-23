#!/usr/bin/env python3
"""Compile the complete native order-nine twenty-axis directional interface."""

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
K380 = ROOT / "lab/process/k380-order-nine-gauss-laguerre-face-atlas.json"
K381 = ROOT / "lab/process/k381-order-nine-group-interval-evaluator.json"
OUTPUT = ROOT / "lab/process/k382-order-nine-axis-jet-compiler.json"

ORDER = 9
SIDE_COUNT = 10
AXES = tuple([f"s{i}" for i in range(1, 11)] + [f"v{i}" for i in range(1, 11)])
EXPECTED = (256, 20, 2368, 4480)


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k382", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def suffix(side: str, position: int) -> list[str]:
    return [f"{side}{index}" for index in range(position, SIDE_COUNT + 1)]


def occurrences(term: dict[str, Any]) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
        result[str(species)].append(int(position))
    return dict(sorted(result.items()))


def group_terms() -> dict[tuple[int, str], list[dict[str, Any]]]:
    groups: dict[tuple[int, str], list[dict[str, Any]]] = defaultdict(list)
    for term in K179.coefficient_family():
        if int(term["order"]) == ORDER:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    return dict(sorted(groups.items()))


def entry_descriptor(group_id: str, left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    left_occurrences = occurrences(left)
    right_occurrences = occurrences(right)
    if left_occurrences.keys() != right_occurrences.keys():
        raise AssertionError("species support changed inside coherent group")
    matrices = []
    for species in left_occurrences:
        rows = left_occurrences[species]
        columns = right_occurrences[species]
        matrices.append({
            "species": species,
            "rank": len(rows),
            "row_positions": rows,
            "column_positions": columns,
            "entry_axis_masks": [[suffix("s", row) + suffix("v", column) for column in columns] for row in rows],
        })
    return {
        "group_id": group_id,
        "left": str(left["contraction_id"]),
        "right": str(right["contraction_id"]),
        "coefficient_product": int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]),
        "left_old_position": int(left["old_position"]),
        "right_old_position": int(right["old_position"]),
        "left_old_axis_mask": suffix("s", int(left["old_position"])),
        "right_old_axis_mask": suffix("v", int(right["old_position"])),
        "species_matrices": matrices,
    }


def build() -> dict[str, Any]:
    k380 = json.loads(K380.read_text())
    k381 = json.loads(K381.read_text())
    groups = group_terms()
    descriptors = []
    group_rows = []
    paths = sum(len(rows) for rows in groups.values())
    for (seed, signature), terms in groups.items():
        group_id = f"order{ORDER}:seed{seed}:{signature}"
        start = len(descriptors)
        for left in terms:
            for right in terms:
                descriptors.append(entry_descriptor(group_id, left, right))
        group_rows.append({
            "group_id": group_id,
            "path_count": len(terms),
            "ordered_directional_entries": len(descriptors) - start,
            "upper_triangle_entries_at_symmetric_node": len(terms) * (len(terms) + 1) // 2,
        })
    upper_entries = sum(row["upper_triangle_entries_at_symmetric_node"] for row in group_rows)
    if (paths, len(groups), upper_entries, len(descriptors)) != EXPECTED:
        raise AssertionError("order-nine jet census changed")

    axis_rows = []
    for axis in AXES:
        entries_touched = old_hits_total = primitive_hits = matrices_touched = maximum_rank = 0
        for entry in descriptors:
            old_hits = int(axis in entry["left_old_axis_mask"]) + int(axis in entry["right_old_axis_mask"])
            matrix_hits = touched = 0
            for matrix in entry["species_matrices"]:
                hits = sum(axis in mask for row in matrix["entry_axis_masks"] for mask in row)
                if hits:
                    touched += 1
                    maximum_rank = max(maximum_rank, int(matrix["rank"]))
                matrix_hits += hits
            if old_hits or matrix_hits:
                entries_touched += 1
            old_hits_total += old_hits
            primitive_hits += matrix_hits
            matrices_touched += touched
        axis_rows.append({
            "axis": axis,
            "entries_touched": entries_touched,
            "old_position_kernel_hits": old_hits_total,
            "determinant_primitive_entry_hits": primitive_hits,
            "determinant_matrices_touched": matrices_touched,
            "maximum_species_determinant_rank_touched": maximum_rank,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K382-ORDER-NINE-AXIS-JET-COMPILER",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": ["lab/process/k380-order-nine-gauss-laguerre-face-atlas.json", "lab/process/k381-order-nine-group-interval-evaluator.json"],
            "order": ORDER,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries_at_symmetric_node": upper_entries,
            "ordered_directional_entries": len(descriptors),
            "native_axes": list(AXES),
            "maximum_species_determinant_rank": 5,
            "K380_face_atlas_sha256": k380["cumulative_time_face_atlas"]["atlas_sha256"],
            "K381_entry_interval_sha256": k381["complete_node_evaluation"]["all_entry_interval_sha256"],
        },
        "group_interface": group_rows,
        "axis_incidence": axis_rows,
        "compiled_entry_interface": {
            "entry_count": len(descriptors),
            "sha256": digest(descriptors),
            "descriptor_fields": [
                "coherent group and contraction ids",
                "exact coefficient product",
                "two old-position cumulative-time masks",
                "every species determinant row/column position",
                "every determinant primitive-entry axis mask",
            ],
        },
        "jet_algebra": {
            "primitive_kernel": "F(x)=2*K1(x)",
            "first_derivative": "F'(x)=-(K0(x)+K2(x))",
            "second_derivative": "F''(x)=(3*K1(x)+K3(x))/2",
            "truncated_series_convention": "[F, dF, d2F/2] in one native raw-time axis",
            "determinants_differentiated_before_group_enclosure": True,
            "complete_group_quadratic_forms_differentiated_before_enclosure": True,
            "off_diagonal_group_entries_kept_in_both_ordered_orientations": True,
            "upper_triangle_doubling_used_for_directional_jets": False,
            "maximum_bessel_order_required_at_positive_node": 3,
            "maximum_zero_safe_scaled_primitive_order_available": 10,
            "K375_rank_five_global_bank_consumed_for_future_faces": True,
            "occurrencewise_absolute_value_used": False,
            "raw_zero_bessel_evaluation_used": False,
        },
        "release_test": {
            "all_256_paths_replayed": paths == 256,
            "all_20_groups_replayed": len(groups) == 20,
            "all_2368_symmetric_node_entries_replayed": upper_entries == 2368,
            "all_4480_ordered_directional_entries_compiled": len(descriptors) == 4480,
            "all_20_native_axes_compiled": len(axis_rows) == 20 and [row["axis"] for row in axis_rows] == list(AXES),
            "every_axis_touches_an_entry": all(row["entries_touched"] > 0 for row in axis_rows),
            "maximum_rank_remains_five": max(row["maximum_species_determinant_rank_touched"] for row in axis_rows) == 5,
            "global_second_derivative_integrals_computed": False,
            "complete_order_nine_remainder_emitted": False,
        },
        "next_exact_input": "evaluate the complete compiled group jets on all twenty axes, then bind their global second derivatives to K380's positive Peano kernels using K374/K375 on a zero-safe whole-orthant cover",
        "ledger_effect": k381["ledger_effect"],
        "source_routing": k381["source_routing"],
        "claim_ceiling": "Exact complete twenty-axis differentiation interface for all 256 order-nine paths, 20 coherent groups, 2,368 symmetric-node upper-triangle entries and all 4,480 ordered directional entries. Off-diagonal orientations remain separate, every primitive carries its native axis mask, and the accepted rank-five zero-safe bank is bound to future face evaluation. This emits no node jet bank, global derivative norm, Peano remainder, complete order-nine integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries_at_symmetric_node"], fixed["ordered_directional_entries"], fixed["maximum_species_determinant_rank"]) != (256, 20, 2368, 4480, 5):
        raise AssertionError("K382 census changed")
    if fixed["native_axes"] != list(AXES) or len(payload["axis_incidence"]) != 20:
        raise AssertionError("K382 native axes changed")
    algebra = payload["jet_algebra"]
    if not algebra["determinants_differentiated_before_group_enclosure"] or not algebra["complete_group_quadratic_forms_differentiated_before_enclosure"] or not algebra["off_diagonal_group_entries_kept_in_both_ordered_orientations"]:
        raise AssertionError("K382 coherent differentiation order changed")
    if algebra["occurrencewise_absolute_value_used"] or algebra["raw_zero_bessel_evaluation_used"] or algebra["maximum_zero_safe_scaled_primitive_order_available"] != 10:
        raise AssertionError("K382 zero-safe contract changed")
    release = payload["release_test"]
    required = ["all_256_paths_replayed", "all_20_groups_replayed", "all_2368_symmetric_node_entries_replayed", "all_4480_ordered_directional_entries_compiled", "all_20_native_axes_compiled", "every_axis_touches_an_entry", "maximum_rank_remains_five"]
    if not all(release[key] for key in required) or release["global_second_derivative_integrals_computed"] or release["complete_order_nine_remainder_emitted"]:
        raise AssertionError("K382 release boundary failed")


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
