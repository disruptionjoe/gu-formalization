#!/usr/bin/env python3
"""Audit the Cycle 3 QFT source-mode packet validator artifact.

This is a structural audit. It checks that the artifact specifies an exact
accept/block/fail/import validator for effect-typed QFT source-mode packets,
runs that validator conceptually against current repo supply, and refuses to
promote QFT recovery, covariance, rho_AB, CHSH, Bell violation, positive finite
seed, or positivity closure from current sources.
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
    / "hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Construction Attempt",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. Impact On GU Claim",
    "## 7. Next Meaningful Proof/Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_DIRECT_DERIVATIONS = {
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "Cycle2_packet_contract_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "Cycle1_effect_projection_finality_loss_typing_requirement",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "P_fin_b_and_16_local_modes_are_required",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation",
    "H_raw_removed_representatives_Q_b_and_H_phys_positivity_are_missing",
    "current_contract_is_specified_but_uninhabited",
    "CHSH_Bell_covariance_and_rho_AB_are_not_promoted_from_current_sources",
}

REQUIRED_VALIDATOR_INPUTS = {
    "packet_id",
    "sector_id",
    "carrier",
    "base_field",
    "source_projector_P_fin_b",
    "local_mode_records",
    "raw_Gram_H_raw",
    "removed_representatives_R_b",
    "Q_b",
    "quotient_compatibility",
    "H_phys",
    "forbidden_import_screen",
    "decision_log",
}

REQUIRED_MODE_FIELDS = {
    "mode_id",
    "label",
    "raw_representative",
    "image_in_K_b",
    "representation_slot",
    "slot_index",
    "local_support_or_local_algebra_inclusion",
    "gu_derived_provenance",
    "source_operator_or_section_reference",
    "target_import_flag_false",
    "effect_type",
    "projection_status",
    "finality_status",
    "loss_status",
}

REQUIRED_EFFECT_TYPES = {
    "source_mode",
    "quotient_constraint",
    "local_observer_input",
    "pairing_input",
    "covariance_input_candidate",
    "observable_input_candidate",
}

REQUIRED_PROJECTION_STATUSES = {
    "raw",
    "projected",
    "quotient_survivor",
    "quotient_removed",
}

REQUIRED_FINALITY_STATUSES = {
    "final",
    "provisional",
    "killed_by_EOM",
    "killed_by_gauge",
    "killed_by_constraint",
    "killed_by_ghost",
    "killed_by_null",
    "unresolved",
}

REQUIRED_LOSS_STATUSES = {
    "no_loss",
    "quotient_removed",
    "locality_lost",
    "positivity_lost",
    "provenance_lost",
    "tensor_factorization_not_supplied",
    "observable_admissibility_not_supplied",
}

REQUIRED_DECISIONS = {
    "missing_sector_or_wrong_sector": "fail",
    "wrong_carrier_or_dimension": "fail",
    "missing_base_field": "blocked",
    "missing_P_fin_b": "blocked",
    "P_fin_b_lacks_gu_derived_provenance": "import",
    "not_exactly_16_local_mode_records": "blocked",
    "duplicate_or_missing_V_L_V_R_slot_indices": "fail",
    "missing_raw_representative_or_image": "blocked",
    "missing_local_support_or_local_algebra": "fail",
    "mode_provenance_not_gu_derived": "import",
    "missing_effect_projection_finality_or_loss_status": "blocked",
    "forbidden_target_string_supplies_source_data": "import",
    "missing_H_raw": "blocked",
    "H_raw_not_Hermitian": "fail",
    "removed_roles_absent_without_empty_role_proof": "blocked",
    "missing_Q_b": "blocked",
    "Q_b_not_full_column_rank": "fail",
    "R_star_H_raw_Q_nonzero": "fail",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail",
    "H_phys_negative": "fail",
    "H_phys_rank_zero": "fail",
    "clean_H_phys_psd_nonzero_rank": "accept_positive_finite_one_particle_seed_only",
}

REQUIRED_FORBIDDEN_IMPORTS = {
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "Stinespring_or_CPTP_channel_as_GU_source_without_derivation",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_or_Pati_Salam_labels_as_physical_Gram",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bQFT recovery is closed\b",
    r"\bQFT state extraction is promoted\b",
    r"\bsource covariance is promoted\b",
    r"\brho_AB is supplied\b",
    r"\bCHSH violation is derived\b",
    r"\bBell violation is derived\b",
    r"\bpositive finite seed is promoted\b",
    r"\bpositivity closure is established\b",
    r"\bH_phys is computable from current sources\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source-mode packet validator artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle3QFTSourceModePacketValidatorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_current_packet_record_and_all_overclaims(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_CURRENT_EFFECT_TYPED_SOURCE_MODE_PACKET_RECORD",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertIs(self.summary["validator_specified"], True)
        self.assertIs(self.summary["packet_record_exists_in_current_repo_supply"], False)
        self.assertIs(self.summary["accepted_packet_exists"], False)
        self.assertIs(self.summary["positive_seed_promoted"], False)
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["covariance_promoted"], False)
        self.assertIs(self.summary["rho_AB_supplied"], False)
        self.assertIs(self.summary["chsh_promoted"], False)
        self.assertIs(self.summary["bell_violation_claimed"], False)
        self.assertIs(self.summary["positivity_closure_claimed"], False)
        self.assertIs(self.summary["not_a_chsh_or_qft_recovery_claim"], True)
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_K_b_is_only_the_named_16_dimensional_carrier(self) -> None:
        carrier = self.summary["K_b"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertEqual(carrier["status"], "representation_carrier_only")

    def test_direct_source_derivations_are_declared(self) -> None:
        derived = set(self.summary["derived_directly_from_sources"])
        self.assertTrue(REQUIRED_DIRECT_DERIVATIONS.issubset(derived))

    def test_validator_schema_and_mode_enums_are_complete(self) -> None:
        self.assertTrue(REQUIRED_VALIDATOR_INPUTS.issubset(set(self.summary["validator_inputs"])))
        self.assertTrue(REQUIRED_MODE_FIELDS.issubset(set(self.summary["mode_record_fields"])))
        self.assertEqual(set(self.summary["effect_types"]), REQUIRED_EFFECT_TYPES)
        self.assertEqual(set(self.summary["projection_statuses"]), REQUIRED_PROJECTION_STATUSES)
        self.assertEqual(set(self.summary["finality_statuses"]), REQUIRED_FINALITY_STATUSES)
        self.assertEqual(set(self.summary["loss_statuses"]), REQUIRED_LOSS_STATUSES)

    def test_validator_steps_cover_accept_block_fail_and_import(self) -> None:
        steps = self.summary["validator_steps"]
        self.assertEqual(len(steps), 21)
        self.assertEqual([step["step"] for step in steps], list(range(1, 22)))
        decisions = {step["failure_decision"] for step in steps}
        for required in ["blocked", "fail", "import", "blocked_or_fail", "none"]:
            self.assertIn(required, decisions)
        checks = {step["check"] for step in steps}
        for required_check in [
            "source_projector_P_fin_b_exists_from_F_phys_b_O_to_K_b",
            "exactly_16_local_mode_records_exist",
            "H_raw_is_exact_16_by_16_Hermitian_and_source_provenanced",
            "R_star_H_raw_Q_equals_zero_exactly",
            "H_phys_equals_Q_star_H_raw_Q_exactly",
            "H_phys_has_exact_psd_certificate",
            "accepted_packet_promotes_positive_finite_one_particle_seed_only",
        ]:
            self.assertIn(required_check, checks)

    def test_decision_table_and_forbidden_imports_are_explicit(self) -> None:
        self.assertEqual(self.summary["decision_table"], REQUIRED_DECISIONS)
        self.assertEqual(set(self.summary["forbidden_imports"]), REQUIRED_FORBIDDEN_IMPORTS)

    def test_current_repo_supply_blocks_at_missing_projector_before_matrix_stage(self) -> None:
        run = self.summary["current_repo_supply_run"]
        self.assertEqual(run["candidate"], "strongest_current_carrier_and_basis_label_shell")
        self.assertEqual(run["sector_id"], "available")
        self.assertEqual(run["carrier"], "available_as_representation_carrier_only")
        self.assertEqual(run["basis_label_pattern"], "available_as_labels_only")
        self.assertEqual(run["source_projector_P_fin_b"], "missing")
        self.assertEqual(run["local_mode_records"], "missing")
        self.assertEqual(run["H_raw"], "missing")
        self.assertEqual(run["Q_b"], "missing")
        self.assertEqual(run["H_phys"], "not_computable")
        self.assertEqual(run["positivity_certificate"], "missing")
        self.assertEqual(run["first_obstruction_step"], 4)
        self.assertEqual(run["first_obstruction"], "missing_source_projector_P_fin_b")
        self.assertEqual(run["decision"], "blocked")
        self.assertIs(run["accepted_record_exists"], False)

    def test_first_exact_obstruction_and_next_object_are_source_extraction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "source_projector_P_fin_b")
        self.assertEqual(
            obstruction["formal_name"],
            "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
        )
        self.assertEqual(obstruction["validator_step"], 4)
        self.assertEqual(obstruction["current_status"], "missing")
        self.assertIn(
            "without_P_fin_b_the_16_slots_are_only_representation_labels_not_source_mode_images",
            obstruction["why_first"],
        )

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1")
        self.assertEqual(next_object["first_pilot"], "SingleModeSourceExtractionCertificate")
        for required in [
            "P_fin_b_from_F_phys_b_O_to_K_b",
            "gu_derived_projector_provenance",
            "exactly_16_mode_records",
            "local_support_or_local_algebra_inclusion",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
        ]:
            self.assertIn(required, next_object["must_emit"])

    def test_impact_and_next_step_are_not_chsh_or_covariance_claims(self) -> None:
        self.assertEqual(
            self.summary["impact_on_GU_claim"],
            "QFT_source_mode_recovery_branch_open_but_blocked_at_source_extraction",
        )
        self.assertEqual(
            self.summary["next_meaningful_step"],
            "Build_SingleModeSourceExtractionCertificate_then_generalize_to_16_mode_packet",
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit a compact JSON result")
    args = parser.parse_args()

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        HourlyCycle3QFTSourceModePacketValidatorAudit
    )
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)

    payload = {
        "ok": result.wasSuccessful(),
        "testsRun": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "doc": str(DOC),
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
