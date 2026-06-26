"""Audit the 1102 cycle 3 frontier packets and synthesis."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1102"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1102-cycle3-dgu-source-byte-custody-packet-readiness.md",
    "TAU": ROOT / "explorations/hourly-20260626-1102-cycle3-tau-reconstruction-only-branch-packet-schema.md",
    "KIG": ROOT / "explorations/hourly-20260626-1102-cycle3-kig-source-selection-boundary-certificate.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1102-cycle3-productab-official-ptuj-acquisition-request.md",
    "QFT": ROOT / "explorations/hourly-20260626-1102-cycle3-qft-firewall-crossing-witness-spec.md",
    "SYNTHESIS": ROOT / "explorations/hourly-20260626-1102-three-cycle-fifteen-hole-synthesis.md",
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
                self.assertFalse(summary.get("claim_status_consistency_triggered", False))

    def test_dgu_custody_packet_is_ready_but_absent(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["packet_readiness_defined"])
        self.assertTrue(dgu["packet_readiness_applied"])
        self.assertTrue(dgu["prior_locator_fields_reusable"])
        self.assertFalse(dgu["source_byte_custody_packet_present"])
        self.assertFalse(dgu["source_byte_path_present"])
        self.assertFalse(dgu["sha256_present"])
        self.assertFalse(dgu["lawful_basis_present"])
        self.assertFalse(dgu["extraction_policy_present"])
        self.assertFalse(dgu["producer_positive_rerun_allowed"])
        self.assertFalse(dgu["frame_retry_allowed"])
        self.assertFalse(dgu["same_operator_retry_allowed"])
        self.assertEqual(dgu["constructive_next_object"], "LawfulLocalUCSDDGU01SourceByteCustodyPacket_V1")

    def test_tau_schema_is_defined_without_ready_branch_packet(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["packet_schema_defined"])
        self.assertTrue(tau["packet_schema_applied"])
        self.assertFalse(tau["reconstruction_only_packet_ready"])
        self.assertTrue(tau["source_promotion_gate_ready"])
        self.assertFalse(tau["source_promotion_gate_satisfied"])
        self.assertFalse(tau["source_selected_branch_mode_present"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])
        self.assertIsNone(tau["ready_branch_packet"])
        self.assertEqual(tau["constructive_next_object"], "TauRecon_FixedAlephGraphPacket_V1")

    def test_kig_certificate_keeps_branch3_source_selection_locked(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["certificate_defined"])
        self.assertTrue(kig["certificate_applied"])
        self.assertFalse(kig["source_selection_candidate_present"])
        self.assertFalse(kig["source_selected_branch3_admitted"])
        self.assertFalse(kig["rival_parent_classes_closed"])
        self.assertFalse(kig["source_row_passing_firewall_allowed"])
        self.assertFalse(kig["trace_eliminator_retry_allowed"])
        self.assertFalse(kig["exact_gr_restart_allowed"])
        self.assertFalse(kig["theta_restart_allowed"])
        self.assertFalse(kig["source_extraction_retried"])
        self.assertFalse(kig["trace_exclusion_retried"])
        self.assertEqual(kig["constructive_next_object"], "PreCodomainParentMomentumDegreeSourceRow_V1")

    def test_product_ab_request_is_ready_but_source_object_absent(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["request_defined"])
        self.assertTrue(product["request_applied"])
        self.assertFalse(product["external_source_acquisition_performed"])
        self.assertTrue(product["official_ptuj_locator_present"])
        self.assertTrue(product["acquisition_request_ready"])
        self.assertFalse(product["formula_bearing_source_asset_present"])
        self.assertFalse(product["source_bytes_or_official_asset_present"])
        self.assertFalse(product["checksum_or_custody_present"])
        self.assertFalse(product["formula_visibility_scope_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertFalse(product["productab_member_emitted"])
        self.assertFalse(product["productab_kig_restart_allowed"])
        self.assertEqual(product["constructive_next_object"], "OfficialTzSEvmqxu48FormulaBearingSourceObject_V1")

    def test_qft_witness_spec_is_defined_without_positive_witness(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["witness_spec_defined"])
        self.assertTrue(qft["witness_spec_applied"])
        self.assertFalse(qft["firewall_crossing_witness_present"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["cover_vocabulary_authorized"])
        self.assertFalse(qft["admissibility_authority_found"])
        self.assertFalse(qft["same_context_edge_present"])
        self.assertFalse(qft["dependency_DAG_positive_instance_present"])
        self.assertFalse(qft["qft_cover_declaration_retry_allowed"])
        self.assertFalse(qft["local_records_unlocked"])
        self.assertFalse(qft["brsch_checks_unlocked"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["first_missing_object"], "SameContextSourceLocatorAuthorityEdge_QFT_V1")

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
        self.assertEqual(synthesis["cycle_commits"]["cycle1"], "4c94baf")
        self.assertEqual(synthesis["cycle_commits"]["cycle2"], "8059bc5")
        self.assertEqual(len(synthesis["cycle3_next_frontier"]), 5)
        self.assertEqual(len(synthesis["sequential_next_lanes"]), 5)
        self.assertTrue(synthesis["three_cycle_wrapper_improved_quality"])
        self.assertTrue(synthesis["material_next_goal_refinement"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
