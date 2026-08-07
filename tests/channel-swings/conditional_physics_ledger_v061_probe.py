#!/usr/bin/env python3
"""Integrity gate for conditional physics ledger v0.61."""

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


ledger = load("lab/process/conditional-physics-ledger-v0.61.json")
prior = load("lab/process/conditional-physics-ledger-v0.60.json")
result = load("lab/process/selected-k77-coupled-all-grade-upsilon-graph.json")
rows = {row["id"]: row for row in ledger["rows"]}
changed = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert ledger["schema_version"] == "0.61"
assert ledger["predecessor"].endswith("v0.60.json")
assert ledger["denominator"] == prior["denominator"]
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"] == prior["residue"]
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1, "conditions_opened": 0, "remaining_named_conditions": 1}
assert "SOURCE-CONFIRMS" in ledger["source_return"] and "SOURCE-SILENT" in ledger["source_return"]
assert len(ledger["rows"]) == len(prior["rows"]) == 84
assert {item["row_id"] for item in ledger["wave_row_dispositions"]} == changed
assert all(item["change"] == "MIGRATED_DISTANCE_MAPPING_GRADE_AND_EVIDENCE_ONLY" for item in ledger["wave_row_dispositions"])
assert all(rows[row]["evidence"] == "selected-k77-coupled-all-grade-upsilon-graph-2026-08-07.md" for row in changed)
assert all("UNIQUE_CONDITIONAL_ALL_GRADE_GRAPH" in rows[row]["mapping_grade"] for row in changed)
assert all("EULER" in rows[row]["distance"].upper() for row in changed)
migrations = [item for item in ledger["migrations"] if item["from_version"] == "0.60" and item["to_version"] == "0.61"]
assert {item["row_id"] for item in migrations} == changed
assert all(item["meaning_changed"] is False for item in migrations)
assert "Euler" in ledger["next_work_queue"][0]["why"]
exact = result["exact_result"]
assert exact["domain_dimension"] == exact["response_rank"] == 1470
assert exact["output_coordinate_support"] == 4330
assert exact["response_nullity"] == 0 and exact["response_cokernel_dimension"] == 2860
assert exact["all_four_exact"] is True and exact["target_family_rank"] == 4
assert exact["solution_supports"] == [71, 48, 48, 48]
assert exact["full_linearized_bianchi"] is True
assert exact["full_labelled_frame_descent"] is True
assert exact["omit_kappa_passes"] is False and exact["wrong_sign_kappa_passes"] is False
assert result["constraint_surplus"]["fixed_target_coefficient_freedom"] == 0
assert result["constraint_surplus"]["local_predictive_surplus"] == 0
assert result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

print("PASS 31/31: v0.61 preserves the meter, constructs the unique conditional all-grade graph, and routes observation Euler/preboundary")
