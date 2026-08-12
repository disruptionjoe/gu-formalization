#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
registry = json.loads((ROOT / "lab/process/selected-k77-minimal-moving-doublet-curvature-gate.json").read_text())
report = (ROOT / "explorations/conditional-build/selected-k77-minimal-moving-doublet-curvature-gate-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-minimal-moving-doublet-curvature-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-minimal-moving-doublet-curvature-source-return-2026-08-12.md").read_text()

assert registry["canonical_doublet_rank"] == 4
assert registry["soldering_kernel_dimension"] == 90
assert registry["distinct_clifford_commutators_nonzero"] == 6
assert registry["canonical_algebraic_curvature_nonzero_components"] == 0
assert registry["kernel_control_curvature_nonzero"] is True
assert registry["new_datum"] is False
assert registry["P1_P2_P3"] == "UNCHANGED_AND_UNUSED"
for token in ("common-leg", "90-dimensional", "action-owned nondecomposable lift"):
    assert token in report
for token in ("SURVIVES_SCOPED", "source-level no-go", "Symplectic"):
    assert token in review
assert "SOURCE_CONFIRMS" in source and "SOURCE_SILENT" in source
for forbidden in ("HIGGS_DERIVED", "VACUUM_SELECTED", "NEW_DATUM", "SETTLED"):
    assert forbidden not in report
print("PASS: v0.198 surfaces the exact zero canonical quartic, nonzero soldering-kernel control, source polarity and hostile fences.")
