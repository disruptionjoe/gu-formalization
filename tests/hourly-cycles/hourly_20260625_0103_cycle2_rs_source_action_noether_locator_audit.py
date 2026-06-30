#!/usr/bin/env python3
"""Audit the Cycle 2 RS source action/Noether locator artifact."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle2-rs-source-action-noether-locator.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. Direct Source Derivations",
    "## 3. Strongest Positive Result",
    "## 4. First Exact Obstruction",
    "## 5. Constructive Next Object",
    "## 6. GU Claim Impact",
    "## 7. Next Proof Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_TOP_LEVEL_FIELDS = {
    "artifact",
    "version",
    "run",
    "cycle",
    "lane",
    "verdict",
    "decision",
    "accepted_source_locator",
    "searched_source_list",
    "locator_decision_table",
    "source_vs_reconstruction_separation",
    "first_exact_obstruction",
    "d_RS_minus_1_claim_gate",
    "rank_generation_quarantine",
    "constructive_next_object",
    "GU_claim_impact",
    "next_proof_step",
}

REQUIRED_SEARCHED_PATHS = {
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "literature/weinstein-ucsd-2025-04-transcript.md",
    "Geometric_UnityDraftApril1st2021.pdf",
    "sources/claim-ledger.md",
    "sources/media-claim-mining-report-v1.md",
    "explorations/hourly-20260625-0103-cycle1-rs-d-minus-1-source-origin-certificate.md",
    "explorations/hourly-cycle3-rs-source-differential-origin-screen-2026-06-25.md",
    "explorations/af4-tau-rs-gauge-fixing-2026-06-23.md",
    "explorations/hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md",
    "explorations/hourly-cycle3-dgu-operator-source-receipt-inventory-2026-06-25.md",
    "explorations/gu-typed-operator-action-spine-2026-06-24.md",
    "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md",
    "explorations/hourly-cycle2-rs-quotient-transport-builder-2026-06-25.md",
    "tests/rs_clifford_projector_model.py",
}

ALLOWED_DECISIONS = {
    "ACCEPT_SOURCE_LOCATOR",
    "BLOCKED_NO_SOURCE_ACTION",
    "IMPORT_OR_RECONSTRUCTION_ONLY",
    "FAIL_CONTRADICTORY_SOURCE",
}

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bphysical rank is derived\b",
    r"\bH-index is derived\b",
    r"\brank\s*3\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*4\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\brank\s*8\s+(is|has been)\s+(derived|promoted|proved|closed)\b",
    r"\bthree generations\s+(are|is|have been|has been)\s+derived\b",
    r"\bfour generations\s+(are|is|have been|has been)\s+derived\b",
    r"\braw principal symbol proves d_RS,-1\b",
    r"\bAF4 .* proves d_RS,-1\b",
]


def extract_summary(text: str) -> dict[str, object]:
    for block in re.findall(r"```json\s*(.*?)\s*```", text, re.DOTALL):
        data = json.loads(block)
        if data.get("artifact") == "RSSourceActionNoetherLocator_V1":
            return data
    raise AssertionError("RSSourceActionNoetherLocator_V1 JSON summary not found")


class RSSourceActionNoetherLocatorAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_required_headings_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_json_has_required_top_level_fields(self) -> None:
        self.assertEqual(set(self.summary), REQUIRED_TOP_LEVEL_FIELDS)

    def test_verdict_blocks_without_accepting_source_locator(self) -> None:
        self.assertEqual(self.summary["verdict"], "BLOCKED_NO_SOURCE_ACTION")
        self.assertEqual(self.summary["decision"], "BLOCKED_NO_SOURCE_ACTION")
        self.assertFalse(self.summary["accepted_source_locator"])

    def test_searched_source_list_covers_required_sources(self) -> None:
        paths = {entry["path"] for entry in self.summary["searched_source_list"]}
        missing = REQUIRED_SEARCHED_PATHS - paths
        self.assertFalse(missing, f"missing searched sources: {sorted(missing)}")
        self.assertGreaterEqual(len(paths), len(REQUIRED_SEARCHED_PATHS))

        statuses = {entry["locator_status"] for entry in self.summary["searched_source_list"]}
        for required_status in {
            "primary_context_not_locator",
            "reconstruction_phrase_only",
            "raw_principal_symbol_context",
            "upstream_source_receipt_missing",
            "blocked_prior",
        }:
            self.assertIn(required_status, statuses)

    def test_locator_decision_table_is_decision_grade_and_non_accepting(self) -> None:
        table = self.summary["locator_decision_table"]
        self.assertGreaterEqual(len(table), 6)
        decisions = {row["decision"] for row in table}
        self.assertTrue(decisions <= ALLOWED_DECISIONS)
        self.assertIn("BLOCKED_NO_SOURCE_ACTION", decisions)
        self.assertIn("IMPORT_OR_RECONSTRUCTION_ONLY", decisions)
        for row in table:
            self.assertFalse(row["accepts"], f"unexpected accepting row: {row}")

        candidates = {row["candidate"] for row in table}
        self.assertIn("primary_GU_action_or_operator_for_RS_sector", candidates)
        self.assertIn("AF4_nabla_epsilon_gauge_phrase", candidates)
        self.assertIn("raw_Cl4_projector_gauge_symbol", candidates)

    def test_source_vs_reconstruction_and_raw_symbol_are_separated(self) -> None:
        separation = self.summary["source_vs_reconstruction_separation"]
        self.assertIn("direct_source_receipts", separation)
        self.assertIn("reconstruction_phrases", separation)
        self.assertIn("raw_principal_symbol_context", separation)
        self.assertIn("forbidden_promotions", separation)

        self.assertTrue(
            any("2021 draft" in item for item in separation["direct_source_receipts"])
        )
        self.assertIn(
            "AF4 psi_a^RS ~ psi_a^RS + nabla_a epsilon",
            separation["reconstruction_phrases"],
        )
        self.assertIn(
            "tests/rs_clifford_projector_model.py gauge_symbol: epsilon -> xi tensor epsilon",
            separation["raw_principal_symbol_context"],
        )
        self.assertIn(
            "raw_symbol_to_source_derivation",
            separation["forbidden_promotions"],
        )

    def test_first_obstruction_is_source_action_or_noether_locator(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["field"], "source_action_or_noether_locator")
        self.assertEqual(obstruction["status"], "MISSING")
        self.assertIn("No repo-local primary source", obstruction["description"])
        self.assertIn("Noether identity", obstruction["description"])
        self.assertIn("BRST theorem", obstruction["description"])

    def test_no_source_derived_d_rs_claim_without_acceptance(self) -> None:
        gate = self.summary["d_RS_minus_1_claim_gate"]
        self.assertFalse(self.summary["accepted_source_locator"])
        self.assertFalse(gate["source_derived_d_RS_minus_1_available"])
        self.assertFalse(gate["may_claim_source_derived_d_RS_minus_1"])
        self.assertTrue(gate["candidate_formula_allowed"])
        self.assertEqual(gate["candidate_status"], "candidate_shape_only_not_source_derived")

    def test_rank_generation_quarantine_is_active(self) -> None:
        quarantine = self.summary["rank_generation_quarantine"]
        self.assertEqual(quarantine["status"], "ACTIVE")
        for key in [
            "physical_rank_promoted",
            "H_index_promoted",
            "rank_3_promoted",
            "rank_4_promoted",
            "rank_8_promoted",
            "three_generations_promoted",
            "four_generations_promoted",
        ]:
            self.assertFalse(quarantine[key])

        for forbidden in [
            "physical_rank_target",
            "H_index_target",
            "rank_3",
            "rank_4",
            "rank_8",
            "three_generations",
            "four_generations",
            "target_normalization",
            "raw_projected_gauge_image_as_physical_loss",
        ]:
            self.assertIn(forbidden, quarantine["forbidden_inputs"])

    def test_constructive_next_object_accepts_only_real_source_kinds(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "RS_SOURCE_ACTION_NOETHER_RECEIPT_V1")
        self.assertEqual(next_object["first_required_field"], "source_locator")
        self.assertIn("Noether_identity", next_object["accepted_source_kinds"])
        self.assertIn("BRST_theorem", next_object["accepted_source_kinds"])
        self.assertIn("reconstruction_phrase", next_object["reject_source_kinds"])
        self.assertIn("raw_symbol_context", next_object["reject_source_kinds"])

    def test_gu_claim_impact_is_blocked_not_falsified(self) -> None:
        impact = self.summary["GU_claim_impact"]
        self.assertFalse(impact["GU_RS_branch_falsified"])
        self.assertEqual(impact["current_status"], "SOURCE_ACTION_NOETHER_LOCATOR_BLOCKED")
        self.assertIn("Noether/BRST theorem", impact["what_must_exist_if_branch_correct"])
        self.assertEqual(impact["rank_generation_claim_status"], "QUARANTINED_NOT_DERIVED")

    def test_no_forbidden_promotion_language(self) -> None:
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                msg=f"forbidden promotion pattern present: {pattern}",
            )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            RSSourceActionNoetherLocatorAuditTests
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
