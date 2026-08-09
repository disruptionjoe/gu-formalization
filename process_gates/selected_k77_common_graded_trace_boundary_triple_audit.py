#!/usr/bin/env python3
"""Fail-closed audit for the K77 common graded trace boundary skeleton."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "lab/process/selected-k77-common-graded-trace-boundary-triple.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.116.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-common-graded-trace-boundary-triple-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-common-graded-trace-boundary-triple-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-common-graded-trace-source-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.116"
assert ledger["predecessor"].endswith("v0.115.json")
assert registry["graded_trace"]["canonical_form"] == "STRONG_NONDEGENERATE"
assert registry["graded_trace"]["H7_H8_uniform_identification"] is False
assert registry["boundary_triple_readiness"]["complete_action_owned_gauge_fixed_bulk_operator"] == "UNOWNED"
assert registry["boundary_triple_readiness"]["common_Green_inverse"] == "UNOWNED"
assert registry["boundary_triple_readiness"]["Krein_positive_physical_domain"] == "UNOWNED"
assert registry["relative_descent"]["physical_boundary_condition_selected"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "TWO_U32_32" in registry["action_parent"]
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "actual bulk domain unowned" in review.lower()
assert "trace space, polarization, boundary condition and" in review
assert "new physical fields: 0" in report
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-common-graded-trace-boundary-triple-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 1,
    "remaining_named_conditions": 2,
}
print("PASS selected K77 common graded trace boundary-triple audit: 20/20")
