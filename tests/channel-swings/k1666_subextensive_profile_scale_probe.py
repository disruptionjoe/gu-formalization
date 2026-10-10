#!/usr/bin/env python3
"""Hostile mutations for K1666."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("scale_bound", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1666",
        "0<=rho_(N,k)<=rho_+" in claim.get("profile", ""),
        "-3eta^2 d_N B_N/N^2" in claim.get("defect_floor", ""),
        "B_N=o(N^3)" in claim.get("coefficient_result", ""),
        ">=-o(N^4)" in claim.get("coefficient_result", ""),
        "not a two-sided o(N^4)" in claim.get("scope_guard", ""),
        decision.get("subextensive_l2_descent_excluded") is True,
        decision.get("two_sided_gap_control_proved") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1666-subextensive-profile-scale.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1661"),
        (("scale_bound", "profile"), "signed unbounded weights"),
        (("scale_bound", "defect_floor"), "no l2 bound"),
        (("scale_bound", "coefficient_result"), "B_N=Theta(N^3)"),
        (("scale_bound", "coefficient_result"), "strict negative Theta(N^4) descent"),
        (("scale_bound", "scope_guard"), "two-sided o(N^4) theorem"),
        (("decision", "subextensive_l2_descent_excluded"), False),
        (("decision", "two_sided_gap_control_proved"), True),
        (("decision", "protected_status_change"), True),
        (("scale_bound", "profile"), "unknown non-orbit law"),
    ]
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
