#!/usr/bin/env python3
"""K1072: classify symmetric pairings for one or two massive-wave generators."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1072-k1071-common-pairing-obstruction.json"


def defect(w, a, b, c):
    return [[-2*w*b, a-w*c], [a-w*c, 2*b]]


def build():
    controls = []
    for w in (F(1), F(4), F(11, 3)):
        controls.append({"omega_squared": str(w), "pairing": [str(w), "0", "1"], "defect": [[str(x) for x in row] for row in defect(w, w, 0, 1)]})
    return {
        "schema_version": "1.0",
        "result_id": "K1072-K1071-COMMON-PAIRING-OBSTRUCTION",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "general_pairing": "S=[[a,b],[b,c]]",
        "generator": "K_w=[[0,1],[-w,0]] with w=lambda+u>0",
        "defect_formula": "K_w^T S+S K_w=[[-2wb,a-wc],[a-wc,2b]]",
        "single_generator_solution": "b=0 and a=w c",
        "two_generator_theorem": "if w1!=w2 and the same S symmetrizes both, then a=b=c=0",
        "positive_consequence": "no nonzero positive-semidefinite coefficient-independent pairing symmetrizes two distinct masses at one fixed mode",
        "controls": controls,
        "contrary_boundary": "an indefinite or positive pairing may symmetrize one chosen coefficient; the obstruction concerns one fixed pairing for two distinct coefficients",
        "claim_ceiling": "exact two-generator linear-algebra obstruction inside the supplied candidate family",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["general_pairing"] == "S=[[a,b],[b,c]]"
    assert "w=lambda+u>0" in d["generator"]
    assert d["defect_formula"] == "K_w^T S+S K_w=[[-2wb,a-wc],[a-wc,2b]]"
    assert d["single_generator_solution"] == "b=0 and a=w c"
    assert "a=b=c=0" in d["two_generator_theorem"]
    assert d["positive_consequence"].startswith("no nonzero positive-semidefinite")
    assert len(d["controls"]) == 3 and all(c["defect"] == [["0", "0"], ["0", "0"]] for c in d["controls"])
    assert "one fixed pairing" in d["contrary_boundary"]
    assert "supplied candidate family" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data); OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1072 controls: 10/10")
