#!/usr/bin/env python3
"""Fail-closed audit for the v0.96 common-field adjoint/Green ownership gate."""

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


registry = strict("lab/process/selected-k77-common-field-formal-adjoint-green.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.96.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-common-field-formal-adjoint-green-review.md").read_text(encoding="utf-8")

bank = registry["actual_varpi_bank"]
assert bank["domain_dimension"] == 24
assert bank["principal_directions"] == 4
assert bank["principal_ranks"] == [13, 13, 13, 13]
assert bank["principal_supports"] == [32, 32, 32, 32]
assert bank["zero_order_rank"] == 24
assert registry["formal_identity"]["actual_direction_checks"] == 4
assert registry["formal_identity"]["green_nonzero_in_all_directions"] is True

ownership = registry["common_field_ownership"]
assert ownership["D_varpi_coefficient_bank"] == "OWNED_AND_EXACT"
assert ownership["D_g_common_residual_coordinate_bank"] == "NOT_EMITTED"
assert ownership["D_epsilon_full_primitive_field_bank"] == "OPEN"
assert ownership["field_space_riesz_map"].startswith("OPEN")
assert ownership["disposition"] == "COMMON_FIELD_ASSEMBLY_FAILS_CLOSED"
assert registry["controls"]["main_exact"] == "30/30 PASS"
assert registry["controls"]["independent_sage"] == "8/8 PASS"
assert registry["constraint_fence"]["new_fields"] == 0
assert registry["constraint_fence"]["new_coefficients"] == 0
assert registry["constraint_fence"]["new_quotients"] == 0
assert {registry["constraint_fence"][key] for key in ("P1", "P2", "P3")} == {"UNUSED"}
assert registry["action_parent_fence"]["weyl_block_product"].startswith("TWO_U32_32")
assert registry["action_parent_fence"]["full_u6464"].startswith("COMPARATOR")

assert ledger["schema_version"] == "0.96"
assert ledger["predecessor"].endswith("v0.95.json")
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 4,
    "conditions_opened": 2, "remaining_named_conditions": 3,
}
assert ledger["source_return"] == registry["source_return"]
v096 = [item for item in ledger["migrations"] if item.get("to_version") == "0.96"]
assert len(v096) == 5
assert {item["row_id"] for item in v096} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.96.json")
directive = contract["standing_ledger"]["signature_branch_directive"]
assert "DVARPI_EQUATION_DUAL_GREEN_EXACT" in directive
assert "NEXT_EMIT_DG_COMMON_BANK_AND_BUILD_FULL_PRIMITIVE_DEPSILON" in directive
assert "FIELD_RIESZ_REQUIRED_ONLY_FOR_OPERATOR_REPRESENTATIVE" in directive

for term in (
    "rank `13`", "rank `24`", "field **covector**", "Symplectic geometry",
    "`U(32,32)` Weyl halves", "full `U(64,64)` comparator",
):
    assert term in report
for term in (
    "PARTIAL_SURVIVES__FULL_COMMON_FIELD_CLAIM_FALSIFIED",
    "primitive epsilon Euler equation", "field-space Riesz map",
    "Mandatory symplectic and analytic review",
):
    assert term in review
for forbidden in (
    "full common-field operator is complete",
    "positive Hilbert space is constructed",
    "global Green operator is constructed",
    "source derives K_loc",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_common_field_formal_adjoint_green_probe.py",
    "process_gates/selected_k77_common_field_formal_adjoint_green_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_common_field_formal_adjoint_green_independent.sage").exists()

for relative in (
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
    "explorations/README.md", "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md",
    "lab/methods/research-evidence-contract-v1.0.md",
):
    assert "v0.96" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 common-field formal-adjoint Green audit")
