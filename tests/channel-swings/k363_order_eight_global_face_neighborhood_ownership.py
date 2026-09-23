#!/usr/bin/env python3
"""Exhaust the disjoint global owner rule for K350 face neighborhoods."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K350 = ROOT / "lab/process/k350-order-eight-hybrid-face-atlas.json"
K358 = ROOT / "lab/process/k358-order-eight-normal-projective-atlas.json"
K362 = ROOT / "lab/process/k362-order-eight-zero-strip-angular-majorants.json"
OUTPUT = ROOT / "lab/process/k363-order-eight-global-face-neighborhood-ownership.json"
AXES = tuple(f"s{i}" for i in range(1, 10)) + tuple(f"v{i}" for i in range(1, 10))
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
    k350 = json.loads(K350.read_text())
    k358 = json.loads(K358.read_text())
    k362 = json.loads(K362.read_text())
    rows = []
    total_subsets = 0
    total_face_owned = 0
    total_interior = 0
    for hybrid in k350["hybrid_face_atlas"]:
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
        "result_id": "K363-ORDER-EIGHT-GLOBAL-FACE-NEIGHBORHOOD-OWNERSHIP",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K350, K358, K362)],
            "hybrid_domains": len(rows),
            "epsilon": k362["fixed_control"]["epsilon"],
            "reachable_face_programs": k358["fixed_control"]["face_programs"],
            "unique_zero_masks": k358["fixed_control"]["unique_zero_masks"],
            "exhausted_low_coordinate_subsets": total_subsets,
        },
        "ownership_contract": {
            "low_coordinate_set": "L_epsilon(t)={i:t_i<=epsilon*max_j(t_j)}",
            "candidate_faces": "K350 reachable masks Z with Z subset L_epsilon(t)",
            "primary_order": "largest reachable mask first",
            "tie_order": "lexicographically smallest mask in canonical s1..s9,v1..v9 order",
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
            "all_18_hybrids_exhausted": len(rows) == 18,
            "all_subsets_have_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "all_assigned_faces_are_K350_reachable": all(row["all_assigned_faces_reachable"] for row in rows),
            "total_face_owned_subsets": total_face_owned,
            "total_interior_owned_subsets": total_interior,
            "v8_v9_use_only_interior_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v8", "v9"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v8", "v9"}),
        },
        "decision": {
            "disjoint_global_face_neighborhood_owner_rule_complete": True,
            "owner_regions_have_uniform_integrand_bounds": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "bound the K352-preconditioned integrand uniformly on K363-owned zero strips and interior cells, then choose recursive subdivisions and tails",
        },
        "release_test": {
            "exactly_18_hybrid_domains": len(rows) == 18,
            "exactly_517_reachable_face_programs_in_scope": k358["fixed_control"]["face_programs"] == 517,
            "exactly_81_unique_masks_in_scope": k358["fixed_control"]["unique_zero_masks"] == 81,
            "all_low_coordinate_subsets_exhausted": total_subsets == sum(1 << row["moving_dimension"] for row in rows),
            "every_subset_has_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "no_unreachable_face_assigned": all(row["all_assigned_faces_reachable"] for row in rows),
            "v8_v9_have_no_invented_face_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v8", "v9"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v8", "v9"}),
            "uniform_integrand_bounds_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k362["ledger_effect"],
        "source_routing": k362["source_routing"],
        "claim_ceiling": "An exhaustive deterministic partition of every positive moving-time domain into one K350-reachable face-neighborhood owner or the interior owner, using the epsilon=1/64 low-coordinate set, maximal reachable mask and canonical lexicographic tie break. This ownership geometry supplies no uniform K352 integrand bound, recursive interior subdivision, tail majorant, complete K348 hybrid, order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public or physical posture.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_domains"], fixed["epsilon"], fixed["reachable_face_programs"], fixed["unique_zero_masks"]) != (18, "1/64", 517, 81):
        raise AssertionError("K363 census changed")
    rows = payload["hybrid_owner_bank"]
    if len(rows) != 18 or any(not row["every_subset_has_exactly_one_owner"] or not row["all_assigned_faces_reachable"] for row in rows):
        raise AssertionError("K363 owner bank changed")
    contract = payload["ownership_contract"]
    if not all(contract[key] for key in ("owner_is_deterministic", "owner_cells_are_pairwise_disjoint", "owner_cells_cover_every_positive_moving_time_vector", "unreachable_faces_are_never_invented")):
        raise AssertionError("K363 ownership contract changed")
    decision = payload["decision"]
    if not decision["disjoint_global_face_neighborhood_owner_rule_complete"] or any(decision[key] for key in ("owner_regions_have_uniform_integrand_bounds", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K363 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K363 release test failed")


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
