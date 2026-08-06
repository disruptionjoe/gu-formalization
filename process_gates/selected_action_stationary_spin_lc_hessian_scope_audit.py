#!/usr/bin/env python3
"""Fail-closed scope audit for the stationary selected-action spin-LC Hessian."""

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


registry = strict(ROOT / "lab/process/selected-action-stationary-spin-lc-hessian.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.30.json")
report = (ROOT / "explorations/conditional-build/selected-action-stationary-spin-lc-hessian-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-stationary-spin-lc-hessian-review.md").read_text()

assert registry["status"].startswith("ACTION_SPIN_LC_RANK9")
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_coefficient_attribution"] == "REPOSITORY_DERIVED"
assert registry["layer0_correction"]["prior_rank_ten_object"] == "COORDINATE_CHRISTOFFEL_SYMBOL"
assert registry["layer0_correction"]["action_object"] == "SYMMETRIC_FRAME_SPIN_LEVI_CIVITA_CONNECTION"
assert registry["layer0_correction"]["same_object"] is False
assert registry["exact_result"]["action_spin_lc_rank"] == {"timelike": 9, "spacelike": 9, "null": 9}
assert registry["exact_result"]["action_spin_lc_kernel"] == "SPAN_K_TENSOR_K"
assert registry["exact_result"]["second_spin_lc_and_observation_jet_hessian_term"] == 0
assert registry["exact_result"]["selected_metric_hessian"]["timelike"] == {"rank": 9, "inertia_for_positive_kappa1": [3, 6, 1]}
assert registry["exact_result"]["selected_metric_hessian"]["spacelike"] == {"rank": 9, "inertia_for_positive_kappa1": [6, 3, 1]}
assert registry["exact_result"]["selected_metric_hessian"]["null"] == {"rank": 6, "inertia_for_positive_kappa1": [3, 3, 4]}
assert registry["exact_result"]["diffeomorphism_cross_rank"] == {"timelike": 3, "spacelike": 3, "null": 3}
assert registry["exact_result"]["isolated_spin_lc_block_is_diffeomorphism_radical"] is False
assert registry["exact_result"]["direct_curvature_full_ii_defect_observation_ward_completion"] == "OPEN"
assert registry["exact_result"]["diffeomorphism_odd_bv"] == "OPEN"
assert registry["exact_result"]["global_krein_green_domain"] == "OPEN"
assert registry["exact_result"]["bfv"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "coordinate Christoffel" in report and "symmetric-frame spin" in report
assert "rank-three diffeomorphism" in report
assert "symplectic" in review.lower()
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_STATIONARY_SPIN_LC_HESSIAN_SCOPE_AUDIT_PASS")
