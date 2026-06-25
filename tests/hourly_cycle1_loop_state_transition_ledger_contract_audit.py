#!/usr/bin/env python3
"""Audit the Cycle 1 LoopStateTransitionLedger_v1 contract artifact.

This audit checks the process contract, not GU mathematics. It verifies that the
artifact supplies a machine-readable summary, includes the required transition
classes, preserves same-session and target-import guards, and refuses to use the
new contract as a retroactive convergence proof.
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
    / "hourly-cycle1-loop-state-transition-ledger-contract-2026-06-25.md"
)

REQUIRED_HEADINGS = [
    "## 1. Verdict",
    "## 2. What Was Derived Directly From Repo Sources",
    "## 3. The Strongest Positive Result",
    "## 4. The First Exact Obstruction Or Missing Proof Object",
    "## 5. The Constructive Next Object That Would Remove Or Test The Obstruction",
    "## 6. What This Means For The Relevant GU Claim",
    "## 7. Next Meaningful Proof Or Computation Step",
    "## 8. Machine-Readable JSON Summary",
]

REQUIRED_ROW_FIELDS = {
    "ledger_version",
    "row_id",
    "item_id",
    "lane_family",
    "session_id",
    "cycle_index",
    "artifact_path",
    "audit_path",
    "previous_state",
    "new_state",
    "transition_type",
    "transition_basis",
    "refinement_delta",
    "guards",
    "source_refs",
}

REQUIRED_STATE_FIELDS = {
    "verdict",
    "missing_object_id",
    "blocker_family",
    "evidence_basis",
}

REQUIRED_TRANSITION_TYPES = {
    "closure",
    "same_status_refinement",
    "repetition",
    "downgrade",
    "false_negative",
    "same_session_circularity",
}

REQUIRED_SAME_SESSION_GUARDS = {
    "flag_raised_session_id",
    "flag_closed_session_id",
    "external_verification_id",
    "later_session_verification_id",
    "deferred_verification_required",
    "same_session_closure_attempted",
}

REQUIRED_TARGET_IMPORT_GUARDS = {
    "target_inputs_seen",
    "target_import_detected",
}

REQUIRED_FALSE_NEGATIVE_GUARDS = {
    "demotion_or_nonpromotion",
    "required_object_already_present",
    "over_deflation_detected",
}

FORBIDDEN_RETROACTIVE_OVERCLAIMS = [
    r'"retroactive_convergence_proof_claimed"\s*:\s*true',
    r'"major_gu_claim_promoted"\s*:\s*true',
    r"\bold three-cycle run has been retroactively proved convergent\b",
    r"\bmajor GU reconstruction gate was promoted\b",
]


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


class HourlyCycle1LoopStateTransitionLedgerContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_supplies_contract_without_retroactive_convergence_claim(self) -> None:
        self.assertEqual(self.summary["verdict"], "conditional")
        self.assertEqual(self.summary["contract_id"], "LoopStateTransitionLedger_v1")
        self.assertIs(self.summary["contract_supplied"], True)
        self.assertIs(self.summary["retroactive_convergence_proof_claimed"], False)
        self.assertIs(self.summary["major_gu_claim_promoted"], False)
        for pattern in FORBIDDEN_RETROACTIVE_OVERCLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden overclaim matched: {pattern}",
            )

    def test_direct_source_derivations_cover_required_repo_inputs(self) -> None:
        sources = self.summary["derived_directly_from_sources"]
        for key in [
            "research_posture",
            "five_lane_frontier_run",
            "cycle3_loop_calibration",
            "three_cycle_synthesis",
            "loop_adversarial_log",
        ]:
            self.assertIn(key, sources)
            self.assertGreaterEqual(len(sources[key]), 3, key)

    def test_required_schema_fields_are_present(self) -> None:
        row_fields = set(self.summary["required_row_fields"])
        self.assertTrue(
            REQUIRED_ROW_FIELDS.issubset(row_fields),
            f"missing row fields: {sorted(REQUIRED_ROW_FIELDS - row_fields)}",
        )
        state_fields = set(self.summary["required_state_fields"])
        self.assertTrue(
            REQUIRED_STATE_FIELDS.issubset(state_fields),
            f"missing state fields: {sorted(REQUIRED_STATE_FIELDS - state_fields)}",
        )

    def test_required_guards_are_machine_readable(self) -> None:
        guards = self.summary["required_guard_fields"]
        same_session = set(guards["same_session"])
        target_import = set(guards["target_import"])
        false_negative = set(guards["false_negative"])
        self.assertTrue(REQUIRED_SAME_SESSION_GUARDS.issubset(same_session))
        self.assertTrue(REQUIRED_TARGET_IMPORT_GUARDS.issubset(target_import))
        self.assertTrue(REQUIRED_FALSE_NEGATIVE_GUARDS.issubset(false_negative))

    def test_transition_types_cover_assignment_classes(self) -> None:
        transition_types = set(self.summary["transition_types_required"])
        self.assertEqual(transition_types, REQUIRED_TRANSITION_TYPES)
        precedence = self.summary["classifier_precedence"]
        self.assertLess(
            precedence.index("same_session_circularity"),
            precedence.index("closure"),
        )
        self.assertLess(precedence.index("false_negative"), precedence.index("closure"))
        for transition_type in REQUIRED_TRANSITION_TYPES:
            self.assertIn(transition_type, precedence)

    def test_example_rows_cover_each_required_transition_class(self) -> None:
        rows = self.summary["example_rows"]
        seen = {row["transition_type"] for row in rows}
        self.assertEqual(seen, REQUIRED_TRANSITION_TYPES)
        self.assertEqual(len(rows), len(REQUIRED_TRANSITION_TYPES))
        for row in rows:
            for key in [
                "row_id",
                "item_id",
                "transition_type",
                "previous_verdict",
                "new_verdict",
                "previous_missing_object_id",
                "new_missing_object_id",
                "guard_pass",
            ]:
                self.assertIn(key, row)

    def test_example_rows_encode_specific_guard_failures(self) -> None:
        by_type = {row["transition_type"]: row for row in self.summary["example_rows"]}
        self.assertIs(by_type["closure"]["guard_pass"], True)
        self.assertIs(by_type["same_status_refinement"]["guard_pass"], True)
        self.assertIs(by_type["repetition"]["guard_pass"], True)
        self.assertIs(by_type["downgrade"]["guard_pass"], True)
        self.assertIs(by_type["false_negative"]["guard_pass"], False)
        self.assertIs(by_type["false_negative"]["over_deflation_detected"], True)
        self.assertIs(by_type["same_session_circularity"]["guard_pass"], False)
        self.assertIs(by_type["same_session_circularity"]["same_session_closure_attempted"], True)

    def test_first_obstruction_blocks_retroactive_proof_for_precise_reason(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "HISTORICAL_PRE_STATE_TRANSITION_ROWS_V1")
        self.assertEqual(obstruction["name"], "HistoricalPreStateTransitionRows_v1")
        self.assertIn("prior-state rows", obstruction["why_first"])
        missing = set(obstruction["missing_components"])
        for component in [
            "universal_stable_item_ids",
            "normalized_previous_verdicts",
            "row_linked_same_session_flags",
            "pre_transition_required_object_presence",
            "exact_missing_object_and_blocker_equality_for_repetition",
        ]:
            self.assertIn(component, missing)

    def test_constructive_next_object_is_bounded_backfill_not_proof_inflation(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "HISTORICAL_PRE_STATE_TRANSITION_ROWS_V1")
        self.assertIn("bounded backfill", next_object["purpose"])
        acceptance = set(next_object["acceptance_test"])
        for step in [
            "choose_bounded_run_family",
            "assign_stable_item_ids_before_using_later_results",
            "backfill_previous_state_only_from_earlier_artifacts",
            "mark_inferred_fields_unknown",
            "run_same_classifier",
        ]:
            self.assertIn(step, acceptance)

    def test_gu_claim_impact_is_process_conditional_not_physics_promotion(self) -> None:
        impact = self.summary["impact_for_gu_claim"]
        self.assertIs(impact["new_physics_claim"], False)
        self.assertIn("LoopStateTransitionLedger_v1 rows", impact["future_convergence_metrics_condition"])
        self.assertEqual(impact["old_three_cycle_convergence_status"], "not_retroactively_proved")
        self.assertIn("separate closure", impact["process_gain"])

    def test_next_step_adds_future_emission_and_classifier_audit(self) -> None:
        self.assertIn("row emission", self.summary["next_meaningful_step"])
        self.assertIn("classifier audit", self.summary["next_meaningful_step"])


def audit_summary() -> dict[str, Any]:
    text = read_artifact()
    summary = extract_summary(text)
    return {
        "document": str(ARTIFACT.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "contract_id": summary["contract_id"],
        "transition_types": summary["transition_types_required"],
        "first_exact_obstruction": summary["first_exact_obstruction"]["name"],
        "retroactive_convergence_proof_claimed": summary["retroactive_convergence_proof_claimed"],
    }


def main(argv: list[str] | None = None) -> int:
    if argv and "--json" in argv:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            HourlyCycle1LoopStateTransitionLedgerContractAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
