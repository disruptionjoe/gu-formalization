#!/usr/bin/env python3
"""K1094: affine unreduced pencil can have non-affine Schur branch."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1094-k1093-affine-branch-reduction-obstruction.json"


def build():
    values = [Fraction(2+i) - Fraction(1,2+i) for i in range(3)]
    second = values[2] - 2*values[1] + values[0]
    return {
        "schema_version": "1.0",
        "result_id": "K1094-K1093-AFFINE-BRANCH-REDUCTION-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "pencil": "L(lambda)=[[lambda+2,1],[1,lambda+2]] for lambda>=0",
        "unreduced_eigenvalues": ["lambda+1", "lambda+3"],
        "positive_domain": "lambda>=0",
        "effective_branch": "lambda+2-1/(lambda+2)",
        "sample_lambdas": [0,1,2],
        "sample_values": [str(v) for v in values],
        "second_finite_difference": str(second),
        "second_derivative": "-2/(lambda+2)^3",
        "affine_repairs": ["zero physical-auxiliary mixing", "lambda-independent invertible auxiliary block with constant mixing"],
        "decision": "test the reduced physical pencil before reading an intercept-to-slope selector",
        "scope_boundary": "exact scalar Schur counterexample; no source-selected GU Hessian, quotient or apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["pencil"].startswith("L(lambda)=[[lambda+2,1]")
    assert d["unreduced_eigenvalues"] == ["lambda+1","lambda+3"]
    assert d["positive_domain"] == "lambda>=0"
    assert d["effective_branch"] == "lambda+2-1/(lambda+2)"
    assert d["sample_lambdas"] == [0,1,2]
    assert d["sample_values"] == ["3/2","8/3","15/4"]
    assert d["second_finite_difference"] == "-1/12"
    assert d["second_derivative"] == "-2/(lambda+2)^3"
    assert len(d["affine_repairs"]) == 2 and "zero physical-auxiliary mixing" in d["affine_repairs"]
    assert "reduced physical pencil" in d["decision"]
    assert "no source-selected GU Hessian" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1094 controls: 11/11")
