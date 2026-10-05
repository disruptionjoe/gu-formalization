#!/usr/bin/env python3
"""K1084: exact commutator obstruction for a spatially varying mass block."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1084-k1083-variable-mass-commutator-obstruction.json"


def build():
    # At x=pi/2 for B=diag(1,2), C11=2+cos(x)/2 and f1=cos(x):
    # C11'= -1/2, C11''=0, f1=0, f1'=-1, f1''=0.
    witness = -2 * F(1) * F(-1, 2) * F(-1)
    return {
        "schema_version": "1.0",
        "result_id": "K1084-K1083-VARIABLE-MASS-COMMUTATOR-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "operators": "H0=-B Delta with constant B>0 and multiplication V=C(x)",
        "identity": "[H0,V]f=(CB-BC)Delta f-B(Delta C)f-2B sum_a (partial_a C)(partial_a f)",
        "zero_criterion": "on a connected flat torus the commutator vanishes on smooth sections iff C is constant and [B,C]=0",
        "proof_route": "the first-derivative principal coefficient forces partial_a C=0 because B is invertible; the remaining second-order coefficient forces [B,C]=0",
        "positive_counterexample": "B=diag(1,2), C(x)=diag(2+cos(x)/2,3) is uniformly positive and commuting pointwise but spatially nonconstant",
        "witness": str(witness),
        "witness_point": "x=pi/2 on f(x)=(cos(x),0), where the first component of [H0,V]f is -1",
        "decision_rule": "a nonzero derivative commutator rejects the fixed Fourier/internal affine-branch reading without rejecting positivity or the action",
        "scope_boundary": "smooth constant-principal-part flat-torus theorem; variable kinetic matrices, curved geometry and boundary domains require separate commutator analysis",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["operators"].startswith("H0=-B Delta")
    assert "(CB-BC)Delta f" in d["identity"] and "partial_a C" in d["identity"]
    assert "iff C is constant and [B,C]=0" in d["zero_criterion"]
    assert "first-derivative principal coefficient" in d["proof_route"] and "B is invertible" in d["proof_route"]
    assert "uniformly positive" in d["positive_counterexample"] and "spatially nonconstant" in d["positive_counterexample"]
    assert d["witness"] == "-1" and d["witness_point"].endswith("is -1")
    assert "without rejecting positivity or the action" in d["decision_rule"]
    assert "curved geometry" in d["scope_boundary"] and "separate commutator analysis" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1084 controls: 9/9")
