#!/usr/bin/env python3
"""Audit the Cycle 2 QFT physical field and positive pairing seed.

This is a structural audit, not a proof of QFT recovery. It checks that the
artifact specifies the candidate physical complex, quotient, positive pairing,
and finite seed space while keeping positivity underived unless a real source
Gram/adjoint/current is supplied.
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
DOC = REPO_ROOT / "explorations" / "cycle2-qft-physical-field-positive-pairing-seed-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate Physical Complex And Quotient",
    "## 3. Candidate Positive Pairing And Positivity Conditions",
    "## 4. Finite Seed Space `K_b` And What Would Make It Source-Derived",
    "## 5. Failure Modes: Negative Norm, Gauge Leakage, Target-Fitted Vacuum, Nonlocal Observables",
    "## 6. First Exact Obstruction",
    "## 7. Impact For QFT State-Space Extraction",
    "## 8. Next Meaningful Finite Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_TEXT_TERMS = [
    "PhysicalFieldComplexAndPositivePairingSeed(b)",
    "D_phys^b",
    "gauge/null quotient",
    "F_phys^b(O)",
    "h_b",
    "K_b",
    "K_b^fin",
    "V_L = (4,2,1)",
    "V_R = (4bar,1,2)",
    "H_phys >= 0",
    "positivity is imported",
    "not a QFT recovery claim",
]

FORBIDDEN_RECOVERY_CLAIMS = [
    r"\bQFT is recovered\b",
    r"\bQFT recovery is closed\b",
    r"\bGU recovers QFT\b",
    r"\bhas recovered QFT\b",
    r"\bpositive two-point function is GU-derived\b",
    r"\bsource-derived positive pairing is constructed\b",
]

REQUIRED_FORBIDDEN_IMPORTS = {
    "claiming_QFT_recovery_from_seed_shell",
    "using_Pati_Salam_labels_as_a_positive_pairing",
    "setting_H_b_to_identity_as_GU_derivation",
    "imported_free_Dirac_vacuum",
    "imported_Hadamard_or_Fock_vacuum",
    "copying_Bell_state_into_GU_slot",
    "using_Pauli_controls_as_GU_observables",
    "target_fitted_CHSH_covariance",
    "chosen_Barandes_Stinespring_or_CPTP_channel_as_GU_source",
}

REQUIRED_ROLLBACKS = {
    "rollback_primary_operator_mismatch",
    "rollback_missing_physical_quotient",
    "rollback_missing_source_adjoint_or_current",
    "rollback_indefinite_H_phys",
    "rollback_zero_rank_after_quotient",
    "rollback_identity_Gram_imported_as_derivation",
    "rollback_imported_vacuum_or_target_state",
    "rollback_gauge_leakage",
    "rollback_nonlocal_finite_reduction",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 2 QFT seed artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class Cycle2QFTPhysicalFieldPositivePairingSeedAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_no_qft_recovery_or_positive_state_claim_is_made(self) -> None:
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["not_a_qft_recovery_claim"], True)
        self.assertIs(self.summary["can_produce_positive_pairing_from_current_repo"], False)
        for pattern in FORBIDDEN_RECOVERY_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden recovery claim matched: {pattern}",
            )

    def test_required_seed_terms_are_explicit(self) -> None:
        for term in REQUIRED_TEXT_TERMS:
            self.assertIn(term, self.text)
        self.assertEqual(self.summary["seed_id"], "PhysicalFieldComplexAndPositivePairingSeed")
        self.assertEqual(self.summary["sector_id"], "QFT-SSX-PS-LR-QUASIFREE-v0")

    def test_candidate_physical_complex_contains_D_phys_and_PS_data(self) -> None:
        complex_summary = self.summary["candidate_physical_complex"]
        self.assertIn("D_phys_b", complex_summary)
        self.assertIn("D_phys^b", complex_summary["D_phys_b_display"])
        self.assertEqual(complex_summary["status"], "conditional_specification_not_constructed")
        fibers = complex_summary["finite_internal_fibers"]
        self.assertEqual(fibers["V_L"], "(4,2,1)")
        self.assertEqual(fibers["V_R"], "(4bar,1,2)")
        self.assertEqual(fibers["dim_C_V_L"], 8)
        self.assertEqual(fibers["dim_C_V_R"], 8)

    def test_quotient_is_present_and_not_silent(self) -> None:
        quotient = self.summary["quotient"]
        self.assertIn("F_phys^b(O)", quotient["formula"])
        self.assertEqual(quotient["status"], "specified_not_executed")
        for required in [
            "equations_of_motion",
            "gauge_or_BRST_exact_directions",
            "physical_constraints",
            "ghost_or_negative_metric_auxiliaries",
            "radical_of_h_b",
        ]:
            self.assertIn(required, quotient["must_remove"])
        self.assertGreaterEqual(len(quotient["descent_conditions"]), 4)

    def test_positive_pairing_is_not_assumed_silently(self) -> None:
        self.assertIs(self.summary["positivity_not_assumed_silently"], True)
        self.assertIn("not_source_derived", self.summary["positive_pairing_status"])
        pairing = self.summary["candidate_positive_pairing"]
        self.assertEqual(pairing["control_Gram"], "H_b=diag(I_8,I_8)")
        self.assertEqual(pairing["control_Gram_status"], "imported_positive_pairing_not_GU_derived")
        for required in [
            "physical_adjoint_or_fundamental_symmetry_J_b",
            "conserved_current_or_equivalent_Gram_rule",
            "quotient_map_Q_b",
            "proof_no_negative_norm_survivors",
        ]:
            self.assertIn(required, pairing["required_source_data"])
        for condition in ["H_phys>=0", "rank_H_phys>0"]:
            self.assertIn(condition, pairing["positivity_conditions"])

    def test_finite_seed_space_K_b_is_machine_readable(self) -> None:
        seed = self.summary["finite_seed_space"]
        self.assertEqual(seed["K_b"], "K_b^fin=K_L^b direct_sum K_R^b")
        self.assertEqual(seed["K_L_b"], "V_L=(4,2,1)")
        self.assertEqual(seed["K_R_b"], "V_R=(4bar,1,2)")
        self.assertEqual(seed["dimension_complex"], 16)
        self.assertIn("A_b^fin=CAR(K_b,h_b^fin)", seed["algebra_route"])
        for forbidden_not_yet in ["rho_AB", "omega_b", "C_b", "W_b", "GU_admissible_observables"]:
            self.assertIn(forbidden_not_yet, seed["not_yet"])
        for required in [
            "gu_derived_mode_projector_P_fin_b",
            "explicit_quotient_map_Q_b",
            "Gram_matrix_H_b_computed_from_h_b",
            "positivity_proof_H_phys_ge_0",
            "no_target_data",
        ]:
            self.assertIn(required, seed["source_derived_requirements"])

    def test_imported_vacuum_and_target_state_are_forbidden(self) -> None:
        forbidden = set(self.summary["forbidden_imports"])
        self.assertTrue(REQUIRED_FORBIDDEN_IMPORTS.issubset(forbidden))
        for pattern in [
            r"standard free Dirac vacuum",
            r"Hadamard/Fock vacuum",
            r"Bell state",
            r"Pauli",
            r"target-fitted",
            r"Barandes/Stinespring",
        ]:
            self.assertRegex(self.text, pattern)

    def test_verdict_and_rollback_conditions_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_POSITIVITY_IMPORTED_IF_STANDARD_PAIRING_IS_USED",
        )
        self.assertEqual(self.summary["status"], "underdefined")
        rollbacks = set(self.summary["rollback_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollbacks))
        self.assertGreaterEqual(len(rollbacks), 9)

    def test_first_exact_obstruction_is_positive_pairing_on_quotient(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "SourceDerivedPositivePairingOnQuotient")
        self.assertEqual(obstruction["inside"], "PhysicalFieldComplexAndPositivePairingSeed")
        self.assertIn("cannot_compute_or_prove", obstruction["why_first_within_conditional_spine"])
        for required in [
            "D_phys_b",
            "Q_b",
            "J_b_or_conserved_current",
            "h_b",
            "H_phys",
            "proof_H_phys_positive_semidefinite_and_nonzero_rank",
            "gu_derived_provenance",
        ]:
            self.assertIn(required, obstruction["must_emit"])

    def test_next_finite_computation_checks_quotient_Gram_not_covariance_first(self) -> None:
        next_step = self.summary["next_meaningful_finite_computation"]
        self.assertEqual(next_step["id"], "finite_source_quotient_Gram_audit_for_K_b")
        for required in ["mode_basis_with_gu_derived_provenance", "H_raw", "Q_b"]:
            self.assertIn(required, next_step["input_required"])
        for check in [
            "no_forbidden_provenance",
            "H_raw_equals_H_raw_star",
            "quotient_directions_pair_trivially",
            "H_phys_equals_Q_star_H_raw_Q",
            "eigenvalues_H_phys_ge_minus_tolerance",
            "rank_H_phys_positive",
        ]:
            self.assertIn(check, next_step["checks"])
        self.assertIn("covariance_check_after_seed_only", next_step)


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "status": summary["status"],
        "qft_recovered": summary["qft_recovered"],
        "can_produce_positive_pairing_from_current_repo": summary[
            "can_produce_positive_pairing_from_current_repo"
        ],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
        "rollback_count": len(summary["rollback_conditions"]),
        "next_computation": summary["next_meaningful_finite_computation"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the Cycle 2 QFT physical field positive pairing seed."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            Cycle2QFTPhysicalFieldPositivePairingSeedAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
