#!/usr/bin/env python3
"""Audit ProofRestartReadinessClassifierAfter1602_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ROUTES = {
    "PTUJ",
    "IG",
    "DGU_VZ",
    "RS",
    "QFT",
    "major_GU_reconstruction",
    "global_no_go",
}


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ProofRestartReadinessClassifier1602Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact_id"], "ProofRestartReadinessClassifierAfter1602_V1"
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["verdict_class"], "blocked")

    def test_global_restart_flags(self) -> None:
        self.assertEqual(self.summary["routes_ready_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_route_rows_are_complete_and_none_ready(self) -> None:
        route_rows = self.summary["route_rows"]
        self.assertEqual(len(route_rows), 7)
        self.assertEqual({row["route"] for row in route_rows}, EXPECTED_ROUTES)
        for row in route_rows:
            with self.subTest(route=row["route"]):
                self.assertIs(row["ready"], False)
                self.assertEqual(row["accepted_receipt_count"], 0)
                self.assertIs(row["accepted_receipt_present"], False)
                self.assertIs(row["family_identity_fields_present"], False)
                self.assertIs(row["route_specific_prerequisites_present"], False)
                self.assertIs(row["target_import_used"], False)
                self.assertTrue(row["first_blocker"])
                self.assertTrue(row["next_object"])

    def test_blocker_and_next_object_maps_cover_every_route(self) -> None:
        self.assertEqual(set(self.summary["first_blockers"].keys()), EXPECTED_ROUTES)
        self.assertEqual(set(self.summary["next_objects"].keys()), EXPECTED_ROUTES)
        for route in EXPECTED_ROUTES:
            with self.subTest(route=route):
                self.assertTrue(self.summary["first_blockers"][route])
                self.assertTrue(self.summary["next_objects"][route])

    def test_global_no_go_not_ready_or_promoted(self) -> None:
        global_row = next(
            row for row in self.summary["route_rows"] if row["route"] == "global_no_go"
        )
        self.assertIs(global_row["ready"], False)
        self.assertEqual(global_row["restart_decision"], "not_promoted")
        self.assertEqual(global_row["accepted_receipt_count"], 0)
        self.assertIs(global_row["promotion_allowed"], False)
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertIs(self.summary["promotion_firewall"]["global_no_go_promotion"], False)
        self.assertIs(self.summary["promotion_firewall"]["scoped_negative_as_global_no_go"], False)

    def test_receipt_count_sums_to_zero(self) -> None:
        self.assertEqual(
            sum(row["accepted_receipt_count"] for row in self.summary["route_rows"]),
            self.summary["accepted_receipt_count"],
        )
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_no_forbidden_ready_or_restart_flags(self) -> None:
        forbidden_patterns = [
            r'"ready"\s*:\s*true',
            r'"proof_restart_allowed"\s*:\s*true',
            r'"accepted_receipt_count"\s*:\s*[1-9]\d*',
            r'"routes_ready_count"\s*:\s*[1-9]\d*',
            r'"target_import_used"\s*:\s*true',
            r'"global_no_go_promoted"\s*:\s*true',
        ]
        for pattern in forbidden_patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.text))


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            ProofRestartReadinessClassifier1602Audit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
