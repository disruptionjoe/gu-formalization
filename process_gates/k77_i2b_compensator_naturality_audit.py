#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

report = (ROOT / "explorations/conditional-build/selected-k77-i2b-compensator-naturality-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-compensator-naturality-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-compensator-naturality-source-return-2026-08-12.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-i2b-compensator-naturality.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.205.json").read_text())

exact = registry["exact_results"]
assert exact["target_relevant_source_columns"] == 99463
assert exact["hodge_basis_masks"] == 16384
assert exact["selected_shiab_transport_failures"] == 0
assert exact["target_involution_transport_failures"] == 0
assert exact["transported_fixed_output_rank"] == 170
assert exact["transported_image_equals_direct_q12_image"] is True
assert exact["q13_target_transports_to_q12_target"] is True
assert exact["q12_fixed_projection_contains_q12_target"] is True
assert exact["q12_fixed_projection_contains_q13_target"] is False
assert exact["v0204_target_closure_bug_reproduced"] is True
assert "target-closure bug" in report
assert "Symplectic geometry" in review and "Controls that fired" in review
assert "SOURCE-CONFIRMS" in source and "REPO-CORRECTS" in source and "SOURCE-SILENT" in source
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.205"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.205"]) == 3

print(
    "PASS: q13/q12 compensator naturality and target admission are exact, "
    "v0.204's target-closure bug is corrected append-only, and action/Euler, "
    "datum, canon and physical promotion remain fenced."
)
