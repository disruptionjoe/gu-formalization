"""Audit the 1302 cycle 2 verifier/firewall artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-1302"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-1302-cycle2-dgu-execution-receipt-admission-verifier.md",
    "TAU": ROOT / "explorations/hourly-20260626-1302-cycle2-tau-certificate-admission-verifier.md",
    "KIG": ROOT / "explorations/hourly-20260626-1302-cycle2-kig-source-row-admission-verifier.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-1302-cycle2-productab-content-access-admission-verifier.md",
    "QFT": ROOT / "explorations/hourly-20260626-1302-cycle2-qft-candidate-packet-admission-verifier.md",
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

    def test_all_verifiers_are_run_scoped_and_non_promotional(self) -> None:
        for name, summary in self.summaries.items():
            with self.subTest(name=name):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertTrue(summary["artifact_path"].startswith(f"explorations/{RUN_ID}-cycle2-"))
                self.assertTrue(summary["verifier_defined"])
                self.assertTrue(summary["verifier_applied"])
                self.assertFalse(summary["current_accepts"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_change"])

    def test_dgu_verifier_rejects_at_route_decision(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["first_failed_atom"], "route_decision")
        self.assertFalse(dgu["route_decision_present"])
        self.assertFalse(dgu["source_byte_object_present"])
        self.assertFalse(dgu["sha256_recomputable"])
        self.assertEqual(dgu["constructive_next_object"], "UCSDDGU01LawfulAcquisitionRouteDecisionReceipt_V1")

    def test_tau_verifier_rejects_at_action_field_space(self) -> None:
        tau = self.summaries["TAU"]
        self.assertEqual(tau["first_failed_atom"], "action_field_space_declaration")
        self.assertFalse(tau["action_field_space_declared"])
        self.assertFalse(tau["field_space_theorem_present"])
        self.assertFalse(tau["D_A_Phi_tau_zero_proved"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertEqual(tau["constructive_next_object"], "TauFixedAlephActionFieldSpaceDeclaration_V1")

    def test_kig_verifier_rejects_at_source_window_order_log(self) -> None:
        kig = self.summaries["KIG"]
        self.assertEqual(kig["first_failed_atom"], "source_window_order_log")
        self.assertFalse(kig["source_window_order_log_present"])
        self.assertFalse(kig["source_handle_present"])
        self.assertFalse(kig["degree_pig_2_pre_operator_found"])
        self.assertEqual(kig["first_blocking_rival"], "CODERIVATIVE_TRACE")

    def test_productab_verifier_rejects_at_content_route(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertEqual(product["first_failed_atom"], "official_content_route")
        self.assertFalse(product["official_content_route_present"])
        self.assertFalse(product["custody_basis_present"])
        self.assertFalse(product["content_bearing_asset_present"])
        self.assertFalse(product["visible_formula_transcription_allowed"])
        self.assertEqual(product["constructive_next_object"], "OfficialTzSEvmqxu48ContentRouteAndCustodyBasisReceipt_V1")

    def test_qft_verifier_rejects_at_source_anchor(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(qft["first_failed_atom"], "source_context_anchor")
        self.assertFalse(qft["source_context_anchor_present"])
        self.assertFalse(qft["source_context_locator_found"])
        self.assertFalse(qft["roles_type_over_same_context"])
        self.assertFalse(qft["carrier_work_allowed"])
        self.assertEqual(qft["constructive_next_object"], "QFTSameContextSourceAnchorTriadReceipt_V1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
