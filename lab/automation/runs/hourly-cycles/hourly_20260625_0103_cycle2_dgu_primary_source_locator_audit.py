#!/usr/bin/env python3
"""Audit the Cycle 2 DGU primary source locator artifact.

This is a structural audit. It checks that the locator parses its JSON summary,
contains the required source decision table, refuses transcript/typed-spine/
reconstruction material as a source receipt, and keeps the forbidden VZ/operator
claims unpromoted.
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
    / "hourly-20260625-0103-cycle2-dgu-primary-source-locator.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Source Locator Decision Table",
    "## 4. Strongest Positive Result",
    "## 5. First Exact Obstruction",
    "## 6. Constructive Next Object",
    "## 7. GU Claim Impact",
    "## 8. Next Proof Step",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_SOURCE_CATEGORIES = {
    "primary_transcript_hint",
    "typed_spine_proposal",
    "reconstruction_algebra",
    "governance_interface_contract",
    "draft_goal",
    "claim_ledger_template",
    "process_source_coverage_note",
    "missing_primary_action_operator_EL_receipt",
}

REQUIRED_DECISION_TABLE_SOURCES = {
    "literature/weinstein-ucsd-2025-04-transcript.md",
    "papers/Transcript into the impossible.md",
    "explorations/generation-count-cl95-dirac-derham-2026-06-22.md",
    "explorations/vz1-schur-complement-symbol-2026-06-23.md",
    "explorations/gu-typed-operator-action-spine-2026-06-24.md",
    "explorations/primary-gu-interface-contract-2026-06-24.md",
    "explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md",
    "sources/claim-ledger.md",
    "sources/media-claim-mining-report-v1.md",
    "primary_GU_action_operator_or_EL_derivation_cell",
}

REQUIRED_ACCEPTANCE_CONDITIONS = {
    "source_locator_present",
    "source_status_primary",
    "operator_source_primary_action_or_EL_present",
    "actual_D_GU_epsilon_0_1_formula_emitted",
    "sigma_1_D_GU_epsilon_computed_from_source",
    "a_b_lambda_d_source_derived",
    "Phi_2_Phi_d_F_xi_Phi_F_order_split_preserved",
    "Q_in_Q_out_projectors_fixed",
    "extra_first_order_terms_listed_or_kernel_audited",
    "typed_spine_candidate_not_used_as_primary_source",
    "reconstruction_algebra_not_used_as_primary_source",
    "transcript_hint_not_used_as_full_operator_receipt",
}

REQUIRED_ROLLBACKS = {
    "operator_source_primary_action_or_EL_missing",
    "typed_spine_candidate_as_primary_source",
    "typed_spine_only",
    "transcript_hint_only",
    "reconstruction_algebra_only",
    "actual_operator_formula_absent",
    "actual_D_GU_0_1_block_absent",
    "actual_operator_differs_from_D_roll_typed_spine",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "extra_first_order_terms_not_audited",
    "trace_coordinate_and_embedded_coordinate_conventions_mixed",
}

FORBIDDEN_POSITIVE_PATTERNS = [
    r"actual operator identification:\s*claimed",
    r"FC-VZ-1\s+for actual D_GU:\s*closed",
    r"FC-VZ-4\s+for actual section-pulled operator:\s*closed",
    r"VZ evasion:\s*claimed",
    r"hyperbolicity:\s*established",
    r"causality:\s*established",
    r"absence of spacelike characteristics:\s*proved",
    r'"DGU01OperatorSourceReceipt_V1_can_accept"\s*:\s*true',
    r'"can_emit_actual_dgu_certificate_instance"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing DGU primary source locator artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGUPrimarySourceLocatorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_rejects_current_source_locator(self) -> None:
        self.assertEqual(self.summary["artifact"], "DGUPrimarySourceLocator_V1")
        self.assertEqual(self.summary["verdict_class"], "underdefined_blocked")
        self.assertEqual(
            self.summary["locator_decision"],
            "REJECT_NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR",
        )
        self.assertFalse(self.summary["DGU01OperatorSourceReceipt_V1_can_accept"])
        self.assertFalse(self.summary["can_emit_actual_dgu_certificate_instance"])

    def test_first_missing_source_receipt_is_exact(self) -> None:
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
        )
        self.assertEqual(
            self.summary["first_missing_source_receipt"],
            "operator_source_primary_action_or_EL",
        )
        self.assertIn("operator_source_primary_action_or_EL", self.text)

    def test_source_categories_are_complete(self) -> None:
        categories = set(self.summary["source_categories"])
        missing = REQUIRED_SOURCE_CATEGORIES - categories
        self.assertFalse(missing, f"missing source categories: {sorted(missing)}")

    def test_source_locator_decision_table_is_complete_and_negative(self) -> None:
        table = self.summary["source_locator_decision_table"]
        sources = {entry["source"] for entry in table}
        missing = REQUIRED_DECISION_TABLE_SOURCES - sources
        self.assertFalse(missing, f"missing decision table sources: {sorted(missing)}")

        for entry in table:
            self.assertIn("category", entry)
            self.assertIn("locator_result", entry)
            self.assertIn("decision_reason", entry)
            self.assertIs(entry["emits_actual_D_GU_epsilon_0_1_operator"], False)
            self.assertIs(entry["acceptable_for_DGU01OperatorSourceReceipt_V1"], False)

        missing_source = next(
            entry
            for entry in table
            if entry["source"] == "primary_GU_action_operator_or_EL_derivation_cell"
        )
        self.assertEqual(missing_source["locator_result"], "not_found")
        self.assertEqual(missing_source["category"], "missing_primary_action_operator_EL_receipt")

    def test_source_kinds_are_not_conflated(self) -> None:
        derivations = self.summary["direct_source_derivations"]
        self.assertGreaterEqual(len(derivations["transcript_hints"]), 3)
        self.assertIn("D_roll_typed_candidate", derivations["typed_spine_proposals"])
        self.assertIn(
            "rolled_up_D_GU_u_psi_formula",
            derivations["reconstruction_algebra"],
        )
        self.assertEqual(derivations["actual_source_receipts"], [])

    def test_strongest_positive_result_is_candidate_not_receipt(self) -> None:
        positive = self.summary["strongest_positive_result"]
        self.assertIn("D_roll^epsilon", positive["candidate"])
        self.assertIn("sigma_1(D_roll^epsilon)", positive["principal_candidate"])
        self.assertEqual(
            positive["candidate_status"],
            "coherent_typed_spine_candidate_not_source_receipt",
        )
        self.assertTrue(positive["requires_primary_source_receipt"])
        self.assertTrue(positive["requires_actual_sigma_1_D_GU"])
        self.assertTrue(positive["requires_source_derived_a_b_lambda_d"])
        self.assertTrue(positive["requires_extra_first_order_terms_audited"])
        self.assertFalse(positive["accepted_as_receipt"])

    def test_acceptance_and_rollback_conditions_are_complete(self) -> None:
        acceptance = set(self.summary["receipt_acceptance_conditions"])
        self.assertFalse(REQUIRED_ACCEPTANCE_CONDITIONS - acceptance)

        rollbacks = set(self.summary["rollback_conditions"])
        self.assertFalse(REQUIRED_ROLLBACKS - rollbacks)

    def test_explicit_nonclaims_are_false_and_not_promoted(self) -> None:
        for key, value in self.summary["explicit_nonclaims"].items():
            self.assertIs(value, False, f"{key} should remain false")

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_next_objects_are_ordered(self) -> None:
        self.assertEqual(self.summary["constructive_next_object"], "DGU01OperatorSourceReceipt_V1")
        self.assertEqual(
            self.summary["follow_on_object_if_accepted"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )
        steps = set(self.summary["next_proof_step"])
        self.assertIn("locate_primary_GU_action_operator_or_EL_source_cell", steps)
        self.assertIn("extract_actual_D_GU_epsilon_0_1_operator", steps)
        self.assertIn("compute_sigma_1_D_GU_epsilon_from_source", steps)
        self.assertIn(
            "emit_ActualDGU01OperatorCertificateInstance_V1_only_after_receipt_acceptance",
            steps,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
