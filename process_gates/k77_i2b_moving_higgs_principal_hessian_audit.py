#!/usr/bin/env python3
"""Process audit for the v0.213 moving-Higgs principal Hessian."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.213.json")
registry = strict(ROOT / "lab/process/selected-k77-i2b-moving-higgs-principal-hessian.json")
report = (ROOT / "explorations/conditional-build/selected-k77-i2b-moving-higgs-principal-hessian-2026-08-12.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-moving-higgs-principal-hessian-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-i2b-moving-higgs-principal-hessian-source-return-2026-08-12.md").read_text(encoding="utf-8")

assert ledger["updated_by"] == "historical-investigation"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 1, "remaining_named_conditions": 2,
}
assert registry["status"].startswith("FIRST_GREEN_ZERO_BUT_SECOND_PRINCIPAL_HESSIAN_RANK2")
assert registry["selected_principal_hessian"]["nonnull_symbol_rank"] == 2
assert registry["selected_principal_hessian"]["radical_responses_nonzero"] is True
assert registry["controls"]["full_timelike_gram_rank"] == 182
assert registry["controls"]["displayed_channel_rank_four_count"] == 0
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "RESULT_SURVIVES" in review
assert "symplectic" in review.lower() and "analytic" in review.lower()
assert "P1/P2/P3" in report
assert "C^(32,32)+C^(32,32)" in report and "U(64,64)" in report
assert "incomplete, not dead" in report
assert "rank four" in report.lower() and "Q_B" in report
print("PASS process audit: v0.213 moving-Higgs principal Hessian")
