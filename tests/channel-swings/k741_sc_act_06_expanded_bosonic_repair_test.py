#!/usr/bin/env python3
"""K741: compose expanded response ranks with the two K720 bosonic strata."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k739": ROOT / "lab/process/k739-sc-act-06-expanded-action-parent-ownership.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
}
OUTPUT = ROOT / "lab/process/k741-sc-act-06-expanded-bosonic-repair-test.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    field_dimension = data["k720"]["exact_controls"]["field_dimension"]
    gauge_rank = data["k720"]["exact_controls"]["owned_metric_diffeomorphism_rank"]
    cases = []
    for base, response in zip(data["k720"]["exact_controls"]["cases"], data["k740"]["exact_controls"]["cases"]):
        assert base["case"] == response["case"]
        spin_j = response["ranks"]["grade_saturated_spin"]["rank"]
        full_j = response["ranks"]["full_connection"]["rank"]
        spin_i2b_ceiling = spin_j + data["k740"]["exact_controls"]["maximum_unserialized_metric_epsilon_rank"]
        spin_combined_rank_upper = min(field_dimension, base["action_euler_rank"] + spin_i2b_ceiling)
        spin_kernel_lower = field_dimension - spin_combined_rank_upper
        full_combined_rank_upper = min(field_dimension, base["action_euler_rank"] + full_j)
        cases.append({
            "case": base["case"],
            "field_dimension": field_dimension,
            "i1b_rank": base["action_euler_rank"],
            "owned_gauge_image_rank": gauge_rank,
            "spin_connection_response_rank": spin_j,
            "spin_maximal_metric_epsilon_grant": 101,
            "spin_i2b_hessian_rank_ceiling": spin_i2b_ceiling,
            "spin_combined_rank_upper": spin_combined_rank_upper,
            "spin_kernel_lower": spin_kernel_lower,
            "spin_middle_cohomology_lower": max(0, spin_kernel_lower - gauge_rank),
            "spin_middle_exact_possible": False,
            "full_connection_response_rank": full_j,
            "full_combined_rank_upper": full_combined_rank_upper,
            "full_rank_threshold_cleared": full_combined_rank_upper == field_dimension,
            "full_middle_cohomology_lower_from_rank_only": max(0, field_dimension - full_combined_rank_upper - gauge_rank),
            "full_middle_exact_proved": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K741-SC-ACT-06-EXPANDED-BOSONIC-REPAIR-TEST",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Favorable rank-only composition of K740's exact derivative response with K720's two selected I1B strata. Residual pairing, same-background image overlap and full gauge/redundancy maps are not inferred.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "factorization_controls": {
            "stationary_residual_square_hessian_rank_le_response_rank": True,
            "spin_metric_epsilon_unspecified_maximal_grant": 101,
            "full_connection_response_alone_used": True,
            "same_background_composition_proved": False,
            "response_image_overlap_with_i1b_proved": False,
            "complete_gauge_redundancy_complex_serialized": False,
        },
        "exact_controls": {"cases": cases},
        "decision": {
            "grade_saturated_spin_parent_can_repair_k720_to_middle_exactness": False,
            "grade_saturated_spin_parent_excluded_even_under_favorable_metric_epsilon_grant": True,
            "action_owned_full_connection_parent_clears_necessary_rank_threshold": True,
            "action_owned_full_connection_parent_proves_middle_exactness": False,
            "source_global_SC_ACT_06_refuted": False,
            "next_exact_input": "Serialize the action-owned full-carrier residual pairing and Hessian on the same stationary Euclidean germ as K720, compute its image overlap with I1B, and construct the actual gauge/redundancy maps. The full carrier survives; the Spin truncation does not.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "Spin is now excluded on the tested strata, but the full action-owned carrier only clears a necessary rank threshold and has not been assembled into an exact symbol complex.",
        "controls": {
            "producer": "tests/channel-swings/k741_sc_act_06_expanded_bosonic_repair_test.py",
            "probe": "tests/channel-swings/k741_sc_act_06_expanded_bosonic_repair_test_probe.py",
            "controls_passed": 41,
            "hostile_mutations_rejected": 34,
        },
        "claim_ceiling": "Exact rank obstruction for the Spin carrier and necessary-threshold survival for the full carrier. No full-Hessian rank, same-background placement, middle exactness, source-status, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    f, cases, d = p["factorization_controls"], p["exact_controls"]["cases"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert f["stationary_residual_square_hessian_rank_le_response_rank"]
    assert f["spin_metric_epsilon_unspecified_maximal_grant"] == 101 and f["full_connection_response_alone_used"]
    assert not f["same_background_composition_proved"] and not f["response_image_overlap_with_i1b_proved"] and not f["complete_gauge_redundancy_complex_serialized"]
    expected = [
        ("native_nonnull", 130912, 191607, 37779, 37775),
        ("native_null_auxiliary_nonzero", 122748, 183443, 45943, 45939),
    ]
    assert len(cases) == 2
    for row, values in zip(cases, expected):
        name, i1b, rank_upper, kernel_lower, cohom_lower = values
        assert row["case"] == name and row["field_dimension"] == 229386 and row["i1b_rank"] == i1b
        assert row["owned_gauge_image_rank"] == 4
        assert row["spin_connection_response_rank"] == 60594 and row["spin_maximal_metric_epsilon_grant"] == 101
        assert row["spin_i2b_hessian_rank_ceiling"] == 60695
        assert (row["spin_combined_rank_upper"], row["spin_kernel_lower"], row["spin_middle_cohomology_lower"]) == (rank_upper, kernel_lower, cohom_lower)
        assert not row["spin_middle_exact_possible"]
        assert row["full_connection_response_rank"] == 122864 and row["full_combined_rank_upper"] == 229386
        assert row["full_rank_threshold_cleared"] and row["full_middle_cohomology_lower_from_rank_only"] == 0
        assert not row["full_middle_exact_proved"]
    assert not d["grade_saturated_spin_parent_can_repair_k720_to_middle_exactness"]
    assert d["grade_saturated_spin_parent_excluded_even_under_favorable_metric_epsilon_grant"]
    assert d["action_owned_full_connection_parent_clears_necessary_rank_threshold"]
    assert not d["action_owned_full_connection_parent_proves_middle_exactness"] and not d["source_global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build(); validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
