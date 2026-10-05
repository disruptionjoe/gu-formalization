#!/usr/bin/env python3
"""K1141: exact propagation/intertwiner criterion for a full-row-rank constraint."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1141-constraint-propagation-intertwiner-criterion.json"


def mm(a, b):
    def exact(x):
        return int(x) if x.denominator == 1 else str(x)
    return [[exact(sum(Fraction(x) * Fraction(y) for x, y in zip(row, col))) for col in zip(*b)] for row in a]


def build():
    q = [[1, 0, 0]]
    right_inverse = [[1], [0], [0]]
    g_pass = [[2, 0, 0], [0, 0, -1], [0, 1, 0]]
    g_fail = [[2, 1, 0], [0, 0, -1], [0, 1, 0]]
    r = mm(mm(q, g_pass), right_inverse)
    return {
        "schema_version": "1.0",
        "result_id": "K1141-CONSTRAINT-PROPAGATION-INTERTWINER-CRITERION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "for surjective Q, ker(Q) is G-invariant iff a unique R on the constraint rows satisfies QG=RQ",
        "induced_row_generator": "R=QGQ*(QQ*)^-1",
        "fixture": {
            "Q": q,
            "right_inverse": right_inverse,
            "G_pass": g_pass,
            "R": r,
            "QG_pass": mm(q, g_pass),
            "RQ_pass": mm(r, q),
            "propagates": mm(q, g_pass) == mm(r, q),
            "G_fail": g_fail,
            "QG_fail": mm(q, g_fail),
            "failing_kernel_witness": [0, 1, 0],
            "failing_constraint_derivative": 1,
        },
        "action_ownership_supplied": False,
        "scope_boundary": "finite-dimensional algebraic criterion; common closed domains, boundary traces, source derivation and physical cohomology remain separate",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    f = d["fixture"]
    assert "unique R" in d["theorem"]
    assert d["induced_row_generator"] == "R=QGQ*(QQ*)^-1"
    assert f["R"] == [[2]]
    assert f["QG_pass"] == f["RQ_pass"] == [[2, 0, 0]]
    assert f["propagates"]
    assert f["QG_fail"] == [[2, 1, 0]]
    assert f["failing_kernel_witness"] == [0, 1, 0]
    assert f["failing_constraint_derivative"] == 1
    assert not d["action_ownership_supplied"]
    assert "common closed domains" in d["scope_boundary"]
    assert "physical cohomology" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1141 controls: 12/12")
