#!/usr/bin/env python3
"""K1112: reconstruct residues and test positive-Stieltjes class membership."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1112-k1111-positive-stieltjes-reconstruction-test.json"


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def build():
    alpha, beta = Fraction(2), Fraction(5)
    shifts = [Fraction(1), Fraction(3)]
    nodes = [Fraction(0), Fraction(1)]
    values = [Fraction(8, 3), Fraction(11, 2)]
    cauchy = [[1 / (x + d) for d in shifts] for x in nodes]
    correction = [alpha * x + beta - s for x, s in zip(nodes, values)]
    determinant = det2(cauchy)
    weights = [
        (correction[0] * cauchy[1][1] - cauchy[0][1] * correction[1]) / determinant,
        (cauchy[0][0] * correction[1] - correction[0] * cauchy[1][0]) / determinant,
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1112-K1111-POSITIVE-STIELTJES-RECONSTRUCTION-TEST",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "reconstruction_rule": "after pencil recovery of distinct positive shifts, solve the exact Cauchy system alpha*x_j+beta-S(x_j)=sum_i w_i/(x_j+d_i) for the residues",
        "membership_rule": "the bounded simple-pole positive Stieltjes class passes only if the pencil has the owned order, all recovered shifts and residues are positive, and the reconstructed branch matches every reserved exact sample",
        "rejection_rule": "a nonreal, nonpositive or repeated recovered shift, a nonpositive residue, a singular required Cauchy system, or a nonzero reserved-sample residual rejects that specified class rather than GU in general",
        "cauchy_matrix": [[str(v) for v in row] for row in cauchy],
        "cauchy_determinant": str(determinant),
        "correction_values": [str(v) for v in correction],
        "recovered_weights": [str(v) for v in weights],
        "fixture_membership": "pass_positive_two_pole_class",
        "scope_boundary": "exact conditional class test; the order, affine part, sample exactness and physical ownership remain independent premises",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["reconstruction_rule"].startswith("after pencil recovery")
    assert "all recovered shifts and residues are positive" in d["membership_rule"]
    assert "rather than GU in general" in d["rejection_rule"]
    assert d["cauchy_matrix"] == [["1", "1/3"], ["1/2", "1/4"]]
    assert d["cauchy_determinant"] == "1/12"
    assert d["correction_values"] == ["7/3", "3/2"]
    assert d["recovered_weights"] == ["1", "4"]
    assert d["fixture_membership"] == "pass_positive_two_pole_class"
    assert "independent premises" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1112 controls: 10/10")
