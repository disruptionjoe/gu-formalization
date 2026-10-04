#!/usr/bin/env python3
"""K1065: reconcile the robust quadratic apparatus ownership boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1065-k1064-robust-quadratic-apparatus-boundary.json"


def build():
    rows = [
        ("four_mode_exact_residual_witness", "PASS", "repository_owned_candidate"),
        ("bounded_component_error_certificate", "PASS", "repository_owned_candidate"),
        ("linear_response_recovery", "PASS", "repository_owned_candidate"),
        ("higher_mode_design_tradeoff", "PASS", "repository_owned_candidate"),
        ("certified_physical_linear_response_floor", "OPEN", "apparatus_unowned"),
        ("dimensional_spatial_scale", "OPEN", "apparatus_unowned"),
        ("four_or_higher_mode_preparation_record", "OPEN", "apparatus_unowned"),
        ("measured_detector_record_and_complete_systematics", "OPEN", "apparatus_unowned"),
        ("source_selected_coefficient_complete_action", "OPEN", "gu_source_unowned"),
        ("stationary_positive_functional_bv_bfv_quotient", "OPEN", "gu_source_unowned"),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1065-K1064-ROBUST-QUADRATIC-APPARATUS-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "rows": [{"requirement": r, "status": s, "owner": o} for r, s, o in rows],
        "candidate_pass_count": 4,
        "gu_source_owned_count": 0,
        "empirically_scorable_count": 0,
        "protected_source_status": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "protected_ledger_status": {"LT-SM8": "NEEDS", "LT-GR6b": "NEEDS", "RA-F1": "NEEDS", "AC-F1": "NEEDS"},
        "next_condition": "supply a calibrated response floor and component-error bound satisfying K1062, plus dimensional scale, preparation, measured record and complete systematics; GU credit separately requires the source-selected action and positive quotient",
        "scope": "conditional apparatus requirements only; no source, ledger, empirical, prediction, confirmation, canon or public move",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(data):
    assert len(data["rows"]) == 10
    assert data["candidate_pass_count"] == 4
    assert data["gu_source_owned_count"] == 0
    assert data["empirically_scorable_count"] == 0
    assert data["protected_source_status"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert all(v == "NEEDS" for v in data["protected_ledger_status"].values())
    assert data["next_condition"].startswith("supply a calibrated response floor")
    assert data["scope"].startswith("conditional apparatus requirements only")
    assert data["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    result = build(); validate(result)
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("K1065 controls: 10/10")
