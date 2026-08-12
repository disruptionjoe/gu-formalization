#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "lab/process/selected-k77-hq-action-owner-potential.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-hq-action-owner-potential-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-hq-action-owner-potential-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-hq-action-owner-source-return-2026-08-12.md").read_text()

assert registry["moving_first_action_mass_coefficient"] == 0
assert registry["moving_first_action_cubic_coefficient"] == 0
assert registry["moving_eddy_hodge_square_coefficient"] == 4
assert registry["conditional_nonzero_branch"] == "r^2=-3*rho"
assert registry["orbit_flat_directions"] == 3
assert registry["eddy_square_action_owner"] == "SOURCE_GUIDED_BUT_NOT_COMPLETE_OR_SELECTED"
assert registry["new_datum"] is False
assert registry["P1_P2_P3"] == "UNCHANGED_AND_UNUSED"
for token in ("SC-ACT-01", "2(\\rho+r^2/3)^2", "r_*^2=-3\\rho", "20-dimensional"):
    assert token in report
for token in ("SURVIVES_SCOPED", "frozen", "Symplectic", "needs-recheck"):
    assert token in review
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
for forbidden in ("HIGGS_DERIVED", "VACUUM_SELECTED", "RHO_DERIVED", "SETTLED"):
    assert forbidden not in report
print("PASS: v0.200 preserves the first-action zero, conditional eddy-square Mexican hat, and action/background/physics fences.")
