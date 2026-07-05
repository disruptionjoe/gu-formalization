#!/usr/bin/env python3
"""Regression checks for the anomaly/Green-Schwarz carrier packet.

Run: python tests/test_anomaly_green_schwarz_packet.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402


def anomaly_green_schwarz_candidate() -> lc.SourceCandidate:
    return lc.SourceCandidate(
        name="anomaly-green-schwarz-security-budget",
        description=(
            "Attempts to use a GU-internal anomaly polynomial or Green-Schwarz "
            "factorization as the candidate-specific security-budget carrier."
        ),
        assumptions=(
            "No target normalization is used.",
            "The bare commutator anchor is preserved.",
            "Anomaly-cancellation vocabulary is not treated as a source action by itself.",
            "A Green-Schwarz factorization must be computed from a candidate S_IG before selection.",
        ),
    )


class AnomalyGreenSchwarzPacketTests(unittest.TestCase):
    def test_computable_guards_remain_clean(self):
        candidate = anomaly_green_schwarz_candidate()

        target_import = lc.l_target_import(candidate)
        acausal_trap = lc.l_acausal_trap(candidate)
        boundary_symbol = lc.l_boundary_symbol(candidate)
        boundary_index = lc.l_boundary_index(candidate)

        self.assertEqual(target_import.value, 0.0)
        self.assertEqual(target_import.details["matches"], [])
        self.assertEqual(acausal_trap.value, 0.0)
        self.assertEqual(acausal_trap.details["matches"], [])
        self.assertEqual(boundary_symbol.value, 0.0)
        self.assertTrue(boundary_symbol.details["map_built"])
        self.assertEqual(boundary_index.value, 1.0)
        self.assertTrue(boundary_index.details["eta_forced_zero"])

    def test_anomaly_channel_is_the_named_blocker(self):
        candidate = anomaly_green_schwarz_candidate()

        with self.assertRaises(lc.MissingCarrierError) as raised:
            lc.l_anomaly(candidate)

        self.assertEqual(raised.exception.channel, "L_anomaly")
        self.assertIn("anomaly polynomial / Green-Schwarz factorization", raised.exception.required_carrier)
        self.assertIn("anomaly-closure data", raised.exception.parent_object)

    def test_available_losses_do_not_make_the_packet_a_source_action(self):
        score = lc.candidate_score_from_available_losses(
            anomaly_green_schwarz_candidate(),
            growth_value=5.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )

        self.assertTrue(score.passes_hard_guards())
        self.assertEqual(score.adversarial_losses["L_boundary_index"], 1.0)
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)


if __name__ == "__main__":
    unittest.main()
