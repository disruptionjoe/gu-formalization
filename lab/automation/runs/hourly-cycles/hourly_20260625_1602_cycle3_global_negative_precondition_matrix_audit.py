#!/usr/bin/env python3
"""Audit GlobalNegativePreconditionMatrixAfter1602_C3_L3_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle3-global-negative-precondition-matrix.md"
)

EXPECTED_ARTIFACT = "GlobalNegativePreconditionMatrixAfter1602_C3_L3_V1"
EXPECTED_ROUTES = {"PTUJ", "IG", "DGU/VZ", "RS", "QFT", "major GU"}
COUNT_CLASSIFICATIONS = {
    "source_absence": "source_absence_count",
    "underdefinition": "underdefined_count",
    "scoped_negative": "scoped_negative_count",
}


def extract_json_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing section 7 machine-readable JSON summary")
    return json.loads(match.group(1))


class GlobalNegativePreconditionAfter1602Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not ARTIFACT.exists():
            raise AssertionError(f"artifact missing: {ARTIFACT}")
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_json_summary(cls.text)

    def test_identity_and_required_booleans(self) -> None:
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT)
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1602")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 3)
        self.assertEqual(
            self.summary["verdict_class"], "blocked_global_negative_promotion"
        )
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertEqual(self.summary["complete_route_coverage_count"], 0)
        self.assertFalse(self.summary["target_import_used"])

    def test_every_route_row_has_classification_and_missing_preconditions(self) -> None:
        route_rows = self.summary["route_rows"]
        self.assertEqual({row["route"] for row in route_rows}, EXPECTED_ROUTES)
        allowed = set(COUNT_CLASSIFICATIONS) | {"structural_no_go"}
        for row in route_rows:
            self.assertIn(row["classification"], allowed, row["route"])
            self.assertIsInstance(row["missing_preconditions"], list, row["route"])
            self.assertGreater(len(row["missing_preconditions"]), 0, row["route"])
            self.assertFalse(row["global_no_go_promoted"], row["route"])
            self.assertFalse(row["complete_route_coverage"], row["route"])
            self.assertFalse(row["target_import_used"], row["route"])

    def test_counts_sum_sensibly(self) -> None:
        route_rows = self.summary["route_rows"]
        counted = {
            key: sum(1 for row in route_rows if row["classification"] == classification)
            for classification, key in COUNT_CLASSIFICATIONS.items()
        }
        for key, value in counted.items():
            self.assertEqual(self.summary[key], value, key)
        self.assertEqual(self.summary["structural_no_go_count"], 0)
        self.assertEqual(
            sum(counted.values()) + self.summary["structural_no_go_count"],
            len(route_rows),
        )

    def test_no_complete_route_coverage(self) -> None:
        self.assertEqual(self.summary["complete_route_coverage_count"], 0)
        self.assertTrue(
            all(not row["complete_route_coverage"] for row in self.summary["route_rows"])
        )

    def test_next_objects_are_explicit(self) -> None:
        next_objects = self.summary["next_objects"]
        self.assertIsInstance(next_objects, list)
        self.assertGreaterEqual(len(next_objects), len(EXPECTED_ROUTES))
        for obj in next_objects:
            self.assertIsInstance(obj, str)
            self.assertGreater(len(obj), 10)
        row_next_objects = {row["next_object"] for row in self.summary["route_rows"]}
        self.assertTrue(row_next_objects.issubset(set(next_objects)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
