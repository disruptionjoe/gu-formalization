#!/usr/bin/env python3
"""Fail-closed audit for the v0.95 fixed-varpi normal Frechet closure."""

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


registry = strict("lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.95.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-fixed-varpi-normal-frechet-closure-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-fixed-varpi-normal-frechet-closure-review.md").read_text(encoding="utf-8")

block = registry["local_fixed_varpi_block"]
assert block["delta_T"] == "MINUS_DELTA_B_LC"
assert block["delta_A"] == "ZERO"
assert block["delta_F_A"] == "ZERO"
assert block["expanded_live_curvature_constituents"] == 3
assert block["expanded_curvature_sum"] == "ZERO"
assert block["full_covariant_lc_first_jet_rank"] == 20
assert block["full_lorentz_connection_carrier_dimension"] == 24
assert set(block["causal_classes"]) == {"timelike", "spacelike", "null"}
for row in block["causal_classes"].values():
    assert row == {
        "levi_civita_rank": 9,
        "diffeomorphism_rank": 4,
        "transverse_rank": 6,
        "transverse_source_rank": 6,
    }
assert block["comoving_coefficient_transport"] == "ZERO_AT_UPSILON_STAR_ZERO"
assert block["moving_observation_term_at_Upsilon_star_zero"] == "ZERO"
assert block["complete_observation_rank_effect"] == "PRESERVES_TRANSVERSE_RANK_SIX"
assert registry["disposition"] == "LOCAL_FIXED_VARPI_DG_UPSILON_BLOCK_CLOSED__COMMON_FIELD_ADJOINT_GREEN_OPEN"
assert registry["free_object_delta"] == 0
assert registry["residue_delta"] == 0
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"

assert ledger["schema_version"] == "0.95"
assert ledger["predecessor"].endswith("v0.94.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 4, "conditions_opened": 0, "remaining_named_conditions": 1}
assert ledger["source_return"] == registry["source_return"]
v095 = [item for item in ledger["migrations"] if item.get("to_version") == "0.95"]
assert len(v095) == 5
assert {item["row_id"] for item in v095} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.95.json")
assert "LOCAL_FIXED_VARPI_DG_UPSILON" in contract["standing_ledger"]["signature_branch_directive"]
assert "FORMAL_ADJOINT" in contract["active_scientific_directives"][0]["next_run_method"]["target"]

for term in (
    "three separately nonzero derivatives",
    "rank `20`",
    "rank six on the timelike",
    "Symplectic geometry",
    "Complex/path-integral",
):
    assert term in report
for term in (
    "SURVIVES_WITH_SCOPE_NARROWING",
    "off-branch source definition",
    "rank `20`",
    "common-field formal adjoint",
    "Symplectic geometry",
):
    assert term in review
for forbidden in (
    "the full field equation is complete",
    "positive Hilbert space is constructed",
    "formal adjoint is constructed",
    "source derives the fixed-varpi closure",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_probe.py",
    "process_gates/selected_k77_fixed_varpi_normal_frechet_closure_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_independent.sage").exists()

for relative in (
    "LANES.yaml",
    "NEXT-STEPS.md",
    "RESEARCH-STATUS.md",
    "explorations/README.md",
    "lab/process/README.md",
    "lab/process/agent-context-pack.md",
    "lab/process/functional-channel-operating-contract-v1.0.md",
):
    assert "v0.95" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 fixed-varpi normal Frechet closure audit")
