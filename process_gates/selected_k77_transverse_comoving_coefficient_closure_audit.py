#!/usr/bin/env python3
"""Fail-closed audit for the v0.94 transverse comoving coefficient closure."""

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


registry = strict("lab/process/selected-k77-transverse-comoving-coefficient-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.94.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-transverse-comoving-coefficient-closure-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-transverse-comoving-coefficient-closure-review.md").read_text(encoding="utf-8")

expected = {
    "projector": 6,
    "metric": 6,
    "coframe": 6,
    "fixed_hodge_degree_one": 6,
    "fixed_hodge_degree_two": 6,
    "single_constituent_target_transport": 6,
    "raw_residual_target_transport": 0,
    "principal_augmented_torsion": 6,
}
assert set(registry["causal_classes"]) == {"timelike", "spacelike", "null"}
assert all(row == expected for row in registry["causal_classes"].values())
assert registry["disposition"] == "COEFFICIENT_PACKET_CLOSED__SOURCE_FIELD_AND_OBSERVATION_DERIVATIVES_OPEN"
assert registry["free_object_delta"] == 0
assert registry["residue_delta"] == 0
assert all(value == "UNUSED" for value in registry["external_datum"].values())
assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
assert registry["third_lane"] == "NOT_PROMOTED"

assert ledger["schema_version"] == "0.94"
assert ledger["predecessor"].endswith("v0.93.json")
assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["continuous_real_range_by_action_parent"] == "84..86"
assert ledger["residue"]["quotients_ranked"] == 5
assert ledger["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 0, "remaining_named_conditions": 2}
assert ledger["source_return"] == registry["source_return"]
assert sum(1 for item in ledger["migrations"] if item.get("to_version") == "0.94") == 5
assert {item["row_id"] for item in ledger["migrations"] if item.get("to_version") == "0.94"} == {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}

assert contract["standing_ledger"]["ref"].endswith("v0.94.json")
assert "TRANSVERSE_COMOVING_COEFFICIENT_PACKET_CLOSED" in contract["standing_ledger"]["signature_branch_directive"]
assert "COMPONENT_NORMAL_DT_DF" in contract["active_scientific_directives"][0]["next_run_method"]["target"]

for term in (
    "all ten metric values",
    "principal augmented-torsion response remains rank six",
    "coefficient packet closed",
    "Symplectic geometry",
    "Complex/path-integral",
):
    assert term in report
for term in (
    "SURVIVES_WITH_SCOPE_NARROWING",
    "top-degree Hodge/density",
    "complete physical `D_g Upsilon`",
    "Symplectic geometry",
):
    assert term in review
for forbidden in (
    "physical D_g Upsilon is complete",
    "positive Hilbert space is constructed",
    "formal adjoint is constructed",
    "source derives the transverse closure",
):
    assert forbidden not in report

for relative in (
    "tests/channel-swings/selected_k77_transverse_comoving_coefficient_closure_probe.py",
    "process_gates/selected_k77_transverse_comoving_coefficient_closure_audit.py",
):
    ast.parse((ROOT / relative).read_text(encoding="utf-8"))
assert (ROOT / "tests/channel-swings/selected_k77_transverse_comoving_coefficient_closure_independent.sage").exists()

for relative in (
    "lab/process/RESEARCH-AGENDA.json",
    "NEXT-STEPS.md",
    "RESEARCH-STATUS.md",
    "explorations/README.md",
    "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md",
    "lab/methods/research-evidence-contract-v1.0.md",
):
    assert "v0.94" in (ROOT / relative).read_text(encoding="utf-8")

print("PASS selected K77 transverse comoving coefficient closure audit")
