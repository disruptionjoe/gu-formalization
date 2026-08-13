#!/usr/bin/env python3
"""Fail closed if the ten-normal K77 result outruns its exact grade."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-full-normal-owner-bank.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.67.json").read_text())

assert "all ten directions" in report
assert "rank one" in report
assert "trivialization" in report
assert "SOURCE-SILENT" in report
assert "It is not a new external" in report and "datum and it does not kill" in report
assert "does not yet give the vertical first-jet lift" in report
assert "common Krein/domain, BV and BFV descent" in report
assert registry["status"].startswith("OWNER_INCOMPLETE")
assert registry["exact_result"]["normal_metric_bank_rank"] == 10
assert registry["exact_result"]["density_bank_rank"] == 1
assert registry["layer0"]["seven_owner_expansion"] == "TRIVIALIZATION_DEPENDENT"
assert registry["owner_disposition"]["complete_selected_action_mixed_hessian_bank"] == "OPEN"
assert registry["external_datum"]["free_object_delta"] == 0
assert set(registry["external_datum"][key] for key in ("P1", "P2", "P3")) == {"UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["quotients_ranked"] == 4
assert "splitting change" in ledger["next_work_queue"][0]["why"]
print("PASS selected K77 full normal-owner bank scope audit")
