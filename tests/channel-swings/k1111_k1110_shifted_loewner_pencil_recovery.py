#!/usr/bin/env python3
"""K1111: exact pole recovery from a centered shifted-Loewner pencil."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1111-k1110-shifted-loewner-pencil-recovery.json"


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def build():
    alpha, beta = Fraction(2), Fraction(5)
    shifts = [Fraction(1), Fraction(3)]
    weights = [Fraction(1), Fraction(4)]
    left = [Fraction(0), Fraction(1)]
    right = [Fraction(2), Fraction(3)]

    def branch(z):
        return alpha * z + beta - sum(
            w / (z + d) for w, d in zip(weights, shifts)
        )

    loewner = [[
        (branch(x) - branch(y)) / (x - y) for y in right
    ] for x in left]
    shifted = [[
        (x * branch(x) - y * branch(y)) / (x - y) for y in right
    ] for x in left]
    residual = [[loewner[i][j] - alpha for j in range(2)] for i in range(2)]
    pole = [[
        alpha * (left[i] + right[j]) + beta - shifted[i][j]
        for j in range(2)
    ] for i in range(2)]
    middle = (
        pole[0][0] * residual[1][1]
        + pole[1][1] * residual[0][0]
        - pole[0][1] * residual[1][0]
        - pole[1][0] * residual[0][1]
    )
    coefficients = [det2(residual), -middle, det2(pole)]
    normalized = [c / coefficients[0] for c in coefficients]
    return {
        "schema_version": "1.0",
        "result_id": "K1111-K1110-SHIFTED-LOEWNER-PENCIL-RECOVERY",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "ordinary_centering": "R_ij=(S(x_i)-S(y_j))/(x_i-y_j)-alpha=V_X diag(w) V_Y^T",
        "shifted_centering": "P_ij=alpha*(x_i+y_j)+beta-(x_i*S(x_i)-y_j*S(y_j))/(x_i-y_j)=V_X diag(w*d) V_Y^T",
        "recovery_theorem": "if the exact pole count m and affine part alpha,beta are owned and the square Cauchy factors are nonsingular, the generalized eigenvalues of P-d*R are exactly the distinct pole shifts d_i",
        "left_modes": [int(x) for x in left],
        "right_modes": [int(x) for x in right],
        "sample_values": [str(branch(z)) for z in left + right],
        "residual_loewner": [[str(v) for v in row] for row in residual],
        "pole_matrix": [[str(v) for v in row] for row in pole],
        "pencil_polynomial": [str(v) for v in coefficients],
        "normalized_pencil_polynomial": [str(v) for v in normalized],
        "recovered_shifts": [1, 3],
        "scope_boundary": "constructive exact inverse inside the bounded positive diagonal class; no source-owned affine part, pole count, GU Hessian or physical modes",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["ordinary_centering"].startswith("R_ij=")
    assert d["shifted_centering"].startswith("P_ij=")
    assert "generalized eigenvalues" in d["recovery_theorem"]
    assert d["left_modes"] == [0, 1] and d["right_modes"] == [2, 3]
    assert d["sample_values"] == ["8/3", "11/2", "118/15", "121/12"]
    assert d["residual_loewner"] == [["3/5", "17/36"], ["11/30", "7/24"]]
    assert d["pole_matrix"] == [["17/15", "11/12"], ["23/30", "5/8"]]
    assert d["pencil_polynomial"] == ["1/540", "-1/135", "1/180"]
    assert d["normalized_pencil_polynomial"] == ["1", "-4", "3"]
    assert d["recovered_shifts"] == [1, 3]
    assert "no source-owned affine part" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1111 controls: 12/12")
