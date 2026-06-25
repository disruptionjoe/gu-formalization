"""Audit NextFrontierDependencyDagAfter1602_C3_L5_V1."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-1602-cycle3-next-frontier-dependency-dag.md"
)

EXPECTED_ARTIFACT_ID = "NextFrontierDependencyDagAfter1602_C3_L5_V1"
EXPECTED_RUN_ID = "hourly-20260625-1602"
EXPECTED_ROUTE_FAMILIES = {"PTUJ", "IG", "DGU", "RS", "QFT"}


def read_artifact() -> str:
    try:
        return ARTIFACT.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {ARTIFACT}") from exc


def extract_summary(text: str) -> dict:
    match = re.search(
        r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class NextFrontierDependencyDagAfter1602Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_artifact()
        cls.summary = extract_summary(cls.text)

    def test_identity_and_no_receipt_firewall(self) -> None:
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["target_import_used"])

    def test_quality_bank_and_next_five_shape(self) -> None:
        self.assertGreaterEqual(self.summary["quality_candidates_claimed"], 5)
        self.assertGreaterEqual(len(self.summary["quality_candidates"]), 5)
        self.assertEqual(
            self.summary["quality_candidates_claimed"],
            len(self.summary["quality_candidates"]),
        )

        recommended = self.summary["recommended_next_five"]
        self.assertEqual(len(recommended), 5)
        self.assertEqual(
            {lane["route_family"] for lane in recommended},
            EXPECTED_ROUTE_FAMILIES,
        )
        for lane in recommended:
            self.assertTrue(lane["id"])
            self.assertTrue(lane["produce"])
            self.assertTrue(lane["must_not_do"])

    def test_recommended_lanes_have_disjoint_owned_surfaces(self) -> None:
        descriptions = [
            lane["owned_surface_description"]
            for lane in self.summary["recommended_next_five"]
        ]
        self.assertEqual(len(descriptions), 5)
        self.assertEqual(len(descriptions), len(set(descriptions)))

        joined = "\n".join(descriptions)
        for expected_term in [
            "TzSEvmqxu48",
            "D7 finite representation",
            "Oxford bosonic anchors",
            "fBozSSLxFvI",
            "QFT source branch fields",
        ]:
            self.assertIn(expected_term, joined)

    def test_sequential_deferred_is_nonempty_and_not_recommended(self) -> None:
        deferred = self.summary["sequential_deferred"]
        self.assertGreater(len(deferred), 0)
        recommended_ids = {lane["id"] for lane in self.summary["recommended_next_five"]}
        for lane in deferred:
            self.assertTrue(lane["id"])
            self.assertTrue(lane["wait_for"])
            self.assertTrue(lane["reason"])
            self.assertNotIn(lane["id"], recommended_ids)

    def test_dependency_edges_are_explicit(self) -> None:
        edges = self.summary["dependency_edges"]
        self.assertGreater(len(edges), 0)
        for edge in edges:
            self.assertTrue(edge["from"])
            self.assertTrue(edge["to"])
            self.assertTrue(edge["kind"])
            self.assertNotEqual(edge["from"], edge["to"])

        edge_pairs = {(edge["from"], edge["to"]) for edge in edges}
        self.assertIn(
            (
                "PTUJ_ACCEPTED_SOURCE_OBJECT_BRANCH_RECEIPT",
                "PTUJ_FORMULA_VISIBILITY_AUDIT_AFTER_RECEIPT",
            ),
            edge_pairs,
        )
        self.assertIn(
            (
                "QFT_SOURCE_DEFINED_RAW_BRANCH_LOCAL_GAUGE_GROUPOID_PACKET_NON_IMPORT",
                "QFT_GAUGE_ORBIT_GENERATOR_RESTRICTION_TEST",
            ),
            edge_pairs,
        )

    def test_anti_overlap_checks_pass(self) -> None:
        checks = self.summary["anti_overlap_checks"]
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertTrue(check["check"])
            self.assertIs(check["passed"], True)
            self.assertTrue(check["details"])


if __name__ == "__main__":
    unittest.main()
