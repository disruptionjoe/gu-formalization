#!/usr/bin/env python3
"""Regression checks for the non-equivariant compensator carrier packet.

Run: python tests/test_non_equivariant_compensator_packet.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402
from lib.adapter_discriminator import run_discriminator, summarize_verdict  # noqa: E402


def compensator_candidate() -> lc.SourceCandidate:
    return lc.SourceCandidate(
        name="non-equivariant-compensator-security-budget",
        description=(
            "Attempts to price the necessary non-equivariant compensator as the "
            "candidate-specific source extension for the security-budget rule."
        ),
        assumptions=(
            "No target normalization is used.",
            "The bare commutator anchor is preserved.",
            "A hand-imposed projector is not treated as a source action.",
            "Arbitrary H-linear index movement is not source-action evidence.",
            "The compensator must still couple to non-vacuous BV bicomplex closure.",
        ),
    )


class NonEquivariantCompensatorPacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = run_discriminator()
        cls.summary = summarize_verdict(cls.rows)

    def test_computable_guards_remain_clean(self):
        candidate = compensator_candidate()

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

    def test_adapter_discriminator_does_not_promote_the_compensator(self):
        structured = [
            row
            for row in self.rows
            if row.structured and not row.metric_so95 and not row.arbitrary
        ]
        arbitrary = [row for row in self.rows if row.arbitrary]

        self.assertGreaterEqual(len(structured), 3)
        self.assertEqual(self.summary["live_structured_candidate_count"], 0)
        self.assertNotEqual(self.summary["round_verdict"], "one_live_structured_candidate")
        self.assertTrue(
            all(
                row.guard_status
                in {
                    "structured_but_zero",
                    "structured_nonmetric_signal_needs_carrier",
                }
                for row in structured
            )
        )
        self.assertTrue(any(row.guard_status == "nonzero_but_arbitrary" for row in arbitrary))

    def test_bv_closure_remains_the_named_compensator_blocker(self):
        with self.assertRaises(lc.MissingCarrierError) as raised:
            lc.l_rs_brst(compensator_candidate())

        self.assertEqual(raised.exception.channel, "L_RS_BRST")
        self.assertIn("candidate non-equivariant compensator", raised.exception.parent_object)
        self.assertIn("full BV bicomplex closure", raised.exception.required_carrier)

    def test_available_losses_do_not_make_the_packet_a_source_action(self):
        score = lc.candidate_score_from_available_losses(
            compensator_candidate(),
            growth_value=5.0,
            validation_cost=0.5,
            finalization_cost=0.5,
        )

        self.assertTrue(score.passes_hard_guards())
        self.assertEqual(score.adversarial_losses["L_boundary_index"], 1.0)
        self.assertEqual(score.worst_case_adversarial_loss(), 1.0)


if __name__ == "__main__":
    unittest.main()
