#!/usr/bin/env python3
"""Fail-closed audit for the K77 branch-Hessian discriminator."""

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


registry = strict(ROOT / "lab/process/selected-k77-branch-hessian-discriminator.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.118.json")
report = (ROOT / "explorations/conditional-build/selected-k77-branch-hessian-discriminator-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-branch-hessian-discriminator-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-branch-hessian-source-reinspection-2026-08-09.md").read_text()
paths = (ROOT / "lab/process/path-dependencies.yaml").read_text()

assert ledger["schema_version"] == "0.118"
assert ledger["predecessor"].endswith("v0.117.json")
assert registry["reconstruction_plane"]["disposition"].startswith("NONINVARIANT")
assert registry["source_varpi_slice"]["first_action_class"].startswith("BOTH_NEGATIVE")
assert registry["source_varpi_slice"]["residual_square_class"].startswith("BOTH_POSITIVE_RANK_ONE")
assert registry["source_varpi_slice"]["selects_branch"] is False
assert registry["action_parents"]["selected"] is False
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"
assert "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source
assert "apparent Morse\ndifference is therefore not an invariant" in report
assert "at a critical point; away\nfrom one" in review
assert "Galois-conjugate reconstruction Hessians" in paths
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE",
    "conditions_closed": 1,
    "conditions_opened": 0,
    "remaining_named_conditions": 6,
}
assert {row["id"] for row in ledger["rows"]
        if row.get("evidence") == "selected-k77-branch-hessian-discriminator-2026-08-09.md"} == {
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
}
assert [entry["row_id"] for entry in ledger["migrations"][-6:]] == [
    "LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6",
]
print("PASS selected K77 branch-Hessian discriminator audit: 19/19")
