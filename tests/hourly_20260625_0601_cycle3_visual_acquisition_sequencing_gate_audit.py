#!/usr/bin/env python3
"""Audit VisualAcquisitionSequencingGate_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md"
)


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing VisualAcquisitionSequencingGate_V1 JSON")
    return json.loads(match.group(1))


class VisualAcquisitionSequencingGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "VisualAcquisitionSequencingGate_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0601")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)
        identity = self.summary["artifact_identity"]
        self.assertEqual(identity["artifact_id"], "VisualAcquisitionSequencingGate_V1")
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0601_cycle3_visual_acquisition_sequencing_gate_audit.py",
        )

    def test_required_packets_and_priority(self) -> None:
        self.assertEqual(
            self.summary["priority_packet"],
            "OxfordPortalPowerPointFormulaFramePacket_V1",
        )
        self.assertEqual(
            self.summary["secondary_packet"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )
        packet_ids = {packet["packet_id"] for packet in self.summary["packets"]}
        self.assertIn("OxfordPortalPowerPointFormulaFramePacket_V1", packet_ids)
        self.assertIn(
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
            packet_ids,
        )

    def test_sequence_and_parallel_rules(self) -> None:
        decision = self.summary["sequencing_decision"]
        self.assertEqual(
            decision["sequential_first"],
            ["OxfordPortalPowerPointFormulaFramePacket_V1"],
        )
        self.assertIn(
            "Keating Pull That Up Jamie raw asset retrieval",
            decision["parallel_allowed"],
        )
        self.assertIn("proof restart", decision["parallel_forbidden"])
        self.assertIn("claim promotion", decision["parallel_forbidden"])
        self.assertEqual(
            decision["second_acceptance_packet"],
            "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
        )

    def test_ordered_sequence_rules(self) -> None:
        rules = self.summary["sequence_rules"]
        for required in [
            "locator_before_capture",
            "capture_before_transcription",
            "transcription_before_family_identity",
            "provenance_before_acceptance",
            "target_import_cleanliness_before_acceptance",
            "family_identity_before_accepted_routing",
            "accepted_receipt_before_proof_restart",
        ]:
            self.assertTrue(rules[required])

    def test_no_receipts_and_no_proof_restart(self) -> None:
        self.assertTrue(self.summary["source_acquisition_only"])
        self.assertEqual(self.summary["accepted_visual_formula_receipt_count"], 0)
        self.assertEqual(self.summary["accepted_visual_formula_receipts"], [])
        self.assertFalse(self.summary["proof_restart"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])

    def test_packet_details(self) -> None:
        oxford = next(
            packet
            for packet in self.summary["packets"]
            if packet["packet_id"] == "OxfordPortalPowerPointFormulaFramePacket_V1"
        )
        self.assertEqual(oxford["priority"], 1)
        self.assertEqual(oxford["next_run_mode"], "sequential_priority_packet")
        self.assertEqual(len(oxford["required_timestamps"]), 5)
        self.assertIn("DGU_VZ", oxford["families_affected"])
        self.assertFalse(oxford["accepted_for_routing"])

        keating = next(
            packet
            for packet in self.summary["packets"]
            if packet["packet_id"]
            == "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1"
        )
        self.assertEqual(keating["priority"], 2)
        self.assertEqual(
            keating["next_run_mode"],
            "parallel_raw_retrieval_only_then_sequential_identity",
        )
        self.assertIn(
            "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
            keating["required_objects"],
        )
        self.assertEqual(
            keating["required_identity_object"],
            "SourceForcedCodomainSelectorForK_IG",
        )
        self.assertFalse(keating["accepted_for_routing"])

    def test_required_sections_present(self) -> None:
        for heading in [
            "## 1. Verdict",
            "## 2. Source Facts",
            "## 3. Strongest Sequencing Attempt",
            "## 4. First Obstruction",
            "## 5. Impact If Closed",
            "## 6. Falsification/Demotion Condition",
            "## 7. Next Acquisition/Computation",
            "## 8. JSON Summary",
        ]:
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
