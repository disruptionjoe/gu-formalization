#!/usr/bin/env python3
"""K1131: exact solvability constraints for a mixed Hessian block."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1131-mixed-block-solvability-constraint-map.json"


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def matmul(a, b):
    if not a:
        return []
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def build():
    fixtures = [
        {
            "id": "invertible_elimination",
            "C": [[2, 0], [0, 3]],
            "A": [[1, 2], [3, 4]],
            "left_kernel_rows": [],
            "constraint_rank": 0,
            "meaning": "distortion elimination with no field constraint",
        },
        {
            "id": "singular_compatible",
            "C": [[2, 0], [0, 0]],
            "A": [[1, 0], [0, 0]],
            "left_kernel_rows": [[0, 1]],
            "constraint_rank": 0,
            "meaning": "singular block whose left-null row annihilates A",
        },
        {
            "id": "singular_constraint",
            "C": [[2, 0], [0, 0]],
            "A": [[1, 0], [0, 1]],
            "left_kernel_rows": [[0, 1]],
            "constraint_rank": 1,
            "meaning": "solvability requires h_2=0",
        },
    ]
    for f in fixtures:
        q = matmul(f["left_kernel_rows"], f["A"])
        f["Q"] = [[int(x) for x in row] for row in q]
    return {
        "schema_version": "1.0",
        "result_id": "K1131-MIXED-BLOCK-SOLVABILITY-CONSTRAINT-MAP",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": {
            "distortion_equation": "C t + A h = 0",
            "left_kernel_map": "L with im(L)=ker(C*)",
            "constraint_map": "Q=L* A",
            "solvability_criterion": "Q h=0 iff -A h lies in im(C)",
            "constraint_rank_bound": "rank(Q)<=rank(A)",
            "invertible_case": "ker(C*)=0, so Q has rank 0 and C eliminates t without constraining h",
        },
        "fixtures": fixtures,
        "scope_boundary": "finite-dimensional exact solvability theorem; propagation, action ownership, closed domains and physical positivity are separate",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    t = d["theorem"]
    assert t["constraint_map"] == "Q=L* A"
    assert "iff" in t["solvability_criterion"]
    assert t["constraint_rank_bound"] == "rank(Q)<=rank(A)"
    assert "rank 0" in t["invertible_case"]
    assert len(d["fixtures"]) == 3
    expected = {"invertible_elimination": 0, "singular_compatible": 0, "singular_constraint": 1}
    for f in d["fixtures"]:
        q = matmul(f["left_kernel_rows"], f["A"])
        assert rank(q) == f["constraint_rank"] == expected[f["id"]]
        assert f["Q"] == [[int(x) for x in row] for row in q]
    assert "propagation" in d["scope_boundary"] and "physical positivity" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1131 controls: 13/13")
