#!/usr/bin/env python3
"""Guard the Eric-lane decisive primary-source collision requirement.

This is a process/provenance audit, not mathematical evidence. It makes sure
the campaign cannot grade a decisive result without recording whether the
local Weinstein source confirms, corrects, or is silent on that result.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "lab/process/construction-space-exploration-protocol.md"
CAMPAIGN = ROOT / "lab/process/eric-curt-ten-wave-campaign.json"
LEDGER = ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md"
ECW3C = ROOT / "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json"
B2A = ROOT / "lab/process/eric-curt-wave3d-b2a-native-time-flux-coercivity-kill.json"
B2B = ROOT / "lab/process/eric-curt-wave3d-b2b-positive-symmetrizer-jordan-obstruction.json"
ALLOWED = {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"}


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


class EricLaneDecisiveSourceCollisionAudit(unittest.TestCase):
    def test_protocol_has_fail_closed_dispositions_and_evidence_boundary(self) -> None:
        text = PROTOCOL.read_text(encoding="utf-8")
        for phrase in (
            "Decisive Eric-lane source-collision gate",
            "`SOURCE-CONFIRMS`",
            "`SOURCE-CORRECTS`",
            "`SOURCE-SILENT`",
            "cannot verify a theorem",
            "remains ungraded",
        ):
            self.assertIn(phrase, text)

    def test_campaign_activates_gate_and_names_retroactive_repair(self) -> None:
        gate = load(CAMPAIGN)["decisive_source_collision_gate"]
        self.assertEqual("ACTIVE_FAIL_CLOSED", gate["status"])
        self.assertEqual(ALLOWED, set(gate["allowed_dispositions"]))
        self.assertEqual(
            "lab/process/eric-curt-wave3c-y14-atlas-cauchy-domain.json",
            gate["retroactive_repair"],
        )
        self.assertIn("mathematical evidence", gate["evidence_boundary"])

    def test_missed_multiple_time_claim_is_restored(self) -> None:
        text = LEDGER.read_text(encoding="utf-8")
        self.assertIn("| WG-A16 |", text)
        self.assertIn("ultrahyperbolic", text)
        self.assertIn("ordinary codimension-one initial conditions", text)

    def test_ecw3c_repair_corrects_scope_without_using_source_as_proof(self) -> None:
        collision = load(ECW3C)["source_collision"]
        self.assertIn(collision["disposition"], ALLOWED)
        self.assertEqual("SOURCE-CORRECTS", collision["disposition"])
        self.assertIn("01:16:13", collision["source_ref"])
        self.assertFalse(collision["source_is_mathematical_evidence"])
        self.assertIn("ultrahyperbolic", collision["corrected_scope"])

    def test_decisive_swings_record_source_silence(self) -> None:
        for path in (B2A, B2B):
            with self.subTest(path=path.name):
                collision = load(path)["source_collision"]
                self.assertIn(collision["disposition"], ALLOWED)
                self.assertEqual("SOURCE-SILENT", collision["disposition"])
                self.assertIn("01:16:13", collision["source_ref"])
                self.assertFalse(collision["source_is_mathematical_evidence"])
                self.assertIn("record/finality", " ".join(collision["silent_on"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
