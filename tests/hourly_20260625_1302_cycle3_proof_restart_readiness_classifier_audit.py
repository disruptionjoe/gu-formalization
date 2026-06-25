#!/usr/bin/env python3
"""Audit ProofRestartReadinessClassifierAfter1302_V1."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DOC = (
    REPO_ROOT
    / "explorations"
    / "hourly-20260625-1302-cycle3-proof-restart-readiness-classifier.md"
)

EXPECTED_ROUTES = {"PTUJ", "IG", "DGU_VZ", "RS", "QFT"}

EXPECTED_HEADINGS = [
    "## 1. Verdict.",
    "## 2. Route table for five routes.",
    "## 3. Strongest positive result per route.",
    "## 4. First exact proof-restart blocker per route.",
    "## 5. What would change if blockers closed.",
    "## 6. Sequential vs parallel consequences.",
    "## 7. Machine-readable JSON summary.",
]

FORBIDDEN_PROMOTION_PATTERNS = [
    r"\bproof_restart_allowed\s*[:=]\s*true\b",
    r"\broutes_ready_count\s*[:=]\s*[1-9]\d*\b",
    r"\baccepted_receipt_count\s*[:=]\s*[1-9]\d*\b",
    r"\bglobal_no_go_promoted\s*[:=]\s*true\b",
    r"\btarget_import_used\s*[:=]\s*true\b",
    r"\bproof\s+restart\s+is\s+allowed\b",
    r"\bproof\s+restart\s+authorized\b",
    r"\bproof\s+restart\s+license\b",
    r"\bready\s+for\s+proof\s+restart\b",
    r"\baccepted\s+source\s+receipt\s+(exists|present|true|passed)\b",
    r"\baccepted\s+selector\s+(exists|present|true|passed)\b",
    r"\baccepted\s+RS\s+receipt\s+(exists|present|true|passed)\b",
    r"\baccepted\s+DGU\s+identity\s+witness\s+(exists|present|true|passed)\b",
    r"\baccepted\s+QFT\s+congruence\s+generator\s+(exists|present|true|passed)\b",
]


def read_doc() -> str:
    try:
        return DOC.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise AssertionError(f"missing artifact: {DOC}") from exc


def extract_summary(text: str) -> dict[str, Any]:
    match = re.search(
        r"## 7\. Machine-readable JSON summary\.\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError("missing machine-readable JSON summary block")
    return json.loads(match.group(1))


class ProofRestartReadinessClassifierAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = read_doc()
        cls.summary = extract_summary(cls.text)

    def test_required_sections_present(self) -> None:
        for heading in EXPECTED_HEADINGS:
            self.assertIn(heading, self.text)

    def test_identity_and_global_decision(self) -> None:
        self.assertEqual(
            self.summary["artifact_id"],
            "ProofRestartReadinessClassifierAfter1302_V1",
        )
        self.assertEqual(self.summary["run_id"], "hourly-20260625-1302")
        self.assertEqual(self.summary["cycle"], 3)
        self.assertEqual(self.summary["lane"], 1)
        self.assertEqual(self.summary["routes_examined"], 5)
        self.assertEqual(self.summary["routes_ready_count"], 0)
        self.assertEqual(self.summary["accepted_receipt_count"], 0)
        self.assertIs(self.summary["proof_restart_allowed"], False)
        self.assertIs(self.summary["global_no_go_promoted"], False)
        self.assertIs(self.summary["target_import_used"], False)

    def test_all_five_routes_are_present_once(self) -> None:
        routes = self.summary["routes"]
        self.assertEqual(len(routes), 5)
        self.assertEqual({route["route"] for route in routes}, EXPECTED_ROUTES)

    def test_no_route_is_ready_or_has_receipts(self) -> None:
        for route in self.summary["routes"]:
            with self.subTest(route=route["route"]):
                self.assertIs(route["accepted_source_receipt_or_object"], False)
                self.assertEqual(route["accepted_receipt_count"], 0)
                self.assertIs(route["family_identity_passed"], False)
                self.assertIs(route["route_specific_prerequisites_met"], False)
                self.assertIs(route["proof_restart_allowed"], False)
                self.assertIs(route["target_import_used"], False)

    def test_route_blockers_are_exact_and_nonempty(self) -> None:
        expected_blockers = {
            "PTUJ": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
            "IG": "VerifiedMultiplicityAndHighestWeightSelectorPacketForShiabHomSpace_V1",
            "DGU_VZ": "missing_complete_DGUIdentityFieldReceiptBundle_V1_for_actual_D_GU_epsilon_0_1",
            "RS": "UCSDFrameSequenceForRolledOperatorWindow_V1",
            "QFT": "LocalGaugeActionGroupoidOnObservedRawGUFields_V1",
        }
        for route in self.summary["routes"]:
            self.assertEqual(route["first_exact_blocker"], expected_blockers[route["route"]])
            self.assertTrue(route["next_object"])
            self.assertTrue(route["would_change_if_blocker_closed"])

    def test_parallel_and_sequential_consequences_are_recorded(self) -> None:
        self.assertEqual(len(self.summary["parallel_next_objects"]), 5)
        self.assertEqual(len(self.summary["sequentially_forbidden_before_blockers_close"]), 5)
        self.assertIn(
            "DGU_symbol_certificate_or_VZ_replay",
            self.summary["sequentially_forbidden_before_blockers_close"],
        )
        self.assertIn(
            "QFT_state_extraction_rho_AB_or_CHSH_restart",
            self.summary["sequentially_forbidden_before_blockers_close"],
        )

    def test_global_receipt_count_matches_route_counts(self) -> None:
        route_receipts = sum(route["accepted_receipt_count"] for route in self.summary["routes"])
        self.assertEqual(route_receipts, self.summary["accepted_receipt_count"])
        self.assertEqual(route_receipts, 0)

    def test_global_ready_count_matches_route_flags(self) -> None:
        ready_routes = sum(
            1
            for route in self.summary["routes"]
            if route["proof_restart_allowed"]
            and route["accepted_source_receipt_or_object"]
            and route["family_identity_passed"]
            and route["route_specific_prerequisites_met"]
            and not route["target_import_used"]
        )
        self.assertEqual(ready_routes, self.summary["routes_ready_count"])
        self.assertEqual(ready_routes, 0)

    def test_no_proof_restart_promotion_phrases(self) -> None:
        text_without_json_keys = re.sub(r'"proof_restart_allowed"\s*:\s*false', "", self.text)
        for pattern in FORBIDDEN_PROMOTION_PATTERNS:
            self.assertIsNone(
                re.search(pattern, text_without_json_keys, flags=re.IGNORECASE),
                f"forbidden promotion phrase matched: {pattern}",
            )


def audit_summary() -> dict[str, Any]:
    text = read_doc()
    summary = extract_summary(text)
    return {
        "document": str(DOC.relative_to(REPO_ROOT)),
        "artifact_id": summary["artifact_id"],
        "routes_examined": summary["routes_examined"],
        "routes_ready_count": summary["routes_ready_count"],
        "accepted_receipt_count": summary["accepted_receipt_count"],
        "proof_restart_allowed": summary["proof_restart_allowed"],
        "global_no_go_promoted": summary["global_no_go_promoted"],
        "target_import_used": summary["target_import_used"],
        "routes": [route["route"] for route in summary["routes"]],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Audit the 1302 cycle 3 proof-restart readiness classifier."
    )
    parser.add_argument("--json", action="store_true", help="Print audit summary as JSON.")
    args, _remaining = parser.parse_known_args(argv)

    if args.json:
        print(json.dumps(audit_summary(), indent=2, sort_keys=True))
        return 0

    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            ProofRestartReadinessClassifierAudit
        )
    )
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
