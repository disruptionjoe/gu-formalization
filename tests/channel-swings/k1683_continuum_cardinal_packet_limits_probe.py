#!/usr/bin/env python3
"""Hostile mutations for K1683."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("continuum_limits", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1683", "conjugation-symmetric" in c.get("block_class", ""),
        "b_g(xi)=sqrt" in c.get("profile_functions", ""),
        "a_g(xi)=[2b_g(xi)]^(-1/2)" in c.get("profile_functions", ""),
        "T_N/N^4" in c.get("trace_limit", ""), "L_N/N^4" in c.get("fourth_mass_limit", ""),
        "1_C(x+y-z)" in c.get("fourth_mass_limit", ""), "ell=(8/27)A^4 alpha^6" in c.get("constant_cube_control", ""),
        "fixed rectangular C" in c.get("scope_guard", ""), d.get("relative_trace_limit_explicit") is True,
        d.get("physical_multiplier_distinguished") is True, d.get("optimal_packet_shape_identified") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1683-continuum-cardinal-packet-limits.json").read_text())
    mutations = [
        (("claim_id",), "K1682"), (("continuum_limits", "block_class"), "one complex mode"),
        (("continuum_limits", "profile_functions"), "a=b"), (("continuum_limits", "trace_limit"), "N^5"),
        (("continuum_limits", "fourth_mass_limit"), "N^3"),
        (("continuum_limits", "constant_cube_control"), "ell=alpha^3"),
        (("continuum_limits", "scope_guard"), "all moving shapes"),
        (("decision", "relative_trace_limit_explicit"), False),
        (("decision", "physical_multiplier_distinguished"), False),
        (("decision", "optimal_packet_shape_identified"), True),
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
