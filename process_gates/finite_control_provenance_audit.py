"""Audit the finite-control provenance ledger.

This is a structural provenance audit, not a mathematical proof. It checks that
the ledger names allowed and forbidden inputs, uses the declared status
vocabulary, keeps why-provenance nonblank, and does not mark target data as
derived when the document says they are imported or selector-failed.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = REPO_ROOT / "explorations" / "cycle-gates-and-audits" / "finite-control-provenance-audit-2026-06-24.md"

ALLOWED_STATUSES = {"derived", "hosted", "imported", "failed", "open"}

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Allowed Inputs And Forbidden Target Inputs",
    "## 3. Provenance Ledger Table",
    "## 4. First Genuine Forbidden-Input Or Selector Failure",
    "## 5. Claim Certificate Table For TYPEII1-SELECTOR, SM-GAUGE, HIGGS, ANOMALY",
    "## 6. Branch/Selector Robustness Table",
    "## 7. Next Meaningful Proof/Computation Step",
]

FORBIDDEN_INPUT_PATTERNS = [
    r"A_F = C \+ H \+ M_3\(C\)",
    r"G_SM = SU\(3\) x SU\(2\) x U\(1\) / Z_6",
    r"central quotient `Z_6`",
    r"`n = 3`",
    r"`K_SM`",
    r"physical Higgs doublet",
    r"ordinary anomaly-free SM shadow",
]

REQUIRED_DATUM_PATTERNS = [
    r"Finite Connes algebra",
    r"SM gauge group",
    r"Central quotient",
    r"Hypercharge",
    r"One-generation Pati-Salam packet",
    r"Exactly three Type II_1 generation sectors",
    r"SM Higgs doublet quantum-number slot",
    r"Physical Higgs scalar",
    r"Higgs potential",
    r"Full GU/Type II_1 anomaly shadow",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing provenance audit: {DOC}") from exc


def parse_provenance_rows(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells == [
            "datum",
            "status",
            "introduced-by operation",
            "why-provenance",
            "missing proof object",
        ]:
            continue
        if len(cells) != 5:
            continue
        if cells[1] not in ALLOWED_STATUSES:
            continue
        rows.append(
            {
                "datum": cells[0],
                "status": cells[1],
                "operation": cells[2],
                "why": cells[3],
                "missing": cells[4],
            }
        )
    return rows


class FiniteControlProvenanceAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.rows = parse_provenance_rows(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_forbidden_target_inputs_are_explicit(self) -> None:
        forbidden_section = self.text.split("### Forbidden Target Inputs", 1)[1]
        forbidden_section = forbidden_section.split("## 3. Provenance Ledger Table", 1)[0]
        for pattern in FORBIDDEN_INPUT_PATTERNS:
            self.assertRegex(forbidden_section, pattern)

    def test_provenance_rows_use_allowed_statuses_and_nonblank_why(self) -> None:
        self.assertGreaterEqual(len(self.rows), 14)
        vague = re.compile(r"^(none|n/a|tbd|open)$", re.IGNORECASE)
        for row in self.rows:
            self.assertIn(row["status"], ALLOWED_STATUSES, row)
            self.assertTrue(row["operation"], row)
            self.assertTrue(row["why"], row)
            self.assertTrue(row["missing"], row)
            self.assertIsNone(vague.match(row["why"]), row)
            self.assertIsNone(vague.match(row["missing"]), row)

    def test_required_data_are_covered(self) -> None:
        row_text = "\n".join(f"{row['datum']} {row['why']}" for row in self.rows)
        for pattern in REQUIRED_DATUM_PATTERNS:
            self.assertRegex(row_text, pattern)

    def test_high_risk_targets_are_not_marked_derived(self) -> None:
        row_by_datum = {row["datum"]: row for row in self.rows}
        checks = {
            "Finite Connes algebra `A_F = C + H + M_3(C)`": {"imported"},
            "SM gauge group `SU(3) x SU(2) x U(1) / Z_6`": {"failed"},
            "Central quotient `Z_6`": {"failed"},
            "Exactly three Type II_1 generation sectors `n = 3`": {"failed"},
            "SM Higgs doublet quantum-number slot `(1,2,+1/2)`": {"hosted"},
            "Full GU/Type II_1 anomaly shadow and Freed-Hopkins compatibility": {"open"},
        }
        for datum, allowed_statuses in checks.items():
            self.assertIn(datum, row_by_datum)
            self.assertIn(row_by_datum[datum]["status"], allowed_statuses)

    def test_first_failure_section_names_a_f_and_no_selector(self) -> None:
        section = self.text.split("## 4. First Genuine Forbidden-Input Or Selector Failure", 1)[1]
        section = section.split("## 5. Claim Certificate Table", 1)[0]
        self.assertIn("The first failure is `A_F`", section)
        self.assertIn("No current selector succeeds", section)
        self.assertIn("G_SM", section)
        self.assertIn("Z_6", section)

    def test_claim_certificates_are_present(self) -> None:
        for certificate in ["TYPEII1-SELECTOR", "SM-GAUGE", "HIGGS", "ANOMALY"]:
            self.assertIn(f"`{certificate}`", self.text)

    def test_selector_robustness_rows_are_present(self) -> None:
        for selector in [
            "Fixed-data rigidity selector",
            "Trace selector",
            "`C_n` crossed-product selector",
            "C3/D4 visible-three selector",
            "Imported finite CC host",
            "GU carrier only",
        ]:
            self.assertIn(selector, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
