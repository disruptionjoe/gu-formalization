#!/usr/bin/env python3
"""Hostile mutations for K1674."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    claim, decision = data.get("ceiling", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1674",
        "sqrt(3)/4" in claim.get("inputs", ""),
        "4(1-epsilon)/(eta sqrt(3))" in claim.get("bound", ""),
        "uniformly in N" in claim.get("bound", ""),
        "vanishing margin" in claim.get("scope_guard", ""),
        decision.get("uniform_profile_ceiling_derived") is True,
        decision.get("separate_ceiling_assumption_required") is False,
        decision.get("vanishing_margin_classified") is False,
        decision.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1674-residual-margin-profile-ceiling.json").read_text())
    assert valid(source)
    mutations = [
        (("claim_id",), "K1673"),
        (("ceiling", "inputs"), "r may vanish"),
        (("ceiling", "bound"), "rho unbounded"),
        (("ceiling", "bound"), "N-dependent ceiling"),
        (("ceiling", "scope_guard"), "all parameter regimes covered"),
        (("decision", "uniform_profile_ceiling_derived"), False),
        (("decision", "separate_ceiling_assumption_required"), True),
        (("decision", "vanishing_margin_classified"), True),
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
