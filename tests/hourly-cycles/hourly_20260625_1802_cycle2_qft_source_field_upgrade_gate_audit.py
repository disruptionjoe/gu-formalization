#!/usr/bin/env python3
"""Audit the 1802 C2/L5 QFT source field upgrade gate artifact."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    "explorations/hourly-20260625-1802-cycle2-qft-source-field-upgrade-gate.md"
)
ARTIFACT = REPO_ROOT / ARTIFACT_PATH


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTSourceFieldUpgradeGateAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity(self) -> None:
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1802")
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["artifact_path"], ARTIFACT_PATH)

    def test_no_schema_or_downstream_upgrade(self) -> None:
        self.assertIs(self.summary["schema_only_upgrade_allowed"], False)
        self.assertIs(self.summary["downstream_selector_upgrade_allowed"], False)
        for candidate in self.summary["upgrade_candidates"]:
            self.assertIs(candidate["upgrade_allowed"], False)

    def test_first_source_fields_not_defined(self) -> None:
        self.assertIs(self.summary["source_defined_iota_b"], False)
        self.assertIs(self.summary["source_defined_typed_R_raw_b_O"], False)
        self.assertEqual(
            self.summary["first_obstruction"]["id"],
            "source_defined_iota_b_and_typed_R_raw_b_O_absent",
        )

    def test_packet_and_receipts_not_admitted(self) -> None:
        self.assertIs(self.summary["packet_admitted"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)

    def test_downstream_locks(self) -> None:
        self.assertIs(self.summary["quotient_descent_allowed"], False)
        self.assertIs(self.summary["finite_extraction_allowed"], False)
        self.assertIs(self.summary["rho_AB_selector_allowed"], False)
        self.assertIs(self.summary["Bell_selector_allowed"], False)
        self.assertIs(self.summary["CHSH_selector_allowed"], False)
        self.assertIs(self.summary["proof_restart_allowed"], False)

    def test_next_object_names_source_iota_and_typed_raw(self) -> None:
        next_object = self.summary["next_object"]
        self.assertEqual(
            next_object["id"],
            "QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1",
        )
        self.assertIn("source-defined iota_b", next_object["names"])
        self.assertIn("typed R_raw^b(O)", next_object["names"])
        self.assertEqual(
            next_object["minimum_acceptance_rows"],
            [
                "source_definition:iota_b",
                "source_definition:typed_R_raw^b(O)",
            ],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
