#!/usr/bin/env python3
"""Scope audit for the K77 total raw-Upsilon and labelled null screen."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-k77-total-upsilon-null-screen-2026-08-07.md").read_text()
artifact_flat = " ".join(artifact.split())
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-total-upsilon-null-screen-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-total-upsilon-null-screen.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.60.json").read_text())

assert "Upsilon_B=Shiab(F_A)+kappa_1 T" in artifact
assert "full linearized covariant Bianchi identity" in artifact
assert "odd-curvature packet alone does not satisfy" in artifact
assert "rank 12" in artifact and "signature `(6,6)`" in artifact
assert "10 -> 6 -> 2" in artifact
assert "rank four" in artifact
assert "grade-one" in artifact and "grade-two" in artifact
assert "without ever dividing by its zero norm" in artifact_flat
assert "reciprocal null label" in artifact
assert "counted as independent constraints" in artifact_flat and "constraint surplus" in artifact_flat
assert "P1/P2/P3" in artifact and "unchanged and unused" in artifact
assert "symplectic geometry" in artifact
assert "summary outruns" in review
assert "superseded or mistyped" in review
assert "ambient screen is not a physical quotient" in review.lower()
assert registry["exact_result"]["full_linearized_superconnection_bianchi"] is True
assert registry["exact_result"]["odd_curvature_only_bianchi"] is False
assert registry["exact_result"]["curvature_only_grade2_graph_cancels"] is True
assert registry["exact_result"]["total_raw_upsilon_graph_natural"] is False
assert registry["exact_result"]["total_raw_upsilon_residual_family_rank"] == 4
assert registry["exact_result"]["ambient_null_screen_rank"] == 12
assert registry["exact_result"]["ambient_null_screen_signature"] == [6, 6]
assert registry["exact_result"]["forgetful_screen_basic"] is False
assert registry["constraint_surplus"]["new_fields"] == 0
assert registry["constraint_surplus"]["bianchi_identities_counted"] == 0
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}

print("PASS 32/32: Bianchi, total raw Upsilon, ambient screen, 4D quotient, symplectic scope, surplus, datum, and posture remain correctly separated")
