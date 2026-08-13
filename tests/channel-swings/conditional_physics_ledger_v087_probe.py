#!/usr/bin/env python3
"""Exact structural checks for conditional-physics ledger v0.87."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.87.json").read_text())
prior = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.86.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-kosmann-moving-shiab-rank3.json").read_text())

assert ledger["schema_version"] == "0.87"
assert ledger["predecessor"].endswith("v0.86.json")
assert ledger["progress"]["mapped"] == prior["progress"]["mapped"] == 82
assert ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"]
assert ledger["residue"] == prior["residue"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 4,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert ledger["source_return"] == "SOURCE-CONFIRMS"
assert len(ledger["migrations"]) == len(prior["migrations"]) + 5
assert registry["exact_closure"]["complete_lower_order_response_cancels"] is True
assert registry["exact_closure"]["moving_shiab_alone_cancels"] is False
assert registry["causal_results"]["spacelike"]["matched_q_supports"] != registry["causal_results"]["spacelike"]["v086_frozen_q0_supports"]
assert registry["causal_results"]["null"]["matched_q_supports"] != registry["causal_results"]["null"]["v086_frozen_q0_supports"]
assert set(registry["external_datum"].values()) == {"UNUSED"}
print("PASS conditional physics ledger v0.87")
