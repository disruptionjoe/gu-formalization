#!/usr/bin/env python3
"""Compile the complete native order-eight eighteen-axis jet interface.

The compiler preserves each coherent group and every Gram entry.  It records
the primitive cumulative-time arguments on which the two old-position kernels
and every species-determinant entry depend.  K347 consumes this interface with
a truncated-polynomial evaluator, so differentiation occurs before any
absolute enclosure and determinant cancellation is retained exactly.
"""

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
K344 = ROOT / "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json"
K345 = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"
OUTPUT = ROOT / "lab/process/k346-order-eight-axis-jet-compiler.json"

ORDER = 8
SIDE_COUNT = 9
AXES = tuple([f"s{i}" for i in range(1, 10)] + [f"v{i}" for i in range(1, 10)])
EXPECTED_PATHS = 192
EXPECTED_GROUPS = 23
EXPECTED_UPPER_ENTRIES = 1296
EXPECTED_ORDERED_ENTRIES = 2400


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k346", K179_PATH)
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
        matrices.append(
            {
                "species": species,
                "rank": len(rows),
                "row_positions": rows,
                "column_positions": columns,
                "entry_axis_masks": [
                    [suffix("s", row) + suffix("v", column) for column in columns]
                    for row in rows
                ],
            }
        )
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
    k344 = json.loads(K344.read_text())
    k345 = json.loads(K345.read_text())
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
        group_rows.append(
            {
                "group_id": group_id,
                "path_count": len(terms),
                "ordered_directional_entries": len(descriptors) - start,
                "upper_triangle_entries_at_symmetric_node": len(terms) * (len(terms) + 1) // 2,
            }
        )
    upper_entries = sum(row["upper_triangle_entries_at_symmetric_node"] for row in group_rows)
    if (paths, len(groups), upper_entries, len(descriptors)) != (EXPECTED_PATHS, EXPECTED_GROUPS, EXPECTED_UPPER_ENTRIES, EXPECTED_ORDERED_ENTRIES):
        raise AssertionError("order-eight jet census changed")

    axis_rows = []
    for axis in AXES:
        entries_touched = 0
        old_kernel_hits = 0
        determinant_entry_hits = 0
        determinant_matrices_touched = 0
        maximum_rank_touched = 0
        for entry in descriptors:
            old_hits = int(axis in entry["left_old_axis_mask"]) + int(axis in entry["right_old_axis_mask"])
            matrix_hits = 0
            touched_matrices = 0
            for matrix in entry["species_matrices"]:
                hits = sum(axis in mask for row in matrix["entry_axis_masks"] for mask in row)
                if hits:
                    touched_matrices += 1
                    maximum_rank_touched = max(maximum_rank_touched, int(matrix["rank"]))
                matrix_hits += hits
            if old_hits or matrix_hits:
                entries_touched += 1
            old_kernel_hits += old_hits
            determinant_entry_hits += matrix_hits
            determinant_matrices_touched += touched_matrices
        axis_rows.append(
            {
                "axis": axis,
                "entries_touched": entries_touched,
                "old_position_kernel_hits": old_kernel_hits,
                "determinant_primitive_entry_hits": determinant_entry_hits,
                "determinant_matrices_touched": determinant_matrices_touched,
                "maximum_species_determinant_rank_touched": maximum_rank_touched,
            }
        )

    interface_digest = digest(descriptors)
    return {
        "schema_version": "1.0",
        "result_id": "K346-ORDER-EIGHT-AXIS-JET-COMPILER",
        "created": "2026-09-22",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k344-order-eight-gauss-laguerre-face-atlas.json",
                "lab/process/k345-order-eight-group-interval-evaluator.json",
            ],
            "order": ORDER,
            "paths": paths,
            "coherent_groups": len(groups),
            "upper_triangle_gram_entries_at_symmetric_node": upper_entries,
            "ordered_directional_entries": len(descriptors),
            "native_axes": list(AXES),
            "maximum_species_determinant_rank": 4,
            "K344_face_atlas_sha256": k344["cumulative_time_face_atlas"]["atlas_sha256"],
            "K345_entry_interval_sha256": k345["complete_node_evaluation"]["all_entry_interval_sha256"],
        },
        "group_interface": group_rows,
        "axis_incidence": axis_rows,
        "compiled_entry_interface": {
            "entry_count": len(descriptors),
            "sha256": interface_digest,
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
            "maximum_bessel_order_required": 3,
            "occurrencewise_absolute_value_used": False,
            "raw_zero_bessel_evaluation_used": False,
        },
        "release_test": {
            "all_192_paths_replayed": paths == EXPECTED_PATHS,
            "all_23_groups_replayed": len(groups) == EXPECTED_GROUPS,
            "all_1296_symmetric_node_entries_replayed": upper_entries == EXPECTED_UPPER_ENTRIES,
            "all_2400_ordered_directional_entries_compiled": len(descriptors) == EXPECTED_ORDERED_ENTRIES,
            "all_18_native_axes_compiled": len(axis_rows) == 18 and [row["axis"] for row in axis_rows] == list(AXES),
            "every_axis_touches_an_entry": all(row["entries_touched"] > 0 for row in axis_rows),
            "maximum_rank_remains_four": max(row["maximum_species_determinant_rank_touched"] for row in axis_rows) == 4,
            "global_second_derivative_integrals_computed": False,
            "complete_order_eight_remainder_emitted": False,
        },
        "next_exact_input": "evaluate the complete compiled group jets on all eighteen axes, then bind their global second derivatives to K344's positive Peano kernels on a zero-safe whole-orthant cover",
        "ledger_effect": k345["ledger_effect"],
        "source_routing": k345["source_routing"],
        "claim_ceiling": "Exact complete eighteen-axis differentiation interface for all 192 order-eight paths, 23 coherent groups, 1,296 symmetric-node upper-triangle entries and all 2,400 ordered directional entries. Off-diagonal orientations are kept separate because one-sided raw-time derivatives break the node symmetry. Every old-position and determinant primitive kernel carries its native axis mask, and complete coherent forms remain assembled before enclosure. This emits no global derivative norm, Peano remainder, complete order-eight integral, action column, R_ref residual, K152 interval, source/ledger move, canon, paper, public or physical claim.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["paths"], fixed["coherent_groups"], fixed["upper_triangle_gram_entries_at_symmetric_node"], fixed["ordered_directional_entries"]) != (192, 23, 1296, 2400):
        raise AssertionError("K346 census changed")
    if fixed["native_axes"] != list(AXES) or fixed["maximum_species_determinant_rank"] != 4:
        raise AssertionError("K346 native axis or rank contract changed")
    if len(payload["axis_incidence"]) != 18 or not all(row["entries_touched"] > 0 for row in payload["axis_incidence"]):
        raise AssertionError("K346 axis incidence incomplete")
    algebra = payload["jet_algebra"]
    if not algebra["determinants_differentiated_before_group_enclosure"] or not algebra["complete_group_quadratic_forms_differentiated_before_enclosure"]:
        raise AssertionError("K346 coherent differentiation order changed")
    if algebra["occurrencewise_absolute_value_used"] or algebra["raw_zero_bessel_evaluation_used"] or algebra["maximum_bessel_order_required"] != 3:
        raise AssertionError("K346 forbidden derivative shortcut introduced")
    release = payload["release_test"]
    if not all(release[key] for key in ["all_192_paths_replayed", "all_23_groups_replayed", "all_1296_symmetric_node_entries_replayed", "all_2400_ordered_directional_entries_compiled", "all_18_native_axes_compiled", "every_axis_touches_an_entry", "maximum_rank_remains_four"]):
        raise AssertionError("K346 release test failed")
    if release["global_second_derivative_integrals_computed"] or release["complete_order_eight_remainder_emitted"]:
        raise AssertionError("K346 overclaimed a global remainder")


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
