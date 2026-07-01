#!/usr/bin/env python3
"""Executable sanity checks for the cryptoeconomic security-budget source-action lens.

Run: python tests/test_security_budget.py
"""

import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib.security_budget import CandidateScore, select_security_budget_winner  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "CRYPTOECONOMIC-SOURCE-ACTION.md"
README = ROOT / "README.md"
SPEC = ROOT / "SPEC.md"
AGENTS = ROOT / "Agents Start Here.md"


def guarded_candidate(name: str, losses: dict[str, float], growth: float = 10.0) -> CandidateScore:
    return CandidateScore(
        name=name,
        growth_value=growth,
        validation_cost=1.0,
        finalization_cost=1.0,
        adversarial_losses=losses,
        hard_guards={
            "master_equation_ok": True,
            "noether_forces_constraint": True,
            "anti_trap_bare_commutator_preserved": True,
            "anti_import": True,
        },
    )


class SecurityBudgetSelectorTests(unittest.TestCase):
    def test_minimax_selector_prefers_lowest_worst_case_loss(self):
        candidates = [
            guarded_candidate("high-growth-fragile", {"anomaly": 0.5, "brst": 7.0}, growth=11.0),
            guarded_candidate("lower-growth-secure", {"anomaly": 1.0, "brst": 1.5}, growth=10.0),
        ]
        winner = select_security_budget_winner(candidates)
        self.assertEqual(winner.name, "lower-growth-secure")
        self.assertEqual(winner.worst_case_adversarial_loss(), 1.5)

    def test_failed_guard_is_disqualifying_even_with_good_score(self):
        bad = CandidateScore(
            name="target-imported",
            growth_value=100.0,
            validation_cost=0.0,
            finalization_cost=0.0,
            adversarial_losses={"target_import": 0.0},
            hard_guards={"anti_import": False},
        )
        good = guarded_candidate("honest-survivor", {"anomaly": 2.0, "brst": 2.0})
        self.assertEqual(select_security_budget_winner([bad, good]).name, "honest-survivor")

    def test_ties_do_not_select(self):
        a = guarded_candidate("a", {"loss": 2.0})
        b = guarded_candidate("b", {"loss": 2.0})
        with self.assertRaisesRegex(ValueError, "tied"):
            select_security_budget_winner([a, b])


class SecurityBudgetDocumentTests(unittest.TestCase):
    def test_note_is_prominent_and_actionable(self):
        for path in (NOTE, README, SPEC, AGENTS):
            with self.subTest(path=path.name):
                self.assertTrue(path.exists())
                text = path.read_text(encoding="utf-8")
                self.assertIn("security-budget", text.lower())

    def test_note_contains_kill_criteria_and_workflow(self):
        text = NOTE.read_text(encoding="utf-8")
        for phrase in [
            "First Actionable Workflow",
            "L_anomaly",
            "L_RS_BRST",
            "L_boundary_index",
            "L_target_import",
            "anti-trap guard",
            "GU-native carrier",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()

