#!/usr/bin/env python3
"""Fail-closed scope and wiring audit for conditional physics ledger v0.1."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads((ROOT / path).read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.1.json")
strict("lab/process/conditional-physics-ledger-schema-v0.1.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.1.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-precontract-wave-0a-ledger-review.md").read_text()

assert ledger["denominator"]["canonical_target_count"] == 78
assert ledger["denominator"]["source_row_count"] == 86
assert ledger["denominator"]["alias_count"] == 8
assert ledger["taxonomy"]["unknown_kind_rule"] == "NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN"
assert ledger["progress"]["verdict_counts"] == {"SAME":32,"DIFFERS":18,"NEEDS":22,"OVER_DETERMINED":6}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["function_valued_at_least"] >= 19
assert ledger["residue"]["quotients_ranked"] == 0
assert len(ledger["over_determined_escalations"]) == 6
assert "Every future Build or Compose wave must name `ledger_row_changes`" in view
assert "HOSTILE POST-REVIEW: PASS AFTER REPAIR" in review
assert "100%" in review and "not completion" in review
print("PASS: ledger denominator, taxonomy, residue, escalation, and freshness wiring retained")
