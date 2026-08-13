#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.202.json").read_text())

assert ledger["schema_version"] == "0.202"
assert ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_202"
assert ledger["predecessor"].endswith("v0.201.json")
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
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.202"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3

rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "selected-k77-i2b-real-shiab-displasion-image" in rows[row_id]["evidence"]
assert "proven unsupplyable" in rows["RA-E1"]["distance"]
assert "source-full-unitary" in rows["RA-E3"]["distance"]
assert "forces kappa_1=0" in rows["LT-SM6"]["distance"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS_SWERVATURE")
assert "SOURCE_SILENT" in ledger["source_return"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 1,
    "remaining_named_conditions": 4,
}
assert ledger["next_work_queue"][0]["rank"] == 1
assert "source-full U64,64 or two U32,32" in ledger["next_work_queue"][0]["why"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]

print(
    "PASS: ledger v0.202 preserves headline accounting and migrates exactly "
    "three distances after excluding direct fixed-Hq real Shiab cancellation."
)
