"""Audit the 1203 cycle 2 verifier/firewall artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1203"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1203-cycle2-dgu-custody-packet-admission-verifier.md",
    "TAU": ROOT / "explorations/hourly-20260626-1203-cycle2-tau-fixed-aleph-packet-verifier.md",
    "KIG": ROOT / "explorations/hourly-20260626-1203-cycle2-kig-pre-codomain-row-verifier.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1203-cycle2-productab-source-object-verifier.md",
    "QFT": ROOT / "explorations/hourly-20260626-1203-cycle2-qft-same-context-edge-verifier.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    marker = "```json"
    start = text.rfind(marker)
    if start == -1:
        raise AssertionError(f"missing JSON summary in {path}")
    start = text.find("\n", start) + 1
    end = text.find("```", start)
    if end == -1:
        raise AssertionError(f"unterminated JSON summary in {path}")
    return json.loads(text[start:end])


class Cycle2VerifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertTrue(summary["verifier_defined"])
                self.assertTrue(summary["verifier_applied"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_verifier_rejects_before_retry_unlocks(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertFalse(dgu["current_packet_accepts"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["source_byte_hashable"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["lawful_basis_present"])
        self.assertFalse(dgu["custody_record_present"])
        self.assertFalse(dgu["extraction_policy_present"])
        self.assertFalse(dgu["retry_unlocks"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "UCSDDGU01LawfulLocalByteAcquisitionManifest_V1")

    def test_tau_verifier_rejects_incomplete_fixed_aleph_packet(self) -> None:
        tau = self.summaries["TAU"]
        self.assertFalse(tau["fixed_aleph_packet_accepts"])
        self.assertFalse(tau["field_space_theorem_present"])
        self.assertFalse(tau["tangent_certificate_present"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["full_EL_tuple_present"])
        self.assertFalse(tau["target_erasure_witness_present"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])
        self.assertEqual(tau["first_failed_atom"], "field_space_theorem")

    def test_kig_verifier_rejects_without_source_row(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["current_row_accepts"])
        self.assertFalse(kig["source_row_present"])
        self.assertFalse(kig["parent_slot_pre_codomain_found"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertFalse(kig["noncircular_order_log_present"])
        self.assertFalse(kig["rival_parent_classes_closed"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])

    def test_productab_verifier_rejects_metadata_only_state(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["current_object_accepts"])
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertEqual(product["video_id"], "TzSEvmqxu48")
        self.assertFalse(product["formula_bearing_source_object_present"])
        self.assertFalse(product["content_bearing_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])

    def test_qft_verifier_rejects_absent_same_context_edge(self) -> None:
        qft = self.summaries["QFT"]
        self.assertFalse(qft["current_edge_accepts"])
        self.assertFalse(qft["same_context_edge_present"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["roles_type_over_same_context"])
        self.assertFalse(qft["dependency_DAG_forbidden_edge_free"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

