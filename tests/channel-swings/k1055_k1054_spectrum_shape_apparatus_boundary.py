#!/usr/bin/env python3
"""K1055: reconcile spectrum-shape identifiability with apparatus ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1055-k1054-spectrum-shape-apparatus-boundary.json"


def build():
    rows = [
        ("absolute_mass_or_ruler_scale", "open", False, False),
        ("dimensionless_mu_from_exact_three_mode_shape", "candidate_exact", False, False),
        ("three_mode_preparation", "open", False, False),
        ("common_affine_readout_cancellation", "candidate_exact", False, False),
        ("relative_gap_resolution_below_2p233_percent", "calibration_target", False, False),
        ("gain_normalized_component_error_below_1p030_percent", "calibration_target", False, False),
        ("measured_record_and_complete_systematics", "open", False, False),
        ("source_selected_coefficient_complete_action", "open", False, False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1055-K1054-SPECTRUM-SHAPE-APPARATUS-BOUNDARY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "identification_result": "three affine-readout modes identify the dimensionless ratio mu=m^2/s^2, not absolute mass or ruler scale",
        "two_mode_route": "fewer prepared modes and 5.573 percent component-relative-frequency tolerance at fixed ruler, but additive offset must be controlled",
        "three_mode_route": "common gain and offset cancel; exact shape is injective in mu, but three-mode preparation and tighter gap/component resolution are required",
        "sharp_targets": {"relative_gap_percent": "2.232297952916870", "gain_normalized_component_percent": "1.029409976338294"},
        "requirements": [
            {"id": i, "candidate_grade": grade, "gu_source_owned": gu, "scorable": score}
            for i, grade, gu, score in rows
        ],
        "score_gate": "closed -- no owned dimensional scale, physical preparation, measured record or complete systematic audit",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "promotion_effect": "none -- no empirical score, GU prediction, confirmation, canon or public posture change",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "dimensionless ratio mu=m^2/s^2" in d["identification_result"] and "not absolute" in d["identification_result"]
    assert "5.573 percent" in d["two_mode_route"] and "offset must be controlled" in d["two_mode_route"]
    assert "common gain and offset cancel" in d["three_mode_route"] and "tighter" in d["three_mode_route"]
    assert 2.23 < float(d["sharp_targets"]["relative_gap_percent"]) < 2.24
    assert 1.02 < float(d["sharp_targets"]["gain_normalized_component_percent"]) < 1.04
    assert len(d["requirements"]) == 8
    assert all(not row["gu_source_owned"] and not row["scorable"] for row in d["requirements"])
    assert d["score_gate"].startswith("closed") and "complete systematic audit" in d["score_gate"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert d["promotion_effect"].startswith("none") and "public posture" in d["promotion_effect"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1055 controls: 12/12")
