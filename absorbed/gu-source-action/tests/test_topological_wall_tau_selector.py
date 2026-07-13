#!/usr/bin/env python3
"""Regression checks for the topological-wall tau selector probe.

Run: python tests/test_topological_wall_tau_selector.py
"""

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.topological_wall_tau_selector import (  # noqa: E402
    TopologicalWallTauVerdict,
    run_topological_wall_tau_selector,
)


class TopologicalWallTauSelectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_topological_wall_tau_selector()

    def test_wall_lens_produces_nonzero_tangent_selectors(self):
        self.assertEqual(
            self.report.verdict,
            TopologicalWallTauVerdict.NONZERO_WALL_SELECTORS_UNDERDETERMINED,
        )
        self.assertTrue(self.report.nonzero_wall_selectors_exist)
        self.assertEqual(self.report.admissible_count, 9)
        self.assertEqual(self.report.distinct_selector_count, 9)
        self.assertLess(self.report.max_noether_residual, 1.0e-8)
        self.assertLess(self.report.max_h_linear_defect, 1.0e-7)
        self.assertLess(self.report.max_krein_wall_residual, 1.0e-8)

    def test_wall_family_is_not_a_forced_unique_source_selector(self):
        self.assertTrue(self.report.wall_family_is_underdetermined)
        self.assertTrue(self.report.wall_lens_still_needs_boundary_data)
        self.assertFalse(self.report.source_forced_unique_selector)
        self.assertGreater(self.report.min_pairwise_selector_distance, 1.0)
        self.assertGreater(self.report.max_pairwise_selector_distance, 1.0)
        self.assertEqual(self.report.next_progress_point, "GLOBAL-BOUNDARY-CONDITION-TAU-DATA")

    def test_each_candidate_still_needs_projection_repair(self):
        self.assertGreater(self.report.min_projection_dependency_norm, 1.0)
        for candidate in self.report.candidates:
            with self.subTest(candidate=candidate.name):
                self.assertTrue(candidate.admissible_finite_fiber_wall)
                self.assertTrue(candidate.still_uses_projection_repair)
                self.assertEqual(candidate.selector_rank, 128)
                self.assertGreater(candidate.selector_norm, 1.0)
                self.assertGreater(candidate.raw_wall_noether_residual, 1.0)
                self.assertGreater(candidate.projection_dependency_norm, 1.0)

    def test_anchor_numbers_are_unchanged(self):
        self.assertLess(abs(self.report.bare_commutator_norm - 58.7215), 1.0e-4)
        self.assertLess(abs(self.report.c2_norm - 155.3625), 1.0e-4)


if __name__ == "__main__":
    unittest.main()
