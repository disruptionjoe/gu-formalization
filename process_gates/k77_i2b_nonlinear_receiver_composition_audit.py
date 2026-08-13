#!/usr/bin/env python3
"""Process audit for the v0.211 nonlinear receiver composition."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.211.json")
registry = strict(ROOT / "lab/process/selected-k77-i2b-nonlinear-receiver-composition.json")
report = (ROOT / "explorations/conditional-build/selected-k77-i2b-nonlinear-receiver-composition-2026-08-12.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-nonlinear-receiver-composition-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-i2b-nonlinear-receiver-composition-source-return-2026-08-12.md").read_text(encoding="utf-8")

assert ledger["updated_by"] == "RUN-20260812-151325-gu-i2b-nonlinear-receiver-composition"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 1,
    "conditions_opened": 0, "remaining_named_conditions": 1,
}
assert registry["status"].startswith("NONLINEAR_PRODUCT_RECEIVER_EXACT")
assert registry["exact_results"]["product_total_rank"] == 5488
assert "ordinary four-dimensional" in report.lower()
assert "SOURCE-CORRECTS" in source and "SOURCE-SILENT" in source
assert "SURVIVES_SCOPED" in review
assert "symplectic" in review.lower() and "analytic" in review.lower()
assert "P1" in report and "P2" in report and "P3" in report
assert "C^(32,32)+C^(32,32)" in report and "U(64,64)" in report
assert registry["scope"]["arbitrary_field_i2b_euler"] == "OPEN"
print("PASS process audit: v0.211 nonlinear receiver composition")
