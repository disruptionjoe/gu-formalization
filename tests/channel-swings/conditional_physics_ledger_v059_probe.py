#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.59."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.59.json")
prior = load("lab/process/conditional-physics-ledger-v0.58.json")
result = load("lab/process/selected-k77-full-reduction-quotient-reconciliation.json")
rows = {row["id"]: row for row in ledger["rows"]}
changed = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert ledger["schema_version"] == "0.59"
assert ledger["predecessor"].endswith("v0.58.json")
assert ledger["denominator"] == prior["denominator"]
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"] == prior["residue"]
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2, "conditions_opened": 0, "remaining_named_conditions": 2}
assert "SOURCE-CORRECTS" in ledger["source_return"]
assert "OBSERVATION_SECTION" in ledger["source_return"]
assert len(ledger["rows"]) == len(prior["rows"]) == 84
assert {item["row_id"] for item in ledger["wave_row_dispositions"]} == changed
assert all(item["change"] == "MIGRATED_DISTANCE_MAPPING_GRADE_AND_EVIDENCE_ONLY" for item in ledger["wave_row_dispositions"])
assert all(rows[row]["evidence"] == "selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md" for row in changed)
assert all("FULL_REDUCTION_PAIR_BASIC" in rows[row]["mapping_grade"] for row in changed)
assert all("FORGETFUL_QUOTIENT_FAILS" in rows[row]["mapping_grade"] for row in changed)
assert all("INVARIANT_REPLACEMENT_KILLED" in rows[row]["mapping_grade"] for row in changed)
assert all("raw-Upsilon" in rows[row]["distance"] for row in changed)
migrations = [item for item in ledger["migrations"] if item["from_version"] == "0.58" and item["to_version"] == "0.59"]
assert {item["row_id"] for item in migrations} == changed
assert all(item["meaning_changed"] is False for item in migrations)
assert "null characteristic screen" in ledger["next_work_queue"][0]["why"]
assert result["exact_result"]["full_reduction_pair_basic"] is True
assert result["exact_result"]["horizontal_plane_forgetful_quotient_basic"] is False
assert result["exact_result"]["invariant_replacement_reproducing_targets"] is False
assert result["constraint_surplus"]["new_fields"] == 0
assert result["constraint_surplus"]["transport_identities_counted"] == 0
assert result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

print("PASS 26/26: v0.59 preserves the meter, reconciles the two quotients, and routes raw-Upsilon plus the null screen")
