#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

report = (ROOT / "explorations/conditional-build/selected-k77-i2b-real-shiab-displasion-image-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-real-shiab-displasion-image-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-real-shiab-displasion-image-source-return-2026-08-12.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-i2b-real-shiab-displasion-image.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.202.json").read_text())

assert "99,463" in report
assert "rank\n`364`" in report and "rank to `365`" in report
assert "unrestricted complex" in report
assert "full source `U(64,64)`" in report
assert "two `U(32,32)`" in report
assert "P1/P2/P3: unchanged and unused" in report
assert "No canon or scientific-status verdict changes" in review
assert "SOURCE_CONFIRMS" in source and "SOURCE_SILENT" in source
assert registry["exact_results"]["fixed_Hq_real_source_columns"] == 99463
assert registry["exact_results"]["fixed_Hq_grade1_image_rank"] == 364
assert registry["exact_results"]["fixed_Hq_grade1_rank_with_target"] == 365
assert registry["exact_results"]["unrestricted_complex_contains_target"] is True
assert registry["exact_results"]["fixed_Hq_contains_target"] is False
assert registry["exact_results"]["two_connection_background"]["nonzero_kappa1_solution"] is False
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert registry["verdict"].startswith("DIRECT_FIXED_HQ_REAL_SHIAB_CANCELLATION_KILLED")
assert ledger["schema_version"] == "0.202"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.202"]) == 3

print(
    "PASS: direct fixed-Hq real selected-Shiab cancellation is excluded by a "
    "complete exact image theorem while complex, moving/full-unitary, jet and "
    "global routes remain correctly fenced."
)
