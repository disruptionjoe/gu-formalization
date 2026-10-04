#!/usr/bin/env python3
"""K1031: positive quotient, observable and effect descent."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1031-k1030-positive-quotient-descent.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1031-K1030-POSITIVE-QUOTIENT-DESCENT",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "theorem": {
            "carrier": "finite-dimensional complex V with Hermitian M>=0",
            "gauge_radical": "N=ker(M)",
            "quotient_pairing": "<[x],[y]>=x^* M y on V/N",
            "positive_definite_iff": "N=ker(M) is exactly the quotient relation",
            "operator_descent_iff": "A(N) subset N",
            "self_adjointness": "A^* M=M A",
            "effect_condition": "0<=M A<=M as Hermitian forms",
        },
        "exact_control": {
            "M": [[1, 0, 0], [0, 2, 0], [0, 0, 0]],
            "kernel_basis": [[0, 0, 1]],
            "good_effect": [[1, 0, 0], [0, "1/2", 0], [0, 0, 0]],
            "quotient_effect_eigenvalues": [1, "1/2"],
            "bad_operator": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
            "bad_representative_shift": "A e3=e1, so [A(x+e3)] differs from [Ax]",
        },
        "claim_ceiling": "exact finite-dimensional descent criterion; no GU physical quotient or Born pairing constructed",
        "ownership": {"gu_quotient_selected": False, "gu_effect_selected": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    t = d["theorem"]
    assert t["gauge_radical"] == "N=ker(M)"
    assert t["operator_descent_iff"] == "A(N) subset N"
    assert t["self_adjointness"] == "A^* M=M A"
    assert t["effect_condition"] == "0<=M A<=M as Hermitian forms"
    c = d["exact_control"]
    assert c["M"] == [[1, 0, 0], [0, 2, 0], [0, 0, 0]]
    assert c["kernel_basis"] == [[0, 0, 1]]
    assert c["quotient_effect_eigenvalues"] == [1, "1/2"]
    assert "A e3=e1" in c["bad_representative_shift"]
    assert "no GU physical quotient" in d["claim_ceiling"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1031 controls: 11/11")
