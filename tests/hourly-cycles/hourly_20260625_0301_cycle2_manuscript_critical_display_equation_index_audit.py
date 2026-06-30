#!/usr/bin/env python3
"""Audit the Cycle 2 manuscript critical display-equation index."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle2-manuscript-critical-display-equation-index.md"
)

REQUIRED_WINDOWS = [(32, 48), (55, 58), (62, 66)]
REQUIRED_PAGES = (
    set(range(32, 49))
    | set(range(55, 59))
    | set(range(62, 67))
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## Critical Display/Object Index",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_FAMILIES = {"IG", "RS", "DGU_VZ", "QFT"}
REQUIRED_TRANSCRIPTION_PAGES = {43, 44, 46, 47, 48, 55, 57, 58, 62, 66}
FORBIDDEN_POSITIVE_PATTERNS = [
    r"\bIG selector is accepted\b",
    r"\bRS differential d_RS,-1 is emitted\b",
    r"\bD_GU\^epsilon 0/1 operator/action/EL receipt is accepted\b",
    r"\bQFT finite projector receipt is present\b",
    r"\bproof restart is allowed\b",
    r'"accepted_receipt_count"\s*:\s*[1-9]',
    r'"family_receipt_promoted"\s*:\s*true',
    r'"proof_restart_allowed"\s*:\s*true',
    r'"text_extraction_alone_adequate_for_family_identity_gates"\s*:\s*true',
]


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ManuscriptCriticalDisplayEquationIndexAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_required_page_windows_are_exactly_indexed(self) -> None:
        self.assertEqual(
            [tuple(window) for window in self.summary["required_page_windows"]],
            REQUIRED_WINDOWS,
        )
        indexed_pages = set(self.summary["indexed_pages"])
        self.assertEqual(indexed_pages, REQUIRED_PAGES)

        row_pages = {row["page"] for row in self.summary["index_rows"]}
        self.assertEqual(row_pages, REQUIRED_PAGES)
        self.assertEqual(len(self.summary["index_rows"]), len(REQUIRED_PAGES))

    def test_each_index_row_has_required_display_fields(self) -> None:
        required_fields = {
            "page",
            "labels",
            "families",
            "object_role",
            "family_relevance",
            "extraction_confidence",
            "identity_sufficient",
            "requires_rendered_or_manual_transcription",
        }
        for row in self.summary["index_rows"]:
            self.assertTrue(required_fields <= set(row), row)
            self.assertIn(row["extraction_confidence"], {"high", "medium", "low"}, row)
            self.assertIs(row["identity_sufficient"], False, row)
            self.assertIsInstance(row["requires_rendered_or_manual_transcription"], bool)
            self.assertTrue(row["labels"], row)
            self.assertTrue(row["families"], row)

    def test_family_gate_assessments_cover_all_receipt_families(self) -> None:
        gates = self.summary["family_gate_assessment"]
        self.assertEqual(set(gates), REQUIRED_FAMILIES)
        for family, assessment in gates.items():
            self.assertFalse(assessment["identity_closed_by_text_extraction"], family)
            self.assertIn("not_identity", assessment["source_index_adequacy"], family)
            self.assertTrue(assessment["critical_pages"], family)

        self.assertIn("SourceForcedCodomainSelectorForK_IG", gates["IG"]["gate"])
        self.assertIn("d_RS,-1", gates["RS"]["gate"])
        self.assertIn("D_GU^epsilon", gates["DGU_VZ"]["gate"])
        self.assertIn("finite projector", gates["QFT"]["gate"])

    def test_text_extraction_is_not_promoted_to_receipt_identity(self) -> None:
        self.assertFalse(
            self.summary["text_extraction_alone_adequate_for_family_identity_gates"]
        )
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertFalse(self.summary["family_receipt_promoted"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])

    def test_rendered_manual_transcription_requirement_is_explicit(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "RenderedCriticalDisplayTranscriptionPacket_V1")
        self.assertEqual(obstruction["status"], "missing")

        queue_pages = {entry["page"] for entry in self.summary["critical_transcription_queue"]}
        self.assertEqual(queue_pages, REQUIRED_TRANSCRIPTION_PAGES)

        rows = {row["page"]: row for row in self.summary["index_rows"]}
        for page in REQUIRED_TRANSCRIPTION_PAGES:
            self.assertTrue(
                rows[page]["requires_rendered_or_manual_transcription"],
                f"page {page} should require rendered/manual transcription",
            )

    def test_first_family_specific_missing_object_is_ig_selector(self) -> None:
        missing = self.summary["first_family_specific_missing_extraction_object"]
        self.assertEqual(missing["family"], "IG")
        self.assertIn("K_IG", missing["id"])
        self.assertEqual(missing["status"], "missing")
        self.assertIn("PDF pp. 42-43", missing["locator"])

    def test_forbidden_promotions_are_false_and_not_claimed(self) -> None:
        for key, value in self.summary["forbidden_promotions"].items():
            self.assertIs(value, False, key)

        for pattern in FORBIDDEN_POSITIVE_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden positive promotion matched: {pattern}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
