#!/usr/bin/env python3
"""Scope audit for the selected K77 metric-section/Bianchi typing gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-metric-section-bianchi-typing-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-metric-section-bianchi-typing-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-metric-section-bianchi-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.80.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-metric-section-bianchi-typing.json").read_text())

for phrase in (
    "The v0.79 two-horn fork was too coarse",
    "metric-section Euler coordinates in complete field variables",
    "ranks `4,6,4`",
    "characteristic polynomial `lambda^2+4`",
    "No sixth quotient is booked",
    "P1/P2/P3 consumed:               0",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert registry["complete_receiver"]["complete_dual_conormal_rank"] == 10
assert registry["einstein_comparator"]["timelike_ranks"] == {
    "diffeomorphism": 4, "einstein": 6, "bianchi": 4}
assert registry["einstein_comparator"]["null_field_cohomology_dimension"] == 2
assert registry["einstein_comparator"]["selected_k77_operator_identified"] is False
assert registry["construction_disposition"]["full_conormal_bv_erasure"] == "REJECTED_AS_GR_PRESERVING_ROUTE"
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.80"
assert "Symplectic geometry and BV/BFV" in review
assert "PASS WITH EINSTEIN-COMPARATOR AND BOUNDARY-CHARGE FENCE" in review
assert "not the selected GU Euler operator" in review
print("PASS selected K77 metric-section/Bianchi typing scope audit")
