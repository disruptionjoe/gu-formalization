#!/usr/bin/env python3
"""Audit ActualDGU01OperatorCertificateInstance_V1 minimal field matrix."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0803-cycle2-dgu-actual-operator-certificate-minimal-field-matrix.md"
)

REQUIRED_SOURCES = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-oxford-dgu01-two-anchor-family-identity-gate.md",
    "explorations/hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
    "explorations/hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
    "canon/no-go-class-relative-map.md",
    "literature/weinstein-ucsd-2025-04-transcript.md",
}

REQUIRED_FIELDS = {
    "sector_rule",
    "actual_operator_action_EL_identity",
    "zero_one_domain_codomain",
    "coefficients",
    "Q_sector_projector_import_data",
    "principal_symbol_or_sufficient_first_order_data",
    "family_identity",
    "target_import_screen",
    "VZ_promotion_control",
    "physical_recovery_control",
}

ADJACENT_ONLY_FIELDS = {
    "actual_operator_action_EL_identity",
    "zero_one_domain_codomain",
    "principal_symbol_or_sufficient_first_order_data",
    "target_import_screen",
}

ABSENT_FIELDS = {
    "sector_rule",
    "coefficients",
    "Q_sector_projector_import_data",
    "family_identity",
    "VZ_promotion_control",
    "physical_recovery_control",
}

REQUIRED_DEMOTION_CONDITIONS = {
    "no_source_emitted_sector_rule",
    "no_source_emitted_actual_D_GU_epsilon_0_1_action_operator_EL_identity",
    "no_source_emitted_zero_one_domain_codomain",
    "no_source_emitted_coefficients_a_b_lambda_d",
    "no_source_emitted_Q_in_Q_out_I_Q_in_P_Q_out",
    "no_source_emitted_sigma_1_D_GU_epsilon_or_sufficient_first_order_data",
    "no_source_emitted_family_identity",
    "no_source_emitted_positive_target_import_screen_for_routing",
}

REQUIRED_MISSING_OBJECTS = {
    "source_emitted_sector_rule",
    "source_emitted_actual_D_GU_epsilon_0_1_action_operator_EL_identity",
    "source_emitted_zero_one_domain_codomain",
    "source_emitted_coefficients_a_b_lambda_d",
    "source_emitted_Q_in_Q_out_I_Q_in_P_Q_out",
    "source_emitted_sigma_1_D_GU_epsilon_or_sufficient_first_order_data",
    "source_emitted_family_identity",
    "source_emitted_positive_target_import_screen_for_routing",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section-10 machine-readable JSON summary")
    return json.loads(match.group(1))


class ActualDGU01OperatorCertificateMinimalFieldMatrixAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity_and_sources(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ActualDGU01OperatorCertificateInstance_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0803")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0803-cycle2-dgu-actual-operator-certificate-minimal-field-matrix.md",
        )
        self.assertEqual(set(self.summary["sources_read_first"]), REQUIRED_SOURCES)
        for source in REQUIRED_SOURCES:
            self.assertIn(source, self.text)

    def test_required_certificate_fields_are_all_present(self) -> None:
        rows = self.summary["field_matrix"]
        self.assertEqual(len(rows), self.summary["required_certificate_field_count"])
        by_field = {row["field"]: row for row in rows}
        self.assertEqual(set(by_field), REQUIRED_FIELDS)
        for field in REQUIRED_FIELDS:
            self.assertIn(field, by_field)
            self.assertFalse(by_field[field]["accepted"])

    def test_field_status_counts_are_exact(self) -> None:
        counts = self.summary["field_status_counts"]
        self.assertEqual(
            set(counts["source_located_positive_certificate_fields"]),
            set(),
        )
        self.assertEqual(set(counts["adjacent_only_fields"]), ADJACENT_ONLY_FIELDS)
        self.assertEqual(set(counts["absent_fields"]), ABSENT_FIELDS)
        self.assertEqual(set(counts["accepted_certificate_fields"]), set())
        self.assertEqual(self.summary["source_located_positive_certificate_field_count"], 0)
        self.assertEqual(self.summary["adjacent_only_field_count"], 4)
        self.assertEqual(self.summary["absent_field_count"], 6)
        self.assertEqual(self.summary["accepted_certificate_field_count"], 0)
        self.assertEqual(self.summary["accepted_certificate_count"], 0)

    def test_required_field_decisions_match_matrix(self) -> None:
        rows = {row["field"]: row for row in self.summary["field_matrix"]}
        for field in ADJACENT_ONLY_FIELDS:
            self.assertEqual(rows[field]["source_status"], "adjacent_only")
        for field in ABSENT_FIELDS:
            self.assertEqual(rows[field]["source_status"], "absent")
        self.assertEqual(rows["coefficients"]["missing_object"], "source_emitted_coefficients_a_b_lambda_d")
        self.assertEqual(
            rows["Q_sector_projector_import_data"]["missing_object"],
            "source_emitted_Q_in_Q_out_I_Q_in_P_Q_out",
        )
        self.assertIn("not accepted as Q_in/Q_out", rows["Q_sector_projector_import_data"]["best_locator_or_adjacency"])

    def test_no_certificate_or_proof_restart_without_all_fields(self) -> None:
        self.assertEqual(self.summary["accepted_certificate_field_count"], 0)
        self.assertEqual(self.summary["accepted_certificate_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        rule = self.summary["proof_restart_rule"]
        self.assertFalse(rule["allowed"])
        self.assertEqual(rule["condition"], "all_required_certificate_fields_must_be_accepted")
        self.assertFalse(rule["all_required_certificate_fields_pass"])
        self.assertIn("proof_restart_allowed: false", self.text)

    def test_no_vz_or_physical_recovery_promotion(self) -> None:
        self.assertFalse(self.summary["vz_promotion_allowed"])
        self.assertFalse(self.summary["physical_recovery_promotion_allowed"])
        controls = self.summary["no_promotion_controls"]
        self.assertTrue(controls["no_vz_promotion"])
        self.assertTrue(controls["no_dgu_physical_recovery"])
        self.assertTrue(controls["no_dark_energy_promotion"])
        self.assertTrue(controls["no_three_family_promotion"])
        self.assertFalse(controls["target_import_used"])
        self.assertFalse(controls["target_import_screen_passed_for_routing"])
        self.assertEqual(
            self.summary["next_meaningful_step"]["not_next"],
            "VZ_replay_or_physical_recovery_promotion",
        )

    def test_strongest_positive_attempt_is_not_certificate(self) -> None:
        attempt = self.summary["strongest_positive_certificate_attempt"]
        self.assertIn("Oxford_023510_023612", attempt["route"])
        self.assertIn("UCSD_Y14", attempt["route"])
        self.assertEqual(
            attempt["positive_result"],
            "coherent_GU_source_region_for_bosonic_replacement_and_family_shape_search",
        )
        self.assertFalse(attempt["accepted_as_actual_operator_certificate"])
        self.assertIn("without_identity_witness", attempt["failure_mode"])

    def test_exact_missing_object_names_first_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_actual_D_GU_epsilon_0_1_identity_witness_with_sector_rule_domain_codomain_coefficients_Q_projectors_principal_symbol_and_target_import_screen",
        )
        self.assertEqual(
            obstruction["missing_object"],
            "ActualDGU01OperatorCertificateInstance_V1.source_clean_actual_operator_identity_witness",
        )
        self.assertIn("accepted_actual_DGU_01_certificate", obstruction["blocks"])
        self.assertIn("VZ_backend_replay", obstruction["blocks"])
        self.assertIn("dark_energy_recovery_promotion", obstruction["blocks"])
        self.assertIn("three_family_recovery_promotion", obstruction["blocks"])
        self.assertIn(obstruction["missing_object"], self.text)

    def test_demotion_conditions_and_next_packet_are_complete(self) -> None:
        self.assertEqual(
            set(self.summary["falsification_or_demotion_condition"]),
            REQUIRED_DEMOTION_CONDITIONS,
        )
        next_step = self.summary["next_meaningful_step"]
        self.assertEqual(
            next_step["object"],
            "source_clean_identity_witness_for_actual_D_GU_epsilon_0_1",
        )
        self.assertEqual(
            set(next_step["minimum_packet"]),
            {
                "sector_rule",
                "actual_D_GU_epsilon_0_1_action_operator_EL_identity",
                "zero_one_domain",
                "zero_one_codomain",
                "coefficients_a_b_lambda_d",
                "Q_in_Q_out_I_Q_in_P_Q_out",
                "sigma_1_D_GU_epsilon_or_sufficient_first_order_data",
                "family_identity",
                "positive_target_import_screen_for_routing",
            },
        )

    def test_required_deliverable_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict.",
            "## 2. Specific GU claim or bridge under test.",
            "## 3. Sources read first.",
            "## 4. Field-by-field certificate matrix.",
            "## 5. Strongest positive certificate attempt.",
            "## 6. First exact obstruction or missing object.",
            "## 7. Impact if closed.",
            "## 8. Falsification/demotion condition.",
            "## 9. Next meaningful proof/source step.",
            "## 10. Machine-readable JSON summary.",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
