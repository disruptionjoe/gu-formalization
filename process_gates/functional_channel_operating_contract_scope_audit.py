#!/usr/bin/env python3
"""Fail-closed wiring and scope audit for the GU functional-channel reset."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs)


contract_path = ROOT / "lab/process/functional-channel-operating-contract-v1.0.json"
contract = strict(contract_path)
human = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.md").read_text(encoding="utf-8")
agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
lanes = (ROOT / "LANES.yaml").read_text(encoding="utf-8")
operating = (ROOT / "lab/process/OPERATING-MODEL.md").read_text(encoding="utf-8")
context_pack = (ROOT / "lab/process/agent-context-pack.md").read_text(encoding="utf-8")
synthesis = (ROOT / "explorations/precontract-waves-0abc-synthesis-2026-08-05.md").read_text(encoding="utf-8")

assert contract["status"] == "RATIFIED"
assert contract["purpose_lanes_preserved"] == ["1", "2", "3", "A"]
assert contract["functional_channels_are_not_lanes"] is True
assert set(contract["channels"]) == {"BUILD", "COMPOSE", "SOURCE", "VERIFY"}
assert contract["dispatch"]["fixed_percentages"] is False
assert contract["durability_level"] == "OWNER_LOCAL_MANDATORY_CONTEXT_PLUS_MACHINE_TESTED_CONTRACT"
assert contract["fleet_runner_interpretation_change"] == "NOT_CHANGED_IN_THIS_RUN"
assert contract["standing_ledger"]["owner"] == "COMPOSE_CHANNEL_WITH_LANE_A_RECONCILIATION"
assert contract["channels"]["COMPOSE"]["cadence"]["after_material_build_outputs"] == 3
assert contract["channels"]["SOURCE"]["return_codes"] == [
    "SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"
]
assert contract["over_determined"]["finder_may_adjudicate"] is False
assert contract["over_determined"]["independent_owner_required"] is True
assert contract["channels"]["VERIFY"]["unchanged_replay_is_progress"] is False
assert contract["channels"]["VERIFY"]["hostile_charges"] == [
    "SUMMARY_OUTRUNS_ARTIFACT", "DEFENDS_SUPERSEDED_OR_MISTYPED_OBJECT"
]

for ref in [
    "lab/process/functional-channel-operating-contract-v1.0.md",
    "lab/process/functional-channel-operating-contract-v1.0.json",
]:
    assert ref in lanes
assert 'manifest_revision: 4' in lanes
assert 'contract_version: "2.0"' in lanes
assert 'id: functional-channel-contract-v1' in lanes
assert "functional-channel-operating-contract-v1.0.md" in agents
assert "GU-COSMO-DYNAMIC-01" in agents
assert "functional-channel-operating-contract-v1.0.md" in operating
assert "functional-channel-operating-contract-v1.0.md" in context_pack
assert "GU-COSMO-DYNAMIC-01" in context_pack
assert "conditional-physics-ledger-v0.4.json" in lanes
assert contract["standing_ledger"]["ref"].endswith("conditional-physics-ledger-v0.4.json")

assert "The finder of an over-determined row escalates it and may not adjudicate it" in human
assert "found over-determined row is valuable" in human
assert "forced fitting is forbidden" in human
assert "There are no fixed channel percentages" in human
assert "unchanged packet" in human
assert "summary outruns the artifact" in human
assert "superseded or mistyped" in human
assert "ledger_row_changes: none" in human
assert "Thin automation triggers" in human

directive = contract["active_scientific_directives"][0]
assert directive["id"] == "GU-COSMO-DYNAMIC-01"
assert directive["owner"] == "SOURCE_PLUS_COMPOSE__INDEPENDENT_FROM_NEXT_BUILD_FINDER"
assert directive["primary_row_on_hold"] is None
assert directive["status"] == "AMBIENT_ACTION_RANK_EXACT__OBSERVED_PRE_SHIAB_RECEIVER_AND_NATIVE_BV_OPEN"
assert directive["source_return"] == "SOURCE-CONFIRMS"
assert directive["release_condition_met"] is True
assert directive["successor_rows"] == ["LT-GR2a", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR2e"]
assert len(set(directive["required_layer0_objects"])) == 7
assert "LITERAL_CONSTANT_LAMBDA_G" in directive["required_layer0_objects"]
assert "VARIABLE_OLIVE_VARPI_AUGMENTED_TORSION_VEV" in directive["required_layer0_objects"]
assert directive["forbidden_collapse"] == "EINSTEIN_RECOVERY_DOES_NOT_IMPLY_DYNAMIC_COSMOLOGICAL_SECTOR_RECOVERY"
assert "PRE_SHIAB_GAUSS_CURVATURE_TO_T" in directive["next_gate"]
assert "would be circular" in human
assert "the Einstein equation was recovered” is not a completion result" in human
assert "historical Einstein" in human

assert "Subsequent ratification" in synthesis
assert "not ratified **in this\nRun**" in synthesis
assert set(contract["non_effects"]) >= {
    "NO_SCHEDULER_CHANGE", "NO_TRIGGER_CHANGE", "NO_ACTIVATION_GRANT_CHANGE",
    "NO_LANE_COUNT_CHANGE", "NO_CANON_CHANGE", "NO_VERDICT_CHANGE",
    "NO_P1_P2_P3_CHANGE", "NO_PUBLIC_POSTURE_CHANGE"
}

print("PASS: functional channels, v0.4 ledger, adverse-row independence, source return, circularity fence and the next dynamic-cosmology receiver/BV gate are wired without lane or system promotion")
