#!/usr/bin/env python3
"""Audit the Cycle 2 QFT effect-typed source-mode packet contract.

This structural audit checks that the artifact specifies an exact schema and
decision table for EffectTypedSourceProjectorPFinBWithLocalModeRecords while
refusing to promote QFT recovery, covariance, rho_AB, CHSH, Bell violation, or
positivity closure from current sources.
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
    / "hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md"
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
    "Cycle1_promised_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "P_fin_b_and_16_local_modes_are_required",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation",
    "H_raw_removed_representatives_Q_b_and_H_phys_positivity_are_missing",
    "PositivePhysicalTwoPointCertificate_is_downstream_for_state_space",
    "CHSH_and_Bell_data_are_not_promoted_from_current_sources",
}

REQUIRED_SCHEMA_FIELDS = {
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
    "decision",
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

REQUIRED_PROJECTION_FIELDS = {
    "H_raw_exact_16_by_16",
    "H_raw_Hermitian_certificate",
    "removed_representatives_R_b",
    "removed_direction_roles",
    "Q_b_exact_16_by_r",
    "Q_b_full_column_rank_certificate",
    "R_star_H_raw_Q_equals_zero",
    "H_phys_equals_Q_star_H_raw_Q",
    "H_phys_psd_certificate",
    "H_phys_positive_rank_certificate",
}

REQUIRED_REMOVED_ROLES = {
    "EOM_b",
    "Gauge_b",
    "Constraint_b",
    "Ghost_b",
    "Null_b",
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

REQUIRED_ACCEPTANCE_CONDITIONS = {
    "sector_id_matches_QFT_SSX_PS_LR_QUASIFREE_v0",
    "carrier_is_16_dimensional_with_8_plus_8_split",
    "base_field_is_exact",
    "P_fin_b_maps_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "exactly_16_local_mode_records",
    "all_mode_provenance_starts_gu_derived",
    "all_modes_have_local_support_or_local_algebra_inclusion",
    "all_modes_have_effect_projection_finality_and_loss_statuses",
    "V_L_and_V_R_each_have_exactly_8_unique_slots",
    "H_raw_is_exact_16_by_16_Hermitian_and_source_provenanced",
    "all_removed_roles_represented_or_source_proved_empty",
    "Q_b_is_exact_16_by_r_and_full_column_rank",
    "R_star_H_raw_Q_equals_zero_exactly",
    "H_phys_equals_Q_star_H_raw_Q_exactly",
    "H_phys_is_Hermitian_psd_and_nonzero_rank_by_exact_certificate",
    "forbidden_import_screen_is_clean",
}

REQUIRED_DECISIONS = {
    "missing_P_fin_b": "blocked",
    "P_fin_b_lacks_gu_derived_provenance": "import",
    "not_exactly_16_local_mode_records": "blocked",
    "duplicate_or_missing_V_L_V_R_slot_indices": "fail_mode_slot_accounting",
    "missing_local_support_or_local_algebra": "fail_local_observer_input",
    "missing_effect_projection_finality_or_loss_status": "blocked_at_effect_typed_packet",
    "mode_provenance_not_gu_derived": "import",
    "forbidden_target_string_supplies_source_data": "import_control_or_rollback",
    "missing_H_raw": "blocked_at_raw_Gram",
    "H_raw_not_Hermitian": "fail_raw_Gram",
    "removed_roles_absent_without_empty_role_proof": "blocked_at_removed_representatives",
    "missing_Q_b": "blocked_at_Q_b",
    "Q_b_not_full_column_rank": "fail_quotient_execution",
    "R_star_H_raw_Q_nonzero": "fail_quotient_leakage",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail_physical_Gram_computation",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_quotient_erased_branch",
    "clean_H_phys_psd_nonzero_rank": "promote_positive_finite_one_particle_seed_only",
    "source_covariance_later_supplied": "advance_to_covariance_gate_not_CHSH",
    "rho_AB_and_GU_admissible_observables_later_supplied": "run_CHSH_gate_without_weakening_provenance",
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
    r"\bpositivity closure is established\b",
    r"\bH_phys is computable from current sources\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing effect-typed packet contract artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle2QFTEffectTypedSourceModePacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_underdefined_and_no_overclaims_are_promoted(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_PACKET_CONTRACT_SPECIFIED_BUT_UNINHABITED",
        )
        self.assertEqual(self.summary["status"], "underdefined")
        self.assertIs(self.summary["contract_specified"], True)
        self.assertIs(self.summary["packet_inhabited_by_current_sources"], False)
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

    def test_direct_source_derivations_are_declared(self) -> None:
        derived = set(self.summary["derived_directly_from_sources"])
        self.assertTrue(REQUIRED_DIRECT_DERIVATIONS.issubset(derived))

    def test_carrier_is_exactly_the_16_dimensional_representation_carrier(self) -> None:
        carrier = self.summary["carrier"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertEqual(carrier["status"], "representation_carrier_only_until_packet_is_inhabited")

    def test_schema_contains_projector_16_modes_quotient_and_positivity_fields(self) -> None:
        schema = self.summary["required_schema"]
        self.assertTrue(REQUIRED_SCHEMA_FIELDS.issubset(set(schema["top_level_fields"])))
        self.assertIn("domain_F_phys_b_O", schema["source_projector_P_fin_b"])
        self.assertIn("codomain_K_b", schema["source_projector_P_fin_b"])
        self.assertIn("exact_map_data", schema["source_projector_P_fin_b"])
        self.assertIn("gu_derived_provenance", schema["source_projector_P_fin_b"])
        self.assertTrue(REQUIRED_MODE_FIELDS.issubset(set(schema["local_mode_record_fields"])))
        self.assertTrue(REQUIRED_PROJECTION_FIELDS.issubset(set(schema["projection_fields"])))
        self.assertEqual(set(schema["required_removed_roles"]), REQUIRED_REMOVED_ROLES)

    def test_allowed_values_cover_effect_projection_finality_and_loss(self) -> None:
        allowed = self.summary["allowed_values"]
        self.assertEqual(set(allowed["effect_types"]), REQUIRED_EFFECT_TYPES)
        self.assertEqual(set(allowed["projection_statuses"]), REQUIRED_PROJECTION_STATUSES)
        self.assertEqual(set(allowed["finality_statuses"]), REQUIRED_FINALITY_STATUSES)
        self.assertEqual(set(allowed["loss_statuses"]), REQUIRED_LOSS_STATUSES)
        self.assertIn("QQ", allowed["base_field"])
        self.assertIn("symbolic_exact", allowed["base_field"])

    def test_acceptance_conditions_are_complete_and_only_promote_finite_seed(self) -> None:
        conditions = set(self.summary["acceptance_conditions"])
        self.assertTrue(REQUIRED_ACCEPTANCE_CONDITIONS.issubset(conditions))
        self.assertIn(
            "Clean accepted packet\n  -> PositiveFiniteOneParticleSeed(K_b) only",
            self.text,
        )
        construction = self.summary["strongest_positive_construction_attempt"]
        self.assertEqual(construction["kind"], "packet_schema_and_validator")
        self.assertIs(construction["contract_accepts_future_clean_packet"], True)
        self.assertIs(construction["contract_is_inhabited_today"], False)
        self.assertEqual(construction["promotes_today"], [])
        self.assertEqual(
            construction["conditional_promotes_if_clean_packet_supplied"],
            ["PositiveFiniteOneParticleSeed_K_b"],
        )
        for not_promoted in [
            "quasifree_covariance",
            "QFT_state",
            "rho_AB",
            "Alice_Bob_tensor_product_reduction",
            "GU_admissible_observables",
            "CHSH_violation",
            "Bell_violation",
        ]:
            self.assertIn(not_promoted, construction["does_not_promote_even_if_positive_seed"])

    def test_decision_table_has_accept_block_fail_import_and_later_gate_outcomes(self) -> None:
        table = self.summary["decision_table"]
        for key, expected in REQUIRED_DECISIONS.items():
            self.assertEqual(table[key], expected, key)
        outcomes = set(table.values())
        self.assertIn("blocked", outcomes)
        self.assertIn("import", outcomes)
        self.assertIn("promote_positive_finite_one_particle_seed_only", outcomes)
        self.assertTrue(any(value.startswith("fail") for value in outcomes))
        self.assertIn("advance_to_covariance_gate_not_CHSH", outcomes)

    def test_current_source_supply_marks_packet_uninhabited(self) -> None:
        supply = self.summary["current_source_supply"]
        for key in [
            "P_fin_b",
            "exactly_16_local_mode_records",
            "gu_derived_mode_provenance",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
            "H_raw",
            "removed_representatives_R_b",
            "Q_b",
            "source_covariance",
            "rho_AB",
            "GU_admissible_observables",
        ]:
            self.assertEqual(supply[key], "missing", key)
        self.assertEqual(supply["H_phys"], "not_computable")
        self.assertEqual(supply["H_phys_positivity"], "not_computable")

    def test_forbidden_import_screen_and_anti_overclaim_guards_are_explicit(self) -> None:
        self.assertTrue(
            REQUIRED_FORBIDDEN_IMPORTS.issubset(set(self.summary["forbidden_target_imports"]))
        )
        guards = self.summary["anti_overclaim_guards"]
        self.assertEqual(guards["QFT_recovery"], "not_claimed")
        self.assertEqual(guards["source_covariance"], "not_claimed")
        self.assertEqual(guards["rho_AB"], "not_supplied")
        self.assertEqual(guards["CHSH"], "not_claimed")
        self.assertEqual(guards["Bell_violation"], "not_claimed")
        self.assertEqual(guards["positivity_closure"], "not_claimed")

    def test_first_exact_obstruction_is_effect_typed_projector_packet(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "EffectTypedSourceProjectorPFinBWithLocalModeRecords")
        self.assertIn("not_the_16_local_source_modes", obstruction["why_first"])
        for missing in [
            "P_fin_b",
            "exactly_16_local_mode_records",
            "gu_derived_mode_provenance",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
            "H_raw",
            "removed_representatives_R_b",
            "Q_b",
            "H_phys_positivity",
        ]:
            self.assertIn(missing, obstruction["missing_fields"])
        self.assertEqual(obstruction["current_status"], "missing")

    def test_constructive_next_object_has_validator_outputs_and_ordered_steps(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0",
        )
        for output in [
            "accepted_positive_finite_seed_only",
            "blocked_missing_source_or_quotient_data",
            "fail_inconsistent_packet_or_negative_seed",
            "import_control_or_rollback",
        ]:
            self.assertIn(output, next_object["validator_outputs"])
        for step in [
            "extract_P_fin_b_from_physical_field_complex",
            "emit_exactly_16_local_source_mode_records",
            "check_gu_derived_provenance_and_local_support",
            "check_effect_projection_finality_and_loss_status",
            "compute_H_raw_from_source_physical_pairing",
            "emit_removed_representatives_or_empty_role_proofs",
            "compute_exact_full_column_rank_Q_b",
            "check_R_star_H_raw_Q_equals_zero",
            "compute_H_phys_equals_Q_star_H_raw_Q",
            "certify_H_phys_psd_and_positive_rank_exactly",
            "promote_only_PositiveFiniteOneParticleSeed_K_b",
        ]:
            self.assertIn(step, next_object["next_steps"])


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "packet_contract_id": summary["packet_contract_id"],
        "packet_inhabited_by_current_sources": summary["packet_inhabited_by_current_sources"],
        "positive_seed_promoted": summary["positive_seed_promoted"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "constructive_next_object": summary["constructive_next_object"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the QFT effect-typed source-mode packet contract."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle2QFTEffectTypedSourceModePacketAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
