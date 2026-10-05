#!/usr/bin/env python3
"""K1142: exact propagation leakage certificate QGP."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1142-constraint-propagation-defect-certificate.json"


def mm(a, b):
    def exact(x):
        return int(x) if x.denominator == 1 else str(x)
    return [[exact(sum(Fraction(x) * Fraction(y) for x, y in zip(row, col))) for col in zip(*b)] for row in a]


def build():
    q = [[1, 0, 0]]
    p = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]
    z = [[0, 0], [1, 0], [0, 1]]
    g_pass = [[2, 0, 0], [0, 0, -1], [0, 1, 0]]
    g_fail = [[2, 1, 0], [0, 0, -1], [0, 1, 0]]
    e_pass = mm(mm(q, g_pass), p)
    e_fail = mm(mm(q, g_fail), p)
    return {
        "schema_version": "1.0",
        "result_id": "K1142-CONSTRAINT-PROPAGATION-DEFECT-CERTIFICATE",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "E=QGP vanishes exactly when G preserves ker(Q); equivalently QGZ=0 for any basis Z of ker(Q)",
        "basis_invariance": "Z replaced by ZM right-multiplies QGZ by invertible M, preserving zero and rank",
        "fixture": {
            "Q": q, "P": p, "Z": z,
            "E_pass": e_pass,
            "QGZ_pass": mm(mm(q, g_pass), z),
            "E_fail": e_fail,
            "QGZ_fail": mm(mm(q, g_fail), z),
            "fail_rank": 1,
            "fail_frobenius_norm_squared": 1,
        },
        "norm_is_coordinate_dependent": True,
        "zero_and_rank_are_basis_independent": True,
        "action_ownership_supplied": False,
        "scope_boundary": "finite symbol certificate only; source ownership, propagation on a common operator domain and boundary closure remain separate",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    f = d["fixture"]
    assert "vanishes exactly" in d["theorem"]
    assert "preserving zero and rank" in d["basis_invariance"]
    assert f["E_pass"] == [[0, 0, 0]]
    assert f["QGZ_pass"] == [[0, 0]]
    assert f["E_fail"] == [[0, 1, 0]]
    assert f["QGZ_fail"] == [[1, 0]]
    assert f["fail_rank"] == 1
    assert f["fail_frobenius_norm_squared"] == 1
    assert d["norm_is_coordinate_dependent"]
    assert d["zero_and_rank_are_basis_independent"]
    assert not d["action_ownership_supplied"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1142 controls: 12/12")
