#!/usr/bin/env python3
"""Audit IGVisualManuscriptSelectorBridge_V1 for Cycle 2 Lane 3."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md"
)

EXPECTED_REQUIRED_OBJECT = "SourceForcedCodomainSelectorForK_IG"
EXPECTED_OBSTRUCTION_OBJECT = (
    "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1"
)
EXPECTED_NEXT_OBJECT = (
    "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1"
)
EXPECTED_SOURCE_SURFACES = {
    "AuthorManuscript2021",
    "OxfordPortal023343VerifiedFrame",
    "KeatingPullThatUpJamieLocator",
}
EXPECTED_RIVAL_IDS = {
    "exterior_covariant_derivative",
    "scalar_trace_divergence_coderivative",
    "symmetric_product_or_derivative",
    "projection_dependent_variant",
    "lower_order_dressed_variant",
    "oxford_visual_vs_manuscript_formula_identity",
    "keating_sheet_identity",
}
EXPECTED_SELECTOR_FIELDS = {
    "candidate_operator_family_under_comparison",
    "representation_or_highest_weight_decomposition",
    "Bianchi_identity_selection_criterion",
    "selected_formula_or_family_member",
    "principal_symbol_class",
    "parent_momentum_degree",
    "projector_policy",
    "projection_loss_behavior",
    "lower_order_rigidity_policy",
    "visual_manuscript_formula_identity",
    "keating_sheet_identity",
    "family_identity_to_SourceForcedCodomainSelectorForK_IG",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class IGVisualManuscriptSelectorBridgeAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], "IGVisualManuscriptSelectorBridge_V1")
        self.assertEqual(self.summary["artifact_id"], "IGVisualManuscriptSelectorBridge_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0711")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_TRIANGULATED_CANDIDATE_NO_SOURCE_FORCED_SELECTOR",
        )
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0711_cycle2_ig_visual_manuscript_selector_bridge_audit.py",
        )

    def test_source_surfaces_are_present_and_read_only(self) -> None:
        self.assertFalse(self.summary["source_acquisition_performed_this_run"])
        self.assertTrue(self.summary["source_surfaces_read_only"])
        surfaces = self.summary["source_surfaces"]
        self.assertEqual({surface["surface_id"] for surface in surfaces}, EXPECTED_SOURCE_SURFACES)
        by_id = {surface["surface_id"]: surface for surface in surfaces}
        manuscript = by_id["AuthorManuscript2021"]
        self.assertEqual(manuscript["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertEqual(
            manuscript["sha256"],
            "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        )
        oxford = by_id["OxfordPortal023343VerifiedFrame"]
        self.assertEqual(oxford["source_id"], "GU-MEDIA-2013-OXFORD")
        self.assertEqual(oxford["timestamp"], "02:33:43")
        self.assertEqual(
            oxford["sha256"],
            "21bb2f7ef3a6a22db7a9650afc1aca8597e66af2c94e48e621da077ba8cdc1b0",
        )
        keating = by_id["KeatingPullThatUpJamieLocator"]
        self.assertEqual(keating["video_id"], "TzSEvmqxu48")
        self.assertEqual(keating["keating_window"], "01:41:43-01:42:50")

    def test_required_selector_object_and_candidate_status(self) -> None:
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(self.summary["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertEqual(
            self.summary["candidate_bridge_id"],
            "ManuscriptOxfordKeating_SharedShiabSelectorCandidate_V1",
        )
        self.assertEqual(
            self.summary["candidate_status"],
            "triangulated_candidate_not_selected",
        )
        self.assertEqual(self.summary["candidate_family"], "IG")
        self.assertFalse(self.summary["source_forced_K_IG_selection"])

    def test_selector_fields_are_explicitly_missing_or_candidate_only(self) -> None:
        selector_fields = self.summary["selector_fields"]
        self.assertEqual(set(selector_fields), EXPECTED_SELECTOR_FIELDS)
        missing_fields = EXPECTED_SELECTOR_FIELDS - {
            "selected_formula_or_family_member",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
        }
        for field in missing_fields:
            self.assertEqual(selector_fields[field]["status"], "missing", field)
            self.assertTrue(selector_fields[field]["required"], field)
        self.assertEqual(
            selector_fields["selected_formula_or_family_member"]["status"],
            "candidate_only_not_source_forced",
        )
        self.assertEqual(
            selector_fields["family_identity_to_SourceForcedCodomainSelectorForK_IG"]["status"],
            "failed_missing_witness",
        )

    def test_rival_eliminator_fields_remain_live(self) -> None:
        rivals = self.summary["rival_eliminator_fields"]
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVAL_IDS)
        for row in rivals:
            self.assertFalse(row["source_eliminator_found"], row["id"])
            self.assertIn(row["status"], {"live_not_eliminated", "blocked_missing_identity_witness", "blocked_missing_asset_or_notes"})
        self.assertFalse(self.summary["all_rivals_eliminated_by_source"])

    def test_receipts_family_identity_and_restart_gate(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_status"], "failed_missing_witness")
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        rule = self.summary["proof_restart_rule"]
        self.assertEqual(
            rule["allowed_if"],
            "accepted_receipt_count_gt_0_and_family_identity_status_passed",
        )
        self.assertFalse(rule["accepted_receipt_condition"])
        self.assertFalse(rule["family_identity_condition"])
        self.assertFalse(rule["proof_restart_allowed"])

    def test_target_import_guard_is_clean_but_insufficient(self) -> None:
        screen = self.summary["target_import_screen"]
        self.assertEqual(screen["target_data_seen"], [])
        self.assertFalse(screen["target_import_detected"])
        self.assertTrue(screen["target_import_clean"])
        self.assertFalse(screen["downstream_physics_used_to_select_source_object"])

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], EXPECTED_OBSTRUCTION_OBJECT)
        self.assertEqual(obstruction["status"], "missing")
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        self.assertEqual(obstruction["blocks_acceptance_for"], EXPECTED_REQUIRED_OBJECT)
        missing = set(obstruction["missing_selector_fields"])
        for required in [
            "candidate_operator_family_under_comparison",
            "Bianchi_identity_selection_criterion",
            "rival_eliminators",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
        ]:
            self.assertIn(required, missing)
        self.assertEqual(self.summary["next_object"], EXPECTED_NEXT_OBJECT)
        self.assertIn("representation/highest-weight", self.summary["next_meaningful_step"])
        self.assertIn(EXPECTED_OBSTRUCTION_OBJECT, self.text)

    def test_impact_and_demotion_conditions_are_decision_grade(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertEqual(impact["accepted_for_routing_count_would_be"], 1)
        self.assertEqual(impact["family_identity_status_would_be"], "passed")
        self.assertTrue(impact["SourceForcedCodomainSelectorForK_IG_source_identity_available"])
        self.assertTrue(impact["proof_restart_possible_only_after_receipt_and_identity"])
        self.assertFalse(impact["downstream_physics_promoted_by_packet_alone"])
        self.assertGreaterEqual(len(self.summary["falsification_or_demotion_conditions"]), 5)
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
