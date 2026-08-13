#!/usr/bin/env python3
"""Scope audit for the selected K77 principal Ward reconciliation."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-principal-ward-gamma-epsilon-reconciliation-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-principal-ward-gamma-epsilon-reconciliation-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-principal-ward-gamma-epsilon-reconciliation-source-reinspection-2026-08-08.md").read_text(encoding="utf-8")
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.86.json").read_text(encoding="utf-8"))
registry = json.loads((ROOT / "lab/process/selected-k77-principal-ward-gamma-epsilon-reconciliation.json").read_text(encoding="utf-8"))
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text(encoding="utf-8"))

for phrase in (
    "direct torsion change from the metric",
    "rank three for timelike, spacelike and null",
    "fourth direction in v0.85",
    "primary sources do not make that identification",
    "moving Shiab/Hodge/curvature/density/observation response",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert source.count("SOURCE-CORRECTS") >= 2
assert "does not identify a spacetime diffeomorphism parameter" in source
assert "rank-three curvature packet" in source
assert registry["source_return"] == "SOURCE-CORRECTS"
for name in ("timelike", "spacelike", "null"):
    row = registry["causal_reconciliations"][name]
    assert row["direct_torsion_cancellation_rank"] == 0
    assert row["source_variable_curvature_packet_rank"] == 3
    assert row["source_longitudinal_response_zero"] is True
    assert row["conditional_gamma_response_rank"] == 4
    assert row["conditional_gamma_kernel_response_nonzero"] is True
    assert row["source_required_operator_rank"] == 3
    assert row["conditional_required_operator_rank"] == 4
assert registry["reconciliation"]["moving_operator"] == "NARROWED_FROM_RANK4_TO_RANK3__NOT_ELIMINATED"
assert registry["full_frechet_ward"] == "OPEN"
assert registry["reduced_symplectic_class"] == "OPEN"
assert set(registry["external_datum"].values()) == {"UNUSED"}
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert ledger["schema_version"] == "0.86"
assert ledger["source_return"] == "SOURCE-CORRECTS"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 3,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert contract["standing_ledger"]["ref"].endswith("v0.86.json")
assert "principal_ward_gamma_epsilon_reconciliation" in contract["active_scientific_directives"][0]
assert "CONSTRUCT_RANK3_MOVING_SHIAB_HODGE" in json.dumps(contract)
assert "Mandatory symplectic review" in review
assert "Krein/operator theory" in report
assert "Complex/path-integral" in report
assert "PASS_AFTER_RANK4_TO_RANK3_SCOPE_CORRECTION" in review
print("PASS selected K77 principal Ward gamma-epsilon reconciliation audit")
