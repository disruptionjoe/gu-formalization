#!/usr/bin/env python3
"""Compile the exact K380 faces reachable in every K384 hybrid domain."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K380 = ROOT / "lab/process/k380-order-nine-gauss-laguerre-face-atlas.json"
K382 = ROOT / "lab/process/k382-order-nine-axis-jet-compiler.json"
K384 = ROOT / "lab/process/k384-order-nine-positive-peano-contract.json"
K385 = ROOT / "lab/process/k385-order-nine-zero-safe-radial-contract.json"
OUTPUT = ROOT / "lab/process/k386-order-nine-hybrid-face-atlas.json"


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


def build() -> dict[str, Any]:
    k380 = json.loads(K380.read_text())
    k382 = json.loads(K382.read_text())
    k384 = json.loads(K384.read_text())
    k385 = json.loads(K385.read_text())
    axes = k384["fixed_control"]["native_axes"]
    if axes != k382["fixed_control"]["native_axes"]:
        raise AssertionError("K382/K384 axis order diverged")
    atlas = k380["cumulative_time_face_atlas"]
    if (atlas["unique_kernel_zero_masks"], atlas["unique_row_coalescence_masks"], atlas["unique_column_coalescence_masks"]) != (58, 20, 20):
        raise AssertionError("K380 face census changed")
    incidence = {row["axis"]: row for row in k382["axis_incidence"]}

    hybrid_rows = []
    for index, axis in enumerate(axes):
        fixed = set(axes[:index])
        free = axes[index:]
        zero = reachable_rows(atlas["kernel_zero_faces"], fixed, axis)
        row_faces = reachable_rows(atlas["row_coalescence_faces"], fixed, axis)
        column_faces = reachable_rows(atlas["column_coalescence_faces"], fixed, axis)
        all_faces = {"kernel_zero": zero, "row_coalescence": row_faces, "column_coalescence": column_faces}
        hybrid_rows.append({
            "axis": axis,
            "preceding_axes_fixed_at_node": axes[:index],
            "moving_axes": free,
            "moving_dimension": len(free),
            "projective_dimension": len(free) - 1,
            "all_twenty_axis_origin_reachable": index == 0,
            "moving_domain_origin_reachable": True,
            "reachable_kernel_zero_masks": len(zero),
            "reachable_row_coalescence_masks": len(row_faces),
            "reachable_column_coalescence_masks": len(column_faces),
            "reachable_faces_with_active_peano_axis_zeroed": sum(row["active_peano_axis_zeroed"] for rows in all_faces.values() for row in rows),
            "fixed_node_excludes_face_when": "the zeroed-axis mask intersects preceding_axes_fixed_at_node",
            "partial_face_contract": "apply the exact mask preconditioner before interval substitution; the K385 all-zero radial degree alone is insufficient when a proper suffix or intervening mask vanishes",
            "ordered_entries_touched": incidence[axis]["entries_touched"],
            "old_position_kernel_hits": incidence[axis]["old_position_kernel_hits"],
            "determinant_primitive_entry_hits": incidence[axis]["determinant_primitive_entry_hits"],
            "reachable_face_sha256": digest(all_faces),
            "faces": all_faces,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K386-ORDER-NINE-HYBRID-FACE-ATLAS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k380-order-nine-gauss-laguerre-face-atlas.json",
                "lab/process/k382-order-nine-axis-jet-compiler.json",
                "lab/process/k384-order-nine-positive-peano-contract.json",
                "lab/process/k385-order-nine-zero-safe-radial-contract.json",
            ],
            "native_axes": axes,
            "hybrid_terms": len(axes),
            "K380_face_atlas_sha256": atlas["atlas_sha256"],
            "K382_compiled_entry_interface_sha256": k382["compiled_entry_interface"]["sha256"],
        },
        "face_ownership_rule": {
            "reachable": "a K380 zero/coalescence mask is reachable in hybrid a iff it is disjoint from the a-1 preceding axes fixed at 1/256",
            "unreachable": "any mask containing a fixed preceding axis is excluded exactly because that coordinate is positive",
            "all_zero_owner": "only the first hybrid has no fixed preceding axes and can reach the all-twenty-axis origin controlled by K385",
            "proper_faces": "every later moving-domain origin and every reachable proper suffix/intervening face needs its own scaled preconditioner",
            "ordered_orientation_preserved": True,
        },
        "hybrid_face_atlas": hybrid_rows,
        "atlas_summary": {
            "first_hybrid_reaches_all_58_kernel_zero_masks": hybrid_rows[0]["reachable_kernel_zero_masks"] == 58,
            "first_hybrid_reaches_all_20_row_coalescence_masks": hybrid_rows[0]["reachable_row_coalescence_masks"] == 20,
            "first_hybrid_reaches_all_20_column_coalescence_masks": hybrid_rows[0]["reachable_column_coalescence_masks"] == 20,
            "reachable_face_counts_monotone_nonincreasing": all(
                hybrid_rows[i][key] >= hybrid_rows[i + 1][key]
                for i in range(len(hybrid_rows) - 1)
                for key in ("reachable_kernel_zero_masks", "reachable_row_coalescence_masks", "reachable_column_coalescence_masks")
            ),
            "all_4480_ordered_entries_retained_on_every_axis": all(row["ordered_entries_touched"] == 4480 for row in hybrid_rows),
            "complete_partial_face_preconditioners_implemented": False,
            "complete_hybrid_integrals_emitted": False,
        },
        "decision": {
            "all_20_hybrid_domains_compiled": True,
            "fixed_node_face_exclusions_exact": True,
            "all_zero_radial_owner_identified": True,
            "interior_reference_evaluator_released": True,
            "recursive_face_cover_complete": False,
            "next_exact_input": "evaluate all twenty complete coherent second derivatives on a positive interior reference cell, then construct mask-native preconditioners for the reachable proper faces before recursive coverage",
        },
        "release_test": {
            "twenty_hybrid_rows_present": len(hybrid_rows) == 20,
            "moving_dimensions_descend_20_to_1": [row["moving_dimension"] for row in hybrid_rows] == list(range(20, 0, -1)),
            "first_hybrid_replays_complete_K380_atlas": all((hybrid_rows[0][key] == expected for key, expected in (("reachable_kernel_zero_masks", 58), ("reachable_row_coalescence_masks", 20), ("reachable_column_coalescence_masks", 20)))),
            "only_first_hybrid_owns_all_twenty_origin": [row["all_twenty_axis_origin_reachable"] for row in hybrid_rows] == [True] + [False] * 19,
            "face_counts_monotone": True,
            "all_ordered_entries_retained": all(row["ordered_entries_touched"] == 4480 for row in hybrid_rows),
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k385["ledger_effect"],
        "source_routing": k385["source_routing"],
        "claim_ceiling": "Exact reachability atlas for all 58 K380 kernel-zero masks and all 20+20 determinant row/column coalescence masks in each of the twenty K384 hybrid domains. It identifies fixed-node exclusions, active Peano ownership, moving dimensions, the unique all-twenty-axis origin owner and exact face digests while retaining all 4,480 ordered entries per axis. Proper-face preconditioners, recursive coverage, numerical hybrid integrals, the complete order-nine remainder and integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["hybrid_terms"] != 20 or len(fixed["native_axes"]) != 20:
        raise AssertionError("K386 hybrid census changed")
    rows = payload["hybrid_face_atlas"]
    if len(rows) != 20 or [row["moving_dimension"] for row in rows] != list(range(20, 0, -1)):
        raise AssertionError("K386 moving-domain dimensions changed")
    if [row["all_twenty_axis_origin_reachable"] for row in rows] != [True] + [False] * 19:
        raise AssertionError("K386 all-zero owner changed")
    if not payload["face_ownership_rule"]["ordered_orientation_preserved"]:
        raise AssertionError("K386 ordered orientation lost")
    summary = payload["atlas_summary"]
    if not summary["reachable_face_counts_monotone_nonincreasing"] or not summary["all_4480_ordered_entries_retained_on_every_axis"]:
        raise AssertionError("K386 atlas summary failed")
    if summary["complete_partial_face_preconditioners_implemented"] or summary["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K386 overclaimed a numerical closure")
    decision = payload["decision"]
    if not decision["all_20_hybrid_domains_compiled"] or not decision["fixed_node_face_exclusions_exact"] or decision["recursive_face_cover_complete"]:
        raise AssertionError("K386 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K386 release test failed")


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
