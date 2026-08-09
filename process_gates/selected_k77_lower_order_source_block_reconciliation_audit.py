#!/usr/bin/env python3
"""Fail-closed audit for the selected K77 lower-order source-block wave."""

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


registry = strict(ROOT / "lab/process/selected-k77-lower-order-source-block-reconciliation.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.120.json")
report = (ROOT / "explorations/conditional-build/selected-k77-lower-order-source-block-reconciliation-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-lower-order-source-block-reconciliation-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-lower-order-source-block-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.120"
assert ledger["predecessor"].endswith("v0.119.json")
assert registry["exact_result"]["raw_residual_zero_both_branches"] is True
assert registry["exact_result"]["lower_epsilon_coefficient"] == "-b+360*(b+t)^2"
assert registry["exact_result"]["epsilon_branch_ranks"] == [91, 91]
assert registry["exact_result"]["branch_lower_coefficients_positive"] is True
assert registry["exact_result"]["metric_fixed_varpi"]["transverse_ranks"] == {
    "timelike": 6, "spacelike": 6, "null": 6,
}
assert registry["exact_result"]["metric_fixed_varpi"]["full_levi_civita_first_jet_rank"] == 20
assert registry["action_parents"]["selected"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "A zero residual therefore need not have a zero derivative" in report
assert "CANDIDATE_SURVIVES_WITH_TWO_LAYER0_CORRECTIONS" in review
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-lower-order-source-block-reconciliation-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
]
assert registry["controls"]["transgression_packet_equals_raw_residual"] == "REJECTED"
print("PASS selected K77 lower-order source-block reconciliation audit: 21/21")
