#!/usr/bin/env python3
"""Audit the Cycle 3 computation-substrate extractor harness.

This is a structural audit, not a physics proof. It checks that the harness
requires the extractor fields, classifies the current substrate families,
records forbidden target inputs, and prevents any substrate proposal from being
promoted without an extractor or constructor certificate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle3-computation-substrate-extractor-harness-2026-06-24.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Harness schema",
    "## 3. Candidate class classification table",
    "## 4. Strongest positive construction attempt",
    "## 5. First exact obstruction or missing object",
    "## 6. Impact for substrate lanes and Mission A",
    "## 7. Rollback/falsification conditions",
    "## 8. Machine-readable JSON summary",
]

REQUIRED_HARNESS_FIELDS = {
    "substrate_data",
    "observer_extractor_or_constructor",
    "locality_causal_update_assumptions",
    "finite_control_output",
    "generation_count_output",
    "chirality_doubling_anomaly_ledger",
    "CHSH_state_observables_if_claimed",
    "forbidden_target_inputs",
    "certificate_accepted",
    "failure_condition",
}

REQUIRED_CANDIDATE_CLASSES = {
    "complexity_recognition_harness",
    "cellular_automata_qca",
    "wolfram_hypergraph_rewriting",
    "tensor_network_qec_holographic_code",
    "constructor_task_substrate",
    "stochastic_gff_hairer",
    "type_ii1_orbit_equivalence_selector",
    "stochastic_parisi_wu",
    "collapse_models_grw_csl_dp",
    "cardinality_only_c3_d4_cn_selector",
    "relabeled_bell_pauli_tensor_controls",
    "target_fitted_rule_or_decoder_search",
}

REQUIRED_STATUS_SET = {"pursue", "protect", "park", "kill"}

REQUIRED_FORBIDDEN_INPUTS = {
    "A_F",
    "finite_CC_tuple",
    "G_SM",
    "central_Z6",
    "K_SM",
    "n_equals_3",
    "generation_count_3",
    "C3",
    "index_3",
    "D4_arms",
    "three_projections",
    "dim_H_F_96",
    "ordinary_anomaly_free_SM_shadow",
    "physical_Higgs_data",
    "SM_chiral_spectrum",
    "parity_odd_drift",
    "chiral_boundary_condition",
    "chosen_chiral_Kraus_operator",
    "Bell_state",
    "Pauli_settings",
    "CHSH_target_value",
    "rho_AB_target",
    "identity_Gram",
    "standard_free_vacuum",
    "Hadamard_or_Fock_vacuum",
    "target_fitted_decoder",
    "target_fitted_rule_search",
}

REQUIRED_ROLLBACKS = {
    "observer_extractor_or_constructor_absent",
    "forbidden_target_input_used",
    "n2_n4_or_Cn_replacement_still_works",
    "finite_control_imported",
    "chirality_inserted_by_drift_boundary_measure_kraus_or_decoder",
    "dropped_no_go_premise_without_cost_ledger",
    "extra_modes_without_anomaly_computation",
    "Bell_Pauli_tensor_or_CHSH_control_relabelled_as_GU_data",
    "no_finite_certificate_or_failure_condition",
    "proposal_promoted_while_certificate_accepted_false",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bcomputation substrate derives finite control\b",
    r"\bcomputation substrate derives three generations\b",
    r"\bWolfram.*derives GU\b",
    r"\bCA.*derives chirality\b",
    r"\btensor network.*derives CHSH\b",
    r"\bconstructor theory.*derives GU\b",
    r"\bstochastic.*derives chirality\b",
    r"\bCHSH violation is derived\b",
    r"\bthree generations are derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing computation-substrate harness: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle3ComputationSubstrateExtractorHarnessAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_current_substrate_promotion(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "HARNESS_GATE_ACTIVE_NO_CURRENT_SUBSTRATE_PROMOTION",
        )
        self.assertEqual(self.summary["status"], "gate_active")
        self.assertIs(self.summary["no_current_substrate_promoted"], True)
        self.assertIs(self.summary["promotion_requires_extractor_or_certificate"], True)
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion claim matched: {pattern}",
            )

    def test_required_harness_fields_are_complete_and_visible(self) -> None:
        fields = set(self.summary["required_harness_fields"])
        self.assertEqual(fields, REQUIRED_HARNESS_FIELDS)
        for field in REQUIRED_HARNESS_FIELDS:
            self.assertIn(field, self.text)

    def test_forbidden_target_inputs_cover_finite_control_generation_chsh_and_chirality(self) -> None:
        forbidden = set(self.summary["forbidden_target_inputs"])
        self.assertTrue(REQUIRED_FORBIDDEN_INPUTS.issubset(forbidden))
        for item in REQUIRED_FORBIDDEN_INPUTS:
            self.assertIn(item, self.text)

    def test_candidate_classes_are_complete_and_have_gate_statuses(self) -> None:
        classes = self.summary["candidate_classes"]
        self.assertEqual(set(classes), REQUIRED_CANDIDATE_CLASSES)

        statuses = {row["status"] for row in classes.values()}
        self.assertEqual(statuses, REQUIRED_STATUS_SET)

        for name, row in classes.items():
            self.assertIn(row["status"], REQUIRED_STATUS_SET, name)
            self.assertTrue(row["harness_verdict"], name)
            self.assertTrue(row["substrate_data_status"], name)
            self.assertTrue(row["extractor_certificate_status"], name)
            self.assertIs(row["certificate_accepted"], False, name)
            self.assertIs(row["promoted"], False, name)
            self.assertTrue(row["first_obstruction"], name)
            self.assertTrue(row["allowed_use"], name)

    def test_status_decisions_match_current_classification(self) -> None:
        classes = self.summary["candidate_classes"]
        self.assertEqual(classes["complexity_recognition_harness"]["status"], "pursue")
        self.assertEqual(classes["cellular_automata_qca"]["status"], "pursue")
        self.assertEqual(classes["wolfram_hypergraph_rewriting"]["status"], "protect")
        self.assertEqual(classes["tensor_network_qec_holographic_code"]["status"], "protect")
        self.assertEqual(classes["constructor_task_substrate"]["status"], "protect")
        self.assertEqual(classes["stochastic_gff_hairer"]["status"], "protect")
        self.assertEqual(classes["type_ii1_orbit_equivalence_selector"]["status"], "protect")
        self.assertEqual(classes["stochastic_parisi_wu"]["status"], "park")
        self.assertEqual(classes["collapse_models_grw_csl_dp"]["status"], "park")
        self.assertEqual(classes["cardinality_only_c3_d4_cn_selector"]["status"], "kill")
        self.assertEqual(classes["relabeled_bell_pauli_tensor_controls"]["status"], "kill")
        self.assertEqual(classes["target_fitted_rule_or_decoder_search"]["status"], "kill")

    def test_no_substrate_can_be_promoted_without_extractor_or_certificate(self) -> None:
        rule = self.summary["promotion_rule"]
        self.assertIs(rule["promotion_allowed_now"], False)
        self.assertIn("ExtractorCertificate_v0", rule["accepted_certificate_types"])
        self.assertIn("ConstructorTaskCertificate_v0", rule["accepted_certificate_types"])

        requirements = set(rule["accepted_as_GU_relevance_requires"])
        for required in [
            "target_free_substrate_data",
            "typed_observer_extractor_or_constructor",
            "forbidden_target_input_screen_passed",
            "at_least_one_live_output_computed",
            "replacement_controls_fail_by_named_obstruction",
        ]:
            self.assertIn(required, requirements)

        failures = set(rule["automatic_failure_if"])
        for required in [
            "extractor_or_constructor_missing",
            "target_data_in_substrate_or_rule_selection",
            "same_proof_works_for_n2_or_n4",
            "certificate_accepted_false_but_promotion_claimed",
        ]:
            self.assertIn(required, failures)

        for name, row in self.summary["candidate_classes"].items():
            if row["promoted"]:
                self.assertIs(row["certificate_accepted"], True, name)
                self.assertNotIn("missing", row["extractor_certificate_status"], name)

    def test_strongest_positive_attempt_is_certificate_shell_only(self) -> None:
        attempt = self.summary["strongest_positive_construction_attempt"]
        self.assertEqual(attempt["id"], "FiniteSubstrateExtractorSandbox_v0")
        self.assertEqual(attempt["status"], "certificate_shell_only")
        self.assertEqual(attempt["promotes_now"], "no_current_candidate")
        for component in [
            "harness_field_schema",
            "forbidden_input_screen",
            "C3_D4_Cn_negative_control",
            "stochastic_parity_insertion_test",
            "CHSH_fixture_controls",
        ]:
            self.assertIn(component, attempt["available_components"])
        for component in [
            "fixed_target_free_substrate_instance",
            "typed_substrate_to_observer_extractor",
            "finite_control_image_computation",
            "generation_count_replacement_obstruction",
            "chirality_doubling_anomaly_certificate",
            "source_derived_rho_AB_and_observables",
        ]:
            self.assertIn(component, attempt["missing_components"])

    def test_first_exact_obstruction_names_extractor_certificate_and_next_gates(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "SUBSTRATE_TO_OBSERVER_EXTRACTOR_CERTIFICATE_MISSING",
        )
        for item in [
            "fixed_substrate_data",
            "update_or_task_law",
            "typed_extractor_or_constructor",
            "forbidden_input_screen",
            "output_packets",
            "replacement_tests",
            "certificate_accepted_boolean_and_reason",
        ]:
            self.assertIn(item, obstruction["must_emit"])
        for item in [
            "FINITE_CONTROL_IMAGE_COMPUTATION",
            "N_NEQ_3_REPLACEMENT_OBSTRUCTION",
            "CHIRALITY_DOUBLING_ANOMALY_CERTIFICATE",
            "SOURCE_DERIVED_RHO_AB_AND_OBSERVABLES",
        ]:
            self.assertIn(item, obstruction["next_obstructions_if_supplied"])

    def test_mission_a_impacts_remain_unpromoted(self) -> None:
        impact = self.summary["impact_for_mission_a"]
        self.assertEqual(impact["finite_control"], "not_promoted")
        self.assertEqual(
            impact["generation_count"],
            "not_promoted_by_computation_substrate",
        )
        self.assertEqual(impact["chirality_anomaly"], "no_new_substrate_derived_shadow")
        self.assertEqual(
            impact["CHSH_observer_finality"],
            "no_GU_derived_rho_AB_or_admissible_observables",
        )
        self.assertIn("requires_extractor", impact["no_go_evasion"])

    def test_rollback_conditions_are_machine_readable(self) -> None:
        rollback = set(self.summary["rollback_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollback))


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "candidate_class_count": len(summary["candidate_classes"]),
        "no_current_substrate_promoted": summary["no_current_substrate_promoted"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the Cycle 3 computation-substrate extractor harness."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle3ComputationSubstrateExtractorHarnessAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
