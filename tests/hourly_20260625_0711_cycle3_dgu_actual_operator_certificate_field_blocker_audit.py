#!/usr/bin/env python3
"""Audit ActualDGU01OperatorCertificateFieldBlockerAfter0711_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0711-cycle3-dgu-actual-operator-certificate-field-blocker.md"
)

EXPECTED_FIELDS = {
    "source.operator_action_EL_identity_to_actual_D_GU_epsilon_0_1",
    "rolled_up_domain",
    "rolled_up_codomain",
    "principal_symbol_sigma_1_D_GU_epsilon",
    "coefficients.a",
    "coefficients.b",
    "coefficients.lambda_d",
    "Phi_d_Phi_F_split",
    "Q_projectors_import_maps",
    "target_import_cleanliness",
    "family_identity",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ActualDGUCertificateFieldBlockerAfter0711Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_decision_flags(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ActualDGU01OperatorCertificateFieldBlockerAfter0711_V1",
        )
        self.assertEqual(
            self.summary["verdict_class"],
            "blocked_missing_actual_dgu_01_operator_certificate_fields",
        )
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["VZ_evasion_promoted"])
        self.assertEqual(self.summary["accepted_actual_certificate_field_count"], 0)
        self.assertEqual(self.summary["accepted_actual_certificate_fields"], [])

    def test_all_certificate_fields_are_present_and_unsatisfied(self) -> None:
        fields = self.summary["certificate_fields"]
        by_name = {row["field"]: row for row in fields}
        self.assertEqual(set(by_name), EXPECTED_FIELDS)

        for field_name, row in by_name.items():
            self.assertFalse(row["satisfied"], field_name)
            self.assertIn(row["status"], {"missing", "missing_for_routing"})
            self.assertTrue(row["reason"])

        self.assertEqual(
            by_name["source.operator_action_EL_identity_to_actual_D_GU_epsilon_0_1"][
                "status"
            ],
            "missing",
        )
        self.assertEqual(
            by_name["target_import_cleanliness"]["status"],
            "missing_for_routing",
        )

    def test_only_context_not_certificate_fields_are_satisfied(self) -> None:
        satisfied = set(self.summary["satisfied_by_current_artifacts"])
        self.assertEqual(
            satisfied,
            {
                "source_locator_context",
                "certificate_schema_known",
                "quarantine_discipline_for_current_artifacts",
            },
        )
        self.assertIn("no listed certificate field is satisfied", self.text)

    def test_first_exact_obstruction_blocks_vz_replay(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_operator_action_EL_identity_to_actual_D_GU_epsilon_0_1",
        )
        self.assertEqual(
            obstruction["field"],
            "source.operator_action_EL_identity_to_actual_D_GU_epsilon_0_1",
        )
        self.assertIn("FC_VZ_proof_replay", obstruction["blocks"])
        blockers = [
            row
            for row in self.summary["certificate_fields"]
            if row.get("first_blocker") is True
        ]
        self.assertEqual(len(blockers), 1)
        self.assertEqual(blockers[0]["field"], obstruction["field"])

    def test_next_object_is_actual_certificate_instance(self) -> None:
        next_object = self.summary["next_object"]
        self.assertEqual(next_object["id"], "ActualDGU01OperatorCertificateInstance_V1")
        self.assertEqual(
            next_object["first_required_field"],
            "source.operator_action_EL_identity_to_actual_D_GU_epsilon_0_1",
        )
        self.assertTrue(
            next_object["proof_replay_allowed_after_object_only_if_all_fields_satisfied"]
        )
        self.assertEqual(set(next_object["required_fields"]), EXPECTED_FIELDS)

    def test_source_artifacts_and_demotion_conditions_cover_assignment(self) -> None:
        derived = {row["artifact"] for row in self.summary["derived_from_source_artifacts"]}
        self.assertIn("RESEARCH-POSTURE.md", derived)
        self.assertIn("process/runbooks/five-lane-frontier-run.md", derived)
        self.assertIn(
            "explorations/hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
            derived,
        )
        self.assertIn(
            "explorations/hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
            derived,
        )
        self.assertIn(
            "explorations/hourly-20260625-0601-cycle2-dgu-bosonic-to-01-sector-identity-firewall.md",
            derived,
        )

        demotion = set(self.summary["falsification_or_demotion_condition"])
        for required in [
            "no_source_emitted_actual_D_GU_epsilon_0_1_operator_action_EL_identity",
            "no_source_emitted_rolled_up_0_1_domain_codomain",
            "no_source_emitted_principal_symbol_or_sufficient_first_order_data",
            "no_source_emitted_coefficients_a_b_lambda_d",
            "no_source_emitted_Phi_d_Phi_F_order_split",
            "no_source_emitted_Q_projectors_import_maps",
            "no_source_clean_target_import_screen_for_routing",
            "no_source_emitted_family_identity_to_actual_DGU_VZ",
        ]:
            self.assertIn(required, demotion)


if __name__ == "__main__":
    unittest.main()
