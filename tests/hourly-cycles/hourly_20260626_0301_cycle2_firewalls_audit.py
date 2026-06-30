"""Audit the 0301 cycle 2 downstream firewall artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0301"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0301-cycle2-ig-source-operator-admission-firewall.md",
    "RS": ROOT / "explorations/hourly-20260626-0301-cycle2-rs-frame-manifest-admission-firewall.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0301-cycle2-ptuj-branch-packet-admission-firewall.md",
    "DGU": ROOT / "explorations/hourly-20260626-0301-cycle2-dgu-primary-row-to-same-operator-firewall.md",
    "QFT": ROOT / "explorations/hourly-20260626-0301-cycle2-qft-branch-row-to-carrier-firewall.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle2FirewallsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_artifacts_are_run_scoped_and_consume_cycle1(self) -> None:
        self.assertEqual(set(self.summaries), {"IG", "RS", "PTUJ", "DGU", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertTrue(summary["cycle1_consumed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertFalse(summary["proof_restart_allowed"])

    def test_ig_blocks_coefficients_and_selector_restart(self) -> None:
        ig = self.summaries["IG"]
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_natural_projector_identity_admitted"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertTrue(ig["source_operator_locator_required"])
        self.assertTrue(ig["source_two_row_action_required"])
        self.assertEqual(
            ig["first_missing_field"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator",
        )
        self.assertEqual(
            ig["next_frontier_object"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1 -> SourceNaturalProductABRivalProjectorIdentity_V1",
        )

    def test_rs_blocks_manifest_and_typed_intake(self) -> None:
        rs = self.summaries["RS"]
        self.assertFalse(rs["frame_manifest_allowed"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertFalse(rs["generation_index_restart_allowed"])
        self.assertFalse(rs["lawful_timestamp_verified_browser_frame_found"])
        self.assertFalse(rs["lawful_immutable_external_frame_package_found"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertEqual(
            rs["first_blocking_manifest_field"],
            "RSFrameCropOCRChecksumManifestForFBozSSLxFvIWindow_V1.source_frame_ref",
        )
        self.assertEqual(rs["next_frontier_object"], "RSImmutableExternalFramePackage_V1")

    def test_ptuj_blocks_formula_visibility_and_identity_comparison(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertFalse(ptuj["ptuj_formula_visibility_audit_allowed"])
        self.assertFalse(ptuj["identity_comparison_allowed"])
        self.assertFalse(ptuj["keating_ptuj_identity_comparison_allowed"])
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["metadata_as_receipt_allowed"])
        self.assertTrue(ptuj["formula_visibility_firewall_active"])
        self.assertEqual(
            ptuj["first_obstruction"],
            "SingleCompletePTUJBranchReceipt_V1.accepted_branch_count_eq_0",
        )

    def test_dgu_blocks_same_operator_symbol_and_vz(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["typed_d_roll_available_as_screen"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source_row"])
        self.assertFalse(dgu["primary_row_payload_found"])
        self.assertFalse(dgu["actual_operator_handle_found"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])
        self.assertEqual(
            dgu["first_missing_field"],
            "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload",
        )
        self.assertIn("DGU01SameOperatorWitness_V1", dgu["blocked_downstream_objects"])

    def test_qft_blocks_carrier_and_local_shadow_work(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["branch_row_provenance_packet_admitted"])
        self.assertFalse(qft["carrier_assignment_allowed"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["source_defined_iota_b_admitted"])
        self.assertFalse(qft["typed_R_raw_b_O_admitted"])
        self.assertFalse(qft["local_groupoid_allowed"])
        self.assertFalse(qft["quotient_descent_allowed"])
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertTrue(qft["host_infrastructure_as_selector_rejected"])
        self.assertIn("QFTBranchToCarrierAssignmentReceipt_V1", qft["blocked_downstream_objects"])
        self.assertEqual(qft["next_frontier_object"], "QFTBranchRowProvenanceSourceAudit_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
