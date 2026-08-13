#!/usr/bin/env python3
"""Exact structural checks for conditional-physics ledger v0.88."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            assert key not in result, f"duplicate key {key!r}: {path}"
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict("lab/process/conditional-physics-ledger-v0.88.json")
prior = strict("lab/process/conditional-physics-ledger-v0.87.json")
registry = strict("lab/process/selected-k77-physical-diffeomorphism-split.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

assert ledger["schema_version"] == "0.88"
assert ledger["predecessor"].endswith("v0.87.json")
assert ledger["progress"]["mapped"] == prior["progress"]["mapped"] == 82
assert ledger["progress"]["verdict_counts"] == prior["progress"]["verdict_counts"]
assert ledger["residue"] == prior["residue"]
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 4,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert ledger["source_return"] == "SOURCE-CONFIRMS"
assert len(ledger["migrations"]) == len(prior["migrations"]) + 5
assert registry["exact_split"]["physical_family_rank"] == 4
assert registry["exact_split"]["metric_skew_kosmann_rank"] == 3
assert registry["exact_split"]["gamma_lift_required"] is False
assert registry["local_naturality"]["observation_graph"] == "EXACT"
assert registry["primitive_epsilon"]["action_frechet_ownership"] == "OPEN"
assert registry["scope_boundary"]["signature_ambient_horn"].startswith("OPEN_")
assert registry["external_datum"] == "P1/P2/P3_UNCHANGED_AND_UNUSED"
assert "76CADF61" in ledger["collision_disposition"]
assert contract["standing_ledger"]["ref"].endswith("v0.88.json")

changed = {item["row_id"] for item in ledger["wave_row_dispositions"]}
assert changed == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}
for row in ledger["rows"]:
    if row["id"] in changed:
        assert row["evidence"] == "selected-k77-physical-diffeomorphism-split-2026-08-08.md"
        assert "LOCAL" in row["mapping_grade"] or "local" in row["distance"]

print("PASS conditional physics ledger v0.88")
