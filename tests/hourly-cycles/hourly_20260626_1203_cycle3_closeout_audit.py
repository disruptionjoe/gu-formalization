"""Audit the 1203 cycle 3 packet specs and synthesis."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1203"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1203-cycle3-dgu-byte-acquisition-manifest.md",
    "TAU": ROOT / "explorations/hourly-20260626-1203-cycle3-tau-derivation-certificate-spec.md",
    "KIG": ROOT / "explorations/hourly-20260626-1203-cycle3-kig-candidate-packet-spec.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1203-cycle3-productab-content-access-packet.md",
    "QFT": ROOT / "explorations/hourly-20260626-1203-cycle3-qft-candidate-packet-spec.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-1203-three-cycle-fifteen-hole-synthesis.md",
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


class Cycle3CloseoutAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {name: extract_summary(path) for name, path in ARTIFACTS.items()}

    def test_cycle3_artifacts_are_run_scoped_and_non_promotional(self) -> None:
        for name in ["DGU", "TAU", "KIG", "PRODUCT_AB", "QFT"]:
            summary = self.summaries[name]
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 3)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle3-"))
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_manifest_is_defined_without_execution(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["manifest_defined"])
        self.assertTrue(dgu["manifest_applied"])
        self.assertFalse(dgu["acquisition_performed"])
        self.assertFalse(dgu["large_media_downloaded"])
        self.assertFalse(dgu["source_byte_custody_packet_present"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "UCSDDGU01LawfulLocalByteAcquisitionExecutionReceipt_V1")

    def test_tau_certificate_spec_is_uninhabited(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["certificate_spec_defined"])
        self.assertFalse(tau["certificate_inhabited"])
        self.assertFalse(tau["field_space_theorem_present"])
        self.assertFalse(tau["tangent_certificate_present"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["full_EL_tuple_present"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])

    def test_kig_candidate_packet_has_no_source_row(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["candidate_packet_schema_defined"])
        self.assertFalse(kig["candidate_packet_present"])
        self.assertFalse(kig["source_row_present"])
        self.assertFalse(kig["parent_slot_pre_codomain_found"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertEqual(kig["underlying_missing_object"], "PreCodomainParentMomentumDegreeSourceRow_V1")

    def test_productab_content_packet_is_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["custody_packet_schema_defined"])
        self.assertFalse(product["content_access_packet_present"])
        self.assertFalse(product["formula_bearing_source_object_present"])
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertFalse(product["content_bearing_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])

    def test_qft_candidate_packet_is_absent(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["candidate_packet_schema_defined"])
        self.assertFalse(qft["same_context_candidate_present"])
        self.assertFalse(qft["same_context_edge_present"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["carrier_work_allowed"])

    def test_synthesis_integrates_fifteen_holes(self) -> None:
        synthesis = self.summaries["SYNTHESIS"]
        self.assertEqual(synthesis["run_id"], RUN_ID)
        self.assertEqual(synthesis["target_quality_holes"], 15)
        self.assertEqual(synthesis["quality_holes_completed"], 15)
        self.assertEqual(synthesis["source_admissions_count"], 0)
        self.assertEqual(synthesis["claim_promotions"], 0)
        self.assertFalse(synthesis["claim_status_consistency_triggered"])
        self.assertFalse(synthesis["proof_restart_allowed_any_route"])
        self.assertFalse(synthesis["target_import_used"])
        self.assertEqual(synthesis["cycle_commits"]["cycle1"], "a7ce6ee")
        self.assertEqual(synthesis["cycle_commits"]["cycle2"], "e3b5f38")
        self.assertEqual(synthesis["cycle_commits"]["cycle3"], "pending_main_thread")
        self.assertGreaterEqual(synthesis["candidate_bank_size"], 18)
        self.assertEqual(len(synthesis["cycle3_next_frontier"]), 5)
        self.assertEqual(len(synthesis["sequential_next_lanes"]), 5)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

