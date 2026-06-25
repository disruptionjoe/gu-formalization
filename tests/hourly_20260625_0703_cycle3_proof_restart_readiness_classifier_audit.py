import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0703-cycle3-proof-restart-readiness-classifier.md"
REQUIRED_FAMILIES = {
    "IG",
    "DGU_VZ",
    "RS",
    "QFT",
    "Oxford_visual",
    "Keating_visual",
}


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    assert blocks, "artifact must contain a fenced JSON summary"
    return json.loads(blocks[-1])


def test_required_families_present():
    summary = load_summary()
    families = summary["families"]
    assert {row["family"] for row in families} == REQUIRED_FAMILIES
    assert len(families) == 6


def test_restart_false_without_receipt_and_identity():
    summary = load_summary()
    for row in summary["families"]:
        if not (row["accepted_receipt"] and row["family_identity_check_passed"]):
            assert row["proof_restart_ready"] is False, row["family"]


def test_counts_match_family_rows():
    summary = load_summary()
    families = summary["families"]
    assert summary["accepted_receipt_count"] == sum(1 for row in families if row["accepted_receipt"])
    assert summary["family_identity_checks_passed"] == sum(
        1 for row in families if row["family_identity_check_passed"]
    )
    assert summary["proof_restart_ready_count"] == sum(
        1 for row in families if row["proof_restart_ready"]
    )
    assert summary["any_proof_restart_allowed"] is any(
        row["proof_restart_ready"] for row in families
    )


def test_global_gate_remains_closed():
    summary = load_summary()
    assert summary["artifact"] == "ProofRestartReadinessClassifierAfterHourly20260625_0703_V1"
    assert summary["run_id"] == "hourly-20260625-0703"
    assert summary["cycle"] == 3
    assert summary["lane"] == 2
    assert summary["proof_restart_ready_count"] == 0
    assert summary["accepted_receipt_count"] == 0
    assert summary["family_identity_checks_passed"] == 0
    assert summary["any_proof_restart_allowed"] is False
