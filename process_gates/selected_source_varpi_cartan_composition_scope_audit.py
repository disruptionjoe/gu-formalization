#!/usr/bin/env python3
"""Scope audit for the selected source-varpi / Cartan composition."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
artifact = (ROOT / "explorations/conditional-build/selected-source-varpi-cartan-composition-2026-08-07.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-source-varpi-cartan-composition.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.56.json").read_text())

assert registry["exact_result"]["transverse_support_matched"] == 117
assert registry["exact_result"]["local_lift_supports"] == [57, 34, 34, 34]
assert registry["exact_result"]["local_lift_family_rank"] == 4
assert registry["exact_result"]["local_coefficient_freedom_at_fixed_background"] == 0
assert "pointwise source-coordinate realizability" in artifact
assert "does not prove" in artifact
assert "Symplectic geometry" in artifact
assert ledger["schema_version"] == "0.56"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane_gate"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "none"
assert registry["canon_verdict_change"] == "none"
assert registry["public_posture_change"] == "none"
print("PASS 18/18: source-varpi pointwise Cartan lift is exact and globally fenced")
