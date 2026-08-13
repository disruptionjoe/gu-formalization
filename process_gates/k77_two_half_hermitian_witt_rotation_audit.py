#!/usr/bin/env python3
"""Fail-closed audit for the K77 two-half Hermitian/Witt gate."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "lab/process/selected-k77-two-half-hermitian-witt-rotation-gate.json"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.193.json"


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
    require(result["checks"] == 53 and result["failures"] == 0, "probe receipt drift")
    require(result["native_J_carrier_complex_dimension"] == 64, "native-J size drift")
    require(result["source_sized_complexification_dimension"] == 128, "source carrier size drift")
    require(result["full_Hq_signature"] == [64, 64], "full Hq inertia drift")
    require(result["weyl_plus_Hq_signature"] == [32, 32], "plus-half inertia drift")
    require(result["weyl_minus_Hq_signature"] == [32, 32], "minus-half inertia drift")
    require(result["split_equivariant_same_half_bilinear_dimensions"] == [0, 0], "equivariant obstruction drift")
    require(result["full_fixed_q_stabilizer_dimension"] == 78, "full stabilizer drift")
    require(result["split_fixed_q_stabilizer_dimension"] == 48, "split stabilizer drift")
    require(result["witt_rotation_exact"] is True, "Witt rotation drift")
    require(result["moving_q_naturality_exact"] is True, "moving-q naturality drift")
    require(result["q_selected"] is False, "q selection overclaim")
    require(result["physical_block_identification"] == "OPEN", "physics block overclaim")
    require(gate["mailbox_postflight"] != "PENDING", "mailbox postflight missing")
    require(ledger["schema_version"] == "0.193", "ledger version drift")
    require(ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}, "verdict movement")
    require(ledger["residue"]["continuous_real"] == 84, "residue movement")
    require(gate["accounting"]["P1_P2_P3_used"] is False, "datum-use drift")
    contract = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
    require("latest_two_half_hermitian_witt_evidence" in json.dumps(contract), "two-half evidence pointer drift")
    lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
    versions = [int(value) for value in re.findall(r"conditional-physics-ledger-v0\.(\d+)\.json", lanes)]
    require(versions and max(versions) >= 193, "live ledger pointer predates v0.193")
    print("K77 two-half Hermitian/Witt rotation audit: PASS")


if __name__ == "__main__":
    main()
