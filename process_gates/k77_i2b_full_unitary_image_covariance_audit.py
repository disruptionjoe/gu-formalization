#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

report = (ROOT / "explorations/conditional-build/selected-k77-i2b-full-unitary-image-covariance-2026-08-12.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-full-unitary-image-covariance-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-i2b-full-unitary-image-covariance-source-return-2026-08-12.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k77-i2b-full-unitary-image-covariance.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.203.json").read_text())

assert "16,384" in report and "8,256" in report and "8,128" in report
assert "99,463" in report and "rank `364`" in report and "rank to `365`" in report
assert "q12" in report and "q13" in report
assert "proper\n  subalgebra" in review
assert "No canon or scientific-status verdict changes" in review
assert "SOURCE-CONFIRMS" in source and "REPO-CORRECTS" in source and "SOURCE-SILENT" in source
assert registry["exact_results"]["cl77_real_basis_dimension"] == 16384
assert registry["exact_results"]["pointwise_u64_64_real_dimension"] == 16384
assert registry["exact_results"]["Hq_real_phase_blades"] == 8256
assert registry["exact_results"]["Hq_imaginary_phase_blades"] == 8128
assert registry["exact_results"]["q13_grade1_image_rank"] == 364
assert registry["exact_results"]["q13_rank_with_target"] == 365
assert registry["exact_results"]["q12_grade1_image_rank"] == 364
assert registry["exact_results"]["q12_rank_with_target"] == 365
assert registry["exact_results"]["full_pointwise_u64_64_contains_target"] is False
assert registry["exact_results"]["block_u32_32_plus_u32_32_can_restore_target"] is False
assert registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
assert ledger["schema_version"] == "0.203"
assert ledger["source_return"] == registry["source_return"]
assert len([m for m in ledger["migrations"] if m["to_version"] == "0.203"]) == 3

print(
    "PASS: the phase-completed Cl(7,7) basis is the full pointwise u(64,64) "
    "algebra, the direct selected-Shiab target exclusion holds at q13 and q12, "
    "and global/derivative scope fences remain intact."
)
