#!/usr/bin/env python3
"""Fail-closed scope audit for conditional physics ledger v0.2."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)
    return json.loads((ROOT / path).read_text(), object_pairs_hook=pairs)


v2 = strict("lab/process/conditional-physics-ledger-v0.2.json")
gate = strict("lab/process/full-domain-shiab-observed-einstein-receiver.json")
view = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.2.md").read_text()
report = (ROOT / "explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-full-domain-shiab-observed-receiver-review.md").read_text()

rows = {row["id"]: row for row in v2["rows"]}
assert v2["schema_version"] == "0.2"
assert v2["predecessor"].endswith("conditional-physics-ledger-v0.1.json")
assert len(v2["migrations"]) == 1
assert {m["row_id"] for m in v2["migrations"]} == {"LT-GR1b"}
assert rows["LT-GR1"]["reason_kind"] == "ONE_BIT"
assert rows["LT-GR1"]["mapping_grade"] == "DETERMINED_GIVEN_U1"
assert rows["LT-GR1b"]["reason_kind"] == "GENUINE_FALSIFICATION"
assert rows["LT-GR1b"]["construction_scope"].endswith("FACTORIZATION_ONLY")
assert "candidate" in rows["LT-GR1b"]["distance"]
assert gate["exact_results"]["selected_shiab_kernel_observed_rank"] == 10
assert gate["route_disposition"]["selected_post_shiab_factorization"] == "KILLED_EXACT"
assert gate["route_disposition"]["source_action_ownership"] == "OPEN"
assert "not booked as a new target" in view
assert "This is a row-local route kill" in report
assert "HOSTILE POST-REVIEW: PASS" in review
assert "P1/P2/P3" in review
print("PASS: ledger v0.2 preserves predecessor history, one scoped migration, route scope, and no-promotion fences")
