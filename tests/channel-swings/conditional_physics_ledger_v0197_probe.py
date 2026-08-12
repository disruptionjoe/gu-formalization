#!/usr/bin/env python3
"""Strict ledger v0.197 migration and meter checks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def strict(relative: str):
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key} in {relative}")
            result[key] = value
        return result

    return json.loads((ROOT / relative).read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


ledger = strict("lab/process/conditional-physics-ledger-v0.197.json")
registry = strict("lab/process/selected-k77-varpi-radial-half-exchange-gate.json")
rows = {row["id"]: row for row in ledger["rows"]}

assert ledger["schema_version"] == "0.197"
assert ledger["predecessor"].endswith("v0.196.json")
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 1,
    "remaining_named_conditions": 4,
}
assert registry["result"]["full_u64_64_contains_radial_cell"] is True
assert registry["result"]["block_u32_32_product_contains_radial_cell"] is False
assert registry["result"]["pure_radial_self_wedge"] == 0
assert registry["result"]["selected_J"] == "OPEN_DIMENSION20_FAMILY"

expected = {
    "RA-E1": "TRACE_RADIAL_FULL_UNITARY_COMPONENT_AND_MOVING_SOLDERED_DOUBLET_EXACT",
    "RA-E3": "VERTICAL_FULL_UNITARY_FORM_CELL_AND_MOVING_DOUBLET_EXACT",
    "RA-E4": "ONE_TRACE_RADIAL_DOUBLET_DIRECTION_EXACT",
    "LT-SM5": "AMBIENT_CROSS_HALF_ZERO_ORDER_CELL_EXACT",
    "LT-SM6": "PURE_RADIAL_SELF_POTENTIAL_ZERO",
}
for row_id, token in expected.items():
    assert token in rows[row_id]["mapping_grade"], (row_id, rows[row_id]["mapping_grade"])

for collection in (ledger["migrations"], ledger["migration_history"]):
    current = [item for item in collection if item["to_version"] == "0.197"]
    assert {item["row_id"] for item in current} == set(expected)
    assert all(item["evidence"] == "selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md" for item in current)

assert ledger["next_work_queue"][0]["rank"] == 1
assert "complete moving U(3,2) doublet connection bank" in ledger["next_work_queue"][0]["why"]
assert registry["accounting"]["P1_P2_P3_used"] is False
assert registry["accounting"]["canon_verdict_change"] is False
print("PASS: ledger v0.197 preserves the headline meter and migrates exactly five Higgs/Yukawa distances around the full-unitary trace-radial component.")
