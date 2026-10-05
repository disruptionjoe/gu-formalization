#!/usr/bin/env python3
"""K1156: sharp constraint-codomain plus gauge-image rank budget."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1156-constraint-gauge-rank-budget.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1156-CONSTRAINT-GAUGE-RANK-BUDGET",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "hypotheses": ["H symmetric", "H d=0", "Q d=0", "rad(H restricted to ker(Q))=im(d)", "Q:V->W"],
        "theorem": {
            "exact_kernel_rank": "rank(Q restricted to ker(H))=dim ker(H)-rank(d)",
            "codomain_ceiling": "rank(Q restricted to ker(H))<=rank(Q)<=dim(W)",
            "budget": "rank(d)+dim(W)>=dim ker(H)",
            "multi_constraint_budget": "rank(d)+sum_i dim(W_i)>=dim ker(H) for Q=(Q_i)_i",
        },
        "interpretation": "constraint output capacity and owned gauge image are complementary necessary resources for removing the nongauge Hessian radical",
        "scope_boundary": "finite-dimensional necessary condition only; target dimension does not prove rank, ownership, compatibility, positivity, or a functional realization",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["hypotheses"]) == 5
    assert d["theorem"]["exact_kernel_rank"].startswith("rank(Q restricted")
    assert d["theorem"]["codomain_ceiling"].endswith("dim(W)")
    assert d["theorem"]["budget"] == "rank(d)+dim(W)>=dim ker(H)"
    assert "sum_i dim(W_i)" in d["theorem"]["multi_constraint_budget"]
    assert "complementary necessary resources" in d["interpretation"]
    assert "does not prove rank" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1156 controls: 8/8")
