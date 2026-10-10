#!/usr/bin/env python3
"""Hostile mutations for K1684."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("upper_coefficient", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1684", "j_R(t)" in c.get("scalar_input", ""),
        "inf_(C,t)" in c.get("functional", ""), "-2g t^2 ell_g(C)" in c.get("functional", ""),
        "limsup_N" in c.get("finite_cutoff_recovery", ""), "h_g^card-up<h_g^prof" in c.get("strictness", ""),
        "not the true unrestricted coefficient" in c.get("scope_guard", ""),
        d.get("opaque_c_g_replaced_by_explicit_upper_functional") is True,
        d.get("strict_improvement_over_profiled_gaussian") is True,
        d.get("true_unrestricted_coefficient_identified") is False,
        d.get("matching_lower_bound_proved") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1684-localized-cardinal-upper-coefficient.json").read_text())
    mutations = [
        (("claim_id",), "K1683"), (("upper_coefficient", "scalar_input"), "unknown"),
        (("upper_coefficient", "functional"), "no infimum"),
        (("upper_coefficient", "finite_cutoff_recovery"), "pointwise equality"),
        (("upper_coefficient", "strictness"), "equal profile"),
        (("upper_coefficient", "scope_guard"), "the true unrestricted coefficient"),
        (("decision", "opaque_c_g_replaced_by_explicit_upper_functional"), False),
        (("decision", "strict_improvement_over_profiled_gaussian"), False),
        (("decision", "true_unrestricted_coefficient_identified"), True),
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
