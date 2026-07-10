#!/usr/bin/env python3
"""Audit the Mission A generation-count analytic machinery artifact.

This audit is not a proof of the RS index. It checks that the artifact names
the missing physical analytic object, keeps K3 as control-only until transport
closes, includes the target-input rollback guard, and does not claim that three
generations have been derived.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "mission-a-generation-count-analytic-machinery-2026-06-24.md"


REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. If GU Is Correct, What Generation-Count Analytic Object Must Exist",
    "## 3. Non-Circular Reconstruction Attempt",
    "## 4. Genuine Pieces Versus Fitted Or Control-Only Pieces",
    "## 5. First Exact Obstruction Or Missing Proof Object",
    "## 6. Constructive Next Computation",
    "## 7. Claim Certificate Table And Machine-Readable Summary",
]


REQUIRED_TERMS = [
    "RS_GU^phys",
    "non-circular",
    "H-linear",
    "Fredholm",
    "APS",
    "Y^14 -> K3",
    "loss ledger",
    "target_input_rollback",
    "INVALID_CIRCULAR",
    "K3_CONTROL_ONLY",
    "physical_DOF_count_as_index",
]


FORBIDDEN_DERIVATION_PATTERNS = [
    r"\bthree generations\s+(is|are)\s+derived\b",
    r"\bgeneration count\s+(is|has been)\s+derived\b",
    r"\bind_H\(D_RS\)\s*=\s*8\s+is\s+proved\b",
]


def artifact_text() -> str:
    return ARTIFACT.read_text(encoding="utf-8")


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "MISSION_A_GENERATION_COUNT_ANALYTIC_MACHINERY":
            return data
    raise AssertionError("machine-readable Mission A summary JSON block not found")


class MissionAGenerationCountAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = artifact_text()
        cls.summary = extract_summary(cls.text)

    def test_required_deliverable_headings_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_guard_and_bridge_terms_are_present(self) -> None:
        for term in REQUIRED_TERMS:
            self.assertIn(term, self.text)

    def test_machine_summary_blocks_promotion_and_generation_claim(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_OPEN_FIRST_COMPUTABLE_OBJECT_IDENTIFIED",
        )
        self.assertFalse(self.summary["three_generations_derived"])
        self.assertEqual(self.summary["generation_count_claim_status"], "NOT_DERIVED")
        self.assertFalse(self.summary["promotion_allowed_now"])
        self.assertEqual(
            self.summary["current_decision"],
            "OPEN_MISSING_RS_GU_PHYS_AND_BRIDGE_CERTIFICATE",
        )

    def test_first_computable_object_is_specified_not_claimed_computed(self) -> None:
        obj = self.summary["first_computable_object"]
        self.assertEqual(obj["id"], "RS_GU_PHYS_SYMBOL_BRIDGE_CERTIFICATE")
        self.assertEqual(obj["status"], "SPECIFIED_NOT_COMPUTED")
        self.assertIn("physical_symbol_class", obj["would_decide"])
        self.assertIn("Y14_to_K3_transport_validity", obj["would_decide"])

    def test_required_objects_cover_rank_fredholm_aps_and_transport(self) -> None:
        required_objects = set(self.summary["required_objects"])
        expected = {
            "RS_GU^phys",
            "non_circular_rank_or_index",
            "H_linear_Fredholm_family",
            "APS_or_unitary_bridge",
            "Y14_to_K3_transport_loss_ledger",
            "target_input_rollback",
        }
        self.assertTrue(expected.issubset(required_objects))

    def test_target_inputs_are_rejected(self) -> None:
        rejected = set(self.summary["rejected_inputs"])
        expected = {
            "ind_H(D_RS)=8",
            "rank_eff=4",
            "ind_H(D_GU)=24",
            "three_generations",
            "physical_DOF_count_as_index",
            "normalization_chosen_after_target",
        }
        self.assertTrue(expected.issubset(rejected))
        self.assertEqual(
            self.summary["branch_decision_rule"]["target_input_seen"],
            "INVALID_CIRCULAR",
        )

    def test_k3_is_control_only_until_bridge_closes(self) -> None:
        control = set(self.summary["control_only_or_underdefined"])
        self.assertIn("raw_compact_K3_as_physical_GU_index", control)
        self.assertIn("same_operator_Y14_to_K3_bridge", control)
        self.assertEqual(
            self.summary["branch_decision_rule"]["bridge_missing"],
            "K3_CONTROL_ONLY_OR_UNDERDEFINED",
        )

    def test_no_positive_three_generation_claim_is_made(self) -> None:
        for pattern in FORBIDDEN_DERIVATION_PATTERNS:
            self.assertIsNone(re.search(pattern, self.text, re.IGNORECASE))
        self.assertIn("three generations: not derived", self.text)
        self.assertIn("generation count: not derived", self.text)


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(MissionAGenerationCountAuditTests)
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
