#!/usr/bin/env python3
"""Fail-closed scope audit for the moving gimmel/Hodge/frame owner."""

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


registry = strict(ROOT / "lab/process/moving-gimmel-hodge-frame-owner.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.26.json")
report = (ROOT / "explorations/conditional-build/moving-gimmel-hodge-frame-owner-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-moving-gimmel-hodge-frame-owner-review.md").read_text()

assert registry["status"].startswith("TT_DENSITY_ZERO")
assert registry["source"]["return_code"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_derivative_attribution"] == "REPOSITORY_DERIVED"
assert registry["gimmel"]["vertical_inertia"] == [6, 4, 0]
assert registry["gimmel"]["total_inertia"] == [7, 7, 0]
assert registry["tt_variation"]["density_derivative"] == 0
assert registry["tt_variation"]["fixed_frame_hodge"] == "NONZERO"
assert registry["frame_fusion"]["vector_frame_compensator"] == "A_EQUALS_MINUS_ONE_HALF_K"
assert registry["control"]["conformal_total_density_derivative"] == -8
assert registry["independent_exact_route"]["engine"] == "SAGE_10_9_RATIONAL_QUADRATIC_FORM"
assert registry["independent_exact_route"]["frame_compensation"] == "EXACT"
assert registry["constraint_cost"] == {"fitted_coefficients": 0, "new_external_datum": 0, "residue_reduction": 0, "new_quotients": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "owner fusion" in report.lower()
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert "symplectic" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("MOVING_GIMMEL_HODGE_FRAME_OWNER_SCOPE_AUDIT_PASS")
