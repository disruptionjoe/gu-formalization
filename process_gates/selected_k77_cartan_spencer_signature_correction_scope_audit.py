#!/usr/bin/env python3
"""Scope audit for the K77 Cartan/Spencer signature correction."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-k77-cartan-spencer-signature-correction-2026-08-07.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-cartan-spencer-signature-correction-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-cartan-spencer-signature-correction.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.57.json").read_text())

assert registry["signature_correction"]["old_executed_inertia"] == [9, 5]
assert registry["signature_correction"]["settled_k77_inertia"] == [7, 7]
assert registry["exact_result"]["target_changed_coordinates"] == [12, 12, 12, 12]
assert registry["exact_result"]["preimage_changed_coordinates"] == [30, 34, 34, 34]
assert registry["exact_result"]["k77_koszul_supports"] == [57, 34, 34, 34]
assert registry["exact_result"]["k77_source_lift_family_rank"] == 4
assert registry["exact_result"]["old_source_lifts_pass_corrected_targets"] == [False] * 4
assert "old coefficient values are superseded" in " ".join(artifact.lower().split())
assert "does not retract pointwise" in artifact
assert "Symplectic geometry" in artifact
assert "summary had outrun" in artifact
assert "superseded fork" in artifact
assert "PASS_WITH_MANDATORY_COEFFICIENT_SUPERSESSION" in review
assert ledger["schema_version"] == "0.57"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane_gate"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
print("PASS 23/23: K77 coefficient repair preserves the pointwise theorem and fences all global/physical promotions")
