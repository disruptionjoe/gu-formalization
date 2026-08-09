#!/usr/bin/env python3
"""Fail-closed audit for the v0.98 source-native physical Ward gate."""

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


registry = strict("lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.98.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-source-native-diffeomorphism-ward-closure-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-source-native-diffeomorphism-ward-closure-review.md").read_text(encoding="utf-8")

assert registry["result"].endswith("TIMELIKE_SPACELIKE_NULL__NO_GAMMA")
assert registry["disposition"]["matched_q_physical_ward"] == "CLOSED_EXACTLY_WITH_ZERO_FIT"
assert registry["disposition"]["grade_one_gamma_for_physical_diffeomorphism"] == "NOT_REQUIRED"
assert registry["disposition"]["arbitrary_primitive_D_epsilon"].startswith("OPEN")
for name, packet in registry["causal_classes"].items():
    assert packet["physical_jacobian_rank"] == 4
    assert packet["spin_connection_rank"] == 3
    assert packet["moving_shiab_rank"] == 3
    assert packet["varpi_cartan_response_rank"] == 3
    assert packet["complete_ward_defect_rank"] == 0
    assert packet["without_moving_defect_rank"] == 3
    assert packet["without_lower_cartan_defect_rank"] == 3
    assert packet["complete_ward_supports"] == [0, 0, 0, 0]
    assert packet["frozen_q0_defect_rank"] == (0 if name == "timelike" else 3)
assert registry["controls"]["main_exact"] == "52/52 PASS"
assert registry["controls"]["independent_sage"] == "19/19 PASS"
assert registry["constraint_fence"] == {
    "new_fields": 0, "new_coefficients": 0, "new_quotients": 0,
    "P1_P2_P3": "UNUSED",
}
assert registry["action_parent_fence"]["two_U32_32_halves"].startswith("PRESERVED")
assert registry["action_parent_fence"]["full_U64_64"] == "COMPARATOR_NOT_COLLAPSED"

assert ledger["schema_version"] == "0.98"
assert ledger["predecessor"].endswith("v0.97.json")
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 0, "remaining_named_conditions": 3,
}
assert ledger["source_return"] == registry["source_return"]
v098 = [item for item in ledger["migrations"] if item.get("to_version") == "0.98"]
assert len(v098) == 5
assert {item["row_id"] for item in v098} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.98.json")
directive = contract["standing_ledger"]["signature_branch_directive"]
assert "MATCHED_Q_METRIC_CARTAN_MOVING_SHIAB_PHYSICAL_WARD_ZERO" in directive
assert "GRADE1_GAMMA_NOT_REQUIRED" in directive
assert "NEXT_BUILD_COMMON_KLOC_GREEN_THEN_ACTION_EULER_NOETHER_PRESYMPLECTIC" in directive

for term in (
    "complete Ward column has empty", "physical Jacobian", "rank `3`",
    "`U(32,32)` Weyl halves", "full `U(64,64)` comparator",
    "SOURCE-CONFIRMS_MOVING_PHI",
):
    assert term in report
for term in (
    "PHYSICAL_WARD_CLOSURE_SURVIVES", "Frozen `q0`", "Symplectic geometry",
    "Analytic/path-integral", "arbitrary field bank `D_epsilon Upsilon[eta]`",
):
    assert term in review
for forbidden in (
    "the full arbitrary primitive D_epsilon is complete",
    "the Einstein equation is recovered",
    "a global Green operator is constructed",
    "the source derives the physical Cartan composition",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_source_native_diffeomorphism_ward_closure_probe.py",
    "process_gates/selected_k77_source_native_diffeomorphism_ward_closure_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_source_native_diffeomorphism_ward_closure_independent.sage").exists()

for relative in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
    "explorations/README.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
):
    assert "v0.98" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 source-native physical-diffeomorphism Ward audit")
