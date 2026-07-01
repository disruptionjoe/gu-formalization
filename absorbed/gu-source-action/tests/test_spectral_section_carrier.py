import unittest

from lib.spectral_section_carrier import (
    run_section_discriminator,
    summarize_section_verdict,
)


class SpectralSectionCarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = run_section_discriminator()
        cls.summary = summarize_section_verdict(cls.rows)

    def test_boundary_spectrum_has_forced_zero_eta(self):
        self.assertEqual(self.summary["d_sigma_positive_count"], 128)
        self.assertEqual(self.summary["d_sigma_negative_count"], 128)
        self.assertEqual(self.summary["d_sigma_eta"], 0)
        self.assertLess(self.summary["anticomm_norm"], 1e-8)

    def test_strict_positive_section_is_symmetric(self):
        row = next(row for row in self.rows if row.name == "strict_positive_aps")
        self.assertEqual(row.nonzero_eta, 0)
        self.assertEqual(row.zero_selected, 0)
        self.assertEqual(row.guard_status, "symmetric_section_zero")

    def test_zero_mode_sections_are_absorbed_not_promoted(self):
        absorbed = [row for row in self.rows if row.guard_status == "zero_mode_choice_absorbed"]
        self.assertGreaterEqual(len(absorbed), 1)
        self.assertTrue(
            all(row.absorber_status == "fixed_projector_or_fixed_H_absorber" for row in absorbed)
        )

    def test_no_section_silently_promoted(self):
        self.assertEqual(self.summary["live_candidate_count"], 0)
        self.assertEqual(
            self.summary["round_verdict"],
            "only_symmetric_or_fixed_zero_mode_sections",
        )


if __name__ == "__main__":
    unittest.main()
