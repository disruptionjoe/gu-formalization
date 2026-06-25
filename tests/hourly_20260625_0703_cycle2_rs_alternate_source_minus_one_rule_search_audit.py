#!/usr/bin/env python3
"""Audit AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle2-rs-alternate-source-minus-one-rule-search.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise AssertionError("missing JSON Summary fenced block")
    return json.loads(match.group(1))


class AlternatePrimarySourceSearchAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_fields(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["artifact_id"],
            "AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle2_rs_alternate_source_minus_one_rule_search_audit.py",
        )

    def test_at_least_four_searched_surfaces_or_unavailability_rows(self) -> None:
        surfaces = self.summary["searched_surfaces"]
        self.assertGreaterEqual(len(surfaces), 4)
        decisions = {surface["decision"] for surface in surfaces}
        self.assertIn("REJECT_REPRESENTATION_FIELD_CONTENT_ONLY", decisions)
        self.assertIn("NO_EXACT_NOTATION_HIT", decisions)
        self.assertIn("UNAVAILABLE_FOR_ACCEPTED_RECEIPT_THIS_PASS", decisions)

    def test_no_accepted_receipt_no_proof_restart(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["source_emitted_rs_minus_one_rule_found"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        lowered = self.text.lower()
        self.assertNotIn('"proof_restart_allowed": true', lowered)
        self.assertNotIn('"accepted_receipt_count": 1', lowered)
        self.assertIn("with accepted receipt count `0`", lowered)
        self.assertIn("there is no honest rs proof restart", lowered)

    def test_global_rs_no_go_not_promoted(self) -> None:
        self.assertFalse(self.summary["global_rs_no_go_promoted"])
        self.assertIn("global\nRS no-go not promoted", self.text)
        self.assertIn("A global no-go would require complete source", self.text)

    def test_first_obstruction_names_missing_source_rule_fields(self) -> None:
        obstruction = self.summary["first_obstruction"]
        for needle in ["d_RS,-1", "source", "target", "minus-one", "rule kind"]:
            self.assertIn(needle, obstruction)
        self.assertIn("SourceEmittedRSMinusOneRule_V1", self.text)

    def test_strongest_positive_is_not_promoted(self) -> None:
        self.assertIn("Oxford/Portal", self.text)
        self.assertIn("Rarita-Schwinger", self.text)
        self.assertIn("REJECT_REPRESENTATION_FIELD_CONTENT_ONLY", self.text)
        self.assertNotIn("ACCEPT_SOURCE_ACTION_NOETHER_RECEIPT", self.text)
        self.assertNotIn("ACCEPT_SOURCE_EMITTED_RS_MINUS_ONE_RULE", self.text)

    def test_json_parses_and_next_frontier_is_specific(self) -> None:
        self.assertEqual(
            self.summary["next_frontier_object"],
            "TimestampedTranscriptAcquisitionForModernRSSurfaces_V1",
        )
        json.dumps(self.summary, sort_keys=True)


if __name__ == "__main__":
    unittest.main()
