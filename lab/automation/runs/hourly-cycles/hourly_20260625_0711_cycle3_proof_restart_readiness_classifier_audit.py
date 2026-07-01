#!/usr/bin/env python3
"""Audit ProofRestartReadinessClassifierAfter0711_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ROUTES = {
    "IG",
    "DGU_VZ",
    "RS",
    "QFT",
    "Oxford_visual",
    "PTUJ_Keating_visual",
}

EXPECTED_FIRST_MISSING = {
    "IG": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
    "DGU_VZ": "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
    "RS": "ImageTypedRSMinusOneRuleCell_V1",
    "QFT": "SourceDefinedFiniteLocalExtractionOperation_V1",
    "Oxford_visual": "FamilyIdentityForVerifiedOxfordPortalFrames_V1",
    "PTUJ_Keating_visual": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
}

EXPECTED_NEXT_OBJECTS = {
    "IG": "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1",
    "DGU_VZ": "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
    "RS": "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
    "QFT": "LocalPhysicalFieldQuotientAndNaturalityLemma_V1",
    "Oxford_visual": "VisualFormulaReceiptCandidatePacket_V1",
    "PTUJ_Keating_visual": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
}

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived from cycle 1-2 artifacts",
    "## 3. Strongest positive route per family/source path",
    "## 4. First exact obstruction per route",
    "## 5. Impact if closed",
    "## 6. Falsification/demotion condition",
    "## 7. Next meaningful sequential lanes",
    "## 8. Machine-readable JSON summary",
]


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ProofRestartReadinessClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.routes = {
            route["route_id"]: route for route in cls.summary["routes"]
        }

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ProofRestartReadinessClassifierAfter0711_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked_all_routes")
        self.assertEqual(self.summary["routes_classified_count"], 6)
        self.assertFalse(self.summary["global_proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_all_required_routes_present_once(self) -> None:
        self.assertEqual(set(self.routes), EXPECTED_ROUTES)
        self.assertEqual(len(self.summary["routes"]), len(EXPECTED_ROUTES))

    def test_global_counts_are_zero(self) -> None:
        counts = self.summary["global_counts"]
        self.assertEqual(counts["accepted_receipt_count"], 0)
        self.assertEqual(counts["accepted_for_routing_count"], 0)
        self.assertEqual(counts["family_identity_checks_passed"], 0)
        self.assertEqual(counts["proof_restart_ready_count"], 0)
        self.assertEqual(counts["claim_promotion_count"], 0)

    def test_every_route_is_closed_to_restart_and_promotion(self) -> None:
        for route_id, route in self.routes.items():
            with self.subTest(route=route_id):
                self.assertEqual(route["accepted_receipt_count"], 0)
                self.assertEqual(route["accepted_for_routing_count"], 0)
                self.assertEqual(route["family_identity_checks_passed"], 0)
                self.assertFalse(route["proof_restart_allowed"])
                self.assertFalse(route["claim_promotion_allowed"])
                self.assertIn(route["classification"], {
                    "blocked",
                    "underdefined",
                    "underdefined_scoped_fail",
                    "conditional_verified_frames_blocked_for_receipt",
                    "blocked_tool_source_acquisition",
                })

    def test_first_missing_objects_and_next_objects_are_exact(self) -> None:
        for route_id in EXPECTED_ROUTES:
            route = self.routes[route_id]
            with self.subTest(route=route_id):
                self.assertEqual(
                    route["first_missing_object"],
                    EXPECTED_FIRST_MISSING[route_id],
                )
                self.assertEqual(
                    route["next_object"],
                    EXPECTED_NEXT_OBJECTS[route_id],
                )
                self.assertGreaterEqual(len(route["sequential_prerequisites"]), 5)

        self.assertEqual(
            self.routes["DGU_VZ"]["alternate_or_upstream_missing_object"],
            "BosonicToDGU01SectorIdentityRule_V1",
        )
        self.assertEqual(
            self.routes["PTUJ_Keating_visual"]["downstream_missing_source_object"],
            "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
        )
        self.assertEqual(
            self.routes["PTUJ_Keating_visual"]["downstream_missing_identity_object"],
            "KeatingRevealed_ShiabProjectionSheet_V1",
        )

    def test_proof_restart_rule_requires_receipt_and_family_identity(self) -> None:
        rule = self.summary["proof_restart_rule"]
        required = set(rule["required_conditions"])
        for condition in [
            "accepted_receipt_count_gt_0",
            "family_identity_checks_passed_gt_0",
            "target_import_screen_passed",
            "route_specific_restart_object_named",
        ]:
            self.assertIn(condition, required)
        self.assertTrue(rule["all_routes_fail_before_restart"])

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        expected_false = {
            "IG_selector_accepted",
            "DGU_VZ_actual_operator_accepted",
            "RS_d_RS_minus_1_accepted",
            "QFT_finite_extraction_valid",
            "Oxford_visual_receipt_accepted",
            "PTUJ_formula_asset_accepted",
            "theta_FLRW_or_dark_energy_promoted",
            "QFT_recovery_promoted",
            "generation_count_promoted",
            "global_GU_claim_promoted",
        }
        self.assertEqual(set(promotions), expected_false)
        for key, value in promotions.items():
            self.assertIs(value, False, key)

    def test_read_sources_include_all_cycle_one_and_two_artifacts(self) -> None:
        sources = set(self.summary["read_sources"])
        for filename in [
            "explorations/hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
            "explorations/hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
            "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
            "explorations/hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
            "explorations/hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md",
            "explorations/hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
            "explorations/hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
            "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
            "explorations/hourly-20260625-0711-cycle2-qft-finite-local-extraction-spec-gate.md",
            "explorations/hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
        ]:
            self.assertIn(filename, sources)

    def test_next_sequential_lanes_are_not_proof_restarts(self) -> None:
        lanes = set(self.summary["next_meaningful_sequential_lanes"])
        for lane in [
            "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1",
            "OxfordBosonicTwoAnchorDGU01FamilyIdentityPacket_V1",
            "AlternatePrimarySourceRSMinusOneRuleSearchBundle_V1",
            "LocalPhysicalFieldQuotientAndNaturalityLemma_V1",
            "VisualFormulaReceiptCandidatePacket_V1_with_accepted_for_routing_false_until_family_identity",
            "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
        ]:
            self.assertIn(lane, lanes)

    def test_text_contains_decision_grade_blockers(self) -> None:
        for phrase in [
            "No route has the required conjunction",
            "routes_ready_for_proof_restart: 0",
            "global_proof_restart_allowed: false",
            "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
            "SourceDefinedFiniteLocalExtractionOperation_V1",
        ]:
            self.assertIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
