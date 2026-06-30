"""Audit the 0202 cycle 1 source-intake frontier artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0202"
ARTIFACTS = {
    "IG": ROOT / "explorations/hourly-20260626-0202-cycle1-ig-source-natural-projector-intake-gate.md",
    "RS": ROOT / "explorations/hourly-20260626-0202-cycle1-rs-immutable-frame-package-intake-gate.md",
    "PTUJ": ROOT / "explorations/hourly-20260626-0202-cycle1-ptuj-asset-custody-bifurcation-gate.md",
    "DGU": ROOT / "explorations/hourly-20260626-0202-cycle1-dgu-primary-row-discriminator-gate.md",
    "QFT": ROOT / "explorations/hourly-20260626-0202-cycle1-qft-branch-row-provenance-gate.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if not blocks:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(blocks[-1])


class Cycle1SourceIntakeAudit(unittest.TestCase):
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

    def test_ig_requires_source_natural_projector_identity(self) -> None:
        ig = self.summaries["IG"]
        self.assertTrue(ig["product_a_table_admitted_route_locally"])
        self.assertTrue(ig["product_b_table_admitted_route_locally"])
        self.assertTrue(ig["two_common_rows_present"])
        self.assertFalse(ig["source_operator_locator_found"])
        self.assertFalse(ig["source_natural_projector_identity_found"])
        self.assertFalse(ig["projector_direction_bound"])
        self.assertFalse(ig["coefficient_derivation_allowed"])
        self.assertEqual(ig["first_missing_object"], "SourceNaturalProductABRivalProjectorIdentity_V1")

    def test_rs_external_frame_package_is_absent(self) -> None:
        rs = self.summaries["RS"]
        self.assertTrue(rs["approved_capture_toolchain_consumed"])
        self.assertTrue(rs["directory_policy_row_consumed"])
        self.assertTrue(rs["captcha_or_challenge_route_rejected"])
        self.assertFalse(rs["immutable_external_frame_package_found"])
        self.assertFalse(rs["external_package_custody_manifest_found"])
        self.assertFalse(rs["external_package_frame_sha256_found"])
        self.assertEqual(rs["accepted_evidence_branch_count"], 0)
        self.assertFalse(rs["first_frame_receipt_admitted"])
        self.assertFalse(rs["typed_rs_intake_allowed"])

    def test_ptuj_branches_remain_bifurcated_and_incomplete(self) -> None:
        ptuj = self.summaries["PTUJ"]
        self.assertTrue(ptuj["official_locator_present"])
        self.assertFalse(ptuj["official_custodian_asset_manifest_found"])
        self.assertFalse(ptuj["lawful_local_source_byte_object_found"])
        self.assertFalse(ptuj["lawful_local_toolchain_identity_found"])
        self.assertTrue(ptuj["branch_bifurcation_enforced"])
        self.assertEqual(ptuj["accepted_branch_count"], 0)
        self.assertFalse(ptuj["cross_branch_assembly_allowed"])
        self.assertFalse(ptuj["formula_visibility_allowed"])

    def test_dgu_and_qft_remain_before_downstream_work(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["typed_d_roll_available_as_screen"])
        self.assertFalse(dgu["primary_source_row_instance_found"])
        self.assertFalse(dgu["primary_row_payload_found"])
        self.assertFalse(dgu["row_discriminator_evaluable"])
        self.assertFalse(dgu["same_operator_witness_evaluable"])
        self.assertFalse(dgu["symbol_certificate_allowed"])
        self.assertFalse(dgu["vz_replay_allowed"])

        qft = self.summaries["QFT"]
        self.assertTrue(qft["source_geometry_contract_consumed"])
        self.assertEqual(qft["accepted_branch_label_source_row_count"], 0)
        self.assertEqual(qft["accepted_admissibility_rule_source_row_count"], 0)
        self.assertFalse(qft["branch_row_provenance_packet_found"])
        self.assertFalse(qft["generic_R_QFT_promoted_to_branch_selector"])
        self.assertFalse(qft["Y_b_branch_selected"])
        self.assertFalse(qft["local_groupoid_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
