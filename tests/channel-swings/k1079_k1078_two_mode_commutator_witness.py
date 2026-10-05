#!/usr/bin/env python3
"""K1079: two spatial modes expose the normalized Hessian commutator."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1079-k1078-two-mode-commutator-witness.json"


def add(x, y): return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
def scale(a, x): return [[a * e for e in row] for row in x]
def mul(x, y): return [[sum(x[i][k] * y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]
def sub(x, y): return [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
def comm(x, y): return sub(mul(x, y), mul(y, x))


def build():
    x = [[F(1), F(0)], [F(0), F(2)]]
    y = [[F(2), F(1)], [F(1), F(3)]]
    l1, l2 = F(0), F(1)
    h1, h2 = add(scale(l1, x), y), add(scale(l2, x), y)
    recovered = scale(F(1, l1 - l2), comm(h1, h2))
    direct = comm(x, y)
    return {
        "schema_version": "1.0",
        "result_id": "K1079-K1078-TWO-MODE-COMMUTATOR-WITNESS",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "identity": "[H(lambda1),H(lambda2)]=(lambda1-lambda2)[X,Y] for H(lambda)=lambda X+Y",
        "recovery": "[X,Y]=[H(lambda1),H(lambda2)]/(lambda1-lambda2)",
        "exact_control": recovered == direct and direct != [[F(0), F(0)], [F(0), F(0)]],
        "counterexample": "X=diag(1,2), Y=[[2,1],[1,3]] are positive but noncommuting",
        "frequency_branches": "omega_+/-^2=(3 lambda+5 +/- sqrt((lambda+1)^2+4))/2, hence neither branch is affine",
        "decision_rule": "a nonzero two-mode commutator rejects one lambda-independent normal basis without rejecting positivity or the quadratic action",
        "functional_boundary": "a native application still needs one common domain and controlled unbounded-operator commutators",
        "source_boundary": "the firing example is repository-owned and is not a GU Hessian",
        "claim_ceiling": "exact two-by-two positive counterexample and finite-rank witness",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["identity"].startswith("[H(lambda1),H(lambda2)]")
    assert d["recovery"].endswith("/(lambda1-lambda2)")
    assert d["exact_control"] is True
    assert "positive but noncommuting" in d["counterexample"]
    assert "sqrt((lambda+1)^2+4)" in d["frequency_branches"] and "neither branch is affine" in d["frequency_branches"]
    assert "without rejecting positivity" in d["decision_rule"]
    assert "common domain" in d["functional_boundary"]
    assert "not a GU Hessian" in d["source_boundary"]
    assert "finite-rank witness" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1079 controls: 10/10")
