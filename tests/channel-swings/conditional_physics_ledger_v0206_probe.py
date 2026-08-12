#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.206.json").read_text())

assert ledger["schema_version"] == "0.206"
assert ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_206"
assert ledger["predecessor"].endswith("v0.205.json")
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
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.206"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "action-real-projection" in rows[row_id]["evidence"]
assert "PPLUS_ACTION_OWNED_AT_FIXED_REAL_EULER_GRADE" in rows["RA-E1"]["mapping_grade"]
assert "FIXED_REAL_ACTION_PRIMALIZER" in rows["RA-E3"]["mapping_grade"]
assert "FIXED_REAL_EULER_PRIMALIZER_ACTION_OWNED" in rows["LT-SM6"]["mapping_grade"]
assert "nonlinear residual" in rows["RA-E1"]["distance"]
assert "Spin/source-epsilon" in rows["RA-E3"]["distance"]
assert "moving projector" in rows["LT-SM6"]["distance"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS_RESIDUAL_NORM_SQUARE")
assert "NONLINEAR_RESIDUAL_REPLACEMENT_REFUTED" in ledger["source_return"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 1,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert ledger["next_work_queue"][0]["rank"] == 1
assert "primalizer" in ledger["next_work_queue"][0]["why"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]

print(
    "PASS: ledger v0.206 preserves headline accounting and migrates exactly "
    "three distances to fixed-real Euler ownership with nonlinear replacement fenced."
)
