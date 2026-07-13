#!/usr/bin/env python3
"""Regression checks for the global-boundary tau-data probe.

Run: python tests/test_global_boundary_condition_tau_data.py
"""

from pathlib import Path
import sys
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.global_boundary_condition_tau_data import (  # noqa: E402
    GlobalBoundaryTauVerdict,
    run_global_boundary_tau_data,
)


class GlobalBoundaryTauDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_global_boundary_tau_data()

    def test_available_boundary_data_does_not_force_a_wall(self):
        self.assertEqual(
            self.report.verdict,
            GlobalBoundaryTauVerdict.EXTERNALLY_KEYED_WALL_SELECTION_BLOCKED,
        )
        self.assertEqual(self.report.admissible_wall_count, 9)
        self.assertFalse(self.report.boundary_current_declared_by_source_action)
        self.assertFalse(self.report.source_forced_unique_selector)
        self.assertTrue(self.report.selection_still_needs_source_current_data)
        self.assertEqual(self.report.next_progress_point, "SOURCE-CURRENT-DERIVATIVE-DATA")

    def test_local_scalar_summaries_are_rule_choice_dependent(self):
        choices = self.report.local_criterion_choices
        self.assertEqual(len(choices), 5)
        selected_components = {choice.selected_component for choice in choices}
        self.assertGreaterEqual(len(selected_components), 3)
        self.assertTrue(self.report.local_scalar_rules_pick_multiple_components)
        self.assertIn(0, selected_components)
        self.assertIn(3, selected_components)
        self.assertIn(4, selected_components)

    def test_external_current_can_select_but_only_as_external_key(self):
        current = np.zeros(9)
        current[2] = 7.0
        report = run_global_boundary_tau_data(boundary_current=current)

        self.assertEqual(
            report.verdict,
            GlobalBoundaryTauVerdict.EXTERNALLY_KEYED_WALL_SELECTION_BLOCKED,
        )
        self.assertTrue(report.externally_supplied_current_can_pick_a_wall)
        self.assertIsNotNone(report.external_current_choice)
        self.assertEqual(report.external_current_choice.selected_component, 2)
        self.assertTrue(report.external_current_choice.externally_keyed)
        self.assertFalse(report.source_forced_unique_selector)

    def test_prior_anchor_numbers_remain_unchanged(self):
        self.assertLess(abs(self.report.wall_report.bare_commutator_norm - 58.7215), 1.0e-4)
        self.assertLess(abs(self.report.wall_report.c2_norm - 155.3625), 1.0e-4)


if __name__ == "__main__":
    unittest.main()
