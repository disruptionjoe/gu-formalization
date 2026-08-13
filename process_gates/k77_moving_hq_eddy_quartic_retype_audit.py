#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "lab/process/selected-k77-moving-hq-eddy-quartic-retype.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-moving-hq-eddy-quartic-retype-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-moving-hq-eddy-quartic-retype-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-moving-hq-eddy-quartic-source-return-2026-08-12.md").read_text()

assert registry["fixed_hq_radial_phase"] == "REAL_GAMMA_Q"
assert registry["fixed_hq_angular_phase"] == "I_GAMMA_H_PERP"
assert registry["wrong_phase_defect_rank"] == 128
assert registry["j_linearity_selected_coefficient"] == 1
assert registry["j_family_unselected_dimension"] == 20
assert registry["completed_exterior_leg_rank"] == 2
assert registry["quartic_coefficient_norm"].startswith("512*")
assert registry["physical_action_coefficient"] == "OPEN"
assert registry["stationary_nonzero_vacuum"] == "OPEN"
assert registry["new_datum"] is False
assert registry["P1_P2_P3"] == "UNCHANGED_AND_UNUSED"
for token in ("C_q(v)", "512", "quartic carrier", "20-dimensional"):
    assert token in report
for token in ("SURVIVES_SCOPED", "Symplectic", "smallest two-leg family"):
    assert token in review
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
for forbidden in ("HIGGS_DERIVED", "VACUUM_SELECTED", "NEW_DATUM", "SETTLED"):
    assert forbidden not in report
print("PASS: v0.199 preserves the phase-corrected unitary bank, zero-fit J completion, exact quartic carrier and physical-action fences.")
