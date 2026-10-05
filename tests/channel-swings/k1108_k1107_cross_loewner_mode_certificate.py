#!/usr/bin/env python3
"""K1108: derivative-free cross-Loewner certificate on disjoint mode sets."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1108-k1107-cross-loewner-mode-certificate.json"


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = Fraction(1)
    for i in range(len(a)):
        pivot = next(j for j in range(i, len(a)) if a[j][i])
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            out = -out
        q = a[i][i]; out *= q
        for j in range(i + 1, len(a)):
            ratio = a[j][i] / q
            for k in range(i, len(a)):
                a[j][k] -= ratio * a[i][k]
    return out


def build():
    left = [Fraction(0), Fraction(1), Fraction(2)]
    right = [Fraction(3), Fraction(4), Fraction(5)]
    alpha = Fraction(2); shifts = [Fraction(1), Fraction(3)]; weights = [Fraction(1), Fraction(4)]
    matrix = [[alpha + sum(w / ((x + d) * (y + d)) for d, w in zip(shifts, weights)) for y in right] for x in left]
    return {
        "schema_version": "1.0",
        "result_id": "K1108-K1107-CROSS-LOEWNER-MODE-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "cross_kernel": "D_ij=(S(x_i)-S(y_j))/(x_i-y_j)=alpha+sum_k w_k/((x_i+d_k)(y_j+d_k))",
        "data_type": "values at two disjoint exact mode sets; no derivatives",
        "rank_theorem": "an (m+1)-by-(m+1) cross-Loewner matrix has nonzero determinant for alpha>0, positive weights, distinct shifts and distinct regular nodes",
        "left_modes": [int(x) for x in left],
        "right_modes": [int(x) for x in right],
        "fixture_matrix": [[str(v) for v in row] for row in matrix],
        "fixture_determinant": str(determinant(matrix)),
        "fixture_rank": 3,
        "fixture_conclusion": "six exact values certify at least two poles for the K1098 branch; with an independently owned at-most-two cap they certify exact order two",
        "relation_to_k1103": "the certificate uses the same 2m+2 exact values as K1103 for m=2 but supplies a constructive rank witness, not parameter recovery or an unbounded upper-order exclusion",
        "scope_boundary": "conditional derivative-free rank certificate; modes, multiplicity cap, physical branch and apparatus remain unowned",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["cross_kernel"].startswith("D_ij=")
    assert d["data_type"].endswith("no derivatives")
    assert "nonzero determinant" in d["rank_theorem"]
    assert d["left_modes"] == [0, 1, 2] and d["right_modes"] == [3, 4, 5]
    assert d["fixture_matrix"] == [
        ["89/36", "251/105", "7/3"],
        ["55/24", "157/70", "53/24"],
        ["133/60", "229/105", "97/45"],
    ]
    assert d["fixture_determinant"] == "1/113400"
    assert d["fixture_rank"] == 3
    assert "at least two poles" in d["fixture_conclusion"]
    assert "same 2m+2 exact values" in d["relation_to_k1103"]
    assert "apparatus remain unowned" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1108 controls: 11/11")
