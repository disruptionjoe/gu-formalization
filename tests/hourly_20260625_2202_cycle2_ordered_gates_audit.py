"""Audit the 2202 cycle 2 ordered frontier gates."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2202"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260625-2202-cycle2-ig-source-operator-locator-scan.md",
    "RS": ROOT / "explorations/hourly-20260625-2202-cycle2-rs-browser-capture-toolchain-row.md",
    "PTUJ": ROOT / "explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md",
    "DGU": ROOT / "explorations/hourly-20260625-2202-cycle2-dgu-source-row-ordering-gate.md",
    "QFT": ROOT / "explorations/hourly-20260625-2202-cycle2-qft-branch-ordering-ledger.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2OrderedGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle2_artifacts_present(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_source_operator_locator_absent(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "blocked_source_locator_absent")
        self.assertTrue(ig["cycle1_two_row_matrix_consumed"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_operator_definition_admitted"])
        self.assertFalse(ig["alpha_source_derived"])
        self.assertFalse(ig["beta_source_derived"])
        self.assertFalse(ig["rival_projector_identity_admitted"])
        self.assertFalse(ig["selector_restart_allowed"])

    def test_rs_capture_toolchain_absent_after_directory_row(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "blocked_capture_toolchain_absent")
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertTrue(rs["python_available"])
        self.assertTrue(rs["pil_available"])
        self.assertFalse(rs["browser_executable_available"])
        self.assertFalse(rs["playwright_available"])
        self.assertFalse(rs["selenium_available"])
        self.assertFalse(rs["yt_dlp_available"])
        self.assertFalse(rs["ffmpeg_available"])
        self.assertFalse(rs["tesseract_available"])
        self.assertFalse(rs["browser_capture_toolchain_row_admitted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_ptuj_branch_exclusivity_blocks_mixed_receipts(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["verdict_class"], "blocked_branch_exclusivity")
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertTrue(ptuj["mixed_branch_packet_rejected"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

    def test_dgu_ordering_keeps_symbol_work_downstream(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked_ordering_clarified")
        self.assertFalse(dgu["source_emitted_0_1_sector_rule_found"])
        self.assertFalse(dgu["same_operator_witness_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertEqual(dgu["ordered_first_row"], "source_emitted_0_1_sector_rule")
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

    def test_qft_ordering_keeps_generic_carrier_from_promoting(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["verdict_class"], "underdefined_ordering_clarified")
        self.assertFalse(qft["branch_label_row_source_defined"])
        self.assertFalse(qft["admissibility_rule_source_defined"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertTrue(qft["generic_Y_carrier_schema_available"])
        self.assertFalse(qft["generic_Y_promoted_to_branch_receipt"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertEqual(qft["ordered_first_row"], "branch_label_source_row")


if __name__ == "__main__":
    unittest.main(verbosity=2)
