#!/usr/bin/env python3
"""Audit SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle2-ig-source-window-bianchi-selector-inventory.md"
)

EXPECTED_WINDOWS = {
    "section_8_eqs_8_1_8_7": ["8.1", "8.2", "8.3", "8.4", "8.5", "8.6", "8.7"],
    "section_9_1_eqs_9_2_9_6": ["9.2", "9.3", "9.4", "9.5", "9.6"],
    "summary_eqs_12_2_12_7": ["12.2", "12.3", "12.4", "12.5", "12.6", "12.7"],
}

EXPECTED_RIVALS = {
    "exterior_derivative",
    "coderivative_trace_scalar",
    "symmetric_derivative",
    "projected_derivative",
    "lower_order_dressed_exterior",
    "displayed_shiab_codomain",
}

REQUIRED_OPERATOR_FIELDS = {
    "id",
    "domain",
    "codomain",
    "principal_symbol",
    "parent_momentum_degree",
    "projection_behavior",
    "lower_order_freedom",
    "required_geometric_data",
    "bianchi_highest_weight_selector_language",
    "rival_eliminator_found",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class IGSourceWindowBianchiSelectorInventoryAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["artifact_id"],
            "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
        )
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle2_ig_source_window_bianchi_selector_inventory_audit.py",
        )

    def test_all_required_windows_and_equations_are_present(self) -> None:
        windows = {row["window_id"]: row for row in self.summary["inventoried_windows"]}
        self.assertEqual(set(windows), set(EXPECTED_WINDOWS))
        for window_id, equations in EXPECTED_WINDOWS.items():
            row = windows[window_id]
            self.assertEqual(row["status"], "present")
            self.assertEqual(row["equations"], equations)
            for eq in equations:
                self.assertIn(f"`{eq}`", self.text)

    def test_operator_rows_are_nonempty_and_typed(self) -> None:
        rows = self.summary["operator_rows"]
        self.assertGreater(len(rows), 0)
        for row in rows:
            self.assertTrue(REQUIRED_OPERATOR_FIELDS.issubset(row), row.get("id"))
            self.assertIsInstance(row["required_geometric_data"], list)
            self.assertGreater(len(row["required_geometric_data"]), 0)
            self.assertFalse(row["rival_eliminator_found"], row["id"])
            for field in REQUIRED_OPERATOR_FIELDS - {
                "required_geometric_data",
                "rival_eliminator_found",
            }:
                self.assertTrue(str(row[field]).strip(), f"{row['id']}:{field}")

    def test_rival_counts_are_consistent(self) -> None:
        rivals = self.summary["rival_classes"]
        self.assertEqual({row["id"] for row in rivals}, EXPECTED_RIVALS)
        eliminated = [row for row in rivals if row["eliminated_by_source"]]
        surviving = [row for row in rivals if not row["eliminated_by_source"]]
        self.assertEqual(self.summary["eliminated_rival_count"], len(eliminated))
        self.assertEqual(self.summary["surviving_rival_count"], len(surviving))
        self.assertEqual(self.summary["eliminated_rival_count"], 0)
        self.assertEqual(self.summary["surviving_rival_count"], len(EXPECTED_RIVALS))

    def test_proof_restart_requires_identity_and_receipt(self) -> None:
        self.assertFalse(self.summary["selector_identity_passed"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertIn("proof_restart_allowed: false", self.text)
        self.assertIn("SourceForcedCodomainSelectorForK_IG", self.text)

    def test_first_obstruction_and_next_frontier_are_specific(self) -> None:
        self.assertIn("highest-weight/Bianchi selector calculation", self.summary["first_obstruction"])
        self.assertEqual(
            self.summary["missing_source_object"],
            "RecoveredBianchiHighestWeightSelectorForShiab_V1",
        )
        self.assertEqual(
            self.summary["next_frontier_object"],
            "RecoveredBianchiHighestWeightSelectorForShiab_V1",
        )
        self.assertIn("PREPARES_SELECTOR_THEOREM_RIVALS_NOT_ELIMINATED", self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
