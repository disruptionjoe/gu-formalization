#!/usr/bin/env python3
"""Process audit for the v0.214 real-primalizer phase gate."""

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


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.214.json")
registry = strict(ROOT / "lab/process/selected-k77-i2b-real-primalizer-phase-gate.json")
report = (ROOT / "explorations/conditional-build/selected-k77-i2b-real-primalizer-phase-gate-2026-08-12.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-12-selected-k77-i2b-real-primalizer-phase-gate-review.md").read_text(encoding="utf-8")
source = (ROOT / "lab/sources/selected-k77-i2b-real-primalizer-phase-gate-source-return-2026-08-12.md").read_text(encoding="utf-8")

assert ledger["updated_by"] == "historical-investigation"
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 1, "remaining_named_conditions": 2,
}
assert registry["exact_results"]["response_carrier_dimension"] == 1274
assert registry["exact_results"]["orthogonal_tensor_dimensions"] == {
    "Lambda3": 364, "trace_V": 14, "traceless_hook": 896,
}
assert registry["exact_results"]["current_nonnull_rank"] == 2
assert registry["exact_results"]["phase_even_nonnull_rank"] == 4
assert registry["exact_results"]["two_half_scalar_weight_max_rank"] == 2
assert registry["exact_results"]["phase_even_full_or_block_unitary_invariant"] is False
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "CONDITIONAL_RANK4_EXISTS" in review
assert "symplectic" in review.lower() and "analytic" in review.lower()
assert "P1/P2/P3" in report
assert "C^(32,32)+C^(32,32)" in report and "U(64,64)" in report
assert "not yet the source action" in report
assert "moving fundamental symmetry" in report and "coupled" in report.lower()
print("PASS process audit: v0.214 real-primalizer phase gate")
