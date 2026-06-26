"""Audit the 1102 cycle 1 acquisition/source-span artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1102"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1102-cycle1-dgu-external-seed-acquisition-packet.md",
    "TAU": ROOT / "explorations/hourly-20260626-1102-cycle1-tau-omega-variation-source-span-audit.md",
    "KIG": ROOT / "explorations/hourly-20260626-1102-cycle1-kig-parent-variation-acquisition-extraction-row.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1102-cycle1-productab-one-branch-payload-acquisition.md",
    "QFT": ROOT / "explorations/hourly-20260626-1102-cycle1-qft-locator-authority-receipt-retry.md",
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


class Cycle1AcquisitionPacketsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 1)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle1-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_seed_acquisition_stays_negative(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["seed_attempted"])
        self.assertTrue(dgu["public_web_search_used"])
        self.assertFalse(dgu["large_media_downloaded"])
        self.assertFalse(dgu["branch_pure_seed_present"])
        self.assertFalse(dgu["official_still_seed_present"])
        self.assertFalse(dgu["lawful_local_video_seed_present"])
        self.assertFalse(dgu["alternate_equivalent_seed_present"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertFalse(dgu["frame_retry_allowed"])
        self.assertFalse(dgu["same_operator_retry_allowed"])

    def test_tau_source_span_audit_keeps_variation_domain_undeclared(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["source_span_audit_attempted"])
        self.assertTrue(tau["action_object_found"])
        self.assertTrue(tau["omega_field_list_found"])
        self.assertTrue(tau["directional_varpi_variation_found"])
        self.assertFalse(tau["positive_variation_domain_declaration_found"])
        self.assertEqual(tau["selected_variation_domain_enum"], "NEGATIVE_NO_DECLARATION_SPAN")
        self.assertFalse(tau["free_over_omega1_adp_declared"])
        self.assertFalse(tau["graph_constrained_fixed_aleph_declared"])
        self.assertFalse(tau["graph_constrained_dynamic_a_declared"])
        self.assertFalse(tau["background_or_nonvariation_policy_declared"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_parent_row_remains_pre_codomain_blocked(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["acquisition_extraction_attempted"])
        self.assertTrue(kig["local_2021_draft_available"])
        self.assertFalse(kig["primary_or_source_equivalent_row_found"])
        self.assertFalse(kig["parent_slot_pre_codomain_found"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertFalse(kig["source_row_passing_firewall_allowed"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertFalse(kig["exact_gr_restart_allowed"])
        self.assertFalse(kig["theta_restart_allowed"])
        self.assertEqual(
            kig["rejection_reason_for_positive_construction"],
            "degree_P_IG_2_follows_after_operator_or_codomain_choice",
        )

    def test_product_ab_payload_absent_after_public_check(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["payload_attempted"])
        self.assertTrue(product["public_web_checked"])
        self.assertTrue(product["official_ptuj_public_locator_present"])
        self.assertFalse(product["large_media_downloaded"])
        self.assertFalse(product["one_branch_payload_present"])
        self.assertFalse(product["official_ptuj_packet_present"])
        self.assertFalse(product["lawful_local_ptuj_extractor_present"])
        self.assertFalse(product["keating_sheet_package_present"])
        self.assertEqual(product["accepted_branch_count"], 0)
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["productab_kig_restart_allowed"])

    def test_qft_receipt_retry_keeps_downstream_locked(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["receipt_attempted"])
        self.assertTrue(qft["negative_receipt_emitted"])
        self.assertFalse(qft["receipt_admitted"])
        self.assertFalse(qft["certificate_inhabited"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["local_records_unlocked"])
        self.assertFalse(qft["brsch_checks_unlocked"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
