#!/usr/bin/env python3
"""Fail-closed scope audit for the selected-Shiab observed receiver wave."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        assert len(keys) == len(set(keys)), f"duplicate key in {path}"
        return dict(items)
    return json.loads((ROOT / path).read_text(), object_pairs_hook=pairs)


reg = strict("lab/process/full-domain-shiab-observed-einstein-receiver.json")
report = (ROOT / "explorations/full-domain-shiab-observed-einstein-receiver-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/full-domain-shiab-observed-receiver-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-full-domain-shiab-observed-receiver-review.md").read_text()

assert reg["exact_results"]["selected_shiab_kernel_observed_rank"] == 10
assert reg["exact_results"]["observed_target_dimension"] == 10
assert reg["exact_results"]["post_shiab_linear_adapter_exists"] is False
assert reg["exact_results"]["post_shiab_nonlinear_adapter_exists"] is False
assert reg["route_disposition"]["selected_post_shiab_factorization"] == "KILLED_EXACT"
assert reg["route_disposition"]["pre_shiab_gauss_receiver"] == "PARAMETER_FREE_LOCAL_FORMULA__FIXTURE_VARIATION_AND_EQUATION_DUAL"
assert reg["route_disposition"]["source_action_ownership"] == "OPEN"
assert reg["source_collision"]["faithful_equation_receiver"] == "SOURCE_SILENT"
assert "there is no deterministic" in report
assert "does not establish full moving" in report
assert "not a claim attributed to Weinstein or Curt" in source
assert "HOSTILE POST-REVIEW: PASS" in review
assert "observed GR" in review
assert reg["next_gate"] == "OBSERVED_GAUSS_RECEIVER_SOURCE_ACTION_OWNERSHIP_AND_MOVING_DEFECT_VARIATIONAL_CLOSURE"
assert {item["row_id"] for item in reg["ledger_row_changes"]} == {"LT-GR1b"}
assert {"LT-GR1", "P1", "P2", "P3"} <= set(reg["no_ledger_change"])
print("PASS: rank-ten no-factor theorem, local repair, source silence, and no-promotion fences retained")
