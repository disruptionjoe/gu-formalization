#!/usr/bin/env python3
"""Audit the Cycle 1 effect-typed witness transport QFT modes artifact.

This is a structural audit. It checks that the artifact reduces the QFT/CHSH
blocker to a source/projection/finality/loss contract without claiming Bell
violation, QFT state extraction, source covariance, or positivity closure.
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
    / "hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_DIRECT_DERIVATIONS = {
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "finite_formula_H_phys_equals_Q_star_H_raw_Q",
    "SourceProjectorPFinBWithLocalModeRecords_is_prior_missing_object",
    "H_raw_Q_b_removed_representatives_H_phys_are_missing",
    "PositivePhysicalTwoPointCertificate_is_downstream_for_state_space",
    "CHSH_fixtures_are_controls_or_ansatz_not_GU_derived",
}

REQUIRED_CONTRACT_SLOTS = {
    "source_modes",
    "projection",
    "finality",
    "loss",
}

REQUIRED_SOURCE_MODE_FIELDS = {
    "P_fin_b",
    "exactly_16_local_mode_records",
    "gu_derived_provenance",
    "local_support_or_local_algebra_inclusion",
    "source_operator_section_constraint_reference",
}

REQUIRED_PROJECTION_FIELDS = {
    "H_raw",
    "R_b_removed_representatives",
    "removed_direction_roles",
    "Q_b",
    "R_star_H_raw_Q_equals_zero",
    "H_phys_equals_Q_star_H_raw_Q",
    "H_phys_psd_nonzero_rank_certificate",
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

REQUIRED_DECISIONS = {
    "missing_P_fin_b": "blocked",
    "not_exactly_16_local_modes": "blocked",
    "missing_gu_derived_provenance": "blocked_or_import",
    "missing_local_support": "fail_local_observer_input",
    "missing_effect_finality_loss_fields": "blocked_at_witness_transport_typing",
    "missing_H_raw_after_modes": "blocked_at_raw_Gram",
    "missing_Q_b_or_removed_representatives": "blocked_at_quotient_representatives",
    "R_star_H_raw_Q_nonzero": "fail_quotient_leakage",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_quotient_erased_branch",
    "clean_positive_nonzero_quotient": "promote_positive_finite_one_particle_seed_only",
    "source_covariance_later_supplied": "advance_to_covariance_gate_not_CHSH",
    "rho_AB_and_GU_admissible_observables_later_supplied": "run_CHSH_gate_without_weakening_provenance",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bBell violation is derived\b",
    r"\bCHSH violation is derived\b",
    r"\bCHSH is promoted\b",
    r"\bQFT state extraction is promoted\b",
    r"\bQFT recovery is closed\b",
    r"\bsource covariance is promoted\b",
    r"\bpositivity closure is established\b",
    r"\bH_phys is computed from current sources\b",
    r"\brho_AB is supplied\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing effect-typed witness artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class EffectTypedWitnessQFTModesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_conditional_and_all_major_overclaims_are_false(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_INTERFACE_BLOCKED_AT_EFFECT_TYPED_SOURCE_PROJECTOR_WITH_LOCAL_MODE_RECORDS",
        )
        self.assertEqual(self.summary["status"], "conditional")
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["positive_seed_promoted"], False)
        self.assertIs(self.summary["covariance_promoted"], False)
        self.assertIs(self.summary["qft_state_extraction_promoted"], False)
        self.assertIs(self.summary["chsh_promoted"], False)
        self.assertIs(self.summary["bell_violation_claimed"], False)
        self.assertIs(self.summary["positivity_closure_claimed"], False)
        self.assertIs(self.summary["not_a_chsh_or_qft_recovery_claim"], True)
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_direct_source_derivations_are_machine_readable(self) -> None:
        derived = set(self.summary["derived_directly_from_sources"])
        self.assertTrue(REQUIRED_DIRECT_DERIVATIONS.issubset(derived))

    def test_K_b_is_only_a_representation_carrier(self) -> None:
        carrier = self.summary["K_b"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertIn("representation_carrier_only", carrier["status"])

    def test_strongest_positive_result_is_interface_not_inhabited_witness(self) -> None:
        result = self.summary["strongest_positive_result"]
        self.assertEqual(result["kind"], "typed_interface_contract")
        self.assertEqual(result["interface"], "EffectTypedWitnessTransport")
        self.assertIs(result["can_reduce_blocker_to_contract"], True)
        self.assertIs(result["is_inhabited_by_current_sources"], False)
        self.assertEqual(result["promotes_today"], [])
        self.assertEqual(
            result["conditional_promotes_if_clean_packet_supplied"],
            ["PositiveFiniteOneParticleSeed_K_b"],
        )
        for not_promoted in [
            "quasifree_covariance",
            "QFT_state",
            "rho_AB",
            "Alice_Bob_tensor_product_reduction",
            "GU_admissible_observables",
            "CHSH_violation",
        ]:
            self.assertIn(not_promoted, result["does_not_promote_even_if_positive_seed"])

    def test_transport_contract_has_source_projection_finality_and_loss(self) -> None:
        contract = self.summary["transport_contract"]
        self.assertEqual(set(contract["required_slots"]), REQUIRED_CONTRACT_SLOTS)
        self.assertTrue(REQUIRED_SOURCE_MODE_FIELDS.issubset(set(contract["source_modes"])))
        self.assertTrue(REQUIRED_PROJECTION_FIELDS.issubset(set(contract["projection"])))
        self.assertEqual(set(contract["finality_statuses"]), REQUIRED_FINALITY_STATUSES)
        self.assertEqual(set(contract["loss_statuses"]), REQUIRED_LOSS_STATUSES)
        for effect_type in [
            "source_mode",
            "quotient_constraint",
            "local_observer_input",
            "pairing_input",
            "covariance_input_candidate",
            "observable_input_candidate",
        ]:
            self.assertIn(effect_type, contract["effect_types"])

    def test_first_obstruction_refines_prior_source_projector_object(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "EffectTypedSourceProjectorPFinBWithLocalModeRecords")
        self.assertEqual(
            obstruction["refines_prior_missing_object"],
            "SourceProjectorPFinBWithLocalModeRecords",
        )
        self.assertIn("not_the_16_local_source_modes", obstruction["why_first"])
        for required in [
            "P_fin_b_from_F_phys_b_O_to_K_b",
            "exactly_16_mode_records",
            "raw_representatives",
            "representation_slots",
            "local_support_or_local_algebra_inclusion",
            "provenance_beginning_gu_derived",
            "source_operator_section_constraint_reference",
            "effect_type",
            "projection_status",
            "finality_status",
            "loss_status",
        ]:
            self.assertIn(required, obstruction["must_emit"])
        self.assertEqual(obstruction["current_status"], "missing")

    def test_current_source_supply_keeps_all_live_data_missing(self) -> None:
        supply = self.summary["current_source_supply"]
        for key in [
            "P_fin_b",
            "exactly_16_local_mode_records",
            "effect_typing_for_modes",
            "projection_status_for_modes",
            "finality_status_for_modes",
            "loss_status_for_modes",
            "H_raw",
            "R_b_removed_representatives",
            "Q_b",
            "source_covariance",
            "rho_AB",
            "GU_admissible_observables",
        ]:
            self.assertEqual(supply[key], "missing", key)
        self.assertEqual(supply["H_phys"], "not_computable")

    def test_forbidden_imports_and_anti_overclaim_guards_are_explicit(self) -> None:
        forbidden = set(self.summary["forbidden_target_imports"])
        self.assertTrue(REQUIRED_FORBIDDEN_IMPORTS.issubset(forbidden))
        guards = self.summary["anti_overclaim_guards"]
        for claim in [
            "Bell_violation",
            "QFT_state_extraction",
            "source_covariance",
            "positivity_closure",
            "Alice_Bob_tensor_product",
            "GU_admissible_observables",
        ]:
            self.assertEqual(guards[claim], "not_claimed")

    def test_decision_table_has_block_fail_promote_and_next_gate_outcomes(self) -> None:
        table = self.summary["decision_table"]
        for key, expected in REQUIRED_DECISIONS.items():
            self.assertEqual(table[key], expected, key)
        self.assertIn("blocked", set(table.values()))
        self.assertIn("promote_positive_finite_one_particle_seed_only", set(table.values()))
        self.assertTrue(any(value.startswith("fail") for value in table.values()))
        self.assertIn("advance_to_covariance_gate_not_CHSH", set(table.values()))

    def test_constructive_next_object_is_effect_typed_source_packet(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "EffectTypedSourceProjectorPFinBWithLocalModeRecords")
        self.assertEqual(
            next_object["packet_id"],
            "effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0",
        )
        self.assertEqual(next_object["input_packet"], "EffectTypedSourceModePacket")
        for step in [
            "verify_exactly_16_local_modes",
            "verify_all_mode_provenance_starts_gu_derived",
            "verify_local_support_or_local_algebra_inclusion",
            "reject_forbidden_source_strings",
            "verify_effect_type_projection_status_finality_status_and_loss_status",
            "emit_decision_table_outcome",
        ]:
            self.assertIn(step, next_object["steps"])
        self.assertEqual(next_object["first_promotable_output"], "PositiveFiniteOneParticleSeed_K_b")
        for not_yet in ["quasifree_covariance", "QFT_state", "rho_AB", "CHSH_violation"]:
            self.assertIn(not_yet, next_object["not_yet"])


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "interface_id": summary["interface_id"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "positive_seed_promoted": summary["positive_seed_promoted"],
        "chsh_promoted": summary["chsh_promoted"],
        "constructive_next_object": summary["constructive_next_object"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the effect-typed witness transport QFT modes artifact."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(EffectTypedWitnessQFTModesAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
