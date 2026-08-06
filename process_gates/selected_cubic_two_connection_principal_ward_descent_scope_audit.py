#!/usr/bin/env python3
"""Fail-closed scope audit for the two-connection principal Ward wave."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.22.json")
registry = strict(ROOT / "lab/process/selected-cubic-two-connection-principal-ward-descent.json")
report = (ROOT / "explorations/conditional-build/selected-cubic-two-connection-principal-ward-descent-2026-08-06.md").read_text()
summary = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.22.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-cubic-two-connection-principal-ward-descent-review.md").read_text()

assert ledger["schema_version"] == "0.22"
assert registry["source_return"] == "SOURCE-CONFIRMS"
assert registry["source_scope"].endswith("NOT_RANK_COEFFICIENT_OR_FULL_QUOTIENT")
assert registry["ledger_rows"] == ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
assert registry["difference_map"]["rank"] == 24
assert registry["difference_map"]["kernel_dimension"] == 24
assert registry["difference_map"]["kernel"] == "COMPLETE_DIAGONAL_CONNECTION_CARRIER"
assert registry["difference_map"]["unique_normalized_coefficients"] == [1, -1]
assert registry["exact_result"]["mixed_tt_kernel"] == "(14/3)*(p.q)*(h0:hm)"
assert registry["quotient_test"]["isolated_connection_gauge_block_rank"] == 5
assert registry["quotient_test"]["two_connection_diagonal_gauge_block_rank"] == 0
assert registry["quotient_test"]["lower_order_homogeneous_orbit"] == "OPEN"
assert registry["quotient_test"]["fifth_quotient"] == "NOT_COUNTED"
assert registry["cost"] == {"new_fields": 0, "new_coefficients": 0, "new_selectors": 0, "new_real_form_identifications": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "old rank-five computation remains correct" in summary
assert "SOURCE-CONFIRMS" in report
assert "Seven-axis audit" in report
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert "principal diagonal gauge block: rank zero" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_CUBIC_TWO_CONNECTION_PRINCIPAL_WARD_DESCENT_SCOPE_AUDIT_PASS")
