"""Audit PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / "hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md"

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT = "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1"
EXPECTED_PATH = "explorations/hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md"
EXPECTED_BRANCHES = {
    "official_custodian_formula_source_asset",
    "lawful_local_byte_toolchain_output_manifest",
}


def load_text() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing PTUJ nonconflation artifact: {DOC}") from exc


def extract_json_summary(text: str) -> dict:
    blocks = re.findall(r"```json\n(.*?)\n```", text, re.DOTALL)
    if not blocks:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(blocks[-1])


class PTUJSingleBranchNonconflationGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = load_text()
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_artifact_path(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["owned_path"], EXPECTED_PATH)
        self.assertEqual(self.summary["gate"], "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE")

    def test_exactly_two_branch_candidates(self) -> None:
        candidates = self.summary["branch_candidates"]
        self.assertEqual(self.summary["branch_candidate_count"], 2)
        self.assertEqual(len(candidates), 2)
        self.assertEqual({candidate["row_id"] for candidate in candidates}, EXPECTED_BRANCHES)
        self.assertTrue(all(candidate["accepted"] is False for candidate in candidates))

    def test_nonconflation_and_metadata_receipt_flags_are_false(self) -> None:
        self.assertFalse(self.summary["cross_branch_conflation_allowed"])
        self.assertFalse(self.summary["branch_conflation_allowed"])
        self.assertFalse(self.summary["metadata_as_receipt_allowed"])
        self.assertFalse(self.summary["metadata_as_receipt_promotion"])
        self.assertFalse(self.summary["metadata_or_locator_continuity_as_receipt_allowed"])
        self.assertFalse(self.summary["locator_continuity_as_receipt_allowed"])
        self.assertFalse(self.summary["schema_as_receipt_allowed"])

    def test_no_acceptance_and_no_downstream_visibility(self) -> None:
        self.assertEqual(self.summary["accepted_branch_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["formula_visibility_allowed"])
        self.assertFalse(self.summary["keating_comparison_allowed"])
        self.assertFalse(self.summary["ig_selector_route_allowed"])

    def test_mixed_construction_is_rejected(self) -> None:
        mixed = self.summary["attempted_mixed_construction"]
        self.assertFalse(mixed["accepted"])
        self.assertEqual(mixed["rejection_reason"], "cross_branch_assembly_is_not_a_receipt")
        self.assertIn("locator_continuity", mixed["official_partial_fields"])
        self.assertIn("receipt_schema", mixed["lawful_local_partial_fields"])

    def test_next_object_is_single_complete_branch_receipt(self) -> None:
        next_object = self.summary["next_object"]
        self.assertEqual(next_object["id"], "SingleCompletePTUJBranchReceipt_V1")
        self.assertTrue(next_object["is_single_complete_branch_receipt"])
        self.assertEqual(next_object["accepted_branch_count_required"], 1)
        self.assertEqual(next_object["accepted_receipt_count_required"], 1)
        self.assertEqual(len(next_object["allowed_instantiations"]), 2)
        self.assertEqual(next_object["forbidden_instantiation"], "mixed_official_metadata_plus_lawful_local_schema")
        self.assertIn("cross_branch_assembly", next_object["must_not_use"])
        self.assertIn("metadata_as_receipt", next_object["must_not_use"])

    def test_block_falsification_requires_one_complete_branch(self) -> None:
        falsifier = self.summary["falsifies_block_if"]
        self.assertEqual(falsifier["object_id"], "SingleCompletePTUJBranchReceipt_V1")
        self.assertEqual(falsifier["accepted_branch_count"], 1)
        self.assertEqual(falsifier["accepted_receipt_count"], 1)
        self.assertTrue(falsifier["all_required_fields_for_one_branch_present"])
        self.assertTrue(falsifier["all_accepted_fields_belong_to_same_branch"])
        self.assertFalse(falsifier["target_import_used"])
        self.assertFalse(falsifier["metadata_as_receipt_allowed"])
        self.assertFalse(falsifier["cross_branch_conflation_allowed"])


if __name__ == "__main__":
    unittest.main()
