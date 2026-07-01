#!/usr/bin/env python3
"""Audit the hourly Cycle 2 QFT source-mode quotient data ledger.

This is a structural audit, not a finite positivity proof. It checks that the
ledger requires the source projector, mode provenance, raw Gram, quotient data,
removed representatives, locality data, and import guardrails before any
positive seed, covariance, or CHSH claim can be promoted.
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
    / "hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Required Source-Mode Quotient Ledger Fields",
    "## 3. What Current QFT/CHSH Files Establish",
    "## 4. Strongest Positive Data Ledger Attempt",
    "## 5. First Exact Missing Object",
    "## 6. Impact For H_phys, Covariance, And CHSH",
    "## 7. Rollback/Falsification Conditions",
    "## 8. Next Meaningful Finite Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_LEDGER_FIELDS = {
    "sector_id",
    "carrier_spec",
    "base_field",
    "source_projector_P_fin_b",
    "raw_mode_records",
    "mode_provenance",
    "mode_support",
    "H_raw",
    "R_b_removed_representatives",
    "removed_direction_roles",
    "Q_b",
    "quotient_compatibility",
    "H_phys",
    "positivity_certificate",
    "source_log",
    "forbidden_import_screen",
    "decision",
}

REQUIRED_REMOVED_ROLES = {
    "EOM_b",
    "Gauge_b",
    "Constraint_b",
    "Ghost_b",
    "Null_b",
}

REQUIRED_CURRENT_MISSING = {
    "base_field": "missing",
    "source_projector_P_fin_b": "missing",
    "raw_mode_records": "missing",
    "mode_provenance": "missing",
    "mode_support": "missing",
    "H_raw": "missing",
    "Q_b": "missing",
    "quotient_compatibility": "not_checkable",
    "H_phys": "not_computable",
    "positivity_certificate": "missing",
    "source_log": "missing",
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

REQUIRED_DECISION_KEYS = {
    "missing_P_fin_b": "blocked",
    "missing_16_gu_derived_local_modes": "blocked",
    "missing_local_support": "fail_local_observer_input",
    "missing_H_raw": "blocked",
    "H_raw_not_Hermitian": "fail_raw_Gram",
    "missing_removed_direction_roles": "blocked",
    "missing_Q_b": "blocked",
    "Q_b_not_full_column_rank": "fail_quotient_execution",
    "R_star_H_raw_Q_nonzero": "fail_gauge_EOM_constraint_leakage",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail_physical_Gram_computation",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_report_quotient_erased_branch",
    "identity_Gram_without_source_log": "import_control",
    "Bell_Pauli_free_vacuum_or_CHSH_target_used": "rollback_target_import",
    "direct_sum_silently_used_as_tensor_product": "rollback_tensor_product_import",
    "clean_packet_H_phys_psd_nonzero_rank": "promote_positive_finite_seed_only",
    "clean_positive_seed_plus_later_source_covariance": "advance_to_covariance_gate_not_CHSH_claim",
}

FORBIDDEN_PROMOTION_CLAIMS = [
    r"\bH_phys is computed from current sources\b",
    r"\bcurrent sources compute H_phys\b",
    r"\bpositive finite seed is promoted\b",
    r"\bpositive seed promoted\b",
    r"\bsource-derived covariance is promoted\b",
    r"\brho_AB is supplied\b",
    r"\bCHSH violation is derived\b",
    r"\bOBS-CHSH is upgraded\b",
    r"\bQFT recovery is closed\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source-mode quotient ledger artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle2QFTSourceModeQuotientDataLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_H_phys_covariance_and_chsh_promotion(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_AND_MODE_QUOTIENT_PACKET",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertEqual(self.summary["finite_gram_gate_status"], "still_blocked")
        self.assertIs(self.summary["can_compute_H_phys_from_current_sources"], False)
        self.assertIs(self.summary["positive_seed_promoted"], False)
        self.assertIs(self.summary["covariance_promoted"], False)
        self.assertIs(self.summary["chsh_promoted"], False)
        self.assertIs(self.summary["not_a_chsh_or_qft_recovery_claim"], True)
        for pattern in FORBIDDEN_PROMOTION_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion claim matched: {pattern}",
            )

    def test_K_b_is_only_the_16_dimensional_Pati_Salam_carrier(self) -> None:
        carrier = self.summary["K_b"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertIn("representation_carrier_only", carrier["status"])

    def test_required_ledger_fields_and_removed_roles_are_complete(self) -> None:
        fields = set(self.summary["required_ledger_fields"])
        self.assertTrue(REQUIRED_LEDGER_FIELDS.issubset(fields))
        roles = set(self.summary["removed_direction_roles"])
        self.assertEqual(roles, REQUIRED_REMOVED_ROLES)
        for role in REQUIRED_REMOVED_ROLES:
            self.assertIn(role, self.text)

    def test_current_source_supply_marks_mode_Gram_and_quotient_data_missing(self) -> None:
        supply = self.summary["current_source_supply"]
        self.assertEqual(supply["sector_id"], "named")
        self.assertEqual(supply["carrier_spec"], "named_as_representation_carrier")
        for key, expected in REQUIRED_CURRENT_MISSING.items():
            self.assertEqual(supply[key], expected, key)
        for role in REQUIRED_REMOVED_ROLES:
            self.assertEqual(supply["R_b_removed_representatives"][role], "missing")
        self.assertEqual(supply["removed_direction_roles"], "named_but_not_represented")
        self.assertIs(supply["enough_to_compute_H_phys"], False)

    def test_current_files_establish_controls_but_not_source_data(self) -> None:
        established = set(self.summary["what_current_files_establish"])
        for required in [
            "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
            "formal_quotient_roles_EOM_gauge_constraint_ghost_null",
            "finite_formula_H_phys_equals_Q_star_H_raw_Q",
            "identity_Gram_is_control_only_without_source_derivation",
            "CHSH_fixture_controls_pass_but_GU_state_and_observables_are_pending",
            "strongest_CHSH_candidate_states_are_ansatz_not_GU_derived",
        ]:
            self.assertIn(required, established)

    def test_strongest_positive_attempt_is_a_ledger_shell_and_identity_control_is_rejected(self) -> None:
        attempt = self.summary["strongest_positive_data_attempt"]
        self.assertEqual(attempt["status"], "ledger_shell_only")
        for available in [
            "sector_id",
            "carrier_spec",
            "basis_label_pattern",
            "forbidden_import_screen",
        ]:
            self.assertIn(available, attempt["available_entries"])
        for missing in [
            "source_projector_P_fin_b",
            "raw_mode_records",
            "mode_provenance",
            "mode_support",
            "H_raw",
            "R_b_removed_representatives",
            "Q_b",
            "H_phys",
            "source_log",
        ]:
            self.assertIn(missing, attempt["missing_entries"])
        control = attempt["control_identity_packet"]
        self.assertEqual(control["H_raw_control"], "I_16")
        self.assertEqual(control["Q_b_control"], "I_16")
        self.assertEqual(control["H_phys_control"], "I_16")
        self.assertEqual(control["decision"], "import_control")
        self.assertIn("forbidden_without_source_log", control["promotion"])

    def test_first_exact_missing_object_is_P_fin_b_with_local_modes(self) -> None:
        missing = self.summary["first_exact_missing_object"]
        self.assertEqual(missing["id"], "SourceProjectorPFinBWithLocalModeRecords")
        self.assertEqual(
            missing["formal_name"],
            "P_fin^b_and_16_gu_derived_local_source_mode_records",
        )
        self.assertIn("does_not_identify_which_local_source_modes", missing["why_first"])
        for required in [
            "P_fin_b_from_F_phys_b_O_to_K_b",
            "exactly_16_mode_records",
            "raw_representatives",
            "representation_slots",
            "local_support_or_local_algebra_inclusion",
            "provenance_beginning_gu_derived",
            "source_branch_operator_section_constraint_reference",
        ]:
            self.assertIn(required, missing["must_emit"])
        self.assertEqual(missing["next_blocker_if_supplied_without_Gram"], "SourceRawGramRuleAndMatrix")
        self.assertEqual(
            missing["next_blocker_if_Gram_supplied_without_quotient"],
            "FinitePhysicalQuotientRepresentatives",
        )

    def test_H_phys_covariance_and_chsh_impact_stays_unpromoted(self) -> None:
        impact = self.summary["H_phys_covariance_chsh_impact"]
        self.assertEqual(impact["H_phys"], "not_computable_without_H_raw_and_Q_b")
        self.assertIn("no_source_derived_H_phys", impact["covariance"])
        self.assertEqual(impact["rho_AB"], "missing")
        self.assertEqual(impact["CHSH"], "parked")
        self.assertEqual(
            impact["positive_H_phys_would_promote_only"],
            "positive_finite_one_particle_seed",
        )
        for forbidden in [
            "quasifree_covariance",
            "QFT_state",
            "rho_AB",
            "Alice_Bob_tensor_product_reduction",
            "GU_admissible_observables",
            "CHSH_violation",
        ]:
            self.assertIn(forbidden, impact["positive_H_phys_would_not_promote"])

    def test_forbidden_target_imports_cover_identity_bell_free_vacuum_and_tensor_imports(self) -> None:
        forbidden = set(self.summary["forbidden_target_imports"])
        self.assertTrue(REQUIRED_FORBIDDEN_IMPORTS.issubset(forbidden))
        for term in [
            "identity Gram",
            "Bell state",
            "Pauli",
            "standard free vacuum",
            "Hadamard/Fock",
            "target CHSH",
            "direct sum",
        ]:
            self.assertRegex(self.text, re.escape(term), term)

    def test_decision_table_has_clear_blocked_fail_import_and_promotion_outcomes(self) -> None:
        table = self.summary["decision_table"]
        for key, expected in REQUIRED_DECISION_KEYS.items():
            self.assertEqual(table[key], expected, key)
        outcomes = set(table.values())
        self.assertIn("blocked", outcomes)
        self.assertIn("import_control", outcomes)
        self.assertIn("promote_positive_finite_seed_only", outcomes)
        self.assertTrue(any(value.startswith("fail") for value in outcomes))
        self.assertTrue(any(value.startswith("rollback") for value in outcomes))

    def test_next_computation_is_source_mode_quotient_packet_not_chsh_fixture(self) -> None:
        next_step = self.summary["next_meaningful_finite_computation"]
        self.assertEqual(next_step["id"], "exact_source_mode_quotient_packet_for_K_b")
        self.assertEqual(next_step["input_packet"], "SourceModeQuotientPacket")
        self.assertEqual(
            next_step["packet_id"],
            "source_mode_quotient_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0",
        )
        for step in [
            "verify_exactly_16_mode_records",
            "verify_all_mode_provenance_starts_gu_derived",
            "verify_local_support_or_local_algebra_inclusion",
            "reject_forbidden_source_strings",
            "verify_H_raw_equals_H_raw_star",
            "verify_removed_roles_present_or_source_proved_empty",
            "verify_Q_b_full_column_rank",
            "verify_R_star_H_raw_Q_equals_zero",
            "compute_H_phys_equals_Q_star_H_raw_Q",
            "certify_H_phys_positive_semidefinite_exactly",
            "verify_rank_H_phys_positive",
            "emit_decision_table_outcome",
        ]:
            self.assertIn(step, next_step["steps"])
        self.assertEqual(next_step["first_promotable_output"], "PositiveFiniteOneParticleSeed_K_b")
        for not_yet in ["quasifree_covariance", "QFT_state", "rho_AB", "CHSH_violation"]:
            self.assertIn(not_yet, next_step["not_yet"])


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "finite_gram_gate_status": summary["finite_gram_gate_status"],
        "can_compute_H_phys_from_current_sources": summary[
            "can_compute_H_phys_from_current_sources"
        ],
        "first_exact_missing_object": summary["first_exact_missing_object"]["id"],
        "next_computation": summary["next_meaningful_finite_computation"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the hourly Cycle 2 QFT source-mode quotient data ledger."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle2QFTSourceModeQuotientDataLedgerAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
