#!/usr/bin/env python3
"""Scope audit for append-only conditional-physics ledger v0.18."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.18.json")
assert ledger["schema_version"] == "0.18"
assert ledger["predecessor"].endswith("v0.17.json")
assert ledger["denominator"]["canonical_target_count"] == 82
assert ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4

rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}
assert rows["LT-SM8"]["verdict"] == "NEEDS"
assert rows["LT-SM8"]["reason_kind"] == "MISSING_CONSTRUCTION"
for row_id in ("LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"):
    assert rows[row_id]["evidence"] == "selected-cubic-reduced-numerator-completion-fork-2026-08-05.md"

migrations = [m for m in ledger["migrations"] if m["from_version"] == "0.17" and m["to_version"] == "0.18"]
assert [m["row_id"] for m in migrations] == ["LT-GR2b", "LT-GR3", "LT-GR5", "LT-SM8"]
assert all(m["meaning_changed"] is False for m in migrations)

print("CONDITIONAL_PHYSICS_LEDGER_V018_SCOPE_AUDIT_PASS")
