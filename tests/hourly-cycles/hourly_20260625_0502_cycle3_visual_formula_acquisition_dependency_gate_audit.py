#!/usr/bin/env python3
"""Audit VisualFormulaAcquisitionDependencyGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle3-visual-formula-acquisition-dependency-gate.md"
)

OXFORD_ANCHORS = {
    "OxfordPortal_PPT_023343_ShiabOperator",
    "OxfordPortal_PPT_023510_Swervature",
    "OxfordPortal_PPT_023612_Displasion",
    "OxfordPortal_PPT_023853_RSDiracAdjacency",
    "OxfordPortal_PPT_024019_PullbackToX",
}

KEATING_OBJECT_IDS = {
    "KeatingRevealed_ShiabProjectionSheet_V1",
    "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
    "ManuscriptShiabOperatorFormulaCandidate_V1",
    "ManuscriptShiabProjectionIdentityCheck_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing VisualFormulaAcquisitionDependencyGate_V1 JSON")
    return json.loads(match.group(1))


class VisualFormulaAcquisitionDependencyGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "VisualFormulaAcquisitionDependencyGate_V1",
        )
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(self.summary["verdict_class"], "conditional")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle3-visual-formula-acquisition-dependency-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle3_visual_formula_acquisition_dependency_gate_audit.py",
        )

    def test_required_oxford_anchors(self) -> None:
        oxford = next(
            row
            for row in self.summary["visual_formula_objects"]
            if row["object_id"] == "OxfordPortalPowerPointFormulaFramePacket_V1"
        )
        self.assertEqual(set(oxford["required_anchor_ids"]), OXFORD_ANCHORS)
        self.assertEqual(
            oxford["source_path"],
            "Oxford/Portal PowerPoint formula anchors",
        )
        self.assertIn("DGU_VZ", oxford["families_affected"])
        self.assertIn("RS", oxford["families_affected"])
        self.assertIn("IG", oxford["families_affected"])
        self.assertFalse(oxford["can_affect_QFT"])
        self.assertFalse(oxford["accepted_for_routing"])
        self.assertIn(
            "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
            oxford["family_required_objects"]["DGU_VZ"],
        )

    def test_keating_pull_that_up_jamie_object_ids_and_families(self) -> None:
        keating = next(
            row
            for row in self.summary["visual_formula_objects"]
            if row["object_id"]
            == "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1"
        )
        self.assertEqual(
            keating["alternate_or_upstream_object_id"],
            "KeatingRevealed_ShiabProjectionSheet_V1",
        )
        self.assertEqual(set(keating["required_object_ids"]), KEATING_OBJECT_IDS)
        self.assertIn("Pull That Up Jamie video_id TzSEvmqxu48", keating["required_locators"])
        for family in ["IG", "DGU_VZ", "RS", "QFT"]:
            self.assertIn(family, keating["families_affected"])
            self.assertIn(family, keating["family_required_objects"])
        self.assertIn("SourceForcedCodomainSelectorForK_IG", keating["family_required_objects"]["IG"])
        self.assertFalse(keating["accepted_for_routing"])

    def test_state_dependencies_are_ordered_and_non_sufficient(self) -> None:
        self.assertEqual(
            self.summary["dependency_order"],
            [
                "exact_locator",
                "visual_frame_or_source_asset_capture",
                "formula_or_rule_transcription",
                "source_provenance_certificate",
                "target_import_cleanliness_certificate",
                "family_identity_check",
                "accepted_for_routing",
                "proof_restart_reconsideration",
            ],
        )
        deps = self.summary["state_dependencies"]
        self.assertTrue(deps["visual_capture_required_before_formula_transcription"])
        self.assertTrue(deps["formula_transcription_required_before_family_identity"])
        self.assertTrue(deps["source_provenance_required_before_acceptance"])
        self.assertTrue(deps["target_import_cleanliness_required_before_acceptance"])
        self.assertFalse(deps["target_import_cleanliness_sufficient_for_acceptance"])
        self.assertTrue(deps["family_identity_required_before_acceptance"])
        self.assertTrue(deps["accepted_receipt_required_before_proof_restart"])

    def test_first_missing_object_and_acceptance_fields(self) -> None:
        missing = self.summary["first_exact_missing_visual_formula_object"]
        self.assertEqual(missing["id"], "OxfordPortalPowerPointFormulaFramePacket_V1")
        self.assertTrue(missing["required_before_any_candidate_moves_to_accepted"])
        self.assertIn("frame/formula capture", missing["reason_first"])

        next_object = self.summary["constructive_next_acquisition_object"]
        self.assertEqual(next_object["id"], "VisualFormulaReceiptCandidatePacket_V1")
        self.assertEqual(
            next_object["first_instance"],
            "OxfordPortalPowerPointFormulaFramePacket_V1",
        )
        fields = set(next_object["required_acceptance_fields"])
        for required in [
            "source_provenance",
            "formula_or_rule_transcription",
            "target_import_clean",
            "family_identity_check",
            "accepted_for_routing",
            "proof_restart_allowed",
            "claim_promotion_allowed",
        ]:
            self.assertIn(required, fields)

    def test_no_proof_restart_and_no_claim_promotion(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_visual_formula_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertTrue(self.summary["no_claim_promotion"])
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("proof restart", forbidden)
        self.assertIn("GU mathematical or physical claim promoted", forbidden)
        self.assertIn("target outcome selects source object", forbidden)

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Direct Inputs From Cycle-1/2 Source Locator Artifacts",
            "## 3. Visual/Formula Dependency Graph or Table",
            "## 4. First Exact Missing Visual/Formula Object",
            "## 5. Constructive Next Acquisition Object and Acceptance Fields",
            "## 6. Claim Impact and Forbidden Promotions",
            "## 7. Next Meaningful Acquisition/Computation Step",
            "## 9. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
