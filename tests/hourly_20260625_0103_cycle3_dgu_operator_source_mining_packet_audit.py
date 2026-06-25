#!/usr/bin/env python3
"""Audit DGUOperatorSourceMiningPacket_V1.

This structural audit parses the embedded JSON summary and checks that the
packet specifies accepted primary evidence, required receipt fields, typed-spine
rejection, nonclaims, and source-first sequencing before the actual certificate
gate.
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
    / "hourly-20260625-0103-cycle3-dgu-operator-source-mining-packet.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Derivations From Repo Sources",
    "## 3. Accepted Primary Evidence Packet",
    "## 4. Required Formula And Symbol Fields",
    "## 5. Rejection Conditions",
    "## 6. Strongest Positive Packet",
    "## 7. First Exact Obstruction",
    "## 8. Constructive Next Object",
    "## 9. GU Impact",
    "## 10. Next Step",
    "## 11. Machine-Readable JSON Summary",
]

REQUIRED_EVIDENCE_CLASSES = {
    "primary_GU_action",
    "primary_GU_operator_definition",
    "Euler_Lagrange_derivation_from_primary_action",
    "primary_timestamped_formal_statement",
}

REQUIRED_SOURCE_STATUSES = {
    "primary_official_manuscript",
    "primary_official_lecture_or_video",
    "primary_official_transcript",
    "primary_author_derivation_cell",
}

REQUIRED_FORMULA_FIELDS = {
    "domain_0_1",
    "codomain_0_1",
    "D_GU_epsilon_formula",
    "principal_symbol_sigma_1",
    "a_coefficient",
    "b_coefficient",
    "lambda_d",
    "Phi_2",
    "Phi_d",
    "F_xi",
    "Phi_F",
    "Q_in",
    "Q_out",
    "chirality_convention",
    "coordinate_convention",
    "extra_first_order_terms",
    "lower_order_terms",
    "normalization_policy",
}

REQUIRED_REJECTIONS = {
    "typed_spine_only",
    "transcript_hint_only",
    "reconstruction_algebra_only",
    "conditional_VZ_backend_only",
    "operator_formula_absent",
    "actual_0_1_block_absent",
    "principal_symbol_absent_or_not_computable",
    "a_b_lambda_d_not_source_derived",
    "Phi_d_and_Phi_F_conflated",
    "F_xi_derived_from_zero_order_Phi_F",
    "Q_in_Q_out_missing",
    "chirality_convention_missing",
    "coordinate_convention_missing_or_switched",
    "extra_first_order_terms_unlisted",
    "typed_spine_used_as_primary_source",
    "receipt_claim_depends_on_target_VZ_success",
}

REQUIRED_SEQUENCE = [
    "primary_source_locator",
    "exact_source_fragment_or_derivation_cell",
    "emitted_actual_0_1_operator",
    "source_derived_symbol_and_fields",
    "comparison_to_typed_spine",
    "receipt_acceptance_decision",
    "ActualDGU01OperatorCertificateInstance_V1_gate",
]

FORBIDDEN_POSITIVE_PATTERNS = [
    r"actual_D_GU_operator_identification:\s*claimed",
    r"DGU01OperatorSourceReceipt_V1:\s*accepted",
    r"FC_VZ_1_for_actual_D_GU:\s*closed",
    r"FC_VZ_4_for_actual_section_pulled_operator:\s*closed",
    r"VZ_evasion:\s*claimed",
    r"hyperbolicity:\s*claimed",
    r"causality:\s*claimed",
    r"absence_of_spacelike_characteristics:\s*claimed",
    r'"DGU01OperatorSourceReceipt_V1_accepted"\s*:\s*true',
    r'"ActualDGU01OperatorCertificateInstance_V1_opened"\s*:\s*true',
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing DGU source mining packet: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 11\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGUOperatorSourceMiningPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_summary_identity_and_blocker(self) -> None:
        self.assertEqual(self.summary["artifact"], "DGUOperatorSourceMiningPacket_V1")
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_PACKET_READY_NO_ACTUAL_DGU01_SOURCE_RECEIPT",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked_packet_ready")
        self.assertEqual(self.summary["receipt_status"], "not_accepted")
        self.assertEqual(self.summary["packet_status"], "ready_for_source_mining")
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "operator_source_primary_action_or_EL",
        )
        self.assertEqual(
            self.summary["certificate_source_path"],
            "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
        )

    def test_primary_evidence_classes_are_formula_complete(self) -> None:
        rows = self.summary["accepted_primary_evidence_classes"]
        classes = {row["evidence_class"] for row in rows}
        self.assertEqual(classes, REQUIRED_EVIDENCE_CLASSES)
        for row in rows:
            self.assertIs(row["accepted_as_receipt"], True)
            required = row["required_content"]
            self.assertTrue(
                "D_GU^epsilon" in required
                or "0/1 operator" in required
                or "operator/action/EL formula" in required
            )

    def test_source_statuses_and_locator_fields_are_primary_first(self) -> None:
        self.assertEqual(set(self.summary["accepted_source_statuses"]), REQUIRED_SOURCE_STATUSES)
        locator_fields = set(self.summary["minimum_locator_fields"])
        for field in [
            "source_id",
            "source_status",
            "primary_url_or_repo_path",
            "timestamp_or_page_or_equation_locator",
            "exact_context",
            "transcript_or_manuscript_fragment",
            "emitted_formula_or_derivation_cell",
        ]:
            self.assertIn(field, locator_fields)

    def test_required_formula_and_symbol_fields_are_complete(self) -> None:
        fields = set(self.summary["required_formula_symbol_fields"])
        missing = REQUIRED_FORMULA_FIELDS - fields
        self.assertFalse(missing, f"missing formula fields: {sorted(missing)}")

    def test_typed_spine_is_rejected_as_receipt(self) -> None:
        policy = self.summary["typed_spine_policy"]
        self.assertEqual(policy["status"], "comparison_material_only")
        self.assertIn("candidate_shape", policy["accepted_uses"])
        self.assertIn("comparison_target_after_source_extraction", policy["accepted_uses"])
        self.assertIn("primary_source_receipt", policy["rejected_uses"])
        self.assertIn("actual_operator_identification", policy["rejected_uses"])
        self.assertIn("FC_VZ_closure_for_actual_D_GU", policy["rejected_uses"])

    def test_rejection_conditions_cover_typed_spine_and_symbol_failures(self) -> None:
        rejections = set(self.summary["rejection_conditions"])
        missing = REQUIRED_REJECTIONS - rejections
        self.assertFalse(missing, f"missing rejection conditions: {sorted(missing)}")

    def test_strongest_positive_packet_remains_candidate_only(self) -> None:
        packet = self.summary["strongest_positive_packet"]
        self.assertEqual(packet["candidate_id"], "D_roll_typed_spine_candidate")
        self.assertEqual(packet["candidate_status"], "coherent_candidate_not_receipt")
        self.assertIn("D_roll^epsilon", packet["candidate_formula"])
        self.assertIn("sigma_1(D_roll^epsilon)", packet["candidate_principal_symbol"])
        self.assertEqual(
            packet["packet_use"],
            "source_mining_template_and_comparison_target_only",
        )

    def test_source_first_sequence_is_ordered(self) -> None:
        self.assertEqual(self.summary["source_first_sequence"], REQUIRED_SEQUENCE)
        text = "\n".join(self.summary["next_step"])
        self.assertIn("extract_actual_0_1_operator_before_comparison", text)
        self.assertIn("emit_DGU01OperatorSourceReceipt_V1_only_if_accepted", text)
        self.assertIn(
            "open_ActualDGU01OperatorCertificateInstance_V1_only_after_receipt_acceptance",
            text,
        )

    def test_nonclaims_are_false_and_positive_claims_absent(self) -> None:
        for key, value in self.summary["nonclaims"].items():
            self.assertIs(value, False, f"{key} should remain false")

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_receipt_schema_feeds_next_certificate_gate(self) -> None:
        schema = set(self.summary["receipt_schema"])
        for field in [
            "emitted_actual_operator_formula",
            "principal_symbol_sigma_1",
            "coefficients_a_b_lambda_d",
            "order_split_Phi_2_Phi_d_F_xi_Phi_F",
            "projectors_Q_in_Q_out",
            "comparison_to_D_roll",
            "acceptance_decision",
            "next_gate",
        ]:
            self.assertIn(field, schema)

        self.assertEqual(self.summary["constructive_next_object"], "DGU01OperatorSourceReceipt_V1")
        self.assertEqual(
            self.summary["next_gate_if_accepted"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
