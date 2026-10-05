#!/usr/bin/env python3
"""K1161: fixed-symbol descendants of one constraint cannot gain rank."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1161-factor-through-prolongation-rank-theorem.json"


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def build():
    q = [[1, 0, 1, 0, 0], [0, 1, 0, 1, 0]]
    scalar_descendants = q + [[2 * x for x in row] for row in q] + [[-3 * x for x in row] for row in q]
    operator_descendants = [q[0], q[1], [q[0][i] + q[1][i] for i in range(5)], [2 * q[0][i] - q[1][i] for i in range(5)]]
    return {
        "schema_version": "1.0",
        "result_id": "K1161-FACTOR-THROUGH-PROLONGATION-RANK-THEOREM",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "hypotheses": ["q:V->W linear", "Q_j=A_j q at one fixed covector", "Q=(Q_1,...,Q_m)"],
        "prior_specialization": "K792 proves the released Xi=D_omega Upsilon row factors through the direct Upsilon response on one flat zero-locus germ; K880 proves its induced old-quotient map is zero. K1161 generalizes that held mechanism to arbitrary finite factor-through stacks and does not claim rediscovery.",
        "theorem": {
            "factorization": "Q=S q with S(w)=(A_1w,...,A_mw)",
            "rank_ceiling": "rank(Q restricted to K)<=rank(q restricted to K)<=dim(W) for every K subset V",
            "scalar_jet_specialization": "sigma(D_j q)(xi)=p_j(xi) sigma(q)(xi), so any finite derivative stack has the same kernel as q when some p_j(xi) is nonzero",
            "zero_symbol_case": "if every p_j(xi)=0, the stacked rank is zero",
        },
        "exact_control": {
            "base_rank": rank(q),
            "three_scalar_descendant_rank": rank(scalar_descendants),
            "operator_descendant_rank": rank(operator_descendants),
            "input_dimension": 5,
            "target_dimension": 2,
        },
        "decision": "derivative order, jet count, and postprocessor target size do not create independent fixed-symbol information when every row factors through one finite constraint symbol",
        "scope_boundary": "finite-dimensional fixed-covector theorem only; variable coefficients, lower-order terms, boundary traces, domains, and genuinely independent principal symbols require separate analysis",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert len(d["hypotheses"]) == 3
    assert "K792 proves" in d["prior_specialization"] and "does not claim rediscovery" in d["prior_specialization"]
    assert d["theorem"]["factorization"].startswith("Q=S q")
    assert "<=rank(q restricted to K)<=dim(W)" in d["theorem"]["rank_ceiling"]
    assert "same kernel" in d["theorem"]["scalar_jet_specialization"]
    assert d["theorem"]["zero_symbol_case"] == "if every p_j(xi)=0, the stacked rank is zero"
    c = d["exact_control"]
    assert c["base_rank"] == c["three_scalar_descendant_rank"] == c["operator_descendant_rank"] == 2
    assert c["input_dimension"] == 5 and c["target_dimension"] == 2
    assert "do not create independent" in d["decision"]
    assert "fixed-covector theorem only" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1161 controls: 11/11")
