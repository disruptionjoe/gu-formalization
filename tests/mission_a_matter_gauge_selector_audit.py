#!/usr/bin/env python3
"""Audit the Mission A matter/gauge selector construction attempt.

This is a structural audit, not a mathematical proof. It checks that the
artifact builds an explicit Phi_SG_MG-style selector candidate, declares legal
source data, forbids target inputs, includes replacement tests, and does not
claim that SM matter is derived.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "mission-a-matter-gauge-selector-construction-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. If GU Is Correct, What Matter/Gauge Selector Object Must Exist",
    "## 3. Candidate Selector Domain/Codomain/Functor And Legal Source Data",
    "## 4. Anti-Smuggling Replacement Tests, Including n != 3 And Alternate Finite Controls",
    "## 5. What Current Pati-Salam/Higgs/Type-II1 Evidence Supplies And What It Does Not",
    "## 6. First Exact Obstruction Or Missing Proof Object",
    "## 7. Constructive Next Computation",
    "## 8. Claim Certificate Table And Machine-Readable Summary",
    "## Machine-Readable Summary",
]

REQUIRED_LEGAL_SOURCE_DATA = {
    "I_GU_branch",
    "source_critical_configuration",
    "observer_section",
    "D_GU",
    "S_GU",
    "variation_space",
    "source_law",
    "boundary_domain_data",
    "source_gauge_action",
}

REQUIRED_FORBIDDEN_INPUTS = {
    "A_F",
    "G_SM",
    "Z_6",
    "K_SM",
    "physical_Higgs",
    "nonzero_Higgs_projection",
    "negative_Higgs_mass_squared",
    "n_equals_3",
    "ind_H_D_RS_equals_8",
    "ind_H_D_GU_equals_24",
    "ordinary_anomaly_free_SM_shadow",
}

REQUIRED_TESTS = {
    "NoTargetInput",
    "LabelErasure",
    "BranchCommitment",
    "StabilizerComputation",
    "GlobalKernel",
    "LowModeGap",
    "CompleteShadow",
    "AnomalyNonSelector",
    "HiggsNullTest",
    "PotentialTest",
    "GenerationReplacement",
    "AlternateFiniteControls",
    "K3Bridge",
}

REQUIRED_CLAIMS = {
    "PHI_SG_MG",
    "SM_GAUGE",
    "MATTER_SHADOW",
    "HIGGS",
    "GEN_COUNT",
    "A_F_OR_BYPASS",
}

NON_DERIVED_CLAIMS = {
    "SM_GAUGE",
    "MATTER_SHADOW",
    "HIGGS",
    "GEN_COUNT",
    "A_F_OR_BYPASS",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Mission A selector artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## Machine-Readable Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing Machine-Readable Summary JSON block")
    return json.loads(match.group(1))


class MissionAMatterGaugeSelectorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_selector_identity_and_posture_are_explicit(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "SOURCE_GEOMETRY_MATTER_GAUGE_SELECTOR_CONSTRUCTION_ATTEMPT",
        )
        self.assertEqual(
            self.summary["verdict"],
            "CANDIDATE_SELECTOR_SCHEMA_SPECIFIED_NOT_INSTANTIATED",
        )
        self.assertEqual(
            self.summary["overclaim_guard"],
            "do_not_claim_SM_matter_is_derived",
        )
        self.assertIn("Phi_SG_MG", self.text)
        self.assertIn("selector", self.text.lower())

    def test_domain_source_data_and_forbidden_inputs_are_declared(self) -> None:
        selector = self.summary["selector"]
        self.assertEqual(selector["name"], "Phi_SG_MG")
        self.assertTrue(REQUIRED_LEGAL_SOURCE_DATA.issubset(set(selector["domain"])))

        forbidden = set(selector["forbidden_target_inputs"])
        self.assertTrue(REQUIRED_FORBIDDEN_INPUTS.issubset(forbidden))
        self.assertIn("target_hypercharge_table", forbidden)
        self.assertIn("target_Pati_Salam_breaking_vacuum", forbidden)

    def test_rank_one_candidate_and_stabilizer_language_are_present(self) -> None:
        routes = {route["id"]: route for route in self.summary["candidate_routes"]}
        self.assertIn("critical_stabilizer_shadow", routes)
        self.assertIn("rank_one_psb_stabilizer", routes)
        self.assertIn("finite_algebra_shadow", routes)

        rank_one = routes["rank_one_psb_stabilizer"]
        self.assertEqual(rank_one["source_slot"], "V_PSB=(10bar,1,3)")
        self.assertEqual(rank_one["source_selection_status"], "missing")
        self.assertIn("source_selected_nonzero_decomposable_rank_one_v_PSB", rank_one["requires"])

        for needle in [
            "Stab_{SU(4) x SU(2)_L x SU(2)_R}(v_PSB)",
            "compute the stabilizer and kernel",
            "not by choice",
        ]:
            self.assertIn(needle, self.text)

    def test_replacement_tests_cover_n_not_three_and_finite_controls(self) -> None:
        self.assertEqual(set(self.summary["anti_smuggling_tests"]), REQUIRED_TESTS)

        replacement = self.summary["replacement_tests"]
        generation = set(replacement["generation"])
        for required in ["n_equals_2", "n_equals_4", "n_arbitrary", "C_n_replacement"]:
            self.assertIn(required, generation)

        finite_controls = set(replacement["finite_controls"])
        for required in [
            "C_plus_H_plus_M_k_for_k_not_3",
            "H_L_plus_H_R_plus_M_4_C",
            "alternate_global_center_quotients",
            "extra_vectorlike_modes",
        ]:
            self.assertIn(required, finite_controls)

        self.assertIn("n = 2", self.text)
        self.assertIn("n = 4", self.text)
        self.assertIn("C + H + M_k(C), k != 3", self.text)

    def test_claim_certificates_do_not_overclaim_sm_matter_as_derived(self) -> None:
        claims = {claim["claim"]: claim for claim in self.summary["claim_certificates"]}
        self.assertEqual(set(claims), REQUIRED_CLAIMS)

        for claim_name in NON_DERIVED_CLAIMS:
            self.assertNotEqual(claims[claim_name]["status"], "derived", claim_name)

        self.assertEqual(claims["SM_GAUGE"]["status"], "conditional_candidate")
        self.assertEqual(claims["MATTER_SHADOW"]["status"], "partial_open")
        self.assertEqual(claims["HIGGS"]["status"], "hosted_open")
        self.assertEqual(claims["GEN_COUNT"]["status"], "open")
        self.assertEqual(claims["A_F_OR_BYPASS"]["status"], "bypass_open")

        for forbidden_phrase in [
            "SM matter is derived",
            "full SM matter is derived",
            "physical Higgs is derived",
            "three generations are derived",
        ]:
            self.assertNotIn(forbidden_phrase, self.text)

    def test_current_evidence_keeps_pati_salam_higgs_typeii1_limited(self) -> None:
        evidence = self.summary["current_evidence"]
        self.assertEqual(
            evidence["pati_salam_branch"]["status"],
            "derived_branch_representation",
        )
        self.assertEqual(evidence["higgs_slots"]["status"], "hosted_open")
        self.assertEqual(evidence["type_ii1"]["status"], "negative_filter_open_empty")

        self.assertIn("does_not_supply", evidence["pati_salam_branch"])
        self.assertIn("does_not_supply", evidence["higgs_slots"])
        self.assertIn("does_not_supply", evidence["type_ii1"])

    def test_missing_proof_object_next_computation_and_rollback_are_concrete(self) -> None:
        self.assertEqual(
            self.summary["first_missing_proof_object"],
            "CriticalRankOnePSBSelectionAndStabilizerTheorem",
        )
        self.assertEqual(
            self.summary["constructive_next_computation"],
            "compute_stabilizer_kernel_and_branching_for_rank_one_V_PSB_without_SM_labels",
        )
        self.assertIn("rollback", self.summary["selector"]["codomain"])

        claims = self.summary["claim_certificates"]
        for claim in claims:
            self.assertTrue(claim["missing_proof_object"])
            self.assertTrue(claim["rollback"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
