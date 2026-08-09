#!/usr/bin/env python3
"""Fail-closed audit for the selected K77 first-action tangent-closure wave."""

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


registry = strict(ROOT / "lab/process/selected-k77-first-action-tangent-closure.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.121.json")
report = (ROOT / "explorations/conditional-build/selected-k77-first-action-tangent-closure-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-first-action-tangent-closure-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-first-action-tangent-source-reinspection-2026-08-09.md").read_text()

assert ledger["schema_version"] == "0.121"
assert ledger["predecessor"].endswith("v0.120.json")
mixed = registry["exact_result"]["grade1_grade2_first_action_hessian"]
assert mixed["shape"] == [1274, 196]
assert mixed["constant_component_nnz"] == 0
assert mixed["b_component_nnz"] == 0
assert mixed["t_component_nnz"] == 0
assert mixed["branch_ranks"] == [0, 0]
assert mixed["horizontal24_ranks"] == [0, 0]
assert mixed["offslice1250_ranks"] == [0, 0]
self_block = registry["exact_result"]["grade1_grade1_first_action_hessian"]
assert self_block["branch_ranks"] == [196, 196]
assert self_block["branch_inertias"] == [[97, 99, 0], [97, 99, 0]]
assert self_block["branches_equal"] is False
assert self_block["branches_galois_conjugate"] is True
assert registry["exact_result"]["minimal_321_disposition"] == "SURVIVES_THIS_CONNECTION_BLOCK_GATE__NOT_SELECTED_OR_COMPLETE"
assert registry["trap"]["bad_prefix_grade_counts"] == {"grade1": 28, "grade2": 168}
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "survives this connection-block gate" in report
assert "CANDIDATE_SURVIVES_WITH_SCOPE_NARROWING_AND_INDEXING_TRAP" in review
assert "symplectic" in review
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 2,
    "conditions_opened": 0,
    "remaining_named_conditions": 2,
}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-first-action-tangent-closure-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
]
print("PASS selected K77 first-action tangent-closure audit: 29/29")
