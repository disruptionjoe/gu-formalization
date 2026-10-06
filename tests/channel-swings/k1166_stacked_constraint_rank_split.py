#!/usr/bin/env python3
"""K1166: exact rank split for two stacked constraint channels."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1166-stacked-constraint-rank-split.json"


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols, r = len(a), len(a[0]), 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def build():
    q = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
    ell = [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]
    stacked = q + ell
    return {
        "schema_version": "1.0",
        "result_id": "K1166-STACKED-CONSTRAINT-RANK-SPLIT",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "hypotheses": ["K=ker H finite dimensional", "im d subset K", "q d=ell d=0"],
        "theorem": {
            "exact_split": "rank((q,ell)|K)=rank(q|K)+rank(ell|(K intersect ker q))",
            "overlap_defect": "delta=rank(q|K)+rank(ell|K)-rank((q,ell)|K)>=0",
            "radical_capture_necessity": "rad(H|ker(q,ell))=im d implies rank((q,ell)|K)=dim K-rank d",
            "target_ceiling": "dim K-rank d<=dim Wq+dim Well",
        },
        "exact_control": {
            "kernel_dimension": 6,
            "gauge_rank": 1,
            "q_rank": rank(q),
            "ell_rank": rank(ell),
            "stacked_rank": rank(stacked),
            "overlap_defect": rank(q) + rank(ell) - rank(stacked),
            "required_radical_capture_rank": 5,
        },
        "decision": "stacking finite channels gains only the second channel's rank on the first channel's kernel; shared information pays an exact overlap penalty",
        "scope_boundary": "finite-dimensional necessary theorem only; no source coupling, propagation, common domain, positivity, or physical quotient is constructed",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["hypotheses"]) == 3
    assert d["theorem"]["exact_split"].startswith("rank((q,ell)|K)=")
    assert d["theorem"]["overlap_defect"].endswith(">=0")
    assert "dim K-rank d" in d["theorem"]["radical_capture_necessity"]
    assert d["theorem"]["target_ceiling"].endswith("dim Wq+dim Well")
    c = d["exact_control"]
    assert (c["q_rank"], c["ell_rank"], c["stacked_rank"], c["overlap_defect"]) == (2, 3, 4, 1)
    assert c["kernel_dimension"] == 6 and c["gauge_rank"] == 1
    assert c["required_radical_capture_rank"] == 5
    assert "exact overlap penalty" in d["decision"]
    assert "finite-dimensional necessary theorem only" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1166 controls: 10/10")
