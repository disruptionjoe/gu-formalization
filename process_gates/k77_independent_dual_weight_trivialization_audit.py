#!/usr/bin/env python3
"""Fail-closed audit for ledger v0.175."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.175.json").read_text())
packet = json.loads((ROOT / "lab/process/selected-k77-independent-dual-weight-trivialization.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-independent-dual-weight-trivialization-2026-08-11.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-11-selected-k77-independent-dual-weight-trivialization-review.md").read_text()

assert ledger["schema_version"] == "0.175" and ledger["predecessor"].endswith("v0.174.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4, "conditions_opened": 1, "remaining_named_conditions": 3}
assert len(ledger["migration_history"]) == 6
assert {item["from_version"] for item in ledger["migration_history"]} == {"0.174"}
assert {item["to_version"] for item in ledger["migration_history"]} == {"0.175"}
assert packet["source_native_weight_invariant_dimension"] == 0
assert packet["normalized_representative"] == [1, 1, "11/12", "11/12"]
assert packet["checks"] == {"total": 43, "failures": 0}
assert packet["unit_cross_degree_blocks_preserved"] and packet["gauge_noether_transport"]
assert packet["observation_rank"] == 640 and packet["transported_observation_required"]
assert "constant nonzero scalar weights" in report
assert "SURVIVES_WITH_SCOPE_REPAIR" in review
assert "two `U(32,32)` halves" in report and "full `U(64,64)`" in report
assert not packet["verdict_change"] and not packet["booked_residue_change"] and not packet["quotient_change"]
assert not packet["canon_verdict_change"] and not packet["public_posture_change"] and not packet["p1_p2_p3_used"]
print("PASS: v0.175 independent-dual weight trivialization is internally consistent and fail-closed")
