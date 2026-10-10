#!/usr/bin/env python3
"""Hostile mutations for K1658."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("fisher_floor", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1658",
        "d_N/N^3<=1/512" in q.get("shell", ""),
        "t_(N,k)=eta r_(N,k) in (0,1)" in q.get("exact_term", ""),
        "t/(1-t)>=4t^2" in q.get("amplitude_inequality", ""),
        "8sqrt(3)" in q.get("small_coupling", ""),
        "kappa_g>=16sqrt(3)g-3>=g" in q.get("profile_self_consistency", ""),
        "(g/2)^(3/2)" in q.get("large_coupling", ""),
        "not an unrestricted Fisher inequality" in q.get("scope_guard", ""),
        z.get("all_admissible_amplitude_floor_proved") is True,
        z.get("unrestricted_fisher_bound_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1658-profile-fisher-amplitude-floor.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1654"),
        (("fisher_floor", "shell"), "arbitrary shell"),
        (("fisher_floor", "exact_term"), "t unrestricted"),
        (("fisher_floor", "amplitude_inequality"), "linear only"),
        (("fisher_floor", "small_coupling"), "no split"),
        (("fisher_floor", "profile_self_consistency"), "no kappa bound"),
        (("fisher_floor", "large_coupling"), "O(eta)"),
        (("fisher_floor", "scope_guard"), "unrestricted"),
        (("decision", "all_admissible_amplitude_floor_proved"), False),
        (("decision", "unrestricted_fisher_bound_proved"), True),
        (("decision", "protected_status_change"), True),
    ]
    for i, (path, value) in enumerate(changes, 1):
        m = copy.deepcopy(source)
        cur = m
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = value
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")


if __name__ == "__main__":
    main()
