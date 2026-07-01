#!/usr/bin/env python3
"""Audit the 1702 C2/L5 QFT source-field locator classification."""

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
    / "hourly-20260625-1702-cycle2-qft-source-field-locator-classification.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_ARTIFACT_ID = "QFTSourceFieldLocatorClassificationForIotaRRawG_1702_C2_L5_V1"
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle2-qft-source-field-locator-classification.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle2_qft_source_field_locator_classification_audit.py"
)
REQUIRED_LOCATOR_FIELDS = {
    "b",
    "iota_b",
    "U_b(O)",
    "R_raw^b(O)",
    "G_b(O)",
    "actions",
    "restrictions",
    "non_import_screen",
}


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTSourceFieldLocatorClassificationAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(
            self.summary["target_packet_id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_required_locator_rows_are_schema_only(self) -> None:
        rows = self.summary["locator_rows"]
        self.assertEqual({row["field"] for row in rows}, REQUIRED_LOCATOR_FIELDS)
        self.assertEqual(set(self.summary["required_locator_fields"]), REQUIRED_LOCATOR_FIELDS)
        for row in rows:
            with self.subTest(field=row["field"]):
                self.assertEqual(row["classification"], "schema-only")
                self.assertIs(row["source_defined"], False)
                self.assertIs(row["schema_only"], True)
                self.assertIs(row["downstream_reconstruction"], False)
                self.assertIs(row["absent"], False)
                self.assertIn(
                    row["admission"],
                    {"reject_as_source_receipt", "active_but_not_sufficient"},
                )

    def test_packet_not_admitted_and_current_data_schema_only(self) -> None:
        self.assertIs(self.summary["admitted_packet"], False)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertEqual(self.summary["current_data_classification"], "schema-only")
        self.assertIs(self.summary["minimal_schema_can_upgrade_to_admitted_packet"], False)
        self.assertIs(self.summary["schema_only_classification_for_current_data"], True)

    def test_no_proof_restart_target_import_or_quotient_descent(self) -> None:
        self.assertIs(self.summary["proof_restart"], False)
        self.assertIs(self.summary["target_import"], False)
        self.assertIs(self.summary["quotient_descent"], False)
        self.assertIs(self.summary["finite_qft_work"], False)
        self.assertIs(self.summary["Bell_CHSH_work"], False)

        locks = self.summary["downstream_locks"]
        for key, value in locks.items():
            self.assertIs(value, False, key)

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_absent",
        )
        self.assertEqual(
            obstruction["first_missing_field_set"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        self.assertIs(obstruction["missing"], True)

        next_object = self.summary["next_object"]
        self.assertEqual(
            next_object["id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertEqual(
            next_object["first_subobject"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        self.assertEqual(next_object["then_test"], "GaugeOrbitGeneratorRestrictionTest_V1")

    def test_non_import_screen_and_selector_firewall(self) -> None:
        screen = self.summary["non_import_screen"]
        self.assertEqual(screen["forbidden_selectors_used"], [])
        self.assertIs(screen["target_import_used_as_source_selector"], False)
        for selector in ["F_phys", "P_fin", "rho_AB", "Bell", "CHSH"]:
            self.assertIn(selector, screen["forbidden_selectors"])

        self.assertIs(self.summary["rho_AB_selector_promotion"], False)
        self.assertIs(self.summary["CHSH_selector_promotion"], False)
        firewall = self.summary["promotion_firewall"]
        self.assertIs(firewall["no_CHSH_or_rho_AB_selector_promotion"], True)
        self.assertIs(firewall["minimal_schema_is_not_packet"], True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
