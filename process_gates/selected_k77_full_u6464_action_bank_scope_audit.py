#!/usr/bin/env python3
"""Scope audit for the selected K77 full pointwise u(64,64) action bank."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-full-u6464-action-bank-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-full-u6464-action-bank-review.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.77.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-full-u6464-action-bank.json").read_text())

for phrase in (
    "16,384 real directions",
    "pointwise",
    "not yet a theorem about global sections",
    "rank-complete",
    "P1/P2/P3 consumed: 0",
    "(4, 6, 0)",
):
    assert phrase in report, phrase

assert registry["exact_results"]["full_real_dimension"] == 16384
assert registry["exact_results"]["seed_grade_union"] == {"1": 14, "2": 59, "5": 476}
assert registry["exact_results"]["full_bank_rank"] == 14
assert registry["exact_results"]["normal_bank_rank"] == 10
assert registry["exact_results"]["raw_normal_gram_inertia"] == [4, 6, 0]
assert registry["exact_results"]["observed_normal_gram_inertia"] == [4, 6, 0]
assert registry["exact_results"]["observation_inverse_exact"] is True
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.77"
assert "SOURCE-SILENT" in registry["source_return"]
assert "Symplectic geometer" in review
assert "PASS AFTER GEOMETRY CORRECTION AND GLOBAL FENCE" in review
assert all(any(term in item for item in registry["boundary"])
           for term in ("adjoint-bundle", "observation", "BFV", "domain"))
print("PASS selected K77 full pointwise u(64,64) action bank scope audit")
