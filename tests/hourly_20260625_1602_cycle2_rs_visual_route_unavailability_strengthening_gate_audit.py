"""Audit RSVisualRouteUnavailabilityStrengtheningGate_1602_C2_L4_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle2-rs-visual-route-unavailability-strengthening-gate.md"
)
EXPECTED_ARTIFACT_ID = "RSVisualRouteUnavailabilityStrengtheningGate_1602_C2_L4_V1"
EXPECTED_RUN_ID = "hourly-20260625-1602"


def load_json_summary(text: str) -> dict:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("Machine-readable JSON summary block not found")
    return json.loads(match.group(1))


class RSVisualRouteUnavailabilityStrengtheningGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_identity_and_required_sections(self) -> None:
        self.assertTrue(ARTIFACT_PATH.exists())
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        for section in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo Sources",
            "## 3. Strongest Positive Current Candidate",
            "## 4. Required Fields For Visual Frame Packet And Documented Unavailability Packet",
            "## 5. Candidate Decision Matrix",
            "## 6. First Exact Obstruction",
            "## 7. Impact On Typed RS Operator, Generation/Index Restart, And GU Claim",
            "## 8. Next Meaningful Source/Tool Computation",
            "## 9. Machine-Readable JSON Summary",
        ]:
            self.assertIn(section, self.text)

    def test_no_accepted_rs_receipt_or_visual_packet(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["visual_packet_present"])
        self.assertFalse(self.summary["documented_unavailability_packet_present"])
        self.assertTrue(self.summary["repo_local_absence_documented"])

    def test_global_route_and_restart_are_not_failed_or_allowed(self) -> None:
        self.assertFalse(self.summary["global_visual_route_failed"])
        self.assertTrue(self.summary["transcript_locator_not_operator"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["generation_restart_allowed"])
        self.assertFalse(self.summary["index_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])

    def test_repo_local_absence_not_promoted_to_documented_unavailability(self) -> None:
        candidate = self.summary["current_candidate"]
        self.assertEqual(candidate["accepted_as"], "weaker_repo_local_absence_only")
        self.assertFalse(
            candidate[
                "accepted_as_UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1"
            ]
        )
        missing = self.summary["missing_fields"]["documented_unavailability_packet"]
        for field in [
            "official_video_capture_attempted",
            "official_video_capture_outcome",
            "official_slide_deck_locator_tested",
            "speaker_slide_deck_locator_tested",
            "archive_locator_tested",
            "tool_or_access_failure_details",
            "retry_or_falsification_condition",
            "scope_statement",
            "why_no_source_safe_visual_capture_is_currently_available",
        ]:
            self.assertIn(field, missing)

    def test_required_field_matrix_is_explicit(self) -> None:
        required = self.summary["required_fields"]
        self.assertIn("visual_frame_packet", required)
        self.assertIn("documented_unavailability_packet", required)
        for field in [
            "sha256_full_frame",
            "ocr_text_raw",
            "visible_operator_name",
            "visible_domain",
            "visible_codomain",
            "visible_rs_projection_or_quotient",
        ]:
            self.assertIn(field, required["visual_frame_packet"])
        for field in [
            "official_video_locator_tested",
            "official_video_capture_attempted",
            "official_video_capture_outcome",
            "archive_locator_tested",
            "tool_or_access_failure_details",
        ]:
            self.assertIn(field, required["documented_unavailability_packet"])

    def test_decision_matrix_blocks_premature_promotion(self) -> None:
        rows = {row["candidate"]: row for row in self.summary["decision_matrix"]}
        for candidate in [
            "transcript_window_only",
            "transcript_plus_stable_locator",
            "repo_local_absence",
            "documented_visual_unavailability",
            "visual_frame_ocr_packet",
        ]:
            self.assertIn(candidate, rows)
            self.assertFalse(rows[candidate]["accepted_rs_receipt"])
            self.assertFalse(rows[candidate]["proof_restart_allowed"])
        self.assertFalse(rows["repo_local_absence"]["global_visual_route_failed"])
        self.assertFalse(rows["documented_visual_unavailability"]["present"])

    def test_next_object_and_first_obstruction_are_explicit(self) -> None:
        obstruction = self.summary["first_obstruction"]
        next_object = self.summary["next_object"]
        self.assertIn("Cycle 1 documents repo-local absence", obstruction)
        self.assertIn(
            "UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1",
            obstruction,
        )
        self.assertIn("RSVisualRouteSourceSafeCaptureOrDocumentedUnavailabilityPass", next_object)
        self.assertIn("UCSDFrameSequenceForRolledOperatorWindow_V1", next_object)
        self.assertIn("UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1", next_object)
        self.assertIn("fBozSSLxFvI", next_object)


if __name__ == "__main__":
    unittest.main()
