#!/usr/bin/env python3
"""Regression checks for the source-Noether/tau carrier attempt.

Run: python tests/test_source_noether_tau_carrier.py
"""

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.source_noether_tau_carrier import (  # noqa: E402
    SourceNoetherTauVerdict,
    run_source_noether_tau_carrier,
)


class SourceNoetherTauCarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_source_noether_tau_carrier()

    def test_tau_schur_solve_derives_the_projected_map(self):
        self.assertEqual(
            self.report.verdict,
            SourceNoetherTauVerdict.TAU_SCHUR_PROJECTOR_ONLY_DERIVATIVE_TAU_BLOCKED,
        )
        self.assertTrue(self.report.finite_fiber_tau_derives_projection)
        self.assertLess(self.report.right_inverse_residual, 1.0e-8)
        self.assertLess(self.report.kkt_stationarity_residual, 1.0e-8)
        self.assertLess(self.report.tau_noether_residual, 1.0e-8)
        self.assertLess(self.report.projector_identity_residual, 1.0e-8)
        self.assertLess(self.report.correction_normal_residual, 1.0e-8)

    def test_tau_solve_is_not_an_independent_source_carrier(self):
        self.assertFalse(self.report.source_derived_independent_tau)
        self.assertTrue(self.report.noether_leaves_tangent_freedom)
        self.assertLess(self.report.tangent_perturbation_noether_residual, 1.0e-8)
        self.assertGreater(self.report.tangent_perturbation_difference_norm, 1.0)
        self.assertEqual(self.report.free_tangent_column_dim, 1664)
        self.assertEqual(self.report.free_tangent_matrix_dim, 1664 * 128)
        self.assertEqual(self.report.next_progress_point, "DERIVATIVE-TAU-HOMOMORPHISM")

    def test_rank_data_preserves_the_a_door_and_null_tau_caveat(self):
        self.assertEqual(self.report.raw_noether_rank, 128)
        self.assertEqual(self.report.tau_multiplier_rank, 128)
        self.assertEqual(self.report.corrected_gauge_rank, 128)
        self.assertEqual(self.report.null_raw_noether_rank, 64)
        self.assertEqual(self.report.null_tau_multiplier_rank, 64)
        self.assertEqual(self.report.null_corrected_gauge_rank, 128)

    def test_anchor_numbers_are_unchanged(self):
        self.assertLess(abs(self.report.bare_commutator_norm - 58.7215), 1.0e-4)
        self.assertLess(abs(self.report.c2_norm - 155.3625), 1.0e-4)


if __name__ == "__main__":
    unittest.main()
