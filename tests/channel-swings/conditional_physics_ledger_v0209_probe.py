#!/usr/bin/env python3
"""Ledger v0.209 append-only correction gate."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def strict_json(path: Path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=unique)


ledger = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.209.json")
previous = strict_json(ROOT / "lab/process/conditional-physics-ledger-v0.208.json")

assert ledger["schema_version"] == "0.209"
assert previous["schema_version"] == "0.208"
assert ledger["denominator"] == previous["denominator"]
assert ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"]
assert ledger["residue"] == previous["residue"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 0,
    "conditions_opened": 2,
    "remaining_named_conditions": 2,
}
assert len([item for item in ledger["migrations"] if item["to_version"] == "0.209"]) == 3
assert len([item for item in ledger["migration_history"] if item["to_version"] == "0.209"]) == 3
rows = {row["id"]: row for row in ledger["rows"]}
for row_id in ("RA-E1", "RA-E3", "LT-SM6"):
    assert row_id in rows
    assert "ambient-fibre-trace-split-correction" in rows[row_id]["evidence"]
assert "nine fibre plus four soldering" in ledger["progress"]["meter"]
assert "C^(32,32)" in ledger["next_work_queue"][0]["why"]

print("PASS: ledger v0.209 is append-only, keeps headline/residue fixed, and records three correction edges.")
