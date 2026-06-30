#!/usr/bin/env python3
"""Audit DGUBosonicTo01SectorIdentityFirewall_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0601-cycle2-dgu-bosonic-to-01-sector-identity-firewall.md"
)

REQUIRED_REQUIREMENTS = {
    "sector_rule",
    "domain",
    "codomain",
    "coefficient_packet",
    "principal_symbol",
    "projectors",
    "family_identity",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class DGUBosonicTo01SectorIdentityFirewallAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = DOC.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_id_and_target_strings(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "DGUBosonicTo01SectorIdentityFirewall_V1",
        )
        self.assertEqual(
            self.summary["artifact_identity"]["artifact_id"],
            "DGUBosonicTo01SectorIdentityFirewall_V1",
        )
        self.assertIn("D_GU^epsilon 0/1", self.text)
        self.assertEqual(
            self.summary["required_object"],
            "actual D_GU^epsilon 0/1 operator/principal-symbol data",
        )

    def test_bosonic_firewall_blocks_promotion(self) -> None:
        self.assertEqual(self.summary["firewall_name"], "bosonic_firewall")
        firewall_rule = self.summary["firewall_rule"]
        self.assertIn("source-emitted bosonic action/EL locators", firewall_rule)
        self.assertIn("sector rule", firewall_rule)
        self.assertIn("domain/codomain", firewall_rule)
        self.assertIn("coefficient packet", firewall_rule)
        self.assertIn("family identity", firewall_rule)
        self.assertIn("bosonic firewall", self.text.lower())

    def test_required_promotion_fields_are_present_and_missing_in_attempts(self) -> None:
        self.assertEqual(set(self.summary["promotion_requirements"]), REQUIRED_REQUIREMENTS)
        attempts = self.summary["bosonic_identity_attempts"]
        self.assertGreaterEqual(len(attempts), 8)
        for row in attempts:
            self.assertIn(row["status"], {"blocked", "fail_as_operator", "fail_as_receipt"})
            self.assertIn("missing", row["coefficient_packet"])
            self.assertIn("missing", row["family_identity"])
            self.assertNotEqual(row["status"], "accepted")

    def test_missing_sector_rule_and_coefficient_packet_are_obstructions(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(
            obstruction["id"],
            "missing_bosonic_to_D_GU_epsilon_0_1_sector_identity_rule",
        )
        self.assertTrue(obstruction["missing"])
        self.assertIn("sector rule", obstruction["description"])
        self.assertIn("coefficient packet", obstruction["description"])
        self.assertIn("family identity", obstruction["description"])

    def test_zero_receipts_and_restart_false(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertIn("Accepted receipt count: `0`", self.text)
        self.assertIn("Proof restart allowed: `false`", self.text)

    def test_demotion_condition_requires_negative_source_pass(self) -> None:
        demotion = set(self.summary["falsification_or_demotion_condition"])
        self.assertIn("no_source_emitted_0_1_sector_rule", demotion)
        self.assertIn("no_source_emitted_D_GU_epsilon_0_1_domain_codomain", demotion)
        self.assertIn("no_source_emitted_coefficient_packet", demotion)
        self.assertIn("no_source_emitted_family_identity_from_bosonic_objects_to_actual_D_GU_epsilon_0_1", demotion)


if __name__ == "__main__":
    unittest.main()
