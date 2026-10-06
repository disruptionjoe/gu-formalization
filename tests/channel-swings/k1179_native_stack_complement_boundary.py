#!/usr/bin/env python3
"""K1179: named native maps add only sequential complement rank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1179-native-stack-complement-boundary.json"
CEILINGS = [650, 915, 1470, 1571]


def build():
    total = sum(CEILINGS)
    return {
        "schema_version": "1.0", "result_id": "K1179-NATIVE-STACK-COMPLEMENT-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-05",
        "inputs": ["K1166-STACKED-CONSTRAINT-RANK-SPLIT", "K1178-NATIVE-RESPONSE-CEILING-LEDGER"],
        "theorem": "for maps Q1,...,Qm on K=ker H, rank(Q1,...,Qm)|K=sum_j rank(Qj restricted to K intersect previous kernels)",
        "candidate_ceilings": CEILINGS,
        "optimistic_direct_sum_ceiling": total,
        "optimistic_residual_deficits": {"timelike": 98372-total, "spacelike": 98372-total, "null": 106536-total},
        "actual_admission_fields": ["typed common K132 carrier", "source-owned coupling", "causal-stratum symbol", "sequential complement ranks", "Qd=0", "functional K1150 packet"],
        "current_actual_stack_rank": "unmeasured",
        "decision": "even granting all four native ceilings independent direct-sum transport gives only 4606 directions and leaves 93766/93766/101930; any overlap or failed transport increases the deficit",
        "zero_credit_rule": "a candidate that factors through the preceding stack has sequential complement rank zero regardless of its name, target size, derivative order or parameter count",
        "scope_boundary": "strongest-favorable ceiling only; the four objects are not asserted to share one carrier or define one K132 constraint stack",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert len(d["inputs"]) == 2
    assert "sum_j rank" in d["theorem"]
    assert d["candidate_ceilings"] == CEILINGS
    assert d["optimistic_direct_sum_ceiling"] == 4606
    assert d["optimistic_residual_deficits"] == {"timelike": 93766, "spacelike": 93766, "null": 101930}
    assert len(d["actual_admission_fields"]) == 6
    assert d["current_actual_stack_rank"] == "unmeasured"
    assert "93766/93766/101930" in d["decision"]
    assert "complement rank zero" in d["zero_credit_rule"]
    assert "not asserted to share one carrier" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-06"
    assert sum(d["candidate_ceilings"]) == d["optimistic_direct_sum_ceiling"]


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1179 controls: 12/12")
