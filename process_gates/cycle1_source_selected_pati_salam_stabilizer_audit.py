#!/usr/bin/env python3
"""Audit the Cycle 1 source-selected Pati-Salam stabilizer gate.

This is a structural audit, not a mathematical proof. It checks that the gate
keeps the source-selected v_PSB question separate from the conditional
stabilizer/kernel computation, names forbidden target inputs, separates hosted,
selected, and derived statuses, and avoids promoting SM matter, the physical
Higgs, or three generations to derived claims.
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
    / "cycle-gates-and-audits" / "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Source Data And Forbidden Target Inputs",
    "## 3. Candidate `v_PSB` Selection Rule",
    "## 4. Stabilizer/Kernel Theorem Statement",
    "## 5. Higgs/Matter/Generation Implications And Non-Implications",
    "## 6. First Exact Obstruction Or Missing Proof Object",
    "## 7. Constructive Next Computation",
    "## 8. Machine-Readable JSON Summary",
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
    "ordinary_anomaly_free_SM_shadow",
    "target_hypercharge_table",
    "target_Pati_Salam_breaking_vacuum",
    "preselected_SM_subgroup",
    "chosen_SM_kernel",
}

REQUIRED_SELECTION_CHECKS = {
    "NoTargetInput",
    "BranchFixed",
    "ProjectionDefined",
    "Nonzero",
    "RankOneOrbit",
    "Naturality",
    "Replacement",
}

REQUIRED_STATUS_WORDS = {
    "hosted",
    "selected",
    "derived",
    "conditional_derived",
    "open",
    "no_go_target_fed",
}

FORBIDDEN_POSITIVE_CLAIMS = [
    r"\bSM matter is derived\b",
    r"\bfull observer matter is derived\b",
    r"\bphysical Higgs is derived\b",
    r"\bthree generations are derived\b",
    r"\bthree generations have been derived\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing stabilizer gate: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    pattern = r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceSelectedPatiSalamStabilizerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_and_core_decision_are_machine_readable(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "CYCLE1_SOURCE_SELECTED_PATI_SALAM_STABILIZER_GATE",
        )
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_SOURCE_SELECTION_WITH_CONDITIONAL_STABILIZER_KERNEL_THEOREM",
        )
        self.assertEqual(self.summary["verdict_class"], "underdefined")
        self.assertFalse(self.summary["can_define_target_free_v_PSB_now"])
        self.assertTrue(self.summary["can_state_conditional_v_PSB_type"])
        self.assertTrue(self.summary["can_compute_stabilizer_kernel_conditionally"])

    def test_no_overclaim_guards_for_matter_higgs_generations(self) -> None:
        guards = self.summary["overclaim_guards"]
        self.assertFalse(guards["sm_matter_derived"])
        self.assertFalse(guards["physical_higgs_derived"])
        self.assertFalse(guards["three_generations_derived"])
        self.assertFalse(guards["target_fed_v_PSB_allowed"])

        for pattern in FORBIDDEN_POSITIVE_CLAIMS:
            self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE), pattern)

    def test_v_psb_and_stabilizer_kernel_language_are_present(self) -> None:
        for needle in [
            "v_PSB",
            "V_PSB = (10bar,1,3)",
            "Stab_G(v)",
            "stabilizer",
            "kernel",
            "mu_6",
            "SourceCriticalRankOnePSBSelectionCertificate",
        ]:
            self.assertIn(needle, self.text)

        theorem = self.summary["conditional_stabilizer_kernel_theorem"]
        self.assertEqual(theorem["name"], "RankOnePSBStabilizerKernelLemma")
        self.assertEqual(theorem["stabilizer_lie_algebra"], "su3_plus_su2_L_plus_u1")
        self.assertEqual(theorem["kernel_on_W_plus_V_H"], "mu_6")
        self.assertIn("complete_low_observer_shadow", theorem["kernel_promotion_condition"])

    def test_forbidden_target_inputs_are_named(self) -> None:
        forbidden = set(self.summary["forbidden_target_inputs"])
        self.assertTrue(REQUIRED_FORBIDDEN_INPUTS.issubset(forbidden))
        forbidden_section = self.text.split("### Forbidden target inputs", 1)[1]
        forbidden_section = forbidden_section.split("## 3.", 1)[0]
        for item in REQUIRED_FORBIDDEN_INPUTS:
            self.assertIn(item, forbidden_section)

    def test_hosted_selected_derived_statuses_are_separated(self) -> None:
        vocab = set(self.summary["status_vocabulary"])
        self.assertTrue(REQUIRED_STATUS_WORDS.issubset(vocab))

        rows = {row["item"]: row for row in self.summary["status_separation"]}
        self.assertEqual(rows["V_PSB_slot"]["status"], "hosted")
        self.assertEqual(rows["v_PSB_rank_one_tensor"]["status"], "open_not_selected")
        self.assertEqual(rows["stabilizer_lie_algebra"]["status"], "conditional_derived")
        self.assertEqual(rows["higgs"]["status"], "hosted_open")
        self.assertEqual(rows["generation_count"]["status"], "open")

        self.assertIn("source-selected vacuum", rows["V_PSB_slot"]["non_claim"])
        self.assertIn("currently selected object", rows["v_PSB_rank_one_tensor"]["non_claim"])
        self.assertIn("full observer matter derivation", rows["matter_shadow"]["non_claim"])
        self.assertIn("physical Higgs projection", rows["higgs"]["non_claim"])

    def test_selection_rule_requires_source_checks_not_target_payoff(self) -> None:
        rule = self.summary["v_PSB_selection_rule"]
        self.assertEqual(rule["current_status"], "open_not_selected")
        self.assertEqual(
            rule["first_missing_object"],
            "SourceCriticalRankOnePSBSelectionCertificate",
        )
        self.assertEqual(rule["required_output"], "nonzero_decomposable_rank_one_v_PSB")
        self.assertTrue(REQUIRED_SELECTION_CHECKS.issubset(set(rule["required_checks"])))
        self.assertIn("target-fed route is rejected", self.text)

    def test_rollback_conditions_are_machine_readable_and_cover_failure_modes(self) -> None:
        rollbacks = set(self.summary["rollback_conditions"])
        for required in [
            "v_PSB_chosen_because_stabilizer_matches_target",
            "pi_PSB_undefined_or_hand_projected",
            "source_projection_zero",
            "source_projection_generic_or_higher_rank",
            "kernel_named_before_action_computation",
            "complete_low_shadow_changes_kernel",
            "physical_Higgs_or_EWSB_inserted_phenomenologically",
            "generation_count_uses_n_equals_3_or_target_index",
            "A_F_G_SM_Z_6_K_SM_consumed_upstream",
        ]:
            self.assertIn(required, rollbacks)

    def test_next_computation_is_constructive_and_exact(self) -> None:
        self.assertEqual(
            self.summary["first_exact_obstruction"],
            "SourceCriticalRankOnePSBSelectionCertificate",
        )
        self.assertEqual(
            self.summary["constructive_next_computation"],
            "RankOnePSBStabilizerKernelLedger_then_pi_PSB_source_selection_search",
        )
        self.assertIn("RankOnePSBStabilizerKernelLedger", self.text)
        self.assertIn("Find or refute pi_PSB(source critical data)", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
