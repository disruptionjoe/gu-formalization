#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.58."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(relative):
    def strict(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key} in {relative}")
            out[key] = value
        return out
    return json.loads((ROOT / relative).read_text(encoding="utf-8"), object_pairs_hook=strict)


ledger = load("lab/process/conditional-physics-ledger-v0.58.json")
prior = load("lab/process/conditional-physics-ledger-v0.57.json")
result = load("lab/process/selected-k77-source-graph-basicness.json")
rows = {row["id"]: row for row in ledger["rows"]}
changed = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert ledger["schema_version"] == "0.58"
assert ledger["predecessor"].endswith("v0.57.json")
assert ledger["denominator"] == prior["denominator"]
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"] == prior["residue"]
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1, "conditions_opened": 1, "remaining_named_conditions": 3}
assert "GAUGE_EPSILON_PROMOTED" in ledger["source_return"]
assert "SOURCE-SILENT" in ledger["source_return"]
assert len(ledger["rows"]) == len(prior["rows"]) == 84
assert {item["row_id"] for item in ledger["wave_row_dispositions"]} == changed
assert all(item["change"] == "MIGRATED_DISTANCE_MAPPING_GRADE_AND_EVIDENCE_ONLY" for item in ledger["wave_row_dispositions"])
assert all(rows[row]["evidence"] == "selected-k77-source-graph-basicness-2026-08-07.md" for row in changed)
assert all("UNFRAMED_BASICNESS_FAILS" in rows[row]["mapping_grade"] for row in changed)
assert all("epsilon" in rows[row]["distance"] and "stabilizer" in rows[row]["distance"] for row in changed)
migrations = [item for item in ledger["migrations"] if item["from_version"] == "0.57" and item["to_version"] == "0.58"]
assert {item["row_id"] for item in migrations} == changed
assert all(item["meaning_changed"] is False for item in migrations)
assert "epsilon" in ledger["next_work_queue"][0]["why"]
assert result["exact_result"]["full_frame_three_patch_descent"] is True
assert result["exact_result"]["quotient_basicness"] is False
assert result["constraint_surplus"]["quotient_surplus"] == "UNBOOKABLE"
assert result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

print("PASS 22/22: v0.58 preserves the headline meter, records exact framed descent, and fences failed quotient basicness")
