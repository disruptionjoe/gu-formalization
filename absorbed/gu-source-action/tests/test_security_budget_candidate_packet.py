#!/usr/bin/env python3
"""Regression checks for the first security-budget candidate packet.

Run: python tests/test_security_budget_candidate_packet.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402
from lib.security_budget import select_security_budget_winner  # noqa: E402


def packet_candidate(name: str = "available-loss-only-security-budget") -> lc.SourceCandidate:
    return lc.SourceCandidate(
        name=name,
        description=(
            "Uses only currently computable boundary-symbol, boundary-index, target-import, "
            "and anti-trap channels."
        ),
        assumptions=(
            "No target normalization is used.",
            "The bare commutator anchor is preserved.",
            "No candidate-specific anomaly, RS/BRST, theta/source, weak-field, or "
            "families-pushforward carrier is supplied.",
        ),
    )


class SecurityBudgetCarrierPacketTests(unittest.TestCase):
    def test_packet_passes_only_the_current_computable_hard_guards(self):
        score = lc.candidate_score_from_available_losses(packet_candidate(), growth_value=4.0)

        self.assertTrue(score.hard_guards["anti_import"])
        self.assertTrue(score.hard_guards["anti_trap_bare_commutator_preserved"])
        self.assertTrue(score.hard_guards["boundary_symbol_carrier_exists"])
        self.assertEqual(score.adversarial_losses["L_boundary_symbol"], 0.0)
        self.assertEqual(score.adversarial_losses["L_boundary_index"], 1.0)
        self.assertEqual(score.adversarial_losses["L_target_import"], 0.0)
        self.assertEqual(score.adversarial_losses["L_acausal_trap"], 0.0)
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)

    def test_required_source_action_carriers_are_still_missing(self):
        candidate = packet_candidate()

        for channel in lc.MISSING_CARRIER_CHANNELS:
            with self.subTest(channel=channel.__name__):
                with self.assertRaises(lc.MissingCarrierError) as raised:
                    channel(candidate)
                self.assertTrue(raised.exception.required_carrier)
                self.assertTrue(raised.exception.parent_object)

    def test_available_generic_losses_do_not_select_between_candidates(self):
        a = lc.candidate_score_from_available_losses(
            packet_candidate("candidate-a"),
            growth_value=4.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )
        b = lc.candidate_score_from_available_losses(
            packet_candidate("candidate-b"),
            growth_value=4.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )

        with self.assertRaisesRegex(ValueError, "tied"):
            select_security_budget_winner([a, b])


if __name__ == "__main__":
    unittest.main()
