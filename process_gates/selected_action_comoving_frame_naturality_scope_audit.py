#!/usr/bin/env python3
"""Fail-closed scope audit for selected-action co-moving-frame naturality."""

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


registry = strict(ROOT / "lab/process/selected-action-comoving-frame-naturality.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.27.json")
report = (ROOT / "explorations/conditional-build/selected-action-comoving-frame-naturality-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-comoving-frame-naturality-review.md").read_text()

assert registry["status"].startswith("PURE_FRAME_SELECTED_ACTION_NATURAL")
assert registry["source"]["return_code"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["source"]["exact_naturality_attribution"] == "REPOSITORY_DERIVED"
assert registry["hodge"]["tested_degrees"] == [1, 2]
assert registry["hodge"]["fixed_frame_derivative"] == "NONZERO"
assert registry["hodge"]["infinitesimal_isometry_naturality"] == "EXACT"
assert registry["phi"]["phi1_pure_frame_derivative"] == 0
assert registry["phi"]["phi2_pure_frame_derivative"] == 0
assert registry["clifford_scalar_pairing"]["comoving_derivative"] == 0
assert registry["clifford_scalar_pairing"]["global_krein_domain"] == "OPEN"
assert registry["selected_action"]["branch"] == ["comm", "symi", "symi"]
assert registry["selected_action"]["nonzero_witness"] is True
assert registry["selected_action"]["pure_frame_derivative"] == 0
assert registry["selected_action"]["physical_soldering_field_observation_derivative"] == "OPEN"
assert registry["constraint_cost"] == {"fitted_coefficients": 0, "new_external_datum": 0, "residue_reduction": 0, "new_quotients": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "-7/2" in report
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert "symplectic" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_COMOVING_FRAME_NATURALITY_SCOPE_AUDIT_PASS")
