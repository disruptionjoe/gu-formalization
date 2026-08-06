#!/usr/bin/env python3
"""Fail-closed scope audit for the selected source-variable zero-jet Hessian."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-action-source-variable-hessian-and-diffeomorphism-lift.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.33.json")
report = (ROOT / "explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-source-variable-hessian-and-diffeomorphism-lift-review.md").read_text()

assert registry["status"].startswith("ZERO_JET_SOURCE_VARIABLE_HESSIAN_EXACT")
assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["layer0_correction"]["source_variables"].startswith("METRIC_G_AND_INDEPENDENT_CONNECTION_VARPI")
assert registry["exact_result"]["tautological_full_slot_lie_response"] == "ZERO"
assert registry["exact_result"]["horizontal_lorentz_connection_carrier_dimension"] == 24
assert registry["exact_result"]["spin_lc_rank"] == 9
assert registry["exact_result"]["connection_principal_diffeomorphism_lift_rank"] == 3
assert registry["exact_result"]["complete_diffeomorphism_generator_rank"] == 4
assert registry["exact_result"]["zero_jet_source_variable_hessian"] == {
    "carrier_dimension": 34,
    "rank": 24,
    "nullity": 10,
    "gauge_rank": 4,
    "nongauge_nullity": 6,
}
assert registry["exact_result"]["both_coupled_ward_block_equations"] == "EXACT_ALL_THREE_CAUSAL_ORBITS"
assert registry["exact_result"]["full_i1b_derivative_curvature_density_observation_blocks"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["schema_version"] == "0.33"
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "rank 24 and nullity ten" in report
assert "six-versus-four" in report
assert "Mandatory symplectic-geometry lens" in review
assert "summary outrun" in review.lower()
assert "superseded object" in review
assert "not the full `I1B` Hessian" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_SOURCE_VARIABLE_HESSIAN_SCOPE_AUDIT_PASS")
