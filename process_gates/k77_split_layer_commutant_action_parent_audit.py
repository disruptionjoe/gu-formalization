#!/usr/bin/env python3
"""Fail-closed audit for the K77 split-layer commutant/action-parent gate."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "lab/process/selected-k77-split-layer-commutant-action-parent-gate.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.191.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def load_unique(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            require(key not in out, f"duplicate key {key!r} in {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


def main():
    gate = load_unique(REG)
    ledger = load_unique(LEDGER)
    result = gate["result"]
    require(gate["target_claim"] == "NONE-NOT-A-KILL", "kill target drift")
    require(result["checks"] == 20 and result["failures"] == 0, "probe receipt drift")
    require(result["real_commutant_dimension"] == 4, "split commutant drift")
    require(result["commutant_algebra"] == "C_PLUS_C", "commutant algebra drift")
    require(result["real_weyl_half_dimensions"] == [64, 64], "half dimensions drift")
    require(result["complexification_eigenspace_dimensions_per_half"] == [32, 32], "complexification drift")
    require(result["invariant_real_bilinear_blocks_pp_mm_pm_mp"] == [0, 0, 2, 2], "bilinear typing drift")
    require(result["action_parent_selection"] == "OPEN", "selection overclaim")
    require(gate["mailbox_postflight"].startswith("NO_NEW_GU_FORMALIZATION"), "mailbox postflight missing")
    require(ledger["schema_version"] == "0.191", "ledger version drift")
    require(ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}, "verdict movement")
    require(ledger["residue"]["continuous_real"] == 84, "residue movement")
    contract = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
    # This is a durability audit for the v0.191 result, not a freeze on its
    # once-current successor.  Later gates must be able to advance the priority
    # while retaining the exact split-layer evidence.
    require("latest_split_layer_commutant_action_parent_evidence" in json.dumps(contract), "split-layer evidence pointer drift")
    lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
    require("lab/process/conditional-physics-ledger-v" in lanes, "live ledger pointer missing")
    require(gate["accounting"]["P1_P2_P3_used"] is False, "datum use drift")
    print("K77 split-layer commutant/action-parent audit: PASS")


if __name__ == "__main__":
    main()
