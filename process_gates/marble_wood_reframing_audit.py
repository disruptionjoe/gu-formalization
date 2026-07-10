#!/usr/bin/env python3
"""Audit the marble/wood source-geometry reframing contract.

This is a structural contract audit, not a proof of GU. It checks that the
artifact keeps Einstein's marble/wood framing tied to a same-source
source-to-shadow proof burden, includes forbidden shortcuts and rollback
conditions, and avoids prohibited overclaims.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "marble-wood-source-geometry-reframing-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Plain-English Translation",
    "## 3. What Changes Relative To Prior Contracts",
    "## 4. What Does Not Change",
    "## 5. Claim Certificate Table",
    "## 6. Machine-Readable Contract Block",
    "## 7. Next Meaningful Proof/Computation Step",
]

REQUIRED_CLAIMS = {
    "MW-FRAMING": "conditional_contract",
    "MARBLE-PREMATURITY-HYPOTHESIS": "heterodox_open",
    "MARBLE-GR-SHADOW": "specified_open",
    "LAMBDA-PATCH-DARK-ENERGY": "open_patch_slot",
    "WOOD-QFT-MATTER-SHADOW": "blocked_open",
    "SAME-SOURCE-DUAL-SHADOW": "required_next_burden",
    "MEASUREMENT-RECORD-SHADOW": "controls_only",
}

REQUIRED_UNCHANGED = {
    "GR_shadow_recovery",
    "QFT_shadow_recovery",
    "SM_finite_control",
    "cosmology_theta_xi_dark_energy_provenance",
    "measurement_state_and_observables",
    "anomaly_shadow",
    "exact_solution_tests",
    "provenance_and_rollback",
}

REQUIRED_FORBIDDEN = {
    "reframe_as_physics_proof",
    "metric_quantization_as_primary_start",
    "source_geometry_by_name_only",
    "compatibility_as_recovery",
    "weak_field_as_exact_GR",
    "bare_Lambda_as_marble",
    "dark_energy_fit_as_derivation",
    "Lambda_residual_absorber",
    "fitted_xi_eff_as_source",
    "hidden_matter_relabeling",
    "qft_recovery_by_slogan",
    "representation_labels_as_quantum_state",
    "host_as_selector",
    "ansatz_state_as_measurement",
    "observer_finality_as_physics_escape",
    "separate_branch_splicing",
    "wood_imported_after_marble",
    "marble_assumed_after_wood",
}

PROHIBITED_OVERCLAIMS = [
    "GU solves quantum gravity",
    "Einstein equation recovered",
]

NEGATION_GUARDS = [
    "not ",
    "does not ",
    "do not ",
    "forbidden",
    "cannot ",
    "no current ",
]


def read_doc() -> str:
    return DOC.read_text(encoding="utf-8")


def extract_contract(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 6\. Machine-Readable Contract Block\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable marble/wood JSON block")
    return json.loads(match.group(1))


class MarbleWoodReframingAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.lower_text = cls.text.lower()
        cls.contract = extract_contract(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_decision_are_contract_not_proof(self) -> None:
        self.assertEqual(self.contract["artifact"], "MARBLE_WOOD_SOURCE_GEOMETRY_REFRAMING_CONTRACT")
        self.assertEqual(self.contract["verdict"], "conditional")
        self.assertEqual(
            self.contract["decision"],
            "REFRAME_SHARPENS_NEXT_PROOF_BURDEN_NOT_PROOF_OF_RECOVERY",
        )
        self.assertIn("contract-open", self.text)
        self.assertIn("does not close GR-SHADOW", self.text)

    def test_marble_wood_and_same_source_shadow_language_present(self) -> None:
        for needle in [
            "marble",
            "wood",
            "same-source",
            "same source geometry",
            "source-to-shadow",
            "R_marble",
            "R_wood",
            "LambdaPatchProvenanceCertificate",
        ]:
            self.assertIn(needle.lower(), self.lower_text)

        terms = self.contract["terms"]
        self.assertEqual(set(terms), {"marble", "lambda_patch", "wood", "source_geometry_shadow"})
        self.assertIn("G_mu_nu", terms["marble"]["plain_english"])
        self.assertIn("Lambda g_mu_nu", terms["lambda_patch"]["plain_english"])
        self.assertEqual(
            terms["lambda_patch"]["required_certificate"],
            "LambdaPatchProvenanceCertificate",
        )
        self.assertIn(
            "R_marble_and_R_wood_consume_the_same_branch_fixed_G_src",
            terms["source_geometry_shadow"]["same_source_requirement"],
        )

    def test_prior_contract_delta_is_the_dual_shadow_burden(self) -> None:
        changed = set(self.contract["changed_relative_to_prior_contracts"])
        for required in [
            "fix_wood_or_quantize_marble_replaced_by_same_source_derivation",
            "not_quantized_gr_reframe_strengthened_to_dual_shadow_burden",
            "metric_marble_audited_as_possible_shadow_not_primitive",
            "lambda_patch_separated_from_principled_marble",
            "matter_wood_cannot_be_phenomenological_rhs_input",
            "next_proof_object_must_bind_R_marble_and_R_wood_to_one_branch",
        ]:
            self.assertIn(required, changed)

        self.assertEqual(set(self.contract["unchanged_obligations"]), REQUIRED_UNCHANGED)

    def test_claim_certificates_include_citation_forbidden_and_rollback(self) -> None:
        claims = {claim["id"]: claim for claim in self.contract["claim_certificates"]}
        self.assertEqual(set(claims), set(REQUIRED_CLAIMS))

        for claim_id, expected_status in REQUIRED_CLAIMS.items():
            claim = claims[claim_id]
            self.assertEqual(claim["status"], expected_status)
            self.assertTrue(claim["allowed_citation"])
            self.assertGreaterEqual(len(claim["forbidden_shortcuts"]), 3)
            self.assertGreaterEqual(len(claim["rollback_conditions"]), 1)

        self.assertIn("SAME-SOURCE-DUAL-SHADOW", claims)
        self.assertIn("WOOD-QFT-MATTER-SHADOW", claims)
        self.assertIn("MARBLE-GR-SHADOW", claims)

    def test_forbidden_shortcuts_and_rollback_are_explicit(self) -> None:
        forbidden = set(self.contract["forbidden_shortcuts"])
        self.assertTrue(REQUIRED_FORBIDDEN.issubset(forbidden))

        self.assertIn("### Forbidden Shortcuts", self.text)
        self.assertIn("### Rollback Rule", self.text)
        self.assertIn("rollback conditions", self.lower_text)

    def test_currently_open_and_progress_criteria_are_decision_grade(self) -> None:
        currently_open = set(self.contract["currently_open"])
        for required in [
            "same_source_dual_shadow_theorem",
            "ELProjectedGRShadowTheorem",
            "LambdaPatchProvenanceCertificate",
            "QFTStateSpaceExtractionCertificate",
            "QFTStateExtractionCertificate",
            "ObservableAdmissibilityCertificate",
            "Phi_SG_MG_source_geometry_finite_control_selector",
            "AnomalyShadowCertificate",
            "GU_measurement_channel",
        ]:
            self.assertIn(required, currently_open)

        progress = set(self.contract["progress_criteria"])
        self.assertIn("one_branch_fixed_G_src", progress)
        self.assertIn("R_marble_full_EL_projection_and_exact_solution_witnesses", progress)
        self.assertIn("Lambda_eff_zero_imported_or_source_derived_with_anti_fitting_test", progress)
        self.assertIn("R_wood_positive_state_observables_matter_selector_and_anomaly_audit", progress)
        self.assertIn("binary_rollback_matrix", progress)

    def test_next_step_is_dual_shadow_packet(self) -> None:
        next_step = self.contract["next_step"]
        self.assertEqual(next_step["id"], "DualShadowDerivationPacketV0")
        must_emit = set(next_step["must_emit"])
        for required in [
            "SourceBranchClosureCertificate",
            "R_marble_certificate",
            "R_Lambda_patch_certificate",
            "R_wood_certificate",
            "shared_provenance_ledger",
            "same_source_loss_ledger",
            "rollback_matrix",
        ]:
            self.assertIn(required, must_emit)

        questions = " ".join(next_step["first_binary_questions"])
        self.assertIn("metric_shadow", questions)
        self.assertIn("Lambda_eff", questions)
        self.assertIn("QFT_matter_shadow", questions)
        self.assertIn("T_shadow_derived", questions)

    def test_prohibited_overclaims_absent_or_explicitly_negated(self) -> None:
        for phrase in PROHIBITED_OVERCLAIMS:
            for match in re.finditer(re.escape(phrase), self.text, flags=re.IGNORECASE):
                start = max(0, match.start() - 96)
                context = self.text[start : match.start()].lower()
                if not any(guard in context for guard in NEGATION_GUARDS):
                    self.fail(f"prohibited overclaim not negated: {phrase!r}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
