#!/usr/bin/env python3
"""Audit the DE-AMP diagnostic closure evidence chain.

This is a process and provenance gate. It checks that the local H46B-verified
inputs, H46C calibration calculation, W129 band sweep, and closure note are wired
as diagnostic evidence. It does not validate the cosmology calculations or change
any claim status.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
RECOVERY_MATRIX = ROOT / "lab" / "process" / "recovery-certification-matrix.json"
H46B_TEST = ROOT / "tests" / "wave45" / "H46B_referee_grade_desi_verification.py"
H46B_NOTE = (
    ROOT / "explorations" / "wave45" / "H46B-referee-grade-desi-verification-2026-07-13.md"
)
H46C_TEST = ROOT / "tests" / "wave46" / "H46C_theta_star_cmb_calibration.py"
H46C_NOTE = (
    ROOT / "explorations" / "wave46" / "H46C-theta-star-gu-cmb-calibration-2026-07-13.md"
)
W129_TEST = ROOT / "tests" / "W129_oq2_m2_band_sweep.py"
W129_NOTE = ROOT / "explorations" / "W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md"
W242_NOTE = ROOT / "explorations" / "W242-desi-intake-and-hourly-prediction-queue-2026-07-15.md"
CLOSURE_NOTE = ROOT / "explorations" / "de-amp-diagnostic-closure-audit-2026-07-15.md"
RESEARCH_STATUS = ROOT / "RESEARCH-STATUS.md"
CANON_THETA_DE = ROOT / "canon" / "theta-field-flrw-dark-energy-eos.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class DeAmpDiagnosticClosureAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.portfolio = json.loads(read(PORTFOLIO))
        cls.matrix = json.loads(read(RECOVERY_MATRIX))
        cls.lanes = {lane["id"]: lane for lane in cls.portfolio["lanes"]}
        cls.h46b_test = read(H46B_TEST)
        cls.h46b_note = read(H46B_NOTE)
        cls.h46c_test = read(H46C_TEST)
        cls.h46c_note = read(H46C_NOTE)
        cls.w129_test = read(W129_TEST)
        cls.w129_note = read(W129_NOTE)
        cls.w242_note = read(W242_NOTE)
        cls.closure_note = read(CLOSURE_NOTE)

    def test_required_evidence_files_exist(self) -> None:
        required = (
            H46B_TEST,
            H46B_NOTE,
            H46C_TEST,
            H46C_NOTE,
            W129_TEST,
            W129_NOTE,
            W242_NOTE,
            CLOSURE_NOTE,
            RESEARCH_STATUS,
            CANON_THETA_DE,
        )
        missing = [path.relative_to(ROOT).as_posix() for path in required if not path.is_file()]
        self.assertEqual([], missing)

    def test_portfolio_keeps_de_amp_diagnostic_and_source_gated(self) -> None:
        lane = self.lanes["DE-AMP-DIAGNOSTIC"]
        self.assertEqual("diagnostic", lane["track"])
        self.assertTrue(lane["hourly_eligible"])
        self.assertIn("H46B", lane["next_swing"])
        self.assertIn("data hygiene", lane["forbidden_shortcut"])
        self.assertIn("not a decisive or distinctive GU prediction", lane["forbidden_shortcut"])
        self.assertIn("Only H46B-verified likelihood inputs", lane["forbidden_shortcut"])

    def test_recovery_matrix_classifies_de_amp_as_negative_control(self) -> None:
        controls = {
            control["id"]: control
            for control in self.matrix["shared_setup"]["negative_controls"]
        }
        de_amp = controls["DE-AMP-DIAGNOSTIC"]
        self.assertEqual("DIAGNOSTIC", de_amp["classification"])
        self.assertIn("not a distinctive prediction", de_amp["reason"])
        self.assertEqual(
            "explorations/W242-desi-intake-and-hourly-prediction-queue-2026-07-15.md",
            de_amp["evidence"],
        )

    def test_h46b_is_the_local_source_input_certificate(self) -> None:
        required_test_fragments = (
            "P2_ROWS",
            "P2_MEAN",
            "P2_COV",
            "Official DESI DR2 BAO Gaussian likelihood files",
            "H46 mean vector == official mean file",
            "H46 covariance == official cov file",
            "DESI DR2 digits VERIFIED",
            "CPL falsification remains headline",
        )
        missing_test = [
            fragment for fragment in required_test_fragments if fragment not in self.h46b_test
        ]
        self.assertEqual([], missing_test)

        required_note_fragments = (
            "DESI DR2 digits are now VERIFIED",
            "official likelihood files",
            "dAIC = -3.17",
            "NOT decisive",
            "OPEN stays OPEN",
        )
        missing_note = [
            fragment for fragment in required_note_fragments if fragment not in self.h46b_note
        ]
        self.assertEqual([], missing_note)

    def test_h46c_consumes_h46b_machinery_for_the_amplitude_resolve(self) -> None:
        required = (
            "Discharges (or fails) blocker B1 of Wave 45 (H46B)",
            "H46_de_raw_bao_likelihood.py",
            "GU's OWN CMB-calibrated amplitude",
            "Row 2  OWN theta_star calibration",
            "A_GU(CMB",
            "rescue dissolves",
        )
        missing = [fragment for fragment in required if fragment not in self.h46c_test]
        self.assertEqual([], missing)

        note_required = (
            "Wave 45 (H46B) cleared the DESI DR2 digit gate",
            "A_GU(CMB)",
            "OVERSHOOTS",
            "canon verdict OPEN unchanged",
        )
        missing_note = [
            fragment for fragment in note_required if fragment not in self.h46c_note
        ]
        self.assertEqual([], missing_note)

    def test_w129_closes_the_band_gate_without_turning_it_into_prediction(self) -> None:
        required = (
            "Import the H46C calibration module VERBATIM",
            "ESCAPE TEST",
            "HOLDS-BAND-WIDE",
            "SNe integration remains OUT of scope",
            "f0/B_i remain fits, not GU predictions",
        )
        missing = [fragment for fragment in required if fragment not in self.w129_test]
        self.assertEqual([], missing)

        note_required = (
            "HOLDS-BAND-WIDE",
            "M^2-dependent softening",
            "Everything the bound allows anywhere on the band is an LCDM mimic",
            "f0 and B_i remain fits, not GU predictions",
        )
        missing_note = [
            fragment for fragment in note_required if fragment not in self.w129_note
        ]
        self.assertEqual([], missing_note)

    def test_w242_names_de_amp_as_ready_but_source_hygiene_only(self) -> None:
        required = (
            "`DE-AMP`: GU CMB acoustic-scale amplitude re-solve",
            "H46B's official 13-element mean and 13 by 13 covariance remain authoritative",
            "none of the report's raw-distance values may enter GU calculations",
            "data hygiene, not GU's dark-energy claim",
            "without calling it a novel prediction",
        )
        missing = [fragment for fragment in required if fragment not in self.w242_note]
        self.assertEqual([], missing)

    def test_closure_note_recommends_only_daily_steward_reconciliation(self) -> None:
        required = (
            "Operational result: CLOSED",
            "recommended daily-steward disposition",
            "diagnostic lane is closable",
            "not a prediction",
            "No canon, verdict, claim-status, public-posture, paper, or external-action move",
            "SNe integration",
            "second BAO dataset",
            "daily steward",
        )
        missing = [fragment for fragment in required if fragment not in self.closure_note]
        self.assertEqual([], missing)

    def test_public_status_surfaces_remain_unmoved(self) -> None:
        status = read(RESEARCH_STATUS)
        canon = read(CANON_THETA_DE)
        self.assertIn("Verdict stays OPEN", status)
        self.assertIn("DARK-ENERGY-06", status)
        self.assertIn("verdict: OPEN", canon)

    def test_new_closure_files_do_not_leak_local_paths_or_em_dashes(self) -> None:
        forbidden_windows = "C:" + "\\\\" + "Users" + "\\\\" + "joe"
        forbidden_posix = "C:" + "/" + "Users" + "/" + "joe"
        for path in (Path(__file__), CLOSURE_NOTE):
            text = read(path)
            with self.subTest(path=path.relative_to(ROOT).as_posix()):
                self.assertNotIn(forbidden_windows, text)
                self.assertNotIn(forbidden_posix, text)
                self.assertNotIn("\u2014", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
