#!/usr/bin/env python3
"""Scope audit for the selected K77 action boundary coefficient bank."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
report = (ROOT / "explorations/conditional-build/selected-k77-action-boundary-coefficient-bank-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-action-boundary-coefficient-bank-review.md").read_text()
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.76.json").read_text())
registry = json.loads((ROOT / "lab/process/selected-k77-action-boundary-coefficient-bank.json").read_text())

for phrase in (
    "Cl1 + Cl2",
    "not the full `U(64,64)`",
    "not a global `tau_A0`",
    "P1/P2/P3 consumed: 0",
    "(4 positive, 6 negative, 0 null)",
    "(5 positive, 5 negative, 0 null)",
):
    assert phrase in report, phrase

assert registry["exact_results"]["normal_bank_rank"] == 10
assert registry["exact_results"]["observed_normal_rank"] == 10
assert registry["exact_results"]["raw_normal_gram_inertia"] == [4, 6, 0]
assert registry["exact_results"]["observed_normal_gram_inertia"] == [5, 5, 0]
assert registry["exact_results"]["observation_inverse_exact"] is True
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert ledger["schema_version"] == "0.76"
assert "SOURCE-SILENT" in registry["source_return"]
assert "Symplectic geometer" in review
assert "PASS AFTER NARROWING" in review
assert all(term in " ".join(registry["boundary"]) for term in ("U(64,64)", "BFV", "domain"))
print("PASS selected K77 action boundary coefficient bank scope audit")

