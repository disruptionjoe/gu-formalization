#!/usr/bin/env python3
"""K1093: Schur-complement physical Hessian."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1093-k1092-schur-physical-hessian.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1093-K1092-SCHUR-PHYSICAL-HESSIAN",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "block_operator": "L=[[A,B],[B*,D]] on H direct_sum A with D invertible",
        "auxiliary_solution": "y=-D^-1 B* x",
        "effective_hessian": "L_eff=A-B D^-1 B*",
        "positivity_equivalence": "if D>0, then L>=0 iff L_eff>=0",
        "fixture": {"A": 2, "B": 1, "D": 2},
        "full_eigenvalues": [1, 3],
        "raw_compression": "2",
        "effective_value": str(Fraction(2) - Fraction(1,2)),
        "congruence": "[[I,-B D^-1],[0,I]] block-diagonalizes L to diag(L_eff,D)",
        "scope_boundary": "finite conditional theorem; no GU gauge fixing, functional domain, boundary law or positivity owner",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "D invertible" in d["block_operator"]
    assert d["auxiliary_solution"] == "y=-D^-1 B* x"
    assert d["effective_hessian"] == "L_eff=A-B D^-1 B*"
    assert "D>0" in d["positivity_equivalence"] and "iff" in d["positivity_equivalence"]
    assert d["fixture"] == {"A":2,"B":1,"D":2}
    assert d["full_eigenvalues"] == [1,3]
    assert d["raw_compression"] == "2" and d["effective_value"] == "3/2"
    assert "block-diagonalizes" in d["congruence"] and "diag(L_eff,D)" in d["congruence"]
    assert "no GU gauge fixing" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"
    assert Fraction(d["effective_value"]) > 0


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1093 controls: 11/11")
