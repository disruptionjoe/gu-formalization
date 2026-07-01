#!/usr/bin/env python3
"""Audit the 1802 C1/L5 QFT source-defined raw branch packet artifact."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1802-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid-packet.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1802"
EXPECTED_ARTIFACT_ID = (
    "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1802_C1_L5_V1"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1802-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid-packet.md"
)
EXPECTED_TARGET_PACKET = "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1"


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTSourceDefinedRawBranchPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_target(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["target_packet_id"], EXPECTED_TARGET_PACKET)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)

    def test_packet_not_admitted_and_no_schema_promotion(self) -> None:
        self.assertIs(self.summary["packet_admitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["schema_only_promoted"], False)

    def test_first_required_source_fields_remain_missing(self) -> None:
        self.assertIs(self.summary["source_defined_iota_b"], False)
        self.assertIs(self.summary["source_defined_typed_R_raw_b_O"], False)
        self.assertIn("iota_b", self.summary["missing_source_fields"])
        self.assertIn("typed_R_raw^b(O)", self.summary["missing_source_fields"])

        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["first_missing_field_set"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        self.assertEqual(
            obstruction["first_missing_fields"],
            ["iota_b", "typed_R_raw^b(O)"],
        )

    def test_downstream_gates_locked_unless_packet_admitted(self) -> None:
        packet_admitted = self.summary["packet_admitted"]
        quotient_allowed = self.summary["quotient_descent_allowed"]
        finite_allowed = self.summary["finite_extraction_allowed"]

        self.assertIs(quotient_allowed, False)
        self.assertIs(finite_allowed, False)
        self.assertTrue(packet_admitted or not quotient_allowed)
        self.assertTrue(packet_admitted or not finite_allowed)

        locks = self.summary["downstream_locks"]
        self.assertIs(locks["quotient_descent_allowed"], False)
        self.assertIs(locks["finite_extraction_allowed"], False)
        self.assertIs(locks["proof_restart_allowed"], False)

    def test_underdefined_artifact_has_missing_source_fields(self) -> None:
        self.assertEqual(self.summary["verdict_class"], "underdefined")
        self.assertGreater(len(self.summary["missing_source_fields"]), 0)
        self.assertEqual(
            set(self.summary["missing_source_fields"]),
            set(self.summary["required_source_fields"]),
        )

    def test_no_forbidden_source_selectors_were_used(self) -> None:
        screen = self.summary["non_import_screen"]
        self.assertIs(screen["target_import_used_as_source_selector"], False)
        self.assertEqual(screen["forbidden_selectors_used"], [])
        for selector in [
            "quotient_descent",
            "finite_extraction",
            "rho_AB",
            "Bell",
            "CHSH",
        ]:
            self.assertIn(selector, screen["forbidden_selectors"])

        self.assertIs(self.summary["rho_AB_selector_allowed"], False)
        self.assertIs(self.summary["Bell_selector_allowed"], False)
        self.assertIs(self.summary["CHSH_selector_allowed"], False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
