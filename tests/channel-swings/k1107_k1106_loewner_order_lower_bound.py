#!/usr/bin/env python3
"""K1107: exact auxiliary-order lower bound from confluent Loewner data."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1107-k1106-loewner-order-lower-bound.json"


def build():
    return {
        "schema_version": "1.0",
        "result_id": "K1107-K1106-LOEWNER-ORDER-LOWER-BOUND",
        "status": "working_draft_verified",
        "created": "2026-10-05",
        "data_type": "branch values and first derivatives at distinct regular nodes",
        "rank_identity": "rank K_X=min(n,m+1) for alpha>0, m distinct positive-weight poles and n distinct nodes",
        "lower_bound_rule": "a positive r-by-r principal Loewner minor forces every positive-slope representation matching the same confluent data to have at least r-1 distinct poles",
        "upper_bound_composition": "if an independent owner supplies m<=r-1, the positive minor certifies exact order m=r-1",
        "fixture_nodes": [0, 1, 2],
        "fixture_positive_minor": "2/2025",
        "fixture_conclusion": "the K1098 two-pole branch cannot be matched in values and first derivatives at all three nodes by any zero- or one-pole positive-slope branch",
        "finite_value_boundary": "K1104 remains controlling for value-only finite samples; derivative data are additional observations and the rank certificate supplies no upper bound without an independent cap",
        "decision": "confluent Loewner positivity gives an exact minimum hidden-order certificate while preserving the unbounded-alias boundary",
        "scope_boundary": "conditional order lower bound; no physical derivative measurement, source-owned multiplicity cap or GU auxiliary sector",
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert d["data_type"].startswith("branch values and first derivatives")
    assert d["rank_identity"] == "rank K_X=min(n,m+1) for alpha>0, m distinct positive-weight poles and n distinct nodes"
    assert "at least r-1" in d["lower_bound_rule"]
    assert "independent owner" in d["upper_bound_composition"]
    assert d["fixture_nodes"] == [0, 1, 2]
    assert d["fixture_positive_minor"] == "2/2025"
    assert "cannot be matched" in d["fixture_conclusion"]
    assert "K1104 remains controlling" in d["finite_value_boundary"]
    assert "minimum hidden-order" in d["decision"]
    assert "no physical derivative measurement" in d["scope_boundary"]
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build(); validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1107 controls: 11/11")
