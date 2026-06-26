"""Audit the 0701 cycle 1 source-intake artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0701"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0701-cycle1-positive-primary-source-dgu-row-candidate.md",
    "TAU": ROOT / "explorations/hourly-20260626-0701-cycle1-tau-reference-graph-source-lock-candidate.md",
    "KIG": ROOT / "explorations/hourly-20260626-0701-cycle1-kig-exterior-singleton-survival-certificate.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0701-cycle1-product-ab-recovered-member-candidate.md",
    "QFT": ROOT / "explorations/hourly-20260626-0701-cycle1-qft-category-identity-composition-laws.md",
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


class Cycle1SourceIntakeAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_positive_row_is_not_admitted(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertEqual(dgu["verdict_class"], "blocked_positive_candidate_not_admitted")
        self.assertFalse(dgu["row_candidate_admitted"])
        self.assertIn("sector_rule_id_for_actual_D_GU_epsilon_0_1", dgu["first_failed_fields"])
        self.assertIn("family_identity_evidence_to_actual_D_GU_epsilon_0_1", dgu["first_failed_fields"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_tau_graph_lock_remains_reference_only(self) -> None:
        tau = self.summaries["TAU"]
        self.assertFalse(tau["tau_graph_lock_admitted"])
        self.assertEqual(tau["current_decision"], "TAU_REFERENCE_ONLY_EQUIVARIANCE")
        self.assertFalse(tau["branch2a_admitted"])
        self.assertFalse(tau["branch2b_admitted"])
        self.assertFalse(tau["exact_gr_restart_allowed"])
        self.assertFalse(tau["theta_restart_allowed"])
        self.assertEqual(tau["first_failed_field"], "source_locked_graph_for_admissible_IG_fields")

    def test_kig_singleton_certificate_rejects_multiple_survivors(self) -> None:
        kig = self.summaries["KIG"]
        self.assertFalse(kig["singleton_survivor"])
        self.assertEqual(kig["surviving_class_count"], len(kig["surviving_classes"]))
        self.assertGreaterEqual(kig["surviving_class_count"], 5)
        self.assertTrue(kig["d_a_u_admissible"])
        self.assertFalse(kig["d_a_u_source_forced"])
        self.assertFalse(kig["branch3_admitted"])
        self.assertEqual(kig["first_exact_missing_eliminator"], "CoderivativeTraceEliminatorForK_IG")

    def test_product_ab_recovered_member_is_not_admitted(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertFalse(product["operator_member_admitted"])
        self.assertFalse(product["locator_receipt_admitted"])
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])
        self.assertFalse(product["kig_restart_allowed"])
        self.assertFalse(product["negative_is_global_no_go"])
        self.assertEqual(product["first_failed_field_after_generic_source_shell"], "operator_member_id")

    def test_qft_category_laws_are_conditional_not_carrier_unlocking(self) -> None:
        qft = self.summaries["QFT"]
        self.assertEqual(
            qft["verdict_class"],
            "conditional_missing_morphism_typing_equality_no_source_action_or_cocycle",
        )
        self.assertFalse(qft["category_laws_defined"])
        self.assertFalse(qft["identity_law_defined"])
        self.assertFalse(qft["composition_law_defined"])
        self.assertEqual(qft["first_missing_law"], "QFTBranchRecordMorphismTypingEqualityLaw_V1")
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["cocycle_defined"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
