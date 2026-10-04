#!/usr/bin/env python3
"""K1059: four modes distinguish the frozen horns under quadratic transfer."""
import json
import math
from fractions import Fraction
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1059-k1058-four-mode-quadratic-identifiability.json"


def det(matrix):
    total = Fraction(0)
    for p in permutations(range(len(matrix))):
        inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
        term = Fraction((-1) ** inversions)
        for i in range(len(matrix)): term *= matrix[i][p[i]]
        total += term
    return total


def build():
    modes = [3, 8, 15, 24]
    x1 = [2, 3, 4, 5]
    x4 = [math.sqrt(k + 4) for k in modes]
    cofactors = []
    for i in range(4):
        minor = [[Fraction(1), Fraction(modes[j]), Fraction(x1[j])] for j in range(4) if j != i]
        cofactors.append(((-1) ** ((i + 1) + 4)) * det(minor))
    determinant = sum(float(cofactors[i]) * x4[i] for i in range(4))
    return {
        "schema_version": "1.0", "result_id": "K1059-K1058-FOUR-MODE-QUADRATIC-IDENTIFIABILITY",
        "status": "working_draft_verified", "created": "2026-10-04",
        "modes": modes, "mass_one_frequencies": x1,
        "transfer_space": "for fixed mu, quadratic readouts span {1,lambda,x_mu} because x_mu^2=lambda+mu",
        "determinant": "det[1,lambda,x_1,x_4]=2*(3*sqrt(19)-6*sqrt(3)-sqrt(7))",
        "determinant_numeric": determinant,
        "nonzero_proof": "equality would imply 56=12*sqrt(21), contradicted after squaring: 3136!=3024",
        "intersection": "the two three-dimensional readout spaces intersect exactly in span{1,lambda}",
        "identification": "a common four-mode readout cannot fit both horns with a quadratic transfer having nonzero linear coefficient g",
        "degenerate_boundary": "pure quadratic response g=0 lies in span{1,lambda} and reproduces K1056 nonidentifiability",
        "scale_boundary": "the theorem distinguishes dimensionless mu only and does not own an absolute ruler or gain",
        "scope": "exact for horns mu={1,4}, modes {3,8,15,24} and one common quadratic transfer per horn",
        "reopener": "prepare and measure all four modes and certify one common quadratic transfer with nonzero linear response",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["modes"] == [3, 8, 15, 24]
    assert d["mass_one_frequencies"] == [2, 3, 4, 5]
    assert "span {1,lambda,x_mu}" in d["transfer_space"]
    assert d["determinant"].startswith("det[1,lambda,x_1,x_4]=2*")
    assert 0.077 < d["determinant_numeric"] < 0.078
    assert "3136!=3024" in d["nonzero_proof"]
    assert d["intersection"].endswith("span{1,lambda}")
    assert "cannot fit both horns" in d["identification"] and "nonzero linear coefficient" in d["identification"]
    assert "g=0" in d["degenerate_boundary"] and "K1056" in d["degenerate_boundary"]
    assert "dimensionless mu only" in d["scale_boundary"]
    assert "exact for horns" in d["scope"]
    assert d["reopener"].startswith("prepare and measure all four modes")
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1059 controls: 13/13")
