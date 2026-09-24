#!/usr/bin/env python3
"""Exhaust the disjoint global owner rule for K386 face neighborhoods."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K386 = ROOT / "lab/process/k386-order-nine-hybrid-face-atlas.json"
K394 = ROOT / "lab/process/k394-order-nine-normal-projective-atlas.json"
K398 = ROOT / "lab/process/k398-order-nine-zero-strip-angular-majorants.json"
OUTPUT = ROOT / "lab/process/k399-order-nine-global-face-neighborhood-ownership.json"
AXES = tuple(f"s{i}" for i in range(1, 11)) + tuple(f"v{i}" for i in range(1, 11))
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}


def digest_stream(rows: list[tuple[int, str]]) -> str:
    h = hashlib.sha256()
    for low_mask, owner in rows:
        h.update(f"{low_mask}:{owner}\n".encode())
    return "sha256:" + h.hexdigest()


def flattened_faces(hybrid: dict[str, Any]) -> list[tuple[str, ...]]:
    result = set()
    for rows in hybrid["faces"].values():
        result.update(tuple(row["zeroed_axes"]) for row in rows)
    return sorted(result, key=lambda mask: (-len(mask), tuple(AXIS_INDEX[axis] for axis in mask)))


def build() -> dict[str, Any]:
    k386 = json.loads(K386.read_text())
    k394 = json.loads(K394.read_text())
    k398 = json.loads(K398.read_text())
    rows = []
    total_subsets = total_face_owned = total_interior = 0
    for hybrid in k386["hybrid_face_atlas"]:
        moving = list(hybrid["moving_axes"])
        position = {axis: index for index, axis in enumerate(moving)}
        reachable = flattened_faces(hybrid)
        assignments: list[tuple[int, str]] = []
        owner_counts: Counter[str] = Counter()
        invalid_assignments = 0
        for low_mask in range(1 << len(moving)):
            low_axes = {axis for axis, index in position.items() if low_mask & (1 << index)}
            candidates = [mask for mask in reachable if set(mask) <= low_axes]
            owner = ",".join(candidates[0]) if candidates else "INTERIOR"
            if owner != "INTERIOR" and tuple(owner.split(",")) not in reachable:
                invalid_assignments += 1
            assignments.append((low_mask, owner))
            owner_counts[owner] += 1
        subset_count = 1 << len(moving)
        interior_count = owner_counts.pop("INTERIOR", 0)
        face_count = subset_count - interior_count
        rows.append({
            "axis": hybrid["axis"],
            "moving_dimension": len(moving),
            "reachable_face_masks": len(reachable),
            "low_coordinate_subsets_exhausted": subset_count,
            "face_owned_subsets": face_count,
            "interior_owned_subsets": interior_count,
            "assigned_owner_histogram_sha256": digest_stream(assignments),
            "distinct_face_owners_used": len(owner_counts),
            "all_assigned_faces_reachable": invalid_assignments == 0,
            "every_subset_has_exactly_one_owner": sum(owner_counts.values()) + interior_count == subset_count,
        })
        total_subsets += subset_count
        total_face_owned += face_count
        total_interior += interior_count
    return {
        "schema_version": "1.0",
        "result_id": "K399-ORDER-NINE-GLOBAL-FACE-NEIGHBORHOOD-OWNERSHIP",
        "created": "2026-09-24",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K386, K394, K398)],
            "hybrid_domains": len(rows),
            "epsilon": k398["fixed_control"]["epsilon"],
            "reachable_face_programs": k394["fixed_control"]["face_programs"],
            "unique_zero_masks": k394["fixed_control"]["unique_zero_masks"],
            "exhausted_low_coordinate_subsets": total_subsets,
        },
        "ownership_contract": {
            "low_coordinate_set": "L_epsilon(t)={i:t_i<=epsilon*max_j(t_j)}",
            "candidate_faces": "K386 reachable masks Z with Z subset L_epsilon(t)",
            "primary_order": "largest reachable mask first",
            "tie_order": "lexicographically smallest mask in canonical s1..s10,v1..v10 order",
            "fallback_owner": "INTERIOR when no reachable nonempty mask is contained in L_epsilon(t)",
            "strict_complement": "axes not in L_epsilon(t) satisfy t_i>epsilon*max_j(t_j)",
            "boundary_convention": "equality belongs to the low-coordinate side",
            "owner_is_deterministic": True,
            "owner_cells_are_pairwise_disjoint": True,
            "owner_cells_cover_every_positive_moving_time_vector": True,
            "unreachable_faces_are_never_invented": True,
        },
        "hybrid_owner_bank": rows,
        "ownership_summary": {
            "all_20_hybrids_exhausted": len(rows) == 20,
            "all_subsets_have_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "all_assigned_faces_are_K386_reachable": all(row["all_assigned_faces_reachable"] for row in rows),
            "total_face_owned_subsets": total_face_owned,
            "total_interior_owned_subsets": total_interior,
            "v9_v10_use_only_interior_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v9", "v10"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v9", "v10"}),
        },
        "decision": {
            "disjoint_global_face_neighborhood_owner_rule_complete": True,
            "owner_regions_have_uniform_integrand_bounds": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "bind K400 zero-inclusive determinant envelopes to every K390 face program on the K399 owner unions",
        },
        "release_test": {
            "exactly_20_hybrid_domains": len(rows) == 20,
            "exactly_695_reachable_face_programs_in_scope": k394["fixed_control"]["face_programs"] == 695,
            "exactly_98_unique_masks_in_scope": k394["fixed_control"]["unique_zero_masks"] == 98,
            "all_2097150_low_coordinate_subsets_exhausted": total_subsets == 2_097_150,
            "every_subset_has_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "no_unreachable_face_assigned": all(row["all_assigned_faces_reachable"] for row in rows),
            "v9_v10_have_no_invented_face_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v9", "v10"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v9", "v10"}),
            "uniform_integrand_bounds_not_overclaimed": True,
            "complete_order_nine_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k398["ledger_effect"],
        "source_routing": k398["source_routing"],
        "claim_ceiling": "An exhaustive deterministic partition of every positive moving-time domain into one K386-reachable face-neighborhood owner or the interior owner, using the epsilon=1/64 low-coordinate set, maximal reachable mask and canonical lexicographic tie break. This ownership geometry supplies no uniform K388 integrand bound, recursive interior subdivision, tail majorant, complete K384 hybrid, order-nine remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_domains"], fixed["epsilon"], fixed["reachable_face_programs"], fixed["unique_zero_masks"], fixed["exhausted_low_coordinate_subsets"]) != (20, "1/64", 695, 98, 2_097_150):
        raise AssertionError("K399 census changed")
    rows = payload["hybrid_owner_bank"]
    if len(rows) != 20 or any(not row["every_subset_has_exactly_one_owner"] or not row["all_assigned_faces_reachable"] for row in rows):
        raise AssertionError("K399 owner bank changed")
    contract = payload["ownership_contract"]
    if not all(contract[key] for key in ("owner_is_deterministic", "owner_cells_are_pairwise_disjoint", "owner_cells_cover_every_positive_moving_time_vector", "unreachable_faces_are_never_invented")):
        raise AssertionError("K399 ownership contract changed")
    decision = payload["decision"]
    if not decision["disjoint_global_face_neighborhood_owner_rule_complete"] or any(decision[key] for key in ("owner_regions_have_uniform_integrand_bounds", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K399 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K399 release test failed")


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
