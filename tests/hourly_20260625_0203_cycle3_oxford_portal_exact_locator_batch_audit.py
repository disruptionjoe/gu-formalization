#!/usr/bin/env python3
"""Audit OxfordPortalExactLocatorBatch_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0203-cycle3-oxford-portal-exact-locator-batch.md"
)

REQUIRED_COMPONENTS = {
    "oxford_2013_transcript": "Oxford transcript",
    "portal_special_shared_oxford_substance": "Portal Special shared Oxford substance",
    "portal_special_preface": "Portal-only preface",
    "portal_special_postlecture": "Portal-only postlecture",
}

REQUIRED_FAMILIES = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

REQUIRED_SCHEMA_FIELDS = {
    "batch_id",
    "source_id",
    "source_component",
    "component_availability",
    "family",
    "required_object",
    "query_terms",
    "exact_locator",
    "exact_fragment_or_absence",
    "emitted_object_type",
    "emitted_formula_or_rule",
    "starter_row_used",
    "starter_row_is_accepted_receipt",
    "target_data_seen",
    "import_status",
    "acceptance_status",
    "proof_restart_allowed",
    "promotion_allowed",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing OxfordPortalExactLocatorBatch_V1 JSON")
    return json.loads(match.group(1))


class OxfordPortalExactLocatorBatchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "OxfordPortalExactLocatorBatch_V1")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_BATCH_SPECIFIED_ZERO_ACCEPTED_RECEIPTS",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["batch_id"], "OxfordPortalExactLocatorBatch_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0203-cycle3-oxford-portal-exact-locator-batch.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0203_cycle3_oxford_portal_exact_locator_batch_audit.py",
        )

    def test_source_components_include_required_surfaces(self) -> None:
        components = {
            row["component_id"]: row for row in self.summary["source_components"]
        }
        self.assertEqual(set(components), set(REQUIRED_COMPONENTS))
        for component_id, label in REQUIRED_COMPONENTS.items():
            self.assertEqual(components[component_id]["label"], label)
            self.assertFalse(components[component_id]["accepted_receipt"])

        self.assertEqual(
            components["portal_special_preface"]["local_availability"],
            "missing_not_locally_mined",
        )
        self.assertEqual(
            components["portal_special_postlecture"]["local_availability"],
            "missing_not_locally_mined",
        )
        self.assertFalse(self.summary["portal_only_preface_postlecture_locally_mined"])

    def test_accepted_receipt_count_is_zero(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["negative_receipt_count"], 0)
        self.assertIn("Current accepted receipts are zero.", self.text)

    def test_query_plan_covers_all_four_families(self) -> None:
        query_plan = {row["family"]: row for row in self.summary["query_plan"]}
        self.assertEqual(set(query_plan), set(REQUIRED_FAMILIES))
        for family, required_object in REQUIRED_FAMILIES.items():
            self.assertEqual(query_plan[family]["required_object"], required_object)
            self.assertGreaterEqual(len(query_plan[family]["query_terms"]), 4)
            self.assertFalse(query_plan[family]["starter_rows_are_accepted_receipts"])

    def test_local_starter_rows_are_not_accepted_receipts(self) -> None:
        starter_rows = self.summary["local_starter_rows"]
        self.assertTrue(starter_rows["useful"])
        self.assertFalse(starter_rows["accepted_receipts"])
        self.assertIn("observerse", starter_rows["anchors"])
        self.assertIn("pi_projection_operator", starter_rows["anchors"])
        self.assertIn("Local Oxford starter rows are useful", self.text)

    def test_candidate_schema_and_negative_requirements(self) -> None:
        self.assertEqual(set(self.summary["candidate_row_schema"]), REQUIRED_SCHEMA_FIELDS)
        requirements = self.summary["negative_row_requirements"]
        true_requirements = [
            "complete_acquired_source_component",
            "declared_component_scope",
            "query_log_preserved",
            "family_specific_terms_and_notation_variants_preserved",
            "inspected_hits_and_false_positive_decisions_preserved",
            "exact_required_object_absence_recorded",
            "target_import_excluded",
        ]
        for field in true_requirements:
            self.assertIs(requirements[field], True, field)
        self.assertFalse(requirements["promotion_allowed"])
        self.assertFalse(requirements["proof_restart_allowed"])

    def test_proof_restart_is_blocked_and_no_claim_promoted(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertTrue(self.summary["no_claim_promotion"])
        for key, value in self.summary["no_claim_promotions"].items():
            self.assertFalse(value, key)
        self.assertIn("Proof restart remains blocked", self.text)
        self.assertIn("No GU claim is promoted.", self.text)

    def test_forbidden_promotions_include_required_blocks(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertIn("Oxford starter rows are accepted receipts", forbidden)
        self.assertIn("Portal Special preface/postlecture is locally mined", forbidden)
        self.assertIn("IG selects K_IG", forbidden)
        self.assertIn("RS source-derived d_RS,-1 is established", forbidden)
        self.assertIn("QFT P_fin^b is supplied", forbidden)
        self.assertIn(
            "DGU/VZ actual D_GU^epsilon 0/1 is identified",
            forbidden,
        )
        self.assertIn("Proof restart is allowed", forbidden)


if __name__ == "__main__":
    unittest.main()
