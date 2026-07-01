import json
import re
from pathlib import Path


ARTIFACT = (
    Path(__file__).resolve().parents[1]
    / "explorations"
    / "hourly-20260625-0703-cycle2-qft-complete-transcript-frame-acquisition-gate.md"
)


def load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
    assert match, "artifact must contain a fenced JSON summary"
    return json.loads(match.group(1))


def test_json_summary_core_invariants():
    summary = load_summary()

    assert summary["artifact"] == "CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1"
    assert summary["run_id"] == "hourly-20260625-0703"
    assert summary["cycle"] == 2
    assert summary["lane"] == 3
    assert summary["proof_restart_allowed"] is False
    assert summary["pfinb_payload_found"] is False
    assert summary["accepted_receipt_count"] == 0


def test_surface_coverage_blocks_global_demotion():
    summary = load_summary()
    surfaces = summary["surfaces"]

    assert len(surfaces) >= 4
    assert any(surface["coverage_complete"] is False for surface in surfaces)
    assert summary["global_demote_allowed"] is False

    all_complete = all(surface["coverage_complete"] is True for surface in surfaces)
    if not all_complete:
        assert summary["global_demote_allowed"] is False


def test_no_accepted_receipt_without_pfinb_payload():
    summary = load_summary()
    for surface in summary["surfaces"]:
        if surface["accepted_receipt"]:
            assert surface["pfinb_payload_found"] is True

    assert not any(surface["accepted_receipt"] for surface in summary["surfaces"])


def test_required_declared_surfaces_are_tracked():
    summary = load_summary()
    labels = " ".join(surface["surface_label"] for surface in summary["surfaces"])

    assert "TOE/Jaimungal" in labels
    assert "Keating DESI" in labels
    assert "Keating Revealed" in labels
    assert "Oxford/Portal" in labels
