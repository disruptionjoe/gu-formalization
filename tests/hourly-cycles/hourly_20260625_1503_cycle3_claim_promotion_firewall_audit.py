#!/usr/bin/env python3
"""Audit ClaimPromotionFirewallAfter1503_V1."""

from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1503-cycle3-claim-promotion-firewall.md"
)

REQUIRED_TOKEN_FAMILIES = [
    "PTUJ",
    "metadata/source locators",
    "formula receipts",
    "IG",
    "Shiab existence",
    "chirality exclusions",
    "full IG selector proof",
    "DGU",
    "VZ",
    "scoped negatives",
    "actual DGU identity witness",
    "VZ certificate",
    "RS",
    "transcript/locator",
    "typed pure-RS operator",
    "QFT",
    "candidate/raw branch template",
    "local groupoid",
    "restriction-stable quotient",
    "descent",
    "rho_AB",
    "CHSH",
    "Bell",
    "generation count",
    "dark energy",
    "major GU claim",
    "global no-go",
]


def extract_summary(text: str) -> dict[str, object]:
    match = re.search(
        r"## 5\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary")
    return json.loads(match.group(1))


class ClaimPromotionFirewallAfter1503Audit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = ARTIFACT.read_text(encoding="utf-8")
        cls.summary = extract_summary(cls.text)

    def test_artifact_exists_and_declares_identity(self) -> None:
        self.assertTrue(ARTIFACT.exists())
        self.assertIn('artifact_id: "ClaimPromotionFirewallAfter1503_V1"', self.text)
        self.assertIn('run_id: "hourly-20260625-1503"', self.text)
        self.assertIn("cycle: 3", self.text)
        self.assertIn("lane: 4", self.text)
        self.assertEqual(self.summary["artifact_id"], "ClaimPromotionFirewallAfter1503_V1")
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1503")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 4)

    def test_required_firewall_booleans_and_counts(self) -> None:
        self.assertEqual(self.summary["promotions_allowed"], 0)
        self.assertFalse(self.summary["claim_promotion_allowed"])
        self.assertFalse(self.summary["target_import_used"])
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertFalse(self.summary["major_GU_claim_promoted"])
        self.assertFalse(self.summary["global_no_go_promoted"])

    def test_exact_cycle_commit_facts_present(self) -> None:
        self.assertEqual(self.summary["cycle_1_commit"], "b1a2cc5")
        self.assertEqual(self.summary["cycle_2_commit"], "74090c4")
        self.assertIn("cycle_1_commit: b1a2cc5", self.text)
        self.assertIn("cycle_2_commit: 74090c4", self.text)

    def test_blocked_claim_tokens_for_all_required_families(self) -> None:
        for token in REQUIRED_TOKEN_FAMILIES:
            with self.subTest(token=token):
                self.assertIn(token, self.text)

    def test_all_claim_families_block_promotion(self) -> None:
        claim_families = self.summary["claim_families"]
        self.assertEqual(len(claim_families), 10)
        for claim in claim_families:
            with self.subTest(claim_id=claim["claim_id"]):
                self.assertEqual(claim["decision"], "blocked")
                self.assertFalse(claim["promotion_allowed"])
                self.assertFalse(claim["target_import_used"])

    def test_required_summary_family_tokens_present(self) -> None:
        expected_summary_tokens = {
            "PTUJ",
            "IG",
            "DGU/VZ",
            "RS",
            "QFT finite extraction",
            "rho_AB",
            "CHSH",
            "Bell",
            "generation count",
            "dark energy",
            "major GU claim",
            "global no-go",
        }
        self.assertEqual(
            set(self.summary["blocked_claim_token_families"]),
            expected_summary_tokens,
        )
        self.assertTrue(self.summary["all_required_families_present"])

    def test_positive_promotion_phrases_absent(self) -> None:
        forbidden_patterns = [
            r"\bpromotions_allowed\s*:\s*[1-9]\d*\b",
            r'"promotions_allowed"\s*:\s*[1-9]\d*',
            r"\bclaim_promotion_allowed\s*:\s*true\b",
            r'"claim_promotion_allowed"\s*:\s*true',
            r"\btarget_import_used\s*:\s*true\b",
            r'"target_import_used"\s*:\s*true',
            r"\baccepted_receipt_count\s*:\s*[1-9]\d*\b",
            r'"accepted_receipt_count"\s*:\s*[1-9]\d*',
            r"\bmajor_GU_claim_promoted\s*:\s*true\b",
            r'"major_GU_claim_promoted"\s*:\s*true',
            r"\bglobal_no_go_promoted\s*:\s*true\b",
            r'"global_no_go_promoted"\s*:\s*true',
        ]
        for pattern in forbidden_patterns:
            with self.subTest(pattern=pattern):
                self.assertIsNone(re.search(pattern, self.text, flags=re.IGNORECASE))


if __name__ == "__main__":
    unittest.main(verbosity=2)
