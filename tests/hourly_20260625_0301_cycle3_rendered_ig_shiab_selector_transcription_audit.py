import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "explorations" / "hourly-20260625-0301-cycle3-rendered-ig-shiab-selector-transcription.md"


def _load_summary():
    text = ARTIFACT.read_text(encoding="utf-8")
    matches = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    assert matches, "artifact must contain a fenced machine-readable JSON summary"
    return json.loads(matches[-1]), text


def test_required_pages_and_equations_are_covered():
    summary, text = _load_summary()
    assert summary["artifact"] == "RenderedCriticalDisplayTranscriptionPacket_IG_V1"
    assert summary["required_pages"] == [42, 43, 44, 57, 66]
    assert summary["covered_pages"] == [42, 43, 44, 57, 66]

    label_map = {row["page"]: set(row["labels"]) for row in summary["critical_equations"]}
    assert {"8.3", "8.4", "8.5", "8.6", "8.7"} <= label_map[42]
    assert {"9.1", "9.2", "9.3"} <= label_map[43]
    assert {"9.4", "9.5", "9.6"} <= label_map[44]
    assert {"12.4", "12.5", "12.6", "12.7"} <= label_map[57]
    assert {"12.24", "12.25", "12.26", "12.27"} <= label_map[66]

    for page in ["PDF page 42", "PDF page 43", "PDF page 44", "PDF page 57", "PDF page 66"]:
        assert page in text


def test_transcription_method_is_bounded_and_rendered():
    summary, _ = _load_summary()
    method = summary["transcription_method"]
    assert method["text_extraction"] == "PyMuPDF page.get_text('text')"
    assert method["rendering"] == "PyMuPDF get_pixmap at 2x scale"
    assert method["manual_visual_inspection_performed"] is True
    assert method["rendered_pages_inspected"] == [42, 43, 44, 57, 66]
    assert method["rendered_images_written_inside_repo"] is False
    assert method["identity_grade_exact_tex"] is False
    assert "normalized plain-text" in method["boundedness_note"]


def test_selector_rival_and_identity_statuses_remain_quarantined():
    summary, _ = _load_summary()
    packet = summary["candidate_packet"]
    assert packet["candidate_is_source_emitted"] is True
    assert packet["selector_is_source_forced"] is False
    assert packet["selected_domain"]["value"] == "Omega^2(Y^(7,7), ad)"
    assert packet["selected_codomain_or_target"]["value"] == "Omega^(d-1)(Y^(7,7), ad)"
    assert packet["source_forced_selector_rule"]["present"] is False
    assert packet["source_forced_selector_rule"]["status"] == "missing"
    assert packet["representation_bianchi_selection_evidence"]["present_as_intent"] is True
    assert packet["representation_bianchi_selection_evidence"]["present_as_executable_rule"] is False
    assert packet["rival_eliminators"]["status"] == "missing"
    assert packet["rival_eliminators"]["source_eliminated_rivals"] == []
    assert len(packet["rival_eliminators"]["rival_classes_still_live"]) >= 5
    assert packet["family_identity_to_SourceForcedCodomainSelectorForK_IG"]["passed"] is False


def test_receipts_target_import_flags_and_restart_gate_are_closed():
    summary, _ = _load_summary()
    assert summary["accepted_receipts"] == []
    assert summary["accepted_receipt_count"] == 0
    assert summary["decision"]["candidate_status"] == "rendered_transcribed_quarantined_candidate"
    assert summary["decision"]["selector_identity_status"] == "scoped_missing"
    assert summary["decision"]["accepted_for_routing"] is False
    assert summary["decision"]["proof_restart_allowed"] is False
    assert summary["decision"]["claim_promotion_allowed"] is False

    target_screen = summary["target_import_screen"]
    assert target_screen["target_data_seen"] == []
    assert target_screen["target_import_detected"] is False
    assert target_screen["target_import_clean"] is True
    for key in [
        "DESI_or_dark_energy_used",
        "FLRW_coefficients_used",
        "VZ_success_used",
        "rank_or_generation_counts_used",
        "QFT_targets_used",
    ]:
        assert target_screen[key] is False

    restart = summary["proof_restart_gate"]
    assert restart["source_intake_acceptance_passed"] is False
    assert restart["family_identity_passed"] is False
    assert restart["proof_restart_allowed"] is False
    assert "accepted_for_routing receipt" in restart["restart_blocker"]


def test_obstruction_and_next_object_are_explicit():
    summary, _ = _load_summary()
    obstruction = summary["first_exact_obstruction"]
    assert obstruction["id"] == "RenderedRepresentationBianchiSelectorAndRivalEliminatorForShiab_V1"
    assert obstruction["status"] == "missing"
    assert obstruction["blocks_acceptance_for"] == "SourceForcedCodomainSelectorForK_IG"

    next_object = summary["constructive_next_object"]
    assert next_object["id"] == "ShiabRepresentationBianchiRivalEliminatorTable_IG_V1"
    assert {
        "candidate_family",
        "representation_selector",
        "Bianchi_criterion",
        "rival_eliminators",
        "family_identity_to_SourceForcedCodomainSelectorForK_IG",
        "target_import_screen",
    } <= set(next_object["required_fields"])

    promotions = summary["no_claim_promotions"]
    assert all(value is False for value in promotions.values())
