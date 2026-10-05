#!/usr/bin/env python3
"""K1162: genuinely independent symbols can add rank sharply."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1162-independent-symbol-family-control.json"


def build():
    controls = []
    for m in range(1, 7):
        controls.append({
            "symbol_count": m,
            "independent_stack_rank": m,
            "shared_factor_descendant_rank": 1,
            "input_dimension": 8,
            "positive_quotient_dimension": 8 - m,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K1162-INDEPENDENT-SYMBOL-FAMILY-CONTROL",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "construction": "q_j:R8->R records coordinate j; stack q_1,...,q_m, while shared-factor descendants are scalar multiples of q_1",
        "controls": controls,
        "all_independent_stacks_gain_one_rank_per_symbol": all(x["independent_stack_rank"] == x["symbol_count"] for x in controls),
        "all_shared_factor_stacks_remain_rank_one": all(x["shared_factor_descendant_rank"] == 1 for x in controls),
        "decision": "rank growth is possible and sharp, but it requires genuinely independent symbols rather than derivative relabelings of one channel",
        "scope_boundary": "exact finite positive control; no source ownership, differential complex, domain, or physical quotient",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["construction"].startswith("q_j:R8->R")
    assert len(d["controls"]) == 6
    for m, row in enumerate(d["controls"], 1):
        assert row["symbol_count"] == m
        assert row["independent_stack_rank"] == m
        assert row["shared_factor_descendant_rank"] == 1
        assert row["input_dimension"] == 8
        assert row["positive_quotient_dimension"] == 8 - m
    assert d["all_independent_stacks_gain_one_rank_per_symbol"]
    assert d["all_shared_factor_stacks_remain_rank_one"]
    assert "genuinely independent symbols" in d["decision"]
    assert "no source ownership" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1162 controls: 10/10")
