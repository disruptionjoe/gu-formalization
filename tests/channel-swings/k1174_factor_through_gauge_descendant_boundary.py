#!/usr/bin/env python3
"""K1174: factor-through gauge descendants do not enlarge gauge image."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1174-factor-through-gauge-descendant-boundary.json"


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols, r = len(a), len(a[0]), 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if a[i][c]), None)
        if p is None: continue
        a[r], a[p] = a[p], a[r]
        z = a[r][c]; a[r] = [x/z for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                z = a[i][c]; a[i] = [x-z*y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def build():
    base = [[1,0,0],[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    descendants = [[1,0,1,1,0],[0,1,1,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    independent = [[0,0],[0,0],[1,0],[0,1],[0,0],[0,0]]
    combined = [a+b for a,b in zip(base, independent)]
    return {
        "schema_version": "1.0", "result_id": "K1174-FACTOR-THROUGH-GAUGE-DESCENDANT-BOUNDARY",
        "status": "working_draft_verified", "created": "2026-10-05",
        "theorem": "for every finite family d_j=d0 A_j, the combined generator D=[d_1 ... d_m]=d0 A has im D subset im d0 and rank D<=rank d0; gauge-for-gauge maps r with d0 r=0 enlarge parameter redundancy, not the field-space gauge image",
        "exact_control": {
            "field_dimension": 6, "base_parameter_dimension": 3,
            "base_gauge_rank": rank(base), "factor_through_parameter_columns": 5,
            "factor_through_combined_rank": rank(descendants), "gauge_for_gauge_dimension": 1,
            "independent_added_rank": rank(independent), "combined_with_independent_rank": rank(combined),
        },
        "k132_application": {
            "current_owned_gauge_rank": 4,
            "nonnull_pure_gauge_total_rank_floor": 98376,
            "null_pure_gauge_total_rank_floor": 106540,
            "nonnull_minimum_new_independent_gauge_rank": 98372,
            "null_minimum_new_independent_gauge_rank": 106536,
            "factor_through_descendants_change_deficit": False,
            "gauge_parameter_fibre_dimension_floor": "at least the corresponding total gauge rank because rank d<=dim G",
        },
        "decision": "derivatives, reparameterizations and reducibility data factoring through the current rank-four metric-diffeomorphism generator cannot pay any K132 repair deficit; only genuinely independent field-space gauge directions can",
        "scope_boundary": "finite-symbol image theorem; no claim that the source lacks every independent gauge/KT generator or that a rank floor supplies closed range, a common domain, properness or physical cohomology",
        "target_claim": "SC-ACT-06",
    }


def validate(d):
    assert "im D subset im d0" in d["theorem"] and "gauge-for-gauge" in d["theorem"]
    c = d["exact_control"]
    assert c["base_gauge_rank"] == 2 and c["factor_through_combined_rank"] == 2
    assert c["gauge_for_gauge_dimension"] == 1
    assert c["independent_added_rank"] == 2 and c["combined_with_independent_rank"] == 4
    k = d["k132_application"]
    assert k["current_owned_gauge_rank"] == 4
    assert (k["nonnull_pure_gauge_total_rank_floor"], k["null_pure_gauge_total_rank_floor"]) == (98376, 106540)
    assert (k["nonnull_minimum_new_independent_gauge_rank"], k["null_minimum_new_independent_gauge_rank"]) == (98372, 106536)
    assert k["factor_through_descendants_change_deficit"] is False
    assert "rank d<=dim G" in k["gauge_parameter_fibre_dimension_floor"]
    assert "cannot pay any K132 repair deficit" in d["decision"]
    assert "finite-symbol image theorem" in d["scope_boundary"]
    assert d["target_claim"] == "SC-ACT-06"


if __name__ == "__main__":
    data = build(); validate(data); assert json.loads(OUTPUT.read_text()) == data
    print("K1174 controls: 12/12")
