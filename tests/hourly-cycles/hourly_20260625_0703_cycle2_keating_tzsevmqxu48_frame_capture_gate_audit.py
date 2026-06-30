#!/usr/bin/env python3
"""Audit FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md"
)

REQUIRED_TOP_LEVEL = {
    "artifact",
    "run_id",
    "cycle",
    "lane",
    "artifact_id",
    "verdict",
    "video_id",
    "capture_attempts",
    "formula_bearing_frame_found",
    "accepted_receipt_count",
    "proof_restart_allowed",
    "first_obstruction",
    "next_frontier_object",
    "companion_audit",
}

REQUIRED_ATTEMPTS = {
    "official_page_embed_caption",
    "youtube_oembed_metadata",
    "youtube_watch_player_response",
    "youtube_storyboard_level_2",
    "youtube_hqdefault_thumbnail",
    "direct_mp4_stream_decode",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class TzSEvmqxu48FrameCaptureGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_json_shape_and_identity(self) -> None:
        self.assertTrue(REQUIRED_TOP_LEVEL.issubset(self.summary))
        self.assertEqual(
            self.summary["artifact"],
            "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(self.summary["video_id"], "TzSEvmqxu48")
        self.assertIn("TzSEvmqxu48", self.text)
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle2_keating_tzsevmqxu48_frame_capture_gate_audit.py",
        )

    def test_capture_attempts_are_present_and_specific(self) -> None:
        attempts = self.summary["capture_attempts"]
        self.assertIsInstance(attempts, list)
        self.assertGreaterEqual(len(attempts), 1)
        by_id = {row["attempt_id"]: row for row in attempts}
        self.assertTrue(REQUIRED_ATTEMPTS.issubset(by_id))
        for row in attempts:
            self.assertIn("source", row)
            self.assertIn("method", row)
            self.assertIn("status", row)
            self.assertIn("formula_bearing_frame_or_asset", row)
            self.assertIn("accepted_receipt", row)

    def test_storyboard_attempt_is_frame_level_but_not_accepted(self) -> None:
        storyboard = {
            row["attempt_id"]: row for row in self.summary["capture_attempts"]
        }["youtube_storyboard_level_2"]
        self.assertIn("69_one_second_storyboard_frames", storyboard["status"])
        self.assertEqual(len(storyboard["sheet_sha256"]), 3)
        self.assertFalse(storyboard["formula_bearing_frame_or_asset"])
        self.assertFalse(storyboard["accepted_receipt"])

    def test_no_accepted_receipt_without_formula_and_identity(self) -> None:
        self.assertFalse(self.summary["formula_bearing_frame_found"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        manuscript = self.summary["manuscript_comparison"]
        self.assertFalse(manuscript["frame_formula_available_for_comparison"])
        self.assertFalse(manuscript["identity_fields_present"])
        self.assertFalse(manuscript["identity_to_SourceForcedCodomainSelectorForK_IG"])
        self.assertIn("8.1", manuscript["equations_checked_if_frame_found"])
        self.assertIn("8.7", manuscript["equations_checked_if_frame_found"])
        self.assertIn("9.2", manuscript["equations_checked_if_frame_found"])
        self.assertIn("9.3", manuscript["equations_checked_if_frame_found"])

    def test_proof_restart_is_blocked_and_obstruction_is_exact(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertIn("HTTP 403", self.summary["first_obstruction"])
        self.assertIn("storyboard", self.summary["first_obstruction"])
        self.assertEqual(
            self.summary["next_frontier_object"],
            "DecodableTzSEvmqxu48ArchiveOrSourceAssetWithFormulaFrameAudit_V1",
        )
        self.assertIn(
            "BLOCKED_FRAME_STREAM_DECODE_STORYBOARD_NEGATIVE_ZERO_ACCEPTED_RECEIPTS",
            self.text,
        )

    def test_target_import_guard_stays_non_sufficient(self) -> None:
        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["target_data_seen"], [])
        self.assertTrue(guard["target_import_clean"])
        self.assertFalse(guard["target_import_clean_sufficient_for_acceptance"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
