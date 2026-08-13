#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.201.json").read_text())

assert ledger["schema_version"] == "0.201"
assert ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_201"
assert ledger["predecessor"].endswith("v0.200.json")
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
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.201"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "selected-k77-source-i2b-hq-stationarity" in rows[row_id]["evidence"]
assert "96(rho+r^2/3)^2" in rows["RA-E1"]["distance"]
assert "fourteen live transverse" in rows["LT-SM6"]["distance"]
assert "SC_ACT_04" in rows["RA-E3"]["mapping_grade"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS_SC_ACT_04")
assert "SOURCE_SILENT" in ledger["source_return"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]
assert ledger["next_work_queue"][0]["rank"] == 1
assert "fourteen transverse" in ledger["next_work_queue"][0]["why"]

print(
    "PASS: ledger v0.201 preserves headline accounting and migrates exactly "
    "three distances to the SC-ACT-04 transverse stationarity/reduction gate."
)
