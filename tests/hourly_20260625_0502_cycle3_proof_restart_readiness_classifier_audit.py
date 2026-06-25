#!/usr/bin/env python3
"""Audit the cycle 3 proof-restart readiness classifier."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
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

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ProofRestartReadinessClassifierAfterCycles1And2_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict"], "NO_FAMILY_READY_ZERO_PROOF_RESTARTS")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle3-proof-restart-readiness-classifier.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle3_proof_restart_readiness_classifier_audit.py",
        )

    def test_manuscript_acquisition_recognized_but_insufficient(self) -> None:
        acquisition = self.summary["manuscript_acquisition"]
        self.assertTrue(acquisition["recognized"])
        self.assertEqual(
            acquisition["object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(acquisition["acquisition_state"], "acquired_remote_public_pdf")
        self.assertEqual(acquisition["page_count_observed"], 69)
        self.assertTrue(acquisition["insufficient_for_restart"])
        self.assertIn("not an accepted family receipt", acquisition["reason_insufficient"])

    def test_all_four_families_are_not_ready(self) -> None:
        classifiers = self.summary["family_classifiers"]
        self.assertEqual(set(classifiers), EXPECTED_FAMILIES)
        for family, row in classifiers.items():
            with self.subTest(family=family):
                self.assertFalse(row["ready"])
                self.assertEqual(row["accepted_receipt_count"], 0)
                self.assertFalse(row["proof_restart_allowed"])
                self.assertFalse(row["claim_promotion_allowed"])
                self.assertTrue(row["first_blocker"]["missing"])
                self.assertIn("next_object", row)

    def test_global_gate_has_zero_restarts_and_no_claim_promotion(self) -> None:
        gate = self.summary["global_gate"]
        self.assertEqual(set(gate["families_considered"]), EXPECTED_FAMILIES)
        self.assertEqual(gate["families_ready"], [])
        self.assertEqual(set(gate["families_not_ready"]), EXPECTED_FAMILIES)
        self.assertEqual(gate["accepted_receipt_count_total"], 0)
        self.assertEqual(gate["proof_restart_count"], 0)
        self.assertEqual(gate["proof_restarts_allowed"], [])
        self.assertFalse(gate["claim_promotion_allowed"])
        self.assertTrue(gate["target_import_rule_enforced"])
        self.assertFalse(gate["target_outcome_used_to_select_source_object"])

    def test_specific_blockers_are_preserved(self) -> None:
        classifiers = self.summary["family_classifiers"]
        self.assertEqual(
            classifiers["IG"]["first_blocker"]["id"],
            "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
        )
        self.assertTrue(classifiers["IG"]["keating_sheet_blocker_accounted"])
        self.assertEqual(
            classifiers["RS"]["first_blocker"]["id"],
            "missing_source_emitted_RS_differential_action_or_operator_for_d_RS_minus_1",
        )
        self.assertTrue(classifiers["RS"]["underdefined_row_accounted"])
        self.assertEqual(
            classifiers["QFT"]["first_blocker"]["id"],
            "SourceProjectorPFinBFromAuthorManuscript",
        )
        self.assertTrue(classifiers["QFT"]["scoped_absence_accounted"])
        self.assertEqual(
            classifiers["DGU_VZ"]["first_blocker"]["id"],
            "identity_to_actual_D_GU_epsilon_0_1_action_operator_or_EL",
        )
        self.assertTrue(classifiers["DGU_VZ"]["quarantined_candidate_accounted"])

    def test_forbidden_promotions_include_all_family_restarts(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        for item in [
            "proof_restart_for_IG",
            "proof_restart_for_RS",
            "proof_restart_for_QFT",
            "proof_restart_for_DGU_VZ",
            "accepted_receipt_without_family_identity",
            "target_outcome_selects_source_object",
        ]:
            self.assertIn(item, forbidden)

    def test_sequencing_recommendations(self) -> None:
        sequencing = self.summary["sequencing_recommendation"]
        self.assertEqual(sequencing["mode"], "source_receipt_before_proof_restart")
        self.assertEqual(sequencing["proof_restart_lanes_in_next_batch"], 0)
        self.assertFalse(sequencing["parallel_downstream_proof_allowed"])
        self.assertEqual(
            sequencing["ordered_next_objects"],
            [
                "AuthorManuscriptIGSelectorIdentityPacket_V1",
                "ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1",
                "AuthorManuscriptRSRuleExtractionCandidate_V1",
                "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1",
            ],
        )
        self.assertIn("scoped negative", sequencing["rationale"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
