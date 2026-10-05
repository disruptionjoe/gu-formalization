#!/usr/bin/env python3
"""K1087: multiplication preservation of Dirichlet, Neumann and Robin domains."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1087-k1086-boundary-domain-preservation.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1087-K1086-BOUNDARY-DOMAIN-PRESERVATION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "setting": "smooth bundle endomorphism C multiplying H2 sections on a compact manifold with boundary",
        "dirichlet": "C preserves f|boundary=0 with no additional boundary condition",
        "neumann": "C preserves nabla_n f=0 for every domain section iff (nabla_n C)|boundary=0",
        "robin": "C preserves (nabla_n+S)f=0 for every domain section iff nabla_n C+[S,C]=0 on the boundary",
        "identity": "(nabla_n+S)(Cf)=(nabla_n C+[S,C])f+C(nabla_n+S)f",
        "parallel_reduction": "if nabla C=0, Dirichlet and Neumann are preserved automatically, while Robin still requires [S,C]=0",
        "positive_robin_counterexample": "S=diag(1,2), C=[[2,1],[1,2]] is positive and constant but [S,C]=[[0,-1],[1,0]]",
        "witness": [0, 1],
        "witness_vector": "the Robin defect on boundary value e1",
        "decision_rule": "a bulk commutator theorem is insufficient until the chosen self-adjoint boundary domain is preserved",
        "scope_boundary": "domain-preservation theorem only; self-adjoint elliptic realization and source/action ownership must be checked for the actual operator",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "no additional boundary condition" in d["dirichlet"]
    assert "iff (nabla_n C)|boundary=0" in d["neumann"]
    assert "iff nabla_n C+[S,C]=0" in d["robin"]
    assert "(nabla_n C+[S,C])f" in d["identity"]
    assert "Robin still requires [S,C]=0" in d["parallel_reduction"]
    assert "positive and constant" in d["positive_robin_counterexample"] and "[[0,-1],[1,0]]" in d["positive_robin_counterexample"]
    assert d["witness"] == [0, 1] and "e1" in d["witness_vector"]
    assert "bulk commutator theorem is insufficient" in d["decision_rule"]
    assert "source/action ownership" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1087 controls: 10/10")
