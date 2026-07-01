#!/usr/bin/env python3
"""Audit OxfordPortalPowerPointFormulaFrameReacquisition_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md"
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
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary")
    return json.loads(match.group(1))


class OxfordPortalFrameReacquisitionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "OxfordPortalPowerPointFormulaFrameReacquisition_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["artifact_id"], self.summary["artifact"])
        self.assertEqual(self.summary["verdict"], "conditional")
        self.assertEqual(
            self.summary["verdict_code"],
            "CONDITIONAL_EXECUTED_SOURCE_HOSTED_FRAME_PACKET_ZERO_ACCEPTED_ROUTING_RECEIPTS",
        )

    def test_owned_paths_are_correct(self) -> None:
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle1_oxford_portal_frame_reacquisition_audit.py",
        )

    def test_all_five_anchors_present_with_checksums(self) -> None:
        anchors = self.summary["anchors"]
        self.assertEqual(len(anchors), 5)
        by_time = {row["timestamp"]: row for row in anchors}
        self.assertEqual(set(by_time), set(REQUIRED_ANCHORS))
        for timestamp, anchor_id in REQUIRED_ANCHORS.items():
            row = by_time[timestamp]
            self.assertEqual(row["anchor_id"], anchor_id)
            self.assertIn(timestamp, self.text)
            self.assertRegex(row["frame_url"], r"^https://geometricunity\.org/.+\.png$")
            self.assertRegex(
                row["checksum_or_archive_id"],
                r"^sha256:[0-9a-f]{64}$",
            )
            self.assertTrue(row["transcription"])

    def test_receipt_counts_and_restart_are_consistent(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)
        for row in self.summary["anchors"]:
            self.assertFalse(row["accepted_for_routing"])
            self.assertFalse(row["required_family_object_emitted"])

    def test_no_official_frame_requirements_are_overclaimed(self) -> None:
        self.assertTrue(self.summary["source_hosted_checksums_recorded"])
        self.assertFalse(self.summary["repo_local_frame_files_added"])
        self.assertIn("did not add repo-local image", self.text)
        self.assertIn("official hosted URLs", self.text)
        self.assertIn("live-computed SHA-256", self.text)

    def test_candidate_rows_open_but_not_routing(self) -> None:
        self.assertTrue(self.summary["candidate_rows_opened"])
        self.assertEqual(
            self.summary["candidate_packet_id"],
            "VisualFormulaReceiptCandidatePacket_V1",
        )
        self.assertIn("enough to open `VisualFormulaReceiptCandidatePacket_V1`", self.text)
        self.assertIn("not enough to accept any row for routing", self.text)

    def test_first_obstruction_and_next_frontier_object(self) -> None:
        self.assertIn("Displayed formulas exist", self.summary["first_obstruction"])
        self.assertIn("family identity check", self.summary["first_obstruction"])
        self.assertEqual(
            self.summary["next_frontier_object"],
            "BosonicOxfordReplacementToDGU01IdentityTest_V1",
        )
        self.assertIn("No accepted receipt and no family identity check passed", self.summary["proof_restart_allowed_reason"])

    def test_live_sources_recorded(self) -> None:
        fetched = {row["url"]: row["status"] for row in self.summary["live_sources_fetched"]}
        self.assertEqual(fetched["https://geometricunity.org/2013-oxford-lecture/"], "fetched_200")
        self.assertEqual(
            fetched["https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/"],
            "fetched_200",
        )
        self.assertEqual(fetched["https://geometricunity.org/"], "fetched_200")


if __name__ == "__main__":
    unittest.main(verbosity=2)
