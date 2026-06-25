#!/usr/bin/env python3
"""Audit QFTSourceDefinedRawBranchLocalGaugeGroupoidPacket_1602_C1_L5_V1."""

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
    / "hourly-20260625-1602-cycle1-qft-source-defined-raw-branch-local-gauge-groupoid.md"
)

EXPECTED_ARTIFACT_ID = (
    "QFTSourceDefinedRawBranchLocalGaugeGroupoidPacket_1602_C1_L5_V1"
)
EXPECTED_RUN_ID = "hourly-20260625-1602"
EXPECTED_VERDICT_CLASS = "underdefined"


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class QFTSourceDefinedRawBranchLocalGaugeGroupoidAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_identity_and_verdict(self) -> None:
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["verdict_class"], EXPECTED_VERDICT_CLASS)
        self.assertEqual(
            self.summary["verdict"],
            "UNDERDEFINED_TEMPLATE_COMPATIBILITY_SKETCH_PRESENT_SOURCE_DEFINED_PACKET_ABSENT",
        )

    def test_no_receipt_or_restart_or_target_import(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_template_is_not_source_defined_packet(self) -> None:
        self.assertIs(self.summary["template_or_compatibility_sketch_present"], True)
        self.assertIs(self.summary["source_defined_packet_present"], False)
        for key in [
            "iota_b_source_defined",
            "R_raw_b_O_source_defined",
            "G_b_O_source_defined",
            "restriction_maps_source_defined",
        ]:
            self.assertIs(self.summary[key], False, key)

    def test_required_and_present_fields_are_separated(self) -> None:
        required = set(self.summary["required_fields"])
        present = set(self.summary["present_fields"])
        for field in [
            "source_defined_iota_b",
            "typed_R_raw_b_O",
            "admissible_local_gauge_groupoid_G_b_O",
            "raw_field_restriction_res_R_O_O_prime",
            "gauge_parameter_restriction_res_G_O_O_prime",
        ]:
            self.assertIn(field, required)
            self.assertNotIn(field, present)
        self.assertIn("template_or_compatibility_sketch", present)

    def test_missing_fields_name_core_absences(self) -> None:
        missing = set(self.summary["missing_fields"])
        for field in [
            "source_defined_iota_b",
            "source_defined_raw_fields_R_raw_b_O",
            "source_defined_local_gauge_groupoid_G_b_O",
            "source_defined_restriction_maps_res_R_and_res_G",
        ]:
            self.assertIn(field, missing)

    def test_first_obstruction_and_next_object_are_explicit(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["first_missing_subobject"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        next_object = self.summary["next_object"]
        self.assertEqual(
            next_object["id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertIn("iota_b", next_object["description"])
        self.assertIn("res_R/res_G", next_object["description"])
        self.assertEqual(
            next_object["then_test"], "GaugeOrbitGeneratorRestrictionTest_V1"
        )

    def test_promotion_firewall_blocks_downstream_claims(self) -> None:
        firewall = self.summary["promotion_firewall"]
        for key in [
            "no_target_hilbert_state_selector",
            "no_target_density_matrix_selector",
            "no_bell_or_chsh_selector",
            "no_pauli_setting_selector",
            "no_representation_label_selector",
            "no_physical_quotient_selector",
            "no_finite_extraction_selector",
            "claim_promotion_blocked",
        ]:
            self.assertIs(firewall[key], True, key)

        downstream = self.summary["downstream"]
        for key in [
            "F_phys_defined",
            "P_fin_defined",
            "rho_AB_work_allowed",
            "CHSH_work_allowed",
            "gauge_generator_promoted",
        ]:
            self.assertIs(downstream[key], False, key)


if __name__ == "__main__":
    unittest.main()
