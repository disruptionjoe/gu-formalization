#!/usr/bin/env python3
"""K1167: sharp independent, partial-overlap, and duplicate channel controls."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1167-independent-overlap-channel-controls.json"


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a: return 0
    rows, cols, r = len(a), len(a[0]), 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if a[i][c]), None)
        if p is None: continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]; a[r] = [x / z for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                z = a[i][c]; a[i] = [x - z*y for x,y in zip(a[i],a[r])]
        r += 1
    return r


def channel(rows):
    q = [[1,0,0,0,0,0],[0,1,0,0,0,0]]
    rq, rl, rs = rank(q), rank(rows), rank(q + rows)
    return {"q_rank": rq, "ell_rank": rl, "stacked_rank": rs, "overlap_defect": rq + rl - rs}


def build():
    return {
        "schema_version": "1.0", "result_id": "K1167-INDEPENDENT-OVERLAP-CHANNEL-CONTROLS",
        "status": "working_draft_verified", "created": "2026-10-05",
        "controls": {
            "independent": channel([[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]]),
            "one_overlap": channel([[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0]]),
            "duplicate": channel([[1,0,0,0,0,0],[0,1,0,0,0,0]]),
        },
        "sharpness": "delta=0,1,2 are realized exactly; the direct-sum dimension is attained only by the independent control",
        "interpretation": "two named targets do not earn additive rank by nomenclature; independence must be proved on the actual K132 kernel",
        "scope_boundary": "coordinate controls only; no claim that the moment map and seven-invariant lock realize any listed overlap pattern",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    a,b,c = d["controls"]["independent"], d["controls"]["one_overlap"], d["controls"]["duplicate"]
    assert a == {"q_rank":2,"ell_rank":3,"stacked_rank":5,"overlap_defect":0}
    assert b == {"q_rank":2,"ell_rank":3,"stacked_rank":4,"overlap_defect":1}
    assert c == {"q_rank":2,"ell_rank":2,"stacked_rank":2,"overlap_defect":2}
    assert "delta=0,1,2" in d["sharpness"]
    assert "independence must be proved" in d["interpretation"]
    assert "coordinate controls only" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data=build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1167 controls: 7/7")
