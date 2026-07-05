#!/usr/bin/env python3
"""Regression checks for the weak-field/source-current carrier packet.

Run: python tests/test_weak_field_source_current_packet.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402


def weak_field_source_candidate() -> lc.SourceCandidate:
    return lc.SourceCandidate(
        name="weak-field-source-current-security-budget",
        description=(
            "Attempts to use a GU-internal weak-field source-current law as the "
            "candidate-specific security-budget carrier."
        ),
        assumptions=(
            "No target normalization is used.",
            "The bare commutator anchor is preserved.",
            "Weak-field compatibility on an imported metric is not treated as a source action.",
            "A weak-field source-current law must be coupled to a candidate S_IG before selection.",
        ),
    )


class WeakFieldSourceCurrentPacketTests(unittest.TestCase):
    def test_computable_guards_remain_clean(self):
        candidate = weak_field_source_candidate()

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

    def test_weak_field_channel_is_the_named_blocker(self):
        candidate = weak_field_source_candidate()

        with self.assertRaises(lc.MissingCarrierError) as raised:
            lc.l_weak_field(candidate)

        self.assertEqual(raised.exception.channel, "L_weak_field")
        self.assertIn("weak-field Schwarzschild/GR recovery loss", raised.exception.required_carrier)
        self.assertIn("weak-field recovery tests", raised.exception.parent_object)

    def test_available_losses_do_not_make_the_packet_a_source_action(self):
        score = lc.candidate_score_from_available_losses(
            weak_field_source_candidate(),
            growth_value=5.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )

        self.assertTrue(score.passes_hard_guards())
        self.assertEqual(score.adversarial_losses["L_boundary_index"], 1.0)
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)


if __name__ == "__main__":
    unittest.main()
