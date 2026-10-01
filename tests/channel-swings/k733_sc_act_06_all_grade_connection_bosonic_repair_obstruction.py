#!/usr/bin/env python3
"""K733: strongest dimension-only all-grade connection repair of K720."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k732": ROOT / "lab/process/k732-sc-act-06-all-grade-connection-i2b-rank-ceiling.json",
}
OUTPUT = ROOT / "lab/process/k733-sc-act-06-all-grade-connection-bosonic-repair-obstruction.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k720 = json.loads(PATHS["k720"].read_text(encoding="utf-8"))
    k732 = json.loads(PATHS["k732"].read_text(encoding="utf-8"))
    n = k720["exact_controls"]["field_dimension"]
    gauge = k720["exact_controls"]["owned_metric_diffeomorphism_rank"]
    repair = k732["existing_all_grade_connection_response"]["i2b_hessian_rank_ceiling"]
    cases = []
    for old in k720["exact_controls"]["cases"]:
        required = n - gauge - old["action_euler_rank"]
        combined_rank_upper = min(n, old["action_euler_rank"] + repair)
        kernel_lower = n - combined_rank_upper
        cohomology_lower = kernel_lower - gauge
        cases.append({
            "case": old["case"],
            "i1b_rank": old["action_euler_rank"],
            "minimum_new_rank_required_for_middle_exactness": required,
            "granted_connection_i2b_rank_ceiling": repair,
            "rank_shortfall_after_grant": required - repair,
            "combined_rank_upper": combined_rank_upper,
            "combined_kernel_lower": kernel_lower,
            "owned_gauge_image_rank": gauge,
            "middle_cohomology_lower": cohomology_lower,
            "middle_exact_possible_under_grant": cohomology_lower <= 0,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K733-SC-ACT-06-ALL-GRADE-CONNECTION-BOSONIC-REPAIR-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Dimension-only strongest-grant test that transports the entire existing rank-1470 all-grade connection response into K720 with arbitrary weight and maximally favorable image placement; this is not a native cross-background composition.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "strongest_grant": {
            "formula": "rank(A+cH) <= rank(A)+rank(H)",
            "arbitrary_nonzero_relative_weight": True,
            "maximally_favorable_image_placement": True,
            "no_i1b_i2b_image_overlap_assumed": True,
            "cross_background_transport_granted_for_dimension_test_only": True,
            "native_cross_background_composition_claimed": False,
        },
        "exact_controls": {
            "field_dimension": n,
            "owned_metric_diffeomorphism_rank": gauge,
            "connection_i2b_rank_ceiling": repair,
            "cases": cases,
            "nonnull_middle_cohomology_lower": cases[0]["middle_cohomology_lower"],
            "native_null_middle_cohomology_lower": cases[1]["middle_cohomology_lower"],
        },
        "decision": {
            "existing_all_grade_connection_response_can_repair_k720_to_middle_exactness": False,
            "connection_only_i2b_route_meets_required_new_rank_on_either_stratum": False,
            "moving_metric_epsilon_or_other_new_principal_directions_remain_required": True,
            "source_global_SC_ACT_06_refuted": False,
            "next_exact_input": "A stationary source-typed Euclidean germ whose complete moving metric/epsilon/connection I2B principal map contributes at least 98470/106634 independent new ranks relative to the selected I1B strata, or a different action-owned principal packet, with actual gauge/redundancy maps.",
        },
        "gu_typed_objects": {
            "carrier": "K720 coupled bosonic carrier of complex dimension 229386",
            "pairing": "selected I1B action form plus a granted arbitrary-weight I2B Hessian factored through the exact rank-1470 connection response",
            "real_structure": "dimension-only transport grant; no coherent Euclidean cross-background owner inferred",
            "grading": "rank-four metric diffeomorphism gauge -> coupled bosonic fields -> combined Euler rows",
            "action_owner": "I1B and printed-endpoint I2B remain distinct; only their maximum possible ranks are combined",
            "target": "middle exactness at both K720 covector strata",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result excludes only a connection-only dimension transfer into one rejected flat realization; it does not construct or exclude the complete moving field Hessian or another stationary germ.",
        "controls": {
            "producer": "tests/channel-swings/k733_sc_act_06_all_grade_connection_bosonic_repair_obstruction.py",
            "probe": "tests/channel-swings/k733_sc_act_06_all_grade_connection_bosonic_repair_obstruction_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 33,
        },
        "claim_ceiling": "Exact lower bounds under a maximally favorable dimension-only transport of the existing all-grade connection response. No native cross-background composition, complete moving-I2B no-go, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    g, c, d = p["strongest_grant"], p["exact_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert g["formula"] == "rank(A+cH) <= rank(A)+rank(H)"
    assert all(g[k] for k in (
        "arbitrary_nonzero_relative_weight", "maximally_favorable_image_placement",
        "no_i1b_i2b_image_overlap_assumed", "cross_background_transport_granted_for_dimension_test_only",
    ))
    assert not g["native_cross_background_composition_claimed"]
    assert c["field_dimension"] == 229386 and c["owned_metric_diffeomorphism_rank"] == 4
    assert c["connection_i2b_rank_ceiling"] == 1470
    assert c["cases"] == [
        {"case": "native_nonnull", "i1b_rank": 130912, "minimum_new_rank_required_for_middle_exactness": 98470, "granted_connection_i2b_rank_ceiling": 1470, "rank_shortfall_after_grant": 97000, "combined_rank_upper": 132382, "combined_kernel_lower": 97004, "owned_gauge_image_rank": 4, "middle_cohomology_lower": 97000, "middle_exact_possible_under_grant": False},
        {"case": "native_null_auxiliary_nonzero", "i1b_rank": 122748, "minimum_new_rank_required_for_middle_exactness": 106634, "granted_connection_i2b_rank_ceiling": 1470, "rank_shortfall_after_grant": 105164, "combined_rank_upper": 124218, "combined_kernel_lower": 105168, "owned_gauge_image_rank": 4, "middle_cohomology_lower": 105164, "middle_exact_possible_under_grant": False},
    ]
    assert c["nonnull_middle_cohomology_lower"] == 97000
    assert c["native_null_middle_cohomology_lower"] == 105164
    assert not d["existing_all_grade_connection_response_can_repair_k720_to_middle_exactness"]
    assert not d["connection_only_i2b_route_meets_required_new_rank_on_either_stratum"]
    assert d["moving_metric_epsilon_or_other_new_principal_directions_remain_required"]
    assert not d["source_global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
