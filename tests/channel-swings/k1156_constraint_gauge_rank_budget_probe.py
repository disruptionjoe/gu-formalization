#!/usr/bin/env python3
"""Hostile mutations for K1156."""
from copy import deepcopy
from k1156_constraint_gauge_rank_budget import build, validate


def main():
    mutations = [
        ("hypotheses", None, []),
        ("theorem", "exact_kernel_rank", "rank=0"),
        ("theorem", "codomain_ceiling", "rank unlimited"),
        ("theorem", "budget", "rank(d)>=dim ker(H)"),
        ("theorem", "multi_constraint_budget", "none"),
        ("interpretation", None, "sufficient resources"),
        ("scope_boundary", None, "dimension proves rank"),
        ("target_claim", None, "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for section, key, value in mutations:
        d = deepcopy(build())
        if section == "hypotheses": d[section] = value
        elif section == "theorem": d[section][key] = value
        else: d[section] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 8
    print("K1156 hostile probes: 8/8")


if __name__ == "__main__": main()
