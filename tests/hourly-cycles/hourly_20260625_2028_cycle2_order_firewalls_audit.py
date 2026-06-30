"""Audit the 2028 cycle 2 admission-order firewall artifacts."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "hourly-20260625-2028"
ARTIFACTS = {
    "PTUJ": ROOT / "explorations/hourly-20260625-2028-cycle2-ptuj-branch-order-firewall.md",
    "IG": ROOT / "explorations/hourly-20260625-2028-cycle2-ig-product-b-before-fc-gates.md",
    "DGU": ROOT / "explorations/hourly-20260625-2028-cycle2-dgu-sector-same-operator-before-symbol.md",
    "RS": ROOT / "explorations/hourly-20260625-2028-cycle2-rs-capture-before-typed-intake.md",
    "QFT": ROOT / "explorations/hourly-20260625-2028-cycle2-qft-iota-rraw-before-groupoid.md",
}


def extract_summary(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r"## 8\. Machine-readable JSON summary\s*```json\s*(\{.*?\})\s*```",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError(f"missing JSON summary in {path}")
    return json.loads(match.group(1))


class Cycle2OrderFirewallsAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summaries = {route: extract_summary(path) for route, path in ARTIFACTS.items()}

    def test_all_route_firewalls_present(self) -> None:
        self.assertEqual(set(self.summaries), {"PTUJ", "IG", "DGU", "RS", "QFT"})
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertEqual(summary["run_id"], RUN_ID)
                self.assertEqual(summary["cycle"], 2)
                self.assertEqual(summary["route"], route)
                self.assertTrue(summary["admission_firewall"])
                self.assertEqual(summary["accepted_receipt_count"], 0)

    def test_downstream_is_locked(self) -> None:
        for route, summary in self.summaries.items():
            with self.subTest(route=route):
                self.assertFalse(summary["proof_restart_allowed"])
                self.assertFalse(summary["claim_promotion_allowed"])
                self.assertFalse(summary["target_import_used"])
                self.assertFalse(summary["claim_status_consistency_triggered"])
                self.assertGreater(len(summary["upstream_required"]), 20)
                self.assertGreaterEqual(len(summary["downstream_blocked"]), 4)
                self.assertGreaterEqual(len(summary["invalid_bypasses"]), 5)

    def test_route_specific_ordering(self) -> None:
        self.assertIn("SingleCompletePTUJBranchReceipt", self.summaries["PTUJ"]["upstream_required"])
        self.assertIn("ProductBFullD7", self.summaries["IG"]["upstream_required"])
        self.assertIn("SourceEmittedDGU01SectorRule", self.summaries["DGU"]["upstream_required"])
        self.assertIn("RSLawfulSourceAcquisitionRoute", self.summaries["RS"]["upstream_required"])
        self.assertIn("QFTSourceDefinedIotaB", self.summaries["QFT"]["upstream_required"])

    def test_known_forbidden_bypasses(self) -> None:
        checks = {
            "PTUJ": "cross_branch_assembly",
            "IG": "target_generation_count",
            "DGU": "VZ_replay_before_source_receipt",
            "RS": "failed_local_capture_as_full_unavailability",
            "QFT": "ordinary_QFT_recovery_as_source_selector",
        }
        for route, expected in checks.items():
            with self.subTest(route=route):
                self.assertIn(expected, self.summaries[route]["invalid_bypasses"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
