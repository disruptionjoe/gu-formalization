#!/usr/bin/env python3
"""Scope and provenance audit for the K77 Kosmann rank-three gate."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-kosmann-moving-shiab-rank3-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-kosmann-moving-shiab-rank3-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-kosmann-moving-shiab-rank3-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.87.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-kosmann-moving-shiab-rank3.json").read_text())

for phrase in (
    "Equal rank is not cancellation",
    "whole lower-order bivector gauge tangent",
    "does **not** yet close the physical spacetime diffeomorphism",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "Mandatory symplectic review" in review
assert "summary" in review.lower() and "superseded" in review.lower()
assert registry["exact_closure"] == {
    "internal_orbit_rank": 3,
    "moving_shiab_alone_cancels": False,
    "complete_lower_order_response_cancels": True,
    "fitted_parameters": 0,
    "wrong_lower_order_sign_rejected": True,
}
for name in ("timelike", "spacelike", "null"):
    assert registry["causal_results"][name]["matched_q_rank"] == 3
    assert registry["causal_results"][name]["completed_rank"] == 0
assert ledger["schema_version"] == "0.87"
assert ledger["source_return"] == "SOURCE-CONFIRMS"
assert ledger["frontier_delta"]["conditions_closed"] == 4
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
print("PASS selected K77 Kosmann moving-Shiab rank-three audit")
