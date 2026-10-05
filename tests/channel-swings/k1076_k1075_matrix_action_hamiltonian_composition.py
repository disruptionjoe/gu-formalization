#!/usr/bin/env python3
"""K1076: compose a positive matrix action with its Hamiltonian pairing."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1076-k1075-matrix-action-hamiltonian-composition.json"


def add(x, y):
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def mul(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]


def tr(x):
    return [list(row) for row in zip(*x)]


def block(z, x, y, w):
    n = len(z)
    return [z[i] + x[i] for i in range(n)] + [y[i] + w[i] for i in range(n)]


def build():
    a_inv = [[F(1, 2), F(0)], [F(0), F(1, 3)]]
    b = [[F(4), F(1)], [F(1), F(5)]]
    c = [[F(3), F(1)], [F(1), F(4)]]
    zero = [[F(0), F(0)], [F(0), F(0)]]
    controls = []
    for lam in (F(0), F(2), F(7)):
        d = add([[lam * e for e in row] for row in b], c)
        k = block(zero, a_inv, [[-e for e in row] for row in d], zero)
        s = block(d, zero, zero, a_inv)
        defect = add(mul(tr(k), s), mul(s, k))
        controls.append({"lambda": str(lam), "defect_zero": all(e == 0 for row in defect for e in row)})
    return {
        "schema_version": "1.0",
        "result_id": "K1076-K1075-MATRIX-ACTION-HAMILTONIAN-COMPOSITION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "action": "L_lambda=1/2 qdot^T A qdot-1/2 q^T(lambda B+C)q with A positive definite and B,C symmetric",
        "canonical_momentum": "p=A qdot",
        "generator": "K(lambda)=[[0,A^-1],[-(lambda B+C),0]]",
        "pairing": "S(lambda)=diag(lambda B+C,A^-1)",
        "identity": "K(lambda)^T S(lambda)+S(lambda)K(lambda)=0",
        "controls": controls,
        "positivity_boundary": "S(lambda) is positive exactly on modes where lambda B+C is positive, given A positive definite",
        "ownership": "finite-rank repository-owned candidate theorem; no source-owned GU Hessian or functional domain",
        "claim_ceiling": "exact finite-matrix action-to-Hamiltonian composition only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["canonical_momentum"] == "p=A qdot"
    assert d["generator"] == "K(lambda)=[[0,A^-1],[-(lambda B+C),0]]"
    assert d["pairing"] == "S(lambda)=diag(lambda B+C,A^-1)"
    assert d["identity"] == "K(lambda)^T S(lambda)+S(lambda)K(lambda)=0"
    assert len(d["controls"]) == 3 and all(x["defect_zero"] for x in d["controls"])
    assert "exactly on modes" in d["positivity_boundary"]
    assert "no source-owned GU Hessian" in d["ownership"]
    assert "finite-matrix" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1076 controls: 9/9")
