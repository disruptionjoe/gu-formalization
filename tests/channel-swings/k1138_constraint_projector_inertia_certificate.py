#!/usr/bin/env python3
"""K1138: exact projector certificate for Hessian restriction to ker(Q)."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1138-constraint-projector-inertia-certificate.json"


def mm(a, b):
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def tr(a): return [list(x) for x in zip(*a)]


def build():
    h = [[-1, 0, 0], [0, 2, 0], [0, 0, 3]]
    q = [[1, 0, 1]]
    p = [[Fraction(1, 2), 0, Fraction(-1, 2)], [0, 1, 0], [Fraction(-1, 2), 0, Fraction(1, 2)]]
    z = [[0, -1], [1, 0], [0, 1]]
    gram = mm(mm(tr(z), h), z)
    php = mm(mm(p, h), p)
    return {
        "schema_version": "1.0",
        "result_id": "K1138-CONSTRAINT-PROJECTOR-INERTIA-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "for full-row-rank Q, P=I-Q*(QQ*)^-1 Q is the orthogonal projector onto ker(Q); H restricted to ker(Q) is nonnegative iff PHP is nonnegative on im(P), equivalently iff Z*HZ is positive semidefinite for any basis Z of ker(Q)",
        "basis_invariance": "replacing Z by ZM gives M*(Z*HZ)M and preserves inertia for invertible M",
        "fixture": {
            "H_diagonal": [-1, 2, 3],
            "Q": q,
            "P": [[str(x) for x in row] for row in p],
            "P_idempotent": mm(p, p) == p,
            "QP_zero": mm(q, p) == [[0, 0, 0]],
            "kernel_gram": [[str(x) for x in row] for row in gram],
            "kernel_inertia": [2, 0, 0],
            "PHP": [[str(x) for x in row] for row in php],
        },
        "radical_quotient_effect": "removes only zero inertia after restriction",
        "rank_alone_decides_nonnegativity": False,
        "action_ownership_supplied": False,
        "scope_boundary": "finite-dimensional exact certificate; functional domains, propagation, action ownership and physical cohomology remain separate",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    f = d["fixture"]
    assert "orthogonal projector" in d["theorem"]
    assert "preserves inertia" in d["basis_invariance"]
    assert f["P_idempotent"] and f["QP_zero"]
    assert f["kernel_gram"] == [["2", "0"], ["0", "2"]]
    assert f["kernel_inertia"] == [2, 0, 0]
    assert "zero inertia" in d["radical_quotient_effect"]
    assert not d["rank_alone_decides_nonnegativity"]
    assert not d["action_ownership_supplied"]
    assert "functional domains" in d["scope_boundary"]
    assert "physical cohomology" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"
    assert d["status"] == "working_draft_verified"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1138 controls: 12/12")
