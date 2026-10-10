#!/usr/bin/env python3
"""Hostile mutations for K1663."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("fisher_coercivity", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1663",
        "eta rho_(N,k)r_(N,k)" in claim.get("variables", ""),
        "C_(F,N)=(N/2)sum_k" in claim.get("exact_term", ""),
        "t/(1-t)>=4t^2" in claim.get("l2_floor", ""),
        "sum_k rho_(N,k)^2" in claim.get("l2_floor", ""),
        "component Fisher term" in claim.get("scope_guard", ""),
        decision.get("l2_profile_floor_proved") is True,
        decision.get("unrestricted_output_fisher_bound_proved") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1663-l2-profile-fisher-coercivity.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1658"),
        (("fisher_coercivity", "variables"), "t=eta r"),
        (("fisher_coercivity", "exact_term"), "linearized formula"),
        (("fisher_coercivity", "l2_floor"), "t/(1-t)>=t"),
        (("fisher_coercivity", "l2_floor"), "sum rho_k"),
        (("fisher_coercivity", "scope_guard"), "unrestricted output Fisher"),
        (("decision", "l2_profile_floor_proved"), False),
        (("decision", "unrestricted_output_fisher_bound_proved"), True),
        (("decision", "protected_status_change"), True),
        (("fisher_coercivity", "variables"), "allow t>=1"),
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
