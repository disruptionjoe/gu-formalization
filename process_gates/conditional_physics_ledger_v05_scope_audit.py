#!/usr/bin/env python3
"""Fail-closed wiring audit for conditional-physics ledger v0.5."""

import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]


def strict(relative: str):
    path = ROOT / relative

    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = strict("lab/process/conditional-physics-ledger-v0.5.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
registry = strict("lab/process/pre-shiab-gauss-defect-action-bv-symbol.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.5.md").read_text()
report = (ROOT / "explorations/conditional-build/pre-shiab-gauss-defect-action-bv-symbol-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-pre-shiab-gauss-defect-action-bv-symbol-review.md").read_text()

rows = {row["id"]: row for row in ledger["rows"]}
active = [row for row in rows.values() if row.get("row_status") != "SUPERSEDED"]

assert ledger["schema_version"] == "0.5"
assert ledger["predecessor"].endswith("conditional-physics-ledger-v0.4.json")
assert len(active) == 82 and len(rows) == 83
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 25, "OVER_DETERMINED": 6
}
assert ledger["residue"]["continuous_real"] == 83
assert ledger["residue"]["quotients_ranked"] == 1
assert "conditional local" in ledger["residue"]["quotients_ranked_scope"]
assert rows["LT-GR2c"]["verdict"] == "NEEDS"
assert rows["LT-GR2c"]["reason_kind"] == "MISSING_CONSTRUCTION"
assert "BV_QUOTIENT_RANK16_EXACT" in rows["LT-GR2c"]["mapping_grade"]
assert "GLOBAL_SOLDERING_WELD_NULL_DOMAIN_OPEN" in rows["LT-GR2c"]["mapping_grade"]

assert reaches_historical_snapshot(
    contract, "lab/process/conditional-physics-ledger-v0.5.json"
)

exact = registry["exact_results"]
assert exact["trace_reversed_frobenius_inertia"] == [6, 4]
assert exact["nonnull_einstein_symbol_rank"] == 6
assert exact["nonnull_diffeomorphism_tangent_rank"] == 4
assert exact["nonnull_repaired_hessian_rank_nonzero_gain"] == 16
assert exact["nonnull_BV_quotient_dimension"] == 16
assert exact["zero_gain_hessian_rank"] == 12
assert exact["null_non_gauge_characteristic_kernel_dimension"] == 6
assert registry["source_return"] == "SOURCE-SILENT"
assert registry["boundaries"]["data"] == "P1_P2_P3_UNCHANGED_UNUSED"

assert "not an ordinary symmetric tensor" in report
assert "SOURCE-SILENT" in report
assert "summary outruns the artifact" in review
assert "superseded or mistyped object" in review
assert "82/82" in view and "Quotients ranked: 1 conditional/local" in view
assert all(token in report for token in ("P1/P2/P3", "canon", "public posture"))

print("PASS: v0.5 wires the scoped current-I1B kill and conditional pre-Shiab non-null even-BV quotient to the global soldering/weld/null-domain gate without booking physical recovery")
