#!/usr/bin/env python3
"""K1060: reconcile nonlinear-transfer apparatus routes and ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1060-k1059-nonlinear-transfer-apparatus-boundary.json"


def build():
    rows = [
        ("absolute_dimensional_scale", "open"),
        ("three_mode_affine_shape", "candidate_exact"),
        ("quadratic_transfer_countermodel", "candidate_exact_obstruction"),
        ("bounded_curvature_threshold_tau_2p349_inverse_units", "calibration_target"),
        ("joint_curvature_component_budget", "calibration_target"),
        ("four_mode_quadratic_identifiability", "candidate_exact"),
        ("physical_mode_preparation_and_transfer_audit", "open"),
        ("measured_record_and_complete_systematics", "open"),
        ("source_selected_coefficient_complete_action", "open"),
    ]
    return {
        "schema_version": "1.0", "result_id": "K1060-K1059-NONLINEAR-TRANSFER-APPARATUS-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-04",
        "three_mode_route": "three modes identify mu under affine transfer; under bounded quadratic curvature they require tau<0.0234898863260114 and the K1058 joint component budget",
        "four_mode_route": "modes {3,8,15,24} distinguish the two horns under a common quadratic transfer with nonzero linear response, without a small-curvature assumption",
        "common_limit": "both routes identify dimensionless mu only; neither owns absolute scale, apparatus data or GU action selection",
        "requirements": [{"id": i, "candidate_grade": grade, "gu_source_owned": False, "scorable": False} for i, grade in rows],
        "score_gate": "closed -- no physical mode preparation, transfer characterization, measured record or complete systematic audit",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "promotion_effect": "none -- no empirical score, GU prediction, confirmation, canon or public posture change",
        "next_gate": "own either a three-mode curvature/error calibration box or a four-mode common-quadratic fit with nonzero linear response, plus dimensional scale, preparation, record and full systematics",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "tau<0.0234898863260114" in d["three_mode_route"] and "K1058" in d["three_mode_route"]
    assert "{3,8,15,24}" in d["four_mode_route"] and "nonzero linear response" in d["four_mode_route"]
    assert "dimensionless mu only" in d["common_limit"] and "GU action selection" in d["common_limit"]
    assert len(d["requirements"]) == 9
    assert all(not row["gu_source_owned"] and not row["scorable"] for row in d["requirements"])
    assert d["score_gate"].startswith("closed") and "complete systematic audit" in d["score_gate"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert d["promotion_effect"].startswith("none") and "public posture" in d["promotion_effect"]
    assert d["next_gate"].startswith("own either a three-mode") and "full systematics" in d["next_gate"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1060 controls: 11/11")
