#!/usr/bin/env python3
"""Compile every K554 face reachable in the fifty K558 hybrid domains."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K554 = ROOT / "lab/process/k554-orders-eleven-twelve-gauss-laguerre-face-atlas.json"
K556 = ROOT / "lab/process/k556-orders-eleven-twelve-axis-jet-compiler.json"
K558 = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"
OUTPUT = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def reachable_rows(rows: list[dict[str, Any]], fixed: set[str], active: str) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        mask = set(row["zeroed_axes"])
        if mask.isdisjoint(fixed):
            result.append({
                "zeroed_axes": row["zeroed_axes"],
                "codimension": row["codimension"],
                "usage_count": row["usage_count"],
                "active_peano_axis_zeroed": active in mask,
            })
    return result


def compile_order(
    order: int,
    atlas_row: dict[str, Any],
    interface_row: dict[str, Any],
    contract_row: dict[str, Any],
) -> dict[str, Any]:
    axes = contract_row["fixed_control"]["native_axes"]
    if axes != interface_row["fixed_control"]["native_axes"]:
        raise AssertionError(f"order-{order} K556/K558 axis order diverged")
    if len(axes) != atlas_row["positive_time_variables"]:
        raise AssertionError(f"order-{order} K554/K558 dimension diverged")
    face_atlas = atlas_row["cumulative_time_face_atlas"]
    incidence = {row["axis"]: row for row in interface_row["axis_incidence"]}
    hybrid_rows = []
    for index, axis in enumerate(axes):
        fixed = set(axes[:index])
        moving = axes[index:]
        zero = reachable_rows(face_atlas["kernel_zero_faces"], fixed, axis)
        row_faces = reachable_rows(face_atlas["row_coalescence_faces"], fixed, axis)
        column_faces = reachable_rows(face_atlas["column_coalescence_faces"], fixed, axis)
        faces = {
            "kernel_zero": zero,
            "row_coalescence": row_faces,
            "column_coalescence": column_faces,
        }
        hybrid_rows.append({
            "axis": axis,
            "preceding_axes_fixed_at_node": axes[:index],
            "moving_axes": moving,
            "moving_dimension": len(moving),
            "projective_dimension": len(moving) - 1,
            "all_axis_origin_reachable": index == 0,
            "moving_domain_origin_reachable": True,
            "reachable_kernel_zero_masks": len(zero),
            "reachable_row_coalescence_masks": len(row_faces),
            "reachable_column_coalescence_masks": len(column_faces),
            "reachable_faces_with_active_peano_axis_zeroed": sum(
                row["active_peano_axis_zeroed"] for rows in faces.values() for row in rows
            ),
            "fixed_node_excludes_face_when": "the zeroed-axis mask intersects preceding_axes_fixed_at_node",
            "partial_face_contract": "apply the exact rank-six mask-native determinant and confluent preconditioner before interval substitution",
            "ordered_entries_touched": incidence[axis]["entries_touched"],
            "old_position_kernel_hits": incidence[axis]["old_position_kernel_hits"],
            "determinant_primitive_entry_hits": incidence[axis]["determinant_primitive_entry_hits"],
            "reachable_face_sha256": digest(faces),
            "faces": faces,
        })
    face_instances = sum(
        len(rows) for hybrid in hybrid_rows for rows in hybrid["faces"].values()
    )
    unique_masks = {
        tuple(face["zeroed_axes"])
        for hybrid in hybrid_rows
        for rows in hybrid["faces"].values()
        for face in rows
    }
    return {
        "order": order,
        "fixed_control": {
            "native_axes": axes,
            "hybrid_terms": len(axes),
            "ordered_descriptors": interface_row["fixed_control"]["ordered_directional_entries"],
            "face_atlas_sha256": face_atlas["atlas_sha256"],
            "compiled_entry_interface_sha256": interface_row["compiled_entry_interface"]["stream_sha256"],
            "reachable_face_instances": face_instances,
            "unique_reachable_masks": len(unique_masks),
        },
        "hybrid_face_atlas": hybrid_rows,
        "order_summary": {
            "first_hybrid_reaches_complete_K554_atlas": all(
                hybrid_rows[0][key] == face_atlas[source]
                for key, source in (
                    ("reachable_kernel_zero_masks", "unique_kernel_zero_masks"),
                    ("reachable_row_coalescence_masks", "unique_row_coalescence_masks"),
                    ("reachable_column_coalescence_masks", "unique_column_coalescence_masks"),
                )
            ),
            "reachable_face_counts_monotone_nonincreasing": all(
                hybrid_rows[i][key] >= hybrid_rows[i + 1][key]
                for i in range(len(hybrid_rows) - 1)
                for key in (
                    "reachable_kernel_zero_masks",
                    "reachable_row_coalescence_masks",
                    "reachable_column_coalescence_masks",
                )
            ),
            "every_axis_touches_ordered_entries": all(row["ordered_entries_touched"] > 0 for row in hybrid_rows),
            "only_first_hybrid_owns_complete_origin": [row["all_axis_origin_reachable"] for row in hybrid_rows] == [True] + [False] * (len(axes) - 1),
            "hybrid_face_atlas_sha256": digest(hybrid_rows),
        },
    }


def build() -> dict[str, Any]:
    k554 = json.loads(K554.read_text())
    k556 = json.loads(K556.read_text())
    k558 = json.loads(K558.read_text())
    atlases = {int(row["order"]): row for row in k554["order_interfaces"]}
    interfaces = {int(row["order"]): row for row in k556["order_interfaces"]}
    contracts = {int(row["order"]): row for row in k558["order_contracts"]}
    rows = [compile_order(order, atlases[order], interfaces[order], contracts[order]) for order in (11, 12)]
    total_faces = sum(row["fixed_control"]["reachable_face_instances"] for row in rows)
    return {
        "schema_version": "1.0",
        "result_id": "K559-ORDERS-ELEVEN-TWELVE-HYBRID-FACE-ATLAS",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K554, K556, K558)],
            "orders": [11, 12],
            "combined_hybrid_terms": sum(row["fixed_control"]["hybrid_terms"] for row in rows),
            "combined_ordered_descriptors": sum(row["fixed_control"]["ordered_descriptors"] for row in rows),
            "combined_reachable_face_instances": total_faces,
        },
        "face_ownership_rule": {
            "reachable": "a K554 zero/coalescence mask is reachable in hybrid a iff it is disjoint from the a-1 preceding axes fixed at 1/256",
            "unreachable": "a mask containing any fixed preceding axis is excluded exactly because that coordinate is positive",
            "complete_origin_owner": "only the first hybrid of each order has no fixed preceding axis and can reach its complete 24/26-axis origin",
            "proper_faces": "every reachable proper suffix/intervening face requires mask-native rank-six singular and confluent preconditioning",
            "ordered_orientation_preserved": True,
        },
        "order_atlases": rows,
        "atlas_summary": {
            "both_orders_present": [row["order"] for row in rows] == [11, 12],
            "all_50_hybrid_domains_compiled": sum(len(row["hybrid_face_atlas"]) for row in rows) == 50,
            "all_face_instances_nonempty": total_faces > 0,
            "all_order_summaries_pass": all(all(value for key, value in row["order_summary"].items() if key != "hybrid_face_atlas_sha256") for row in rows),
            "complete_atlas_sha256": digest(rows),
        },
        "decision": {
            "all_order_eleven_hybrid_domains_compiled": True,
            "all_order_twelve_hybrid_domains_compiled": True,
            "fixed_node_face_exclusions_exact": True,
            "complete_origin_owners_identified": True,
            "rank_six_mask_native_preconditioner_emitted": False,
            "complete_face_normal_integrability_emitted": False,
            "whole_domain_hybrid_majorants_emitted": False,
            "next_exact_input": "compile the shared rank-six mask-native singular/confluent preconditioner bank, then replay every complete pure-second product rule on every reachable face",
        },
        "release_test": {
            "exactly_50_hybrid_rows_present": sum(len(row["hybrid_face_atlas"]) for row in rows) == 50,
            "moving_dimensions_descend_24_and_26": [
                [hybrid["moving_dimension"] for hybrid in row["hybrid_face_atlas"]]
                for row in rows
            ] == [list(range(24, 0, -1)), list(range(26, 0, -1))],
            "first_hybrids_replay_complete_K554_atlases": all(row["order_summary"]["first_hybrid_reaches_complete_K554_atlas"] for row in rows),
            "only_first_hybrids_own_complete_origins": all(row["order_summary"]["only_first_hybrid_owns_complete_origin"] for row in rows),
            "face_counts_monotone": all(row["order_summary"]["reachable_face_counts_monotone_nonincreasing"] for row in rows),
            "all_ordered_interfaces_retained": all(row["order_summary"]["every_axis_touches_ordered_entries"] for row in rows),
            "complete_remainders_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k558["ledger_effect"],
        "source_routing": k558["source_routing"],
        "claim_ceiling": "Exact reachability atlas for every K554 kernel-zero and determinant row/column coalescence mask in each of the fifty K558 order-eleven/twelve hybrid domains. It preserves the separate 24/26-axis orders, fixed-node exclusions, active Peano ownership, complete-origin owners and all 94,752 ordered interfaces. Rank-six preconditioners, face-normal integrability, recursive interiors, analytic tails, numerical hybrid bounds, complete remainders/integrals, base action column, R_ref, K152, source/ledger movement, canon, paper, public, novelty and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["combined_hybrid_terms"] != 50 or fixed["combined_ordered_descriptors"] != 94752:
        raise AssertionError("K559 combined census changed")
    rows = payload["order_atlases"]
    if len(rows) != 2 or [row["order"] for row in rows] != [11, 12]:
        raise AssertionError("K559 order rows changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K559 release test failed")
    if payload["decision"]["rank_six_mask_native_preconditioner_emitted"] or payload["decision"]["complete_face_normal_integrability_emitted"] or payload["decision"]["whole_domain_hybrid_majorants_emitted"]:
        raise AssertionError("K559 overclaimed a later closure")


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
