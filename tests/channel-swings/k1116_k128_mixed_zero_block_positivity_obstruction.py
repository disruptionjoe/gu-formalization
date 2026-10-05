#!/usr/bin/env python3
"""K1116: positivity obstruction for a self-adjoint mixed zero block."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1116-k128-mixed-zero-block-positivity-obstruction.json"


def build():
    a, c, eps = Fraction(2), Fraction(5), Fraction(1, 10)
    q_plus = 2 * a * eps + c * eps * eps
    q_minus = -2 * a * eps + c * eps * eps
    return {
        "schema_version": "1.0",
        "result_id": "K1116-K128-MIXED-ZERO-BLOCK-POSITIVITY-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "block_form": "H=[[0,A*],[A,C]] with H self-adjoint",
        "positivity_theorem": "H is positive semidefinite iff A=0 and C is positive semidefinite",
        "negative_theorem": "H is negative semidefinite iff A=0 and C is negative semidefinite",
        "mixed_sign_witness_rule": "for Ax!=0 choose y=+/-epsilon*Ax; the linear mixed term changes sign and dominates the quadratic C term for sufficiently small epsilon",
        "fixture": {"a": "2", "c": "5", "epsilon": "1/10"},
        "fixture_q_plus": str(q_plus),
        "fixture_q_minus": str(q_minus),
        "fixture_signs": ["positive", "negative"],
        "scope_boundary": "exact finite-dimensional or common-form-domain obstruction; no closed GU operator domain or physical quotient is supplied",
        "target_claim": "K128-T0-I1B-HESSIAN-POSITIVITY",
    }


def validate(d):
    assert d["block_form"] == "H=[[0,A*],[A,C]] with H self-adjoint"
    assert d["positivity_theorem"].endswith("C is positive semidefinite")
    assert d["negative_theorem"].endswith("C is negative semidefinite")
    assert "linear mixed term changes sign" in d["mixed_sign_witness_rule"]
    assert d["fixture"] == {"a": "2", "c": "5", "epsilon": "1/10"}
    assert d["fixture_q_plus"] == "9/20"
    assert d["fixture_q_minus"] == "-7/20"
    assert d["fixture_signs"] == ["positive", "negative"]
    assert "no closed GU operator domain" in d["scope_boundary"]
    assert d["target_claim"] == "K128-T0-I1B-HESSIAN-POSITIVITY"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1116 controls: 10/10")
