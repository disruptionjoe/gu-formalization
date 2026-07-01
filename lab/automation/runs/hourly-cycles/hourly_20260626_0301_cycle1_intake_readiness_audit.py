"""Audit the 0301 cycle 1 intake-readiness frontier artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0301"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0301-cycle1-ig-projector-identity-intake-readiness.md",
    "RS": ROOT / "explorations/hourly-20260626-0301-cycle1-rs-frame-evidence-intake-readiness.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0301-cycle1-ptuj-branch-pure-packet-intake-readiness.md",
    "DGU": ROOT / "explorations/hourly-20260626-0301-cycle1-dgu-primary-row-intake-readiness.md",
    "QFT": ROOT / "explorations/hourly-20260626-0301-cycle1-qft-branch-provenance-intake-readiness.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1IntakeReadinessAudit(unittest.TestCase):
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

    def test_ig_source_operator_identity_is_absent(self) -> None:
        ig = self.summaries["IG"]
        self.assertFalse(ig["finite_host_tables_recomputed"])
        self.assertTrue(ig["product_a_packet_quoted_as_input"])
        self.assertTrue(ig["product_b_table_quoted_as_input"])
        self.assertEqual(ig["common_row_count"], 2)
        self.assertTrue(ig["intake_contract_specified"])
        self.assertFalse(ig["receipt_admissible_now"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_natural_projector_identity_admitted"])
        self.assertFalse(ig["selector_restart_allowed"])
        self.assertEqual(
            ig["first_missing_field"],
            "ProductABSourceOperatorSourceLocatorReceipt_V1.source_native_operator_locator",
        )

    def test_rs_requires_checksummed_target_frame_bytes(self) -> None:
        rs = self.summaries["RS"]
        self.assertFalse(rs["captcha_or_challenge_interaction_attempted"])
        self.assertTrue(rs["metadata_thumbnail_transcript_substitutes_rejected"])
        self.assertTrue(rs["unchecksummed_screenshot_substitutes_rejected"])
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["approved_capture_toolchain_consumed"])
        self.assertFalse(rs["lawful_timestamp_verified_browser_frame_found"])
        self.assertFalse(rs["lawful_immutable_external_frame_package_found"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])
        self.assertEqual(rs["current_rule_failure"], "frame_bytes_path_absent_under_admitted_evidence_root")

    def test_ptuj_branch_pure_packet_is_not_instantiated(self) -> None:
        ptuj = self.summaries["PTUJ"]
        receipt = ptuj["single_complete_ptuj_branch_receipt"]
        self.assertTrue(receipt["intake_ready_as_schema"])
        self.assertFalse(receipt["instantiated"])
        self.assertFalse(receipt["cross_branch_assembly_allowed"])
        self.assertFalse(receipt["metadata_as_receipt_allowed"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertEqual(ptuj["accepted_receipt_count"], 0)
        self.assertFalse(ptuj["branch_purity_invariant_satisfied"])
        self.assertFalse(ptuj["formula_visibility_allowed"])
        self.assertFalse(ptuj["keating_ptuj_identity_comparison_allowed"])
        self.assertEqual(
            ptuj["first_obstruction"],
            "SingleCompletePTUJBranchReceipt_V1.branch_purity_invariant_satisfied_false",
        )
        self.assertEqual(len(ptuj["branch_rows"]), 2)
        for row in ptuj["branch_rows"]:
            with self.subTest(branch=row["branch_id"]):
                self.assertFalse(row["complete"])
                self.assertFalse(row["accepted"])

    def test_dgu_primary_row_blocks_downstream_symbol_work(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["typed_d_roll_available_as_screen"])
        self.assertFalse(dgu["typed_d_roll_allowed_as_source_row"])
        self.assertFalse(dgu["primary_row_instance_found"])
        self.assertFalse(dgu["primary_row_payload_found"])
        self.assertFalse(dgu["row_extraction_method_found"])
        self.assertFalse(dgu["actual_operator_handle_found"])
        self.assertFalse(dgu["intake_ready_for_same_operator_witness"])
        self.assertFalse(dgu["intake_ready_for_symbol_certificate"])
        self.assertFalse(dgu["intake_ready_for_vz_replay"])
        self.assertEqual(
            dgu["first_missing_field"],
            "PrimarySourceDGU01SectorRuleRowInstance_V1.source_row_payload",
        )

    def test_qft_branch_rows_are_underdefined_before_carrier_work(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["source_geometry_contract_consumed"])
        self.assertTrue(qft["branch_row_provenance_packet_defined_as_required_intake"])
        self.assertFalse(qft["branch_row_provenance_packet_admitted"])
        self.assertEqual(qft["accepted_source_branch_label_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["precarrier_independence_proof_present"])
        self.assertIn("QFTBranchRowProvenancePacket_V1.source_branch_label_row", qft["exact_missing_rows"])
        locks = qft["downstream_locks"]
        self.assertFalse(locks["Y_b_branch_selected"])
        self.assertFalse(locks["source_defined_iota_b_admitted"])
        self.assertFalse(locks["typed_R_raw_b_O_admitted"])
        self.assertFalse(locks["local_groupoid_allowed"])
        self.assertFalse(locks["quotient_descent_allowed"])
        self.assertFalse(locks["proof_restart_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
