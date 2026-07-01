#!/usr/bin/env python3
"""Audit the stress-energy shadow emergence certificate.

This is a structural/status audit, not a physics proof. It checks that the
certificate distinguishes derived stress-energy from imported, hosted, ansatz,
residual, and control content; keeps conservation and rollback obligations
explicit; and does not overclaim that T_mu_nu is currently derived.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "stress-energy-shadow-emergence-certificate-2026-06-24.md"

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Derived Stress-Energy Versus Imports, Hosts, Ansatze, And Residual Relabeling",
    "## 3. Required Certificate Pipeline",
    "## 4. Branch Table",
    "## 5. Claim Certificate Table",
    "## 6. First Exact Missing Proof Object",
    "## 7. Machine-Readable Summary",
    "## 8. Next Meaningful Proof/Computation Step",
]

REQUIRED_PIPELINE = {
    "SourceStressActionCertificate",
    "VariationCertificate",
    "SourceCurrentCertificate",
    "ObserverProjectionCertificate",
    "ConservationCertificate",
    "GRShadowCouplingCertificate",
    "EnergyPositivityCertificate",
    "MatterQFTProvenanceCertificate",
}

REQUIRED_DISTINCTIONS = {
    "derived",
    "imported",
    "hosted",
    "ansatz",
    "residual",
    "control",
}

REQUIRED_BRANCHES = {
    "branch_2a",
    "branch_2b",
    "branch_3",
    "free_beta",
    "background_stueckelberg",
    "finite_control_host_import",
}

REQUIRED_CLAIMS = {
    "STRESS-ENERGY-SHADOW",
    "SOURCE-CURRENT",
    "LAMBDA-DARK-ENERGY-PATCH",
    "MATTER-SHADOW",
    "QFT-STRESS",
}

REQUIRED_FORBIDDEN = {
    "hidden_matter_relabeling",
    "residual_to_T_mu_nu",
    "residual_to_Lambda_eff",
    "bare_Lambda_as_marble",
    "fitted_xi_eff_as_source",
    "target_tuned_dark_energy_fluid",
    "Q_TF_B_named_matter_without_variation",
    "weak_field_compatibility_as_T_mu_nu_derivation",
    "IC4_reconstruction_as_full_branch_certificate",
    "imported_SM_QFT_as_GU_derived",
    "hosted_representation_as_physical_matter",
    "ansatz_fluid_or_scalar_as_derivation",
    "free_beta_nonzero_theta",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing stress-energy certificate: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 7\. Machine-Readable Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable stress-energy JSON block")
    return json.loads(match.group(1))


def claim_map(summary: dict[str, object]) -> dict[str, dict[str, object]]:
    claims = summary.get("claim_certificates", [])
    if not isinstance(claims, list):
        raise AssertionError("claim_certificates must be a list")
    return {str(claim["id"]): claim for claim in claims}


class StressEnergyShadowAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_current_status_is_not_overclaimed_as_derived(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "CERTIFICATE_SPECIFIED_STRESS_ENERGY_SHADOW_NOT_DERIVED",
        )
        self.assertEqual(self.summary["current_status"], "specified_open_not_derived")
        self.assertEqual(self.summary["overclaim_guard"], "do_not_claim_T_mu_nu_derived")
        self.assertIn("T_mu_nu is not yet GU-derived wood", self.text)
        self.assertNotEqual(self.summary["current_status"], "derived")

    def test_tmunu_and_stress_energy_language_is_explicit(self) -> None:
        for needle in [
            "T_mu_nu",
            "stress-energy",
            "T_mu_nu^shadow",
            "observer-facing stress-energy",
            "source-current/stress-energy",
            "Lambda_eff",
            "LambdaDarkEnergyProvenanceCertificate",
        ]:
            self.assertIn(needle, self.text)

    def test_distinctions_cover_derive_select_host_import_ansatz_control(self) -> None:
        distinctions = {row["class"]: row for row in self.summary["distinctions"]}
        self.assertTrue(REQUIRED_DISTINCTIONS.issubset(distinctions))
        for key in REQUIRED_DISTINCTIONS:
            self.assertGreater(len(distinctions[key]["definition"]), 20)

        statuses = set(self.summary["classification_statuses"])
        for status in ["derived", "hosted", "imported", "ansatz", "residual", "control"]:
            self.assertIn(status, statuses)

        for prose in [
            "derived stress-energy",
            "Imported matter",
            "Hosted matter",
            "Ansatz matter",
            "Residual relabeling",
        ]:
            self.assertIn(prose, self.text)

    def test_pipeline_requires_variation_projection_conservation_and_qft_provenance(self) -> None:
        pipeline = {stage["id"]: stage for stage in self.summary["pipeline"]}
        self.assertEqual(set(pipeline), REQUIRED_PIPELINE)

        self.assertIn("full_EL_tuple", pipeline["VariationCertificate"]["requires"])
        self.assertIn("Pi_obs", pipeline["ObserverProjectionCertificate"]["requires"])
        self.assertIn("Lambda_eff_status", pipeline["ObserverProjectionCertificate"]["requires"])
        self.assertIn("nabla_mu_T_mu_nu_zero", pipeline["ConservationCertificate"]["requires"])
        self.assertIn("QFT_state_space", pipeline["MatterQFTProvenanceCertificate"]["requires"])
        self.assertEqual(pipeline["ConservationCertificate"]["status"], "blocked")
        self.assertEqual(pipeline["MatterQFTProvenanceCertificate"]["status"], "blocked")

    def test_hidden_matter_relabeling_is_forbidden(self) -> None:
        shortcuts = set(self.summary["forbidden_shortcuts"])
        self.assertTrue(REQUIRED_FORBIDDEN.issubset(shortcuts))
        for needle in [
            "hidden matter relabeling",
            "Residual relabeling is the hidden-matter failure mode",
            "Anti-smuggling rule",
            "No term may enter derived T_mu_nu^shadow unless",
            "hidden Lambda relabeling",
        ]:
            self.assertIn(needle, self.text)

    def test_branch_table_covers_ig_and_finite_control_cases(self) -> None:
        branches = {branch["key"]: branch for branch in self.summary["branches"]}
        self.assertEqual(set(branches), REQUIRED_BRANCHES)

        self.assertEqual(branches["branch_2a"]["stress_energy_status"], "possible_template_not_derived")
        self.assertEqual(branches["branch_2b"]["source_current"], "theta_corrected_by_multiplier_current")
        self.assertEqual(branches["branch_3"]["source_current"], "theta_eff")
        self.assertEqual(branches["free_beta"]["stress_energy_status"], "fails_nonzero_theta_stress")
        self.assertEqual(branches["finite_control_host_import"]["stress_energy_status"], "hosted_imported_not_derived")

    def test_claim_certificates_have_forbidden_shortcuts_and_rollback(self) -> None:
        claims = claim_map(self.summary)
        self.assertEqual(set(claims), REQUIRED_CLAIMS)

        stress = claims["STRESS-ENERGY-SHADOW"]
        self.assertEqual(stress["status"], "specified_open")
        self.assertEqual(stress["decision"], "not_derived")
        self.assertIn("residual_relabeling", stress["forbidden_shortcuts"])
        self.assertIn("hidden_matter_needed", stress["rollback_conditions"])

        source = claims["SOURCE-CURRENT"]
        self.assertEqual(source["decision"], "bare_theta_not_generally_certified")
        self.assertIn("Branch_3_without_theta_eff", source["rollback_conditions"])

        patch = claims["LAMBDA-DARK-ENERGY-PATCH"]
        self.assertEqual(patch["status"], "open_patch_slot")
        self.assertEqual(patch["decision"], "not_derived")
        self.assertIn("residual_to_Lambda_eff", patch["forbidden_shortcuts"])
        self.assertIn("no_generated_Z_theta_C_Rtheta_xi_eff", patch["rollback_conditions"])

        matter = claims["MATTER-SHADOW"]
        self.assertEqual(matter["status"], "partial_open")
        self.assertIn("A_F_import", matter["forbidden_shortcuts"])

        qft = claims["QFT-STRESS"]
        self.assertEqual(qft["status"], "blocked")
        self.assertIn("no_positive_state_space", qft["rollback_conditions"])

    def test_first_missing_proof_object_prevents_relabeling(self) -> None:
        proof_object = self.summary["first_missing_proof_object"]
        self.assertEqual(proof_object["id"], "NoHiddenMatterStressEnergyShadowTheorem")
        requires = set(proof_object["requires"])
        for required in [
            "branch_fixed_S_GU",
            "term_provenance_ledger",
            "conservation_theorem",
            "positivity_or_QFT_theorem",
            "vacuum_no_hidden_matter_test",
        ]:
            self.assertIn(required, requires)
        prevents = set(proof_object["prevents"])
        for prevented in [
            "hidden_matter_relabeling",
            "import_as_derivation",
            "host_as_selector",
            "ansatz_as_proof",
            "residual_absorption",
        ]:
            self.assertIn(prevented, prevents)

    def test_next_step_is_concrete_and_branch_local(self) -> None:
        self.assertEqual(
            self.summary["next_step"],
            "build_term_provenance_ledger_for_Branch_2A_or_reject_Phi_then_rewrite_to_Branch_3_theta_eff",
        )
        self.assertIn("Attempt a Branch 2A term provenance ledger", self.text)
        self.assertIn("no nonzero imported, ansatz, hosted, or relabeled matter stress", self.text)


def summary() -> dict[str, object]:
    text = read_doc()
    cert = extract_summary(text)
    claims = claim_map(cert)
    return {
        "not_a_proof": True,
        "document": str(DOC.relative_to(REPO_ROOT)),
        "verdict": cert["verdict"],
        "current_status": cert["current_status"],
        "claims": {claim_id: claim["status"] for claim_id, claim in sorted(claims.items())},
        "next_step": cert["next_step"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit the stress-energy shadow certificate.")
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(summary(), indent=2, sort_keys=True))
        return 0

    print("Stress-energy shadow emergence audit: structural certificate only, not a proof.")
    print()
    suite = unittest.defaultTestLoader.loadTestsFromName("__main__.StressEnergyShadowAudit")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
