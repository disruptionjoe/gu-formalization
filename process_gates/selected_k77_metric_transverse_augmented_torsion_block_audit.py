#!/usr/bin/env python3
"""Scope audit for the selected K77 transverse augmented-torsion block."""

from pathlib import Path
import json

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-metric-transverse-augmented-torsion-block-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-metric-transverse-augmented-torsion-block-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-metric-transverse-augmented-torsion-block-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.85.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-metric-transverse-augmented-torsion-block.json").read_text())
contract = json.loads((ROOT / "lab/methods/research-evidence-contract-v1.0.json").read_text())

for phrase in (
    "delta T=-L_q h",
    "restriction to the six transverse metric directions is injective",
    "rank four in every causal class",
    "moving Shiab/Hodge/curvature/density/",
    "not constructed",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source
assert "SOURCE-SILENT" in source
assert "delta_g T" in source
assert registry["result"] == "LEVI_CIVITA_RANK9__TRANSVERSE_RANK6__PARTIAL_WARD_DEFECT_RANK4"
for name in ("timelike", "spacelike", "null"):
    row = registry["causal_blocks"][name]
    assert row["levi_civita_rank"] == 9
    assert row["diffeomorphism_rank"] == 4
    assert row["transverse_rank"] == 6
    assert row["transverse_levi_civita_rank"] == 6
    assert row["transverse_torsion_residual_rank"] == 6
    assert row["partial_ward_defect_rank"] == 4
assert registry["constraint_surplus"]["new_fields"] == 0
assert registry["constraint_surplus"]["new_continuous_coefficients"] == 0
assert registry["constraint_surplus"]["new_discrete_datum"] == 0
assert registry["constraint_surplus"]["source_derivation_claimed_for_complete_metric_block"] is False
assert registry["held_open"]["moving_shiab_hodge_curvature_density_observation_orbit_packet"].startswith("OPEN")
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert ledger["schema_version"] == "0.85"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.85.json"
)
assert "symplectic" in review
assert "Krein/operator theory" in report
assert "Complex/path-integral" in report
assert "PASS_WITH_PRINCIPAL_TRANSVERSE_AND_PARTIAL_WARD_SCOPE" in review
print("PASS selected K77 metric-transverse augmented-torsion block audit")
