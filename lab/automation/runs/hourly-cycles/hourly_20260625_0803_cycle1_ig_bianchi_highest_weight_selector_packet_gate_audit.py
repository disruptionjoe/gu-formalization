#!/usr/bin/env python3
"""Audit PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md"
)

EXPECTED_ARTIFACT = "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1"
EXPECTED_REQUIRED_OBJECT = "SourceForcedCodomainSelectorForK_IG"
EXPECTED_MISSING_OBJECT = "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1"
EXPECTED_SOURCE_SURFACES = {
    "AuthorManuscript2021",
    "OxfordPortal023343VerifiedFrame",
    "PTUJKeatingTzSEvmqxu48Locator",
    "UCSD2025Transcript",
}
EXPECTED_RIVALS = {
    "exterior_covariant_derivative",
    "einstein_ricci_contraction_analog",
    "hodge_star_or_dimension_shift_analog",
    "symmetric_product_or_derivative",
    "projection_dependent_shiab_variant",
    "lower_order_dressed_variant",
    "oxford_visual_formula_variant",
    "ptuj_missing_sheet_variant",
}
EXPECTED_REQUIREMENT_KEYS = {
    "candidate_operator_family_under_comparison",
    "representation_or_highest_weight_decomposition",
    "Bianchi_identity_selection_criterion",
    "selected_Shiab_formula_or_family_member",
    "principal_symbol_class",
    "parent_momentum_degree",
    "projector_policy",
    "projection_loss_behavior",
    "lower_order_rigidity_policy",
    "formula_surface_identity",
    "rival_eliminators",
    "family_identity_to_SourceForcedCodomainSelectorForK_IG",
    "target_import_screen",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 10 machine-readable JSON summary")
    return json.loads(match.group(1))


class BianchiHighestWeightSelectorPacketGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_ZERO_ACCEPTED_SELECTOR_PACKET_NO_PROOF_RESTART",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(self.summary["packet_status"], "source_motivated_but_not_source_forced")
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0803_cycle1_ig_bianchi_highest_weight_selector_packet_gate_audit.py",
        )

    def test_sources_and_surfaces_are_decision_inputs_not_receipts(self) -> None:
        self.assertEqual(set(self.summary["source_surfaces"][i]["surface_id"] for i in range(4)), EXPECTED_SOURCE_SURFACES)
        for surface in self.summary["source_surfaces"]:
            self.assertEqual(surface["selector_rule_status"], "missing", surface["surface_id"])
            self.assertFalse(surface["accepted_for_selector_packet"], surface["surface_id"])
        self.assertIn("literature/weinstein-ucsd-2025-04-transcript.md", self.summary["sources_read_first"])
        positive = self.summary["positive_construction"]
        self.assertEqual(positive["status"], "source_motivated_selector_search_target")
        self.assertFalse(positive["source_forced_selector_rule_found"])
        self.assertIn("omega_one_to_omega_d_minus_one_middle_map_problem", positive["ucsd_positive_motifs"])

    def test_selector_acceptance_requirements_remain_missing(self) -> None:
        requirements = self.summary["selector_acceptance_requirements"]
        self.assertEqual(set(requirements), EXPECTED_REQUIREMENT_KEYS)
        for key in EXPECTED_REQUIREMENT_KEYS - {
            "selected_Shiab_formula_or_family_member",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
            "target_import_screen",
        }:
            self.assertEqual(requirements[key], "missing", key)
        self.assertEqual(
            requirements["selected_Shiab_formula_or_family_member"],
            "candidate_only_not_source_forced",
        )
        self.assertEqual(
            requirements["family_identity_to_SourceForcedCodomainSelectorForK_IG"],
            "failed_missing_witness",
        )
        self.assertEqual(requirements["target_import_screen"], "clean_but_not_sufficient_for_acceptance")

    def test_rival_eliminators_all_remain_unaccepted(self) -> None:
        rivals = self.summary["rival_eliminator_fields"]
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVALS)
        for row in rivals:
            self.assertFalse(row["source_eliminator_found"], row["id"])
            self.assertIn(
                row["status"],
                {
                    "live_not_eliminated",
                    "blocked_missing_identity_witness",
                    "blocked_missing_asset_or_notes",
                },
                row["id"],
            )
        self.assertFalse(self.summary["all_representation_natural_rivals_eliminated"])

    def test_zero_acceptance_blocks_proof_restart(self) -> None:
        self.assertEqual(self.summary["accepted_selector_packets"], [])
        self.assertEqual(self.summary["accepted_selector_packet_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_for_routing_count"], 0)
        self.assertEqual(self.summary["family_identity_status"], "failed_missing_witness")
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertFalse(self.summary["source_forced_K_IG_selection"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        rule = self.summary["proof_restart_rule"]
        self.assertIn("all_representation_natural_rivals_eliminated", rule["allowed_if"])
        self.assertFalse(rule["accepted_selector_packet_condition"])
        self.assertFalse(rule["family_identity_condition"])
        self.assertFalse(rule["rival_elimination_condition"])
        self.assertFalse(rule["proof_restart_allowed"])

    def test_missing_object_is_exact_and_blocks_restart(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], EXPECTED_MISSING_OBJECT)
        self.assertEqual(obstruction["status"], "missing")
        self.assertEqual(obstruction["obstruction_type"], "missing_source_object")
        self.assertEqual(obstruction["blocks_acceptance_for"], EXPECTED_ARTIFACT)
        self.assertTrue(obstruction["blocks_proof_restart"])
        self.assertTrue(obstruction["or_sharper_successor_allowed"])
        must_provide = set(obstruction["must_provide"])
        for required in [
            "Bianchi_identity_selection_criterion",
            "representation_natural_rival_eliminators",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
            "target_import_screen",
        ]:
            self.assertIn(required, must_provide)
        self.assertIn(EXPECTED_MISSING_OBJECT, self.text)

    def test_no_target_imported_physics_is_recorded(self) -> None:
        screen = self.summary["target_import_screen"]
        self.assertEqual(screen["target_data_seen"], [])
        self.assertFalse(screen["target_import_detected"])
        self.assertTrue(screen["target_import_clean"])
        self.assertFalse(screen["target_import_clean_sufficient_for_acceptance"])
        self.assertFalse(screen["downstream_physics_used_to_select_source_object"])
        self.assertEqual(screen["target_imported_physics_recorded"], [])

    def test_impact_demotion_and_next_step_are_scoped(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_selector_packet_count_would_be"], 1)
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertTrue(impact["SourceForcedCodomainSelectorForK_IG_source_identity_available"])
        self.assertTrue(impact["proof_restart_possible_only_after_receipt_and_identity"])
        self.assertFalse(impact["downstream_physics_promoted_by_packet_alone"])
        self.assertGreaterEqual(len(self.summary["falsification_or_demotion_conditions"]), 7)
        self.assertEqual(self.summary["next_object"], EXPECTED_MISSING_OBJECT)
        self.assertIn("representation/highest-weight", self.summary["next_meaningful_step"])
        self.assertIn("accepted_selector_packet_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
