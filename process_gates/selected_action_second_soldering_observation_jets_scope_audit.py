#!/usr/bin/env python3
"""Fail-closed scope audit for selected-action second soldering/observation jets."""

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


registry = strict(ROOT / "lab/process/selected-action-second-soldering-observation-jets.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.29.json")
report = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-second-soldering-observation-jets-review.md").read_text()

assert registry["status"].startswith("SECOND_SPIN_LEVI_CIVITA")
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_jet_attribution"] == "REPOSITORY_DERIVED"
assert registry["exact_result"]["christoffel_second_metric_jet"] == "EXACT_NONZERO_SYMMETRIC"
assert registry["exact_result"]["symmetric_frame_second_spin_connection_jet"] == "EXACT_NONZERO_SYMMETRIC"
assert registry["exact_result"]["tetrad_postulate_through_mixed_order"] == "EXACT"
assert registry["exact_result"]["spin_connection_eta_skew_through_mixed_order"] == "EXACT"
assert registry["exact_result"]["observation_pure_section_second_frechet_jet"] == 0
assert registry["exact_result"]["observation_section_field_cross_jet"] == "EXACT_NONZERO"
assert registry["exact_result"]["spatial_second_section_jet_owner"] == "DERIVED_BY_TOTAL_DERIVATIVE"
assert registry["exact_result"]["nonlinear_formal_adjoint_euler_owner"] == "EXACT"
assert registry["exact_result"]["nonlinear_preboundary_owner"] == "EXACT"
assert registry["exact_result"]["direct_selected_action_metric_coefficients"] == "OPEN"
assert registry["exact_result"]["diffeomorphism_odd_bv"] == "OPEN"
assert registry["exact_result"]["bfv"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "Christoffel and spin connections" in report
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert "symplectic lens" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_SECOND_SOLDERING_OBSERVATION_JETS_SCOPE_AUDIT_PASS")
