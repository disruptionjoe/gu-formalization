#!/usr/bin/env python3
"""Scope audit for the selected K77 common-field D-Upsilon varpi block."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-common-field-dupsilon-varpi-block-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-common-field-dupsilon-varpi-block-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-common-field-dupsilon-varpi-block-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.83.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-common-field-dupsilon-varpi-block.json").read_text())
contract = json.loads((ROOT / "lab/process/functional-channel-operating-contract-v1.0.json").read_text())

for phrase in (
    "24-dimensional horizontal Lorentz-connection carrier",
    "grade 1: 22",
    "grade 2: 24",
    "grade 5: 10",
    "rank(J_g D)<=3",
    "complementary projector has rank six",
    "fixed-`epsilon` `(g,varpi)` horn",
    "Xi=D_omega Upsilon",
    "not the field derivative with respect to `epsilon`",
    "P1/P2/P3 remain unused",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source
assert "SOURCE-SILENT" in source
assert "D_epsilon Upsilon" in source
assert registry["result"] == "SOURCE_HORIZONTAL_VARPI_DUPSILON_BLOCK_RANK24__DIFFEO_RESPONSE_RANK3__SIX_TRANSVERSE_METRIC_COLUMNS_UNSELECTED"
assert registry["varpi_block"] == {
    "domain_dimension": 24,
    "rank": 24,
    "output_support": 56,
    "output_grade_counts": {"1": 22, "2": 24, "5": 10},
}
assert {name: row["residual_rank"] for name, row in registry["causal_orbits"].items()} == {
    "timelike": 3,
    "spacelike": 3,
    "null": 3,
}
assert registry["fixed_epsilon_fork"]["transverse_metric_dimensions_unselected"] == 6
assert registry["fixed_epsilon_fork"]["old_metric_ward_load_rank"] == 4
assert registry["fixed_epsilon_fork"]["old_metric_diagnostic_import"] == "REJECTED_ON_FIXED_EPSILON_G_VARPI_HORN"
assert registry["fixed_epsilon_fork"]["source_epsilon_revival"].startswith("OPEN")
assert registry["residual_pairing"] == {
    "K_star": "OPEN",
    "formal_adjoint": "OPEN",
    "green_concomitant": "OPEN",
    "stationary_gram_hessian": "OPEN",
}
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert ledger["schema_version"] == "0.83"
assert contract["standing_ledger"]["ref"].endswith("v0.83.json")
assert "CONSTRUCT_PHYSICAL_METRIC_PLUS_SOURCE_EPSILON" in json.dumps(contract)
assert "symplectic geometry" in review
assert "Krein/operator theory" in report
assert "Complex/path-integral" in report
assert "PASS_WITH_HORN_SCOPE" in review
print("PASS selected K77 common-field D-Upsilon varpi block audit")
