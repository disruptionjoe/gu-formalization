#!/usr/bin/env python3
"""Compile the current gauge/KT/BFV custody ceiling on the K132 joint kernel."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1206-current-gauge-bfv-custody-ceiling.json"

def load(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "lab/process" / name).read_text())

def build() -> dict[str, Any]:
    k1182 = load("k1182-native-upsilon-k132-complement-ranks.json")
    k873 = load("k873-sc-act-06-owned-symmetry-custody.json")
    k941 = load("k941-source-epsilon-cotangent-moment-map.json")
    k944 = load("k944-source-epsilon-regular-bfv-boundary.json")
    k949 = load("k949-source-epsilon-seven-lock-boundary-contract.json")
    cases = k1182["exact_controls"]["cases"]
    joint = [cases[0]["ker_h_intersect_ker_j_dimension"]] * 2 + [cases[1]["ker_h_intersect_ker_j_dimension"]]
    gauge = cases[0]["owned_gauge_rank"]
    full_u = k873["owned_image"]["image_dimension"]
    after_full_u = [n - gauge - full_u for n in joint]
    after_rank98 = [n - 98 for n in after_full_u]
    release = {
        "selected_joint_kernel_dimensions_pinned": joint == [98312, 98312, 98315],
        "native_t0_distortion_gauge_rank_is_four": gauge == 4,
        "connection_coordinate_gauge_rank_is_16384": full_u == 16384,
        "connection_gauge_not_authenticated_as_independent_k132_distortion_column": not k873["decision"]["owned_complete_full_field_symmetry_image_authenticated"],
        "cotangent_constraint_rank_is_91_on_separate_parent": k941["theorem"]["vertical_derivative_rank"] == 91,
        "finite_bfv_is_zero_level_only": not k944["decision"]["current_nonzero_endpoint_admitted_by_zero_BFV"],
        "seven_lock_owner_missing": not k949["theorem"]["formal_multiplier_action_is_source_owned"],
        "full_u_overgrant_leaves_nonnull_81924": after_full_u[:2] == [81924, 81924],
        "full_u_overgrant_leaves_null_81927": after_full_u[2] == 81927,
        "rank98_overgrant_still_leaves_81826_81829": after_rank98 == [81826, 81826, 81829],
    }
    return {
        "schema_version": "1.0", "result_id": "K1206-CURRENT-GAUGE-BFV-CUSTODY-CEILING",
        "created": "2026-10-06", "status": "working_draft_verified", "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native", "target_claim": "SC-ACT-06",
        "scope": "Custody and favorable-overgrant census for current native and auxiliary gauge/KT/BFV candidates at the selected K132 symbol.",
        "gu_typed_objects": {
            "carrier": "selected K132 full field fibre on positive, negative and null covectors",
            "native_map": "metric diffeomorphism image inside ker(H) intersect ker(J)",
            "coordinate_candidate": "full U(64,64) principal connection gauge image on connection coordinates",
            "separate_parent": "source-epsilon cotangent/BFV parent and seven-lock boundary contract",
            "target": "MAP-TYPE=custody-preserving joint-kernel gauge census",
        },
        "exact_control": {
            "causal_strata": ["nonnull_positive", "nonnull_negative", "null_auxiliary_nonzero"],
            "joint_kernel_dimensions": joint, "actual_native_t0_gauge_rank": gauge,
            "full_u_connection_coordinate_rank": full_u, "unowned_best_rank": 98,
            "residual_after_full_u_overgrant": after_full_u,
            "residual_after_full_u_and_rank98_overgrant": after_rank98,
            "cotangent_constraint_rank": 91, "seven_lock_rank": 7,
        },
        "decision": {
            "known_candidate_meeting_native_k132_enlarged_gauge_packet": False,
            "full_u_connection_map_promoted_to_independent_distortion_gauge": False,
            "cotangent_bfv_transported_to_k132": False,
            "ordinary_known_gauge_enlargement_closes_joint_kernel": False,
            "new_source_owned_map_remains_open": True,
            "protected_status_moves": False,
        },
        "release_test": release,
        "source_and_ledger_effect": "none",
        "claim_ceiling": "Known-candidate custody ceiling and favorable rank overgrant only; no global impossibility, changed-parent construction, physical quotient or protected verdict follows.",
    }

def validate_payload(p: dict[str, Any]) -> None:
    if not all(p["release_test"].values()): raise AssertionError("K1206 release test failed")
    x = p["exact_control"]
    if x["residual_after_full_u_overgrant"] != [81924, 81924, 81927]: raise AssertionError("K1206 full-U arithmetic changed")
    if x["residual_after_full_u_and_rank98_overgrant"] != [81826, 81826, 81829]: raise AssertionError("K1206 rank-98 arithmetic changed")
    if p["decision"]["full_u_connection_map_promoted_to_independent_distortion_gauge"]: raise AssertionError("K1206 custody promotion")
    if p["decision"]["protected_status_moves"]: raise AssertionError("K1206 protected move")

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    p = build(); validate_payload(p); text = json.dumps(p, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(text) if args.write else print(text, end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())
