#!/usr/bin/env python3
"""Fail-closed scope audit for the coupled diffeomorphism Ward retype."""

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


registry = strict(ROOT / "lab/process/selected-action-coupled-diffeomorphism-ward-retype.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.32.json")
report = (ROOT / "explorations/conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-coupled-diffeomorphism-ward-retype-review.md").read_text()

assert registry["status"].startswith("COUPLED_DIFFEO_ORBIT_CORRECTS")
assert registry["source_return"] == "SOURCE-CORRECTS"
assert registry["layer0"]["objects_are_distinct"] is True
assert set(registry["exact_result"]["connection_one_form_lie_symbol_rank"].values()) == {4}
assert set(registry["exact_result"]["coupled_generator_rank"].values()) == {4}
assert registry["exact_result"]["metric_only_ward_system"]["rank"] == 34
assert registry["exact_result"]["metric_only_ward_system"]["affine_dimension"] == 21
assert registry["exact_result"]["coupled_unknown_dimension"] == 296
assert registry["exact_result"]["coupled_count_scope"].startswith("MINIMAL_OBSERVED_HORIZONTAL")
assert registry["exact_result"]["coupled_fixed_metric_block_system"] == {"rank": 98, "affine_dimension": 198}
assert set(registry["exact_result"]["coupled_completion_preserving_metric_block_exists"].values()) == {True}
assert registry["exact_result"]["metric_metric_companion_required_by_ward"] is False
assert registry["exact_result"]["diagnostic_coupled_completion"] == "EXACT_NOT_ACTION_DERIVED"
assert registry["exact_result"]["actual_i1b_cross_and_connection_blocks"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "rank `98`" in report and "affine dimension `198`" in report
assert "mandatory symplectic-geometry lens" in review.lower()
assert "summary outrun" in review.lower()
assert "superseded or mistyped" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_COUPLED_DIFFEO_WARD_RETYPE_SCOPE_AUDIT_PASS")
