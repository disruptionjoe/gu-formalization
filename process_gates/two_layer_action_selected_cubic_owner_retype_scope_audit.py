#!/usr/bin/env python3
"""Fail-closed scope audit for the two-layer selected-cubic retype."""

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


registry = strict(ROOT / "lab/process/two-layer-action-selected-cubic-owner-retype.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.24.json")
report = (ROOT / "explorations/conditional-build/two-layer-action-selected-cubic-owner-retype-2026-08-06.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-06-two-layer-action-selected-cubic-owner-retype-review.md").read_text()

assert registry["status"] == "TWO_LAYER_QUEUE_SPLIT_CONFIRMED__LT_GR3_OWNER_MAP_OPEN"
assert registry["source"]["return_code"] == "SOURCE-CORRECTS"
assert registry["layer0"]["residual_norm_square_vs_observer_full_ii"] == "NOT_ESTABLISHED"
assert registry["exact_probe"]["generic_common_scale"] is False
assert registry["exact_probe"]["generic_d3_i2_over_d3_i1_ratios"] == ["3", "4", "5", "6"]
assert registry["queue"]["reconciliation_before_q1"] is True
assert registry["constraint_cost"] == {"fitted_coefficients": 0, "new_external_datum": 0, "residue_reduction": 0, "new_quotients": 0}
assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
assert ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 4
assert "three owners are distinct" in report
assert "symplectic" in review
assert "summary outruns" in review
assert "superseded or mistyped object" in review
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"
assert registry["claim_status_change"] == "NONE"
assert registry["canon_verdict_change"] == "NONE"
assert registry["public_posture_change"] == "NONE"

print("TWO_LAYER_ACTION_SELECTED_CUBIC_OWNER_RETYPE_SCOPE_AUDIT_PASS")
