#!/usr/bin/env python3
"""Audit the Cycle 1 positive physical two-point certificate.

This is a structural audit, not a proof of QFT recovery. It checks that the
artifact explicitly specifies PositivePhysicalTwoPointCertificate(b), keeps the
positivity inequalities visible, forbids imported-vacuum shortcuts, treats
Barandes/Stinespring only as a comparator/null model unless GU sources the
channel, and makes verdict plus rollback conditions machine readable.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "cycle1-qft-positive-two-point-certificate-2026-06-24.md"

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What The Repo Already Supplies",
    "## 3. Candidate Construction Of `K_b`, `h_b`, `C_b`, And `omega_b` If Possible",
    "## 4. Positivity, Locality, Gauge/Null Quotient, And Observable Gates",
    "## 5. First Exact Obstruction",
    "## 6. What This Means For The Steelman Anti-Quantize-Gravity Direction",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

FORBIDDEN_RECOVERY_CLAIMS = [
    r"(?<!not a )\bQFT recovery claim\b",
    r"\bQFT is recovered\b",
    r"\bQFT recovery is closed\b",
    r"\bGU recovers QFT\b",
    r"\bhas recovered QFT\b",
    r"\bsource-derived certificate: closed\b",
]

REQUIRED_CERTIFICATE_TERMS = [
    "PositivePhysicalTwoPointCertificate(b)",
    "QFT-SSX-PS-LR-QUASIFREE-v0",
    "K_b",
    "h_b",
    "C_b",
    "W_b",
    "omega_b",
    "GNS_b",
    "PhysicalFieldComplexAndPositivePairingSeed(b)",
]

REQUIRED_POSITIVITY_TEXT = [
    "h_b(f, f) >= 0",
    "0 <= C_b <= I_b",
    "0 <= h_b(f, C_b f) <= h_b(f, f)",
    "0 <= h_b(f, (I_b - C_b) f) <= h_b(f, f)",
    "H >= 0",
    "0 <= Gamma <= H",
    "rho_AB >= 0",
    "Tr(rho_AB) = 1",
]

REQUIRED_FORBIDDEN_SHORTCUTS = {
    "claiming_QFT_recovery_from_certificate_shell",
    "using_representation_labels_as_quantum_state",
    "copying_Bell_state_into_GU_slot",
    "using_Pauli_controls_as_GU_observables",
    "imported_free_Dirac_vacuum",
    "imported_Hadamard_or_Fock_vacuum",
    "chosen_CPTP_or_Stinespring_channel_as_GU_source",
    "Barandes_correspondence_as_state_derivation",
}

REQUIRED_ROLLBACKS = {
    "rollback_seed_missing",
    "rollback_indefinite_pairing",
    "rollback_covariance_missing",
    "rollback_covariance_not_positive",
    "rollback_imported_vacuum",
    "rollback_target_smuggling",
    "rollback_barandes_overuse",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing positive two-point certificate: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class Cycle1PositiveTwoPointCertificateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_no_qft_recovery_claim_is_made(self) -> None:
        self.assertIs(self.summary["qft_recovered"], False)
        self.assertIs(self.summary["not_a_qft_recovery_claim"], True)
        self.assertFalse(self.summary["can_construct_from_current_repo"])
        for pattern in FORBIDDEN_RECOVERY_CLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden recovery claim matched: {pattern}",
            )

    def test_positive_physical_two_point_certificate_is_explicit(self) -> None:
        self.assertEqual(self.summary["certificate_id"], "PositivePhysicalTwoPointCertificate")
        self.assertEqual(self.summary["sector_id"], "QFT-SSX-PS-LR-QUASIFREE-v0")
        for term in REQUIRED_CERTIFICATE_TERMS:
            self.assertIn(term, self.text)
        construction = self.summary["candidate_construction"]
        for key in ["K_b", "h_b", "C_b", "W_b", "omega_b", "GNS_b"]:
            self.assertIn(key, construction)

    def test_positivity_inequalities_are_present_in_text_and_json(self) -> None:
        text_no_space = re.sub(r"\s+", "", self.text)
        for inequality in REQUIRED_POSITIVITY_TEXT:
            self.assertIn(inequality, self.text)
            self.assertIn(re.sub(r"\s+", "", inequality), text_no_space)
        json_inequalities = set(self.summary["positivity_inequalities"])
        for inequality in [
            "h_b(f,f)>=0",
            "0<=C_b<=I_b",
            "H>=0",
            "0<=Gamma<=H",
            "rho_AB>=0",
            "Tr(rho_AB)=1",
        ]:
            self.assertIn(inequality, json_inequalities)

    def test_imported_vacuum_and_target_shortcuts_are_forbidden(self) -> None:
        forbidden = set(self.summary["forbidden_shortcuts"])
        self.assertTrue(REQUIRED_FORBIDDEN_SHORTCUTS.issubset(forbidden))
        for pattern in [
            r"standard free\s+Dirac state",
            r"standard free vacuum",
            r"Hadamard",
            r"Bell state",
            r"Pauli",
            r"ansatz",
        ]:
            self.assertRegex(self.text, pattern)

    def test_barandes_stinespring_is_comparator_or_null_model_only(self) -> None:
        role = self.summary["barandes_stinespring_role"]
        self.assertEqual(role["allowed_role"], "comparator_null_model_only")
        self.assertIs(role["may_source_channel"], False)
        self.assertIn("GU_independently_derives", role["exception"])
        self.assertIn("Barandes/Stinespring belongs here only as a comparator and null model", self.text)
        self.assertIn("It cannot source `C_b` or `omega_b` unless GU", self.text)

    def test_verdict_and_rollback_conditions_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_AT_PHYSICAL_FIELD_COMPLEX_AND_POSITIVE_PAIRING_SEED",
        )
        self.assertEqual(self.summary["status"], "blocked")
        rollbacks = set(self.summary["rollback_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollbacks))
        self.assertGreaterEqual(len(rollbacks), 8)

    def test_first_obstruction_is_before_covariance(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "PhysicalFieldComplexAndPositivePairingSeed")
        self.assertIn("C_b_is_a_physical_positive_contraction_only_after_K_b_and_h_b_exist", obstruction["why_first"])
        for item in ["D_phys_b", "F_phys_b_O", "h_b", "K_b_O", "proof_h_b_positive_on_quotient"]:
            self.assertIn(item, obstruction["must_emit"])

    def test_smallest_worked_check_is_real_and_finite(self) -> None:
        check = self.summary["smallest_worked_check"]
        self.assertEqual(check["id"], "finite_source_mode_positive_contraction_check")
        self.assertIn("one_source_selected_left_mode", check["minimal_modes"])
        self.assertIn("H_ij=h_b(e_i,e_j)", check["inputs"])
        self.assertIn("Gamma_ij=W_b(e_i,e_j)", check["inputs"])
        for required in [
            "H_positive_semidefinite",
            "Gamma_positive_semidefinite",
            "H_minus_Gamma_positive_semidefinite",
            "generalized_eigenvalues_in_unit_interval",
            "no_forbidden_provenance",
        ]:
            self.assertIn(required, check["checks"])

    def test_next_step_targets_seed_then_contraction_check(self) -> None:
        self.assertEqual(
            self.summary["next_step"],
            "derive_or_refute_PhysicalFieldComplexAndPositivePairingSeed_then_run_finite_source_mode_positive_contraction_check",
        )
        self.assertIn("finite source-mode seed check", self.text)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(Cycle1PositiveTwoPointCertificateAudit)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
