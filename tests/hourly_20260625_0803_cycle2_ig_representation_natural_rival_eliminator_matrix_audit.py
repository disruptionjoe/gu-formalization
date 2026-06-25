#!/usr/bin/env python3
"""Audit CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md"
)

EXPECTED_ARTIFACT = "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1"
EXPECTED_REQUIRED_OBJECT = "SourceForcedCodomainSelectorForK_IG"
EXPECTED_NEXT_OBJECT = "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1"
EXPECTED_RIVAL_IDS = {
    "displayed_or_canon_shiab_clifford_contraction",
    "exterior_covariant_derivative",
    "einstein_ricci_contraction_analog",
    "hodge_star_or_dimension_shift_analog",
    "symmetric_product_or_derivative",
    "projection_dependent_shiab_variant",
    "lower_order_dressed_variant",
    "oxford_visual_formula_variant",
    "ptuj_missing_sheet_variant",
    "ucsd_middle_map_variant",
}
EXPECTED_SOURCES = [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
    "explorations/hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
    "explorations/hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
    "canon/shiab-existence-cl95.md",
    "literature/weinstein-ucsd-2025-04-transcript.md",
]


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 10 machine-readable JSON summary")
    return json.loads(match.group(1))


class IGRepresentationNaturalRivalEliminatorMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 2)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_MATRIX_BUILT_ZERO_SOURCE_NATURAL_RIVAL_ELIMINATIONS",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["matrix_status"],
            "built_as_blocking_inventory_not_acceptance_receipt",
        )
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0803_cycle2_ig_representation_natural_rival_eliminator_matrix_audit.py",
        )

    def test_required_sources_and_claim_under_test(self) -> None:
        self.assertEqual(self.summary["sources_read_first"], EXPECTED_SOURCES)
        self.assertEqual(self.summary["family"], "IG")
        self.assertEqual(self.summary["required_object"], EXPECTED_REQUIRED_OBJECT)
        self.assertIn("selects_K_IG_codomain_selector", self.summary["claim_under_test"])
        self.assertEqual(self.summary["shiab_existence_status"], "canon_exists_in_Cl95_setting")
        self.assertFalse(self.summary["shiab_existence_sufficient_for_selection"])
        self.assertTrue(self.summary["canon_open_uniqueness_issue"])

    def test_rival_coverage_is_complete_and_uneliminated(self) -> None:
        matrix = self.summary["candidate_rival_family_matrix"]
        ids = {row["id"] for row in matrix}
        self.assertEqual(ids, EXPECTED_RIVAL_IDS)
        self.assertEqual(set(self.summary["rival_coverage_required_ids"]), EXPECTED_RIVAL_IDS)
        self.assertEqual(self.summary["candidate_rows_considered"], len(EXPECTED_RIVAL_IDS))
        self.assertEqual(self.summary["source_natural_rival_rows"], len(EXPECTED_RIVAL_IDS) - 1)
        for row in matrix:
            self.assertFalse(row["source_natural_eliminator_found"], row["id"])
            self.assertIn(
                row["status"],
                {
                    "hosted_or_canon_exists_not_selected",
                    "live_not_eliminated",
                    "blocked_missing_identity_witness",
                    "blocked_missing_asset_or_notes",
                    "motivated_but_under_specified",
                },
                row["id"],
            )
            self.assertTrue(row["required_eliminator_field"], row["id"])
        self.assertEqual(self.summary["source_natural_eliminations_today"], 0)
        self.assertFalse(self.summary["all_representation_natural_rivals_eliminated"])
        self.assertFalse(self.summary["selected_K_IG_codomain_selector_today"])

    def test_zero_accepted_selector_and_no_proof_restart(self) -> None:
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
        self.assertIn("accepted_selector_packet_count_gt_0", rule["allowed_if"])
        self.assertIn("all_representation_natural_rivals_eliminated", rule["allowed_if"])
        self.assertFalse(rule["accepted_selector_packet_condition"])
        self.assertFalse(rule["family_identity_condition"])
        self.assertFalse(rule["rival_elimination_condition"])
        self.assertTrue(rule["target_import_condition"])
        self.assertFalse(rule["proof_restart_allowed"])

    def test_no_target_import_selector_is_accepted(self) -> None:
        screen = self.summary["target_import_screen"]
        self.assertEqual(screen["target_data_seen"], [])
        self.assertFalse(screen["target_import_detected"])
        self.assertFalse(screen["target_import_selector_detected"])
        self.assertFalse(screen["target_import_selector_allowed"])
        self.assertTrue(screen["target_import_clean"])
        self.assertFalse(screen["target_import_clean_sufficient_for_acceptance"])
        self.assertFalse(screen["downstream_physics_used_to_select_source_object"])
        self.assertEqual(screen["target_imported_physics_recorded"], [])

    def test_strongest_positive_attempt_is_not_a_selector(self) -> None:
        attempt = self.summary["strongest_positive_eliminator_attempt"]
        self.assertEqual(
            attempt["status"],
            "source_natural_candidate_family_and_required_eliminator_fields_identified",
        )
        self.assertTrue(attempt["uses_canon_shiab_existence"])
        self.assertTrue(attempt["uses_ucsd_bianchi_contraction_middle_map_motivation"])
        self.assertTrue(attempt["uses_manuscript_oxford_ptuj_selector_locator_triangle"])
        self.assertEqual(attempt["selector_status"], "not_source_forced")
        self.assertEqual(attempt["eliminator_status"], "not_obtained")

    def test_exact_next_object_and_obstruction_contract(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], EXPECTED_NEXT_OBJECT)
        self.assertEqual(obstruction["status"], "missing")
        self.assertEqual(obstruction["obstruction_type"], "missing_source_natural_selector_theorem")
        self.assertEqual(obstruction["within_broader_artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(obstruction["blocks_acceptance_for"], EXPECTED_REQUIRED_OBJECT)
        self.assertTrue(obstruction["blocks_proof_restart"])
        must_provide = set(obstruction["must_provide"])
        for required in [
            "representation_or_highest_weight_decomposition",
            "Bianchi_identity_selection_rule",
            "equivariant_hom_space_multiplicity",
            "per_rival_eliminators_for_matrix_rows",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
            "target_import_screen",
        ]:
            self.assertIn(required, must_provide)
        self.assertEqual(self.summary["next_object"], EXPECTED_NEXT_OBJECT)
        self.assertIn("equivariant_hom_space_multiplicity", self.summary["next_meaningful_step"])
        self.assertIn(EXPECTED_NEXT_OBJECT, self.text)

    def test_impact_and_demotion_are_scoped(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertEqual(impact["accepted_selector_packet_count_would_be"], 1)
        self.assertEqual(impact["accepted_receipt_count_would_be"], 1)
        self.assertEqual(impact["accepted_for_routing_count_would_be"], 1)
        self.assertTrue(impact["source_natural_eliminations_would_equal_rival_rows"])
        self.assertEqual(impact["family_identity_status_would_be"], "passed")
        self.assertTrue(impact["SourceForcedCodomainSelectorForK_IG_source_identity_available"])
        self.assertTrue(
            impact["proof_restart_possible_only_after_receipt_identity_and_rival_elimination"]
        )
        self.assertFalse(impact["downstream_physics_promoted_by_packet_alone"])
        self.assertGreaterEqual(len(self.summary["falsification_or_demotion_conditions"]), 7)
        self.assertIn("accepted_selector_packet_count: 0", self.text)
        self.assertIn("proof_restart_allowed: false", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
