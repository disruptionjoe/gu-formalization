"""Audit the 1102 cycle 2 verifier/firewall artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1102"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1102-cycle2-dgu-lawful-source-byte-seed-verifier.md",
    "TAU": ROOT / "explorations/hourly-20260626-1102-cycle2-tau-no-declaration-branch-mode-firewall.md",
    "KIG": ROOT / "explorations/hourly-20260626-1102-cycle2-kig-reconstruction-only-parent-action-boundary.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1102-cycle2-productab-official-ptuj-packet-verifier.md",
    "QFT": ROOT / "explorations/hourly-20260626-1102-cycle2-qft-host-schema-authority-firewall.md",
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


class Cycle2VerifierFirewallsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_all_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_lawful_local_seed_verifier_rejects_current_state(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["verifier_defined"])
        self.assertTrue(dgu["verifier_applied"])
        self.assertTrue(dgu["source_locator_present"])
        self.assertTrue(dgu["transcript_window_tie_present"])
        self.assertFalse(dgu["lawful_local_source_byte_seed_present"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["lawful_basis_present"])
        self.assertFalse(dgu["custody_record_present"])
        self.assertFalse(dgu["extraction_policy_present"])
        self.assertFalse(dgu["branch_pure_seed_present"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertFalse(dgu["frame_retry_allowed"])
        self.assertFalse(dgu["same_operator_retry_allowed"])

    def test_tau_no_declaration_firewall_preserves_reconstruction_only_modes(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["firewall_defined"])
        self.assertTrue(tau["firewall_applied"])
        self.assertFalse(tau["source_selected_branch_mode_present"])
        self.assertTrue(tau["reconstruction_only_modes_allowed"])
        self.assertFalse(tau["free_beta_branch_admitted"])
        self.assertFalse(tau["fixed_aleph_graph_admitted"])
        self.assertFalse(tau["dynamic_a_graph_admitted"])
        self.assertFalse(tau["background_policy_admitted"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_boundary_allows_template_but_bars_source_selected_branch3(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["boundary_defined"])
        self.assertTrue(kig["boundary_applied"])
        self.assertTrue(kig["reconstruction_only_template_allowed"])
        self.assertTrue(kig["rival_parents_survive"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertFalse(kig["source_row_passing_firewall_allowed"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertFalse(kig["exact_gr_restart_allowed"])
        self.assertFalse(kig["theta_restart_allowed"])
        self.assertFalse(kig["source_extraction_retried"])
        self.assertFalse(kig["trace_exclusion_retried"])

    def test_product_ab_official_ptuj_verifier_stops_at_source_asset(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["verifier_defined"])
        self.assertTrue(product["verifier_applied"])
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertFalse(product["official_ptuj_packet_present"])
        self.assertFalse(product["formula_bearing_source_asset_present"])
        self.assertFalse(product["source_bytes_or_official_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["productab_kig_restart_allowed"])
        self.assertEqual(
            product["first_failed_field"],
            "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes",
        )

    def test_qft_host_schema_firewall_blocks_authority_substitution(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["firewall_defined"])
        self.assertTrue(qft["firewall_applied"])
        self.assertTrue(qft["host_infrastructure_present"])
        self.assertTrue(qft["schema_verifier_infrastructure_present"])
        self.assertFalse(qft["generic_host_as_locator_allowed"])
        self.assertFalse(qft["schema_as_cover_authority_allowed"])
        self.assertFalse(qft["brsch_as_cover_generator_allowed"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["local_records_unlocked"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
