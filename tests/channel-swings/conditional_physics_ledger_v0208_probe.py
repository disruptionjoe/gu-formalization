#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.208.json").read_text())

assert ledger["schema_version"] == "0.208"
assert ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_208"
assert ledger["predecessor"].endswith("v0.207.json")
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32,
    "DIFFERS": 19,
    "NEEDS": 26,
    "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 5
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.208"]) == 3
assert len([m for m in ledger["migration_history"] if m["to_version"] == "0.208"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "full-trace-orbit-derivative" in rows[row_id]["evidence"]
    assert "FULL_NORMALIZED_TRACE_ORBIT" in rows[row_id]["mapping_grade"] or "FULL_TRACE_ORBIT" in rows[row_id]["mapping_grade"]
assert "All 13 fixed-norm" in rows["RA-E1"]["distance"]
assert "C^(32,32) plus C^(32,32) carrier split" in rows["RA-E3"]["distance"]
assert "remaining independent" in rows["LT-SM6"]["distance"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS_MOVING_EPSILON")
assert "C32_32_WEYL_CARRIER_SPLIT" in ledger["source_return"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 1,
    "conditions_opened": 0,
    "remaining_named_conditions": 1,
}
assert ledger["next_work_queue"][0]["rank"] == 1
assert "complete fixed-norm normalized trace-q orbit" in ledger["next_work_queue"][0]["why"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]

print(
    "PASS: ledger v0.208 preserves headline accounting and migrates exactly "
    "three distances to the complete normalized trace-orbit derivative."
)
