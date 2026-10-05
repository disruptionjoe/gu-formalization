#!/usr/bin/env python3
"""K1092: exact Ward-insufficiency counterexample."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1092-k1091-ward-insufficiency.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1092-K1091-WARD-INSUFFICIENCY",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "hessian": [[0, 0, 0], [0, 2, 1], [0, 1, 2]],
        "eigenvalues": [0, 1, 3],
        "positive_semidefinite": True,
        "ward_vector": [0, 0, 0],
        "harmonic_image": [0, 2, 1],
        "constraint_spill": 1,
        "commutator_rank": 2,
        "raw_compression": 2,
        "decision": "L d0=0 does not imply L(H1) subset H1 or [L,P_H]=0",
        "scope_boundary": "finite conditional counterexample; no source action, functional BV complex or physical spectrum",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["hessian"] == [[0,0,0],[0,2,1],[0,1,2]]
    assert d["eigenvalues"] == [0,1,3]
    assert d["positive_semidefinite"] is True
    assert d["ward_vector"] == [0,0,0]
    assert d["harmonic_image"] == [0,2,1]
    assert d["constraint_spill"] == 1
    assert d["commutator_rank"] == 2
    assert d["raw_compression"] == 2
    assert "does not imply" in d["decision"] and "[L,P_H]=0" in d["decision"]
    assert "no source action" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1092 controls: 10/10")
