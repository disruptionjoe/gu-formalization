#!/usr/bin/env python3
"""Audit the 1802 C3/L5 next-frontier dependency DAG."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle3-next-frontier-dependency-dag.md"
)
ARTIFACT = REPO_ROOT / ARTIFACT_PATH


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class NextFrontierDependencyDag1802Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_artifact_path(self) -> None:
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["artifact_path"], ARTIFACT_PATH)

    def test_candidate_bank_size_and_unique_count(self) -> None:
        candidates = self.summary["quality_candidates"]
        self.assertGreaterEqual(self.summary["quality_candidates_claimed"], 18)
        self.assertEqual(self.summary["quality_candidates_claimed"], len(candidates))
        self.assertEqual(len(candidates), len(set(candidates)))

    def test_immediate_parallel_safe_lanes_exactly_five(self) -> None:
        lanes = self.summary["immediate_parallel_safe_lanes"]
        self.assertEqual(len(lanes), 5)
        self.assertEqual(
            lanes,
            [lane["id"] for lane in self.summary["recommended_next_five"]],
        )
        self.assertEqual(
            sorted(lane["route_family"] for lane in self.summary["recommended_next_five"]),
            ["DGU", "IG", "PTUJ", "QFT", "RS"],
        )

    def test_no_downstream_replay_zero_receipts_and_no_import(self) -> None:
        self.assertIs(self.summary["no_downstream_replay_in_recommended_lanes"], True)
        self.assertIs(self.summary["downstream_replay_allowed"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)

        by_route = self.summary["accepted_receipt_count_by_route"]
        self.assertEqual(set(by_route), {"PTUJ", "IG", "DGU", "RS", "QFT"})
        self.assertTrue(all(count == 0 for count in by_route.values()))

    def test_recommended_next_five_names_required_frontier_objects(self) -> None:
        haystack = json.dumps(self.summary["recommended_next_five"])
        required_fragments = [
            "PTUJ",
            "IG_PRODUCT_B",
            "ProductB",
            "DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT",
            "sector rule plus same-operator",
            "RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE",
            "capture route",
            "QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT",
            "iota_b",
            "R_raw",
        ]
        for fragment in required_fragments:
            self.assertIn(fragment, haystack)

    def test_sequential_deferred_has_real_dependencies(self) -> None:
        sequential = self.summary["sequential_deferred"]
        self.assertGreaterEqual(len(sequential), 5)
        for row in sequential:
            self.assertTrue(row["id"])
            self.assertTrue(row["wait_for"])
            self.assertTrue(row["reason"])

    def test_anti_overlap_and_guard_contracts(self) -> None:
        checks = {check["check"]: check for check in self.summary["anti_overlap_checks"]}
        self.assertIn("no_downstream_replay_in_recommended_lanes", checks)
        self.assertTrue(all(check["passed"] for check in checks.values()))
        self.assertIn(
            "GLOBAL_NO_RECEIPT_NO_PROOF_RESTART_FIREWALL",
            self.summary["demoted_guard_lanes"],
        )
        self.assertIn(
            "QFT_FINITE_EXTRACTION_RHO_AB_BELL_CHSH_FIREWALL",
            self.summary["demoted_guard_lanes"],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
