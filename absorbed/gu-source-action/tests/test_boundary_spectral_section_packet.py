#!/usr/bin/env python3
"""Regression checks for the boundary spectral-section carrier packet.

Run: python tests/test_boundary_spectral_section_packet.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402


def boundary_spectral_section_candidate() -> lc.SourceCandidate:
    return lc.SourceCandidate(
        name="boundary-spectral-section-security-budget",
        description=(
            "Attempts to use the computed BV-to-boundary symbol and APS "
            "spectral section as the candidate-specific security-budget carrier."
        ),
        assumptions=(
            "No target normalization, Euler-characteristic shortcut, or K3 import is used.",
            "The bare commutator anchor is preserved.",
            "Zero-mode filling is not treated as source-side issuance.",
            "A fixed boundary spectral section is not treated as closed internal S_IG data.",
        ),
    )


class BoundarySpectralSectionPacketTests(unittest.TestCase):
    def test_computable_guards_remain_clean(self):
        candidate = boundary_spectral_section_candidate()

        target_import = lc.l_target_import(candidate)
        acausal_trap = lc.l_acausal_trap(candidate)
        boundary_symbol = lc.l_boundary_symbol(candidate)

        self.assertEqual(target_import.value, 0.0)
        self.assertEqual(target_import.details["matches"], [])
        self.assertEqual(acausal_trap.value, 0.0)
        self.assertEqual(acausal_trap.details["matches"], [])
        self.assertEqual(boundary_symbol.value, 0.0)
        self.assertTrue(boundary_symbol.details["map_built"])
        self.assertTrue(boundary_symbol.details["C2_is_HS_symbol_norm"])
        self.assertAlmostEqual(boundary_symbol.details["C2"], lc.EXPECTED_C2, places=2)

    def test_boundary_index_channel_records_the_eta_wall(self):
        boundary_index = lc.l_boundary_index(boundary_spectral_section_candidate())

        self.assertEqual(boundary_index.status, "computed")
        self.assertEqual(boundary_index.value, 1.0)
        self.assertEqual(boundary_index.details["eta_D_sigma"], 0)
        self.assertTrue(boundary_index.details["eta_forced_zero"])
        self.assertFalse(boundary_index.details["section_connects"])
        self.assertEqual(
            boundary_index.details["verdict"],
            "BV_BOUNDARY_MAP_EXISTS_BUT_APS_INDEX_ROUTE_FAILS",
        )

    def test_available_losses_do_not_make_the_packet_a_source_action(self):
        score = lc.candidate_score_from_available_losses(
            boundary_spectral_section_candidate(),
            growth_value=5.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )

        self.assertTrue(score.passes_hard_guards())
        self.assertEqual(score.adversarial_losses["L_boundary_symbol"], 0.0)
        self.assertEqual(score.adversarial_losses["L_boundary_index"], 1.0)
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)


if __name__ == "__main__":
    unittest.main()
