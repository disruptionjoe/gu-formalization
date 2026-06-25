#!/usr/bin/env python3
"""Audit the 0803 cycle 2 PTUJ lawful acquisition contract matrix."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md"
)

EXPECTED_SOURCES_READ_FIRST = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md",
    "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
    "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
    "sources/media-index.md",
}

EXPECTED_SOURCE_SURFACES = {
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE",
}

EXPECTED_MISSING_OBJECTS = {
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
    "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
    "KeatingRevealed_ShiabProjectionSheet_V1",
    "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG",
}

EXPECTED_PACKET_FIELDS = {
    "source_asset_branch",
    "source_ids",
    "input_asset_manifest",
    "formula_asset_manifest",
    "formula_or_rule_transcription",
    "visibility_status",
    "identity_to_missing_sheet_or_equivalent",
    "selector_family_review_state",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class PtujLawfulAcquisitionContractMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_decision_state(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "LawfulLocalTzSEvmqxu48AcquisitionContractMatrix_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_CONTRACT_DEFINED_NO_ACCEPTABLE_PATH_PRESENT",
        )
        self.assertEqual(
            self.summary["target_admission_object"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )
        self.assertEqual(self.summary["target_video_id"], "TzSEvmqxu48")
        self.assertFalse(self.summary["repo_has_acceptable_path_today"])
        self.assertFalse(self.summary["source_reachability_check_repeated"])

    def test_sources_and_required_sections(self) -> None:
        self.assertEqual(
            set(self.summary["sources_read_first"]),
            EXPECTED_SOURCES_READ_FIRST,
        )
        self.assertEqual(
            set(self.summary["required_source_surfaces"]),
            EXPECTED_SOURCE_SURFACES,
        )
        for source in EXPECTED_SOURCES_READ_FIRST:
            self.assertIn(source, self.text)

        for heading in [
            "## 1. Verdict.",
            "## 2. Specific GU claim or bridge under test.",
            "## 3. Sources read first.",
            "## 4. Strongest positive construction/contract.",
            "## 5. Field-by-field acquisition matrix.",
            "## 6. First exact obstruction or missing object.",
            "## 7. Impact if closed.",
            "## 8. Falsification/demotion condition.",
            "## 9. Next meaningful source/computation step.",
            "## 10. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)

    def test_contract_branches_and_required_fields(self) -> None:
        branches = {
            branch["branch_id"]: branch for branch in self.summary["contract_branches"]
        }
        self.assertEqual(
            set(branches),
            {
                "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
                "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
            },
        )
        local = branches["LawfulLocalTzSEvmqxu48FrameExtractor_V1"]
        official = branches["OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1"]

        self.assertEqual(local["contract_branch"], "lawful_local_extractor")
        self.assertFalse(local["accepted_today"])
        for field in [
            "lawful_basis",
            "input_locator",
            "toolchain_identity",
            "decode_scope",
            "output_manifest",
            "formula_visibility_evidence",
            "target_import_guard",
        ]:
            self.assertIn(field, local["required_fields"])

        self.assertEqual(official["contract_branch"], "official_source_asset")
        self.assertFalse(official["accepted_today"])
        for field in [
            "custodian_or_source_surface",
            "asset_locator",
            "provenance_chain",
            "asset_manifest",
            "formula_visibility_evidence",
            "identity_basis",
            "target_import_guard",
        ]:
            self.assertIn(field, official["required_fields"])

        self.assertEqual(
            set(self.summary["formula_packet_required_fields"]),
            EXPECTED_PACKET_FIELDS,
        )

    def test_zero_receipts_and_no_proof_restart(self) -> None:
        receipt = self.summary["receipt_state"]
        for count_key in [
            "accepted_source_asset_count",
            "accepted_formula_receipt_count",
            "accepted_frame_packet_count",
            "accepted_receipt_count",
            "accepted_for_routing_count",
        ]:
            self.assertEqual(receipt[count_key], 0, count_key)
        self.assertEqual(receipt["accepted_receipts"], [])
        for bool_key in [
            "metadata_or_caption_receipt_accepted",
            "thumbnail_receipt_accepted",
            "storyboard_receipt_accepted",
            "formula_asset_captured",
            "proof_restart_allowed",
            "claim_promotion_allowed",
        ]:
            self.assertFalse(receipt[bool_key], bool_key)
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_exact_missing_objects_and_obstruction(self) -> None:
        self.assertEqual(set(self.summary["missing_objects"]), EXPECTED_MISSING_OBJECTS)
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        )
        self.assertEqual(obstruction["obstruction_type"], "contract_branches_missing")
        self.assertIn("Neither", obstruction["description"])

    def test_metadata_oembed_captions_are_not_accepted(self) -> None:
        rows = {
            row["object_type"]: row
            for row in self.summary["non_accepted_receipt_types"]
        }
        for object_type in [
            "PTUJ_caption_text",
            "YouTube_oEmbed_JSON",
            "YouTube_watch_page_reachability",
            "YouTube_thumbnail",
            "low_resolution_storyboard_frames",
            "Keating_transcript_window",
            "manuscript_pages_41_to_44",
        ]:
            self.assertIn(object_type, rows)
            self.assertFalse(
                rows[object_type]["accepted_as_formula_receipt"],
                object_type,
            )

        forbidden = self.summary["forbidden_promotions"]
        self.assertFalse(forbidden["caption_or_oembed_selector_receipt_accepted"])
        self.assertFalse(
            forbidden["metadata_converted_to_formula_packet_without_source_asset"]
        )
        self.assertFalse(forbidden["thumbnail_receipt_accepted"])
        self.assertFalse(forbidden["proof_restart"])

    def test_acquisition_matrix_records_only_locator_zero_state_acceptances(self) -> None:
        matrix = {row["field"]: row for row in self.summary["acquisition_matrix"]}
        self.assertTrue(matrix["target_video_id"]["accepted_today"])
        self.assertEqual(matrix["target_video_id"]["acceptance_scope"], "locator_only")
        self.assertTrue(matrix["source_ids"]["accepted_today"])
        self.assertEqual(matrix["source_ids"]["acceptance_scope"], "provenance_map_only")
        self.assertTrue(matrix["accepted_receipt_count"]["accepted_today"])
        self.assertEqual(matrix["accepted_receipt_count"]["current_state"], 0)
        self.assertTrue(matrix["proof_restart_allowed"]["accepted_today"])
        self.assertFalse(matrix["proof_restart_allowed"]["current_state"])

        for field in [
            "lawful_basis",
            "toolchain_identity",
            "direct_source_asset",
            "source_asset_checksums",
            "frame_or_asset_manifest",
            "formula_visibility_evidence",
            "KeatingRevealed_ShiabProjectionSheet_V1",
            "manuscript_identity_to_selector",
        ]:
            self.assertFalse(matrix[field]["accepted_today"], field)


if __name__ == "__main__":
    unittest.main(verbosity=2)
