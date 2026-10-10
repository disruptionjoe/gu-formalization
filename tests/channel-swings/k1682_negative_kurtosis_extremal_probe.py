#!/usr/bin/env python3
"""Hostile mutations for K1682."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("extremal_law", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1682", "kappa_4(X)>=-2" in c.get("moment_floor", ""),
        "X^2=1" in c.get("equality_case", ""), "u^2 tau/24" in c.get("weak_gap", ""),
        "q_*=12g ell/tau" in c.get("effective_coordinate", ""), "u=2" in c.get("rademacher_role", ""),
        "no exact global" in c.get("scope_guard", ""),
        d.get("negative_fourth_cumulant_floor_sharp") is True,
        d.get("rademacher_unique_centered_equality_case") is True,
        d.get("finite_t_global_optimality_proved") is False,
        d.get("unrestricted_field_lower_bound_proved") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1682-negative-kurtosis-extremal.json").read_text())
    mutations = [
        (("claim_id",), "K1681"), (("extremal_law", "moment_floor"), "unbounded below"),
        (("extremal_law", "equality_case"), "Gaussian"), (("extremal_law", "weak_gap"), "linear Fisher"),
        (("extremal_law", "effective_coordinate"), "wrong optimizer"),
        (("extremal_law", "rademacher_role"), "u=3"), (("extremal_law", "scope_guard"), "exact global"),
        (("decision", "negative_fourth_cumulant_floor_sharp"), False),
        (("decision", "rademacher_unique_centered_equality_case"), False),
        (("decision", "finite_t_global_optimality_proved"), True),
        (("decision", "unrestricted_field_lower_bound_proved"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source); cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
