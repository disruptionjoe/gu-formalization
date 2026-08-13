#!/usr/bin/env python3
"""Process audit for the v0.210 radial LC / section-q-row composition."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.210.json")
registry = strict(ROOT / "lab/process/selected-k77-i2b-radial-lc-section-qrow-composition.json")
report = (ROOT / "explorations/conditional-build/selected-k77-i2b-radial-lc-section-qrow-composition-2026-08-12.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-radial-lc-section-qrow-composition-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-i2b-radial-lc-section-qrow-composition-source-return-2026-08-12.md").read_text(encoding="utf-8")

assert ledger["updated_by"] == "historical-investigation"
assert ledger["frontier_delta"]["conditions_closed"] == 2
assert registry["status"].startswith("LOCAL_FIRST_ORDER_COMPOSITION_PASSES")
assert "residual derivatives are nonzero" in report.lower()
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "SURVIVES_SCOPED" in review
assert "presymplectic" in review.lower() and "analytic" in review.lower()
assert "P1" in report and "P2" in report and "P3" in report
assert "C^(32,32)+C^(32,32)" in report and "U(64,64)" in report
print("PASS process audit: v0.210 radial LC / section-q-row composition")
