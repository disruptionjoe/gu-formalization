#!/usr/bin/env python3
"""Audit the hourly single-mode QFT source extraction certificate.

This is a structural audit. It parses the machine-readable JSON summary,
requires the one-mode fields and validator steps reached, enforces forbidden
import guards, refuses positive finite-seed/QFT/covariance/rho_AB/CHSH
promotion, and checks the exact first obstruction.
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
    / "hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md"
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

REQUIRED_DIRECT_DERIVATIONS = {
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "Cycle3_validator_promises_single_mode_pilot",
    "Cycle3_validator_requires_source_projector_before_mode_admission",
    "Cycle2_packet_contract_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "Cycle2_quotient_ledger_requires_P_fin_b_and_16_local_source_records",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation_only",
    "Mission_A_places_covariance_rho_AB_and_CHSH_downstream",
}

REQUIRED_ONE_MODE_FIELDS = {
    "sector_id",
    "carrier",
    "selected_slot",
    "source_projector_P_fin_b",
    "projector_gu_derived_provenance",
    "raw_representative_or_physical_representative",
    "local_support_or_local_algebra_inclusion",
    "image_in_K_b",
    "mode_gu_derived_provenance",
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

REQUIRED_FORBIDDEN_IMPORTS = {
    "ordinary_Pati_Salam_labels_as_source_data",
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_labels_as_physical_Gram",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bsingle-mode source extraction is closed\b",
    r"\bone local physical source mode is constructed\b",
    r"\bpositive finite seed is promoted\b",
    r"\bQFT recovery is closed\b",
    r"\bsource covariance is promoted\b",
    r"\brho_AB is supplied\b",
    r"\bCHSH violation is derived\b",
    r"\bBell violation is derived\b",
    r"\bpositivity closure is established\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing single-mode source extraction artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlySingleModeQFTSourceExtractionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_without_positive_promotions(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "SingleModeSourceExtractionCertificate_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_P_FIN_B",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertIs(self.summary["one_mode_pilot_attempted"], True)

        promotions = self.summary["positive_promotions"]
        for key in [
            "single_mode_source_extraction_closed",
            "sixteen_mode_packet_admitted",
            "positive_finite_seed_promoted",
            "qft_recovered",
            "covariance_promoted",
            "rho_AB_supplied",
            "chsh_promoted",
            "bell_violation_claimed",
            "positivity_closure_claimed",
        ]:
            self.assertIs(promotions[key], False, key)

        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_selected_slot_and_carrier_are_only_representation_data(self) -> None:
        slot = self.summary["selected_slot"]
        self.assertEqual(slot["representation_slot"], "V_L")
        self.assertEqual(slot["slot_index"], 1)
        self.assertEqual(slot["slot_label"], "V_L[1]")
        self.assertEqual(slot["role"], "intended_target_slot_only")

        carrier = self.summary["carrier"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertEqual(carrier["status"], "representation_carrier_only")

    def test_direct_source_derivations_are_declared(self) -> None:
        self.assertTrue(
            REQUIRED_DIRECT_DERIVATIONS.issubset(
                set(self.summary["derived_directly_from_sources"])
            )
        )

    def test_validator_steps_reach_exact_projector_block(self) -> None:
        steps = self.summary["validator_steps_reached"]
        self.assertEqual([step["step"] for step in steps], [1, 2, 3, 4])
        self.assertEqual(steps[0]["result"], "pass")
        self.assertEqual(steps[1]["result"], "pass_as_representation_carrier")
        self.assertEqual(
            steps[2]["result"],
            "symbolic_exact_shell_only_no_source_matrix_data",
        )
        self.assertEqual(
            steps[3]["check"],
            "source_projector_P_fin_b_exists_from_F_phys_b_O_to_K_b",
        )
        self.assertEqual(steps[3]["result"], "blocked")
        self.assertEqual(self.summary["validator_first_block_step"], 4)

    def test_one_mode_fields_are_required_and_current_statuses_are_blocked(self) -> None:
        self.assertTrue(
            REQUIRED_ONE_MODE_FIELDS.issubset(set(self.summary["one_mode_required_fields"]))
        )
        status = self.summary["one_mode_field_status"]
        self.assertEqual(status["sector_id"], "available")
        self.assertEqual(status["carrier"], "available_as_representation_carrier_only")
        self.assertEqual(status["selected_slot"], "available_as_intended_label_only")
        self.assertEqual(status["source_projector_P_fin_b"], "missing")
        self.assertEqual(status["projector_gu_derived_provenance"], "missing")
        self.assertEqual(
            status["raw_representative_or_physical_representative"],
            "not_reachable_before_P_fin_b",
        )
        self.assertEqual(
            status["local_support_or_local_algebra_inclusion"],
            "not_reachable_before_source_representative",
        )
        self.assertEqual(status["image_in_K_b"], "not_source_certified")
        self.assertEqual(status["mode_gu_derived_provenance"], "missing")
        self.assertEqual(status["source_operator_or_section_reference"], "missing")
        self.assertIs(status["target_import_flag_false"], True)
        self.assertEqual(status["effect_type"], "unassigned_no_source_mode")
        self.assertEqual(status["projection_status"], "unassigned_no_source_mode")
        self.assertEqual(status["finality_status"], "unassigned_no_source_mode")
        self.assertEqual(status["loss_status"], "unassigned_no_source_mode")

    def test_effect_projection_finality_and_loss_vocabularies_are_preserved(self) -> None:
        self.assertEqual(set(self.summary["allowed_effect_types"]), REQUIRED_EFFECT_TYPES)
        self.assertEqual(
            set(self.summary["allowed_projection_statuses"]),
            REQUIRED_PROJECTION_STATUSES,
        )
        self.assertEqual(
            set(self.summary["allowed_finality_statuses"]),
            REQUIRED_FINALITY_STATUSES,
        )
        self.assertEqual(set(self.summary["allowed_loss_statuses"]), REQUIRED_LOSS_STATUSES)

    def test_forbidden_import_guards_are_explicit(self) -> None:
        self.assertEqual(set(self.summary["forbidden_imports"]), REQUIRED_FORBIDDEN_IMPORTS)

    def test_first_obstruction_is_missing_p_fin_b_and_blocks_one_mode_fields(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_source_projector_P_fin_b_for_single_mode_extraction",
        )
        self.assertEqual(
            obstruction["formal_name"],
            "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
        )
        self.assertEqual(obstruction["validator_step"], 4)
        self.assertEqual(obstruction["current_status"], "missing")
        self.assertIn(
            "without_P_fin_b_V_L_1_is_not_certified_as_an_image_of_a_local_physical_source_mode",
            obstruction["why_first"],
        )
        for blocked_field in [
            "raw_representative_or_physical_representative",
            "local_support_or_local_algebra_inclusion",
            "image_in_K_b",
            "mode_gu_derived_provenance",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
        ]:
            self.assertIn(blocked_field, obstruction["blocks_fields"])

    def test_constructive_next_object_is_single_mode_image_certificate_only(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "SingleModePFinBImageCertificate_V1")
        self.assertEqual(next_object["selected_slot"], "V_L[1]")
        for required in [
            "P_fin_b_from_F_phys_b_O_to_K_b",
            "gu_derived_projector_provenance",
            "raw_or_physical_representative",
            "local_support_or_local_algebra_inclusion",
            "exact_image_in_K_b_occupying_V_L_1",
            "source_operator_section_constraint_reference",
            "target_import_flag_false",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
        ]:
            self.assertIn(required, next_object["must_emit"])
        for forbidden_promotion in [
            "PositiveFiniteOneParticleSeed_K_b",
            "quasifree_covariance",
            "QFT_state",
            "rho_AB",
            "CHSH_violation",
            "Bell_violation",
        ]:
            self.assertIn(forbidden_promotion, next_object["does_not_promote_by_itself"])

    def test_impact_and_next_step_are_source_extraction_not_chsh(self) -> None:
        self.assertEqual(
            self.summary["impact_on_GU_claim"],
            "QFT_source_mode_recovery_branch_open_but_blocked_before_one_certified_local_source_mode",
        )
        self.assertEqual(
            self.summary["next_meaningful_step"],
            "Construct_or_refute_SingleModePFinBImageCertificate_V1_for_V_L_1",
        )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "artifact": summary["artifact"],
        "selected_slot": summary["selected_slot"]["slot_label"],
        "validator_first_block_step": summary["validator_first_block_step"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_meaningful_step": summary["next_meaningful_step"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the single-mode QFT source extraction certificate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlySingleModeQFTSourceExtractionAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
