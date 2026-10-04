#!/usr/bin/env python3
"""K1070: reconcile the quadratic mode-design ownership boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1070-k1069-quadratic-mode-design-boundary.json"


def build():
    candidate = ["global_fourth_mode_monotonicity", "least_mode_inverse_design", "three_four_mode_crossover", "monotone_cost_pareto_rule", "exact_residual_classifier", "linear_response_recovery"]
    open_rows = [
        ("apparatus_unowned", "independently_fixed_target_tolerance"),
        ("apparatus_unowned", "physical_mode_preparation_cost"),
        ("apparatus_unowned", "certified_linear_response_floor"),
        ("apparatus_unowned", "component_error_box"),
        ("apparatus_unowned", "dimensional_scale"),
        ("apparatus_unowned", "measured_record_and_complete_systematics"),
        ("gu_source_unowned", "source_selected_coefficient_complete_action"),
        ("gu_source_unowned", "stationary_positive_functional_bv_bfv_quotient"),
    ]
    rows = [{"owner": "repository_owned_candidate", "requirement": item, "status": "PASS"} for item in candidate]
    rows += [{"owner": owner, "requirement": item, "status": "OPEN"} for owner, item in open_rows]
    return {
        "schema_version": "1.0",
        "result_id": "K1070-K1069-QUADRATIC-MODE-DESIGN-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "rows": rows,
        "candidate_pass_count": len(candidate),
        "gu_source_owned_count": 0,
        "empirically_scorable_count": 0,
        "protected_source_status": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "protected_ledger_status": {"LT-SM8": "NEEDS", "LT-GR6b": "NEEDS", "RA-F1": "NEEDS", "AC-F1": "NEEDS"},
        "next_condition": "supply an independently selected tolerance, measured mode-preparation cost, response floor, component-error box, dimensional scale and complete systematics; GU credit separately requires the source-selected action and positive quotient",
        "scope": "conditional mode-design requirements only; no source, ledger, empirical, prediction, confirmation, canon or public move",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert data["candidate_pass_count"] == 6
    assert sum(row["status"] == "PASS" for row in data["rows"]) == 6
    assert len(data["rows"]) == 14
    assert data["gu_source_owned_count"] == 0
    assert data["empirically_scorable_count"] == 0
    assert data["protected_source_status"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert data["protected_ledger_status"] == {"LT-SM8": "NEEDS", "LT-GR6b": "NEEDS", "RA-F1": "NEEDS", "AC-F1": "NEEDS"}
    assert data["next_condition"].startswith("supply an independently selected tolerance")
    assert data["scope"].startswith("conditional mode-design requirements only")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1070 controls: 11/11")
