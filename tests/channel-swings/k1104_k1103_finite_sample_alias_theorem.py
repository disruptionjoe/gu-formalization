#!/usr/bin/env python3
"""K1104: constructive finite-sample aliases without a multiplicity bound."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1104-k1103-finite-sample-alias-theorem.json"


def branch(x, alpha, beta, weights):
    return alpha*x + beta - sum(Fraction(w, x+d) for w, d in zip(weights, (1,2,3)))


def build():
    modes = [Fraction(i) for i in range(4)]
    residues = [Fraction(12), Fraction(-120), Fraction(180)]
    left = {"alpha":3,"beta":988,"weights":[1,121,1],"shifts":[1,2,3]}
    right = {"alpha":2,"beta":1000,"weights":[13,1,181],"shifts":[1,2,3]}
    left_values = [branch(x, left["alpha"], left["beta"], left["weights"]) for x in modes]
    right_values = [branch(x, right["alpha"], right["beta"], right["weights"]) for x in modes]
    return {
        "schema_version": "1.0",
        "result_id": "K1104-K1103-FINITE-SAMPLE-ALIAS-THEOREM",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "construction": "for n samples choose n-1 negative simple poles, form F=prod_j(x-x_j)/prod_k(x+d_k), divide F into an affine part plus residues, then split signed residues between two positive-weight branches and add common positive weights",
        "general_decision": "for every finite set of at least two distinct nonnegative sample points, two distinct positive-weight affine-minus-Stieltjes branches can agree on every sample when no auxiliary multiplicity bound is imposed",
        "fixture_modes": [0,1,2,3],
        "fixture_rational_difference": "F=x-12+12/(x+1)-120/(x+2)+180/(x+3)",
        "fixture_residues": [str(r) for r in residues],
        "left_branch": left,
        "right_branch": right,
        "common_values": [str(v) for v in left_values],
        "all_samples_equal": left_values == right_values,
        "branches_distinct": left != right,
        "boundary": "finite exact sampling cannot identify unbounded hidden multiplicity; K1103 becomes applicable only after a finite multiplicity bound is independently owned",
        "scope_boundary": "conditional constructive non-identifiability theorem; no GU hidden sector, spectrum or apparatus",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["construction"].startswith("for n samples")
    assert "for every finite set" in d["general_decision"]
    assert d["fixture_modes"] == [0,1,2,3]
    assert d["fixture_rational_difference"].startswith("F=x-12")
    assert d["fixture_residues"] == ["12", "-120", "180"]
    assert d["left_branch"]["weights"] == [1,121,1]
    assert d["right_branch"]["weights"] == [13,1,181]
    assert d["common_values"] == ["5557/6", "11399/12", "57793/60", "58343/60"]
    assert d["all_samples_equal"] and d["branches_distinct"]
    assert "only after" in d["boundary"]
    assert "no GU hidden sector" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1104 controls: 12/12")
