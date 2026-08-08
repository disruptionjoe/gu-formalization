#!/usr/bin/env python3
"""Scope audit for the physical observation-section faithfulness gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-physical-section-faithfulness-gate-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-physical-section-faithfulness-gate-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-physical-section-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.79.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-physical-section-faithfulness-gate.json").read_text())

for phrase in (
    "A local observation section can have an exact holonomic",
    "spin four-manifold",
    "rank four and the exact ten-dimensional",
    "source-action witness",
    "No sixth quotient is booked",
    "P1/P2/P3 consumed:               0",
):
    assert phrase in report, phrase

assert "depends on topology" in source
assert "SOURCE-CORRECTS" in source
assert registry["topology"]["spin"] is True
assert registry["topology"]["lorentz_section"] is False
assert registry["exact_results"]["ordinary_pullback_rank"] == 4
assert registry["exact_results"]["conormal_kernel_rank"] == 10
assert registry["exact_results"]["action_conormal_witness_nonzero"] is True
assert registry["exact_results"]["action_conormal_witness_pullback_zero"] is True
assert registry["construction_fork"]["selected"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.79"
assert "Symplectic geometry and BV/BFV" in review
assert "PASS WITH ADMISSIBLE-SECTOR AND TWO-HORN CONSTRUCTION FENCE" in review
assert "dissolved" in review and "needs construction" in review
print("PASS selected K77 physical-section faithfulness scope audit")
