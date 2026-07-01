#!/usr/bin/env python3
"""Audit the manuscript RS operator receipt candidate artifact."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0301-cycle1-manuscript-rs-operator-receipt-candidates.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. First Exact Obstruction Or Missing Proof Object",
    "## 5. Constructive Next Object",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## Candidate Rows",
    "## Machine-Readable JSON Summary",
]

REQUIRED_TERMS = {
    "Rarita",
    "Schwinger",
    "spin 3/2",
    "spin-3/2",
    "gravitino",
    "Dirac",
    "DeRham",
    "DeRahm",
    "de Rham",
    "ship in a bottle",
    "Shiab",
    "complex",
    "elliptic",
    "operator",
    "action",
    "differential",
    "Noether",
    "gauge variation",
    "gauge",
    "variation",
    "BRST",
    "Lagrangian",
    "Euler-Lagrange",
    "Euler Lagrange",
    "deformation complex",
}

REQUIRED_LOCATOR_PAGES = {41, 43, 45, 46, 47, 50, 55, 58, 62, 65}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bderives d_RS,-1\b",
    r"\bpage 46 .* is the RS gauge differential\b",
    r"\bthree generations\s+(are|is|have been|has been)\s+derived\b",
    r"\bgeneration-count result\s+(is|has been)\s+(proved|promoted|derived)\b",
    r"\belliptic deformation complex restarts the RS proof\b(?!.*Forbidden)",
    r"\bproof_restart_allowed:\s*true\b",
    r'"proof_restart_allowed"\s*:\s*true',
]


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "ManuscriptRSOperatorReceiptCandidates_V1":
            return data
    raise AssertionError("ManuscriptRSOperatorReceiptCandidates_V1 JSON not found")


class ManuscriptRSOperatorReceiptCandidatesAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_headings_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_searched_terms_are_recorded(self) -> None:
        terms = {entry["term"] for entry in self.summary["searched_terms"]}
        missing = REQUIRED_TERMS - terms
        self.assertFalse(missing, f"missing searched terms: {sorted(missing)}")

        term_pages = {entry["term"]: entry["pages"] for entry in self.summary["searched_terms"]}
        self.assertEqual(term_pages["Noether"], [])
        self.assertEqual(term_pages["BRST"], [])
        self.assertEqual(term_pages["gauge variation"], [])
        self.assertEqual(term_pages["gravitino"], [])
        self.assertIn(46, term_pages["Rarita"])
        self.assertIn(46, term_pages["operator"])
        self.assertIn(47, term_pages["DeRahm"])
        self.assertIn(65, term_pages["DeRham"])

    def test_candidate_rows_have_page_locators_and_zero_acceptance(self) -> None:
        rows = self.summary["candidate_rows"]
        self.assertEqual(len(rows), 10)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_receipts"], [])

        seen_pages: set[int] = set()
        for row in rows:
            self.assertFalse(row["accepted"], f"unexpected accepted row: {row}")
            self.assertRegex(row["locator"], r"PDF p\.\d+")
            match = re.search(r"PDF p\.(\d+)", row["locator"])
            self.assertIsNotNone(match)
            seen_pages.add(int(match.group(1)))
            self.assertIn("acceptance_status", row)
            self.assertIn("first_blocker", row)

        self.assertEqual(seen_pages, REQUIRED_LOCATOR_PAGES)

    def test_strongest_positive_result_is_quarantined_not_accepted(self) -> None:
        strongest = self.summary["strongest_positive_result"]
        self.assertEqual(strongest["row_id"], "MSRS-04")
        self.assertIn("PDF p.46", strongest["locator"])
        self.assertIn("not accepted RS receipt", strongest["status"])

        row = next(row for row in self.summary["candidate_rows"] if row["row_id"] == "MSRS-04")
        self.assertEqual(row["acceptance_status"], "quarantined_strong_adjacent_context")
        self.assertFalse(row["accepted"])

    def test_restart_blocked_unless_accepted_candidate_exists(self) -> None:
        accepted = [row for row in self.summary["candidate_rows"] if row["accepted"]]
        if accepted:
            statuses = {row["acceptance_status"] for row in accepted}
            self.assertIn("accepted_for_routing", statuses)
        else:
            self.assertFalse(self.summary["proof_restart_allowed"])
            self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_first_obstruction_is_rs_gauge_differential(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source_emitted_RS_gauge_differential")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("Noether identity", obstruction["description"])
        self.assertIn("BRST rule", obstruction["description"])
        self.assertIn("d_RS,-1", obstruction["description"])

    def test_no_generation_count_or_rs_claim_promotion(self) -> None:
        self.assertFalse(self.summary["generation_count_promotion_allowed"])
        impact = self.summary["claim_impact"]
        self.assertFalse(impact["GU_RS_branch_falsified"])
        self.assertEqual(impact["current_status"], "source-origin blocked")
        self.assertIn("generation_count_proved", impact["forbidden_promotions"])
        self.assertIn("page_46_operator_is_RS_gauge_differential", impact["forbidden_promotions"])

        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                msg=f"forbidden promotion pattern present: {pattern}",
            )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            ManuscriptRSOperatorReceiptCandidatesAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
