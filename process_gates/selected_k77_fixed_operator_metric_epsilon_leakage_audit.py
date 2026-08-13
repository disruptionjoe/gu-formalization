#!/usr/bin/env python3
"""Fail-closed audit for the fixed-operator metric/epsilon leakage wave."""

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


registry = strict(ROOT / "lab/process/selected-k77-fixed-operator-metric-epsilon-leakage.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.122.json")
report = (ROOT / "explorations/conditional-build/selected-k77-fixed-operator-metric-epsilon-leakage-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-fixed-operator-metric-epsilon-leakage-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-metric-epsilon-hessian-source-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.122"
assert ledger["predecessor"].endswith("v0.121.json")
ranks = registry["exact_result"]["rank_pattern_all_three_causal_representatives_both_branches"]
assert ranks == {
    "full": {"metric": 9, "epsilon": 91, "combined": 97},
    "horizontal24": {"metric": 9, "epsilon": 6, "combined": 12},
    "offslice1250": {"metric": 4, "epsilon": 88, "combined": 89},
}
assert registry["exact_result"]["branch_rank_equality"] is True
assert registry["exact_result"]["causal_rank_equality"] is True
assert registry["exact_result"]["fixed_operator_321_disposition"] == "LEAKS__SHORTCUT_KILLED"
assert registry["exact_result"]["total_source_321_disposition"].startswith("OPEN__")
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "rank-89 off-slice target" in report
assert "TOTAL_SOURCE_DISPOSITION_OPEN" in review
assert "symplectic" in review and "analytic_krein" in review
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 1,
    "conditions_opened": 1,
    "remaining_named_conditions": 2,
}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-fixed-operator-metric-epsilon-leakage-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
]
print("PASS selected K77 fixed-operator metric/epsilon leakage audit: 24/24")
