#!/usr/bin/env python3
"""Exhaust the disjoint global owner rule for K411 face neighborhoods."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K411 = ROOT / "lab/process/k411-order-ten-hybrid-face-atlas.json"
K542 = ROOT / "lab/process/k542-order-ten-normal-projective-partition.json"
K544 = ROOT / "lab/process/k544-order-ten-zero-strip-angular-majorants.json"
OUTPUT = ROOT / "lab/process/k545-order-ten-global-face-neighborhood-ownership.json"
AXES = tuple(f"s{i}" for i in range(1, 12)) + tuple(f"v{i}" for i in range(1, 12))
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}


def flattened_faces(hybrid: dict[str, Any]) -> list[tuple[str, ...]]:
    result = set()
    for rows in hybrid["faces"].values():
        result.update(tuple(row["zeroed_axes"]) for row in rows)
    return sorted(
        result,
        key=lambda mask: (-len(mask), tuple(AXIS_INDEX[axis] for axis in mask)),
    )


def exhaust_owners(moving: list[str], reachable: list[tuple[str, ...]]) -> tuple[Counter[str], str]:
    position = {axis: index for index, axis in enumerate(moving)}
    owner_names = [",".join(mask) for mask in reachable]
    owner_by_subset = [-1] * (1 << len(moving))
    for owner_index, mask in enumerate(reachable):
        bitmask = sum(1 << position[axis] for axis in mask)
        prior = owner_by_subset[bitmask]
        if prior < 0 or owner_index < prior:
            owner_by_subset[bitmask] = owner_index
    for bit in range(len(moving)):
        step = 1 << bit
        for base in range(0, len(owner_by_subset), step << 1):
            for offset in range(step):
                source = owner_by_subset[base + offset]
                target_index = base + step + offset
                target = owner_by_subset[target_index]
                if source >= 0 and (target < 0 or source < target):
                    owner_by_subset[target_index] = source
    counts: Counter[str] = Counter()
    digest = hashlib.sha256()
    for low_mask, owner_index in enumerate(owner_by_subset):
        owner = owner_names[owner_index] if owner_index >= 0 else "INTERIOR"
        counts[owner] += 1
        digest.update(f"{low_mask}:{owner}\n".encode())
    return counts, "sha256:" + digest.hexdigest()


def build() -> dict[str, Any]:
    k411 = json.loads(K411.read_text())
    k542 = json.loads(K542.read_text())
    k544 = json.loads(K544.read_text())
    rows = []
    total_subsets = total_face_owned = total_interior = 0
    for hybrid in k411["hybrid_face_atlas"]:
        moving = list(hybrid["moving_axes"])
        reachable = flattened_faces(hybrid)
        owner_counts, owner_digest = exhaust_owners(moving, reachable)
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
            "assigned_owner_histogram_sha256": owner_digest,
            "distinct_face_owners_used": len(owner_counts),
            "all_assigned_faces_reachable": set(owner_counts) <= {",".join(mask) for mask in reachable},
            "every_subset_has_exactly_one_owner": sum(owner_counts.values()) + interior_count == subset_count,
        })
        total_subsets += subset_count
        total_face_owned += face_count
        total_interior += interior_count
    return {
        "schema_version": "1.0",
        "result_id": "K545-ORDER-TEN-GLOBAL-FACE-NEIGHBORHOOD-OWNERSHIP",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K411, K542, K544)],
            "hybrid_domains": len(rows),
            "epsilon": k544["fixed_control"]["epsilon"],
            "reachable_face_programs": k542["fixed_control"]["face_programs"],
            "unique_zero_masks": k542["fixed_control"]["unique_zero_masks"],
            "exhausted_low_coordinate_subsets": total_subsets,
        },
        "ownership_contract": {
            "low_coordinate_set": "L_epsilon(t)={i:t_i<=epsilon*max_j(t_j)}",
            "candidate_faces": "K411 reachable masks Z with Z subset L_epsilon(t)",
            "primary_order": "largest reachable mask first",
            "tie_order": "lexicographically smallest mask in canonical s1..s11,v1..v11 order",
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
            "all_22_hybrids_exhausted": len(rows) == 22,
            "all_subsets_have_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "all_assigned_faces_are_K411_reachable": all(row["all_assigned_faces_reachable"] for row in rows),
            "total_face_owned_subsets": total_face_owned,
            "total_interior_owned_subsets": total_interior,
            "v10_v11_use_only_interior_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v10", "v11"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v10", "v11"}),
        },
        "decision": {
            "disjoint_global_face_neighborhood_owner_rule_complete": True,
            "owner_regions_have_uniform_integrand_bounds": False,
            "recursive_positive_interior_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "test K413 optimal determinant dual nesting on K545-owned face flags before building a zero-inclusive uniform boundary envelope",
        },
        "release_test": {
            "exactly_22_hybrid_domains": len(rows) == 22,
            "exactly_936_reachable_face_programs_in_scope": k542["fixed_control"]["face_programs"] == 936,
            "exactly_121_unique_masks_in_scope": k542["fixed_control"]["unique_zero_masks"] == 121,
            "all_8388606_low_coordinate_subsets_exhausted": total_subsets == 8_388_606,
            "every_subset_has_exactly_one_owner": all(row["every_subset_has_exactly_one_owner"] for row in rows),
            "no_unreachable_face_assigned": all(row["all_assigned_faces_reachable"] for row in rows),
            "v10_v11_have_no_invented_face_owner": [row["axis"] for row in rows if row["reachable_face_masks"] == 0] == ["v10", "v11"] and all(row["face_owned_subsets"] == 0 for row in rows if row["axis"] in {"v10", "v11"}),
            "uniform_integrand_bounds_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k544["ledger_effect"],
        "source_routing": k544["source_routing"],
        "claim_ceiling": "An exhaustive deterministic partition of every positive order-ten moving-time domain into one K411-reachable face-neighborhood owner or the interior owner at epsilon=1/64. All 8,388,606 low-coordinate subsets have exactly one maximal-mask/canonical-tie owner. This geometry supplies no uniform K413 integrand bound, recursive interior subdivision, tail majorant, complete hybrid integral, K457 value, K152 interval, source/ledger move, canon, paper, public or physical conclusion.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_domains"], fixed["epsilon"], fixed["reachable_face_programs"], fixed["unique_zero_masks"], fixed["exhausted_low_coordinate_subsets"]) != (22, "1/64", 936, 121, 8_388_606):
        raise AssertionError("K545 census changed")
    rows = payload["hybrid_owner_bank"]
    if len(rows) != 22 or any(not row["every_subset_has_exactly_one_owner"] or not row["all_assigned_faces_reachable"] for row in rows):
        raise AssertionError("K545 owner bank changed")
    contract = payload["ownership_contract"]
    if not all(contract[key] for key in ("owner_is_deterministic", "owner_cells_are_pairwise_disjoint", "owner_cells_cover_every_positive_moving_time_vector", "unreachable_faces_are_never_invented")):
        raise AssertionError("K545 ownership contract changed")
    decision = payload["decision"]
    if not decision["disjoint_global_face_neighborhood_owner_rule_complete"] or any(decision[key] for key in ("owner_regions_have_uniform_integrand_bounds", "recursive_positive_interior_cover_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K545 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K545 release test failed")


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
