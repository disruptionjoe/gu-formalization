#!/usr/bin/env python3
"""Scope audit for the selected K77 coupled all-grade Upsilon graph."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-k77-coupled-all-grade-upsilon-graph-2026-08-07.md").read_text()
artifact_flat = " ".join(artifact.split())
review = (ROOT / "lab/process/hostile-reviews/2026-08-07-selected-k77-coupled-all-grade-upsilon-graph-review.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-coupled-all-grade-upsilon-graph.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.61.json").read_text())

assert "R(\\delta A)" in artifact
assert "domain dimension                         1470" in artifact
assert "finite output coordinate support         4330" in artifact
assert "cokernel dimension in that support       2860" in artifact
assert "supports are `71,48,48,48`" in artifact
assert "target compatibility codimension" in artifact_flat
assert "zero local predictive surplus" in artifact
assert "not a derivation" in artifact
assert "P1/P2/P3" in artifact and "unchanged and unused" in artifact
assert "symplectic geometry" in artifact
assert "summary outruns" in review.lower()
assert "superseded or mistyped" in review.lower()
assert "arbitrary coordinate-wise counterterm" in review
exact = registry["exact_result"]
assert exact["domain_dimension"] == exact["response_rank"] == 1470
assert exact["output_coordinate_support"] == 4330
assert exact["response_nullity"] == 0
assert exact["independent_sage_flint_rank"] == 1470
assert exact["independent_sage_flint_nullity"] == 0
assert exact["response_cokernel_dimension"] == 2860
assert exact["all_four_exact"] is True
assert exact["old_curvature_only_lifts_equal_new"] is False
assert exact["omit_kappa_passes"] is False
assert exact["wrong_sign_kappa_passes"] is False
assert exact["grade3_output_plant_in_image"] is False
assert exact["full_linearized_bianchi"] is True
assert exact["full_labelled_frame_descent"] is True
assert registry["constraint_surplus"]["new_fields"] == 0
assert registry["constraint_surplus"]["new_local_coefficients"] == 0
assert registry["constraint_surplus"]["local_predictive_surplus"] == 0
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert "Euler" in ledger["next_work_queue"][0]["why"]

print("PASS 37/37: source response, conditional target, independent rank, cokernel, surplus, Bianchi, labelled descent, and symplectic scope remain separated")
