#!/usr/bin/env python3
"""Audit OxfordPortalPowerPointFormulaFramePacket_V1 spec gate."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle1-oxford-portal-formula-frame-packet-spec.md"
)

REQUIRED_TIMESTAMPS = {
    "02:33:43",
    "02:35:10",
    "02:36:12",
    "02:38:53",
    "02:40:19",
}

REQUIRED_ANCHOR_IDS = {
    "OxfordPortal_PPT_023343_ShiabOperator",
    "OxfordPortal_PPT_023510_Swervature",
    "OxfordPortal_PPT_023612_Displasion",
    "OxfordPortal_PPT_023853_RSDiracAdjacency",
    "OxfordPortal_PPT_024019_PullbackToX",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing OxfordPortalPowerPointFormulaFramePacket_V1 JSON")
    return json.loads(match.group(1))


class OxfordPortalFormulaFramePacketSpecAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "OxfordPortalPowerPointFormulaFramePacket_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_FORMULA_FRAME_PACKET_MISSING_ZERO_ACCEPTED_VISUAL_RECEIPTS",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle1-oxford-portal-formula-frame-packet-spec.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle1_oxford_portal_formula_frame_packet_spec_audit.py",
        )
        self.assertEqual(
            identity["artifact_id"],
            "OxfordPortalPowerPointFormulaFramePacket_V1",
        )

    def test_all_five_timestamps_and_anchor_ids_are_required(self) -> None:
        self.assertEqual(set(self.summary["required_timestamps"]), REQUIRED_TIMESTAMPS)
        rows = self.summary["per_anchor_acquisition_spec"]
        self.assertEqual({row["timestamp"] for row in rows}, REQUIRED_TIMESTAMPS)
        self.assertEqual({row["anchor_id"] for row in rows}, REQUIRED_ANCHOR_IDS)
        for timestamp in REQUIRED_TIMESTAMPS:
            self.assertIn(timestamp, self.text)

    def test_zero_receipts_no_restart_no_promotion(self) -> None:
        self.assertFalse(self.summary["current_repo_source_suffices"])
        self.assertEqual(self.summary["accepted_visual_formula_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("accepted_visual_formula_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_family_identity_is_blocked(self) -> None:
        self.assertEqual(self.summary["family_identity_status"], "blocked")
        self.assertTrue(self.summary["family_identity_blocked"])
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "OxfordPortalPowerPointFormulaFramePacket_V1",
        )
        self.assertTrue(obstruction["missing"])
        self.assertIn("family identity cannot be checked", obstruction["description"])
        self.assertIn("family_identity_status: blocked", self.text)

    def test_per_anchor_family_impacts_and_fields(self) -> None:
        rows = {row["timestamp"]: row for row in self.summary["per_anchor_acquisition_spec"]}
        self.assertIn("IG", rows["02:33:43"]["candidate_family_impact"][0])
        self.assertIn("DGU_VZ", rows["02:35:10"]["candidate_family_impact"])
        self.assertIn("DGU_VZ", rows["02:36:12"]["candidate_family_impact"])
        self.assertIn("RS", rows["02:38:53"]["candidate_family_impact"])
        self.assertIn("DGU_VZ", rows["02:40:19"]["candidate_family_impact"])
        for row in rows.values():
            self.assertFalse(row["accepted_for_routing"])
            self.assertGreaterEqual(
                len(row["required_displayed_formula_or_rule_fields"]),
                4,
            )

    def test_required_packet_fields_and_family_objects(self) -> None:
        fields = set(self.summary["required_packet_fields"])
        for required in [
            "frame_capture",
            "frame_checksum_or_archive_id",
            "formula_or_rule_transcription",
            "transcription_uncertainty",
            "target_data_seen",
            "family_identity_status",
            "accepted_for_routing",
        ]:
            self.assertIn(required, fields)

        family_objects = self.summary["family_required_objects"]
        self.assertEqual(
            family_objects["DGU_VZ"],
            "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
        )
        self.assertEqual(family_objects["RS"], "source.action_or_operator for d_RS,-1")
        self.assertEqual(family_objects["IG"], "SourceForcedCodomainSelectorForK_IG")
        self.assertIn("P_fin^b", family_objects["QFT"])

    def test_demotion_condition_preserves_source_scope(self) -> None:
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertIn("Demote Oxford/Portal PowerPoint anchors", condition)
        self.assertIn("emit no required DGU_VZ RS or IG family object", condition)
        self.assertIn("source-scope limited", self.text)
        self.assertIn("not create a global no-go", self.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo/Source Surfaces",
            "## 3. Strongest Positive Acquisition Attempt",
            "## 4. First Exact Obstruction/Missing Visual/Formula Object",
            "## 5. Impact If Closed",
            "## 6. Falsification/Demotion Condition",
            "## 7. Next Meaningful Acquisition/Computation Step",
            "## 8. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
