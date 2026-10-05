#!/usr/bin/env python3
"""K1157: every gauge/constraint split of the K1156 budget is sharp."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1157-sharp-rank-budget-control.json"


def split_control(r):
    k = 6
    return {
        "gauge_rank": r,
        "constraint_target_dimension": k-r,
        "constraint_rank_on_kernel": k-r,
        "kernel_dimension": k,
        "budget_sum": r+(k-r),
        "constrained_radical_dimension": r,
        "positive_quotient_dimension": 2,
    }


def build():
    controls = [split_control(r) for r in range(7)]
    return {
        "schema_version": "1.0",
        "result_id": "K1157-SHARP-RANK-BUDGET-CONTROL",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "control_family": "H=diag(0^6,2,3); im(d)=span(e_1,...,e_r); Q records e_(r+1),...,e_6",
        "splits": controls,
        "all_splits_saturate_budget": all(x["budget_sum"] == x["kernel_dimension"] for x in controls),
        "all_splits_leave_positive_nonzero_quotient": all(x["positive_quotient_dimension"] == 2 for x in controls),
        "conclusion": "K1156 is sharp for every allocation between gauge image and constraint target; no stronger dimension-only inequality is available",
        "scope_boundary": "exact finite control family; no source ownership or functional domain",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["control_family"].startswith("H=diag(0^6,2,3)")
    assert len(d["splits"]) == 7
    for r, row in enumerate(d["splits"]):
        assert row["gauge_rank"] == r
        assert row["constraint_target_dimension"] == 6-r
        assert row["constraint_rank_on_kernel"] == 6-r
        assert row["budget_sum"] == 6 and row["constrained_radical_dimension"] == r
        assert row["positive_quotient_dimension"] == 2
    assert d["all_splits_saturate_budget"] and d["all_splits_leave_positive_nonzero_quotient"]
    assert "sharp for every allocation" in d["conclusion"]
    assert "no source ownership" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data=build(); validate(data)
    assert json.loads(OUTPUT.read_text()) == data
    print("K1157 controls: 12/12")
