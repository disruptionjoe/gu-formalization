#!/usr/bin/env python3
"""Hostile mutations for K1679."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("descent", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1679", "cannot increase" in c.get("stationarization", ""),
        "t^4N^4" in c.get("bound", ""), "t^2N^4" in c.get("bound", ""),
        "alpha_g first" in c.get("parameter_order", ""), "limsup E_N/N^4" in c.get("conclusion", ""),
        d.get("stationary_admissible_trial") is True,
        d.get("profiled_gaussian_leading_rigidity_false") is True,
        d.get("unrestricted_nonnegative_fisher_defect_coercivity_false") is True,
        d.get("true_coefficient_identified") is False, d.get("matching_lower_bound_proved") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1679-stationary-nonorbit-leading-descent.json").read_text())
    mutations = [
        (("claim_id",), "K1678"), (("descent", "stationarization"), "Fisher increases"),
        (("descent", "bound"), "O(N3)"), (("descent", "parameter_order"), "t depends on N"),
        (("descent", "conclusion"), "no limsup"), (("decision", "stationary_admissible_trial"), False),
        (("decision", "profiled_gaussian_leading_rigidity_false"), False),
        (("decision", "unrestricted_nonnegative_fisher_defect_coercivity_false"), False),
        (("decision", "true_coefficient_identified"), True),
        (("decision", "matching_lower_bound_proved"), True),
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
