"""Audit the 0604 cycle 2 admission-predicate artifacts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260626-0604"
ARTIFACTS = {
    "DGU": ROOT / "explorations/hourly-20260626-0604-cycle2-dgu-primary-row-admission-predicate.md",
    "TAU": ROOT / "explorations/hourly-20260626-0604-cycle2-tau-slice-lock-decision-table.md",
    "KIG": ROOT / "explorations/hourly-20260626-0604-cycle2-kig-rival-class-eliminator-preorder.md",
    "PRODUCT_AB": ROOT / "explorations/hourly-20260626-0604-cycle2-product-ab-negative-coverage-bundle.md",
    "QFT": ROOT / "explorations/hourly-20260626-0604-cycle2-qft-branch-record-primitive-schema.md",
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


class Cycle2AdmissionPredicatesAudit(unittest.TestCase):
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
                self.assertFalse(summary["claim_status_consistency_triggered"])

    def test_dgu_predicate_defined_without_admitting_row(self) -> None:
        dgu = self.summaries["DGU"]
        self.assertTrue(dgu["predicate_defined"])
        self.assertFalse(dgu["row_admitted_by_predicate"])
        self.assertGreaterEqual(dgu["minimum_required_fields_count"], 10)
        self.assertFalse(dgu["same_operator_witness_allowed"])
        self.assertFalse(dgu["proof_restart_allowed"])

    def test_tau_table_preserves_reference_only_decision(self) -> None:
        tau = self.summaries["TAU"]
        self.assertTrue(tau["decision_table_defined"])
        self.assertEqual(tau["current_decision"], "TAU_REFERENCE_ONLY_EQUIVARIANCE")
        self.assertFalse(tau["branch2a_admitted"])
        self.assertFalse(tau["branch2b_admitted"])
        self.assertTrue(tau["branch3_fallback_required_if_no_future_slice"])
        self.assertFalse(tau["exact_gr_restart_allowed"])

    def test_kig_preorder_has_multiple_survivors(self) -> None:
        kig = self.summaries["KIG"]
        self.assertTrue(kig["preorder_defined"])
        self.assertFalse(kig["singleton_survivor"])
        self.assertEqual(kig["surviving_class_count"], len(kig["surviving_classes"]))
        self.assertGreaterEqual(kig["surviving_class_count"], 5)
        self.assertTrue(kig["d_a_u_still_strongest_candidate"])
        self.assertFalse(kig["d_a_u_source_forced"])

    def test_product_ab_negative_is_scoped_not_global(self) -> None:
        product = self.summaries["PRODUCT_AB"]
        self.assertTrue(product["negative_coverage_bundle_defined"])
        self.assertFalse(product["operator_member_admitted"])
        self.assertFalse(product["negative_is_global_no_go"])
        self.assertGreaterEqual(product["surfaces_accounted_count"], 4)
        self.assertFalse(product["binding_gate_allowed"])
        self.assertFalse(product["alpha_beta_identity_allowed"])

    def test_qft_primitive_schema_does_not_unlock_carrier(self) -> None:
        qft = self.summaries["QFT"]
        self.assertTrue(qft["primitive_schema_defined"])
        self.assertFalse(qft["category_defined"])
        self.assertFalse(qft["source_action_defined"])
        self.assertFalse(qft["cocycle_defined"])
        self.assertFalse(qft["hidden_branch_key_emitted"])
        self.assertFalse(qft["carrier_work_allowed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
