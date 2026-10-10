#!/usr/bin/env python3
"""Hostile mutations for K1659."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("sign_classification", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1659",
        "-3g eta^2 c_N^2" in q.get("negative_floor", ""),
        "3sqrt(3)/64" in q.get("small_coupling_margin", ""),
        "(g/2)^(3/2)" in q.get("large_coupling_margin", ""),
        "O_(g,eta,R)(N^3)" in q.get("posterior_remainder", ""),
        "unrestricted anisotropic laws remain open" in q.get("scope_guard", ""),
        z.get("all_fixed_admissible_amplitudes_classified") is True,
        z.get("positive_leading_gap_proved") is True,
        z.get("unrestricted_coefficient_identified") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1659-all-amplitude-complete-cube-sign.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1654"),
        (("sign_classification", "negative_floor"), "no floor"),
        (("sign_classification", "small_coupling_margin"), "no margin"),
        (("sign_classification", "large_coupling_margin"), "no profile"),
        (("sign_classification", "posterior_remainder"), "O(N^4)"),
        (("sign_classification", "scope_guard"), "unrestricted"),
        (("decision", "all_fixed_admissible_amplitudes_classified"), False),
        (("decision", "positive_leading_gap_proved"), False),
        (("decision", "unrestricted_coefficient_identified"), True),
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
