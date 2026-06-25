"""Audit the 2202 cycle 1 frontier receipt artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2202"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260625-2202-cycle1-ig-two-row-source-operator-receipt.md",
    "RS": ROOT / "explorations/hourly-20260625-2202-cycle1-rs-owned-directory-policy-row.md",
    "PTUJ": ROOT / "explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md",
    "DGU": ROOT / "explorations/hourly-20260625-2202-cycle1-dgu-primary-source-row-scan.md",
    "QFT": ROOT / "explorations/hourly-20260625-2202-cycle1-qft-branch-label-source-scan.md",
}
RS_DIRECTORY_README = ROOT / "automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md"


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1FrontierReceiptsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_cycle1_artifacts_present(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_two_row_source_operator_is_precise_blocker(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "blocked")
        self.assertTrue(ig["product_a_receipt_consumed"])
        self.assertTrue(ig["product_b_receipt_consumed"])
        self.assertEqual(ig["accepted_receipt_count"], 2)
        self.assertEqual(ig["common_rows"], ["V(omega_1 + omega_7)", "V(omega_6)"])
        self.assertTrue(ig["abstract_two_row_matrix_defined"])
        self.assertFalse(ig["source_operator_definition_admitted"])
        self.assertFalse(ig["rival_projector_identity_admitted"])
        self.assertEqual(
            ig["first_obstruction"],
            "ProductABSourceOperatorTwoRowProjectorMatrixReceipt_V1.source_operator_definition",
        )

    def test_rs_directory_policy_row_closed_only_first_precondition(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "conditional_directory_policy_closed")
        self.assertTrue(rs["route_receipt_consumed"])
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertEqual(rs["owned_directory_path"], "automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi")
        self.assertTrue(RS_DIRECTORY_README.exists())
        directory_summary = extract_summary(RS_DIRECTORY_README)
        self.assertTrue(directory_summary["directory_policy_row_admitted"])
        self.assertEqual(directory_summary["persisted_frame_count"], 0)
        self.assertFalse(rs["browser_capture_toolchain_row_admitted"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_ptuj_remains_branch_packet_blocked(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["verdict_class"], "blocked")
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["official_branch_accepted"])
        self.assertFalse(ptuj["lawful_local_branch_accepted"])
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

    def test_dgu_scoped_negative_blocks_symbol_work(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked_scoped_negative")
        self.assertTrue(dgu["source_stable_packet_consumed"])
        self.assertTrue(dgu["typed_spine_algebra_available"])
        self.assertFalse(dgu["source_emitted_0_1_sector_rule_found"])
        self.assertFalse(dgu["same_operator_witness_found"])
        self.assertFalse(dgu["source_emitted_receipt_admitted"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

    def test_qft_branch_label_source_rows_absent(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["verdict_class"], "underdefined")
        self.assertFalse(qft["branch_label_row_source_defined"])
        self.assertFalse(qft["admissibility_rule_source_defined"])
        self.assertFalse(qft["observation_section_source_defined"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["typed_R_raw_b_O_admitted"])
        self.assertFalse(qft["carrier_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
