import unittest

from lib.compensator_adapter import (
    run_compensator_discriminator,
    summarize_compensator_verdict,
)


class CompensatorAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = run_compensator_discriminator()
        cls.summary = summarize_compensator_verdict(cls.rows)

    def test_full_escape_cancellation_is_a_trap(self):
        row = next(row for row in self.rows if row.name == "full_escape_cancellation")
        self.assertLess(row.escape_ratio, 1e-8)
        self.assertEqual(row.guard_status, "clean_decoupling_trap")

    def test_partial_compensators_do_not_move_bare_anchors(self):
        self.assertTrue(all(row.preserves_bare_anchor for row in self.rows))

    def test_no_compensator_silently_promoted(self):
        self.assertEqual(self.summary["live_candidate_count"], 0)
        self.assertEqual(
            self.summary["round_verdict"],
            "only_decoupling_or_zero_index_compensators",
        )


if __name__ == "__main__":
    unittest.main()
