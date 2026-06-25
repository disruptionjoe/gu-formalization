#!/usr/bin/env python3
"""Audit ProofRestartReadinessClassifierAfter1503_V1."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ROUTES = {"PTUJ", "IG", "DGU_VZ", "RS", "QFT"}

FIREWALL_TOKENS = [
    "PTUJ_formula_packet",
    "IG_selector",
    "DGU_VZ_replay",
    "RS_generation_index_route",
    "QFT_rho_AB_CHSH_Bell",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 6\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ProofRestartReadinessClassifier1503Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertIn('artifact_id: "ProofRestartReadinessClassifierAfter1503_V1"', self.text)
        self.assertIn('run_id: "hourly-20260625-1503"', self.text)
        self.assertIn("cycle: 3", self.text)
        self.assertIn("lane: 1", self.text)
        self.assertEqual(self.summary["artifact_id"], "ProofRestartReadinessClassifierAfter1503_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)

    def test_global_restart_decision(self) -> None:
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["routes_ready_count"], 0)
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_all_five_route_rows_present_and_blocked(self) -> None:
        table_match = re.search(
            r"## 2\. Route table\.\s*(.*?)\s*## 3\.",
            self.text,
            flags=re.DOTALL,
        )
        self.assertIsNotNone(table_match)
        route_rows = re.findall(
            r"^\| (PTUJ|IG|DGU/VZ|RS|QFT) \|",
            table_match.group(1),
            flags=re.MULTILINE,
        )
        self.assertEqual(route_rows, ["PTUJ", "IG", "DGU/VZ", "RS", "QFT"])
        self.assertEqual(len(self.summary["routes"]), 5)
        self.assertEqual({route["route"] for route in self.summary["routes"]}, EXPECTED_ROUTES)
        for route in self.summary["routes"]:
            with self.subTest(route=route["route"]):
                self.assertEqual(route["accepted_receipt_count"], 0)
                self.assertIs(route["accepted_source_receipt_or_object"], False)
                self.assertIs(route["family_identity_passed"], False)
                self.assertIs(route["route_specific_prerequisites_met"], False)
                self.assertIs(route["proof_restart_allowed"], False)
                self.assertTrue(route["first_exact_obstruction"])

    def test_route_receipts_sum_to_zero(self) -> None:
        self.assertEqual(
            sum(route["accepted_receipt_count"] for route in self.summary["routes"]),
            self.summary["accepted_receipt_count"],
        )
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_firewall_tokens_are_present_and_blocked(self) -> None:
        self.assertEqual(set(self.summary["firewalls"].keys()), set(FIREWALL_TOKENS))
        for token in FIREWALL_TOKENS:
            with self.subTest(token=token):
                self.assertIn(token, self.text)
                self.assertEqual(self.summary["firewalls"][token], "blocked")

    def test_specific_firewall_surface_terms_present(self) -> None:
        required_terms = [
            "PTUJ formula packet",
            "IG selector",
            "DGU/VZ replay",
            "RS generation/index route",
            "rho_AB",
            "CHSH",
            "Bell",
        ]
        for term in required_terms:
            with self.subTest(term=term):
                self.assertIn(term, self.text)

    def test_required_1503_facts_recorded(self) -> None:
        self.assertEqual(self.summary["cycle_1_commit"], "b1a2cc5")
        self.assertEqual(self.summary["cycle_2_commit"], "74090c4")
        required_obstructions = {
            "PTUJ": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object",
            "IG": "VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1",
            "DGU_VZ": "missing_source_emitted_actual_DGU_01_sector_identity_packet_with_sector_rule",
            "RS": "stable_official_video_locator_exists_but_no_captured_and_checksummed_frame_slide_crop_OCR_or_visual_transcription_exists_for_00_32_07_00_37_41",
            "QFT": "SourceObservedRawFieldBranchPacketForRRawBO_V1_missing_source_defined_iota_b_and_typed_R_raw_b_O",
        }
        for route in self.summary["routes"]:
            self.assertIn(required_obstructions[route["route"]], route["first_exact_obstruction"])

    def test_no_forbidden_promotion_flags(self) -> None:
        forbidden_patterns = [
            r'"proof_restart_allowed"\s*:\s*true',
            r'"accepted_receipt_count"\s*:\s*[1-9]\d*',
            r'"routes_ready_count"\s*:\s*[1-9]\d*',
            r'"global_no_go_promoted"\s*:\s*true',
            r"\bglobal\s+(GU|physics)\s+no-go\b",
        ]
        for pattern in forbidden_patterns:
            self.assertIsNone(
                re.search(pattern, self.text, flags=re.IGNORECASE),
                f"forbidden promotion matched: {pattern}",
            )


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            ProofRestartReadinessClassifier1503Audit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
