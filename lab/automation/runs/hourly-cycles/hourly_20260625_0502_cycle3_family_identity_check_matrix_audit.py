#!/usr/bin/env python3
"""Audit FamilyIdentityCheckMatrix_Cycle3_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle3-family-identity-check-matrix.md"
)

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}
REQUIRED_NEXT_WITNESSES = {
    "IG": {
        "id": "AuthorManuscriptIGSelectorIdentityPacket_V1",
        "required_fields": {
            "source_locator",
            "selected_domain",
            "selected_codomain",
            "representation_or_Bianchi_selector_rule",
            "rival_elimination_or_projection_loss_rule",
            "family_identity_to_SourceForcedCodomainSelectorForK_IG",
            "target_import_screen",
        },
    },
    "RS": {
        "id": "AuthorManuscriptRSRuleExtractionCandidate_V1",
        "required_fields": {
            "exact_formula_or_diagram_cell",
            "rule_kind",
            "source_space",
            "target_space",
            "degree_or_complex_slot",
            "field_component",
            "family_identity_to_d_RS_minus_1",
        },
    },
    "QFT": {
        "id": "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1",
        "required_fields": {
            "source_locator",
            "emitted_rule_type",
            "domain_equivalent_to_F_phys_b_O",
            "target_equivalent_to_K_b",
            "explicit_map",
            "local_mode_records",
            "import_screen",
        },
    },
    "DGU_VZ": {
        "id": "ActualDGU01OperatorReceiptCandidateFromAuthorManuscript_V1",
        "required_fields": {
            "source_formula_locator",
            "emitted_operator_or_action_or_EL",
            "sector_rule_0_1",
            "domain_codomain",
            "principal_symbol",
            "coefficient_packet",
            "family_identity_check",
            "target_import_check",
        },
    },
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing FamilyIdentityCheckMatrix_Cycle3_V1 JSON")
    return json.loads(match.group(1))


class FamilyIdentityCheckMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row
            for row in cls.summary["family_identity_matrix"]  # type: ignore[index]
        }

    def test_artifact_identity(self) -> None:
        self.assertEqual(self.summary["artifact"], "FamilyIdentityCheckMatrix_Cycle3_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle3-family-identity-check-matrix.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle3_family_identity_check_matrix_audit.py",
        )
        self.assertEqual(identity["artifact_id"], "FamilyIdentityCheckMatrix_Cycle3_V1")

    def test_all_four_families_present(self) -> None:
        self.assertEqual(set(self.summary["families_checked"]), REQUIRED_FAMILIES)
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        self.assertEqual(self.summary["family_count"], 4)
        self.assertEqual(self.summary["candidate_row_count"], 5)

    def test_zero_identity_checks_passed_and_no_receipts_accepted(self) -> None:
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        for family, row in self.rows.items():
            self.assertFalse(row["family_identity_check_passed"], family)
            self.assertFalse(row["accepted_receipt"], family)
            self.assertFalse(row["proof_restart_allowed"], family)

    def test_proof_restart_and_claim_promotion_are_blocked(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(next_step["step_type"], "sequential_source_identity_pass")
        self.assertFalse(next_step["proof_restart_currently_allowed"])
        self.assertEqual(
            next_step["restart_condition"],
            "family_specific_source_receipt_and_family_mathematical_identity_both_pass",
        )

    def test_no_global_no_go_is_promoted(self) -> None:
        self.assertFalse(self.summary["global_no_go_established"])
        self.assertEqual(
            self.summary["negative_result_scope"],
            "cycle_2_candidate_receipt_rows_only",
        )
        forbidden = self.summary["forbidden_promotions"]
        self.assertFalse(forbidden["global_no_go_theorem_established"])
        self.assertIn("does **not** promote a global no-go theorem", self.text)

    def test_required_objects_are_exact(self) -> None:
        self.assertEqual(
            self.rows["IG"]["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        self.assertEqual(
            self.rows["RS"]["required_object"],
            "source.action_or_operator for d_RS,-1",
        )
        self.assertEqual(
            self.rows["QFT"]["required_object"],
            "P_fin^b: F_phys^b(O) -> K_b",
        )
        self.assertEqual(
            self.rows["DGU_VZ"]["required_object"],
            "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
        )

    def test_first_missing_witnesses_are_present(self) -> None:
        expected = {
            "IG": "ManuscriptRepresentationTheoryBianchiSelectorForShiab_V1",
            "RS": "SourceEmittedRSMinusOneRule_V1",
            "QFT": "SourceProjectorPFinBFromAuthorManuscript",
            "DGU_VZ": "identity_to_actual_D_GU_epsilon_0_1_action_operator_or_EL",
        }
        for family, witness_id in expected.items():
            witness = self.rows[family]["first_missing_identity_witness"]
            self.assertEqual(witness["id"], witness_id, family)
            self.assertTrue(witness["missing"], family)
            self.assertIn("description", witness, family)

    def test_required_next_witness_fields(self) -> None:
        for family, expected in REQUIRED_NEXT_WITNESSES.items():
            witness = self.rows[family]["constructive_next_witness"]
            self.assertEqual(witness["id"], expected["id"], family)
            self.assertTrue(
                expected["required_fields"].issubset(set(witness["required_fields"])),
                family,
            )

    def test_forbidden_family_promotions_are_false(self) -> None:
        forbidden = self.summary["forbidden_promotions"]
        for key in [
            "IG_K_IG_selected",
            "RS_d_RS_minus_1_source_derived",
            "QFT_P_fin_b_supplied",
            "DGU_actual_D_GU_epsilon_0_1_identified",
            "VZ_evasion_or_closure_established",
            "RS_rank_or_generation_recovery_established",
            "finite_QFT_or_Bell_CHSH_established",
            "dark_energy_or_FLRW_recovery_established",
        ]:
            self.assertFalse(forbidden[key], key)


if __name__ == "__main__":
    unittest.main(verbosity=2)
