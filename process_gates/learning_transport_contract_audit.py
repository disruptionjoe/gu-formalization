#!/usr/bin/env python3
"""Audit the compact learning-transport contract introduced after ledger v0.221.

This is a process gate, not a mathematical certificate.  It checks that a
successor wave cannot silently transfer a result across a changed concrete
structure merely because ranks, dimensions or abstract group names agree.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "lab/process/functional-channel-operating-contract-v1.0.json"
NAMES = ROOT / "lab/process/NAMES.md"
CORRECTIONS = ROOT / "lab/process/correction-registry.yaml"
PATHS = ROOT / "lab/process/path-dependencies.yaml"
LANES = ROOT / "LANES.yaml"
CARD = ROOT / "lab/process/session-agent-card.md"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def transfer_admissible(
    predecessor: dict[str, str],
    successor: dict[str, str],
    *,
    adapter_receipt: str | None = None,
    layer0_reset: bool = False,
) -> bool:
    """The minimal rule: same fingerprint, or an explicit typed transition."""
    if predecessor == successor:
        return True
    return bool(adapter_receipt) or layer0_reset


class LearningTransportContractAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = load_json(CONTRACT)
        cls.standing = cls.contract["standing_ledger"]

    def test_current_progress_pointer_matches_highest_ledger(self) -> None:
        versions: list[tuple[int, Path]] = []
        for path in (ROOT / "lab/process").glob("conditional-physics-ledger-v0.*.json"):
            match = re.fullmatch(r"conditional-physics-ledger-v0\.(\d+)\.json", path.name)
            if match:
                versions.append((int(match.group(1)), path))
        self.assertTrue(versions)
        minor, ledger_path = max(versions)
        expected_ref = str(ledger_path.relative_to(ROOT))
        expected_human = f"explorations/conditional-build/conditional-physics-ledger-v0.{minor}.md"
        self.assertEqual(
            self.standing["ref"],
            expected_ref,
        )
        self.assertEqual(
            self.standing["human_ref"],
            expected_human,
        )
        ledger = load_json(ledger_path)
        self.assertEqual(ledger["schema_version"], f"0.{minor}")
        self.assertEqual(ledger["status"], f"CURRENT_APPEND_ONLY_LEDGER_V0_{minor}")
        self.assertTrue((ROOT / self.standing["ref"]).exists())
        self.assertTrue((ROOT / self.standing["human_ref"]).exists())
        lanes = load_yaml(LANES)
        work_refs = lanes["extensions"]["operating_architecture"]["work_state_refs"]
        self.assertIn(self.standing["ref"], work_refs)
        self.assertIn(self.standing["human_ref"], work_refs)

    def test_typed_handoff_fields_and_vocabularies_are_explicit(self) -> None:
        required = {
            "structure_fingerprint",
            "variational_altitude",
            "globalization_grade",
            "commutation_status",
            "forbidden_transfers",
            "adapter_receipt_or_layer0_reset",
        }
        self.assertTrue(required.issubset(self.standing["wave_required_fields"]))
        self.assertEqual(
            self.standing["structure_fingerprint_required_fields"],
            [
                "carrier",
                "pairing_or_form",
                "real_structure",
                "grading",
                "signature_horn",
                "ambient_embedding",
            ],
        )
        self.assertEqual(
            self.standing["commutation_status_values"],
            ["PROVED", "FAILED", "OPEN"],
        )
        self.assertIn("ACTION_OWNED_TANGENT", self.standing["variational_altitudes"])
        self.assertIn("STATIONARY_SOLUTION_JET", self.standing["variational_altitudes"])
        self.assertIn("ASSOCIATED_BUNDLE", self.standing["globalization_grades"])
        self.assertIn("GLOBALLY_DESCENDED", self.standing["globalization_grades"])

    def test_v0220_style_structure_swap_is_rejected(self) -> None:
        trace_hq = {
            "carrier": "C^(32,32) + C^(32,32)",
            "pairing_or_form": "H_q = i B gamma(q/2)",
            "real_structure": "trace-H_q fixed real form",
            "grading": "two chiral halves",
            "signature_horn": "K77",
            "ambient_embedding": "source U(64,64) parent",
        }
        b_skew = dict(trace_hq)
        b_skew["pairing_or_form"] = "B-skew comparator"
        b_skew["real_structure"] = "B-skew embedded real form"

        self.assertFalse(transfer_admissible(trace_hq, b_skew))
        self.assertTrue(
            transfer_admissible(
                trace_hq,
                b_skew,
                adapter_receipt="constructed-intertwiner-receipt.md",
            )
        )
        self.assertTrue(transfer_admissible(trace_hq, b_skew, layer0_reset=True))
        self.assertTrue(transfer_admissible(trace_hq, dict(trace_hq)))

    def test_homonym_correction_and_path_chain_are_routed(self) -> None:
        names = NAMES.read_text(encoding="utf-8")
        for token in ("H_q", "H_u", "H^-", "H^+"):
            self.assertIn(token, names)
        corrections = load_yaml(CORRECTIONS)["corrections"]
        self.assertIn("HQ-CONTACT-20260812", {item["id"] for item in corrections})
        chains = load_yaml(PATHS)["chains"]
        chain = next(item for item in chains if item["id"] == "PD-STRUCTURE-TRANSPORT")
        self.assertTrue(chain["traps"])
        self.assertIn("OBJECT_CHANGED__LAYER0_RESET", chain["check"])
        card = CARD.read_text(encoding="utf-8")
        self.assertIn("structure fingerprint", card)
        self.assertIn("variational_altitude", card)


if __name__ == "__main__":
    unittest.main(verbosity=2)
