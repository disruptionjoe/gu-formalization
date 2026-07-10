#!/usr/bin/env python3
"""Regression checks for the source-action buildbench packet.

Run: python tests/test_source_action_buildbench.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))

from lib import loss_channels as lc  # noqa: E402
from lib.source_action_buildbench import (  # noqa: E402
    BuildbenchCandidate,
    BuildbenchVerdict,
    CandidatePhase,
    FieldSpaceDeclaration,
    InvarianceAssumption,
    buildbench_summary,
    evaluate_candidate,
    run_default_buildbench,
)


class SourceActionBuildbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reports = run_default_buildbench()
        cls.summary = buildbench_summary(cls.reports)

    def test_default_rows_are_explicitly_declared_and_guarded(self):
        self.assertEqual(self.summary["candidate_count"], 4)
        self.assertEqual(self.summary["hard_failures"], {})

        for report in self.reports:
            with self.subTest(candidate=report.candidate.name):
                self.assertNotEqual(report.effective_field_space, FieldSpaceDeclaration.UNDECLARED)
                self.assertEqual(
                    set(report.computable_losses),
                    {
                        "L_boundary_symbol",
                        "L_boundary_index",
                        "L_target_import",
                        "L_acausal_trap",
                    },
                )
                self.assertTrue(report.hard_guards["anti_import"])
                self.assertTrue(report.hard_guards["anti_trap_bare_commutator_preserved"])

    def test_sg4_anchor_scale_row_advances_to_source_noether_tau(self):
        a_door = next(
            report
            for report in self.reports
            if report.candidate.name == "sg4-minimal-bv-kt-finite-fiber-closure"
        )

        self.assertEqual(a_door.candidate.field_space, FieldSpaceDeclaration.FULL_VECTOR_SPINOR)
        self.assertEqual(a_door.effective_field_space, FieldSpaceDeclaration.FULL_VECTOR_SPINOR)
        self.assertEqual(a_door.candidate.phase, CandidatePhase.SOURCE_NOETHER_TAU)
        self.assertEqual(a_door.verdict, BuildbenchVerdict.MISSING_CARRIER_BLOCKED)
        self.assertIn("Noether/tau carrier", a_door.next_action)
        self.assertEqual(self.summary["ready_for_anchor_scale_a_door"], ())

    def test_named_missing_carriers_are_collected_for_hourly_handoff(self):
        expected_missing = {
            "L_anomaly",
            "L_RS_BRST",
            "L_theta_source",
            "L_weak_field",
            "L_families_pushforward",
        }

        for report in self.reports:
            with self.subTest(candidate=report.candidate.name):
                self.assertTrue(expected_missing.issubset(set(report.missing_channel_names())))

        self.assertEqual(self.summary["next_hourly_progress_point"], "SOURCE-NOETHER-TAU-CARRIER")

    def test_boundary_bridge_row_records_the_index_wall_without_promoting(self):
        boundary = next(
            report
            for report in self.reports
            if report.candidate.name == "boundary-spectral-section-bridge"
        )

        self.assertEqual(boundary.verdict, BuildbenchVerdict.BOUNDARY_INDEX_WALL)
        self.assertEqual(boundary.computable_losses["L_boundary_symbol"], 0.0)
        self.assertEqual(boundary.computable_losses["L_boundary_index"], 1.0)
        self.assertIn("BV-to-boundary-Dirac bridge", boundary.next_action)

    def test_available_loss_security_budget_is_downstream_not_a_source_action(self):
        budget = next(
            report
            for report in self.reports
            if report.candidate.name == "available-loss-only-security-budget"
        )

        self.assertEqual(budget.effective_field_space, FieldSpaceDeclaration.SELECTOR_NOT_ACTION)
        self.assertEqual(budget.verdict, BuildbenchVerdict.DOWNSTREAM_PREMATURE)
        self.assertTrue(budget.hard_guards["field_space_declared_or_auto_declared"])
        self.assertIn("defer selection", budget.next_action)

    def test_target_import_candidate_fails_before_scoring(self):
        imported = BuildbenchCandidate(
            name="bad-target-import",
            description="Uses chi(K3)=24 to normalize the source action.",
            field_space=FieldSpaceDeclaration.FULL_VECTOR_SPINOR,
            invariance=InvarianceAssumption.H_LINEAR_NON_EQUIVARIANT,
            phase=CandidatePhase.BV_CLOSURE,
            assumptions=("chi(K3)=24",),
        )

        report = evaluate_candidate(imported)

        self.assertEqual(report.verdict, BuildbenchVerdict.HARD_GUARD_FAILED)
        self.assertFalse(report.hard_guards["anti_import"])
        self.assertEqual(report.computable_losses["L_target_import"], float("inf"))

    def test_acausal_trap_candidate_fails_before_scoring(self):
        acausal = BuildbenchCandidate(
            name="bad-acausal-trap",
            description="Attempts clean decoupling by driving the bare commutator to 0.",
            field_space=FieldSpaceDeclaration.FULL_VECTOR_SPINOR,
            invariance=InvarianceAssumption.H_LINEAR_NON_EQUIVARIANT,
            phase=CandidatePhase.BV_CLOSURE,
            metrics={"bare_commutator": 0.0},
        )

        report = evaluate_candidate(acausal)

        self.assertEqual(report.verdict, BuildbenchVerdict.HARD_GUARD_FAILED)
        self.assertFalse(report.hard_guards["anti_trap_bare_commutator_preserved"])
        self.assertEqual(report.computable_losses["L_acausal_trap"], float("inf"))


if __name__ == "__main__":
    unittest.main()
