#!/usr/bin/env python3
"""Audit the cycle 2 QFT source-defined branch packet minimal schema artifact."""

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
    / "hourly-20260625-1602-cycle2-qft-source-defined-branch-packet-minimal-schema.md"
)

EXPECTED_ARTIFACT_ID = (
    "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_MinimalSchema_1602_C2_L5"
)
EXPECTED_RUN_ID = "hourly-20260625-1602"


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 9\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class SourceDefinedBranchPacketMinimalSchemaAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["cycle"], 2)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_no_receipts_restart_or_target_import(self) -> None:
        complete = self.summary["source_branch_packet_present"]
        if not complete:
            self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["source_branch_packet_present"], False)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_missing_fields_include_core_packet_absences(self) -> None:
        missing = set(self.summary["missing_fields"])
        expected_fragments = [
            "iota",
            "R_raw",
            "G_b",
            "restriction",
            "non_import",
        ]
        for fragment in expected_fragments:
            self.assertTrue(
                any(fragment in field for field in missing),
                f"missing field equivalent to {fragment!r}",
            )

    def test_required_fields_include_schema_and_gate(self) -> None:
        required = set(self.summary["required_fields"])
        for field in [
            "source_defined_iota_b_or_equivalent_observed_pullback",
            "typed_raw_fields_R_raw_b_O_and_R_raw_b_O_prime",
            "admissible_local_gauge_groupoids_G_b_O_and_G_b_O_prime",
            "raw_field_restriction_res_R_O_O_prime",
            "gauge_parameter_restriction_res_G_O_O_prime",
            "packet_level_non_import_screen",
        ]:
            self.assertIn(field, required)

    def test_non_import_screen_blocks_forbidden_selectors(self) -> None:
        screen = self.summary["non_import_screen"]
        self.assertTrue(screen["required_pass_before_receipt"])
        forbidden = set(screen["reject_if_selected_by"])
        for selector in [
            "F_phys",
            "P_fin",
            "rho_AB",
            "Bell_or_CHSH",
            "target_Hilbert_data",
            "target_density_matrix",
        ]:
            self.assertIn(selector, forbidden)

    def test_downstream_quotient_and_chsh_are_locked(self) -> None:
        downstream = self.summary["downstream_allowed"]
        for key in [
            "gauge_generator_promotion",
            "quotient_descent",
            "F_phys",
            "P_fin",
            "rho_AB",
            "CHSH",
            "target_Hilbert_data",
        ]:
            self.assertIs(downstream[key], False, key)

    def test_first_obstruction_and_next_object_are_explicit(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertEqual(
            obstruction["first_missing_subobject"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        next_object = self.summary["next_object"]
        self.assertEqual(
            next_object["id"],
            "FindOrConstructSourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertIn("source-emitted packet", next_object["description"])
        self.assertEqual(
            next_object["then_test"], "GaugeOrbitGeneratorRestrictionTest_V1"
        )


if __name__ == "__main__":
    unittest.main()
