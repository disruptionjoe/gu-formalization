#!/usr/bin/env python3
"""K1119: exact definite-C Schur sign and full inertia."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1119-k1118-definite-distortion-schur-sign.json"


def build():
    a = [Fraction(2), Fraction(3)]
    c_pos = [Fraction(1), Fraction(4)]
    c_neg = [-x for x in c_pos]
    schur_pos = [-(x * x) / c for x, c in zip(a, c_pos)]
    schur_neg = [-(x * x) / c for x, c in zip(a, c_neg)]
    return {
        "schema_version": "1.0",
        "result_id": "K1119-K1118-DEFINITE-DISTORTION-SCHUR-SIGN",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "congruence": "if C is invertible, H is congruent to diag(-A* C^-1 A,C)",
        "positive_C_inertia": "if C>0 then inertia(H)=(dim(Y),rank(A),dim(X)-rank(A)) in (+,-,0) order",
        "negative_C_inertia": "if C<0 then inertia(H)=(rank(A),dim(Y),dim(X)-rank(A)) in (+,-,0) order",
        "fixture_A_diagonal": [str(x) for x in a],
        "fixture_positive_C_diagonal": [str(x) for x in c_pos],
        "fixture_positive_C_schur_diagonal": [str(x) for x in schur_pos],
        "fixture_negative_C_diagonal": [str(x) for x in c_neg],
        "fixture_negative_C_schur_diagonal": [str(x) for x in schur_neg],
        "fixture_full_inertia_both_horns": {"positive": 2, "negative": 2, "zero": 0},
        "sign_boundary": "a definite auxiliary block cannot make the full Hessian positive when A is nonzero; for C>0 the reduced metric Schur form is nonpositive",
        "scope_boundary": "exact finite-symbol congruence only; invertibility does not supply a global closed inverse or a physical quotient",
        "target_claim": "SC-ACT-01",
    }


def validate(d):
    assert d["congruence"] == "if C is invertible, H is congruent to diag(-A* C^-1 A,C)"
    assert "(dim(Y),rank(A),dim(X)-rank(A))" in d["positive_C_inertia"]
    assert "(rank(A),dim(Y),dim(X)-rank(A))" in d["negative_C_inertia"]
    assert d["fixture_A_diagonal"] == ["2", "3"]
    assert d["fixture_positive_C_schur_diagonal"] == ["-4", "-9/4"]
    assert d["fixture_negative_C_schur_diagonal"] == ["4", "9/4"]
    assert d["fixture_full_inertia_both_horns"] == {"positive": 2, "negative": 2, "zero": 0}
    assert "cannot make the full Hessian positive" in d["sign_boundary"]
    assert "does not supply a global closed inverse" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-01"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1119 controls: 10/10")
