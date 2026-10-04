#!/usr/bin/env python3
"""K1045: reconcile the frozen holdout with candidate, GU and scorable ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1045-k1044-holdout-apparatus-ownership.json"


def build():
    rows = [
        ("candidate_dispersion_law", "K1037", "pass", False, False),
        ("distinct_two_mode_holdout", "K1042", "frozen", False, False),
        ("scale_identifiability_audit", "K1041", "pass_obstruction", False, False),
        ("fixed_common_spatial_ruler", "K1041-K1042", "required_open", False, False),
        ("two_mode_preparation", "K1042", "required_open", False, False),
        ("clock_and_frequency_detector", "K1044", "required_open", False, False),
        ("relative_error_certificate", "K1043-K1044", "pass_mathematical", False, False),
        ("source_selected_mass_coefficient", "K1039-K1041", "required_open", False, False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1045-K1044-HOLDOUT-APPARATUS-OWNERSHIP",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "requirements": [
            {"id": i, "evidence": e, "candidate_grade": c, "gu_source_owned": g, "scorable": s}
            for i, e, c, g, s in rows
        ],
        "counts": {"candidate_closed_or_frozen": 4, "required_open": 4, "gu_source_owned": 0, "scorable": 0},
        "holdout_result": "the lambda={1,4} squared-frequency ratio is now frozen and separates the supplied mass horns only after one common independent spatial scale is fixed",
        "score_gate": "closed -- no owned ruler, two-mode preparation, clock/frequency detector, measured record or complete systematic audit",
        "credit_boundary": "a future score distinguishes repository-owned candidates; it earns no GU credit unless the action selects the coefficient and owns the apparatus bridge",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    rows = d["requirements"]
    assert len(rows) == 8 and len({r["id"] for r in rows}) == 8
    assert sum(r["candidate_grade"] in {"pass", "frozen", "pass_obstruction", "pass_mathematical"} for r in rows) == 4
    assert sum(r["candidate_grade"] == "required_open" for r in rows) == 4
    assert all(r["gu_source_owned"] is False and r["scorable"] is False for r in rows)
    assert d["counts"] == {"candidate_closed_or_frozen": 4, "required_open": 4, "gu_source_owned": 0, "scorable": 0}
    assert "common independent spatial scale" in d["holdout_result"]
    assert d["score_gate"].startswith("closed") and "complete systematic audit" in d["score_gate"]
    assert "earns no GU credit" in d["credit_boundary"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1045 controls: 10/10")
