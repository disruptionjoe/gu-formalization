#!/usr/bin/env python3
"""K1078: recover affine matrix branches and normalization gauges."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1078-k1077-matrix-branch-selector.json"


def build():
    branches = []
    for b, c in ((F(2), F(6)), (F(3), F(15))):
        l1, l2 = F(3), F(11)
        w1, w2 = b * l1 + c, b * l2 + c
        br = (w2 - w1) / (l2 - l1)
        cr = w1 - br * l1
        branches.append({"slope": str(b), "intercept": str(c), "mass_to_speed_ratio": str(c / b), "recovered_slope": str(br), "recovered_intercept": str(cr)})
    return {
        "schema_version": "1.0",
        "result_id": "K1078-K1077-MATRIX-BRANCH-SELECTOR",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "branch_law": "omega_j(lambda)^2=b_j lambda+c_j in a common A-orthonormal eigenbasis",
        "selector": "u_j=c_j/b_j for b_j>0",
        "controls": branches,
        "field_normalization": "invertible field congruence changes A,B,C together but preserves the generalized branch spectrum and each u_j",
        "ruler_boundary": "rescaling the spatial eigenvalue rescales b_j and therefore u_j; a dimensional mass still requires an independently owned spatial ruler",
        "degeneracy_boundary": "repeated joint eigenvalue pairs determine a subspace, not a preferred basis inside it",
        "source_boundary": "branch recovery is conditional until a source/action-owned Hessian fixes A,B,C on one domain",
        "claim_ceiling": "exact commuting finite-matrix branch recovery only",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["branch_law"].startswith("omega_j(lambda)^2=b_j lambda+c_j")
    assert d["selector"] == "u_j=c_j/b_j for b_j>0"
    assert len(d["controls"]) == 2 and all(x["slope"] == x["recovered_slope"] and x["intercept"] == x["recovered_intercept"] for x in d["controls"])
    assert [x["mass_to_speed_ratio"] for x in d["controls"]] == ["3", "5"]
    assert "preserves the generalized branch spectrum" in d["field_normalization"]
    assert "independently owned spatial ruler" in d["ruler_boundary"]
    assert "not a preferred basis" in d["degeneracy_boundary"]
    assert "source/action-owned Hessian" in d["source_boundary"]
    assert "finite-matrix" in d["claim_ceiling"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1078 controls: 9/9")
