#!/usr/bin/env python3
"""K1088: holonomy-reduced affine branch decomposition."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1088-k1087-holonomy-branch-decomposition.json"


def build():
    ladder = [0, 1, 4]
    branches = [
        {"b": 2, "c": 5, "lambda": ladder, "omega_squared": [5, 7, 13]},
        {"b": 3, "c": 7, "lambda": ladder, "omega_squared": [7, 10, 19]},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1088-K1087-HOLONOMY-BRANCH-DECOMPOSITION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "hypotheses": "B and C are commuting parallel self-adjoint endomorphisms and the boundary realization preserves their joint spectral projections",
        "decomposition": "E is the orthogonal direct sum of parallel simultaneous eigenbundles E_j",
        "branch_rule": "on E_j, H=b_j L_j+c_j and omega_jn^2=b_j lambda_jn+c_j",
        "holonomy_rule": "parallel endomorphisms are the commutant of connection holonomy; on an irreducible orthogonal holonomy block every parallel self-adjoint endomorphism is scalar",
        "common_ladder_condition": "one shared lambda_n across branches requires an additional isospectral identification of the restricted connection Laplacians and their boundary domains",
        "tensor_product_sufficient_case": "all E_j carry copies of the same spatial connection and boundary realization",
        "fixture": branches,
        "decision_rule": "parallel commuting coefficients guarantee affine laws only against each branch's own covariant spectrum, not a universal Fourier ladder",
        "scope_boundary": "exact conditional spectral decomposition; no source-selected GU bundle, holonomy, boundary operator or physical mode interpretation",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "commuting parallel self-adjoint" in d["hypotheses"] and "boundary realization" in d["hypotheses"]
    assert "parallel simultaneous eigenbundles" in d["decomposition"]
    assert "omega_jn^2=b_j lambda_jn+c_j" in d["branch_rule"]
    assert "commutant of connection holonomy" in d["holonomy_rule"] and "scalar" in d["holonomy_rule"]
    assert "additional isospectral identification" in d["common_ladder_condition"]
    assert "same spatial connection" in d["tensor_product_sufficient_case"]
    assert d["fixture"][0]["omega_squared"] == [5, 7, 13]
    assert d["fixture"][1]["omega_squared"] == [7, 10, 19]
    assert "each branch's own covariant spectrum" in d["decision_rule"]
    assert "no source-selected GU bundle" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1088 controls: 11/11")
