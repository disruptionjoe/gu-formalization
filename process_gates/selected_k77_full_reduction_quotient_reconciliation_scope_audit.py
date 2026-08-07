#!/usr/bin/env python3
"""Scope audit for the K77 full-reduction quotient reconciliation."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-k77-full-reduction-quotient-reconciliation-2026-08-07.md").read_text()
artifact_flat = " ".join(artifact.split())
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-full-reduction-quotient-reconciliation-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-full-reduction-quotient-reconciliation.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.59.json").read_text())
object_map = (ROOT / "GEOMETER-VS-PHYSICS-OBJECTS.md").read_text()

assert "full labelled Clifford reduction" in artifact
assert "horizontal-plane-only quotient" in artifact
assert "scalar `U(1)`" in artifact
assert "acts trivially" in artifact
assert "rank four and 80 nonzero entries" in artifact
assert "invariant-replacement horn is closed" in artifact
assert "SOURCE-CORRECTS" in artifact and "SOURCE-SILENT" in artifact
assert "observation-section" in artifact and "Euler" in artifact
assert "transport equations" in artifact_flat and "not counted as surplus" in artifact_flat
assert "P1/P2/P3" in artifact and "unchanged and unused" in artifact
assert "symplectic geometry" in artifact
assert "configuration basicness" in review and "physical reduction" in review
assert "source-locus" in review.lower() or "source locus" in review.lower()
assert "summary outruns" in review
assert registry["exact_result"]["full_reduction_pair_basic"] is True
assert registry["exact_result"]["horizontal_plane_forgetful_quotient_basic"] is False
assert registry["exact_result"]["invariant_replacement_reproducing_targets"] is False
assert registry["constraint_surplus"]["new_fields"] == 0
assert registry["constraint_surplus"]["transport_identities_counted"] == 0
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert "Signature (7,7)" in object_map and "rival fork" in object_map

print("PASS 27/27: full-reduction basicness is separated from the forgetful failure, physical descent, surplus, datum, and posture")
