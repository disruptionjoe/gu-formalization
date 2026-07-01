"""Audit the 0103 cycle 1 frontier specificity artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0103"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0103-cycle1-ig-source-locator-specificity-gate.md",
    "RS": ROOT / "explorations/hourly-20260626-0103-cycle1-rs-evidence-route-classifier.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0103-cycle1-ptuj-branch-packet-field-ledger.md",
    "DGU": ROOT / "explorations/hourly-20260626-0103-cycle1-dgu-source-row-payload-gate.md",
    "QFT": ROOT / "explorations/hourly-20260626-0103-cycle1-qft-precarrier-source-row-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1FrontierSpecificityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_no_restart(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_specific_locator_still_missing(self) -> None:
        ig = self.summaries["IG"]
        self.assertTrue(ig["finite_host_available"])
        self.assertTrue(ig["source_neighborhood_hits_exist"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["operator_direction_bound"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertEqual(
            ig["constructive_next_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1",
        )

    def test_rs_rejects_non_frame_branches(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["approved_capture_toolchain_consumed"])
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["direct_public_route_still_challenged"])
        self.assertTrue(rs["metadata_route_rejected"])
        self.assertTrue(rs["thumbnail_route_rejected"])
        self.assertTrue(rs["transcript_route_rejected"])
        self.assertFalse(rs["external_immutable_frame_package_found"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_source_object_routes_remain_at_upstream_fields(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertFalse(ptuj["official_branch_complete"])
        self.assertFalse(ptuj["lawful_local_branch_complete"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["primary_source_row_instance_found"])
        self.assertFalse(dgu["source_row_payload_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertTrue(dgu["typed_d_roll_allowed_as_quarantined_screen"])

        qft = self.summaries["QFT"]
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
