import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0703-cycle1-keating-pullthatupjamie-asset-reacquisition.md"


def _json_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
    assert match, "artifact must contain a fenced JSON summary"
    return json.loads(match.group(1)), text


def test_json_summary_parses_and_identifies_lane():
    data, _ = _json_summary()
    assert data["artifact"] == "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1"
    assert data["run_id"] == "hourly-20260625-0703"
    assert data["cycle"] == 1
    assert data["lane"] == 2
    assert data["artifact_id"] == "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1"


def test_locator_window_present_and_exact():
    data, text = _json_summary()
    assert data["locator_window"] == "01:41:43-01:42:50"
    assert "01:41:43-01:42:50" in text


def test_no_acceptance_without_actual_formula_sheet_frame_and_provenance():
    data, _ = _json_summary()
    assert data["actual_formula_sheet_frame_available"] is False
    assert data["accepted_receipt_count"] == 0
    assert data["accepted_for_routing_count"] == 0
    assert data["accepted_receipts"] == []
    for surface in data["source_surfaces"]:
        assert surface["accepted_for_routing"] is False
    assert any("provenance" in requirement for requirement in data["asset_requirements"])


def test_proof_restart_forbidden():
    data, text = _json_summary()
    assert data["proof_restart_allowed"] is False
    assert "proof_restart_allowed = false" in text


def test_first_obstruction_names_missing_identity_object():
    data, _ = _json_summary()
    obstruction = data["first_obstruction"]
    assert "No actual formula/sheet/frame" in obstruction
    assert "SourceForcedCodomainSelectorForK_IG" in obstruction
    assert data["next_frontier_object"] == "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1"
