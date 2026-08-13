#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

report = (ROOT / "explorations/conditional-build/selected-k77-i2b-real-structure-intertwining-defect-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-real-structure-intertwining-defect-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-real-structure-intertwining-defect-source-return-2026-08-12.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-i2b-real-structure-intertwining-defect.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.204.json").read_text())

exact = registry["exact_results"]
assert exact["target_relevant_source_columns"] == 99463
assert exact["fixed_output_rank"] == 170
assert exact["anti_fixed_output_rank"] == 195
assert exact["total_realified_intertwining_defect_rank"] == 390
assert exact["q13_fixed_projection_contains_target"] is True
assert exact["q12_fixed_projection_contains_target"] is False
assert exact["additive_galois_descent_obstruction_available"] is False
assert "q13" in report and "q12" in report and "characteristic-zero averaging" in report
assert "Symplectic geometry" in review and "Controls that fired" in review
assert "SOURCE-CONFIRMS" in source and "REPO-CORRECTS" in source and "SOURCE-SILENT" in source
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.204"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.204"]) == 3

print(
    "PASS: additive descent is excluded, the selected Shiab's exact mixed "
    "reality is recorded, and the q13 fixed-output escape fails held-out q12 "
    "naturality without canon, datum, or verdict promotion."
)
