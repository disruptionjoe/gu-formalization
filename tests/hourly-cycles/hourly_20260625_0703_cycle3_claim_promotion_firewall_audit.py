#!/usr/bin/env python3
"""Audit ClaimPromotionFirewallAfterHourly20260625_0703_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-0703-cycle3-claim-promotion-firewall.md"
)

REQUIRED_FORBIDDEN_PROMOTIONS = {
    "hosted_is_not_selected",
    "bosonic_is_not_dgu01",
    "scoped_negative_is_not_global_no_go",
    "captions_or_storyboards_are_not_receipts",
}

EXPECTED_CLAIM_IDS = {
    "DGU_VZ_Oxford_bosonic",
    "IG_theta_shiab_selector",
    "RS_generation_minus_one",
    "QFT_state_space_CHSH",
    "Oxford_visual_receipts",
    "Keating_visual_receipts",
    "global_no_go_map",
}


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 9\. JSON Summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing JSON summary block")
    return json.loads(match.group(1))


class ClaimPromotionFirewallAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_identity(self) -> None:
        self.assertEqual(
            self.summary["artifact"],
            "ClaimPromotionFirewallAfterHourly20260625_0703_V1",
        )
        self.assertEqual(
            self.summary["artifact_id"],
            "ClaimPromotionFirewallAfterHourly20260625_0703_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-0703")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 5)
        self.assertEqual(
            self.summary["companion_audit"],
            "tests/hourly_20260625_0703_cycle3_claim_promotion_firewall_audit.py",
        )

    def test_claim_rows_cover_required_families(self) -> None:
        rows = self.summary["claim_rows"]
        self.assertGreaterEqual(len(rows), 5)
        self.assertEqual({row["id"] for row in rows}, EXPECTED_CLAIM_IDS)
        joined = json.dumps(rows)
        for needle in ["DGU", "IG", "RS", "QFT", "Oxford", "Keating", "global_no_go"]:
            self.assertIn(needle, joined)

    def test_no_promotions_demotions_or_status_changes(self) -> None:
        self.assertEqual(self.summary["promoted_claim_count"], 0)
        self.assertEqual(self.summary["demoted_claim_count"], 0)
        self.assertFalse(self.summary["canon_status_changed"])
        self.assertFalse(self.summary["active_research_status_changed"])
        self.assertFalse(self.summary["global_no_go_promoted"])
        self.assertFalse(self.summary["proof_restart_allowed"])
        for row in self.summary["claim_rows"]:
            self.assertEqual(row["promotion_decision"], "not_promoted")
            self.assertEqual(row["demotion_decision"], "not_demoted")
            self.assertFalse(row["proof_restart_allowed"], row["id"])

    def test_forbidden_promotions_include_required_firewalls(self) -> None:
        forbidden = set(self.summary["forbidden_promotions"])
        self.assertTrue(REQUIRED_FORBIDDEN_PROMOTIONS.issubset(forbidden))
        for item in REQUIRED_FORBIDDEN_PROMOTIONS:
            self.assertIn(item, self.text)

    def test_first_obstruction_requires_accepted_receipt_or_proof_certificate(self) -> None:
        obstruction = self.summary["first_obstruction"]
        self.assertIn("accepted source receipt", obstruction)
        self.assertIn("proof certificate", obstruction)
        self.assertIn("canonical or active-research", obstruction)
        self.assertIn("No Cycle 1-2 result", obstruction)

    def test_next_frontier_and_json_parse(self) -> None:
        self.assertEqual(
            self.summary["next_frontier_object"],
            "RecoveredBianchiHighestWeightSelectorForShiab_V1",
        )
        json.dumps(self.summary, sort_keys=True)

    def test_no_forbidden_status_change_phrases(self) -> None:
        lowered = self.text.lower()
        self.assertNotIn('"canon_status_changed": true', lowered)
        self.assertNotIn('"active_research_status_changed": true', lowered)
        self.assertNotIn('"global_no_go_promoted": true', lowered)
        self.assertNotIn('"proof_restart_allowed": true', lowered)
        self.assertNotIn('"promoted_claim_count": 1', lowered)
        self.assertNotIn('"demoted_claim_count": 1', lowered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
