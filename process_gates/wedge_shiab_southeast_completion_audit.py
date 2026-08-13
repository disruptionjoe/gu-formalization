#!/usr/bin/env python3
"""Fail-closed audit for the v0.173 K77 wedge/southeast packet."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.173.json").read_text())
packet = json.loads((ROOT / "lab/process/selected-k77-wedge-shiab-southeast-completion.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-wedge-shiab-southeast-completion-2026-08-11.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-11-selected-k77-wedge-shiab-southeast-completion-review.md").read_text()

assert ledger["schema_version"] == "0.173"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4, "conditions_opened": 1, "remaining_named_conditions": 4}
assert len(ledger["migration_history"]) == 6
assert {item["from_version"] for item in ledger["migration_history"]} == {"0.172"}
assert {item["to_version"] for item in ledger["migration_history"]} == {"0.173"}
assert packet["relations"] == ["12*w_plus*ell_minus-11=0", "12*w_minus*ell_plus-11=0"]
assert packet["fingerprint"]["spatial_jordan_ranks"] == [0, 0, 0]
assert packet["fingerprint"]["null_rank"] == packet["fingerprint"]["nullity"] == 960
assert packet["fingerprint"]["k95_wrong_sign_jordan_rank"] == 128
assert packet["checks"] == {"total": 60, "failures": 0}
assert "two `U(32,32)` halves" in report and "full `U(64,64)`" in report
assert "SURVIVES_WITH_SCOPE_REPAIR" in review
assert not packet["verdict_change"] and not packet["canon_verdict_change"] and not packet["public_posture_change"]
assert not packet["p1_p2_p3_used"]
print("PASS: v0.173 K77 wedge-Shiab/southeast packet is internally consistent and fail-closed")
