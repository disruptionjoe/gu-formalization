import unittest

from lib.adapter_discriminator import run_discriminator, summarize_verdict


class AdapterDiscriminatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = run_discriminator()
        cls.summary = summarize_verdict(cls.rows)

    def test_metric_controls_stay_zero(self):
        metric = [row for row in self.rows if row.metric_so95]
        self.assertGreaterEqual(len(metric), 2)
        self.assertTrue(all(row.sig_delta == 0 for row in metric))
        self.assertTrue(self.summary["metric_controls_zero"])

    def test_discriminator_has_nonmetric_signal_or_clean_zero_verdict(self):
        self.assertIn(
            self.summary["round_verdict"],
            {
                "structured_nonmetric_signals_exist_but_no_source_carrier",
                "one_live_structured_candidate",
                "all_structured_candidates_zero",
            },
        )

    def test_no_candidate_silently_promoted(self):
        live = [
            row
            for row in self.rows
            if row.guard_status == "one_live_structured_candidate"
        ]
        self.assertEqual(live, [])


if __name__ == "__main__":
    unittest.main()
