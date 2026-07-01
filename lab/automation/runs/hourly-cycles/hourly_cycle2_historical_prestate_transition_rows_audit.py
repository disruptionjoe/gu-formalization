#!/usr/bin/env python3
"""Audit HistoricalPreStateTransitionRows_v1 bounded backfill artifact.

This audit checks process discipline, not GU mathematics. It verifies that the
artifact uses the ten bounded Cycle 1/2 hourly blocker artifacts, emits stable
item IDs, reports classifiable/ambiguous/blocked rows, preserves same-session
and target guards, and refuses retroactive convergence overclaim.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-cycle2-historical-prestate-transition-rows-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What was derived directly from repo sources",
    "## 3. Strongest positive construction attempt",
    "## 4. First exact obstruction or missing proof object",
    "## 5. Constructive next object",
    "## 6. Impact on GU/process claim",
    "## 7. Next meaningful proof/computation step",
    "## 8. Machine-readable JSON summary",
]

BOUNDED_ARTIFACTS = {
    "explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md",
    "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md",
    "explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md",
    "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md",
    "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md",
    "explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md",
    "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md",
    "explorations/hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md",
    "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md",
    "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md",
}

REQUIRED_STABLE_ITEM_IDS = {
    "item:ig-theta-source-forced-selector",
    "item:rs-physical-effective-rank",
    "item:phi-obs-fixed-data-selector",
    "item:qft-source-mode-quotient-gram",
    "item:vz-actual-operator-characteristic",
}

REQUIRED_CLASSIFIABLE_ROWS = {
    "hist-prestate-c2-ig-theta": "K_IG_selector",
    "hist-prestate-c2-rs": "d_RS,-1",
    "hist-prestate-c2-qft": "SourceProjectorPFinBWithLocalModeRecords",
    "hist-prestate-c2-vz": "ActualDGU01OperatorCertificate",
}

FORBIDDEN_OVERCLAIMS = [
    r'"retroactive_convergence_proof_claimed"\s*:\s*true',
    r'"major_gu_claim_promoted"\s*:\s*true',
    r'"new_physics_claim"\s*:\s*true',
    r'"same_session_closure_claimed"\s*:\s*true',
    r'"target_import_closure_claimed"\s*:\s*true',
    r"\bold three-cycle run (?:is|was|has been) retroactively proved convergent\b",
    r"\bretroactive convergence (?:is|was|has been) proved\b",
    r"\bmajor GU claim (?:is|was|has been) promoted\b",
]


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HistoricalPreStateTransitionRowsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)
        cls.rows = cls.summary["rows"]
        cls.rows_by_id = {row["row_id"]: row for row in cls.rows}

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_partial_backfill_not_retroactive_convergence(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "BOUNDED_BACKFILL_PARTIAL_CLASSIFICATION_RETROACTIVE_CONVERGENCE_BLOCKED",
        )
        self.assertIs(self.summary["retroactive_convergence_proof_claimed"], False)
        self.assertIs(self.summary["major_gu_claim_promoted"], False)
        self.assertIs(self.summary["new_physics_claim"], False)
        self.assertIs(self.summary["same_session_closure_claimed"], False)
        self.assertIs(self.summary["target_import_closure_claimed"], False)
        self.assertIs(self.summary["false_negative_found"], False)
        for pattern in FORBIDDEN_OVERCLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden overclaim matched: {pattern}",
            )

    def test_bounded_family_is_exactly_ten_cycle1_cycle2_hourlies(self) -> None:
        family = self.summary["bounded_family"]
        self.assertEqual(family["artifact_count"], 10)
        self.assertEqual(family["included_cycles"], [1, 2])
        self.assertEqual(family["excluded_cycles"], [3])

        row_artifacts = {row["artifact_path"] for row in self.rows}
        self.assertEqual(row_artifacts, BOUNDED_ARTIFACTS)
        self.assertEqual(len(self.rows), 10)

    def test_stable_item_ids_are_family_level_and_reused(self) -> None:
        self.assertEqual(set(self.summary["stable_item_ids"]), REQUIRED_STABLE_ITEM_IDS)
        item_ids = [row["item_id"] for row in self.rows]
        for item_id in REQUIRED_STABLE_ITEM_IDS:
            self.assertEqual(item_ids.count(item_id), 2, item_id)

    def test_classification_counts_match_rows(self) -> None:
        counts = self.summary["classification_counts"]
        self.assertEqual(counts["classifiable"], 4)
        self.assertEqual(counts["ambiguous"], 1)
        self.assertEqual(counts["blocked_missing_pre_state"], 5)
        self.assertEqual(counts["same_status_refinement"], 4)
        for forbidden_type in [
            "closure",
            "repetition",
            "downgrade",
            "false_negative",
            "same_session_circularity",
        ]:
            self.assertEqual(counts[forbidden_type], 0, forbidden_type)

        buckets = [row["classification_bucket"] for row in self.rows]
        self.assertEqual(buckets.count("classifiable"), 4)
        self.assertEqual(buckets.count("ambiguous"), 1)
        self.assertEqual(buckets.count("blocked"), 5)

    def test_cycle1_rows_are_blocked_by_missing_pre_state(self) -> None:
        cycle1 = [row for row in self.rows if row["cycle_index"] == 1]
        self.assertEqual(len(cycle1), 5)
        for row in cycle1:
            self.assertEqual(row["transition_type"], "blocked_missing_pre_state")
            self.assertEqual(row["classification_bucket"], "blocked")
            self.assertEqual(row["previous_state"]["verdict"], "unknown")
            self.assertEqual(row["previous_state"]["evidence_basis"], "missing_pre_state")

    def test_cycle2_classifiable_rows_are_same_status_refinements(self) -> None:
        for row_id, expected_missing in REQUIRED_CLASSIFIABLE_ROWS.items():
            row = self.rows_by_id[row_id]
            self.assertEqual(row["transition_type"], "same_status_refinement")
            self.assertEqual(row["classification_bucket"], "classifiable")
            self.assertEqual(row["new_state"]["first_missing_object_id"], expected_missing)
            self.assertIn("refinement", row["refinement_basis"].lower())
            self.assertNotEqual(row["previous_state"]["verdict"], "unknown")

    def test_phi_obs_cycle2_row_is_ambiguous_not_forced(self) -> None:
        row = self.rows_by_id["hist-prestate-c2-phi-obs"]
        self.assertEqual(row["transition_type"], "ambiguous_not_classified")
        self.assertEqual(row["classification_bucket"], "ambiguous")
        self.assertIn("item identity", row["ambiguity_reason"])
        self.assertNotEqual(row["transition_type"], "same_status_refinement")

    def test_same_session_and_target_guards_are_present_for_every_row(self) -> None:
        for row in self.rows:
            guards = row["guard_summary"]
            self.assertIn("same_session_guard", guards, row["row_id"])
            self.assertIn("target_import_guard", guards, row["row_id"])
            self.assertIn("false_negative_guard", guards, row["row_id"])
            self.assertIn("no_closure", guards["same_session_guard"], row["row_id"])
            self.assertNotIn("closure_passed", guards["same_session_guard"], row["row_id"])
            self.assertNotIn("target_import_closure", guards["target_import_guard"], row["row_id"])

    def test_source_receipts_cover_required_read_first_files_and_paired_audits(self) -> None:
        receipts = self.summary["source_receipts"]
        self.assertEqual(receipts["research_posture"], "RESEARCH-POSTURE.md")
        self.assertEqual(receipts["runbook"], "process/runbooks/five-lane-frontier-run.md")
        self.assertEqual(
            receipts["cycle1_contract"],
            "explorations/hourly-cycle1-loop-state-transition-ledger-contract-2026-06-25.md",
        )
        self.assertEqual(
            receipts["cycle3_calibration"],
            "explorations/hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md",
        )
        self.assertEqual(
            receipts["three_cycle_synthesis"],
            "explorations/hourly-three-cycle-fifteen-hole-synthesis-2026-06-24.md",
        )
        self.assertEqual(len(receipts["paired_audits"]), 10)
        for audit_path in receipts["paired_audits"]:
            self.assertTrue((REPO_ROOT / audit_path).exists(), audit_path)

    def test_first_obstruction_and_next_object_are_machine_readable(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "MISSING_HISTORICAL_PRE_STATE_ROWS")
        self.assertEqual(obstruction["blocks"], "retroactive_convergence_proof")

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "LoopStateTransitionLedger_v1_hourly_wrapper_emission")
        self.assertIs(next_object["required_before_future_convergence_metrics"], True)
        for field in [
            "item_id",
            "previous_state",
            "new_state",
            "transition_type",
            "same_session_guard",
            "target_import_guard",
            "false_negative_guard",
        ]:
            self.assertIn(field, next_object["required_fields"])

    def test_impact_is_process_gain_only(self) -> None:
        impact = self.summary["impact_on_gu_process_claim"]
        self.assertIn("same-status refinement", impact["process_gain"])
        self.assertEqual(
            impact["old_three_cycle_convergence_status"],
            "not_retroactively_proved",
        )
        self.assertIn("LoopStateTransitionLedger_v1", impact["future_metrics_condition"])
        self.assertIn("classifier audit", self.summary["next_meaningful_step"])


def audit_summary() -> dict[str, Any]:
    text = read_artifact()
    summary = extract_summary(text)
    return {
        "document": str(ARTIFACT.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "classification_counts": summary["classification_counts"],
        "retroactive_convergence_proof_claimed": summary[
            "retroactive_convergence_proof_claimed"
        ],
        "first_exact_obstruction": summary["first_exact_obstruction"]["id"],
    }


def main(argv: list[str] | None = None) -> int:
    if argv and "--json" in argv:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HistoricalPreStateTransitionRowsAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
