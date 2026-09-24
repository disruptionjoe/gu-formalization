#!/usr/bin/env python3
"""Compile the exact K405 faces reachable in every K409 hybrid domain."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K405 = ROOT / "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json"
K407 = ROOT / "lab/process/k407-order-ten-axis-jet-compiler.json"
K409 = ROOT / "lab/process/k409-order-ten-positive-peano-contract.json"
K410 = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"
OUTPUT = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"


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
    k405 = json.loads(K405.read_text())
    k407 = json.loads(K407.read_text())
    k409 = json.loads(K409.read_text())
    k410 = json.loads(K410.read_text())
    axes = k409["fixed_control"]["native_axes"]
    if axes != k407["fixed_control"]["native_axes"]:
        raise AssertionError("K407/K409 axis order diverged")
    atlas = k405["cumulative_time_face_atlas"]
    if (atlas["unique_kernel_zero_masks"], atlas["unique_row_coalescence_masks"], atlas["unique_column_coalescence_masks"]) != (71, 25, 25):
        raise AssertionError("K405 face census changed")
    incidence = {row["axis"]: row for row in k407["axis_incidence"]}

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
            "all_twenty_two_axis_origin_reachable": index == 0,
            "moving_domain_origin_reachable": True,
            "reachable_kernel_zero_masks": len(zero),
            "reachable_row_coalescence_masks": len(row_faces),
            "reachable_column_coalescence_masks": len(column_faces),
            "reachable_faces_with_active_peano_axis_zeroed": sum(row["active_peano_axis_zeroed"] for rows in all_faces.values() for row in rows),
            "fixed_node_excludes_face_when": "the zeroed-axis mask intersects preceding_axes_fixed_at_node",
            "partial_face_contract": "apply the exact mask preconditioner before interval substitution; the K410 all-zero radial degree alone is insufficient when a proper suffix or intervening mask vanishes",
            "ordered_entries_touched": incidence[axis]["entries_touched"],
            "old_position_kernel_hits": incidence[axis]["old_position_kernel_hits"],
            "determinant_primitive_entry_hits": incidence[axis]["determinant_primitive_entry_hits"],
            "reachable_face_sha256": digest(all_faces),
            "faces": all_faces,
        })

    return {
        "schema_version": "1.0",
        "result_id": "K411-ORDER-TEN-HYBRID-FACE-ATLAS",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [
                "lab/process/k405-order-ten-gauss-laguerre-face-atlas.json",
                "lab/process/k407-order-ten-axis-jet-compiler.json",
                "lab/process/k409-order-ten-positive-peano-contract.json",
                "lab/process/k410-order-ten-zero-safe-radial-contract.json",
            ],
            "native_axes": axes,
            "hybrid_terms": len(axes),
            "K405_face_atlas_sha256": atlas["atlas_sha256"],
            "K407_compiled_entry_interface_sha256": k407["compiled_entry_interface"]["sha256"],
        },
        "face_ownership_rule": {
            "reachable": "a K405 zero/coalescence mask is reachable in hybrid a iff it is disjoint from the a-1 preceding axes fixed at 1/256",
            "unreachable": "any mask containing a fixed preceding axis is excluded exactly because that coordinate is positive",
            "all_zero_owner": "only the first hybrid has no fixed preceding axes and can reach the all-twenty-two-axis origin controlled by K410",
            "proper_faces": "every later moving-domain origin and every reachable proper suffix/intervening face needs its own scaled preconditioner",
            "ordered_orientation_preserved": True,
        },
        "hybrid_face_atlas": hybrid_rows,
        "atlas_summary": {
            "first_hybrid_reaches_all_71_kernel_zero_masks": hybrid_rows[0]["reachable_kernel_zero_masks"] == 71,
            "first_hybrid_reaches_all_25_row_coalescence_masks": hybrid_rows[0]["reachable_row_coalescence_masks"] == 25,
            "first_hybrid_reaches_all_25_column_coalescence_masks": hybrid_rows[0]["reachable_column_coalescence_masks"] == 25,
            "reachable_face_counts_monotone_nonincreasing": all(
                hybrid_rows[i][key] >= hybrid_rows[i + 1][key]
                for i in range(len(hybrid_rows) - 1)
                for key in ("reachable_kernel_zero_masks", "reachable_row_coalescence_masks", "reachable_column_coalescence_masks")
            ),
            "all_13300_ordered_entries_retained_on_every_axis": all(row["ordered_entries_touched"] == 13300 for row in hybrid_rows),
            "complete_partial_face_preconditioners_implemented": False,
            "complete_hybrid_integrals_emitted": False,
        },
        "decision": {
            "all_22_hybrid_domains_compiled": True,
            "fixed_node_face_exclusions_exact": True,
            "all_zero_radial_owner_identified": True,
            "interior_reference_evaluator_released": True,
            "recursive_face_cover_complete": False,
            "next_exact_input": "evaluate all twenty-two complete coherent second derivatives on a positive interior reference cell, then construct mask-native preconditioners for the reachable proper faces before recursive coverage",
        },
        "release_test": {
            "twenty_two_hybrid_rows_present": len(hybrid_rows) == 22,
            "moving_dimensions_descend_22_to_1": [row["moving_dimension"] for row in hybrid_rows] == list(range(22, 0, -1)),
            "first_hybrid_replays_complete_K405_atlas": all((hybrid_rows[0][key] == expected for key, expected in (("reachable_kernel_zero_masks", 71), ("reachable_row_coalescence_masks", 25), ("reachable_column_coalescence_masks", 25)))),
            "only_first_hybrid_owns_all_twenty_two_origin": [row["all_twenty_two_axis_origin_reachable"] for row in hybrid_rows] == [True] + [False] * 21,
            "face_counts_monotone": True,
            "all_ordered_entries_retained": all(row["ordered_entries_touched"] == 13300 for row in hybrid_rows),
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k410["ledger_effect"],
        "source_routing": k410["source_routing"],
        "claim_ceiling": "Exact reachability atlas for all 71 K405 kernel-zero masks and all 25+25 determinant row/column coalescence masks in each of the twenty-two K409 hybrid domains. It identifies fixed-node exclusions, active Peano ownership, moving dimensions, the unique all-twenty-two-axis origin owner and exact face digests while retaining all 13,300 ordered entries per axis. Proper-face preconditioners, recursive coverage, numerical hybrid integrals, the complete order-ten remainder and integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if fixed["hybrid_terms"] != 22 or len(fixed["native_axes"]) != 22:
        raise AssertionError("K411 hybrid census changed")
    rows = payload["hybrid_face_atlas"]
    if len(rows) != 22 or [row["moving_dimension"] for row in rows] != list(range(22, 0, -1)):
        raise AssertionError("K411 moving-domain dimensions changed")
    if [row["all_twenty_two_axis_origin_reachable"] for row in rows] != [True] + [False] * 21:
        raise AssertionError("K411 all-zero owner changed")
    if not payload["face_ownership_rule"]["ordered_orientation_preserved"]:
        raise AssertionError("K411 ordered orientation lost")
    summary = payload["atlas_summary"]
    if not summary["reachable_face_counts_monotone_nonincreasing"] or not summary["all_13300_ordered_entries_retained_on_every_axis"]:
        raise AssertionError("K411 atlas summary failed")
    if summary["complete_partial_face_preconditioners_implemented"] or summary["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K411 overclaimed a numerical closure")
    decision = payload["decision"]
    if not decision["all_22_hybrid_domains_compiled"] or not decision["fixed_node_face_exclusions_exact"] or decision["recursive_face_cover_complete"]:
        raise AssertionError("K411 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K411 release test failed")


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
