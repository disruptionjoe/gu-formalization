#!/usr/bin/env python3
"""Fail-closed scope audit for the selected augmented-torsion D3 wave."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.20.json")
registry = strict(ROOT / "lab/process/selected-cubic-augmented-torsion-d3-owner-decomposition.json")
report = (ROOT / "explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md").read_text()
summary = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.20.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-cubic-augmented-torsion-d3-owner-review.md").read_text()

assert ledger["schema_version"] == "0.20"
assert registry["source_return"] == "SOURCE-SILENT"
assert registry["ledger_rows"] == ["LT-GR2b", "LT-GR5", "LT-SM8"]
assert registry["exact_d3"]["trace_over_native_norm"] == "136/3"
assert registry["exact_d3"]["traceless_diagonal_over_native_norm"] == "-56/3"
assert registry["free_pencil"]["theta_rad_q0_qm_intrinsic"] == "ZERO"
assert registry["free_pencil"]["theta_rad_qm_qm_intrinsic"] == "-(56/3)*alpha_II^2*<v,*v>"
assert registry["row_disposition"]["LT-GR3"] == "UNCHANGED__DIRECT_CURVATURE_D3_NOT_COMPUTED"
assert registry["cost"] == {"new_fields": 0, "new_coefficients": 0, "new_selectors": 0, "new_real_form_identifications": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["function_valued_at_least"] == 19
assert ledger["residue"]["open_discrete_forks"] == 9
assert ledger["residue"]["quotients_ranked"] == 4
assert "It is not silently identified" in report
assert "Build rank one remains the selected cubic" in summary
assert "summary_outruns_artifact" in review
assert "rigor_defends_superseded_or_mistyped_object" in review
assert "symplectic_reduction_veto" in review
assert registry["wrong_real_form_comparator"]["imported"] is False
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"

print("SELECTED_CUBIC_AUGMENTED_TORSION_D3_OWNER_SCOPE_AUDIT_PASS")
