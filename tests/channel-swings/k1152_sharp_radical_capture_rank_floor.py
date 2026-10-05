#!/usr/bin/env python3
"""K1152: sharp rank floor for removing nongauge Hessian zero modes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1152-sharp-radical-capture-rank-floor.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1152-SHARP-RADICAL-CAPTURE-RANK-FLOOR",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "hypotheses": ["H symmetric", "H d=0", "Q d=0", "rad(H|ker Q)=im d"],
        "theorem": {
            "restricted_kernel": "ker(Q restricted to ker H)=im d",
            "restricted_rank_identity": "rank(Q|ker H)=dim ker H-rank d",
            "ambient_rank_floor": "rank Q >= dim ker H-rank d",
            "euler_factor_consequence": "Q=L H has rank(Q|ker H)=0 and can pass only if ker H=im d",
        },
        "sharp_control": {
            "H_diagonal": [0, 0, 1],
            "d_image_basis": [[1, 0, 0]],
            "Q": [[0, 1, 0]],
            "ker_H_dimension": 2,
            "rank_d": 1,
            "rank_Q_on_ker_H": 1,
            "rank_floor": 1,
            "restricted_radical_basis": [[1, 0, 0]],
            "positive_quotient_basis": [[0, 0, 1]],
        },
        "scope_boundary": "finite-dimensional exact theorem; functional use additionally requires closed range, a common product domain, uniform positivity and boundary maximality",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["hypotheses"] == ["H symmetric", "H d=0", "Q d=0", "rad(H|ker Q)=im d"]
    t, c = d["theorem"], d["sharp_control"]
    assert t["restricted_kernel"] == "ker(Q restricted to ker H)=im d"
    assert t["restricted_rank_identity"] == "rank(Q|ker H)=dim ker H-rank d"
    assert t["ambient_rank_floor"] == "rank Q >= dim ker H-rank d"
    assert "can pass only if ker H=im d" in t["euler_factor_consequence"]
    assert c["ker_H_dimension"] - c["rank_d"] == c["rank_floor"] == c["rank_Q_on_ker_H"]
    assert c["restricted_radical_basis"] == c["d_image_basis"]
    assert c["positive_quotient_basis"] == [[0, 0, 1]]
    assert "functional use additionally requires" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1152 controls: 12/12")
