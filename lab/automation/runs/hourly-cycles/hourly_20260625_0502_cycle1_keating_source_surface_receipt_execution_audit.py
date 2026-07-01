#!/usr/bin/env python3
"""Audit KeatingSourceSurfaceReceiptExecution_V1.

The audit parses the embedded JSON summary and checks the lane contract:
the four owned Keating source IDs are represented, target-import guard status is
enforced, all four receipt families are covered, accepted receipts remain zero,
proof restart and claim promotion are blocked, and the first exact obstruction
is the missing Keating Revealed Shiab/projection sheet.
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
    / "hourly-20260625-0502-cycle1-keating-source-surface-receipt-execution.md"
)

EXPECTED_SOURCE_IDS = {
    "GU-MEDIA-KEATING-QG-FBOZSSLXFVI",
    "GU-POD-2025-KEATING-DESI-GU",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
}

EXPECTED_FAMILIES = {"IG", "RS", "QFT", "DGU_VZ"}

EXPECTED_REQUIRED_OBJECTS = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing Keating source execution artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class KeatingSourceSurfaceReceiptExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "KeatingSourceSurfaceReceiptExecution_V1",
        )
        self.assertEqual(self.summary["version"], "2026-06-25")
        self.assertEqual(self.summary["run"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 4)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_ONE_SOURCE_SIDE_LOCATOR_CANDIDATE_ZERO_ACCEPTED_RECEIPTS",
        )
        self.assertEqual(self.summary["verdict_class"], "blocked")
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle1-keating-source-surface-receipt-execution.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle1_keating_source_surface_receipt_execution_audit.py",
        )

    def test_four_keating_source_ids_represented(self) -> None:
        represented = set(self.summary["keating_source_ids_represented"])
        self.assertEqual(represented, EXPECTED_SOURCE_IDS)
        result_ids = {row["source_id"] for row in self.summary["source_surface_results"]}
        self.assertEqual(result_ids, EXPECTED_SOURCE_IDS)

    def test_target_import_guard_status(self) -> None:
        self.assertEqual(self.summary["target_import_guard_status"], "enforced")
        guard = self.summary["target_import_guard"]
        self.assertEqual(guard["status"], "enforced")
        self.assertTrue(guard["DESI_dark_energy_used_only_for_acquisition_priority"])
        self.assertFalse(guard["target_data_used_to_select_source_object"])
        self.assertFalse(guard["candidate_with_target_data_seen_nonempty_accepted"])
        guarded_terms = set(guard["guarded_terms"])
        for term in ["DESI", "dark_energy", "FLRW", "VZ_closure"]:
            self.assertIn(term, guarded_terms)

        desi_row = next(
            row
            for row in self.summary["source_surface_results"]
            if row["source_id"] == "GU-POD-2025-KEATING-DESI-GU"
        )
        self.assertTrue(desi_row["target_import_sensitive"])
        self.assertFalse(desi_row["accepted_for_routing"])

    def test_required_family_coverage(self) -> None:
        coverage = self.summary["required_family_coverage"]
        self.assertEqual(set(coverage), EXPECTED_FAMILIES)
        for family, required_object in EXPECTED_REQUIRED_OBJECTS.items():
            row = coverage[family]
            self.assertEqual(row["required_object"], required_object)
            self.assertTrue(row["represented"], family)
            self.assertFalse(row["receipt_found"], family)
            self.assertEqual(row["restart_gate"], "blocked", family)
            self.assertIn("first_missing_object", row)

    def test_acceptance_restart_and_promotion_are_blocked(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

        locator = self.summary["strongest_positive_locator"]
        self.assertEqual(locator["acceptance_status"], "quarantined")
        self.assertEqual(locator["restart_gate"], "blocked")
        self.assertEqual(locator["emitted_formula_or_rule"], "none")
        self.assertEqual(locator["target_data_seen"], [])
        self.assertTrue(locator["source_side_not_target_facing"])

        for key, value in self.summary["no_claim_promotions"].items():
            self.assertFalse(value, key)

    def test_first_exact_obstruction_is_missing_shiab_projection_sheet(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "KeatingRevealed_ShiabProjectionSheet_V1")
        self.assertEqual(obstruction["missing_field"], "emitted_formula_or_rule")
        self.assertIn("Shiab operator", obstruction["description"])
        self.assertIn("projection formula", obstruction["description"])
        self.assertIn("PrimarySourceReceiptInstance_V1", obstruction["description"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "KeatingRevealed_ShiabProjectionSheet_V1")
        self.assertTrue(next_object["would_test_or_remove_obstruction"])
        self.assertGreaterEqual(len(next_object["acquisition_steps"]), 3)

    def test_required_sections_and_verdict_language_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. What Was Derived Directly From Repo/Source Surfaces",
            "## 3. Strongest Positive Locator or Construction Attempt",
            "## 4. First Exact Obstruction or Missing Proof/Source Object",
            "## 5. Constructive Next Object That Would Remove or Test the Obstruction",
            "## 6. What This Means for the Relevant GU Claim",
            "## 7. Next Meaningful Source/Proof Computation Step",
            "## 9. Machine-Readable JSON Summary",
        ]:
            self.assertIn(heading, self.text)
        self.assertIn("No GU claim is promoted.", self.text)
        self.assertIn("Proof computation remains blocked", self.text)


if __name__ == "__main__":
    unittest.main()
