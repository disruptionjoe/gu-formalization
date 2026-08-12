#!/usr/bin/env python3
"""Process audit for the v0.212 arbitrary-field Euler/Green bank."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(path: Path):
    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.212.json")
registry = strict(ROOT / "lab/process/selected-k77-i2b-arbitrary-field-euler-green-bank.json")
report = (ROOT / "explorations/conditional-build/selected-k77-i2b-arbitrary-field-euler-green-bank-2026-08-12.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-arbitrary-field-euler-green-bank-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-i2b-arbitrary-field-euler-green-bank-source-return-2026-08-12.md").read_text(encoding="utf-8")

assert ledger["updated_by"] == "RUN-20260812-153049-gu-i2b-arbitrary-field-euler-green-bank"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 1, "remaining_named_conditions": 2,
}
assert registry["status"].startswith("FIXED_HQ_ARBITRARY_CONNECTION_EULER")
assert registry["field_bank"]["euler_family_rank"] == 3
assert registry["green_bank"]["physical_row_rank"] == 0
assert registry["green_bank"]["off_family_nonzero_control"] is True
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "RESULT_SURVIVES" in review
assert "symplectic" in review.lower() and "analytic" in review.lower()
assert "P1" in report and "P2" in report and "P3" in report
assert "C^(32,32)+C^(32,32)" in report and "U(64,64)" in report
assert "not yet a kill" in report.lower()
print("PASS process audit: v0.212 arbitrary-field Euler/Green bank")
