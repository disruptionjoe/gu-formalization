#!/usr/bin/env python3
"""Fail-closed audit for the v0.99 common physical dual/Green gate."""

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


registry = strict("lab/process/selected-k77-common-physical-equation-dual-green.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.99.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-common-physical-equation-dual-green-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-common-physical-equation-dual-green-review.md").read_text(encoding="utf-8")

assert registry["status"] == "COMMON_METRIC_VARPI_EQUATION_DUAL_GREEN_EXACT__PHYSICAL_PULLBACK_ZERO__ACTION_NOETHER_OPEN"
assert registry["common_operator"]["domain_dimension"] == 34
assert registry["common_operator"]["metric_domain_dimension"] == 10
assert registry["common_operator"]["varpi_domain_dimension"] == 24
assert registry["common_operator"]["metric_principal_ranks"] == [9, 9, 9, 9]
assert registry["common_operator"]["varpi_principal_ranks"] == [13, 13, 13, 13]
assert registry["common_operator"]["varpi_zero_order_rank"] == 24
assert registry["common_operator"]["green_nonzero"] is True
assert registry["common_operator"]["combined_rank_disposition"].startswith("NOT_RECOMPUTED")
for packet in registry["physical_pullback"].values():
    assert packet == {
        "ward_defect_rank": 0,
        "equation_dual_pullback": "ZERO_FOUR_COLUMNS",
        "constituents_nontrivial": True,
    }
assert registry["controls"]["main_exact"] == "44/44 PASS"
assert registry["controls"]["independent_sage"] == "12/12 PASS"
assert registry["constraint_fence"]["P1_P2_P3"] == "UNUSED"
assert registry["constraint_fence"]["new_fields"] == 0
assert registry["action_parent_fence"]["weyl_block_product"].startswith("TWO_U32_32")
assert registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED"

assert ledger["schema_version"] == "0.99"
assert ledger["predecessor"].endswith("v0.98.json")
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 0, "remaining_named_conditions": 2,
}
assert ledger["source_return"] == registry["source_return"]
v099 = [item for item in ledger["migrations"] if item.get("to_version") == "0.99"]
assert len(v099) == 5
assert {item["row_id"] for item in v099} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.99.json")
directive = contract["standing_ledger"]["signature_branch_directive"]
assert "COMMON_34_FIELD_KLOC_EQUATION_DUAL_GREEN_EXACT" in directive
assert "PHYSICAL_DUAL_PULLBACK_ZERO" in directive
assert "NEXT_BUILD_MOVING_ACTION_PAIRING_DENSITY_EPSILON_EULER_PREBOUNDARY_NOETHER" in directive

for term in (
    "10 metric variables + 24 horizontal varpi variables = 34 variables",
    "equation dual", "Green concomitant", "Symplectic geometry",
    "two `U(32,32)` Weyl halves", "`U(64,64)` comparator",
):
    assert term in report
for term in (
    "COMMON_EQUATION_DUAL_GREEN_SURVIVES", "old queue",
    "Symplectic geometry", "Analytic/path-integral",
    "field-space Riesz map",
):
    assert term in review
for forbidden in (
    "the complete selected-action Noether theorem is proved",
    "a global Green operator is constructed",
    "the full arbitrary primitive D_epsilon is complete",
    "the Einstein equation is recovered",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_common_physical_equation_dual_green_probe.py",
    "process_gates/selected_k77_common_physical_equation_dual_green_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_common_physical_equation_dual_green_independent.sage").exists()

for relative in (
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
    "explorations/README.md", "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md",
    "lab/methods/research-evidence-contract-v1.0.md",
):
    assert "v0.99" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 common physical equation-dual/Green audit")
