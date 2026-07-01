#!/usr/bin/env python3
"""Audit FiniteLocalQFTExtractionMapSpec_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle3-finite-local-qft-extraction-map-spec.md"
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

REQUIRED_SPEC_FIELDS = {
    "observation_context",
    "source_space",
    "operation",
    "codomain",
    "naturality_covariance",
    "non_import_condition",
    "finite_stability_test",
}

FORBIDDEN_SELECTION_INPUTS = {
    "Gram",
    "CHSH",
    "Bell",
    "rho_AB",
    "desired_finite_recovery",
    "standard_Bell_state",
    "Pauli_controls",
    "target_fitted_Hilbert_factorization",
    "ordinary_QFT_vacuum_or_state_as_source_data",
    "post_hoc_choice_of_K_b_to_match_recovery",
}

REQUIRED_STABILITY_CHECKS = {
    "K_b_is_finite",
    "P_fin_b_total_on_admitted_local_data",
    "gauge_or_projection_equivalent_representatives_have_declared_equal_or_transformed_outputs",
    "observation_restrictions_and_section_changes_satisfy_naturality",
    "finite_image_not_selected_by_forbidden_qft_targets",
    "falsifiable_failure_mode_emitted",
}


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class FiniteLocalQFTExtractionMapSpecAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)
        cls.fields = cls.summary["spec_fields"]

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_artifact_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact"], "FiniteLocalQFTExtractionMapSpec_V1")
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0301")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_RECONSTRUCTION_GRADE_SPEC_SOURCE_DERIVATION_UNDERDEFINED",
        )
        self.assertEqual(self.summary["verdict_class"], "conditional")
        self.assertIs(self.summary["source_derived"], False)
        self.assertIs(self.summary["reconstruction_grade_conditional"], True)
        self.assertIs(self.summary["underdefined_without_new_object"], True)
        self.assertEqual(
            self.summary["artifact_identity"]["owned_path"],
            "explorations/hourly-20260625-0301-cycle3-finite-local-qft-extraction-map-spec.md",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["companion_audit"],
            "tests/hourly_20260625_0301_cycle3_finite_local_qft_extraction_map_spec_audit.py",
        )

    def test_source_basis_includes_required_inputs(self) -> None:
        basis = self.summary["source_basis"]
        for key in [
            "posture",
            "runbook",
            "cycle2_qft_receipt",
            "cycle2_display_index",
            "cycle2_transition_ledger",
            "source_pdf",
        ]:
            self.assertIn(key, basis)
        self.assertEqual(basis["source_pdf"], "Geometric_UnityDraftApril1st2021.pdf")

    def test_all_spec_fields_are_present(self) -> None:
        self.assertEqual(set(self.fields), REQUIRED_SPEC_FIELDS)
        for field_name in REQUIRED_SPEC_FIELDS:
            self.assertIn("status", self.fields[field_name], field_name)

    def test_source_derived_vs_reconstruction_labels_are_explicit(self) -> None:
        observation = self.fields["observation_context"]
        self.assertEqual(observation["symbol"], "O")
        self.assertEqual(observation["evidence_label"], "source_derived")
        self.assertEqual(observation["status"], "defined")
        self.assertGreaterEqual(len(observation["source_locators"]), 3)

        source_space = self.fields["source_space"]
        self.assertEqual(source_space["symbol"], "F_GU,loc^b(O)")
        self.assertEqual(source_space["replaces"], "F_phys^b(O)")
        self.assertEqual(source_space["evidence_label"], "reconstruction_label_from_source_context")
        self.assertEqual(source_space["status"], "candidate_only")
        self.assertIn("omega=(epsilon,varpi,nu,zeta)", source_space["candidate"])

        operation = self.fields["operation"]
        self.assertEqual(operation["symbol"], "P_fin^b")
        self.assertEqual(operation["evidence_label"], "not_source_derived")
        self.assertEqual(operation["source_locators"], [])
        self.assertEqual(operation["status"], "missing_operation")

        codomain = self.fields["codomain"]
        self.assertEqual(codomain["symbol"], "K_b")
        self.assertEqual(codomain["evidence_label"], "not_source_derived")
        self.assertEqual(codomain["source_locators"], [])
        self.assertEqual(codomain["status"], "missing_codomain")

    def test_naturality_covariance_rules_are_declared_but_unproved(self) -> None:
        naturality = self.fields["naturality_covariance"]
        self.assertEqual(naturality["evidence_label"], "source_facing_requirement")
        self.assertEqual(naturality["status"], "required_unproved")
        required_rules = set(naturality["required_rules"])
        for rule in [
            "observation_restriction_commutes_with_finite_transition_map",
            "change_of_observation_section_matches_finite_carrier_transport",
            "gauge_action_is_equivariant_or_quotiented_by_source_defined_rule",
            "representative_redundancy_kernel_or_quotient_is_named_before_acceptance",
            "local_frame_change_acts_through_declared_finite_carrier_action",
        ]:
            self.assertIn(rule, required_rules)

    def test_non_import_flags_forbid_qft_target_selection(self) -> None:
        non_import = self.fields["non_import_condition"]
        self.assertEqual(set(non_import["forbidden_selection_inputs"]), FORBIDDEN_SELECTION_INPUTS)
        self.assertEqual(non_import["qft_targets_used_to_select_map"], [])
        self.assertIs(non_import["target_import_detected"], False)
        self.assertEqual(non_import["status"], "defined")

    def test_finite_stability_test_is_specified_not_passed(self) -> None:
        stability = self.fields["finite_stability_test"]
        self.assertIs(stability["specified"], True)
        self.assertIs(stability["passed"], False)
        self.assertEqual(set(stability["required_checks"]), REQUIRED_STABILITY_CHECKS)
        self.assertEqual(
            stability["current_failure_reason"],
            "P_fin^b_and_K_b_are_not_source_emitted_or_constructed",
        )
        self.assertEqual(stability["status"], "specified_not_passed")

    def test_zero_receipts_and_no_qft_proof_promotion(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["finite_qft_recovery_promoted"], False)
        self.assertIs(self.summary["qft_proof_promotion_allowed"], False)
        promotions = self.summary["no_claim_promotions"]
        for key, value in promotions.items():
            self.assertIs(value, False, key)
        self.assertIn("Not allowed:", self.text)
        self.assertIn("Finite QFT recovery is restarted.", self.text)
        self.assertIn("Finite stability is proved.", self.text)

    def test_first_obstruction_and_next_object_are_precise(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "SourceEmittedFiniteLocalExtractionOperatorWithFiniteCodomain_V1",
        )
        self.assertIs(obstruction["missing"], True)
        self.assertIn("P_fin^b", obstruction["description"])
        self.assertIn("K_b", obstruction["description"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "SourceEmittedOrReconstructedFiniteCarrierAndExtractionRule_V1",
        )
        self.assertEqual(next_object["pilot"], "SingleObservationFiniteExtractionPilot_V1")
        self.assertEqual(
            set(next_object["required_fields"]),
            {
                "source_locator_or_reconstruction_axiom",
                "observation_context",
                "source_space",
                "operation",
                "codomain",
                "transport_maps",
                "finite_stability_certificate",
                "non_import_audit",
            },
        )

    def test_no_forbidden_positive_phrases_outside_denial_context(self) -> None:
        denial_removed = re.sub(
            r"Not allowed:\s*```text\s*.*?```",
            "",
            self.text,
            flags=re.DOTALL,
        )
        forbidden_promotional_phrases = [
            "GU derives finite local QFT extraction.",
            "The manuscript supplies P_fin^b.",
            "The manuscript defines K_b.",
        ]
        for phrase in forbidden_promotional_phrases:
            self.assertNotIn(phrase, denial_removed)


if __name__ == "__main__":
    unittest.main()
