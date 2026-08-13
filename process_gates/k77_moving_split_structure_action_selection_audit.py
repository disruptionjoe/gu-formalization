#!/usr/bin/env python3
"""Fail-closed audit for the moving split structure/action-selection gate."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "lab/process/selected-k77-moving-split-structure-action-selection-gate.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.192.json"


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
    require(result["checks"] == 40 and result["failures"] == 0, "probe receipt drift")
    require(result["compatible_connection_Domega_zero"] is True, "compatible omega drift")
    require(result["compatible_connection_DJ_zero"] is True, "compatible J drift")
    require(result["block_connection_Domega_zero"] is True, "block omega drift")
    require(result["block_connection_DJ_zero"] is False, "block/fine collapse")
    require(result["full_endomorphism_Domega_zero"] is False, "full/block collapse")
    require(result["Komega_recovered_from_Domega"] is True, "Komega reconstruction drift")
    require(result["KJ_recovered_from_omega_even_DJ"] is True, "KJ reconstruction drift")
    require(result["current_pointwise_action_reduction_selected"] is False, "selection overclaim")
    require(result["physical_block_identification"] == "OPEN", "physics identification overclaim")
    require(gate["mailbox_postflight"].startswith("NO_NEW_GU_FORMALIZATION"), "mailbox postflight missing")
    require(ledger["schema_version"] == "0.192", "ledger version drift")
    require(ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}, "verdict movement")
    require(ledger["residue"]["continuous_real"] == 84, "residue movement")
    require(gate["accounting"]["P1_P2_P3_used"] is False, "datum use drift")
    contract = load_unique(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
    require("latest_moving_split_structure_action_selection_evidence" in json.dumps(contract), "moving-split evidence pointer drift")
    lanes = (ROOT / "LANES.yaml").read_text()
    versions = [int(value) for value in re.findall(r"conditional-physics-ledger-v0\.(\d+)\.json", lanes)]
    require(versions and max(versions) >= 192, "live ledger pointer predates v0.192")
    print("K77 moving split structure/action-selection audit: PASS")


if __name__ == "__main__":
    main()
