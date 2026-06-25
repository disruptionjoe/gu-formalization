#!/usr/bin/env python3
"""Audit LoopStateTransitionRowEmissionGate_V1.

This audit checks process instrumentation, not GU mathematics. It verifies that
the artifact defines prospective pre/post row emission, a classifier audit, and
an acceptance gate while preserving the Cycle 2 backfill limits and refusing
retroactive convergence or physics overclaims.
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
    / "hourly-cycle3-loop-transition-row-emission-gate-2026-06-25.md"
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

REQUIRED_SOURCE_RECEIPTS = {
    "research_posture": "RESEARCH-POSTURE.md",
    "runbook": "process/runbooks/five-lane-frontier-run.md",
    "cycle1_contract": "explorations/hourly-cycle1-loop-state-transition-ledger-contract-2026-06-25.md",
    "cycle2_backfill": "explorations/hourly-cycle2-historical-prestate-transition-rows-2026-06-25.md",
    "cycle3_calibration": "explorations/hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md",
}

REQUIRED_PRE_ROW_FIELDS = {
    "ledger_version",
    "emission_gate_version",
    "row_phase",
    "row_id",
    "item_id",
    "lane_family",
    "session_id",
    "cycle_index",
    "worker_id",
    "owned_artifact_path",
    "owned_audit_path",
    "previous_state",
    "pre_state_locked_at",
    "pre_state_locked_by",
    "same_session_guard",
    "target_import_guard",
}

REQUIRED_POST_ROW_FIELDS = {
    "row_phase",
    "row_id",
    "item_id",
    "new_state",
    "transition_type",
    "transition_basis",
    "post_state_emitted_at",
    "worker_final_verdict",
    "worker_first_missing_object_id",
    "guard_declarations",
}

REQUIRED_STATE_FIELDS = {
    "verdict",
    "missing_object_id",
    "blocker_family",
    "evidence_basis",
    "source_refs",
}

REQUIRED_TRANSITION_TYPES = [
    "same_session_circularity",
    "target_import_violation",
    "false_negative",
    "closure",
    "downgrade",
    "same_status_refinement",
    "repetition",
    "upgrade_without_closure",
    "new_item",
    "underdefined_item_identity",
]

FORBIDDEN_OVERCLAIMS = [
    r'"retroactive_convergence_proof_claimed"\s*:\s*true',
    r'"major_gu_claim_promoted"\s*:\s*true',
    r'"new_physics_claim"\s*:\s*true',
    r'"same_session_closure_claimed"\s*:\s*true',
    r'"false_negative_correction_claimed"\s*:\s*true',
    r'"target_import_closure_claimed"\s*:\s*true',
    r"\bold runs? (?:is|are|was|were|has been) retroactively proved convergent\b",
    r"\bGU physics progress (?:is|was|has been) proved\b",
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


class LoopTransitionRowEmissionGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_are_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_verdict_is_future_gate_not_retroactive_or_physics_claim(self) -> None:
        self.assertEqual(
            self.summary["verdict"],
            "CONDITIONAL_FUTURE_ROW_EMISSION_GATE_RETROACTIVE_CONVERGENCE_BLOCKED",
        )
        self.assertIs(self.summary["process_instrumentation_only"], True)
        self.assertIs(self.summary["retroactive_convergence_proof_claimed"], False)
        self.assertIs(self.summary["major_gu_claim_promoted"], False)
        self.assertIs(self.summary["new_physics_claim"], False)
        self.assertIs(self.summary["same_session_closure_claimed"], False)
        self.assertIs(self.summary["false_negative_correction_claimed"], False)
        self.assertIs(self.summary["target_import_closure_claimed"], False)
        for pattern in FORBIDDEN_OVERCLAIMS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden overclaim matched: {pattern}",
            )

    def test_source_receipts_match_required_read_first_files(self) -> None:
        receipts = self.summary["derived_directly_from_sources"]
        self.assertEqual(receipts, REQUIRED_SOURCE_RECEIPTS)
        for path in receipts.values():
            self.assertTrue((REPO_ROOT / path).exists(), path)

    def test_cycle2_backfill_limits_are_carried_forward(self) -> None:
        decision = self.summary["cycle2_backfill_decision"]
        counts = decision["classification_counts"]
        self.assertEqual(counts["classifiable"], 4)
        self.assertEqual(counts["ambiguous"], 1)
        self.assertEqual(counts["blocked_missing_pre_state"], 5)
        self.assertEqual(counts["same_status_refinement"], 4)
        for key in [
            "closure",
            "repetition",
            "downgrade",
            "false_negative",
            "same_session_circularity",
        ]:
            self.assertEqual(counts[key], 0, key)
        self.assertEqual(
            decision["decision"],
            "partial_backfill_supports_blocker_sharpening_only",
        )
        self.assertIn("ambiguous_phi_obs_item_identity", decision["remaining_blocked"])

    def test_future_row_emission_rule_has_pre_and_post_contracts(self) -> None:
        rule = self.summary["future_row_emission_rule"]
        self.assertEqual(rule["gate_id"], "LoopStateTransitionRowEmissionGate_V1")
        self.assertEqual(rule["pre_row_emitter"], "coordinator_before_worker_assignment")
        self.assertEqual(rule["post_row_emitter"], "worker_or_coordinator_after_worker_artifact")
        self.assertTrue(
            REQUIRED_PRE_ROW_FIELDS.issubset(set(rule["required_pre_row_fields"])),
            sorted(REQUIRED_PRE_ROW_FIELDS - set(rule["required_pre_row_fields"])),
        )
        self.assertTrue(
            REQUIRED_POST_ROW_FIELDS.issubset(set(rule["required_post_row_fields"])),
            sorted(REQUIRED_POST_ROW_FIELDS - set(rule["required_post_row_fields"])),
        )
        self.assertTrue(
            REQUIRED_STATE_FIELDS.issubset(set(rule["required_state_fields"])),
            sorted(REQUIRED_STATE_FIELDS - set(rule["required_state_fields"])),
        )
        for locked in ["row_id", "item_id", "previous_state", "pre_state_locked_at"]:
            self.assertIn(locked, rule["pre_row_immutable_fields"])

    def test_required_guards_are_machine_readable(self) -> None:
        guards = self.summary["future_row_emission_rule"]["required_guard_fields"]
        self.assertIn("same_session_guard", guards)
        self.assertIn("target_import_guard", guards)
        self.assertIn("guard_declarations", guards)
        for field in [
            "flag_raised_session_id",
            "flag_closed_session_id",
            "external_verification_id",
            "later_session_verification_id",
            "same_session_closure_attempted",
        ]:
            self.assertIn(field, guards["same_session_guard"])
        self.assertIn("target_import_detected", guards["target_import_guard"])
        self.assertIn("required_object_already_present", guards["guard_declarations"])

    def test_classifier_audit_precedence_and_counts_are_complete(self) -> None:
        classifier = self.summary["classifier_audit"]
        self.assertIs(classifier["required_before_synthesis"], True)
        self.assertIs(classifier["worker_self_classification_allowed"], False)
        self.assertEqual(classifier["transition_types_required"], REQUIRED_TRANSITION_TYPES)
        self.assertEqual(classifier["classifier_precedence"], REQUIRED_TRANSITION_TYPES)
        self.assertEqual(classifier["counts_required"], REQUIRED_TRANSITION_TYPES)
        self.assertLess(
            classifier["classifier_precedence"].index("same_session_circularity"),
            classifier["classifier_precedence"].index("closure"),
        )
        self.assertLess(
            classifier["classifier_precedence"].index("target_import_violation"),
            classifier["classifier_precedence"].index("closure"),
        )
        self.assertLess(
            classifier["classifier_precedence"].index("false_negative"),
            classifier["classifier_precedence"].index("closure"),
        )
        self.assertIn("underdefined_item_identity", classifier["closure_guard_failures"])

    def test_acceptance_gate_blocks_synthesis_until_rows_and_audit_exist(self) -> None:
        gate = self.summary["acceptance_gate"]
        self.assertIs(gate["gate_pass_required_before_synthesis"], True)
        requirements = set(gate["requirements"])
        for requirement in [
            "one_pre_row_per_lane_before_worker_assignment",
            "one_post_row_per_lane_after_worker_completion",
            "post_row_identity_matches_pre_row_identity",
            "pre_row_locked_fields_not_overwritten",
            "classifier_audit_completed_before_synthesis",
            "process_metrics_reported_separately_from_gu_claims",
        ]:
            self.assertIn(requirement, requirements)
        synthesis_allowed_if = set(gate["synthesis_allowed_if"])
        for condition in [
            "pre_rows_count_equals_lane_count",
            "post_rows_count_equals_lane_count",
            "classifier_results_count_equals_lane_count",
            "all_identity_links_valid",
            "no_locked_pre_row_overwrite",
        ]:
            self.assertIn(condition, synthesis_allowed_if)

    def test_first_obstruction_and_next_object_are_precise(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "MISSING_PROSPECTIVE_PRE_TRANSITION_ROWS")
        self.assertIn("future pre/post rows", obstruction["why_first"])
        for component in [
            "pre_state_rows_before_worker_assignment",
            "immutable_row_identity",
            "row_linked_same_session_flags",
            "row_linked_target_import_guards",
            "classifier_results_before_synthesis",
        ]:
            self.assertIn(component, obstruction["missing_components"])

        next_object = self.summary["constructive_next_object"]
        self.assertEqual(next_object["id"], "CycleLocalTransitionLedger_3_1_5_4_V1")
        self.assertIs(next_object["synthesis_allowed_boolean_required"], True)
        self.assertEqual(
            set(next_object["required_sections"]),
            {"pre_rows", "post_rows", "classifier_results", "acceptance_gate"},
        )

    def test_impact_and_next_step_are_process_only(self) -> None:
        impact = self.summary["impact_on_gu_process_claim"]
        self.assertIn("future runs", impact["process_gain"])
        self.assertEqual(impact["old_three_cycle_convergence_status"], "not_retroactively_proved")
        self.assertEqual(impact["physics_claim_status"], "no_new_physics_claim")
        self.assertIn("LoopStateTransitionRowEmissionGate_V1", impact["future_metrics_condition"])
        self.assertIn("classifier audit", self.summary["next_meaningful_step"])


def audit_summary() -> dict[str, Any]:
    text = read_artifact()
    summary = extract_summary(text)
    return {
        "document": str(ARTIFACT.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "gate_id": summary["future_row_emission_rule"]["gate_id"],
        "retroactive_convergence_proof_claimed": summary[
            "retroactive_convergence_proof_claimed"
        ],
        "cycle2_counts": summary["cycle2_backfill_decision"]["classification_counts"],
    }


def main(argv: list[str] | None = None) -> int:
    if argv and "--json" in argv:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            LoopTransitionRowEmissionGateAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
