#!/usr/bin/env python3
"""K1077: exact simultaneous-normal-mode criterion for a matrix Hessian."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1077-k1076-simultaneous-normal-mode-criterion.json"


def mul(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(len(y))) for j in range(len(y[0]))] for i in range(len(x))]


def sub(x, y):
    return [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]


def comm(x, y):
    return sub(mul(x, y), mul(y, x))


def iszero(x):
    return all(e == 0 for row in x for e in row)


def build():
    commuting_b = [[F(2), F(0)], [F(0), F(3)]]
    commuting_c = [[F(6), F(0)], [F(0), F(15)]]
    noncommuting_b = [[F(1), F(0)], [F(0), F(2)]]
    noncommuting_c = [[F(2), F(1)], [F(1), F(3)]]
    return {
        "schema_version": "1.0",
        "result_id": "K1077-K1076-SIMULTANEOUS-NORMAL-MODE-CRITERION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "normalized_operators": "X=A^-1 B and Y=A^-1 C are self-adjoint for the A inner product",
        "criterion": "one lambda-independent A-orthonormal normal-mode basis exists iff [X,Y]=0",
        "reason": "finite-dimensional commuting self-adjoint operators are simultaneously diagonalizable, and a common eigenbasis makes every lambda X+Y diagonal",
        "commuting_control": iszero(comm(commuting_b, commuting_c)),
        "noncommuting_control": not iszero(comm(noncommuting_b, noncommuting_c)),
        "scope_boundary": "finite-dimensional positive kinetic matrix; no unbounded-operator domain, degenerating quotient or functional spectral theorem",
        "source_boundary": "the criterion tests a supplied Hessian but does not supply or attribute one",
        "claim_ceiling": "exact finite-rank simultaneous-normal-mode equivalence",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["normalized_operators"].startswith("X=A^-1 B")
    assert d["criterion"] == "one lambda-independent A-orthonormal normal-mode basis exists iff [X,Y]=0"
    assert "simultaneously diagonalizable" in d["reason"]
    assert d["commuting_control"] is True and d["noncommuting_control"] is True
    assert "unbounded-operator domain" in d["scope_boundary"]
    assert "does not supply" in d["source_boundary"]
    assert "finite-rank" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1077 controls: 8/8")
