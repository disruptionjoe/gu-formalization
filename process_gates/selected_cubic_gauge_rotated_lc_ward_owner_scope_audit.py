#!/usr/bin/env python3
"""Fail-closed scope audit for the selected LC/Ward owner wave."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.21.json")
registry = strict(ROOT / "lab/process/selected-cubic-gauge-rotated-lc-ward-owner.json")
report = (ROOT / "explorations/conditional-build/selected-cubic-gauge-rotated-lc-ward-owner-2026-08-06.md").read_text()
summary = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.21.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-cubic-gauge-rotated-lc-ward-owner-review.md").read_text()

assert ledger["schema_version"] == "0.21"
assert registry["source_return"] == "SOURCE-CONFIRMS"
assert registry["source_scope"].endswith("NOT_COEFFICIENT_OR_QUOTIENT")
assert registry["ledger_rows"] == ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
assert registry["exact_result"]["mixed_tt_kernel"] == "(14/3)*(p.q)*(h0:hm)"
assert registry["carrier_exhaustion"]["lc_gauss_radial_block"] == "ZERO_ON_24_BY_100"
assert registry["carrier_exhaustion"]["radial_hessian_full_k77_cl2"] == "ZERO_ON_1274_DIRECTIONS"
assert registry["carrier_exhaustion"]["lc_lc_bilinear_rank"] == 24
assert registry["quotient_test"]["gauge_gauge_block_rank"] == 5
assert registry["quotient_test"]["disposition"] == "NONZERO_REPRESENTATIVE_WARD_REQUIRED"
assert registry["cost"] == {"new_fields": 0, "new_coefficients": 0, "new_selectors": 0, "new_real_form_identifications": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "This does not contradict v0.20" in summary
assert "SOURCE-CONFIRMS" in report
assert "Seven-axis audit" in report
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert "rank-five connection-gauge block" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_CUBIC_GAUGE_ROTATED_LC_WARD_OWNER_SCOPE_AUDIT_PASS")
