#!/usr/bin/env python3
"""Audit the 2021 manuscript DGU/VZ operator receipt candidate search.

This audit checks that the artifact searched the required term family, recorded
page-level candidate locators, accepted no receipt without the target source
object, kept target-import flags false, avoided VZ/dark-energy promotion, and
kept proof restart blocked unless both source acceptance and identity gates pass.
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
    / "hourly-20260625-0301-cycle1-manuscript-dgu-vz-operator-receipt-candidates.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_SEARCHED_TERMS = {
    "action",
    "operator",
    "Euler",
    "Lagrange",
    "equation",
    "field equation",
    "alpha",
    "theta",
    "pi",
    "epsilon",
    "curvature",
    "divergence",
    "Bianchi",
    "inhomogeneous gauge group",
    "D_GU",
    "D_GU^epsilon",
    "deformation",
    "first order",
    "second order",
    "principal symbol",
}

REQUIRED_CANDIDATES = {
    "MS2021-NO-DGU-LITERAL",
    "MS2021-SHIAB-FAMILY",
    "MS2021-BOSONIC-ACTION-EL",
    "MS2021-FERMIONIC-DIRACLIKE",
    "MS2021-DEFORMATION-COMPLEX",
    "MS2021-EQUATION-SUMMARY",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"VZ evasion:\s*(claimed|established|true)",
    r"dark-energy recovery:\s*(claimed|established|true)",
    r"FLRW proof status:\s*(improved|closed|true)",
    r"DGU/VZ actual D_GU\^epsilon 0/1:\s*(identified|claimed|true)",
    r"proof restart:\s*(allowed|true)",
    r'"proof_restart_allowed"\s*:\s*true',
    r'"accepted_receipt_count"\s*:\s*[1-9]',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing manuscript candidate artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ManuscriptDguVzOperatorReceiptCandidateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ManuscriptDGU_VZ_OperatorReceiptCandidateSearch_V1",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertEqual(
            self.summary["target_object"],
            "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
        )
        self.assertEqual(self.summary["source_pdf"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(self.summary["pdf_page_count_extracted"], 69)

    def test_required_search_terms_were_checked(self) -> None:
        searched = set(self.summary["searched_terms"])
        missing = REQUIRED_SEARCHED_TERMS - searched
        self.assertFalse(missing, f"missing searched terms: {sorted(missing)}")
        results = self.summary["searched_term_results"]
        self.assertFalse(results["D_GU"]["found"])
        self.assertFalse(results["D_GU^epsilon"]["found"])
        self.assertFalse(results["principal symbol"]["found"])
        self.assertFalse(results["divergence"]["found"])
        self.assertEqual(results["D_GU"]["pages"], [])
        self.assertEqual(results["principal symbol"]["pages"], [])

    def test_candidate_rows_have_page_locators_and_no_acceptance(self) -> None:
        rows = {row["candidate_id"]: row for row in self.summary["candidate_rows"]}
        self.assertEqual(set(rows), REQUIRED_CANDIDATES)
        for candidate_id, row in rows.items():
            self.assertIn("acceptance_status", row, candidate_id)
            self.assertFalse(row["emits_actual_D_GU_epsilon_0_1_operator"], candidate_id)
            self.assertFalse(row["emits_action_or_EL_for_actual_D_GU_epsilon_0_1"], candidate_id)
            self.assertFalse(row["emits_principal_symbol"], candidate_id)
            self.assertEqual(row["target_data_seen"], [], candidate_id)
            self.assertNotIn("accepted", row["acceptance_status"], candidate_id)

        self.assertEqual(rows["MS2021-NO-DGU-LITERAL"]["page_locators"], [])
        for candidate_id in REQUIRED_CANDIDATES - {"MS2021-NO-DGU-LITERAL"}:
            self.assertTrue(rows[candidate_id]["page_locators"], candidate_id)
            for page in rows[candidate_id]["page_locators"]:
                self.assertIsInstance(page, int)
                self.assertGreaterEqual(page, 1)
                self.assertLessEqual(page, 69)

    def test_no_receipt_accepted_and_restart_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["identity_gate_passed"])
        positive = self.summary["strongest_positive_result"]
        self.assertEqual(positive["candidate_id"], "MS2021-BOSONIC-ACTION-EL")
        self.assertFalse(positive["accepted_as_receipt"])
        self.assertIn("not the actual D_GU^epsilon", positive["reason"])

    def test_target_import_flags_are_false(self) -> None:
        flags = self.summary["target_import_flags"]
        expected = {
            "VZ_used_to_select_operator",
            "dark_energy_used_to_select_operator",
            "DESI_used_to_select_operator",
            "FLRW_used_to_select_operator",
            "downstream_target_success_used_as_source_evidence",
        }
        self.assertEqual(set(flags), expected)
        for key, value in flags.items():
            self.assertIs(value, False, key)

    def test_forbidden_promotions_remain_false_and_absent_as_positive_claims(self) -> None:
        for key, value in self.summary["forbidden_promotions"].items():
            self.assertIs(value, False, key)
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion matched: {pattern}",
            )

    def test_proof_restart_requires_accepted_source_and_identity_gate(self) -> None:
        allowed_if = set(self.summary["constructive_next_object_allowed_only_if"])
        required = {
            "source_emits_actual_D_GU_epsilon_0_1_operator",
            "source_emits_or_derives_action_or_EL_for_that_operator",
            "source_emits_or_allows_computation_of_sigma_1_D_GU_epsilon",
            "target_import_flags_all_false",
            "family_identity_gate_passed",
        }
        self.assertEqual(allowed_if, required)
        self.assertIn(
            "compute_principal_symbol_only_after_identity_gate",
            self.summary["next_meaningful_step"],
        )
        self.assertIn(
            "keep_proof_restart_blocked_until_receipt_acceptance",
            self.summary["next_meaningful_step"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
