"""Audit RS_UCSD_VISUAL_LOCATOR_OR_UNAVAILABILITY_PACKET."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle2-rs-ucsd-visual-locator-unavailability-packet.md"
)
EXPECTED_ARTIFACT_ID = "RS_UCSD_VISUAL_LOCATOR_OR_UNAVAILABILITY_PACKET"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1503-cycle2-rs-ucsd-visual-locator-unavailability-packet.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1503_cycle2_rs_ucsd_visual_locator_unavailability_packet_audit.py"
)
EXPECTED_VERDICT = (
    "BLOCKED_STABLE_OFFICIAL_VIDEO_LOCATOR_PRESENT_VISUAL_PACKET_ABSENT_UNAVAILABILITY_NOT_DOCUMENTED"
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


class RSUCSDVisualLocatorUnavailabilityPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT_PATH.read_text(encoding="utf-8")
        cls.summary = load_json_summary(cls.text)

    def test_artifact_exists_and_frontmatter_identity(self) -> None:
        self.assertTrue(ARTIFACT_PATH.exists())
        self.assertTrue(self.text.startswith("---\n"))
        self.assertIn(f'artifact_id: "{EXPECTED_ARTIFACT_ID}"', self.text)
        self.assertIn(f'verdict: "{EXPECTED_VERDICT}"', self.text)
        self.assertIn(f'owned_path: "{EXPECTED_OWNED_PATH}"', self.text)
        self.assertIn(f'companion_audit: "{EXPECTED_AUDIT}"', self.text)

    def test_required_sections_present(self) -> None:
        for section in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo Sources And Lookup",
            "## 3. The Strongest Positive Source Locator Result",
            "## 4. The First Exact Obstruction Or Missing Source Object",
            "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
            "## 6. What This Means For Typed RS Operator, Quotient, And Generation Restart",
            "## 7. Next Meaningful Source Computation Step",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(section, self.text)

    def test_json_identity_fields(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(self.summary["target_object"], "UCSDTypedRSMinusOneOperator_V1")

    def test_required_explicit_summary_fields(self) -> None:
        required_fields = [
            "transcript_window_present",
            "visual_packet_present",
            "stable_visual_locator_present",
            "source_safe_locator_count",
            "documented_unavailability_packet_present",
            "global_visual_route_failed",
            "typed_operator_can_start",
            "accepted_rs_receipt_count",
            "proof_restart_allowed",
            "generation_restart_allowed",
            "target_import_used",
        ]
        for field in required_fields:
            self.assertIn(field, self.summary)

    def test_decision_state_distinguishes_locator_from_packet(self) -> None:
        self.assertIs(self.summary["transcript_window_present"], True)
        self.assertEqual(self.summary["transcript_window"], "[00:32:07]-[00:37:41]")
        self.assertIs(self.summary["visual_packet_present"], False)
        self.assertEqual(self.summary["visual_packet_artifacts"], [])
        self.assertIs(self.summary["stable_visual_locator_present"], True)
        self.assertEqual(self.summary["source_safe_locator_count"], 1)
        self.assertIs(self.summary["documented_unavailability_packet_present"], False)
        self.assertIs(self.summary["global_visual_route_failed"], False)
        self.assertIs(self.summary["target_import_used"], False)

        self.assertIs(self.summary["actual_visual_packet_present"], False)
        self.assertIs(
            self.summary["immutable_official_visual_locator_present_but_not_captured"],
            True,
        )
        self.assertIs(self.summary["source_safe_locator_absent"], False)
        self.assertIs(self.summary["global_visual_route_failure_justified"], False)

    def test_strongest_positive_locator_is_specific_and_source_safe(self) -> None:
        locator = self.summary["strongest_positive_source_locator"]
        self.assertEqual(locator["source_id"], "GU-MEDIA-KEATING-QG-FBOZSSLXFVI")
        self.assertEqual(locator["video_id"], "fBozSSLxFvI")
        self.assertEqual(
            locator["official_watch_url"],
            "https://www.youtube.com/watch?v=fBozSSLxFvI",
        )
        self.assertEqual(
            locator["timestamp_start_locator"],
            "https://www.youtube.com/watch?v=fBozSSLxFvI&t=1927s",
        )
        self.assertEqual(locator["timestamp_start_seconds"], 1927)
        self.assertEqual(locator["timestamp_end_seconds"], 2261)
        self.assertEqual(locator["target_time_window"], "[00:32:07]-[00:37:41]")
        self.assertEqual(
            locator["title_from_oembed"],
            "The Problem With Quantum Gravity (ft. Eric Weinstein)",
        )
        self.assertEqual(locator["author_name_from_oembed"], "Dr Brian Keating")
        self.assertFalse(locator["media_downloaded"])
        self.assertFalse(locator["frames_captured"])
        self.assertEqual(locator["receipt_status"], "locator_only_not_visual_packet")

    def test_lookup_did_not_create_visual_receipt(self) -> None:
        lookup = self.summary["lookup_summary"]
        self.assertTrue(lookup["web_search_performed"])
        self.assertTrue(lookup["youtube_oembed_performed"])
        self.assertTrue(lookup["repo_local_media_filename_search_performed"])
        self.assertFalse(lookup["media_download_performed"])
        self.assertFalse(lookup["frame_capture_performed"])
        self.assertFalse(lookup["binary_artifact_created"])

    def test_typed_operator_and_restart_remain_blocked(self) -> None:
        self.assertFalse(self.summary["typed_operator_can_start"])
        self.assertEqual(self.summary["accepted_rs_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["generation_restart_allowed"])

        typed = self.summary["typed_operator_status"]
        self.assertEqual(typed["status"], "blocked_before_typed_operator")
        self.assertFalse(typed["ucsd_typed_operator_exists"])
        self.assertFalse(typed["accepted_as_typed_operator"])
        self.assertFalse(typed["accepted_as_rs_minus_one_receipt"])
        self.assertFalse(typed["pure_rs_domain_present"])
        self.assertFalse(typed["pure_rs_codomain_present"])
        self.assertFalse(typed["minus_one_slot_present"])
        self.assertFalse(typed["operator_formula_present"])
        self.assertFalse(typed["rs_projection_or_quotient_present"])
        self.assertFalse(typed["family_identity_runnable"])
        self.assertFalse(typed["can_proceed_to_UCSDTypedRSMinusOneOperator_V1"])

    def test_route_decision_rejects_global_visual_failure(self) -> None:
        route = self.summary["route_decision"]
        self.assertEqual(route["transcript_branch_status"], "demoted_to_aggregate_motivation_only")
        self.assertEqual(route["visual_route_status"], "locator_present_capture_absent")
        self.assertFalse(route["visual_route_demoted_aggregate_only"])
        self.assertFalse(route["visual_route_failed_globally"])
        self.assertFalse(route["source_safe_locator_absent"])
        self.assertFalse(route["documented_unavailability_sufficient"])

    def test_required_frame_windows_are_exact_contract(self) -> None:
        expected = [
            ("ucsd_rs_context_y14", "00:32:07", "00:32:46"),
            ("ucsd_rs_generation_pullback", "00:32:46", "00:34:27"),
            ("ucsd_rs_complex_middle_map", "00:34:27", "00:35:30"),
            ("ucsd_rs_coupled_derivative", "00:35:30", "00:36:13"),
            ("ucsd_rs_rolled_symbol", "00:36:13", "00:37:41"),
        ]
        actual = [
            (row["id"], row["start"], row["end"])
            for row in self.summary["required_frame_windows"]
        ]
        self.assertEqual(actual, expected)

    def test_next_object_names_capture_or_unavailability_packet(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["preferred_id"], "UCSDFrameSequenceForRolledOperatorWindow_V1")
        self.assertEqual(
            next_object["fallback_id_if_capture_blocked"],
            "UCSDVisualUnavailabilityPacketForRolledOperatorWindow_V1",
        )
        self.assertIn("fBozSSLxFvI", next_object["source_locator_to_test"])
        self.assertEqual(next_object["required_window"], "[00:32:07]-[00:37:41]")


if __name__ == "__main__":
    unittest.main()
