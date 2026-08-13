#!/usr/bin/env python3
"""Fail-closed audit for the selected K77 two-branch action-block port."""

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


registry = strict(ROOT / "lab/process/selected-k77-two-branch-action-block-port.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.119.json")
report = (ROOT / "explorations/conditional-build/selected-k77-two-branch-action-block-port-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-two-branch-action-block-port-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-two-branch-action-block-source-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.119"
assert ledger["predecessor"].endswith("v0.118.json")
assert registry["first_action_cross"]["branch_ranks"] == [91, 91]
assert registry["first_action_cross"]["branch_nonzero_entries"] == [182, 182]
assert registry["residual_zero_jet_varpi"]["branch_ranks"] == [1470, 1470]
assert registry["residual_zero_jet_varpi"]["branch_maps_equal"] is False
assert [registry["selected_principal_bank"][name]["rank"]
        for name in ("timelike", "spacelike", "null")] == [110, 110, 16]
assert registry["selected_principal_bank"]["complete_frechet"] == "OPEN"
assert registry["action_parents"]["selected"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "Principal-symbol equality is not complete Frechet equality" in report
assert "COMMON_PRINCIPAL_DISTINCT_LOWER_ORDER" in ledger["status"]
assert "complete\n`g/varpi/epsilon` Hessian port" in review
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 0,
    "remaining_named_conditions": 4,
}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-two-branch-action-block-port-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
]
print("PASS selected K77 two-branch action-block port audit: 21/21")
