#!/usr/bin/env python3
"""Hostile mutations for K1668."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("sign_classification", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1668",
        "includes t=0" in claim.get("nonnegative_profile_coercivity", ""),
        "rho_-^2 q_N=Theta(N^3)" in claim.get("anchor_mass", ""),
        "O(N^3)" in claim.get("posterior_remainder", ""),
        "N^4" in claim.get("posterior_remainder", ""),
        "anchor-free" in claim.get("scope_guard", ""),
        decision.get("positive_leading_gap_proved") is True,
        decision.get("anchor_free_sector_classified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1668-anchor-profile-positive-gap.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1664"),
        (("sign_classification", "nonnegative_profile_coercivity"), "positive weights only"),
        (("sign_classification", "anchor_mass"), "one mode"),
        (("sign_classification", "posterior_remainder"), "O(N^4) missing term"),
        (("sign_classification", "posterior_remainder"), "no leading gap"),
        (("sign_classification", "scope_guard"), "unrestricted theorem"),
        (("decision", "positive_leading_gap_proved"), False),
        (("decision", "anchor_free_sector_classified"), True),
        (("decision", "protected_status_change"), True),
        (("sign_classification", "anchor_mass"), "unknown profile estimate"),
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
