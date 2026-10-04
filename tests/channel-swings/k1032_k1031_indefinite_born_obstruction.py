#!/usr/bin/env python3
"""K1032: mixed-sign forms are not full-space Born pairings."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1032-k1031-indefinite-born-obstruction.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1032-K1031-INDEFINITE-BORN-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "theorem": "a nondegenerate Hermitian form of inertia (p,q) with p,q>0 cannot be a positive probability pairing on its full carrier",
        "inertia_is_congruence_invariant": True,
        "exact_control": {
            "J": [[1, 0], [0, -1]],
            "positive_vector": [1, 0],
            "positive_norm": 1,
            "negative_vector": [0, 1],
            "negative_norm": -1,
            "full_space_radical_dimension": 0,
        },
        "repair_boundary": [
            "select an invariant positive subspace",
            "or supply a positive semidefinite form whose exact radical is quotiented",
            "prove the action/generator and every physical effect preserve the selected structure",
        ],
        "source_scope": {
            "SC-META-53": "UNCERTAIN -- source says the unbounded-spectrum problem is not known and proposes maximal-compact shielding",
            "SC-ACT-01": "ASSERTS -- classical first-order action; does not by itself select a Born pairing",
        },
        "claim_ceiling": "necessary positivity obstruction; not a no-go for a separately selected positive invariant subquotient",
        "ownership": {"positive_sector_selected": False, "probability_rule_derived": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "inertia (p,q)" in d["theorem"] and "p,q>0" in d["theorem"]
    assert d["inertia_is_congruence_invariant"] is True
    c = d["exact_control"]
    assert c["J"] == [[1, 0], [0, -1]]
    assert c["positive_norm"] == 1 and c["negative_norm"] == -1
    assert c["full_space_radical_dimension"] == 0
    assert len(d["repair_boundary"]) == 3
    assert d["source_scope"]["SC-META-53"].startswith("UNCERTAIN")
    assert d["source_scope"]["SC-ACT-01"].startswith("ASSERTS")
    assert "not a no-go" in d["claim_ceiling"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1032 controls: 12/12")
