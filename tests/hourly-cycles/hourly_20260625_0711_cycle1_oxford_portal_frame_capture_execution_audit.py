#!/usr/bin/env python3
"""Audit OxfordPortalFrameCaptureExecution_0711_Cycle1_Lane1_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md"
)

REQUIRED_ANCHORS = {
    "02:33:43": "OxfordPortal_PPT_023343_ShiabOperator",
    "02:35:10": "OxfordPortal_PPT_023510_Swervature",
    "02:36:12": "OxfordPortal_PPT_023612_Displasion",
    "02:38:53": "OxfordPortal_PPT_023853_RSDiracAdjacency",
    "02:40:19": "OxfordPortal_PPT_024019_PullbackToX",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class OxfordPortalFrameCaptureExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "OxfordPortalFrameCaptureExecution_0711_Cycle1_Lane1_V1",
        )
        self.assertEqual(self.summary["artifact_id"], self.summary["artifact"])
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0711_cycle1_oxford_portal_frame_capture_execution_audit.py",
        )
        self.assertEqual(
            self.summary["verdict_code"],
            "CONDITIONAL_VERIFIED_SOURCE_HOSTED_FRAMES_ZERO_ACCEPTED_RECEIPTS",
        )

    def test_all_five_required_anchors_are_present(self) -> None:
        self.assertEqual(set(self.summary["required_timestamps"]), set(REQUIRED_ANCHORS))
        anchors = self.summary["anchors"]
        self.assertEqual(len(anchors), 5)
        by_time = {row["timestamp"]: row for row in anchors}
        self.assertEqual(set(by_time), set(REQUIRED_ANCHORS))
        for timestamp, anchor_id in REQUIRED_ANCHORS.items():
            row = by_time[timestamp]
            self.assertEqual(row["anchor_id"], anchor_id)
            self.assertIn(timestamp, self.text)
            self.assertRegex(row["frame_url"], r"^https://geometricunity\.org/.+\.png$")

    def test_frame_verification_fields_are_real(self) -> None:
        self.assertTrue(self.summary["source_frame_verification_substep_closed"])
        self.assertTrue(self.summary["actual_image_frame_capture_possible"])
        for row in self.summary["anchors"]:
            self.assertEqual(row["http_status"], 200)
            self.assertEqual(row["content_type"], "image/png")
            self.assertGreater(row["bytes"], 0)
            self.assertRegex(
                row["checksum_or_archive_id"],
                r"^sha256:[0-9a-f]{64}$",
            )
            self.assertTrue(row["checksum_matches_0703"])
            self.assertTrue(row["formula_or_rule_transcription"])

    def test_receipt_counts_and_proof_restart_are_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)
        for row in self.summary["anchors"]:
            self.assertFalse(row["required_family_object_emitted"])
            self.assertEqual(row["family_identity_status"], "blocked")
            self.assertFalse(row["accepted_for_routing"])
            self.assertEqual(row["receipt_status"], "candidate_only_not_accepted")

    def test_official_page_and_tooling_state_are_recorded(self) -> None:
        pages = {row["url"]: row for row in self.summary["official_page_checks"]}
        oxford = pages["https://geometricunity.org/2013-oxford-lecture/"]
        self.assertEqual(oxford["status"], 200)
        self.assertTrue(oxford["all_required_png_filenames_present"])
        portal = pages[
            "https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/"
        ]
        self.assertEqual(portal["status"], 200)
        self.assertFalse(portal["all_required_png_filenames_present"])
        tooling = self.summary["local_tooling_checks"]
        self.assertFalse(tooling["yt_dlp_resolved_in_path"])
        self.assertFalse(tooling["ffmpeg_resolved_in_path"])
        self.assertFalse(tooling["video_frame_extraction_used"])
        self.assertEqual(
            tooling["positive_route_used"],
            "official_source_hosted_png_still_verification",
        )

    def test_obstruction_and_next_objects_are_specific(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "FamilyIdentityForVerifiedOxfordPortalFrames_V1",
        )
        self.assertIn("required displayed family object", obstruction["description"])
        self.assertIn("family identity check", obstruction["description"])
        self.assertIn("accepted_visual_formula_receipt", obstruction["blocks"])
        self.assertEqual(
            self.summary["next_object"],
            "VisualFormulaReceiptCandidatePacket_V1",
        )
        self.assertEqual(
            self.summary["next_computation"],
            "BosonicOxfordReplacementToDGU01IdentityTest_V1",
        )

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo/Source Surfaces",
            "## 3. Strongest Positive Acquisition or Construction Attempt",
            "## 4. First Exact Obstruction or Missing Object",
            "## 5. Impact if Closed",
            "## 6. Falsification or Demotion Condition",
            "## 7. Next Meaningful Acquisition/Computation Step",
            "## 8. Machine-readable JSON summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
