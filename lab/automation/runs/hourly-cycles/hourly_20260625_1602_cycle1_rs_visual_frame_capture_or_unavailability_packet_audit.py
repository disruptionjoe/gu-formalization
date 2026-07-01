"""Audit RSVisualFrameCaptureOrUnavailabilityPacket_1602_C1_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle1-rs-visual-frame-capture-or-unavailability-packet.md"
)
EXPECTED_ARTIFACT_ID = "RSVisualFrameCaptureOrUnavailabilityPacket_1602_C1_L4_V1"
EXPECTED_RUN_ID = "hourly-20260625-1602"
EXPECTED_VERDICT_CLASS = "blocked"


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class RSVisualFrameCaptureOrUnavailabilityPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertTrue(ARTIFACT_PATH.exists())
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["verdict_class"], EXPECTED_VERDICT_CLASS)
        self.assertIn("NO_FRAMES_OCR_OR_TYPED_RS_OPERATOR", self.summary["verdict"])

    def test_required_sections_present(self) -> None:
        for section in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo Sources",
            "## 3. The Strongest Positive Result",
            "## 4. The First Exact Obstruction Or Missing Proof/Source Object",
            "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
            "## 6. What This Means For The RS/GU Claim",
            "## 7. Next Meaningful Proof Or Computation Step",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(section, self.text)

    def test_required_assignment_fields(self) -> None:
        required = [
            "artifact",
            "run_id",
            "accepted_receipt_count",
            "proof_restart_allowed",
            "target_import_used",
            "visual_surfaces_checked",
            "frames_or_ocr_present",
            "unavailability_packet_present",
            "first_obstruction",
            "next_object",
            "promotion_firewall",
        ]
        for field in required:
            self.assertIn(field, self.summary)

    def test_no_receipt_or_restart_without_frames(self) -> None:
        self.assertFalse(self.summary["frames_or_ocr_present"])
        self.assertFalse(self.summary["visual_frame_packet_admitted"])
        self.assertFalse(self.summary["ocr_crop_sequence_admitted"])
        self.assertTrue(self.summary["unavailability_packet_present"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])

    def test_transcript_locator_not_operator_firewall(self) -> None:
        self.assertTrue(self.summary["transcript_locator_not_operator"])
        firewall = self.summary["promotion_firewall"]
        self.assertFalse(firewall["transcript_as_typed_operator"])
        self.assertFalse(firewall["locator_as_visual_packet"])
        self.assertFalse(firewall["repo_local_unavailability_as_global_failure"])
        self.assertFalse(firewall["generation_count_restart"])
        self.assertTrue(firewall["target_import_blocked"])

    def test_visual_surfaces_checked_include_prior_blockers_and_inventory(self) -> None:
        checked = self.summary["visual_surfaces_checked"]
        self.assertIn("literature/weinstein-ucsd-2025-04-transcript.md", checked)
        self.assertIn("sources/media-index.md", checked)
        self.assertIn(
            "explorations/hourly-20260625-1503-cycle2-rs-ucsd-visual-locator-unavailability-packet.md",
            checked,
        )
        self.assertTrue(any("repo_filename_inventory" in item for item in checked))
        self.assertTrue(any("excluded_as_non_ucsd_manuscript_pages" in item for item in checked))

    def test_first_obstruction_and_next_object_are_explicit(self) -> None:
        obstruction = self.summary["first_obstruction"]
        next_object = self.summary["next_object"]
        self.assertIn("UCSDFrameSequenceForRolledOperatorWindow_V1", obstruction)
        self.assertIn("[00:32:07]-[00:37:41]", obstruction)
        self.assertIn("checksummed frames", obstruction)
        self.assertIn("UCSDFrameSequenceForRolledOperatorWindow_V1", next_object)
        self.assertIn("UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1", next_object)
        self.assertIn("fBozSSLxFvI", next_object)

    def test_typed_operator_status_remains_blocked(self) -> None:
        status = self.summary["typed_operator_status"]
        self.assertEqual(status["status"], "blocked_before_typed_operator")
        self.assertFalse(status["ucsd_typed_operator_exists"])
        self.assertFalse(status["accepted_as_typed_operator"])
        self.assertFalse(status["accepted_as_rs_minus_one_receipt"])
        self.assertFalse(status["pure_rs_domain_present"])
        self.assertFalse(status["pure_rs_codomain_present"])
        self.assertFalse(status["minus_one_slot_present"])
        self.assertFalse(status["operator_formula_present"])
        self.assertFalse(status["rs_projection_or_quotient_present"])
        self.assertFalse(status["family_identity_runnable"])


if __name__ == "__main__":
    unittest.main()
