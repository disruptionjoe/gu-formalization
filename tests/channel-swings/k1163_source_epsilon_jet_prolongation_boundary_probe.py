#!/usr/bin/env python3
"""Hostile mutations for K1163."""
from copy import deepcopy
from k1163_source_epsilon_jet_prolongation_boundary import build, validate


def main():
    mutations = [
        ("inputs", None, []),
        ("tested_class", None, "independent maps"),
        ("m_time", None, 0),
        ("m_null", None, 0),
        ("s_time", None, 0),
        ("s_null", None, 0),
        ("pass", None, True),
        ("ceiling", None, 92),
        ("decision", None, "derivatives close the gap"),
        ("scope_boundary", None, "global no-go"),
        ("target_claim", None, "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for kind, _, value in mutations:
        d = deepcopy(build())
        if kind == "m_time": d["targets"]["full_moment_map_91"]["timelike"]["rank_shortfall"] = value
        elif kind == "m_null": d["targets"]["full_moment_map_91"]["null"]["rank_shortfall"] = value
        elif kind == "s_time": d["targets"]["seven_invariant_lock"]["timelike"]["rank_shortfall"] = value
        elif kind == "s_null": d["targets"]["seven_invariant_lock"]["null"]["rank_shortfall"] = value
        elif kind == "pass": d["targets"]["full_moment_map_91"]["spacelike"]["any_finite_derivative_stack_passes"] = value
        elif kind == "ceiling": d["targets"]["full_moment_map_91"]["spacelike"]["shared_factor_rank_ceiling"] = value
        else: d[kind] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1163 hostile probes: 11/11")


if __name__ == "__main__": main()
