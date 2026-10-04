#!/usr/bin/env python3
"""K1040: reconcile candidate, GU-source and scorable apparatus ownership."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1040-k1039-action-apparatus-ownership-matrix.json"


def build():
    rows = [
        ("physical_quotient", "K1036", "pass", False, False),
        ("state_effect_pairing", "K1038", "pass", False, False),
        ("action_generator", "K1037", "pass", False, False),
        ("preparation_herald", "K1023", "open", False, False),
        ("fresh_settings", "K1021-K1022", "open", False, False),
        ("local_observables", "K1038", "pass_algebraic", False, False),
        ("causal_event_record", "K1026-K1029", "open", False, False),
        ("detector_systematics", "K1016-K1030", "open", False, False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1040-K1039-ACTION-APPARATUS-OWNERSHIP-MATRIX",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "requirements": [
            {"id": i, "evidence": e, "candidate_grade": c, "gu_source_owned": g, "scorable": s}
            for i, e, c, g, s in rows
        ],
        "counts": {"candidate_pass_or_algebraic": 4, "gu_source_owned": 0, "scorable": 0, "fully_open_candidate_rows": 4},
        "candidate_result": "K77 plus K1036--K1039 closes quotient, state/effect, closed-generator and algebraic-locality rows for one repository-owned candidate class",
        "selection_result": "the same rows pass for mass squared 1 and 4, so the packet does not select a unique action",
        "score_gate": "closed -- preparation/herald, fresh settings, spacelike records, detector/systematics, source ownership and a distinct frozen holdout remain absent",
        "source_scope": {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"},
        "ledger_effect": "none -- LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    rows = d["requirements"]
    assert len(rows) == 8 and len({r["id"] for r in rows}) == 8
    assert all(r["evidence"].startswith("K") for r in rows)
    assert sum(r["candidate_grade"].startswith("pass") for r in rows) == 4
    assert all(r["gu_source_owned"] is False for r in rows)
    assert all(r["scorable"] is False for r in rows)
    assert d["counts"] == {"candidate_pass_or_algebraic": 4, "gu_source_owned": 0, "scorable": 0, "fully_open_candidate_rows": 4}
    assert "repository-owned candidate class" in d["candidate_result"]
    assert "does not select" in d["selection_result"]
    assert d["score_gate"].startswith("closed") and "holdout" in d["score_gate"]
    assert d["source_scope"] == {"SC-ACT-01": "ASSERTS", "SC-ACT-02": "ASSERTS", "SC-ACT-06": "ASSERTS", "SC-META-53": "UNCERTAIN"}
    assert d["ledger_effect"].startswith("none") and d["ledger_effect"].endswith("NEEDS")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1040 controls: 13/13")
