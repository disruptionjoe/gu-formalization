#!/usr/bin/env python3
"""Fail-closed scope audit for intrinsic homogeneous Ward closure."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.23.json")
registry = strict(ROOT / "lab/process/selected-cubic-intrinsic-homogeneous-ward-closure.json")
report = (ROOT / "explorations/conditional-build/selected-cubic-intrinsic-homogeneous-ward-closure-2026-08-06.md").read_text()
summary = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.23.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-cubic-intrinsic-homogeneous-ward-closure-review.md").read_text()

assert ledger["schema_version"] == "0.23"
assert registry["source"]["return_code"] == "SOURCE-CONFIRMS"
assert registry["source"]["scope"].endswith("NOT_EXACT_WARD_OR_PHYSICS")
assert registry["ledger_rows"] == ["LT-GR1", "LT-GR2b", "LT-GR5", "LT-GR6", "LT-SM8"]
assert registry["production"]["bivector_generators"] == 91
assert registry["production"]["moving_shiab_covariance"] == 91
assert registry["production"]["cubic_ward_zero"] == 91
assert registry["production"]["quadratic_ward_zero"] == 91
assert registry["production"]["frozen_shiab_nonzero_defects"] == 4
assert registry["production"]["wrong_sign_nonzero_defects"] == 4
assert registry["production"]["radial_branch_nonvacuous"] is True
assert registry["independent_control"]["scope"] == "STRUCTURAL_CONTROL__NOT_FULL_K77"
assert registry["independent_control"]["frozen_defect"] == "-4"
assert registry["constraint_cost"]["fitted_coefficients"] == 0
assert registry["constraint_cost"]["new_external_datum"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "four nonzero\ndefects" in summary
assert "SOURCE-CONFIRMS" in report
assert "Seven-axis disposition" in report
assert "summary outruns artifact" in review
assert "superseded or mistyped object" in review
assert "Mandatory symplectic-geometry review" in review
assert "No fifth quotient" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_CUBIC_INTRINSIC_HOMOGENEOUS_WARD_CLOSURE_SCOPE_AUDIT_PASS")
