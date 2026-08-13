#!/usr/bin/env python3
"""Fail-closed audit for the v0.100 action Noether/preboundary gate."""

from pathlib import Path
import ast
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


registry = strict("lab/process/selected-k77-action-noether-preboundary.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.100.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-action-noether-preboundary-review.md").read_text(encoding="utf-8")

assert registry["status"] == "LOCAL_SELECTED_ACTION_NOETHER_EXACT__COMPACT_SUPPORT_PRESYMPLECTIC_BASIC__UNRESTRICTED_BOUNDARY_MOMENT_MAP_LIVE"
assert registry["moving_quadratic_layer"]["background_residual"] == "NONZERO"
assert registry["moving_quadratic_layer"]["all_three_terms_live"] is True
assert registry["moving_quadratic_layer"]["total_variation"] == "ZERO_EXACT"
assert registry["moving_quadratic_layer"]["freeze_pairing"] == "REJECTED"
assert registry["moving_quadratic_layer"]["freeze_density"] == "REJECTED"
assert registry["matched_q_action_noether"] == {
    "timelike": "ZERO_EXACT", "spacelike": "ZERO_EXACT", "null": "ZERO_EXACT",
}
assert registry["action_boundary_owner"]["coefficient"] == "selected-action E_B-E_T"
assert registry["action_boundary_owner"]["normal_rank"] == 10
assert registry["action_boundary_owner"]["generic_p_equals_KT"].startswith("REJECTED")
assert registry["presymplectic"]["compact_support_basic"] is True
assert registry["presymplectic"]["unrestricted_boundary_charge"] == "LIVE"
assert registry["presymplectic"]["all_boundary_transformations_quotientable"] is False
assert registry["presymplectic"]["new_scoped_quotient_booked"] is False
assert registry["controls"]["main_exact"] == "56/56 PASS"
assert registry["controls"]["independent_sage"] == "18/18 PASS"
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["action_parent_fence"]["weyl_block_product"].startswith("TWO_U32_32")
assert registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED"

assert ledger["schema_version"] == "0.100"
assert ledger["predecessor"].endswith("v0.99.json")
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 2,
    "conditions_opened": 0, "remaining_named_conditions": 1,
}
assert ledger["source_return"] == registry["source_return"]
v100 = [item for item in ledger["migrations"] if item.get("to_version") == "0.100"]
assert len(v100) == 5
assert {item["row_id"] for item in v100} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.100.json")
directive = contract["standing_ledger"]["signature_branch_directive"]
assert "LOCAL_SELECTED_ACTION_NOETHER_EXACT_NONZERO_RESIDUAL_CONTROL" in directive
assert "COMPACT_SUPPORT_PRESYMPLECTIC_BASIC" in directive
assert "UNRESTRICTED_BOUNDARY_MOMENT_MAP_LIVE" in directive

for term in (
    "nonzero residual", "primitive epsilon", "E_B-E_T",
    "Symplectic geometry", "boundary moment map",
    "product of two", "`U(32,32)` Weyl-half groups", "`U(64,64)` comparator",
):
    assert term in report
for term in (
    "LOCAL_ACTION_COMPOSITION_SURVIVES", "where the summary outruns",
    "Symplectic geometry", "Analytic/path-integral", "needs-recheck",
):
    assert term in review
for forbidden in (
    "a global BFV phase space is constructed",
    "all boundary transformations are gauge",
    "the K77 pairing is positive definite",
    "the Einstein equation is recovered",
    "the two U(32,32) halves are the full U(64,64)",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_action_noether_preboundary_probe.py",
    "process_gates/selected_k77_action_noether_preboundary_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_action_noether_preboundary_independent.sage").exists()

for relative in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
    "explorations/README.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
):
    assert "v0.100" in (ROOT / relative).read_text(encoding="utf-8")

tests_manifest = (ROOT / "tests/README.md").read_text(encoding="utf-8")
assert "473 Python + 62 Sage" in tests_manifest

print("PASS selected K77 action Noether/preboundary audit")
