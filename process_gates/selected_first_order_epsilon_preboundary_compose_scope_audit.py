#!/usr/bin/env python3
"""Fail-closed scope audit for selected first-order epsilon/preboundary Compose."""

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


registry = strict(ROOT / "lab/process/selected-first-order-epsilon-preboundary-compose.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.25.json")
report = (ROOT / "explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-first-order-epsilon-preboundary-compose-review.md").read_text()

assert registry["status"].startswith("SELECTED_FIXED_METRIC_EPSILON_PREBOUNDARY_COMPOSED")
assert registry["source"]["return_code"] == "SOURCE-CORRECTS"
assert registry["selected_product"]["row"] == ["comm", "symi", "symi"]
assert registry["selected_product"]["source_attribution"] == "NOT_ATTRIBUTED_TO_WEINSTEIN"
assert registry["selected_product"]["member_of_prior_eight_row_epsilon_domain"] is True
assert registry["composed_chain"]["principal_diagonal_rank"] == 0
assert registry["composed_chain"]["homogeneous_moving_shiab_generators"] == 91
assert registry["composed_chain"]["dirichlet_flux"] == 0
assert registry["independent_control"] == {"model": "EXACT_RATIONAL_ORIENTED_INTERVAL_SUMMATION_BY_PARTS", "unrestricted_flux": 11, "dirichlet_flux": 0}
assert registry["constraint_cost"] == {"fitted_coefficients": 0, "new_external_datum": 0, "residue_reduction": 0, "new_quotients": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "explicit unrestricted boundary flux" in report.lower()
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert "symplectic" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_FIRST_ORDER_EPSILON_PREBOUNDARY_COMPOSE_SCOPE_AUDIT_PASS")
