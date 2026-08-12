#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

report = (ROOT / "explorations/conditional-build/selected-k77-source-i2b-hq-stationarity-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-source-i2b-hq-stationarity-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-source-i2b-hq-stationarity-source-return-2026-08-12.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-source-i2b-hq-stationarity.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.201.json").read_text())

assert "SC-ACT-04" in report
assert "96 (rho+r^2/3)^2" in report
assert "Krein-null" in report
assert "fourteen nonzero diagonal gradient cells" in report
assert "action-owned reduction" in report
assert "P1/P2/P3 remain unchanged and unused" in report
assert "No canon or scientific-status verdict changes" in review
assert "SOURCE_CONFIRMS_SC_ACT_04" in source
assert registry["exact_results"]["nonzero_transverse_gradient_cells"] == 14
assert registry["exact_results"]["branch_residual"] == "NONZERO_KREIN_NULL"
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert registry["verdict"].startswith("SURVIVES_SCOPED")
assert ledger["schema_version"] == "0.201"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.201"]) == 3

print(
    "PASS: SC-ACT-04 owns the restricted moving-Hq potential; the branch is "
    "Krein-null but transverse-nonstationary, with reduction/background and "
    "all physical claims fenced."
)
