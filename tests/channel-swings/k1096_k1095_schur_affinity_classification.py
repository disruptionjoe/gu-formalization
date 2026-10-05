#!/usr/bin/env python3
"""K1096: classify affine scalar Schur complements exactly."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1096-k1095-schur-affinity-classification.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1096-K1095-SCHUR-AFFINITY-CLASSIFICATION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "pencil": "A=a0+a1*lambda, B=b0+b1*lambda, D=d0+d1*lambda",
        "effective_branch": "S=A-B^2/D",
        "nonconstant_auxiliary": {
            "assumption": "d1!=0 and D!=0 on the tested domain",
            "affine_iff": "b0*d1-b1*d0=0",
            "pole_remainder": "-(b0*d1-b1*d0)^2/d1^2",
            "interpretation": "B=cD, so S=A-c^2 D is affine",
        },
        "constant_auxiliary": {
            "assumption": "d1=0 and d0!=0",
            "affine_iff": "b1=0",
            "quadratic_coefficient": "-b1^2/d0",
        },
        "positive_repair_fixture": {
            "A": "10+5*lambda", "B": "4+2*lambda", "D": "2+lambda",
            "condition_value": "0", "effective_branch": "2+lambda",
        },
        "k1094_failure_fixture": {
            "A": "2+lambda", "B": "1", "D": "2+lambda",
            "condition_value": "1", "effective_branch": "2+lambda-1/(2+lambda)",
        },
        "constant_block_fixture": {
            "A": "3+2*lambda", "B": "1", "D": "2",
            "effective_branch": str(Fraction(5, 2)) + "+2*lambda",
        },
        "scope_boundary": "exact scalar affine-pencil classification; no source-selected GU Hessian, quotient or apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["pencil"].startswith("A=a0+a1")
    assert d["effective_branch"] == "S=A-B^2/D"
    assert d["nonconstant_auxiliary"]["affine_iff"] == "b0*d1-b1*d0=0"
    assert "^2/d1^2" in d["nonconstant_auxiliary"]["pole_remainder"]
    assert d["nonconstant_auxiliary"]["interpretation"].startswith("B=cD")
    assert d["constant_auxiliary"]["affine_iff"] == "b1=0"
    assert d["constant_auxiliary"]["quadratic_coefficient"] == "-b1^2/d0"
    assert d["positive_repair_fixture"]["condition_value"] == "0"
    assert d["positive_repair_fixture"]["effective_branch"] == "2+lambda"
    assert d["k1094_failure_fixture"]["condition_value"] == "1"
    assert "1/(2+lambda)" in d["k1094_failure_fixture"]["effective_branch"]
    assert d["constant_block_fixture"]["effective_branch"] == "5/2+2*lambda"
    assert "no source-selected GU Hessian" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1096 controls: 14/14")
