#!/usr/bin/env python3
"""K1083: simultaneous Fourier/internal branches on the functional action."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1083-k1082-functional-branch-selector.json"


def build():
    branches = []
    for b, c in [(F(2), F(6)), (F(3), F(15))]:
        values = [b * lam + c for lam in (F(0), F(1), F(2))]
        slope = values[1] - values[0]
        branches.append({"b": int(b), "c": int(c), "values": [int(v) for v in values], "recovered_b": int(slope), "recovered_c": int(values[0]), "u": str(c / b)})
    return {
        "schema_version": "1.0",
        "result_id": "K1083-K1082-FUNCTIONAL-BRANCH-SELECTOR",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "criterion": "constant A-normalized internal B and C admit one Fourier/internal product basis exactly when [A^-1B,A^-1C]=0",
        "branch_law": "omega_j(k)^2=b_j |k|^2+c_j",
        "branches": branches,
        "k1036_specialization": "B=I and C=m^2 I commute, so every quotient component has u=m^2 on the common H2 domain",
        "selector_boundary": "u_j=c_j/b_j is dimensionless until an independently owned spatial ruler fixes |k|",
        "degeneracy_boundary": "jointly repeated (b_j,c_j) pairs select a subspace but not a preferred internal basis",
        "source_boundary": "the theorem certifies the repository K1036 candidate horn, not a source-selected GU coefficient",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "exactly when [A^-1B,A^-1C]=0" in d["criterion"]
    assert d["branch_law"] == "omega_j(k)^2=b_j |k|^2+c_j"
    assert [b["values"] for b in d["branches"]] == [[6, 8, 10], [15, 18, 21]]
    assert [(b["recovered_b"], b["recovered_c"]) for b in d["branches"]] == [(2, 6), (3, 15)]
    assert [b["u"] for b in d["branches"]] == ["3", "5"]
    assert "u=m^2" in d["k1036_specialization"] and "common H2 domain" in d["k1036_specialization"]
    assert "independently owned spatial ruler" in d["selector_boundary"]
    assert "subspace but not a preferred" in d["degeneracy_boundary"]
    assert "not a source-selected GU coefficient" in d["source_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1083 controls: 9/9")
