"""Audit the 0202 cycle 2 downstream firewall artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0202"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0202-cycle2-ig-projector-coefficient-firewall.md",
    "RS": ROOT / "explorations/hourly-20260626-0202-cycle2-rs-frame-package-manifest-firewall.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0202-cycle2-ptuj-branch-receipt-formula-firewall.md",
    "DGU": ROOT / "explorations/hourly-20260626-0202-cycle2-dgu-row-to-same-operator-firewall.md",
    "QFT": ROOT / "explorations/hourly-20260626-0202-cycle2-qft-branch-row-carrier-firewall.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2DownstreamFirewallsAudit(unittest.TestCase):
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

    def test_ig_coefficients_wait_for_projector_identity(self) -> None:
        ig = self.summaries["IG"]
        self.assertTrue(ig["two_common_rows_present"])
        self.assertFalse(ig["source_natural_projector_identity_found"])
        self.assertTrue(ig["projector_to_coefficient_firewall_active"])
        self.assertFalse(ig["alpha_source_derived"])
        self.assertFalse(ig["beta_source_derived"])
        self.assertFalse(ig["finite_common_rows_promoted_to_selector"])

    def test_rs_and_ptuj_manifest_layers_are_firewalled(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["approved_capture_toolchain_consumed"])
        self.assertFalse(rs["immutable_external_frame_package_found"])
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertTrue(rs["frame_manifest_firewall_active"])
        self.assertFalse(rs["crop_ocr_manifest_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

        ptuj = self.summaries["PTUJ"]
        self.assertTrue(ptuj["branch_bifurcation_enforced"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertTrue(ptuj["formula_visibility_firewall_active"])
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertFalse(ptuj["keating_ptuj_identity_comparison_allowed"])

    def test_dgu_and_qft_downstream_work_is_blocked(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["typed_d_roll_available_as_screen"])
        self.assertFalse(dgu["primary_row_payload_found"])
        self.assertFalse(dgu["row_discriminator_evaluable"])
        self.assertTrue(dgu["same_operator_firewall_active"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

        qft = self.summaries["QFT"]
        self.assertTrue(qft["source_geometry_contract_consumed"])
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["branch_row_provenance_packet_found"])
        self.assertTrue(qft["carrier_selection_firewall_active"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["quotient_descent_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
