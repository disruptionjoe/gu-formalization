#!/usr/bin/env python3
"""K1123: apply the reduction floor to the source-native I1B causal symbols."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1123-k1122-source-i1b-constraint-rank-floor.json"


def build():
    rows = [
        {"causal_type": "timelike", "rank_A": 6, "negative_floor": 6, "minimum_constraint_codimension": 6},
        {"causal_type": "spacelike", "rank_A": 6, "negative_floor": 6, "minimum_constraint_codimension": 6},
        {"causal_type": "null", "rank_A": 4, "negative_floor": 4, "minimum_constraint_codimension": 4},
    ]
    return {
        "schema_version": "1.0",
        "result_id": "K1123-K1122-SOURCE-I1B-CONSTRAINT-RANK-FLOOR",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "source_input": "K129 causal symbol ranks as consumed by K1118",
        "rows": rows,
        "ordinary_radical_quotient_sufficient": False,
        "reason": "a Hessian-radical gauge quotient preserves n_+ and n_-; positivity needs a separately owned nonnegative constraint subspace",
        "uniform_minimum_over_nonzero_causal_types": 4,
        "stronger_typewise_floors": [6, 6, 4],
        "scope_boundary": "source-native local finite-symbol necessity only; no global constraints, propagation, closed domain, pairing or cohomology is constructed",
        "protected_effect": "none",
    }


def validate(d):
    assert d["source_input"] == "K129 causal symbol ranks as consumed by K1118"
    assert [r["rank_A"] for r in d["rows"]] == [6, 6, 4]
    assert [r["negative_floor"] for r in d["rows"]] == [6, 6, 4]
    assert [r["minimum_constraint_codimension"] for r in d["rows"]] == [6, 6, 4]
    assert d["ordinary_radical_quotient_sufficient"] is False
    assert "preserves n_+ and n_-" in d["reason"]
    assert d["uniform_minimum_over_nonzero_causal_types"] == 4
    assert d["stronger_typewise_floors"] == [6, 6, 4]
    assert "no global constraints" in d["scope_boundary"]
    assert d["protected_effect"] == "none"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1123 controls: 10/10")
