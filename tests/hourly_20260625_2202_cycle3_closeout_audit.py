"""Audit the 2202 cycle 3 closeout and synthesis artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2202"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260625-2202-cycle3-ig-representation-host-firewall.md",
    "RS": ROOT / "explorations/hourly-20260625-2202-cycle3-rs-manifest-admission-classifier.md",
    "PTUJ": ROOT / "explorations/hourly-20260625-2202-cycle3-ptuj-proof-restart-classifier.md",
    "DGU": ROOT / "explorations/hourly-20260625-2202-cycle3-dgu-symbol-firewall-closeout.md",
    "QFT": ROOT / "explorations/hourly-20260625-2202-cycle3-qft-carrier-firewall-closeout.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260625-2202-three-cycle-fifteen-hole-synthesis.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_cycle3_artifacts_present(self) -> None:
        for route in ("IG", "RS", "PTUJ", "DGU", "QFT"):
            summary = self.summaries[route]
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_is_host_not_selector(self) -> None:
        ig = self.summaries["IG"]
        self.assertEqual(ig["verdict_class"], "host_not_selector")
        self.assertTrue(ig["finite_representation_host_admitted"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["rival_projector_identity_admitted"])
        self.assertFalse(ig["selector_restart_allowed"])

    def test_rs_only_directory_policy_row_closed(self) -> None:
        rs = self.summaries["RS"]
        self.assertEqual(rs["verdict_class"], "conditional_directory_policy_closed_manifest_blocked")
        self.assertTrue(rs["directory_policy_row_admitted"])
        self.assertFalse(rs["browser_capture_toolchain_row_admitted"])
        self.assertFalse(rs["frame_manifest_admitted"])
        self.assertEqual(rs["persisted_frame_count"], 0)
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_restart_allowed"])
        self.assertFalse(rs["index_restart_allowed"])

    def test_ptuj_dgu_qft_remain_before_downstream_work(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["source_emitted_0_1_sector_rule_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

        qft = self.summaries["QFT"]
        self.assertFalse(qft["branch_label_row_source_defined"])
        self.assertFalse(qft["generic_Y_promoted_to_branch_receipt"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])

    def test_synthesis_records_fifteen_holes_and_no_restart(self) -> None:
        syn = self.summaries["SYNTHESIS"]
        self.assertEqual(syn["run_id"], RUN_ID)
        self.assertEqual(syn["target_quality_holes"], 15)
        self.assertEqual(syn["quality_holes_completed"], 15)
        self.assertFalse(syn["proof_restart_allowed_any_route"])
        self.assertFalse(syn["target_import_used"])
        self.assertEqual(syn["blocked_routes"], ["IG", "RS", "PTUJ", "DGU", "QFT"])
        self.assertTrue(syn["three_cycle_wrapper_improved_quality"])
        self.assertIn(
            "RSOwnedFrameCropOCRManifestArtifactDirectoryForFBozSSLxFvIWindow_V1.directory_policy_row",
            syn["closed_or_conditional_objects"],
        )
        self.assertEqual(len(syn["next_frontier_ranked"]), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
