#!/usr/bin/env python3
"""Fail-closed scope audit for selected-action Ward-completion identifiability."""

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


registry = strict(ROOT / "lab/process/selected-action-ward-completion-identifiability.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.31.json")
report = (ROOT / "explorations/conditional-build/selected-action-ward-completion-identifiability-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-ward-completion-identifiability-review.md").read_text()

assert registry["status"].startswith("WARD_COMPLETION_TARGET_EXACT")
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_linear_algebra_attribution"] == "REPOSITORY_DERIVED"
assert registry["layer0"]["objects_are_distinct"] is True
assert registry["exact_result"]["symmetric_metric_coefficient_dimension"] == 55
assert registry["exact_result"]["diffeomorphism_symbol_rank"] == 4
assert registry["exact_result"]["ward_completion_linear_system_rank"] == 34
assert registry["exact_result"]["ward_unfixed_quotient_form_directions"] == 21
assert set(registry["exact_result"]["symmetric_completion_exists"].values()) == {True}
assert registry["exact_result"]["diagnostic_projector_completion"] == "EXACT_NONNATURAL_TARGET_ONLY__NOT_ACTION_DERIVED"
assert registry["exact_result"]["separately_diffeomorphism_invariant_block_can_cancel_spin_residual"] is False
assert set(registry["exact_result"]["observation_congruence_residual_rank"].values()) == {3}
assert registry["exact_result"]["same_i1b_direct_metric_coframe_completion"] == "OPEN"
assert registry["exact_result"]["diffeomorphism_odd_bv"] == "OPEN"
assert registry["exact_result"]["global_krein_green_domain"] == "OPEN"
assert registry["exact_result"]["bfv"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "rank 34" in report and "21-dimensional affine space" in report
assert "same first-layer action `I1B`" in report
assert "mandatory symplectic" in review and "geometry lens" in review
assert "summary outruns" in review.lower()
assert "superseded or mistyped" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_WARD_COMPLETION_IDENTIFIABILITY_SCOPE_AUDIT_PASS")
