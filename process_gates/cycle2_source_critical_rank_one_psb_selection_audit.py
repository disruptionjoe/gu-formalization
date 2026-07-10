#!/usr/bin/env python3
"""Audit the Cycle 2 source-critical rank-one PSB selection certificate.

This is a structural audit, not a mathematical proof. It checks that the
certificate names SourceCriticalRankOnePSBSelectionCertificate, keeps current
v_PSB selection blocked, makes forbidden target inputs and anti-smuggling tests
explicit, separates hosted/selected/derived statuses, and emits machine-readable
verdict and rollback conditions.
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
    / "cycle-gates-and-audits" / "cycle2-source-critical-rank-one-psb-selection-certificate-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Candidate Source-Critical Selection Criterion",
    "## 3. Allowed Source Inputs And Forbidden Target Inputs",
    "## 4. Anti-Smuggling Tests",
    "## 5. Stabilizer/Kernel Consequence If The Certificate Closes",
    "## 6. First Exact Obstruction",
    "## 7. Impact For SM Gauge/Higgs/Matter Claims",
    "## 8. Next Meaningful Computation",
    "## 9. Machine-Readable JSON Summary",
]

REQUIRED_FORBIDDEN_INPUTS = {
    "A_F",
    "G_SM",
    "Z_6",
    "K_SM",
    "physical_Higgs",
    "nonzero_Higgs_projection",
    "negative_Higgs_mass_squared",
    "n_equals_3",
    "three_generations",
    "ind_H_D_RS_equals_8",
    "ind_H_D_GU_equals_24",
    "ordinary_anomaly_free_SM_shadow",
    "target_hypercharge_table",
    "target_Pati_Salam_breaking_vacuum",
    "preselected_SM_subgroup",
    "chosen_SM_kernel",
    "ordinary_SM_matter_packet",
    "desired_stabilizer_su3_su2_u1",
    "mu_6_kernel_as_input",
}

REQUIRED_ANTI_SMUGGLING_TESTS = {
    "NoTargetInput",
    "BranchCommitment",
    "ProjectionProvenance",
    "LabelErasure",
    "PayoffBlindness",
    "RankConditionNotSelector",
    "NonzeroFromSource",
    "ExactVectorNotLine",
    "OrbitReplacement",
    "AlternateSlotReplacement",
    "KernelAfterAction",
    "CompleteShadowQuarantine",
    "HiggsGenerationQuarantine",
    "Naturality",
    "RollbackActive",
}

REQUIRED_PASS_CONDITIONS = {
    "BranchFixed",
    "ProjectionDefined",
    "SourceFunctionalDefined",
    "CriticalSelection",
    "Nonzero",
    "ExactVectorNotLine",
    "RankOneOrbit",
    "OrbitRigidity",
    "Naturality",
    "ReplacementObstruction",
}

REQUIRED_STATUS_WORDS = {
    "hosted",
    "selected",
    "derived",
    "conditional_derived",
    "specified_not_instantiated",
    "open",
    "blocked",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bSM matter is derived\b",
    r"\bfull observer matter is derived\b",
    r"\bphysical Higgs is derived\b",
    r"\bthree generations are derived\b",
    r"\bthree generations have been derived\b",
    r"\bSM gauge quotient is derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Cycle 2 PSB selection certificate: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    pattern = r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceCriticalRankOnePSBSelectionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_named_certificate_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "CYCLE2_SOURCE_CRITICAL_RANK_ONE_PSB_SELECTION_CERTIFICATE",
        )
        self.assertEqual(
            self.summary["verdict"],
            "SELECTION_PROBLEM_SPECIFIED_SOURCE_SELECTION_NOT_CLOSED",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        self.assertFalse(self.summary["source_selection_possible_from_current_sources"])
        self.assertTrue(self.summary["selection_problem_specified"])
        self.assertTrue(self.summary["can_compute_stabilizer_if_certificate_closes"])
        self.assertEqual(
            self.summary["named_certificate"],
            "SourceCriticalRankOnePSBSelectionCertificate",
        )
        self.assertIn("SourceCriticalRankOnePSBSelectionCertificate", self.text)

    def test_missing_source_functional_or_invariant_is_exact(self) -> None:
        obstruction = self.summary["missing_source_functional_or_invariant"]
        self.assertEqual(obstruction["name"], "kappa_R1_PSB")
        self.assertEqual(obstruction["current_status"], "missing")
        self.assertIn("select_nonzero_exact_rank_one_v_PSB", obstruction["required_effect"])
        self.assertIn("F_R1_PSB_src", self.text)
        self.assertIn("kappa_R1_PSB", self.text)
        self.assertIn("pi_PSB", self.summary["first_exact_obstruction"])

    def test_candidate_criterion_requires_source_selection_not_rank_wishlist(self) -> None:
        criterion = self.summary["candidate_criterion"]
        self.assertEqual(criterion["current_status"], "specified_not_instantiated")
        self.assertEqual(
            criterion["source_slot"],
            "V_PSB=(10bar,1,3)=Sym^2(A^*)_tensor_Sym^2(R)",
        )
        self.assertTrue(
            REQUIRED_PASS_CONDITIONS.issubset(set(criterion["required_pass_conditions"]))
        )
        for required in [
            "tensor_flattening_rank_one",
            "A_symmetric_factor_rank_one",
            "R_symmetric_factor_rank_one",
            "nonzero_vector",
        ]:
            self.assertIn(required, criterion["rank_one_algebraic_tests"])
        self.assertIn("only a certificate audit", self.text)

    def test_forbidden_target_inputs_are_explicit_in_json_and_section(self) -> None:
        forbidden = set(self.summary["forbidden_target_inputs"])
        self.assertTrue(REQUIRED_FORBIDDEN_INPUTS.issubset(forbidden))

        forbidden_section = self.text.split("### Forbidden target inputs", 1)[1]
        forbidden_section = forbidden_section.split("## 4.", 1)[0]
        for item in REQUIRED_FORBIDDEN_INPUTS:
            self.assertIn(item, forbidden_section)

    def test_anti_smuggling_tests_are_explicit(self) -> None:
        tests = set(self.summary["anti_smuggling_tests"])
        self.assertTrue(REQUIRED_ANTI_SMUGGLING_TESTS.issubset(tests))

        anti_section = self.text.split("## 4. Anti-Smuggling Tests", 1)[1]
        anti_section = anti_section.split("## 5.", 1)[0]
        for item in REQUIRED_ANTI_SMUGGLING_TESTS:
            self.assertIn(item, anti_section)
        self.assertIn("projective-line failure", anti_section)

    def test_hosted_selected_derived_statuses_remain_separated(self) -> None:
        vocab = set(self.summary["status_vocabulary"])
        self.assertTrue(REQUIRED_STATUS_WORDS.issubset(vocab))

        rows = {row["item"]: row for row in self.summary["status_separation"]}
        self.assertEqual(rows["V_PSB_slot"]["status"], "hosted")
        self.assertEqual(rows["rank_one_algebraic_orbit"]["status"], "specified_not_instantiated")
        self.assertEqual(rows["v_PSB_rank_one_tensor"]["status"], "open_not_selected")
        self.assertEqual(rows["source_functional_or_invariant"]["status"], "missing")
        self.assertEqual(rows["stabilizer_lie_algebra"]["status"], "conditional_derived")
        self.assertEqual(rows["kernel_on_W_plus_V_H"]["status"], "conditional_derived_packet_kernel")
        self.assertEqual(rows["higgs"]["status"], "hosted_open")
        self.assertEqual(rows["generation_count"]["status"], "open")

        self.assertIn("source-selected vacuum", rows["V_PSB_slot"]["non_claim"])
        self.assertIn("currently selected object", rows["v_PSB_rank_one_tensor"]["non_claim"])
        self.assertIn("source choice of v_PSB", rows["stabilizer_lie_algebra"]["non_claim"])
        self.assertIn("full observer matter derivation", rows["matter_shadow"]["non_claim"])
        self.assertIn("physical Higgs projection", rows["higgs"]["non_claim"])
        self.assertIn("three-generation derivation", rows["generation_count"]["non_claim"])

    def test_no_sm_matter_higgs_or_generation_derivation_claim(self) -> None:
        guards = self.summary["overclaim_guards"]
        self.assertFalse(guards["sm_matter_derived"])
        self.assertFalse(guards["physical_higgs_derived"])
        self.assertFalse(guards["three_generations_derived"])
        self.assertFalse(guards["sm_gauge_quotient_derived_now"])
        self.assertFalse(guards["target_fed_v_PSB_allowed"])

        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE), pattern)

    def test_conditional_stabilizer_consequences_are_limited(self) -> None:
        consequences = self.summary["consequences_if_certificate_closes"]
        self.assertEqual(consequences["v_PSB"], "selected")
        self.assertIn("su3_plus_su2_L_plus_u1", consequences["stabilizer_lie_algebra"])
        self.assertEqual(consequences["packet_kernel"], "mu_6_on_W_plus_V_H")
        self.assertEqual(consequences["global_kernel"], "pending_complete_low_observer_shadow")
        self.assertIn("remain_open_or_hosted", consequences["matter_higgs_generation_claims"])

        consequence_section = self.text.split(
            "## 5. Stabilizer/Kernel Consequence If The Certificate Closes", 1
        )[1]
        consequence_section = consequence_section.split("## 6.", 1)[0]
        self.assertIn("What this would not promote", consequence_section)
        self.assertIn("exact three-generation count", consequence_section)

    def test_rollback_conditions_are_machine_readable_and_cover_failure_modes(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        for required in [
            "forbidden_target_input_appears_upstream",
            "pi_PSB_undefined_or_multiplicity_hand_chosen",
            "source_functional_or_invariant_missing",
            "selected_output_zero",
            "selected_output_generic_or_higher_rank",
            "selected_output_projective_line_only",
            "rank_one_justified_by_SM_like_stabilizer_payoff",
            "kernel_named_before_action_computation",
            "complete_low_shadow_changes_kernel",
            "SM_matter_Higgs_or_three_generation_claim_promoted_without_downstream_certificates",
        ]:
            self.assertIn(required, rollbacks)

        self.assertIn(
            "define_E_src_and_pi_PSB_for_one_branch",
            self.summary["next_meaningful_computation"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
