"""Audit the 0002 cycle 2 downstream frontier gates."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0002"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0002-cycle2-ig-located-operator-binding-gate.md",
    "RS": ROOT / "explorations/hourly-20260626-0002-cycle2-rs-first-frame-execution-gate.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0002-cycle2-ptuj-branch-purity-recheck-gate.md",
    "DGU": ROOT / "explorations/hourly-20260626-0002-cycle2-dgu-same-operator-intake-gate.md",
    "QFT": ROOT / "explorations/hourly-20260626-0002-cycle2-qft-branch-locator-receipt-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2DownstreamGatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_consume_cycle1(self) -> None:
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertTrue(summary["cycle1_consumed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_rs_execution_rejects_challenge_page(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "blocked_public_route_challenge_not_target_frame")
        self.assertTrue(rs["approved_capture_toolchain_admitted"])
        self.assertTrue(rs["capture_tool_identity_admitted"])
        self.assertTrue(rs["headless_capture_executed"])
        self.assertTrue(rs["temp_png_produced"])
        self.assertTrue(rs["temp_png_sha256_computed"])
        self.assertTrue(rs["challenge_page_captured"])
        self.assertFalse(rs["source_timestamp_verification_passed"])
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["first_frame_persisted_as_evidence"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_non_rs_routes_remain_locked_at_upstream_objects(self) -> None:
        ig = self.summaries["IG"]
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["located_operator_binding_evaluable"])
        self.assertFalse(ig["coefficient_derivation_allowed"])

        ptuj = self.summaries["PTUJ"]
        self.assertTrue(ptuj["branch_purity_invariant_defined"])
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["primary_source_row_instance_found"])
        self.assertFalse(dgu["sector_rule_locator_admitted"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])

        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["branch_locator_receipt_admitted"])
        self.assertFalse(qft["Y_b_branch_selected"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
