#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.207.json").read_text())

assert ledger["schema_version"] == "0.207"
assert ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_207"
assert ledger["predecessor"].endswith("v0.206.json")
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
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.207"]) == 3
assert len([m for m in ledger["migration_history"] if m["to_version"] == "0.207"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "global-primalizer-descent" in rows[row_id]["evidence"]
assert "PPLUS_ASSOCIATED_DESCENT" in rows["RA-E1"]["mapping_grade"]
assert "GLOBAL_ASSOCIATED_ACTION_PRIMALIZER" in rows["RA-E3"]["mapping_grade"]
assert "GLOBAL_ASSOCIATED_EULER_PRIMALIZER" in rows["LT-SM6"]["mapping_grade"]
assert "without a chosen Spin frame" in rows["RA-E1"]["distance"]
assert "full U(64,64) versus two-U(32,32)" in rows["RA-E3"]["distance"]
assert "complete Euler/preboundary" in rows["LT-SM6"]["distance"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS_MOVING_EPSILON")
assert "ASSOCIATED_PPLUS_DESCENT" in ledger["source_return"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 1,
    "conditions_opened": 0,
    "remaining_named_conditions": 1,
}
assert ledger["next_work_queue"][0]["rank"] == 1
assert "arbitrary composite" in ledger["next_work_queue"][0]["why"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]

print(
    "PASS: ledger v0.207 preserves headline accounting and migrates exactly "
    "three distances to global associated P_plus descent and pure-frame dot P_plus."
)
