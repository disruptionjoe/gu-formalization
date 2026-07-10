#!/usr/bin/env python3
"""Regression checks for the anchor-scale A-door fork.

Run: python tests/test_anchor_scale_a_door.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib.anchor_scale_a_door import ADoorVerdict, run_anchor_scale_a_door  # noqa: E402
from lib.loss_channels import EXPECTED_BARE_COMMUTATOR, EXPECTED_C2  # noqa: E402


class AnchorScaleADoorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_anchor_scale_a_door()
        cls.metrics = cls.report.metrics

    def test_full_scale_representation_anchors_are_preserved(self):
        self.assertEqual(self.report.verdict, ADoorVerdict.PARTIAL_PASS_BV_TAU_BLOCKED)
        self.assertAlmostEqual(self.metrics["bare_commutator"], EXPECTED_BARE_COMMUTATOR, places=2)
        self.assertAlmostEqual(self.metrics["C2"], EXPECTED_C2, places=2)
        self.assertTrue(self.metrics["anchor_ok"])
        self.assertEqual(self.metrics["gamma_rank"], 128)
        self.assertEqual(self.metrics["ker_gamma_dim"], 1664)

    def test_non_null_component_scalar_spinor_shifts_are_not_ker_gamma_tangent(self):
        self.assertTrue(self.metrics["non_null_components_not_tangent"])
        self.assertTrue(self.metrics["non_null_components_have_normal_part"])
        self.assertTrue(self.metrics["non_null_components_have_kernel_part"])
        self.assertEqual(set(self.metrics["basis_trace_ranks"].values()), {128})
        self.assertEqual(set(self.metrics["basis_q_ranks"].values()), {128})
        self.assertEqual(set(self.metrics["basis_kernel_projection_ranks"].values()), {128})

    def test_quaternionic_and_krein_anchor_compatibility(self):
        self.assertTrue(self.metrics["h_linear_component_shifts"])
        self.assertTrue(self.metrics["h_linear_gamma_traces"])
        self.assertLess(self.metrics["max_component_h_defect"], 1e-7)
        self.assertLess(self.metrics["max_trace_h_defect"], 1e-7)
        self.assertEqual(self.metrics["spinor_krein_signature"], (64, 64, 0))
        self.assertTrue(self.metrics["component_krein_compatible"])
        self.assertLess(self.metrics["beta_pseudo_antihermitian_residual"], 1e-7)

    def test_null_direction_records_the_derivative_tau_caveat(self):
        self.assertEqual(self.metrics["null_trace_rank"], 64)
        self.assertEqual(self.metrics["null_kernel_dim"], 64)
        self.assertAlmostEqual(self.metrics["null_square_norm"], 0.0, places=7)
        self.assertTrue(self.metrics["null_direction_has_tangent_spinors"])
        self.assertIn("BV/Koszul-Tate closure", self.report.next_action)
        self.assertIn("null-direction tau caveat", self.report.next_action)


if __name__ == "__main__":
    unittest.main()
