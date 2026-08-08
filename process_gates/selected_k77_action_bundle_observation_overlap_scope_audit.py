#!/usr/bin/env python3
"""Scope audit for selected K77 action/observation bundle overlap."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-action-bundle-observation-overlap-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-action-bundle-observation-overlap-review.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.78.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-action-bundle-observation-overlap.json").read_text())

for phrase in (
    "noncommuting three-patch",
    "recomputed",
    "Freezing either one",
    "left-invertibility alone is not promoted to no leakage",
    "does **not** construct an integrable physical observation section",
    "P1/P2/P3 consumed: 0",
):
    assert phrase in report, phrase

assert registry["exact_results"]["transitions_noncommuting"] is True
assert registry["exact_results"]["patchwise_action_banks_recomputed"] is True
assert registry["exact_results"]["seed_direct_action_overlap"] is True
assert registry["exact_results"]["heldout_direct_action_overlap"] is True
assert registry["exact_results"]["no_leakage_projector_direct"] is True
assert registry["controls"]["frozen_observation_receiver"] == "FIRED"
assert registry["controls"]["frozen_no_leakage_projector"] == "FIRED"
assert registry["controls"]["hidden_covector_under_left_inverse"] == "FIRED"
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.78"
assert "SOURCE-SILENT" in registry["source_return"]
assert "Symplectic geometer" in review
assert "PASS WITH FINITE-ATLAS AND PHYSICAL-SECTION FENCE" in review
assert all(any(term in item for item in registry["boundary"])
           for term in ("observation-section", "pullback", "BFV", "domain"))
print("PASS selected K77 action-bundle observation overlap scope audit")
