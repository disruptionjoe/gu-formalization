#!/usr/bin/env python3
"""Audit the DGU01OperatorSourceReceipt_V1 artifact.

This is a structural receipt audit. It does not prove or disprove VZ closure.
It checks that the artifact parses as a smaller source-receipt gate, rejects
typed-spine-only material as a primary source, keeps non-claims explicit, and
allows ActualDGU01OperatorCertificateInstance_V1 only after receipt acceptance.
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
    / "hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_RECEIPT_FIELDS = {
    "source_locator",
    "source_kind",
    "source_status",
    "operator_source_primary_action_or_EL",
    "operator_emitted",
    "principal_symbol_emitted",
    "coefficients_source_derived",
    "typed_spine_candidate",
    "typed_spine_candidate_is_primary_source",
    "typed_spine_match",
    "extra_first_order_terms_ledger",
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
    "coordinate_convention_fixed",
    "extra_first_order_terms_listed_or_kernel_audited",
    "typed_spine_candidate_not_used_as_primary_source",
}

REQUIRED_ROLLBACKS = {
    "operator_source_primary_action_or_EL_missing",
    "typed_spine_candidate_as_primary_source",
    "typed_spine_only",
    "reconstruction_algebra_only",
    "actual_operator_formula_absent",
    "actual_D_GU_0_1_block_absent",
    "actual_operator_differs_from_D_roll_typed_spine",
    "rolled_up_domain_or_codomain_mismatch",
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
    r'"can_accept_source_receipt"\s*:\s*true',
    r'"can_emit_actual_dgu_certificate_instance"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing DGU source receipt artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGU01OperatorSourceReceiptAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_receipt_verdict_rejects_current_sources(self) -> None:
        self.assertEqual(self.summary["artifact"], "DGU01OperatorSourceReceipt_V1")
        self.assertEqual(self.summary["verdict_class"], "underdefined_blocked")
        self.assertEqual(
            self.summary["receipt_decision"],
            "REJECT_NO_PRIMARY_ACTION_OR_EL",
        )
        self.assertFalse(self.summary["can_accept_source_receipt"])
        self.assertFalse(self.summary["can_emit_actual_dgu_certificate_instance"])
        self.assertEqual(
            self.summary["first_exact_missing_field"],
            "operator_source_primary_action_or_EL",
        )
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
        )

    def test_receipt_fields_are_present_and_unaccepted(self) -> None:
        fields = self.summary["receipt_fields"]
        missing = REQUIRED_RECEIPT_FIELDS - set(fields)
        self.assertFalse(missing, f"missing receipt fields: {sorted(missing)}")
        self.assertIsNone(fields["source_locator"])
        self.assertEqual(fields["source_kind"], "missing")
        self.assertEqual(fields["source_status"], "missing")
        self.assertIsNone(fields["operator_source_primary_action_or_EL"])
        self.assertIsNone(fields["operator_emitted"])
        self.assertIsNone(fields["principal_symbol_emitted"])
        self.assertFalse(fields["typed_spine_candidate_is_primary_source"])
        self.assertEqual(fields["typed_spine_match"], "no_operator_emitted")

    def test_typed_spine_candidate_is_rejected_as_primary_source(self) -> None:
        candidates = {
            candidate["candidate"]: candidate
            for candidate in self.summary["source_candidates_checked"]
        }
        self.assertIn("typed_spine_candidate", candidates)
        typed = candidates["typed_spine_candidate"]
        self.assertEqual(typed["status"], "typed_spine_candidate")
        self.assertFalse(typed["accepted_as_primary_source_receipt"])
        self.assertIn("canonical proposal", typed["reason"])

        algebra = candidates["D_roll_reconstruction_algebra"]
        self.assertEqual(algebra["status"], "reconstruction_algebra")
        self.assertFalse(algebra["accepted_as_primary_source_receipt"])

        primary = candidates["primary_GU_action_or_operator_or_EL"]
        self.assertEqual(primary["status"], "missing")
        self.assertFalse(primary["accepted_as_primary_source_receipt"])

    def test_strongest_positive_result_remains_candidate_only(self) -> None:
        positive = self.summary["strongest_positive_result"]
        self.assertIn("D_roll^epsilon", positive["candidate"])
        self.assertIn("sigma_1(D_roll^epsilon)", positive["principal_candidate"])
        self.assertEqual(positive["candidate_status"], "coherent_typed_spine_candidate")
        self.assertTrue(positive["requires_primary_source_receipt"])
        self.assertTrue(positive["requires_actual_sigma_1_D_GU"])
        self.assertTrue(positive["requires_source_derived_a_b_lambda_d"])
        self.assertTrue(positive["requires_extra_first_order_terms_audited"])
        self.assertFalse(positive["accepted_as_receipt"])

    def test_acceptance_conditions_are_explicit(self) -> None:
        conditions = set(self.summary["receipt_acceptance_conditions"])
        missing = REQUIRED_ACCEPTANCE_CONDITIONS - conditions
        self.assertFalse(missing, f"missing acceptance conditions: {sorted(missing)}")

    def test_actual_certificate_instance_is_gated_on_acceptance(self) -> None:
        self.assertEqual(
            self.summary["constructive_next_object"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )
        self.assertTrue(
            self.summary["constructive_next_object_allowed_only_if_receipt_accepts"]
        )
        self.assertIn(
            "emit_ActualDGU01OperatorCertificateInstance_V1_only_if_receipt_accepts",
            self.summary["next_meaningful_step"],
        )

    def test_explicit_non_claims_are_false_and_not_promoted(self) -> None:
        for key, value in self.summary["explicit_non_claims"].items():
            self.assertIs(value, False, f"{key} should remain false")

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_rollback_conditions_are_complete(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        missing = REQUIRED_ROLLBACKS - rollbacks
        self.assertFalse(missing, f"missing rollback conditions: {sorted(missing)}")

    def test_next_steps_are_source_extraction_not_matrix_repetition(self) -> None:
        steps = set(self.summary["next_meaningful_step"])
        self.assertIn("locate_primary_GU_action_operator_or_EL_source", steps)
        self.assertIn("extract_actual_D_GU_epsilon_0_1_operator", steps)
        self.assertIn("compute_sigma_1_D_GU_epsilon_from_source", steps)
        self.assertIn("derive_source_coefficients_a_b_lambda_d", steps)
        self.assertIn("list_or_audit_extra_first_order_terms", steps)


if __name__ == "__main__":
    unittest.main(verbosity=2)
