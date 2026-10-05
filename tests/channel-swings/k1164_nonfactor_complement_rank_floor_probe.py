#!/usr/bin/env python3
"""Hostile mutations for K1164."""
from copy import deepcopy
from k1164_nonfactor_complement_rank_floor import build, validate


def main():
    mutations = [
        ("exact_rank_split", "rank adds automatically"),
        ("necessary_increment", "no lower bound"),
        ("factor_through_corollary", "factor descendants add rank"),
        ("m_time", 0),
        ("m_null", 0),
        ("s_time", 0),
        ("s_null", 0),
        ("decision", "restacking suffices"),
        ("necessity_not_sufficiency", "proves positivity"),
        ("target_claim", "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for kind, value in mutations:
        d = deepcopy(build())
        if kind in d["theorem"]: d["theorem"][kind] = value
        elif kind == "m_time": d["full_moment_map_91"]["timelike"]["minimum_complement_rank_on_base_kernel"] = value
        elif kind == "m_null": d["full_moment_map_91"]["null"]["minimum_complement_rank_on_base_kernel"] = value
        elif kind == "s_time": d["seven_invariant_lock"]["timelike"]["minimum_complement_rank_on_base_kernel"] = value
        elif kind == "s_null": d["seven_invariant_lock"]["null"]["minimum_complement_rank_on_base_kernel"] = value
        else: d[kind] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1164 hostile probes: 10/10")


if __name__ == "__main__": main()
