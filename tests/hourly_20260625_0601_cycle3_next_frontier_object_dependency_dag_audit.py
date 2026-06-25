#!/usr/bin/env python3
"""Audit NextFrontierObjectDependencyDAGAfterHourly20260625_0601_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md"
)

EXPECTED_NEXT_OBJECTS = {
    "IG": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
    "DGU_VZ": "BosonicToDGU01SectorIdentityRule_V1",
    "RS": "ManualImageLevelRSFormulaDiagramAudit_V1",
    "QFT": "QFTAlternatePrimarySourceQueryBundle_V1",
    "Oxford": "OxfordPortalPowerPointFormulaFramePacket_V1",
    "Keating": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing next-frontier DAG JSON summary")
    return json.loads(match.group(1))


class NextFrontierObjectDependencyDAGAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "NextFrontierObjectDependencyDAGAfterHourly20260625_0601_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 3)
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["artifact_id"],
            "NextFrontierObjectDependencyDAGAfterHourly20260625_0601_V1",
        )
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle3_next_frontier_object_dependency_dag_audit.py",
        )

    def test_named_next_objects_for_all_required_lanes(self) -> None:
        next_objects = self.summary["next_objects"]
        self.assertEqual(set(next_objects), set(EXPECTED_NEXT_OBJECTS))
        for lane, object_id in EXPECTED_NEXT_OBJECTS.items():
            self.assertEqual(next_objects[lane]["object_id"], object_id)
            self.assertFalse(next_objects[lane]["proof_restart_allowed"])
            self.assertIn(object_id, self.text)

    def test_parallel_safe_set_contains_source_object_tasks(self) -> None:
        parallel_safe = set(self.summary["parallel_safe_next_objects"])
        self.assertEqual(parallel_safe, set(EXPECTED_NEXT_OBJECTS.values()))
        self.assertIn("Parallel-safe acquisition/query layer", self.text)

    def test_sequential_lanes_are_receipt_then_identity_then_restart(self) -> None:
        sequences = {row["id"]: row["steps"] for row in self.summary["sequential_lanes"]}
        generic = sequences["generic_family_receipt_sequence"]
        self.assertEqual(
            generic,
            [
                "source_or_formula_acquisition",
                "accepted_receipt_row",
                "family_identity_check",
                "proof_restart_readiness_classifier",
                "downstream_proof_replay",
            ],
        )
        self.assertIn("SourceModeQuotientPacket(K_b)", sequences["qft_sequence"])
        self.assertIn(
            "SourceForcedCodomainSelectorForK_IG_family_identity_check",
            sequences["ig_sequence"],
        )
        self.assertIn("ActualDGU01OperatorCertificateInstance_V1", sequences["dgu_vz_sequence"])
        self.assertIn("RS_family_identity_check", sequences["rs_sequence"])

    def test_proof_restart_is_globally_forbidden(self) -> None:
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertEqual(self.summary["accepted_family_receipts"], 0)
        self.assertEqual(self.summary["family_identity_checks_passed"], 0)
        forbidden = self.summary["forbidden_proof_restarts_until_upstream_gates_close"]
        self.assertGreaterEqual(len(forbidden), 6)
        for phrase in [
            "IG_theta_FLRW",
            "DGU_VZ_principal_symbol",
            "RS_symbol_K3_index",
            "QFT_finite_one_particle",
            "Oxford_Portal",
            "Keating_PullThatUpJamie",
        ]:
            self.assertTrue(any(phrase in item for item in forbidden), phrase)

    def test_material_change_to_next_goals(self) -> None:
        self.assertTrue(self.summary["material_change_to_next_goals"])
        self.assertIn("upstream source/formula receipt", self.summary["material_change_description"])
        next_computation = self.summary["next_computation"]
        self.assertEqual(next_computation["batch_type"], "six_lane_source_object_batch")
        self.assertFalse(next_computation["proof_restart_currently_allowed"])
        self.assertEqual(len(next_computation["goals"]), 6)
        self.assertIn("material change to next goals", self.text.lower())

    def test_dependency_edges_include_family_gates(self) -> None:
        edges = {tuple(edge) for edge in self.summary["dependency_edges"]}
        self.assertIn(
            (
                "QFTAlternatePrimarySourceQueryBundle_V1",
                "AcceptedPrimarySourceReceiptForQFTPFinB",
            ),
            edges,
        )
        self.assertIn(
            (
                "AcceptedPrimarySourceReceiptForQFTPFinB",
                "SourceModeQuotientPacket(K_b)",
            ),
            edges,
        )
        self.assertIn(("accepted_receipt_row", "family_identity_check"), edges)
        self.assertIn(("family_identity_check", "proof_restart_readiness_classifier"), edges)

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Source Facts",
            "## 3. Strongest Positive Route Through The DAG",
            "## 4. First Obstruction",
            "## 5. Impact If Closed",
            "## 6. Falsification/Demotion Condition",
            "## 7. Next Computation",
            "## 8. JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
