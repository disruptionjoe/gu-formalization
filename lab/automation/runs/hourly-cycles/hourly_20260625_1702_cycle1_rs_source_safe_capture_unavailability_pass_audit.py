"""Audit RSSourceSafeCaptureUnavailabilityPass_1702_C1_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1702-cycle1-rs-source-safe-capture-unavailability-pass.md"
)
EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_ARTIFACT_ID = "RSSourceSafeCaptureUnavailabilityPass_1702_C1_L4_V1"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle1-rs-source-safe-capture-unavailability-pass.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle1_rs_source_safe_capture_unavailability_pass_audit.py"
)


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class RSSourceSafeCaptureUnavailabilityPassAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_identity_and_paths(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict"], "blocked")

    def test_capture_and_unavailability_branch_rows(self) -> None:
        rows = {row["branch"]: row for row in self.summary["branch_rows"]}
        self.assertEqual(
            rows["capture"]["candidate"], "UCSDFrameSequenceForRolledOperatorWindow_V1"
        )
        self.assertEqual(
            rows["unavailability"]["candidate"],
            "UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1",
        )
        self.assertFalse(rows["capture"]["present"])
        self.assertFalse(rows["unavailability"]["present"])
        self.assertFalse(rows["capture"]["accepted_rs_receipt"])
        self.assertFalse(rows["unavailability"]["accepted_rs_receipt"])

    def test_frame_ocr_checksum_booleans(self) -> None:
        capture = self.summary["capture_branch"]
        row = {row["branch"]: row for row in self.summary["branch_rows"]}["capture"]
        self.assertFalse(capture["frame_artifacts_present"])
        self.assertFalse(capture["crop_artifacts_present"])
        self.assertFalse(capture["ocr_artifacts_present"])
        self.assertFalse(capture["checksum_artifacts_present"])
        self.assertFalse(capture["visible_operator_fields_present"])
        self.assertFalse(row["frame"])
        self.assertFalse(row["ocr"])
        self.assertFalse(row["checksum"])

    def test_receipts_restart_and_target_import(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["generation_restart_allowed"])
        self.assertFalse(self.summary["index_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertFalse(self.summary["target_import"]["used"])

    def test_unavailability_not_overclaimed(self) -> None:
        unavailability = self.summary["unavailability_branch"]
        self.assertTrue(unavailability["official_video_locator_tested"])
        self.assertTrue(unavailability["official_video_reachable"])
        self.assertTrue(unavailability["oembed_metadata_reachable"])
        self.assertTrue(unavailability["tool_access_failures_recorded"])
        self.assertFalse(unavailability["slide_archive_inventory_complete"])
        self.assertFalse(unavailability["constructable_this_pass"])

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_obstruction"]
        next_object = self.summary["next_object"]
        self.assertIn("No source-safe visual source object exists", obstruction)
        self.assertIn("yt-dlp, ffmpeg, and tesseract", obstruction)
        self.assertIn("official video locator is reachable", obstruction)
        self.assertIn("UCSDSourceSafeCaptureExecutionLogForRolledOperatorWindow_V1", next_object)
        self.assertIn("UCSDFrameSequenceForRolledOperatorWindow_V1", next_object)
        self.assertIn("UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1", next_object)

    def test_promotion_firewall(self) -> None:
        firewall = self.summary["promotion_firewall"]
        self.assertEqual(firewall["transcript_or_locator_to_typed_rs_operator"], "forbidden")
        self.assertEqual(firewall["unavailability_packet_to_positive_rs_claim"], "forbidden")
        self.assertEqual(
            firewall["frame_packet_to_typed_rs_operator"],
            "requires_separate_visible_field_and_pure_RS_typing_audit",
        )
        self.assertFalse(firewall["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main()
