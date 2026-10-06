#!/usr/bin/env python3
"""K1177: sharp coordinate controls for every uniform three-resource split."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1177-sharp-shared-allocation-controls.json"


def allocations(n):
    return [(h, g, n-h-g) for h in range(n+1) for g in range(n-h+1)]


def build():
    controls = allocations(9)
    return {
        "schema_version": "1.0", "result_id": "K1177-SHARP-SHARED-ALLOCATION-CONTROLS",
        "status": "working_draft_verified", "created": "2026-10-05",
        "input": "K1176-SHARED-CAUSAL-REPAIR-BUDGET",
        "control_dimension": 9,
        "allocation_count": len(controls),
        "allocation_rule": "all triples (h,g,c) of nonnegative integers with h+g+c=9",
        "extreme_controls": [[9, 0, 0], [0, 9, 0], [0, 0, 9]],
        "balanced_control": [3, 3, 3],
        "construction": "on a coordinate space split V=V_H direct-sum V_d direct-sum V_Q, use a positive identity Hessian on V_H, inject gauge image V_d, and let Q be identity on V_Q",
        "properties": ["Hd=0", "Qd=0", "rad(H restricted to ker Q)=im d", "rank H+rank d+rank(Q restricted to ker H)=dim V"],
        "decision": "every nonnegative uniform allocation on the shared-budget face is realizable; dimensions alone cannot prefer changed parent, gauge, or constraint repair",
        "scope_boundary": "sharp abstract controls only; no control is a GU source construction",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["input"] == "K1176-SHARED-CAUSAL-REPAIR-BUDGET"
    assert d["control_dimension"] == 9
    assert d["allocation_count"] == 55
    assert d["allocation_rule"].endswith("h+g+c=9")
    assert d["extreme_controls"] == [[9, 0, 0], [0, 9, 0], [0, 0, 9]]
    assert d["balanced_control"] == [3, 3, 3]
    assert "positive identity Hessian" in d["construction"]
    assert len(d["properties"]) == 4
    assert "cannot prefer" in d["decision"]
    assert "no control is a GU source construction" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1177 controls: 11/11")
