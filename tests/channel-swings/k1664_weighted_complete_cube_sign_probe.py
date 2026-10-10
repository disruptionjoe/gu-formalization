#!/usr/bin/env python3
"""Hostile mutations for K1664."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("sign_classification", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1664",
        "sum_k rho_k^2" in claim.get("shared_scale", ""),
        "3sqrt(3)/64" in claim.get("small_coupling_margin", ""),
        "2(g/2)^(3/2)-3g/512>0" in claim.get("large_coupling_margin", ""),
        "O(N^3)" in claim.get("posterior_remainder", ""),
        "Sparse or degenerating profiles" in claim.get("scope_guard", ""),
        decision.get("positive_leading_gap_proved") is True,
        decision.get("unrestricted_coefficient_identified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1664-weighted-complete-cube-sign.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1659"),
        (("sign_classification", "shared_scale"), "sum rho_k only"),
        (("sign_classification", "small_coupling_margin"), "zero"),
        (("sign_classification", "large_coupling_margin"), "unknown"),
        (("sign_classification", "posterior_remainder"), "O(N^4) missing"),
        (("sign_classification", "scope_guard"), "all profiles covered"),
        (("decision", "positive_leading_gap_proved"), False),
        (("decision", "unrestricted_coefficient_identified"), True),
        (("decision", "protected_status_change"), True),
        (("sign_classification", "scope_guard"), "source-owned physical law"),
    ]
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
