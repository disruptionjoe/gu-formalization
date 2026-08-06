#!/usr/bin/env python3
"""Fail-closed scope audit for the selected curvature graph six-versus-four gate."""

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


registry = strict(ROOT / "lab/process/selected-action-curvature-graph-six-versus-four.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.34.json")
report = (ROOT / "explorations/conditional-build/selected-action-curvature-graph-six-versus-four-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-curvature-graph-six-versus-four-review.md").read_text()

assert registry["status"] == "CONSTANT_TORSION_GRAPH_CURVATURE_EXACT__OFF_GRAPH_DBT_AND_GLOBAL_REDUCTION_OPEN"
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["layer0"]["tested_carrier"].startswith("SOURCE_NATIVE_CONSTANT_AUGMENTED_TORSION_GRAPH")
assert "ARBITRARY_AMBIENT_CURVATURE" in registry["layer0"]["not_tested"]
assert registry["exact_result"]["selected_riemann_response"] == "MINUS_TWO_TIMES_AMBIENT_EINSTEIN"
assert registry["exact_result"]["phi1_trace_ratio_to_scalar_curvature"] == 12
assert registry["exact_result"]["stationary_radial_value_at_kappa_one"] == "-1/312"
assert registry["exact_result"]["curvature_gain"] == "-1/26"
assert registry["exact_result"]["nonnull_total"] == {
    "rank": 30,
    "nullity": 4,
    "kernel": "GAUGE_EXACT",
}
assert registry["exact_result"]["null_total"] == {
    "rank": 28,
    "nullity": 6,
    "kernel": "GAUGE4_PLUS_PHYSICAL2",
}
assert registry["exact_result"]["off_graph_dbt_torsion_block"] == "OPEN"
assert registry["free_object_delta"] == 0
assert registry["quotient_count_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["schema_version"] == "0.34"
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "all six zero-jet nongauge directions are lifted off" in report
assert "two gravitational-wave polarizations" in report
assert "Why the ambient-kernel no-go survives" in report
assert "Mandatory symplectic-geometry lens" in review
assert "summary outrun" in review.lower()
assert "superseded object" in review
assert "not yet a\npresymplectic quotient" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_CURVATURE_GRAPH_SIX_VERSUS_FOUR_SCOPE_AUDIT_PASS")
