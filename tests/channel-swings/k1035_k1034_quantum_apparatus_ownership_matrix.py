#!/usr/bin/env python3
"""K1035: compose the action and apparatus ownership requirements."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1035-k1034-quantum-apparatus-ownership-matrix.json"


def build():
    rows = [
        ("physical_quotient", "K1031", "positive M with exact gauge radical and owned quotient", False),
        ("state_effect_pairing", "K1031-K1033", "normalized positive states and complete local effects", False),
        ("action_generator", "K1034", "radical-preserving M-skew closed flow or fully owned CPTP open flow", False),
        ("preparation_herald", "K1023", "pre-settings physical preparation and herald", False),
        ("fresh_settings", "K1021-K1022", "device-conditional setting freshness or audited deviation bound", False),
        ("local_observables", "K1033", "commuting/tensor-local quotient effect algebras", False),
        ("causal_event_record", "K1026-K1029", "measured two-way spacelike records with predictable compromise audit", False),
        ("detector_systematics", "K1016-K1030", "detector response and complete statistical/systematic budget", False),
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1035-K1034-QUANTUM-APPARATUS-OWNERSHIP-MATRIX",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "reverse_lineage": ["EXT-QM-MASSIVE-MATTER-INTERFERENCE", "EXT-QM-SPACELIKE-BELL-NOSIGNAL"],
        "stage": "candidate_action_requirements",
        "requirements": [{"id": a, "evidence": b, "acceptance": c, "gu_owned": d} for a, b, c, d in rows],
        "source_scope": {
            "SC-ACT-01": "ASSERTS classical first-order action",
            "SC-ACT-02": "ASSERTS stated first-order field equation",
            "SC-ACT-06": "ASSERTS rich moduli/Euclidean ellipticity at source scope; complete proof remains open",
            "SC-META-53": "UNCERTAIN on the indefinite-form/unbounded-spectrum physical resolution",
        },
        "score_status": "forbidden_until_every_required_row_is_owned_and_a_distinct_holdout_is_frozen",
        "current_result": "all eight action/apparatus rows remain unowned by GU; imported conditional mathematics is reusable but earns no prediction or confirmation credit",
        "ledger_effect": "none -- v0.263 rows and distances remain unchanged",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["reverse_lineage"] == ["EXT-QM-MASSIVE-MATTER-INTERFERENCE", "EXT-QM-SPACELIKE-BELL-NOSIGNAL"]
    assert d["stage"] == "candidate_action_requirements"
    rows = d["requirements"]
    assert len(rows) == 8 and len({row["id"] for row in rows}) == 8
    assert all(row["evidence"].startswith("K") for row in rows)
    assert all(row["gu_owned"] is False for row in rows)
    assert d["source_scope"]["SC-ACT-01"].startswith("ASSERTS")
    assert d["source_scope"]["SC-ACT-02"].startswith("ASSERTS")
    assert d["source_scope"]["SC-ACT-06"].startswith("ASSERTS")
    assert d["source_scope"]["SC-META-53"].startswith("UNCERTAIN")
    assert d["score_status"].startswith("forbidden_until_every_required_row_is_owned")
    assert "no prediction or confirmation" in d["current_result"]
    assert d["ledger_effect"].startswith("none")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1035 controls: 12/12")
