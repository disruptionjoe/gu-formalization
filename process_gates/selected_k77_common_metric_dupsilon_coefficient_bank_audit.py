#!/usr/bin/env python3
"""Fail-closed audit for the v0.97 common metric coefficient-bank gate."""

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


registry = strict("lab/process/selected-k77-common-metric-dupsilon-coefficient-bank.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.97.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-common-metric-dupsilon-coefficient-bank-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-common-metric-dupsilon-coefficient-bank-review.md").read_text(encoding="utf-8")

bank = registry["metric_bank"]
assert bank["domain_dimension"] == 10
assert bank["principal_directions"] == 4
assert bank["principal_ranks"] == [9, 9, 9, 9]
assert bank["principal_supports"] == [12, 12, 12, 12]
assert bank["combined_covariant_first_jet_rank"] == 20
assert all(packet == {
    "metric_symbol_rank": 9,
    "transverse_metric_rank": 6,
    "metric_orbit_rank": 3,
    "torsion_graph_defect_rank": 0,
} for packet in registry["causal_classes"].values())
assert all(packet["source_orbit_rank"] == 4
           and packet["physical_metric_orbit_rank"] == 3
           and packet["diagnostic_metric_orbit_rank"] == 4
           and packet["physical_ward_defect_rank"] == 4
           and packet["physical_vs_diagnostic_discrepancy_rank"] == 4
           for packet in registry["ward_comparison"].values())
assert registry["disposition"]["metric_bank"] == "CLOSED_ON_COMMON_RESIDUAL_COORDINATES"
assert registry["disposition"]["prior_ward_metric_completion"] == "REJECTED_AS_PHYSICAL_DG_OWNER"
assert registry["disposition"]["full_g_varpi_epsilon_principal_ward"] == "OPEN_WITH_EXACT_RANK4_DEFECT"
assert registry["controls"]["main_exact"] == "54/54 PASS"
assert registry["controls"]["independent_sage"] == "19/19 PASS"
assert registry["constraint_fence"] == {
    "new_fields": 0, "new_coefficients": 0, "new_quotients": 0,
    "P1_P2_P3": "UNUSED",
}
assert registry["action_parent_fence"]["weyl_block_product"].startswith("TWO_U32_32")
assert registry["action_parent_fence"]["full_u6464"].startswith("COMPARATOR")

assert ledger["schema_version"] == "0.97"
assert ledger["predecessor"].endswith("v0.96.json")
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5,
}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {
    "headline_delta": "NONE", "conditions_closed": 3,
    "conditions_opened": 1, "remaining_named_conditions": 3,
}
assert ledger["source_return"] == registry["source_return"]
v097 = [item for item in ledger["migrations"] if item.get("to_version") == "0.97"]
assert len(v097) == 5
assert {item["row_id"] for item in v097} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.97.json")
directive = contract["standing_ledger"]["signature_branch_directive"]
assert "COMMON_DG_BANK_RANK9X4_COMBINED20_TRANSVERSE6" in directive
assert "PRIOR_WARD_METRIC_OWNER_REJECTED" in directive
assert "NEXT_BUILD_COMPLETE_PRIMITIVE_DEPSILON_AND_PHYSICAL_DIFFEO_TRANSPORT" in directive

for term in (
    "rank-twenty", "rank six", "rank-four Ward defect",
    "Symplectic geometry", "two `U(32,32)` Weyl halves",
    "full `U(64,64)` comparator",
):
    assert term in report
for term in (
    "METRIC_BANK_SURVIVES__PRIOR_WARD_ORBIT_PROMOTION_FALSIFIED",
    "identity-defined metric orbit", "Mandatory symplectic and analytic review",
    "construction fork, not a GU no-go",
):
    assert term in review
for forbidden in (
    "the full primitive D_epsilon Upsilon is complete",
    "the Einstein equation is recovered",
    "a global Green operator is constructed",
    "source derives the gamma-soldered diffeomorphism law",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_common_metric_dupsilon_coefficient_bank_probe.py",
    "process_gates/selected_k77_common_metric_dupsilon_coefficient_bank_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_common_metric_dupsilon_coefficient_bank_independent.sage").exists()

for relative in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md",
    "explorations/README.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
):
    assert "v0.97" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 common metric D-Upsilon coefficient-bank audit")
