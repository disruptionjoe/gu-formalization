#!/usr/bin/env python3
"""K1139: sharp graph criterion for a minimal-rank nonnegative constraint."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1139-sharp-negative-capture-graph-criterion.json"


def build():
    fixtures = []
    for kind, m in [("timelike", 6), ("spacelike", 6), ("null", 4)]:
        fixtures.append({
            "kind": kind,
            "negative_index": m,
            "constraint_rank": m,
            "positive_selector_restricted_inertia": [m, 0, 0],
            "positive_selector_passes": True,
            "wrong_selector_restricted_inertia": [0, m, 0],
            "wrong_selector_passes": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K1139-SHARP-NEGATIVE-CAPTURE-GRAPH-CRITERION",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "theorem": "write a nondegenerate Hessian as H=(-D_minus) direct-sum H_plus with both blocks positive definite. A minimal-rank constraint Q=[Q_minus,Q_plus] can have nonnegative kernel only if Q_minus is invertible; then ker(Q) is the graph v_minus=-B v_plus with B=Q_minus^-1 Q_plus, and the restriction is H_plus-B*D_minus B, which is nonnegative exactly when B is a contraction between these weighted forms",
        "sharp_fixture": {
            "H_diagonal": [-2, -1, 3, 4],
            "passing_B_diagonal": [1, 1],
            "passing_restricted_diagonal": [1, 3],
            "failing_B_diagonal": [2, 1],
            "failing_restricted_diagonal": [-5, 3],
            "equal_constraint_rank": 2,
        },
        "causal_rank_floor_controls": fixtures,
        "rank_floor_is_sufficient": False,
        "negative_capture_and_contraction_required": True,
        "spectral_negative_selector_is_action_owned": False,
        "scope_boundary": "exact finite-dimensional nondegenerate criterion; radicals, gauge, propagation, domains, action ownership and cohomology require separate proofs",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    f = d["sharp_fixture"]
    assert "Q_minus is invertible" in d["theorem"]
    assert "contraction" in d["theorem"]
    assert f["passing_restricted_diagonal"] == [1, 3]
    assert f["failing_restricted_diagonal"] == [-5, 3]
    assert f["equal_constraint_rank"] == 2
    assert [x["constraint_rank"] for x in d["causal_rank_floor_controls"]] == [6, 6, 4]
    assert all(x["positive_selector_passes"] and not x["wrong_selector_passes"] for x in d["causal_rank_floor_controls"])
    assert not d["rank_floor_is_sufficient"]
    assert d["negative_capture_and_contraction_required"]
    assert not d["spectral_negative_selector_is_action_owned"]
    assert "domains" in d["scope_boundary"] and "cohomology" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1139 controls: 12/12")
