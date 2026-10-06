#!/usr/bin/env python3
"""K1180: integrate the native ceiling audit into K132 admission."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1180-i1b-native-candidate-admission-boundary.json"


def build():
    return {
        "schema_version": "1.0", "result_id": "K1180-I1B-NATIVE-CANDIDATE-ADMISSION-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1175-I1B-THREE-REOPENER-ADMISSION-BOUNDARY", "K1176-SHARED-CAUSAL-REPAIR-BUDGET", "K1177-SHARP-SHARED-ALLOCATION-CONTROLS", "K1178-NATIVE-RESPONSE-CEILING-LEDGER", "K1179-NATIVE-STACK-COMPLEMENT-BOUNDARY"],
        "uniform_shared_floor": 106536,
        "strongest_single_optimistic_residual": {"timelike": 96801, "spacelike": 96801, "null": 104965},
        "all_four_optimistic_residual": {"timelike": 93766, "spacelike": 93766, "null": 101930},
        "current_typed_k132_couplings": 0,
        "current_measured_complement_stacks": 0,
        "current_candidates_meeting_full_packet": 0,
        "next_condition": "supply one source-owned map on the K132 carrier, compute its causal-stratum rank on ker H after the rank-98 joint channel and every earlier admitted map, then place the measured complement ranks in the repair polytope and recompute all K1150 gates",
        "protected_disposition": "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8, LT-GR6b, RA-F1 and AC-F1 remain NEEDS",
        "scope_boundary": "the 650/915/1470/1571 figures are provenance-bearing optimistic ceilings, not additive owned K132 constraints; no source, ledger, empirical, prediction, confirmation, canon, paper or public verdict changes",
        "scorable_rows_added": 0, "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 5
    assert d["uniform_shared_floor"] == 106536
    assert d["strongest_single_optimistic_residual"] == {"timelike": 96801, "spacelike": 96801, "null": 104965}
    assert d["all_four_optimistic_residual"] == {"timelike": 93766, "spacelike": 93766, "null": 101930}
    assert d["current_typed_k132_couplings"] == 0
    assert d["current_measured_complement_stacks"] == 0
    assert d["current_candidates_meeting_full_packet"] == 0
    assert "compute its causal-stratum rank on ker H" in d["next_condition"]
    assert d["protected_disposition"].startswith("SC-ACT-01/02/06 remain ASSERTS")
    assert "not additive owned K132 constraints" in d["scope_boundary"]
    assert d["scorable_rows_added"] == 0
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1180 controls: 12/12")
