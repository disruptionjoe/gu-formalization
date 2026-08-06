#!/usr/bin/env python3
"""Fail-closed scope audit for the selected off-graph dBT principal-symbol gate."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-action-offgraph-dbt-principal-symbol.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.35.json")
report = (ROOT / "explorations/conditional-build/selected-action-offgraph-dbt-principal-symbol-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-selected-action-offgraph-dbt-principal-symbol-review.md").read_text()

assert registry["status"] == "ADJACENT_GRADE_DBT_EULER_LIVE__CURRENT_34_VARIABLE_TRUNCATION_NOT_ACTION_INVARIANT"
assert registry["source_return"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT"
assert registry["exact_result"]["same_grade_horizontal_cl2_raw_and_euler_ranks"] == {"timelike": 0, "spacelike": 0, "null": 0}
assert registry["exact_result"]["same_grade_full_cl2_raw_and_euler_ranks"] == {"timelike": 0, "spacelike": 0, "null": 0}
assert registry["exact_result"]["cl1_horizontal_cl2_formal_euler_cross_ranks"] == {"timelike": 12, "spacelike": 12, "null": 11}
assert registry["exact_result"]["parity_completed_offdiagonal_euler_ranks"] == {"timelike": 24, "spacelike": 24, "null": 22}
assert registry["exact_result"]["current_34_variable_source_truncation"] == "NOT_ACTION_INVARIANT_UNDER_DBT"
assert registry["free_object_delta"] == 0 and registry["quotient_count_delta"] == 0
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["schema_version"] == "0.35"
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84 and ledger["residue"]["quotients_ranked"] == 4
assert "formal-adjoint Euler symbol" in report
assert "current\n34-variable truncation is not invariant" in report
assert "constant-augmented-torsion graph result remains intact" in report
assert "Mandatory symplectic reading" in report
assert "summary outrun the artifact" in review.lower()
assert "superseded or mistyped object" in review.lower()
assert "symplectic" in review.lower()
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("SELECTED_ACTION_OFFGRAPH_DBT_PRINCIPAL_SYMBOL_SCOPE_AUDIT_PASS")
