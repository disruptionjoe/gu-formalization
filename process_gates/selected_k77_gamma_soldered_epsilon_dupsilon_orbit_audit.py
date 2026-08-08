#!/usr/bin/env python3
"""Scope audit for the selected K77 gamma-soldered epsilon orbit."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-gamma-soldered-epsilon-dupsilon-orbit-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-gamma-soldered-epsilon-dupsilon-orbit-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-gamma-soldered-epsilon-dupsilon-orbit-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.84.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-gamma-soldered-epsilon-dupsilon-orbit.json").read_text())
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text())

for phrase in (
    "negative of the spin Levi-Civita",
    "rank three and the identical longitudinal kernel",
    "gamma_epsilon : C -> ad(P_H)",
    "Its four columns have exact rank four",
    "Six transverse physical metric columns",
    "source supplies its two endpoint types but does not state the identification",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source
assert "SOURCE-SILENT" in source
assert "gamma_epsilon(xi-flat)" in source
assert registry["result"] == "KOSMANN_RANK3_NO_GAIN__GAMMA_EPSILON_RANK4__COMMON_FIELD_PRINCIPAL_ORBIT_JR_ZERO"
for name in ("timelike", "spacelike", "null"):
    row = registry["causal_orbits"][name]
    assert row["kosmann_rank"] == 3
    assert row["gamma_input_rank"] == 4
    assert row["gamma_residual_rank"] == 4
    assert row["combined_orbit_rank"] == 4
    assert row["transverse_metric_dimensions_open"] == 6
assert registry["constraint_surplus"]["new_fields"] == 0
assert registry["constraint_surplus"]["new_continuous_coefficients"] == 0
assert registry["constraint_surplus"]["new_discrete_datum"] == 0
assert registry["constraint_surplus"]["source_derivation_claimed"] is False
assert registry["old_metric_diagnostic"]["disposition"] == "REVIVED_FOR_RECHECK__NOT_PROMOTED"
assert registry["held_open"]["complete_physical_D_g_Upsilon"].startswith("OPEN")
assert registry["held_open"]["lower_order_and_nonlinear_D_epsilon_Upsilon"] == "OPEN"
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert ledger["schema_version"] == "0.84"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 4,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert contract["standing_ledger"]["ref"].endswith("v0.84.json")
assert "latest_gamma_epsilon_orbit_evidence" in contract["active_scientific_directives"][0]
assert "CONSTRUCT_COMPLETE_PHYSICAL_DG_UPSILON_SIX_TRANSVERSE" in json.dumps(contract)
assert "symplectic" in review
assert "Krein/operator theory" in report
assert "Complex/path-integral" in report
assert "PASS_WITH_PRINCIPAL_ORBIT_AND_SOURCE_SILENCE_SCOPE" in review
print("PASS selected K77 gamma-soldered epsilon D-Upsilon orbit audit")
