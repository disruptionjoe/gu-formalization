#!/usr/bin/env python3
"""Scope audit for the selected K77 source-graph basicness gate."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-k77-source-graph-basicness-2026-08-07.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-source-graph-basicness-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-source-graph-basicness.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.58.json").read_text())

assert "upstairs framed lift" in artifact
assert "not a basic" in artifact
assert "normal rotation" in artifact
assert "rank-four, 80-coordinate defect" in artifact
assert "three-dimensional block-invariant" in artifact
assert "UNBOOKABLE_ON_QUOTIENT" in artifact
assert "SOURCE-CONFIRMS" in artifact and "SOURCE-SILENT" in artifact
assert "gauge `epsilon`" in artifact and "observation/soldering" in artifact
assert "P1/P2/P3" in artifact and "unchanged and unused" in artifact
assert "raw-`Upsilon`" in artifact and "Euler/preboundary/symplectic" in artifact
assert "A smaller source-selected" in review
assert "Symplectic review" in review
assert "summary had outrun" not in review.lower()
assert "Summary outruns artifact charge — fired" in review
assert registry["exact_result"]["quotient_basicness"] is False
assert registry["exact_result"]["full_frame_three_patch_descent"] is True
assert registry["constraint_surplus"]["quotient_surplus"] == "UNBOOKABLE"
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

print("PASS 24/24: framed covariance is separated from stabilizer basicness, surplus, symplectic descent, datum, and posture")
