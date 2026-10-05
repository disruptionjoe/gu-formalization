#!/usr/bin/env python3
"""K1106: symmetric Loewner factorization for positive Stieltjes branches."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1106-k1105-symmetric-loewner-factorization.json"


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = Fraction(1)
    for i in range(len(a)):
        pivot = next(j for j in range(i, len(a)) if a[j][i])
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            out = -out
        q = a[i][i]
        out *= q
        for j in range(i + 1, len(a)):
            ratio = a[j][i] / q
            for k in range(i, len(a)):
                a[j][k] -= ratio * a[i][k]
    return out


def kernel(x, y, alpha, shifts, weights):
    return alpha + sum(
        w / ((x + d) * (y + d)) for d, w in zip(shifts, weights)
    )


def build():
    nodes = [Fraction(0), Fraction(1), Fraction(2)]
    alpha = Fraction(2)
    shifts = [Fraction(1), Fraction(3)]
    weights = [Fraction(1), Fraction(4)]
    matrix = [[kernel(x, y, alpha, shifts, weights) for y in nodes] for x in nodes]
    minors = [determinant([row[:n] for row in matrix[:n]]) for n in range(1, 4)]
    return {
        "schema_version": "1.0",
        "result_id": "K1106-K1105-SYMMETRIC-LOEWNER-FACTORIZATION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "kernel": "K_S(x,y)=(S(x)-S(y))/(x-y), with diagonal K_S(x,x)=S'(x)",
        "factorization": "K=alpha*11^T+V diag(w_i) V^T, V_ji=1/(x_j+d_i)",
        "theorem": "for alpha>=0 and w_i>0, every finite symmetric Loewner matrix is positive semidefinite; with distinct shifts and alpha>0 its rank is min(n,m+1)",
        "fixture_nodes": [int(x) for x in nodes],
        "fixture_matrix": [[str(v) for v in row] for row in matrix],
        "leading_principal_minors": [str(v) for v in minors],
        "fixture_rank": 3,
        "fixture_determinant": str(determinant(matrix)),
        "decision": "the positive diagonal Stieltjes branch has an exact positive finite-rank Loewner kernel whose rank exposes affine-plus-pole complexity on sufficiently rich data",
        "scope_boundary": "conditional rational-function theorem; no source-selected GU Hessian, physical derivative record or apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["kernel"].startswith("K_S(x,y)=")
    assert "V diag(w_i) V^T" in d["factorization"]
    assert "positive semidefinite" in d["theorem"] and "min(n,m+1)" in d["theorem"]
    assert d["fixture_nodes"] == [0, 1, 2]
    assert d["fixture_matrix"] == [
        ["31/9", "17/6", "13/5"],
        ["17/6", "5/2", "71/30"],
        ["13/5", "71/30", "511/225"],
    ]
    assert d["leading_principal_minors"] == ["31/9", "7/12", "2/2025"]
    assert d["fixture_rank"] == 3
    assert d["fixture_determinant"] == "2/2025"
    assert "finite-rank Loewner kernel" in d["decision"]
    assert "no source-selected GU Hessian" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1106 controls: 11/11")
