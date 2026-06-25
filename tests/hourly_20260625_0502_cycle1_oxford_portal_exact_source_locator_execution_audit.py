#!/usr/bin/env python3
"""Audit OxfordPortalExactSourceLocatorExecution_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "explorations"
    / "hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md"
)

REQUIRED_FAMILIES = {
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "RS": "source.action_or_operator for d_RS,-1",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b",
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
}

EXPECTED_OBSTRUCTION_ID = "accepted PrimarySourceReceiptInstance_V1/family identity check"


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. Machine-Readable JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class OxfordPortalExactSourceLocatorExecutionAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "OxfordPortalExactSourceLocatorExecution_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0502")
        self.assertEqual(self.summary["cycle"], 1)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(
            self.summary["verdict"],
            "BLOCKED_ZERO_ACCEPTED_PRIMARY_SOURCE_RECEIPTS",
        )
        identity = self.summary["artifact_identity"]
        self.assertEqual(
            identity["owned_path"],
            "explorations/hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md",
        )
        self.assertEqual(
            identity["companion_audit"],
            "tests/hourly_20260625_0502_cycle1_oxford_portal_exact_source_locator_execution_audit.py",
        )
        self.assertEqual(
            identity["artifact_id"],
            "OxfordPortalExactSourceLocatorExecution_V1",
        )

    def test_required_family_coverage(self) -> None:
        rows = {
            row["family"]: row for row in self.summary["required_family_coverage"]
        }
        self.assertEqual(set(rows), set(REQUIRED_FAMILIES))
        for family, required_object in REQUIRED_FAMILIES.items():
            row = rows[family]
            self.assertEqual(row["required_object"], required_object)
            self.assertEqual(row["acceptance_status"], "blocked")
            self.assertEqual(row["accepted_receipt_count"], 0)
            self.assertFalse(row["proof_restart_allowed"])
            self.assertFalse(row["claim_promotion_allowed"])

    def test_receipt_and_promotion_gates_are_closed(self) -> None:
        self.assertEqual(self.summary["accepted_receipts"], [])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["proof_restart_allowed"])
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertTrue(self.summary["no_claim_promotion"])
        self.assertIn("Current accepted receipts are zero.", self.text)
        self.assertIn("Proof restart remains blocked.", self.text)
        self.assertRegex(self.text, r"No GU claim\s+is promoted\.")

    def test_first_exact_obstruction(self) -> None:
        obstruction = self.summary["first_exact_obstruction"]
        self.assertEqual(obstruction["id"], EXPECTED_OBSTRUCTION_ID)
        self.assertIs(obstruction["missing"], True)
        self.assertIn("source-emitted required family object", obstruction["description"])
        self.assertIn("family identity check", obstruction["description"])

    def test_strongest_locator_is_positive_but_not_accepted(self) -> None:
        locator = self.summary["strongest_positive_locator"]
        self.assertEqual(locator["family"], "DGU_VZ")
        self.assertIn("02:35:10", locator["locator"])
        self.assertIn("02:36:12", locator["locator"])
        self.assertIn("swervature", locator["positive_content"])
        self.assertIn("does not emit", locator["why_not_accepted"])
        self.assertIn("D_GU^epsilon", locator["why_not_accepted"])

    def test_constructive_next_object_and_forbidden_promotions(self) -> None:
        next_object = self.summary["constructive_next_object"]
        self.assertEqual(
            next_object["id"],
            "OxfordPortalPrimarySourceReceiptInstanceCandidate_V1",
        )
        self.assertEqual(
            next_object["entry_type"],
            "PrimarySourceReceiptInstance_V1_candidate",
        )
        self.assertIn("PowerPoint image/formula anchors", next_object["minimum_test"])

        forbidden = set(self.summary["forbidden_promotions"])
        for phrase in [
            "IG selects K_IG",
            "RS source-derived d_RS,-1 is established",
            "QFT P_fin^b is supplied",
            "DGU/VZ actual D_GU^epsilon 0/1 is identified",
            "Oxford/Portal exact locator execution permits proof restart",
        ]:
            self.assertIn(phrase, forbidden)

    def test_source_surfaces_were_fetchable(self) -> None:
        surfaces = {row["source_id"]: row for row in self.summary["source_surfaces"]}
        self.assertEqual(
            set(surfaces),
            {
                "GU-MEDIA-2013-OXFORD",
                "GU-MEDIA-2020-PORTAL-SPECIAL",
                "GU-POD-2020-PORTAL-SPECIAL",
            },
        )
        for row in surfaces.values():
            self.assertIn("fetched_public", row["access_status"])
            self.assertTrue(row["url"].startswith("https://"))


if __name__ == "__main__":
    unittest.main()
