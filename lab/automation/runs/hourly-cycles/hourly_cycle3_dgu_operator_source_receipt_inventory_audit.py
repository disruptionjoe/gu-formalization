#!/usr/bin/env python3
"""Audit the Cycle 3 DGU operator source receipt inventory.

This audit checks the structural contract of the decision artifact. It does not
prove VZ closure. It verifies that the artifact distinguishes source receipt
from typed-spine candidate, refuses to emit an actual certificate instance, and
names the exact first obstruction.
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
    / "hourly-cycle3-dgu-operator-source-receipt-inventory-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. Impact On GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_SOURCES = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-cycle1-effect-typed-witness-vz-operator-2026-06-25.md",
    "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md",
    "explorations/hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md",
    "explorations/gu-typed-operator-action-spine-2026-06-24.md",
    "explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md",
}

REQUIRED_ACCEPTANCE_CONDITIONS = {
    "primary_GU_action_or_operator_or_EL_locator_present",
    "D_GU_epsilon_0_1_formula_emitted",
    "sigma_1_D_GU_epsilon_computed_from_source",
    "a_b_lambda_d_source_derived",
    "Phi_2_Phi_d_Phi_F_order_split_preserved",
    "Q_in_Q_out_projectors_fixed",
    "extra_first_order_terms_listed",
}

REQUIRED_ROLLBACKS = {
    "operator_source_primary_action_or_EL_missing",
    "typed_spine_only",
    "reconstruction_only",
    "actual_operator_formula_absent",
    "actual_operator_differs_from_D_roll_typed_spine",
    "coefficient_lambda_d_zero",
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
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source receipt inventory artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGUOperatorSourceReceiptInventoryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_sources_are_named(self) -> None:
        for source in REQUIRED_SOURCES:
            self.assertIn(source, self.text)

    def test_verdict_blocks_emission(self) -> None:
        self.assertEqual(self.summary["artifact"], "DGU01OperatorSourceReceiptInventory_V1")
        self.assertEqual(self.summary["verdict_class"], "underdefined_blocked")
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_BLOCKED__NO_SOURCE_RECEIPT_FOR_ACTUAL_DGU01_OPERATOR",
        )
        self.assertFalse(self.summary["can_emit_actual_dgu_certificate_instance"])
        self.assertFalse(self.summary["can_emit_source_receipt"])
        self.assertEqual(
            self.summary["inventory_decision"],
            "REJECT_TYPED_SPINE_ONLY_AS_SOURCE_RECEIPT",
        )

    def test_first_obstruction_is_exact_source_field(self) -> None:
        expected = "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL"
        self.assertEqual(self.summary["first_exact_obstruction"], expected)
        self.assertEqual(self.summary["source_receipt_field"], "operator_source_primary_action_or_EL")
        self.assertIn(expected, self.text)

    def test_inventory_distinguishes_receipt_from_typed_spine(self) -> None:
        inventory = {entry["object"]: entry for entry in self.summary["source_inventory"]}
        self.assertEqual(inventory["D_roll_typed_spine_candidate"]["status"], "typed_spine_candidate")
        self.assertFalse(
            inventory["D_roll_typed_spine_candidate"][
                "can_cite_for_operator_source_primary_action_or_EL"
            ]
        )
        self.assertEqual(inventory["typed_E_block_algebra"]["status"], "algebra_backend")
        self.assertFalse(
            inventory["typed_E_block_algebra"][
                "can_cite_for_operator_source_primary_action_or_EL"
            ]
        )
        self.assertEqual(inventory["primary_GU_action_or_EL_for_D_GU_0_1_sector"]["status"], "missing")

    def test_strongest_positive_construction_remains_conditional(self) -> None:
        construction = self.summary["strongest_positive_construction"]
        self.assertIn("D_roll^epsilon", construction["candidate"])
        self.assertTrue(construction["requires_primary_source_receipt"])
        self.assertTrue(construction["requires_actual_sigma_1_D_GU"])
        self.assertTrue(construction["requires_source_derived_a_b_lambda_d"])
        self.assertTrue(construction["requires_extra_first_order_terms_audited"])
        self.assertEqual(construction["current_status"], "candidate_only_not_receipt")

    def test_next_objects_are_ordered(self) -> None:
        self.assertEqual(self.summary["constructive_next_object"], "DGU01OperatorSourceReceipt_V1")
        self.assertEqual(
            self.summary["follow_on_object_if_accepted"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )
        self.assertIn("DGU01OperatorSourceReceipt_V1", self.text)
        self.assertIn("ActualDGU01OperatorCertificateInstance_V1", self.text)

    def test_acceptance_conditions_and_rollback_conditions_are_complete(self) -> None:
        acceptance = set(self.summary["receipt_acceptance_conditions"])
        self.assertFalse(REQUIRED_ACCEPTANCE_CONDITIONS - acceptance)

        rollbacks = set(self.summary["rollback_conditions"])
        self.assertFalse(REQUIRED_ROLLBACKS - rollbacks)

    def test_forbidden_claims_are_false_and_not_promoted(self) -> None:
        for key, value in self.summary["explicit_non_claims"].items():
            self.assertIs(value, False, f"{key} should remain false")

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_next_steps_are_computational(self) -> None:
        steps = set(self.summary["next_meaningful_step"])
        self.assertIn("build_DGU01OperatorSourceReceipt_V1", steps)
        self.assertIn("locate_primary_GU_action_operator_or_EL_source", steps)
        self.assertIn("extract_D_GU_epsilon_0_1_operator", steps)
        self.assertIn("compute_sigma_1_D_GU_epsilon_from_source", steps)
        self.assertIn("only_then_emit_ActualDGU01OperatorCertificateInstance_V1", steps)


if __name__ == "__main__":
    unittest.main(verbosity=2)
