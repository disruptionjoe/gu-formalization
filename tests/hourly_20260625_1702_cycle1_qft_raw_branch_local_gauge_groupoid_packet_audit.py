#!/usr/bin/env python3
"""Audit the 1702 C1/L5 QFT raw branch local gauge groupoid packet."""

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
    / "hourly-20260625-1702-cycle1-qft-raw-branch-local-gauge-groupoid-packet.md"
)

EXPECTED_RUN_ID = "hourly-20260625-1702"
EXPECTED_ARTIFACT_ID = (
    "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_1702_C1_L5_V1"
)
EXPECTED_OWNED_PATH = (
    "explorations/hourly-20260625-1702-cycle1-qft-raw-branch-local-gauge-groupoid-packet.md"
)
EXPECTED_AUDIT = (
    "tests/hourly_20260625_1702_cycle1_qft_raw_branch_local_gauge_groupoid_packet_audit.py"
)

REQUIRED_FIELDS = {
    "branch_label_b",
    "injection_selector_iota_b",
    "local_domains_U_b_O_and_U_b_O_prime",
    "local_raw_field_space_R_raw_b_O_and_R_raw_b_O_prime",
    "local_gauge_groupoids_G_b_O_and_G_b_O_prime",
    "action_gamma_on_raw_fields",
    "restriction_maps_res_R_and_res_G",
    "restriction_stability_certificate",
    "packet_level_non_import_screen",
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


class QFTRawBranchLocalGaugeGroupoidPacketAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_identity_and_owned_paths(self) -> None:
        self.assertEqual(self.summary["run_id"], EXPECTED_RUN_ID)
        self.assertEqual(self.summary["artifact_id"], EXPECTED_ARTIFACT_ID)
        self.assertEqual(self.summary["target_packet_id"], "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1")
        self.assertEqual(self.summary["owned_path"], EXPECTED_OWNED_PATH)
        self.assertEqual(self.summary["companion_audit"], EXPECTED_AUDIT)
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(self.summary["verdict_class"], "underdefined")

    def test_required_field_matrix_is_complete_and_rejected(self) -> None:
        rows = self.summary["required_field_matrix"]
        self.assertEqual({row["field"] for row in rows}, REQUIRED_FIELDS)
        for row in rows:
            with self.subTest(field=row["field"]):
                self.assertIs(row["schema_defined"], True)
                self.assertIs(row["source_defined"], False)
                self.assertIs(row["import_used"], False)
                self.assertIs(row["downstream_selector_allowed"], False)
                self.assertIn(row["admission"], {"reject_as_receipt", "active_but_not_sufficient"})

    def test_source_defined_vs_schema_import_booleans(self) -> None:
        flags = self.summary["source_defined_vs_schema_import_booleans"]
        self.assertIs(flags["minimal_schema_defined"], True)
        self.assertIs(flags["compatibility_template_present"], True)
        self.assertIs(flags["import_used_for_any_required_field"], False)
        for key in [
            "branch_label_b_source_defined",
            "iota_b_source_defined",
            "R_raw_b_O_source_defined",
            "G_b_O_source_defined",
            "restriction_maps_source_defined",
            "action_source_defined",
            "non_import_screen_packet_receipt_present",
        ]:
            self.assertIs(flags[key], False, key)

    def test_receipt_restart_and_target_import_are_closed(self) -> None:
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["source_defined_packet_present"], False)
        self.assertIs(self.summary["all_required_fields_source_defined"], False)
        self.assertIs(self.summary["schema_or_template_present"], True)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["target_import_used"], False)
        self.assertIs(self.summary["target_import_used_as_source_selector"], False)

    def test_non_import_screen_blocks_target_selectors(self) -> None:
        screen = self.summary["non_import_screen"]
        self.assertEqual(screen["source_selectors_used"], [])
        self.assertEqual(screen["forbidden_source_selectors_used"], [])
        forbidden = set(screen["reject_if_selected_by"])
        for target in ["F_phys", "P_fin", "rho_AB", "Bell", "CHSH", "target_Hilbert_data"]:
            self.assertIn(target, forbidden)

    def test_first_obstruction_and_next_object(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertTrue(obstruction["missing"])
        self.assertEqual(
            obstruction["id"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1_absent",
        )
        self.assertEqual(
            obstruction["first_missing_subobject"],
            "source_defined_iota_b_and_typed_R_raw_b_O",
        )
        next_object = self.summary["next_object"]
        self.assertEqual(next_object["id"], "QFTSourceFieldLocatorClassificationForIotaRRawG_V1")
        self.assertEqual(
            next_object["acceptance_followup"],
            "SourceDefinedRawBranchLocalGaugeGroupoidPacketForRRawBO_V1",
        )
        self.assertEqual(next_object["then_test"], "GaugeOrbitGeneratorRestrictionTest_V1")

    def test_promotion_firewall_and_downstream_locks(self) -> None:
        firewall = self.summary["promotion_firewall"]
        self.assertIs(firewall["promotion_allowed"], False)
        self.assertIs(firewall["claim_promotion_blocked"], True)
        self.assertIs(firewall["proof_restart_allowed"], False)
        self.assertIs(firewall["no_rho_AB_Bell_CHSH_as_source_selector"], True)
        self.assertIs(firewall["type_ii1_requirements_not_substitute_packet"], True)

        locks = self.summary["downstream_locks"]
        for key, value in locks.items():
            self.assertIs(value, False, key)


if __name__ == "__main__":
    unittest.main(verbosity=2)
