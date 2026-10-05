#!/usr/bin/env python3
"""Hostile mutations for K1161."""
from copy import deepcopy
from k1161_factor_through_prolongation_rank_theorem import build, validate


def main():
    mutations = [
        ("hypotheses", None, []),
        ("prior_specialization", None, "novel mechanism"),
        ("theorem", "factorization", "independent"),
        ("theorem", "rank_ceiling", "rank grows with rows"),
        ("theorem", "scalar_jet_specialization", "new kernel"),
        ("theorem", "zero_symbol_case", "nonzero"),
        ("exact_control", "base_rank", 3),
        ("exact_control", "three_scalar_descendant_rank", 5),
        ("exact_control", "operator_descendant_rank", 4),
        ("decision", None, "derivatives are independent"),
        ("scope_boundary", None, "global domain theorem"),
        ("target_claim", None, "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for section, key, value in mutations:
        d = deepcopy(build())
        if key is None: d[section] = value
        else: d[section][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1161 hostile probes: 12/12")


if __name__ == "__main__": main()
