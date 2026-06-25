#!/usr/bin/env python3
"""Audit PrimaryGUSourceReceiptAvailabilityLedger_V1.

This structural audit parses the embedded JSON summary and checks that the
ledger has four family rows, uses the required source-status categories, refuses
claim promotions, gives sequential/parallel guidance, identifies the first
global missing object, and names next source-mining tasks.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md"
)

EXPECTED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Strongest Positive Result",
    "## 4. First Exact Obstruction",
    "## 5. Constructive Next Object",
    "## 6. GU Claim Impact",
    "## 7. Next Proof Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_CATEGORIES = {
    "primary_source_receipt",
    "reconstruction_proposal",
    "transcript_hint",
    "representation_label",
    "raw_computation",
    "missing_source",
}

REQUIRED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

REQUIRED_NO_PROMOTIONS = {
    "IG_K_IG_selected",
    "RS_d_RS_minus_1_source_derived",
    "QFT_P_fin_b_supplied",
    "DGU_actual_operator_identified",
    "VZ_evasion_closed",
    "dark_energy_or_FLRW_recovered",
    "QFT_state_or_CHSH_recovered",
    "physical_rank_or_generation_readout",
}

REQUIRED_NEXT_TASK_TERMS = {
    "IG": ["Mine", "IG", "selector"],
    "RS": ["Mine", "RS", "gauge"],
    "QFT": ["Mine", "P_fin"],
    "DGU_VZ": ["Mine", "D_GU"],
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing source availability ledger: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class PrimaryGUSourceReceiptAvailabilityLedgerAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)
        cls.rows = {
            row["family"]: row for row in cls.summary["family_rows"]  # type: ignore[index]
        }

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_summary_identity_and_global_obstruction(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "PrimaryGUSourceReceiptAvailabilityLedger_V1",
        )
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_NO_FAMILY_HAS_PRIMARY_SOURCE_RECEIPT",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        missing = self.summary["first_missing_global_object"]
        self.assertEqual(missing["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        self.assertIs(missing["missing"], True)
        self.assertIn("primary GU source locators", missing["description"])

    def test_four_family_rows_are_present(self) -> None:
        self.assertEqual(set(self.rows), REQUIRED_FAMILIES)
        self.assertEqual(len(self.rows), 4)
        for family, row in self.rows.items():
            self.assertIn("required_object", row, family)
            self.assertIn("first_exact_obstruction", row, family)
            self.assertIn("next_source_mining_task", row, family)
            self.assertIs(row["primary_source_receipt"], False, family)
            self.assertIs(row["missing_source"], True, family)
            self.assertIs(row["promotion_allowed"], False, family)

    def test_source_status_categories_are_required_and_used(self) -> None:
        categories = set(self.summary["source_status_categories"])
        self.assertEqual(categories, REQUIRED_CATEGORIES)
        for row in self.rows.values():
            for category in REQUIRED_CATEGORIES:
                if category == "primary_source_receipt":
                    self.assertIn(category, row)
                elif category in row:
                    self.assertIsInstance(row[category], bool)

    def test_family_classification_matches_current_receipt_availability(self) -> None:
        self.assertIs(self.rows["IG"]["reconstruction_proposal"], True)
        self.assertIs(self.rows["IG"]["transcript_hint"], True)
        self.assertIs(self.rows["IG"]["raw_computation"], False)
        self.assertEqual(
            self.rows["IG"]["required_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )

        self.assertIs(self.rows["RS"]["raw_computation"], True)
        self.assertIs(self.rows["RS"]["transcript_hint"], False)
        self.assertIn("d_RS,-1", self.rows["RS"]["required_object"])

        self.assertIs(self.rows["QFT"]["representation_label"], True)
        self.assertIs(self.rows["QFT"]["raw_computation"], False)
        self.assertIn("P_fin^b", self.rows["QFT"]["required_object"])

        self.assertIs(self.rows["DGU_VZ"]["transcript_hint"], True)
        self.assertIs(self.rows["DGU_VZ"]["raw_computation"], True)
        self.assertIn(
            "operator_source_primary_action_or_EL",
            self.rows["DGU_VZ"]["required_object"],
        )

    def test_no_claim_promotions(self) -> None:
        promotions = self.summary["no_claim_promotions"]
        self.assertEqual(set(promotions), REQUIRED_NO_PROMOTIONS)
        for key, value in promotions.items():
            self.assertIs(value, False, key)

        for row in self.rows.values():
            self.assertIs(row["promotion_allowed"], False)

    def test_sequential_and_parallel_guidance_present(self) -> None:
        sequential = self.summary["sequential_guidance"]
        self.assertEqual(set(sequential), REQUIRED_FAMILIES)
        self.assertIn("source selector before", sequential["IG"])
        self.assertIn("rank arithmetic", sequential["RS"])
        self.assertIn("P_fin^b locator before", sequential["QFT"])
        self.assertIn("primary operator receipt before", sequential["DGU_VZ"])

        parallel = self.summary["parallel_guidance"]
        allowed = set(parallel["allowed_now"])
        blocked = set(parallel["not_allowed_until_receipt"])
        self.assertIn("independent source-mining over distinct primary source IDs", allowed)
        self.assertIn("independent transcript timestamp extraction", allowed)
        self.assertIn("IG target coefficient computation", blocked)
        self.assertIn("RS rank or generation arithmetic", blocked)
        self.assertIn("QFT Gram covariance rho_AB or CHSH construction", blocked)
        self.assertIn("DGU/VZ actual-operator closure from typed spine alone", blocked)

    def test_next_source_mining_tasks_are_specific(self) -> None:
        for family, terms in REQUIRED_NEXT_TASK_TERMS.items():
            task = self.rows[family]["next_source_mining_task"]
            for term in terms:
                self.assertIn(term, task, f"{family} task missing {term!r}")

    def test_constructive_next_object_schema_is_present(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RepoLocalPrimaryGUSourceReceiptMap_V1")
        required = set(next_object["required_fields"])
        for field in [
            "family",
            "required_object",
            "primary_source_locator",
            "receipt_kind",
            "exact_source_fragment_or_derivation_cell",
            "emitted_formula_or_rule",
            "promotion_allowed",
            "next_source_mining_task",
            "parallelization_guidance",
        ]:
            self.assertIn(field, required)


if __name__ == "__main__":
    unittest.main()
