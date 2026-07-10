#!/usr/bin/env python3
"""Audit the Mission A Lambda/dark-energy provenance construction artifact.

This is a structural text/provenance audit, not a cosmology computation. It
checks that the artifact defines the required certificate, uses theta/IG source
language, keeps xi_eff provenance and DESI/Rubin anti-fitting explicit, forbids
bare Lambda promotion, includes rollback conditions, and does not claim that GU
has already derived dark energy or cancelled Lambda.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "dark-energy-cosmology" / "mission-a-lambda-dark-energy-provenance-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. If GU Is Correct, What Lambda/Dark-Energy Object Must Exist",
    "## 3. Candidate Source-Derived Route From Theta/IG Data",
    "## 4. Term Classification",
    "## 5. Anti-Fitting Protocol For DESI/Rubin-Style Target Windows",
    "## 6. First Exact Obstruction Or Missing Proof Object",
    "## 7. Constructive Next Computation",
    "## 8. Claim Certificate Table And Machine-Readable Summary",
]

REQUIRED_ANTI_FIT_ITEMS = {
    "branch_freeze_before_targets",
    "coefficient_provenance_lock",
    "target_quarantine",
    "replacement_withheld_target_check",
    "negative_control_branches",
    "post_derivation_comparison_only",
    "rollback_on_target_leakage",
}

REQUIRED_ROLLBACKS = {
    "S_IG_dyn_absent_or_not_source_forced",
    "Z_U_or_V_target_selected",
    "theta_eff_not_conserved",
    "no_FLRW_scalar_mode",
    "C_Rtheta_inserted_by_hand",
    "xi_eff_fitted_after_target_data",
    "DESI_Rubin_target_used_upstream",
    "bare_Lambda_inserted_as_source_derivation",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bGU\s+(?:has\s+)?derives?\s+Lambda\b",
    r"\bGU\s+(?:has\s+)?cancels?\s+Lambda\b",
    r"\bGU\s+(?:has\s+)?derived\s+dark energy\b",
    r"\bGU\s+(?:has\s+)?solved\s+dark energy\b",
    r"\bLambda\s+is\s+derived\s+by\s+GU\b",
    r"\bdark energy\s+is\s+derived\s+by\s+GU\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Lambda/dark-energy artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Claim Certificate Table And Machine-Readable Summary\s*.*?```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable summary JSON block")
    return json.loads(match.group(1))


class LambdaDarkEnergyProvenanceAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_certificate_object_is_explicit_and_not_closed(self) -> None:
        self.assertIn("LambdaDarkEnergyProvenanceCertificate", self.text)
        cert = self.summary["lambda_dark_energy_provenance_certificate"]
        self.assertEqual(cert["id"], "LambdaDarkEnergyProvenanceCertificate")
        self.assertTrue(cert["required"])
        self.assertTrue(cert["branch_local"])
        self.assertTrue(cert["same_source_required"])
        self.assertEqual(cert["current_status"], "specified_not_closed")
        self.assertEqual(self.summary["current_status"], "specified_open_not_derived")

    def test_theta_ig_and_total_current_route_are_present(self) -> None:
        route = self.summary["candidate_route"]
        self.assertEqual(route["strongest_dynamic_route"], "Branch_3_dynamical_IG_total_current")
        self.assertEqual(route["source_law"], "D_A^*F_A=theta_eff")
        for needle in ["theta/IG", "theta_eff", "D_A^* F_A = theta_eff", "Branch 2A", "Branch 3"]:
            self.assertIn(needle, self.text)
        for required in ["S_IG_dyn", "theta", "U_or_P_IG", "observer_projection"]:
            self.assertIn(required, route["required_fields"])

    def test_xi_eff_provenance_is_required_not_fitted(self) -> None:
        cert = self.summary["lambda_dark_energy_provenance_certificate"]
        self.assertTrue(cert["no_fitted_xi_eff"])
        self.assertIn("xi_eff = C_Rtheta / Z_theta", self.text)
        chain = self.summary["candidate_route"]["coefficient_chain"]
        for required in ["Z_theta", "C_Rtheta", "xi_eff"]:
            self.assertIn(required, chain)
        classes = self.summary["term_classifications"]
        self.assertEqual(classes["xi_eff"], "undefined_not_generated")
        self.assertIn("fitted_xi_eff", self.summary["constructive_next_computation"]["forbidden_inputs"])

    def test_desi_rubin_anti_fitting_protocol_is_machine_readable(self) -> None:
        cert = self.summary["lambda_dark_energy_provenance_certificate"]
        self.assertTrue(cert["no_desi_rubin_target_input"])
        self.assertIn("DESI/Rubin", self.text)
        self.assertTrue(REQUIRED_ANTI_FIT_ITEMS.issubset(set(self.summary["anti_fitting_protocol"])))
        forbidden = set(self.summary["constructive_next_computation"]["forbidden_inputs"])
        self.assertIn("DESI_Rubin_target_window", forbidden)

    def test_no_bare_lambda_promotion(self) -> None:
        cert = self.summary["lambda_dark_energy_provenance_certificate"]
        self.assertTrue(cert["no_bare_lambda"])
        classes = self.summary["term_classifications"]
        self.assertEqual(classes["bare_Lambda"], "forbidden_as_source_derivation")
        forbidden = set(self.summary["constructive_next_computation"]["forbidden_inputs"])
        self.assertIn("bare_Lambda", forbidden)
        self.assertIn("no bare Lambda", self.text)

    def test_rollback_conditions_cover_dark_energy_failure_modes(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        self.assertTrue(REQUIRED_ROLLBACKS.issubset(rollbacks))
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(obstruction["dynamic_route"], "missing_DynamicIGDarkEnergyCoefficientPacket")
        self.assertEqual(obstruction["bare_theta_route"], "missing_Branch2AConstraintTangentCertificate")
        self.assertEqual(obstruction["coefficient_status"], "no_generated_Z_theta_C_Rtheta_xi_eff")

    def test_no_solution_or_cancellation_claim_is_made(self) -> None:
        cert = self.summary["lambda_dark_energy_provenance_certificate"]
        claims = self.summary["claim_status"]
        self.assertFalse(cert["broad_lambda_solution_claimed"])
        self.assertFalse(claims["GU_dark_energy_derived"])
        self.assertFalse(claims["GU_Lambda_cancelled"])
        self.assertFalse(claims["source_derived_dynamic_candidate_constructed"])
        self.assertTrue(claims["certificate_shape_defined"])
        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE), pattern)

    def test_summary_verdict_stays_open(self) -> None:
        verdict = self.summary["verdict"]
        self.assertIn("BLOCKED_BEFORE_COEFFICIENTS", verdict)
        self.assertNotIn("RESOLVED", verdict)
        self.assertNotIn("CLOSED", verdict)
        self.assertIn("not closed", self.text)
        self.assertIn("not a derived stress tensor today", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
