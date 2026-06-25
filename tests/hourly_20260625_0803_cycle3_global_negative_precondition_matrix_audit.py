#!/usr/bin/env python3
"""Audit GlobalNegativeReceiptBundlePreconditionAfter0803_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_ARTIFACT = "GlobalNegativeReceiptBundlePreconditionAfter0803_V1"
EXPECTED_VERDICT = "NO_GLOBAL_NO_GO_PROMOTED_SCOPED_FAILURES_REMAIN_ROUTE_SCOPED"
EXPECTED_PRECONDITIONS = {
    "complete_primary_source_coverage",
    "complete_alternate_source_coverage",
    "complete_family_identity_failure_or_impossibility_matrix",
    "complete_source_natural_rival_coverage",
    "positive_no_target_import_audit",
    "precise_class_boundary_statement",
}
EXPECTED_ROUTES = {
    "RS_d_RS_minus_1_receipt",
    "DGU_actual_D_GU_epsilon_0_1_certificate",
    "IG_K_IG_source_forced_selector",
    "QFT_local_finite_extraction",
    "cross_route_global_GU_negative",
}
EXPECTED_SCOPED_ROUTES = {
    "RS_d_RS_minus_1_receipt",
    "DGU_actual_D_GU_epsilon_0_1_certificate",
    "IG_K_IG_source_forced_selector",
    "QFT_local_finite_extraction",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 9 machine-readable JSON summary")
    return json.loads(match.group(1))


class GlobalNegativePreconditionMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(
            self.summary["verdict_class"], "blocked_global_negative_promotion"
        )

    def test_global_no_go_is_not_promoted(self) -> None:
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["global_negative_receipt_bundle_exists"])
        self.assertFalse(self.summary["complete_source_coverage"])
        self.assertFalse(self.summary["alternate_source_coverage"])
        self.assertFalse(self.summary["family_identity_failure_coverage"])
        self.assertFalse(self.summary["no_target_import_audit_complete"])
        self.assertIn("global_no_go_promoted: false", self.text)
        self.assertIn("forbidden_now: global no-go promotion", self.text)

    def test_required_global_preconditions_are_listed(self) -> None:
        self.assertEqual(
            set(self.summary["required_global_preconditions"]), EXPECTED_PRECONDITIONS
        )
        for precondition in EXPECTED_PRECONDITIONS:
            self.assertIn(precondition, self.text)

    def test_scoped_failures_stay_route_scoped(self) -> None:
        scoped = self.summary["scoped_negative_evidence"]
        self.assertEqual({row["route"] for row in scoped}, EXPECTED_SCOPED_ROUTES)
        for row in scoped:
            self.assertEqual(row["scope"], "route_scoped", row["route"])
            self.assertFalse(row["global_no_go_allowed"], row["route"])

    def test_precondition_matrix_denies_every_global_promotion(self) -> None:
        matrix = self.summary["global_no_go_precondition_matrix"]
        self.assertEqual({row["route"] for row in matrix}, EXPECTED_ROUTES)
        for row in matrix:
            self.assertFalse(row["complete_source_coverage"], row["route"])
            self.assertFalse(row["alternate_source_coverage"], row["route"])
            self.assertFalse(row["family_identity_failures_complete"], row["route"])
            self.assertFalse(row["no_target_import_audit_complete"], row["route"])
            self.assertFalse(row["global_no_go_promotion_allowed"], row["route"])
        cross_route = next(
            row for row in matrix if row["route"] == "cross_route_global_GU_negative"
        )
        self.assertFalse(cross_route["negative_evidence_exists"])
        self.assertEqual(cross_route["local_demotions_allowed"], [])

    def test_complete_source_and_alternate_coverage_remain_missing(self) -> None:
        matrix = self.summary["global_no_go_precondition_matrix"]
        for row in matrix:
            self.assertFalse(row["complete_source_coverage"], row["route"])
            self.assertFalse(row["alternate_source_coverage"], row["route"])
        self.assertFalse(self.summary["complete_source_coverage"])
        self.assertFalse(self.summary["alternate_source_coverage"])

        rs = next(row for row in matrix if row["route"] == "RS_d_RS_minus_1_receipt")
        self.assertIn("exact_UCSD_slide_frame_source_surface", rs["coverage_missing"])
        self.assertIn("family_identity", rs["coverage_missing"])

        dgu = next(
            row
            for row in matrix
            if row["route"] == "DGU_actual_D_GU_epsilon_0_1_certificate"
        )
        self.assertIn("actual_D_GU_epsilon_0_1_identity_witness", dgu["coverage_missing"])
        self.assertIn("positive_target_import_screen", dgu["coverage_missing"])

    def test_local_demotions_are_allowed_without_global_no_go(self) -> None:
        demotions = set(self.summary["local_demotions_allowed_now"])
        for expected in [
            "equation_10_10_as_RS_d_RS_minus_1_receipt",
            "UCSD_aggregate_rolled_operator_as_typed_pure_RS_minus_one_rule",
            "Oxford_or_manuscript_bosonic_adjacency_as_actual_D_GU_epsilon_0_1_certificate",
            "VZ_or_physical_recovery_replay_without_actual_DGU_certificate",
            "Cl95_Shiab_existence_as_source_forced_K_IG_selector",
            "K_IG_proof_restart_without_rival_elimination",
            "QFT_finite_extraction_without_source_defined_tilde_phys_F_phys_descent",
        ]:
            self.assertIn(expected, demotions)
        self.assertIn("None of these demotions says GU is false.", self.text)

    def test_first_missing_global_negative_object_is_complete_bundle(self) -> None:
        missing = self.summary["first_exact_missing_global_negative_object"]
        self.assertEqual(missing["id"], "CompleteGlobalNegativeReceiptBundleAfter0803_V1")
        self.assertEqual(missing["status"], "missing")
        self.assertEqual(missing["currently_populated_fields"], ["partial_route_matrix"])
        required = set(missing["required_fields"])
        for field in [
            "claim_class",
            "source_inventory",
            "alternate_source_inventory",
            "route_matrix",
            "family_identity_failure_matrix",
            "rival_coverage_matrix",
            "target_import_audit",
            "class_boundary_statement",
            "rollback_condition",
        ]:
            self.assertIn(field, required)

    def test_impact_if_closed_remains_class_relative_not_global_gu_falsifier(self) -> None:
        impact = self.summary["impact_if_closed"]
        self.assertTrue(impact["would_allow_class_relative_no_go"])
        self.assertTrue(impact["would_block_proof_restarts_across_audited_class"])
        self.assertTrue(impact["would_force_different_source_class_or_stronger_category"])
        self.assertTrue(impact["would_not_automatically_falsify_all_GU"])

    def test_falsification_and_next_step_require_coverage_audit(self) -> None:
        condition = self.summary["falsification_or_demotion_condition"]
        self.assertIn(
            "complete_global_negative_receipt_bundle",
            condition["artifact_falsified_by"],
        )
        self.assertEqual(
            set(condition["demote_future_global_no_go_if_any_missing"]),
            {
                "unaudited_primary_or_alternate_source_surface",
                "family_identity_absent_rather_than_failed",
                "source_natural_rival_still_live",
                "negative_result_depends_on_target_data_or_repo_preference",
                "imprecise_class_boundary",
            },
        )

        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(
            next_step["id"],
            "CompleteSourceAndAlternateRouteCoverageAuditFor0803Failures_V1",
        )
        self.assertEqual(next_step["not_next"], "global_no_go_declaration")
        self.assertIn("run_positive_no_target_import_audit", next_step["required_work"])
        self.assertIn(
            "then_test_class_relative_global_negative_statement",
            next_step["required_work"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
