#!/usr/bin/env python3
"""Executable checks for GU-native loss channels.

Run: python tests/test_loss_channels.py
"""

import math
import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402


class BoundaryLossChannelTests(unittest.TestCase):
    def test_boundary_symbol_channel_computes_existing_carrier(self):
        report = lc.l_boundary_symbol()
        self.assertEqual(report.status, "computed")
        self.assertEqual(report.value, 0.0)
        self.assertTrue(report.details["map_built"])
        self.assertTrue(report.details["C2_is_HS_symbol_norm"])
        self.assertAlmostEqual(report.details["C2"], lc.EXPECTED_C2, places=2)

    def test_boundary_index_channel_records_eta_wall(self):
        report = lc.l_boundary_index()
        self.assertEqual(report.status, "computed")
        self.assertEqual(report.value, 1.0)
        self.assertEqual(report.details["eta_D_sigma"], 0)
        self.assertTrue(report.details["eta_forced_zero"])
        self.assertFalse(report.details["section_connects"])
        self.assertEqual(report.details["verdict"], "BV_BOUNDARY_MAP_EXISTS_BUT_APS_INDEX_ROUTE_FAILS")


class GuardLossChannelTests(unittest.TestCase):
    def test_target_import_patterns_are_fatal(self):
        candidate = lc.SourceCandidate(
            name="bad-normalization",
            description="selects the answer by 24 / 8 after assuming K3",
        )
        report = lc.l_target_import(candidate)
        self.assertTrue(math.isinf(report.value))
        self.assertGreaterEqual(len(report.details["matches"]), 2)

    def test_acausal_bare_commutator_motion_is_fatal(self):
        candidate = lc.SourceCandidate(
            name="clean-decoupler",
            description="clean decoupling by trivial block-subtraction",
            metrics={"bare_commutator": 0.0},
        )
        report = lc.l_acausal_trap(candidate)
        self.assertTrue(math.isinf(report.value))
        self.assertGreaterEqual(len(report.details["matches"]), 2)

    def test_candidate_score_uses_only_computable_channels(self):
        candidate = lc.SourceCandidate(name="honest-boundary-candidate")
        score = lc.candidate_score_from_available_losses(candidate, growth_value=4.0)
        self.assertIn("L_boundary_index", score.adversarial_losses)
        self.assertIn("L_target_import", score.adversarial_losses)
        self.assertTrue(score.passes_hard_guards())
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)


class MissingCarrierChannelTests(unittest.TestCase):
    def test_missing_carrier_channels_fail_loudly(self):
        for channel in (
            lc.l_anomaly,
            lc.l_rs_brst,
            lc.l_theta_source,
            lc.l_weak_field,
            lc.l_families_pushforward,
        ):
            with self.subTest(channel=channel.__name__):
                with self.assertRaises(lc.MissingCarrierError) as raised:
                    channel()
                self.assertIn("no computable GU-native carrier", str(raised.exception))
                self.assertTrue(raised.exception.required_carrier)
                self.assertTrue(raised.exception.parent_object)


if __name__ == "__main__":
    unittest.main()
