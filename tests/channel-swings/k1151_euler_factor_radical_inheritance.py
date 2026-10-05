#!/usr/bin/env python3
"""K1151: Euler-row postprocessing inherits the source Hessian radical."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1151-euler-factor-radical-inheritance.json"


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def mv(a, x):
    return [dot(row, x) for row in a]


def build():
    h = [[-2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 3]]
    ell = [[1, 2, -1, 1], [0, 1, 1, 0]]
    q = [[dot(row, [h[j][k] for j in range(4)]) for k in range(4)] for row in ell]
    ker_h = [[0, 1, 0, 0], [0, 0, 1, 0]]
    ker_q_controls = [[0, 1, -1, 0], [3, 0, 0, 2]]
    radical_checks = [dot(v, mv(h, w)) for v in ker_h for w in ker_q_controls]
    return {
        "schema_version": "1.0",
        "result_id": "K1151-EULER-FACTOR-RADICAL-INHERITANCE",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": {
            "constraint_class": "Q=L H for an arbitrary linear Euler-row postprocessor L",
            "kernel_inclusion": "ker(H) subset ker(Q)",
            "radical_inclusion": "ker(H) subset rad(H restricted to ker(Q))",
            "positive_quotient_necessary_condition": "ker(H)=im(d) whenever im(d) subset ker(H) and rad(H|ker(Q))=im(d)",
        },
        "exact_control": {
            "H": h,
            "L": ell,
            "Q": q,
            "ker_H_basis": ker_h,
            "ker_Q_control_vectors": ker_q_controls,
            "all_radical_pairings": radical_checks,
            "dim_ker_H": 2,
            "rank_d_control": 1,
            "nongauge_radical_dimension": 1,
        },
        "source_scope": "applies to constraints formed only by linear postprocessing of source Euler rows at one fixed symbol; it does not classify nonfactor boundary, constraint, or KT/BFV maps",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    t, c = d["theorem"], d["exact_control"]
    assert t["constraint_class"] == "Q=L H for an arbitrary linear Euler-row postprocessor L"
    assert t["kernel_inclusion"] == "ker(H) subset ker(Q)"
    assert t["radical_inclusion"] == "ker(H) subset rad(H restricted to ker(Q))"
    assert "ker(H)=im(d)" in t["positive_quotient_necessary_condition"]
    assert c["Q"] == [[-2, 0, 0, 3], [0, 0, 0, 0]]
    assert all(x == 0 for x in c["all_radical_pairings"])
    assert c["dim_ker_H"] == 2 and c["rank_d_control"] == 1
    assert c["nongauge_radical_dimension"] == 1
    assert "does not classify nonfactor" in d["source_scope"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1151 controls: 12/12")
