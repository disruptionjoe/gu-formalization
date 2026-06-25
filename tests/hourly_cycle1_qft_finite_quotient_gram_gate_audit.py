#!/usr/bin/env python3
"""Audit the hourly Cycle 1 QFT finite quotient-Gram gate.

This is a structural audit, not a positivity proof. It checks that the artifact
keeps the finite Gram data contract explicit, marks current GU-derived inputs as
missing, forbids identity/Bell/free-vacuum promotion, and does not make a CHSH
claim before a source-derived state and observables exist.
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
    / "hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. Strongest Positive Finite Seed Construction",
    "## 4. First Exact Obstruction Or Missing Object",
    "## 5. Failure Modes: Negative Norm, Gauge Leakage, Imported Identity Gram, Nonlocal Finite Modes",
    "## 6. Impact For CHSH/Observer Forcing",
    "## 7. Next Meaningful Finite Computation",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_CURRENT_MISSING = {
    "gu_derived_mode_provenance": "missing_individual_modes",
    "source_extraction_map_P_fin_b": "missing",
    "H_raw": "missing",
    "Q_b": "missing",
    "removed_direction_representatives": "missing",
    "H_phys": "not_computed",
    "positive_H_phys": "not_established",
}

REQUIRED_GRAM_FIELDS = {
    "branch_id",
    "base_field",
    "raw_basis",
    "mode_provenance",
    "mode_support",
    "source_extraction_map_P_fin_b",
    "H_raw",
    "R_b_removed_direction_matrix",
    "removed_direction_roles",
    "Q_b",
    "H_phys",
    "source_log",
}

REQUIRED_FINITE_CHECKS = {
    "all_mode_provenance_starts_gu_derived",
    "no_forbidden_provenance",
    "H_raw_equals_H_raw_star",
    "Q_b_full_column_rank",
    "R_star_H_raw_Q_equals_zero",
    "H_phys_equals_Q_star_H_raw_Q",
    "H_phys_equals_H_phys_star",
    "H_phys_positive_semidefinite_exact_certificate",
    "rank_H_phys_positive",
    "surviving_modes_inside_Pati_Salam_LR_block",
    "local_support_not_global_nonlocal_fixture",
}

REQUIRED_FORBIDDEN_PROMOTIONS = {
    "imported_identity_Gram_as_GU_derivation",
    "Pati_Salam_labels_as_positive_pairing",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_CHSH_state_or_covariance",
    "Stinespring_or_CPTP_channel_as_GU_source_without_GU_derivation",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bsource-derived positive finite seed is constructed\b",
    r"\bpositive H_phys is established\b",
    r"\bGU-derived H_raw is supplied\b",
    r"\bQ_b is supplied\b",
    r"\bOBS-CHSH is upgraded\b",
    r"\bCHSH violation is derived\b",
    r"\bQFT recovery is closed\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing finite quotient-Gram artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class HourlyCycle1QFTFiniteQuotientGramGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_blocks_promotion_and_recovery_claims(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_AT_SOURCE_DERIVED_FINITE_QUOTIENT_GRAM_DATA",
        )
        self.assertEqual(self.summary["status"], "blocked")
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["positive_seed_promoted"], False)
        self.assertIs(self.summary["chsh_claimed"], False)
        self.assertIs(self.summary["not_a_chsh_or_qft_recovery_claim"], True)
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive claim matched: {pattern}",
            )

    def test_K_b_is_exactly_the_finite_direct_sum_carrier(self) -> None:
        carrier = self.summary["K_b"]
        self.assertEqual(carrier["formula"], "K_b=V_L direct_sum V_R")
        self.assertEqual(carrier["V_L"], "(4,2,1)")
        self.assertEqual(carrier["V_R"], "(4bar,1,2)")
        self.assertEqual(carrier["dim_C_V_L"], 8)
        self.assertEqual(carrier["dim_C_V_R"], 8)
        self.assertEqual(carrier["dim_C_K_b"], 16)
        self.assertIn("representation_carrier_only", carrier["status"])

    def test_current_repo_supply_marks_all_finite_Gram_inputs_missing(self) -> None:
        supply = self.summary["current_repo_supply"]
        for key, expected in REQUIRED_CURRENT_MISSING.items():
            self.assertEqual(supply[key], expected, key)
        self.assertEqual(supply["identity_Gram"], "control_only_if_inserted")
        self.assertEqual(supply["rho_AB"], "missing")
        self.assertEqual(supply["gu_admissible_observables"], "missing")

    def test_strongest_positive_seed_is_only_an_identity_control(self) -> None:
        seed = self.summary["strongest_positive_finite_seed_construction"]
        self.assertEqual(seed["control_carrier"], "C^8_L direct_sum C^8_R")
        self.assertEqual(seed["control_H_raw"], "I_16")
        self.assertEqual(seed["control_Q_b"], "I_16")
        self.assertEqual(seed["control_H_phys"], "I_16")
        self.assertEqual(seed["control_status"], "finite_linear_algebra_control_not_GU_derivation")
        self.assertIn("source_derived_H_raw_and_Q_b", seed["promotion_condition"])

    def test_first_obstruction_requires_mode_H_Q_representatives_and_H_phys(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceDerivedFiniteQuotientGramData")
        self.assertIn("PhysicalFieldComplexAndPositivePairingSeed", obstruction["inside"])
        self.assertIn("SourceDerivedPositivePairingOnQuotient", obstruction["inside"])
        for required in [
            "gu_derived_finite_mode_provenance",
            "source_extraction_map_P_fin_b",
            "H_raw",
            "Q_b",
            "EOM_gauge_constraint_ghost_null_representatives",
            "H_phys",
            "positive_semidefinite_nonzero_rank_certificate",
            "local_support_data",
        ]:
            self.assertIn(required, obstruction["must_emit"])

    def test_finite_Gram_fields_and_exact_base_fields_are_enforced(self) -> None:
        contract = self.summary["finite_gram_input_contract"]
        self.assertEqual(
            contract["packet_id"],
            "finite_source_quotient_Gram_packet_for_QFT_SSX_PS_LR_QUASIFREE_v0",
        )
        self.assertTrue(REQUIRED_GRAM_FIELDS.issubset(set(contract["required_finite_Gram_fields"])))
        self.assertEqual(
            set(contract["allowed_exact_base_fields"]),
            {"QQ", "QQ_i", "number_field", "symbolic_exact"},
        )
        self.assertEqual(contract["expected_shapes"]["H_raw"], "16x16")
        self.assertEqual(contract["expected_shapes"]["R_b"], "16xm")
        self.assertEqual(contract["expected_shapes"]["Q_b"], "16xr")
        self.assertEqual(contract["expected_shapes"]["H_phys"], "rxr")
        self.assertTrue(REQUIRED_FINITE_CHECKS.issubset(set(contract["finite_checks"])))

    def test_failure_modes_cover_negative_norm_gauge_leakage_identity_and_nonlocality(self) -> None:
        modes = self.summary["failure_modes"]
        self.assertIn("negative_eigenvalue_of_H_phys", modes["negative_norm"])
        self.assertIn("R_star_H_raw_Q_nonzero", modes["gauge_leakage"])
        self.assertIn("I_16_without_source_log", modes["imported_identity_Gram"])
        self.assertIn("global_basis_without_local_support", modes["nonlocal_finite_modes"])
        for term in ["Negative Norm", "Gauge Leakage", "Imported Identity Gram", "Nonlocal Finite Modes"]:
            self.assertIn(term, self.text)

    def test_forbidden_imports_cannot_be_promoted(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertTrue(REQUIRED_FORBIDDEN_PROMOTIONS.issubset(forbidden))
        for term in [
            "identity Gram",
            "Bell state",
            "standard free vacuum",
            "Hadamard/Fock state",
            "Pauli setting",
        ]:
            self.assertIn(term, self.text)

    def test_no_CHSH_claim_before_state_and_observables(self) -> None:
        impact = self.summary["chsh_observer_impact"]
        self.assertEqual(impact["obs_chsh_status"], "parked")
        self.assertEqual(impact["positive_H_phys_would_imply"], "positive_one_particle_seed_only")
        for not_implied in ["rho_AB", "gu_admissible_observables", "CHSH_violation"]:
            self.assertIn(not_implied, impact["positive_H_phys_would_not_imply"])
        for required in [
            "positive_finite_quotient_Gram",
            "source_derived_covariance_or_state",
            "finite_Alice_Bob_reduction",
            "gu_admissible_observables",
            "locality_NAC_for_live_data",
        ]:
            self.assertIn(required, impact["requires_before_chsh_claim"])

    def test_next_computation_decision_table_is_finite_and_non_covariance_first(self) -> None:
        next_step = self.summary["next_meaningful_finite_computation"]
        self.assertEqual(next_step["id"], "exact_finite_source_quotient_Gram_computation_for_K_b")
        self.assertEqual(next_step["input_packet"], "FiniteSourceQuotientGramData")
        self.assertEqual(
            next_step["first_promotable_output"],
            "positive_finite_seed_if_H_phys_psd_nonzero_rank_with_clean_provenance",
        )
        for not_yet in ["quasifree_covariance", "QFT_state", "rho_AB", "CHSH_claim"]:
            self.assertIn(not_yet, next_step["not_yet"])
        table = next_step["decision_table"]
        self.assertEqual(table["missing_H_raw_or_Q_b"], "blocked")
        self.assertEqual(table["identity_Gram_without_source_log"], "import_control")
        self.assertEqual(table["R_star_H_raw_Q_nonzero"], "gauge_leakage_fail")
        self.assertEqual(table["H_phys_negative"], "finite_seed_fail")
        self.assertEqual(table["H_phys_rank_zero"], "quotient_erased_seed")
        self.assertEqual(
            table["H_phys_positive_clean_provenance"],
            "promote_positive_finite_seed_only",
        )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "positive_seed_promoted": summary["positive_seed_promoted"],
        "chsh_claimed": summary["chsh_claimed"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "next_computation": summary["next_meaningful_finite_computation"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the hourly Cycle 1 QFT finite quotient-Gram gate."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle1QFTFiniteQuotientGramGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
