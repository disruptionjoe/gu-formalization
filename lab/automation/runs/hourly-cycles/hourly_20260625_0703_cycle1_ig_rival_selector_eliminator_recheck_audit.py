#!/usr/bin/env python3
"""Audit ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab recheck."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md"
)

EXPECTED_RIVAL_IDS = {
    "exterior_derivative",
    "coderivative_trace_scalar",
    "symmetric_derivative",
    "projected_derivative",
    "lower_order_dressed_exterior",
    "displayed_shiab_codomain",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 10\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class IGRivalSelectorEliminatorRecheckAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["artifact_id"],
            "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1",
        )
        self.assertEqual(
            self.summary["owned_path"],
            "explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle1_ig_rival_selector_eliminator_recheck_audit.py",
        )

    def test_required_rival_classes_are_tracked(self) -> None:
        rivals = self.summary["rival_classes"]
        self.assertGreaterEqual(len(rivals), 4)
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVAL_IDS)
        for row in rivals:
            self.assertIn("candidate_shape", row)
            self.assertIn("eliminator_required", row)
            self.assertFalse(row["eliminator_found"], row["id"])

    def test_surviving_count_is_nonnegative_and_consistent(self) -> None:
        rivals = self.summary["rival_classes"]
        surviving = [
            row
            for row in rivals
            if row["status"] in {"survives", "hosted_candidate_not_selected"}
        ]
        self.assertEqual(self.summary["surviving_rival_count"], len(surviving))
        self.assertGreaterEqual(self.summary["surviving_rival_count"], 0)
        self.assertFalse(self.summary["selector_identity_passed"])
        self.assertGreater(self.summary["surviving_rival_count"], 0)

    def test_no_proof_restart_when_rivals_survive(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["selector_identity_passed"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertIn("proof_restart_allowed: false", self.text)
        self.assertIn("hosted_candidate_not_selected", self.text)

    def test_obstruction_and_next_frontier_are_specific(self) -> None:
        self.assertIn(
            "representation-theory/Bianchi/projection rival-eliminator",
            self.summary["first_obstruction"],
        )
        self.assertEqual(
            self.summary["missing_source_object"],
            "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
        )
        self.assertEqual(
            self.summary["next_frontier_object"],
            "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
        )
        self.assertIn("SourceForcedCodomainSelectorForK_IG", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
