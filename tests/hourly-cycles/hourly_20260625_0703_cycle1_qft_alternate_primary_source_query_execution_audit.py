import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0703-cycle1-qft-alternate-primary-source-query-execution.md"


def load_json_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    assert match, "JSON Summary fenced block not found"
    return json.loads(match.group(1))


def test_json_summary_contract_and_invariants():
    data = load_json_summary()

    required_keys = {
        "artifact",
        "run_id",
        "cycle",
        "lane",
        "artifact_id",
        "verdict",
        "inspected_surfaces",
        "accepted_receipt_count",
        "accepted_for_routing_count",
        "proof_restart_allowed",
        "global_demote_allowed",
        "first_obstruction",
        "next_frontier_object",
        "companion_audit",
    }
    assert required_keys <= data.keys()

    assert data["artifact"] == "QFTAlternatePrimarySourceQueryBundle_V1"
    assert data["run_id"] == "hourly-20260625-0703"
    assert data["cycle"] == 1
    assert data["lane"] == 3
    assert data["artifact_id"] == "QFTAlternatePrimarySourceQueryBundle_V1"
    assert data["verdict"] == "conditional"

    surfaces = data["inspected_surfaces"]
    assert isinstance(surfaces, list)
    assert len(surfaces) >= 3

    accepted_rows = [surface for surface in surfaces if surface.get("accepted_receipt")]
    assert data["accepted_receipt_count"] == len(accepted_rows) == 0
    assert data["accepted_for_routing_count"] == 0

    # No accepted receipt is allowed without the finite projector/source-mode object.
    for surface in surfaces:
        if surface.get("accepted_receipt"):
            joined = json.dumps(surface)
            assert "P_fin" in joined or "source-mode" in joined or "source mode" in joined

    assert data["proof_restart_allowed"] is False
    assert data["global_demote_allowed"] is False
    assert "F_phys" in data["first_obstruction"]
    assert "K_b" in data["first_obstruction"]
    assert "P_fin" in data["first_obstruction"]
    assert data["next_frontier_object"] == "CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1"
    assert data["companion_audit"] == "tests/hourly_20260625_0703_cycle1_qft_alternate_primary_source_query_execution_audit.py"


def test_artifact_declares_no_global_demotion_without_complete_coverage():
    text = ARTIFACT.read_text(encoding="utf-8")
    assert "No global QFT demotion is promoted" in text
    assert "complete-coverage condition" in text
    assert "global_demote_allowed: false" in text
    assert "proof_restart_allowed: false" in text
