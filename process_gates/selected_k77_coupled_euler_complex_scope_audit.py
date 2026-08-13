#!/usr/bin/env python3
"""Scope audit for the selected K77 coupled Euler-complex gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-coupled-euler-complex-scope-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-coupled-euler-complex-scope-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-coupled-euler-complex-source-reinspection-2026-08-08.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.81.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-coupled-euler-complex-scope.json").read_text())

for phrase in (
    "not yet a closed ten-variable selected-action Euler complex",
    "34` source variables",
    "physical symbol cohomology is therefore zero",
    "helicity `+/-1`, not Einstein helicity `+/-2`",
    "defect has rank `4`",
    "affine dimension",
    "55-34=21",
    "P1/P2/P3 consumed:               0",
):
    assert phrase in report, phrase

assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert registry["first_layer"]["source_variable_dimension"] == 34
assert set(registry["first_layer"]["generic_physical_symbol_cohomology"].values()) == {0}
assert registry["first_layer"]["exceptional_N2"]["helicity_absolute_value"] == 1
assert registry["second_layer_metric_block"]["ward_defect_rank"] == 4
assert registry["composition"]["naive_first_plus_metric_second_ward_defect_rank"] == 4
assert registry["composition"]["formal_symmetric_completion"]["affine_solution_dimension"] == 21
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.81"
assert "Symplectic geometry and BV-BFV" in review
assert "Microlocal PDE" in review
assert "PASS WITH COUPLED-OWNER, MICROLOCAL AND SYMPLECTIC FENCES" in review
print("PASS selected K77 coupled Euler-complex scope audit")
