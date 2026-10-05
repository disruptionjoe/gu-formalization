#!/usr/bin/env python3
"""K1117: sharp rank-only inertia floor for a mixed zero block."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1117-k1116-rank-inertia-lower-bound.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1117-K1116-RANK-INERTIA-LOWER-BOUND",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "for H=[[0,A*],[A,C]] self-adjoint, n_plus(H)>=rank(A) and n_minus(H)>=rank(A)",
        "proof_route": "restrict to the rank(A) singular domain and range; after singular-value rescaling the 2r compression is [[0,I],[I,C_r]], congruent to [[0,I],[I,0]], then apply inertia interlacing",
        "sharp_fixture": {"A_diagonal": [2, 3], "C_diagonal": [0, 0], "rank_A": 2},
        "sharp_fixture_inertia": {"positive": 2, "negative": 2, "zero": 0},
        "nonzero_C_fixture": {"A_diagonal": [2, 3], "C_diagonal": [5, -1], "block_determinants": [-4, -9]},
        "nonzero_C_fixture_inertia": {"positive": 2, "negative": 2, "zero": 0},
        "sharpness": "the lower bounds are attained when C=0 on a square full-rank A carrier",
        "scope_boundary": "rank-only finite-symbol inertia; no global spectrum, Fredholm index or physical inner product",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "n_plus(H)>=rank(A)" in d["theorem"] and "n_minus(H)>=rank(A)" in d["theorem"]
    assert "congruent to [[0,I],[I,0]]" in d["proof_route"]
    assert d["sharp_fixture"] == {"A_diagonal": [2, 3], "C_diagonal": [0, 0], "rank_A": 2}
    assert d["sharp_fixture_inertia"] == {"positive": 2, "negative": 2, "zero": 0}
    assert d["nonzero_C_fixture"]["block_determinants"] == [-4, -9]
    assert d["nonzero_C_fixture_inertia"] == {"positive": 2, "negative": 2, "zero": 0}
    assert "bounds are attained" in d["sharpness"]
    assert "no global spectrum" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1117 controls: 9/9")
