#!/usr/bin/env python3
"""Audit AuthorManuscriptDGUVZActionReceiptGate_V1.

This audit parses the embedded JSON summary and checks that the cycle 2 DGU/VZ
receipt gate preserves the acquired manuscript identity while quarantining, not
accepting, the Sections 9/12 action-EL locator.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle2-author-manuscript-dgu-vz-action-receipt-gate.md"
)

EXPECTED_SHA256 = "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo/source surfaces",
    "## 3. Strongest positive DGU/VZ construction attempt",
    "## 4. First exact obstruction or missing proof/source object",
    "## 5. Constructive next object that would remove or test the obstruction",
    "## 6. GU claim impact and forbidden promotions",
    "## 7. Next meaningful proof/source computation",
    "## 8. Intake decision table",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_LOCATOR_FRAGMENTS = {
    "Section 9.1 PDF page 43 equations 9.1-9.3",
    "Section 9.1 PDF page 44 equations 9.4-9.6",
    "Section 9.1 PDF page 45 equations 9.7-9.10",
    "Section 9.2 PDF page 45 equations 9.11-9.15",
    "Section 12.1 PDF page 55 equations 12.2-12.3",
}

REQUIRED_NO_PROMOTIONS = {
    "DGU_actual_operator_identified",
    "DGU_actual_principal_symbol_source_derived",
    "DGU_coefficient_packet_source_derived",
    "VZ_E_block_computed_from_actual_operator",
    "FC_VZ_1_closed",
    "FC_VZ_4_closed",
    "VZ_evasion_or_closure_established",
    "proof_restart_allowed_now",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class AuthorManuscriptDGUVZActionReceiptGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            cls.text = DOC.read_text(encoding="utf-8")
        except FileNotFoundError as exc:
            raise AssertionError(f"missing DGU/VZ receipt gate artifact: {DOC}") from exc
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptDGUVZActionReceiptGate_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            self.summary["verdict"],
            "QUARANTINED_POSITIVE_BOSONIC_ACTION_LOCATOR_ZERO_ACCEPTED_DGU_VZ_RECEIPTS",
        )
        self.assertEqual(self.summary["verdict_class"], "quarantined")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle2-author-manuscript-dgu-vz-action-receipt-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle2_author_manuscript_dgu_vz_action_receipt_gate_audit.py",
        )
        self.assertEqual(
            identity["artifact_id"],
            "AuthorManuscriptDGUVZActionReceiptGate_V1",
        )

    def test_manuscript_object_id_and_hash(self) -> None:
        manuscript = self.summary["manuscript_object"]
        self.assertEqual(manuscript["artifact"], "AcquiredAuthorManuscriptObject_V1")
        self.assertEqual(
            manuscript["object_id"],
            "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
        )
        self.assertEqual(manuscript["source_id"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertIn("Geometric_Unity-Draft-April-1st-2021.pdf", manuscript["url"])
        self.assertEqual(manuscript["sha256"], EXPECTED_SHA256)
        self.assertEqual(manuscript["page_count_observed"], 69)
        self.assertIs(manuscript["local_pdf_verified"], True)

    def test_dgu_vz_required_object_and_candidate_status(self) -> None:
        self.assertEqual(
            self.summary["dgu_vz_required_object"],
            "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
        )
        row = self.summary["candidate_row"]
        self.assertEqual(
            row["row_id"],
            "PrimarySourceReceiptInstance_V1:DGU_VZ:GU-MEDIA-2021-DRAFT-RELEASE:sections-9-12",
        )
        self.assertEqual(row["family"], "DGU_VZ")
        self.assertEqual(row["entry_type"], "PrimarySourceReceiptInstance_V1_candidate")
        self.assertEqual(row["candidate_status"], "quarantined")
        self.assertEqual(
            row["acceptance_status"],
            "not_accepted_missing_family_identity_to_actual_D_GU_epsilon_0_1",
        )
        self.assertEqual(set(row["allowed_statuses"]), {"quarantined", "blocked"})

    def test_target_import_cleanliness_and_no_restart(self) -> None:
        row = self.summary["candidate_row"]
        self.assertIs(row["target_import_clean"], True)
        self.assertEqual(row["target_data_seen"], [])
        self.assertIs(row["proof_restart_allowed"], False)
        self.assertIs(row["claim_promotion_allowed"], False)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["claim_promotion_allowed"], False)

    def test_source_locators_cover_sections_9_and_12(self) -> None:
        locators = {row["locator"] for row in self.summary["source_locators_checked"]}
        self.assertEqual(locators, REQUIRED_LOCATOR_FRAGMENTS)
        joined_relevance = " ".join(
            row["receipt_relevance"] for row in self.summary["source_locators_checked"]
        )
        self.assertIn("family_identity_missing", joined_relevance)
        self.assertIn("not_D_GU_epsilon_0_1", joined_relevance)

    def test_required_object_checks_block_acceptance(self) -> None:
        checks = self.summary["required_object_checks"]
        self.assertEqual(checks["source_primary_action_emitted"], "yes_bosonic_sector_only")
        self.assertIs(checks["operator_emitted"], False)
        self.assertEqual(
            checks["euler_lagrange_equation_emitted"],
            "yes_reduced_or_bosonic_not_identified_as_D_GU_epsilon_0_1",
        )
        self.assertIs(checks["principal_symbol_emitted"], False)
        self.assertIs(checks["coefficient_packet_emitted"], False)
        self.assertIs(checks["D_GU_epsilon_0_1_rule_emitted"], False)
        self.assertIs(checks["family_identity_check_passed"], False)

    def test_first_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "identity_to_actual_D_GU_epsilon_0_1_action_operator_or_EL",
        )
        self.assertIs(obstruction["missing"], True)
        self.assertIn("Sections 9 and 12 emit bosonic action/EL locators", obstruction["description"])
        self.assertIn("principal symbol", obstruction["description"])
        self.assertIn("0/1 rule", obstruction["description"])

    def test_constructive_next_object(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1",
        )
        self.assertEqual(
            next_object["entry_type"],
            "PrimarySourceReceiptInstance_V1_or_NegativePrimarySourceReceiptInstance_V1",
        )
        required_fields = set(next_object["required_fields"])
        self.assertIn("principal_symbol", required_fields)
        self.assertIn("coefficient_packet", required_fields)
        self.assertIn("family_identity_check", required_fields)
        self.assertIn("target_import_check", required_fields)

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("Forbidden promotions", self.text)
        self.assertIn("Do not restart DGU/VZ proof work", self.text)


if __name__ == "__main__":
    unittest.main()
