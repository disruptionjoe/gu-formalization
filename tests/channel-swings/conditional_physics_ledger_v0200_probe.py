#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.200.json").read_text())

assert ledger["schema_version"] == "0.200"
assert ledger["predecessor"].endswith("v0.199.json")
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 5
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.200"]) == 3
assert len(ledger["wave_row_dispositions"]) == 3
rows = {row["id"]: row for row in ledger["rows"]}
for row in ("RA-E1", "RA-E3", "LT-SM6"):
    assert "selected-k77-hq-action-owner-potential" in rows[row]["evidence"]
assert "first action is blind" in rows["RA-E1"]["distance"]
assert "2(rho+r^2/3)^2" in rows["LT-SM6"]["distance"]
assert ledger["source_return"].startswith("SOURCE_CONFIRMS")
assert "SOURCE_SILENT" in ledger["source_return"]
assert "P1/P2/P3 remain unchanged" in ledger["residue"]["meter"]
print("PASS: ledger v0.200 preserves headline accounting and migrates exactly three distances to the second-action/background/physical-reduction gate.")
