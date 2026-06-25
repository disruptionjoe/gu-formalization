"""Audit the author-manuscript QFT finite-projector locator-row artifact."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "explorations" / (
    "hourly-20260625-0601-cycle1-author-manuscript-qft-finite-projector-locator-row.md"
)


def load_summary() -> tuple[str, dict]:
    text = DOC.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        re.DOTALL,
    )
    if not match:
        raise AssertionError("machine-readable JSON summary not found")
    return text, json.loads(match.group(1))


class AuthorManuscriptQFTFiniteProjectorLocatorRowAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text, cls.summary = load_summary()

    def test_core_invariant_strings_are_present(self) -> None:
        required = [
            "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1",
            "P_fin^b",
            "F_phys^b(O)",
            "K_b",
            "scoped negative not global no-go",
            "accepted_receipt_count: 0",
            "proof_restart_allowed: false",
            "no proof restart",
        ]
        for needle in required:
            self.assertIn(needle, self.text)

    def test_summary_keeps_negative_scoped_and_restart_blocked(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "AuthorManuscriptQFTFiniteProjectorLocatorRow_V1",
        )
        self.assertEqual(
            self.summary["required_object"],
            "P_fin^b: F_phys^b(O) -> K_b",
        )
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertTrue(self.summary["negative_result_scoped"])
        self.assertFalse(self.summary["global_no_go_allowed"])
        self.assertFalse(self.summary["global_demotion_allowed"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertTrue(self.summary["no_proof_restart"])

    def test_all_page_window_locator_rows_are_rejected(self) -> None:
        rows = self.summary["locator_rows"]
        self.assertGreaterEqual(len(rows), 5)
        for row in rows:
            self.assertEqual(row["receipt_decision"], "rejected", row["locator"])
            self.assertIn("rejection_reason", row)


if __name__ == "__main__":
    unittest.main()
