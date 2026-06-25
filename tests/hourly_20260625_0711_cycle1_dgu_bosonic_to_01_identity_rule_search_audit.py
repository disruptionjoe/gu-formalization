#!/usr/bin/env python3
"""Audit BosonicToDGU01SectorIdentityRuleSearch_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGUBosonicTo01IdentityRuleSearchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_and_manuscript_source_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "BosonicToDGU01SectorIdentityRuleSearch_V1",
        )
        source = self.summary["manuscript_source"]
        self.assertEqual(source["file"], "Geometric_UnityDraftApril1st2021.pdf")
        self.assertEqual(source["source_family"], "GU-MEDIA-2021-DRAFT-RELEASE")
        self.assertEqual(source["pages"], 69)
        self.assertEqual(source["size_bytes"], 2087649)
        self.assertIn("sections_8_10_pdf_pages_41_48", source["target_windows_checked"])
        self.assertIn("section_12_pdf_pages_54_62", source["target_windows_checked"])

    def test_required_dgu_vz_object_and_sector_rule_status(self) -> None:
        self.assertEqual(
            self.summary["required_dgu_vz_object"],
            "actual D_GU^epsilon 0/1 action/operator/EL/principal-symbol data",
        )
        self.assertEqual(
            self.summary["sought_rule"],
            "BosonicToDGU01SectorIdentityRule_V1",
        )
        self.assertEqual(self.summary["sector_rule_status"], "missing")
        self.assertIn("D_GU^epsilon 0/1", self.text)
        self.assertIn("BosonicToDGU01SectorIdentityRule_V1", self.text)

    def test_manuscript_literal_search_does_not_emit_identity_names(self) -> None:
        hits = self.summary["manuscript_source"]["required_literal_hits"]
        for key in ("D_GU", "DGU", "D^epsilon", "D^\\epsilon", "0/1", "domain"):
            self.assertEqual(hits[key], 0)
        adjacent = self.summary["manuscript_source"]["adjacent_positive_hits"]
        self.assertGreater(adjacent["Dirac_pages"], 0)
        self.assertGreater(adjacent["Shiab_pages"], 0)

    def test_source_object_identity_rows_are_not_accepted(self) -> None:
        rows = self.summary["source_objects_derived"]
        self.assertGreaterEqual(len(rows), 6)
        names = {row["object"] for row in rows}
        self.assertIn("fermionic Dirac-like slash_D_omega operator display", names)
        self.assertIn("I_1^B, T_omega, bosonic action and Euler-Lagrange setup", names)
        for row in rows:
            self.assertEqual(row["identity_to_actual_D_GU_epsilon_0_1"], "missing")
            self.assertFalse(row["accepted"])

    def test_promotion_fields_remain_missing(self) -> None:
        fields = self.summary["promotion_fields"]
        self.assertEqual(fields["sector_rule"], "missing")
        self.assertIn("missing", fields["domain"])
        self.assertIn("missing", fields["codomain"])
        self.assertIn("missing", fields["principal_symbol"])
        coeffs = fields["coefficient_packet"]
        self.assertEqual(coeffs["status"], "missing")
        self.assertEqual(coeffs["a"], "missing")
        self.assertEqual(coeffs["b"], "missing")
        self.assertEqual(coeffs["lambda_d"], "missing")
        projectors = fields["projectors"]
        self.assertEqual(projectors["status"], "missing")
        self.assertEqual(projectors["Q_in"], "missing")
        self.assertEqual(projectors["Q_out"], "missing")
        self.assertEqual(fields["target_import_cleanliness"], "missing")
        self.assertEqual(fields["family_identity"], "missing")

    def test_zero_receipts_and_no_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("Accepted receipt count: `0`", self.text)
        self.assertIn("Proof restart allowed: `false`", self.text)

    def test_obstruction_and_next_object_are_explicit(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_emitted_identity_from_bosonic_action_EL_locators_to_actual_D_GU_epsilon_0_1_operator_action_EL_principal_symbol_data",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "BosonicToDGU01SectorIdentityRule_V1",
        )
        self.assertIn("coefficient packet", obstruction["description"])
        self.assertIn("family identity", obstruction["description"])
        next_step = self.summary["next_meaningful_proof_or_source_step"]
        self.assertEqual(next_step["object"], "ActualDGU01OperatorCertificateInstance_V1")
        self.assertEqual(
            next_step["first_required_field"],
            "source.operator_source_primary_action_or_EL_with_identity_to_D_GU_epsilon",
        )

    def test_demotion_conditions_include_coefficient_and_projector_failures(self) -> None:
        demotion = set(self.summary["falsification_or_demotion_condition"])
        self.assertIn("no_source_emitted_BosonicToDGU01SectorIdentityRule_V1", demotion)
        self.assertIn("no_source_emitted_actual_D_GU_epsilon_0_1_formula", demotion)
        self.assertIn("no_source_emitted_coefficient_packet_a_b_lambda_d", demotion)
        self.assertIn("no_source_emitted_Q_in_Q_out_projectors", demotion)
        self.assertIn("lambda_d_zero_or_Phi_d_absent_in_later_valid_source_packet", demotion)


if __name__ == "__main__":
    unittest.main()
