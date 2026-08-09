#!/usr/bin/env python3
"""Fail-closed audit for the K77 mixed-order bulk-operator admission gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "lab/process/selected-k77-bulk-operator-admission.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.117.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-bulk-operator-admission-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-bulk-operator-admission-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-bulk-operator-source-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.117"
assert ledger["predecessor"].endswith("v0.116.json")
assert registry["dependency_grammar"]["unique_componentwise_minimal_symmetric_DN_weight"] == [2, 1, 1]
assert registry["dependency_grammar"]["actual_top_coefficients"].startswith("UNTESTED")
assert registry["dependency_grammar"]["uniform_weight_two"].startswith("COMPATIBLE")
assert registry["operator_ownership"]["branch_specific_first_action_hessian"] == "UNOWNED"
assert registry["operator_ownership"]["branch_specific_second_action_jacobian"] == "UNOWNED"
assert registry["operator_ownership"]["gauge_fixing_and_bulk_ghost_operator"] == "UNOWNED"
assert registry["operator_ownership"]["operator_derived_H7_H8_trace"].startswith("UNOWNED")
assert registry["action_parents"]["selected_by_stationarity"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "not a principal-symbol theorem" in review
assert "kinematic target" in report
assert "new fields/coefficients/selectors/bundle classes/quotients: 0" in report
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-bulk-operator-admission-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 0,
    "remaining_named_conditions": 6,
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"
]
print("PASS selected K77 bulk-operator admission audit: 22/22")
