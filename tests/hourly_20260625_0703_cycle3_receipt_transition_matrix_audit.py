import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0703-cycle3-receipt-transition-matrix.md"


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(.*?)\s*```", text, re.S)
    assert blocks, "artifact must contain a fenced JSON summary"
    return json.loads(blocks[-1])


def test_transition_matrix_json_contract_and_counts():
    summary = load_summary()
    rows = summary["rows"]

    assert summary["artifact"] == "ReceiptTransitionMatrixAfterHourly20260625_0703_V1"
    assert summary["run_id"] == "hourly-20260625-0703"
    assert summary["cycle"] == 3
    assert summary["lane"] == 1
    assert summary["artifact_id"] == "ReceiptTransitionMatrixAfterHourly20260625_0703_V1"
    assert summary["companion_audit"] == (
        "tests/hourly_20260625_0703_cycle3_receipt_transition_matrix_audit.py"
    )

    assert len(rows) >= 10
    assert len(rows) == 68
    assert len({row["row_id"] for row in rows}) == len(rows)

    accepted_receipts = sum(row["accepted_receipt"] for row in rows)
    accepted_for_routing = sum(row["accepted_for_routing"] for row in rows)
    family_identity = sum(row["family_identity_passed"] for row in rows)
    proof_restart_rows = sum(row["proof_restart_allowed"] for row in rows)
    global_no_go_rows = sum(row["global_no_go"] for row in rows)
    claim_promotion_rows = sum(row["claim_promotion"] for row in rows)

    assert accepted_receipts == summary["accepted_receipt_count"]
    assert accepted_for_routing == summary["accepted_for_routing_count"]
    assert family_identity == summary["family_identity_checks_passed"]
    assert proof_restart_rows == 0
    assert global_no_go_rows == 0
    assert claim_promotion_rows == 0

    assert summary["accepted_receipt_count"] == 0
    assert summary["accepted_for_routing_count"] == 0
    assert summary["family_identity_checks_passed"] == 0
    assert summary["proof_restart_allowed"] is False
    assert summary["global_no_go_promoted"] is False
    assert summary["claim_promotion_allowed"] is False
    assert summary["first_obstruction"]
    assert summary["next_frontier_object"] == "ReceiptTransitionMatrixSourceCompletionQueue_V1"


def test_transition_booleans_are_false_for_every_row():
    summary = load_summary()
    transition_keys = {
        "accepted_receipt",
        "accepted_for_routing",
        "family_identity_passed",
        "proof_restart_allowed",
        "global_no_go",
        "claim_promotion",
    }

    for row in summary["rows"]:
        missing = transition_keys - row.keys()
        assert not missing, f"{row['row_id']} missing {sorted(missing)}"
        assert all(row[key] is False for key in transition_keys), row["row_id"]
        assert row["source_artifact"]
        assert row["row_kind"]
        assert row["family"]
        assert row["positive_status"]
        assert row["first_obstruction"]


def test_proof_restart_requires_an_accepted_receipt():
    summary = load_summary()
    if summary["accepted_receipt_count"] == 0:
        assert summary["proof_restart_allowed"] is False
        assert all(not row["proof_restart_allowed"] for row in summary["rows"])
