#!/usr/bin/env python3
"""Audit ProofRestartReadinessFamilyClassifier_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle3-proof-restart-readiness-family-classifier.md"
)

EXPECTED_FAMILIES = {
    "IG",
    "DGU_VZ",
    "RS",
    "QFT",
    "Oxford_visual",
    "Keating_visual",
}

EXPECTED_NEXT_OBJECTS = {
    "IG": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
    "DGU_VZ": "BosonicToDGU01SectorIdentityRule_V1",
    "RS": "ManualImageLevelRSFormulaDiagramAudit_V1",
    "QFT": "QFTAlternatePrimarySourceQueryBundle_V1",
    "Oxford_visual": "OxfordPortalPowerPointFormulaFramePacket_V1",
    "Keating_visual": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing ProofRestartReadinessFamilyClassifier_V1 JSON")
    return json.loads(match.group(1))


class ProofRestartReadinessFamilyClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ProofRestartReadinessFamilyClassifier_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["artifact_id"], "ProofRestartReadinessFamilyClassifier_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle3-proof-restart-readiness-family-classifier.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle3_proof_restart_readiness_family_classifier_audit.py",
        )

    def test_all_families_are_classified(self) -> None:
        self.assertEqual(set(self.summary["families_classified"]), EXPECTED_FAMILIES)
        rows = self.summary["family_rows"]
        self.assertEqual({row["family"] for row in rows}, EXPECTED_FAMILIES)
        self.assertEqual(len(rows), len(EXPECTED_FAMILIES))

    def test_no_receipts_restart_or_claim_promotion(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["proof_restart_ready_count"], 0)
        self.assertFalse(self.summary["claim_promotion_allowed"])
        restart = self.summary["restart_decision"]
        self.assertFalse(restart["any_proof_restart_allowed"])
        self.assertFalse(restart["any_claim_promotion_allowed"])
        self.assertIn("accepted_receipt_count: 0", self.text)
        self.assertIn("proof_restart_ready_count: 0", self.text)
        self.assertIn("claim_promotion_allowed: false", self.text)

    def test_each_family_row_blocks_restart_and_promotion(self) -> None:
        for row in self.summary["family_rows"]:
            self.assertEqual(row["accepted_receipt_count"], 0, row["family"])
            self.assertFalse(row["proof_restart_ready"], row["family"])
            self.assertFalse(row["claim_promotion_allowed"], row["family"])
            self.assertTrue(row["strongest_positive_readiness_attempt"], row["family"])
            self.assertTrue(row["first_obstruction"], row["family"])
            self.assertTrue(row["impact_if_closed"], row["family"])
            self.assertTrue(row["falsification_or_demotion_condition"], row["family"])

    def test_exact_next_object_for_each_family(self) -> None:
        self.assertEqual(self.summary["next_objects_by_family"], EXPECTED_NEXT_OBJECTS)
        rows = {row["family"]: row for row in self.summary["family_rows"]}
        for family, expected_next in EXPECTED_NEXT_OBJECTS.items():
            self.assertEqual(rows[family]["next_object"], expected_next)
            self.assertIn(expected_next, self.text)

    def test_source_fact_contracts_preserve_cycle_context(self) -> None:
        self.assertFalse(self.summary["transition_matrix_available_at_read_time"])
        facts = set(self.summary["source_facts"])
        self.assertIn("cycle1_cycle2_artifacts_used_directly", facts)
        self.assertIn(
            "FIVE_LANE_RUNBOOK_requires_exact_obstruction_and_forbids_hosted_to_selected_promotion",
            facts,
        )
        self.assertIn(
            "RESEARCH_POSTURE_forbids_verdict_inflation_compatibility_as_derivation_and_target_import",
            facts,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
