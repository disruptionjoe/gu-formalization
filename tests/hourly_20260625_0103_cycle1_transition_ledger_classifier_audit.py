#!/usr/bin/env python3
"""Audit the completed cycle-1 transition ledger classifier gate."""

from __future__ import annotations

import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle1-transition-ledger-classifier-gate.md"
)
LEDGER = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0103-cycle-local-transition-ledger.json"
)

LOCKED_IDENTITY_FIELDS = {
    "row_id",
    "item_id",
    "session_id",
    "cycle_index",
    "worker_id",
    "owned_artifact_path",
    "owned_audit_path",
}

REQUIRED_PRE_ROW_FIELDS = {
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
    "false_negative_guard",
}

REQUIRED_POST_ROW_FIELDS = {
    "row_phase",
    "row_id",
    "item_id",
    "session_id",
    "cycle_index",
    "worker_id",
    "owned_artifact_path",
    "owned_audit_path",
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

CLASSIFIER_PRECEDENCE = [
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

FORBIDDEN_OVERCLAIM_PATTERNS = [
    r'"major_gu_claim_promoted"\s*:\s*true',
    r'"new_physics_claim"\s*:\s*true',
    r'"retroactive_convergence_proof_claimed"\s*:\s*true',
    r'"gu_or_physics_closure_claimed"\s*:\s*true',
    r"\bproves GU\b",
    r"\bderives new physics\b",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing required file: {path}") from exc


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{path} is not valid JSON: {exc}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing fenced JSON summary after section 8")
    return json.loads(match.group(1))


def assert_fields(test: unittest.TestCase, obj: dict[str, Any], fields: set[str]) -> None:
    missing = fields - set(obj)
    test.assertFalse(missing, f"missing fields: {sorted(missing)}")


class CycleLocalTransitionLedgerClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_text(ARTIFACT)
        cls.summary = extract_summary(cls.text)
        cls.ledger = load_json(LEDGER)

    def test_summary_is_process_only_completed_cycle1_gate(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "CycleLocalTransitionLedger_3_1_5_4_V1_classifier_gate",
        )
        self.assertEqual(self.summary["verdict"], "conditional")
        self.assertIs(self.summary["process_only"], True)
        self.assertIs(self.summary["major_gu_claim_promoted"], False)
        self.assertIs(self.summary["new_physics_claim"], False)
        self.assertIs(self.summary["retroactive_convergence_proof_claimed"], False)
        self.assertIs(self.summary["gu_or_physics_closure_claimed"], False)
        self.assertIs(self.summary["process_gate_closed_for_cycle1"], True)
        self.assertIs(self.summary["synthesis_allowed_after_classifier_results"], True)

    def test_no_textual_or_json_overclaims(self) -> None:
        for pattern in FORBIDDEN_OVERCLAIM_PATTERNS:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden overclaim matched: {pattern}",
            )

    def test_summary_counts_and_precedence_are_complete(self) -> None:
        current = self.summary["current_stage_requirements"]
        self.assertEqual(current["required_pre_rows"], 5)
        self.assertEqual(current["required_post_rows"], 5)
        self.assertEqual(current["required_classifier_results"], 5)
        self.assertIs(current["synthesis_allowed"], True)
        self.assertEqual(self.summary["classifier_precedence"], CLASSIFIER_PRECEDENCE)
        gate = self.summary["acceptance_gate_after_workers_return"]
        self.assertEqual(gate["required_pre_rows"], 5)
        self.assertEqual(gate["required_post_rows"], 5)
        self.assertEqual(gate["required_classifier_results"], 5)
        self.assertIs(gate["process_metrics_separated_from_gu_claims"], True)

    def test_ledger_completed_shape(self) -> None:
        ledger = self.ledger
        self.assertEqual(ledger["ledger_version"], "CycleLocalTransitionLedger_3_1_5_4_V1")
        self.assertEqual(ledger["run_id"], "hourly-20260625-0103")
        self.assertEqual(ledger["cycle_index"], 1)
        self.assertIs(ledger["synthesis_allowed"], True)
        self.assertEqual(len(ledger["pre_rows"]), 5)
        self.assertEqual(len(ledger["post_rows"]), 5)
        self.assertEqual(len(ledger["classifier_results"]), 5)
        gate = ledger["acceptance_gate"]
        self.assertEqual(gate["status"], "passed")
        self.assertIs(gate["identity_links_valid"], True)
        self.assertIs(gate["locked_pre_rows_overwritten"], False)
        self.assertIs(gate["process_metrics_separated_from_gu_claims"], True)

    def test_pre_rows_have_locked_identity_state_and_guards(self) -> None:
        row_ids: set[str] = set()
        for row in self.ledger["pre_rows"]:
            assert_fields(self, row, REQUIRED_PRE_ROW_FIELDS)
            self.assertEqual(row["row_phase"], "pre")
            self.assertEqual(row["session_id"], "hourly-20260625-0103")
            self.assertEqual(row["cycle_index"], 1)
            self.assertEqual(row["pre_state_locked_by"], "coordinator")
            self.assertNotIn(row["row_id"], row_ids)
            row_ids.add(row["row_id"])
            assert_fields(self, row["previous_state"], REQUIRED_STATE_FIELDS)
            self.assertIsInstance(row["previous_state"]["source_refs"], list)
            self.assertIs(row["same_session_guard"]["same_session_closure_attempted"], False)
            self.assertIs(row["target_import_guard"]["target_import_detected"], False)
            self.assertIs(row["false_negative_guard"]["required_object_already_present"], False)
        self.assertEqual(len(row_ids), 5)

    def test_post_rows_match_locked_pre_row_identity(self) -> None:
        pre_by_row = {row["row_id"]: row for row in self.ledger["pre_rows"]}
        post_by_row = {row["row_id"]: row for row in self.ledger["post_rows"]}
        self.assertEqual(set(pre_by_row), set(post_by_row))
        for row_id, post in post_by_row.items():
            assert_fields(self, post, REQUIRED_POST_ROW_FIELDS)
            pre = pre_by_row[row_id]
            for field in LOCKED_IDENTITY_FIELDS:
                self.assertEqual(post[field], pre[field], f"{row_id}:{field}")
            assert_fields(self, post["new_state"], REQUIRED_STATE_FIELDS)
            self.assertFalse(post["guard_declarations"]["same_session_closure_attempted"])
            self.assertFalse(post["guard_declarations"]["target_import_detected"])
            self.assertFalse(post["guard_declarations"]["required_object_already_present"])

    def test_owned_paths_are_disjoint_and_existing_after_integration(self) -> None:
        artifact_paths = [row["owned_artifact_path"] for row in self.ledger["pre_rows"]]
        audit_paths = [row["owned_audit_path"] for row in self.ledger["pre_rows"]]
        self.assertEqual(len(set(artifact_paths)), 5)
        self.assertEqual(len(set(audit_paths)), 5)
        for rel_path in artifact_paths + audit_paths:
            self.assertTrue((REPO_ROOT / rel_path).exists(), rel_path)

    def test_classifier_results_apply_precedence_and_counts(self) -> None:
        results = self.ledger["classifier_results"]
        row_ids = {row["row_id"] for row in self.ledger["pre_rows"]}
        self.assertEqual({result["row_id"] for result in results}, row_ids)
        counts = Counter(result["selected_transition_type"] for result in results)
        self.assertEqual(counts["same_status_refinement"], 4)
        self.assertEqual(counts["closure"], 1)
        for transition in [
            "same_session_circularity",
            "target_import_violation",
            "false_negative",
            "downgrade",
            "repetition",
            "upgrade_without_closure",
            "new_item",
            "underdefined_item_identity",
        ]:
            self.assertEqual(counts[transition], 0)
        for result in results:
            self.assertTrue(result["precedence_applied"])
            self.assertEqual(result["guard_failures"], [])
            self.assertIn(result["selected_transition_type"], CLASSIFIER_PRECEDENCE)

    def test_acceptance_gate_counts_match_classifier_results(self) -> None:
        gate = self.ledger["acceptance_gate"]
        counts = gate["classification_counts"]
        self.assertEqual(counts["same_status_refinement"], 4)
        self.assertEqual(counts["closure"], 1)
        self.assertEqual(sum(counts.values()), 5)
        self.assertEqual(gate["pre_rows_count"], 5)
        self.assertEqual(gate["post_rows_count"], 5)
        self.assertEqual(gate["classifier_results_count"], 5)
        self.assertIs(gate["synthesis_allowed"], True)

    def test_next_obstruction_is_cycle2_pre_rows(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], "CYCLE2_PRE_ROWS_NOT_YET_EMITTED")
        self.assertEqual(
            self.summary["constructive_next_object"]["id"],
            "CycleLocalTransitionLedger_3_1_5_4_V1.cycle2_pre_rows",
        )
        self.assertIn("cycle2 pre_rows", self.summary["next_meaningful_step"])


def audit_summary() -> dict[str, Any]:
    text = read_text(ARTIFACT)
    summary = extract_summary(text)
    ledger = load_json(LEDGER)
    return {
        "artifact": str(ARTIFACT.relative_to(REPO_ROOT)),
        "ledger": str(LEDGER.relative_to(REPO_ROOT)),
        "verdict": summary["verdict"],
        "pre_rows": len(ledger.get("pre_rows", [])),
        "post_rows": len(ledger.get("post_rows", [])),
        "classifier_results": len(ledger.get("classifier_results", [])),
        "synthesis_allowed": ledger.get("synthesis_allowed"),
    }


def main(argv: list[str] | None = None) -> int:
    if argv and "--json" in argv:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(
        CycleLocalTransitionLedgerClassifierAudit
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
