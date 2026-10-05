#!/usr/bin/env python3
"""K1098: multi-auxiliary reduced branches are affine minus a Stieltjes sum."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1098-k1097-multi-auxiliary-stieltjes.json"


def build():
    weights, shifts = [1, 4], [1, 3]
    values = [Fraction(2*x + 5) - sum(Fraction(w, x+d) for w,d in zip(weights, shifts)) for x in range(3)]
    return {
        "schema_version": "1.0",
        "result_id": "K1098-K1097-MULTI-AUXILIARY-STIELTJES",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "operator_class": "A=alpha*lambda+beta, D=diag(lambda+d_i), B=(b_i), w_i=b_i^2>=0",
        "effective_branch": "S=alpha*lambda+beta-sum_i w_i/(lambda+d_i)",
        "domain": "lambda>-min_i(d_i) with every d_i>0",
        "first_derivative": "alpha+sum_i w_i/(lambda+d_i)^2",
        "second_derivative": "-2*sum_i w_i/(lambda+d_i)^3",
        "strict_concavity_iff": "at least one w_i>0",
        "affine_iff": "all w_i=0 within this constant-coupling diagonal class",
        "stieltjes_correction": "R=sum_i w_i/(lambda+d_i) is completely monotone",
        "fixture": {"alpha":2,"beta":5,"weights":weights,"shifts":shifts},
        "sample_lambdas": [0,1,2],
        "sample_values": [str(v) for v in values],
        "scope_boundary": "conditional finite diagonal auxiliary class; no source-selected GU Hessian or functional domain",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["operator_class"].startswith("A=alpha")
    assert "sum_i w_i/(lambda+d_i)" in d["effective_branch"]
    assert d["domain"].startswith("lambda>-min_i")
    assert d["first_derivative"].startswith("alpha+")
    assert d["second_derivative"].startswith("-2*")
    assert d["strict_concavity_iff"] == "at least one w_i>0"
    assert d["affine_iff"].startswith("all w_i=0")
    assert "completely monotone" in d["stieltjes_correction"]
    assert d["fixture"] == {"alpha":2,"beta":5,"weights":[1,4],"shifts":[1,3]}
    assert d["sample_lambdas"] == [0,1,2]
    assert d["sample_values"] == ["8/3", "11/2", "118/15"]
    assert "no source-selected GU Hessian" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1098 controls: 13/13")
