"""Audit the SM gauge/Higgs finite-control extraction ledger.

This is intentionally a structural audit, not a mathematical proof. It checks that
the ledger keeps the required categories explicit and does not leave proof-object
cells blank.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER = (
    REPO_ROOT
    / "explorations"
    / "sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
)

ALLOWED_STATUSES = {"derive", "host", "import", "open", "fail"}

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Extraction Ledger Table",
    "## 3. First Genuine Derivation Failure",
    "## 4. Higgs-Specific Conclusion",
    "## 5. Anomaly Compatibility Conclusion",
    "## 6. What This Means For Standard Model Emergence Claims",
    "## 7. Next Meaningful Proof/Computation Step",
]

REQUIRED_DATUM_PATTERNS = [
    r"SM gauge quotient",
    r"Hypercharge normalization",
    r"One-generation Pati-Salam packet",
    r"One-generation SM charge packet",
    r"Ambient Higgs bidoublet",
    r"Physical Higgs scalar",
    r"Freed-Hopkins/anomaly compatibility",
]


def read_ledger() -> str:
    try:
        return LEDGER.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"Ledger file is missing: {LEDGER}") from exc


def parse_ledger_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells == ["datum", "status", "reason", "missing proof object"]:
            continue
        if len(cells) != 4:
            continue
        rows.append(
            {
                "datum": cells[0],
                "status": cells[1],
                "reason": cells[2],
                "missing": cells[3],
            }
        )
    return rows


class FiniteControlLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_ledger()
        cls.rows = parse_ledger_rows(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_ledger_rows_use_allowed_statuses(self) -> None:
        self.assertGreaterEqual(len(self.rows), 10)
        for row in self.rows:
            self.assertIn(row["status"], ALLOWED_STATUSES, row)

    def test_required_data_are_covered(self) -> None:
        row_text = "\n".join(row["datum"] for row in self.rows)
        for pattern in REQUIRED_DATUM_PATTERNS:
            self.assertRegex(row_text, pattern)

    def test_missing_proof_objects_are_named(self) -> None:
        vague = re.compile(r"^(none|n/a|tbd|open)$", re.IGNORECASE)
        for row in self.rows:
            self.assertTrue(row["missing"], row)
            if row["status"] != "derive":
                self.assertIsNone(vague.match(row["missing"]), row)

    def test_first_failure_is_gauge_selection_not_higgs(self) -> None:
        failure_section = self.text.split("## 3. First Genuine Derivation Failure", 1)[1]
        failure_section = failure_section.split("## 4. Higgs-Specific Conclusion", 1)[0]
        self.assertIn("SU(3) x SU(2) x U(1) / Z_6", failure_section)
        self.assertIn("A_F = C + H + M_3(C)", failure_section)
        self.assertIn("selector", failure_section.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
