#!/usr/bin/env python3
"""Hostile mutations for K1673."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("rigidity", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1673",
        "N B_N" in claim.get("coercive_margin", ""),
        ">=-CN log N" in claim.get("full_gap", ""),
        "nonnegative" in claim.get("coefficient", ""),
        "need not have a proved positive gap" in claim.get("scope_guard", ""),
        decision.get("all_bounded_known_profiles_coefficient_rigid") is True,
        decision.get("extensive_anchor_free_sector_closed") is True,
        decision.get("uniform_positive_gap_for_tiny_profiles") is False,
        decision.get("unrestricted_coercivity_proved") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1673-known-profile-coefficient-rigidity.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1672"),
        (("rigidity", "coercive_margin"), "no B_N control"),
        (("rigidity", "full_gap"), "uncontrolled"),
        (("rigidity", "coefficient"), "negative coefficient"),
        (("rigidity", "scope_guard"), "positive gap for every profile"),
        (("decision", "all_bounded_known_profiles_coefficient_rigid"), False),
        (("decision", "extensive_anchor_free_sector_closed"), False),
        (("decision", "uniform_positive_gap_for_tiny_profiles"), True),
        (("decision", "unrestricted_coercivity_proved"), True),
        (("decision", "protected_status_change"), True),
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
