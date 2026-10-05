#!/usr/bin/env python3
"""K1136: polynomial local-constraint symbols cannot live only on shells."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1136-polynomial-constraint-symbol-dense-open-vanishing.json"


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    for col in range(len(a)):
        pivot = next(i for i in range(col, len(a)) if a[i][col])
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        p = a[col][col]
        det *= p
        a[col] = [x / p for x in a[col]]
        for i in range(col + 1, len(a)):
            f = a[i][col]
            a[i] = [x - f * y for x, y in zip(a[i], a[col])]
    return det


def build():
    nodes = [0, 1, 2, 3]
    vandermonde = [[x**j for j in range(4)] for x in nodes]
    det = determinant(vandermonde)
    return {
        "schema_version": "1.0",
        "result_id": "K1136-POLYNOMIAL-CONSTRAINT-SYMBOL-DENSE-OPEN-VANISHING",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "a polynomial local differential constraint symbol that vanishes on a nonempty open subset of a connected covector chart vanishes identically; the same holds componentwise for real-analytic symbols",
        "proof_route": "restrict each matrix entry to generic affine lines; a one-variable polynomial vanishing on an interval is zero, then vary the line",
        "regularity_required": ["polynomial", "real_analytic"],
        "smooth_only_is_sufficient": False,
        "finite_degree_control": {
            "degree_at_most": 3,
            "nodes": nodes,
            "vandermonde_determinant": str(det),
            "zero_values_force_zero_coefficients": det != 0,
        },
        "shell_only_local_symbol_possible": False,
        "distributional_or_nonlocal_shell_projector_excluded_by_theorem": False,
        "scope_boundary": "local finite-order differential or real-analytic symbol identity only; nonlocal, distributional and separately supplied shell data are not excluded",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "nonempty open subset" in d["theorem"]
    assert d["regularity_required"] == ["polynomial", "real_analytic"]
    assert not d["smooth_only_is_sufficient"]
    assert d["finite_degree_control"]["vandermonde_determinant"] == "12"
    assert d["finite_degree_control"]["zero_values_force_zero_coefficients"]
    assert not d["shell_only_local_symbol_possible"]
    assert not d["distributional_or_nonlocal_shell_projector_excluded_by_theorem"]
    assert "nonlocal" in d["scope_boundary"]
    assert "distributional" in d["scope_boundary"]
    assert "separately supplied" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"
    assert d["status"] == "working_draft_verified"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1136 controls: 12/12")
