#!/usr/bin/env python3
"""Audit GlobalNegativeReceiptBundlePreconditionAfter1302_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_ARTIFACT = "GlobalNegativeReceiptBundlePreconditionAfter1302_V1"
EXPECTED_VERDICT = "NO_GLOBAL_NO_GO_PROMOTED_SCOPED_NEGATIVES_REMAIN_ROUTE_LOCAL"
EXPECTED_ROUTES = {"PTUJ", "IG", "DGU_VZ", "RS", "QFT"}
EXPECTED_GLOBAL_PRECONDITIONS = {
    "complete_primary_source_coverage",
    "complete_alternate_source_coverage",
    "complete_family_identity_failure_or_impossibility_matrix",
    "complete_source_natural_rival_coverage",
    "positive_no_target_import_audit",
    "precise_class_boundary_statement",
    "rollback_conditions",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 6\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 6 machine-readable JSON summary")
    return json.loads(match.group(1))


class GlobalNegativePreconditionAfter1302Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_required_booleans(self) -> None:
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(self.summary["verdict"], EXPECTED_VERDICT)
        self.assertEqual(
            self.summary["verdict_class"], "blocked_global_negative_promotion"
        )
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["complete_global_negative_bundle_present"])
        self.assertFalse(self.summary["target_import_used"])

    def test_required_global_preconditions_are_complete(self) -> None:
        self.assertEqual(
            set(self.summary["required_global_preconditions"]),
            EXPECTED_GLOBAL_PRECONDITIONS,
        )
        for precondition in EXPECTED_GLOBAL_PRECONDITIONS:
            self.assertIn(precondition, self.text)

    def test_route_coverage_fields_block_global_promotion(self) -> None:
        routes = self.summary["routes"]
        self.assertEqual({row["route"] for row in routes}, EXPECTED_ROUTES)
        self.assertEqual(self.summary["scoped_negative_count"], len(EXPECTED_ROUTES))

        required_keys = {
            "complete_source_coverage_needed",
            "alternate_source_coverage_needed",
            "current_strongest_negative",
            "why_global_no_go_blocked",
            "missing_complete_bundle",
        }
        for row in routes:
            self.assertFalse(row["global_no_go_promoted"], row["route"])
            self.assertFalse(row["complete_source_coverage_present"], row["route"])
            self.assertFalse(row["alternate_source_coverage_present"], row["route"])
            self.assertFalse(row["target_import_used"], row["route"])
            for key in required_keys:
                self.assertIn(key, row, row["route"])
                self.assertTrue(row[key], f"{row['route']} has empty {key}")
            self.assertGreaterEqual(len(row["complete_source_coverage_needed"]), 5)
            self.assertGreaterEqual(len(row["alternate_source_coverage_needed"]), 3)

    def test_no_global_no_go_promotion_from_incomplete_source_coverage(self) -> None:
        for row in self.summary["routes"]:
            incomplete = (
                not row["complete_source_coverage_present"]
                or not row["alternate_source_coverage_present"]
            )
            self.assertTrue(incomplete, row["route"])
            if incomplete:
                self.assertFalse(row["global_no_go_promoted"], row["route"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["complete_global_negative_bundle_present"])

    def test_route_specific_blockers_remain_scoped(self) -> None:
        by_route = {row["route"]: row for row in self.summary["routes"]}
        self.assertEqual(
            by_route["PTUJ"]["scoped_negative"],
            "local_extractor_manifest_branch_absent",
        )
        self.assertEqual(
            by_route["IG"]["scoped_negative"],
            "uniqueness_based_selector_proof_start_not_closed",
        )
        self.assertEqual(
            by_route["DGU_VZ"]["scoped_negative"],
            "actual_DGU_0_1_identity_witness_absent_from_current_sources",
        )
        self.assertEqual(
            by_route["RS"]["scoped_negative"],
            "transcript_only_RS_promotion_rejected",
        )
        self.assertEqual(
            by_route["QFT"]["scoped_negative"],
            "source_defined_restriction_stable_generator_count_zero",
        )

    def test_target_import_false_everywhere(self) -> None:
        self.assertFalse(self.summary["target_import_used"])
        for row in self.summary["routes"]:
            self.assertFalse(row["target_import_used"], row["route"])
        self.assertIn("target_import_used: false", self.text)

    def test_forbidden_global_promotion_phrases_are_not_asserted(self) -> None:
        lower_text = self.text.lower()
        forbidden_assertions = [
            "global_no_go_promoted: true",
            '"global_no_go_promoted": true',
            "verdict: **global no-go",
            "global no-go is promoted",
            "gu is globally blocked by these route-local negatives",
            "no source-natural `k_ig` selector exists",
            "no actual dgu/vz operator identity can exist",
            "no source-defined qft quotient/descent can exist",
        ]
        for phrase in forbidden_assertions:
            self.assertNotIn(phrase, lower_text)

    def test_local_demotions_and_forbidden_promotions_are_recorded(self) -> None:
        demotions = set(self.summary["local_demotions_allowed_now"])
        for expected in [
            "metadata_or_storyboard_as_PTUJ_formula_receipt",
            "Shiab_existence_or_chirality_exclusion_as_K_IG_selector",
            "Oxford_manuscript_UCSD_adjacency_as_actual_DGU_certificate",
            "VZ_replay_without_actual_DGU_identity_witness",
            "UCSD_transcript_as_typed_pure_RS_operator",
            "QFT_finite_extraction_without_source_defined_physical_quotient",
        ]:
            self.assertIn(expected, demotions)

        forbidden = set(self.summary["forbidden_global_promotions"])
        for expected in [
            "no_PTUJ_formula_source_exists",
            "no_source_natural_K_IG_selector_exists",
            "no_actual_DGU_VZ_operator_identity_can_exist",
            "no_UCSD_or_alternate_RS_source_can_supply_d_RS_minus_1",
            "no_source_defined_QFT_quotient_can_exist",
            "GU_is_globally_blocked_by_route_local_negatives",
        ]:
            self.assertIn(expected, forbidden)

    def test_first_missing_global_negative_bundle(self) -> None:
        missing = self.summary["first_missing_global_negative_object"]
        self.assertEqual(missing["id"], "CompleteGlobalNegativeReceiptBundleAfter1302_V1")
        self.assertEqual(missing["status"], "missing")
        self.assertEqual(
            missing["currently_populated_fields"], ["partial_route_local_blocker_matrix"]
        )
        for field in [
            "claim_class",
            "exhaustive_primary_source_inventory",
            "alternate_source_inventory",
            "route_failure_receipts_not_only_blockers",
            "family_identity_failure_matrix",
            "source_natural_rival_coverage",
            "positive_no_target_import_audit",
            "class_boundary_theorem_statement",
            "rollback_conditions",
        ]:
            self.assertIn(field, missing["required_fields"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
