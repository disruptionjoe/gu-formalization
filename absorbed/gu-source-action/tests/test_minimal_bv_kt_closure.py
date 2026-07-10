from __future__ import annotations

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "lib"
if str(LIB) not in sys.path:
    sys.path.insert(0, str(LIB))

from minimal_bv_kt_closure import (  # noqa: E402
    MinimalBvKtVerdict,
    run_minimal_bv_kt_closure,
)


class MinimalBvKtClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = run_minimal_bv_kt_closure()

    def test_minimal_bv_kt_closure_is_partial_not_source_action(self):
        self.assertEqual(
            self.report.verdict,
            MinimalBvKtVerdict.FINITE_FIBER_CLOSES_SOURCE_NOETHER_BLOCKED,
        )
        self.assertTrue(self.report.finite_fiber_closes)
        self.assertFalse(self.report.source_derived_noether_differential)
        self.assertEqual(self.report.next_progress_point, "SOURCE-NOETHER-TAU-CARRIER")

    def test_raw_gauge_map_is_second_class_before_projection(self):
        self.assertTrue(self.report.raw_map_is_second_class)
        self.assertGreater(self.report.raw_noether_norm, 1.0)
        self.assertEqual(self.report.raw_noether_rank, 128)

    def test_projected_gauge_map_closes_noether_and_kt_cross_terms(self):
        self.assertEqual(self.report.projected_gauge_rank, 128)
        self.assertLess(self.report.projected_noether_norm, 1.0e-8)
        self.assertLess(self.report.kt_cross_norm, 1.0e-8)

    def test_escape_is_kt_exact_but_anchor_scale_obstructions_remain(self):
        self.assertGreater(self.report.escape_norm, 1.0)
        self.assertLess(self.report.escape_kt_exact_residual, 1.0e-8)
        self.assertLess(abs(self.report.bare_commutator_norm - 58.7215), 1.0e-4)
        self.assertLess(abs(self.report.c2_norm - 155.3625), 1.0e-4)
        self.assertEqual(self.report.null_tau_trace_rank, 64)
        self.assertTrue(self.report.bare_commutator_anchor_preserved)


if __name__ == "__main__":
    unittest.main()
