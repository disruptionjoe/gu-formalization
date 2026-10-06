#!/usr/bin/env python3
"""Hostile mutations for K1173."""
from copy import deepcopy
from k1173_k132_causal_repair_polytope import build, validate


def main():
    mutations = [
        ("inputs", None, []), ("favorable_baseline", None, "source-owned rank 98"),
        ("timelike", "best_case_repair_deficit", 98371), ("null", "best_case_repair_deficit", 106535),
        ("timelike", "constraint_only_total_rank_floor", 98469), ("null", "constraint_only_total_rank_floor", 106633),
        ("timelike", "gauge_only_total_rank_floor", 98375), ("null", "gauge_only_total_rank_floor", 106539),
        ("spacelike", "changed_parent_hessian_rank_floor", 229283), ("tradeoff", None, "one resource is free"),
        ("necessity_not_sufficiency", None, "physical quotient complete"), ("protected_disposition", None, "SC-ACT-06 refuted"),
    ]
    caught = 0
    for a, b, v in mutations:
        d = deepcopy(build())
        if a in d["causal"]: d["causal"][a][b] = v
        else: d[a] = v
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1173 hostile probes: 12/12")


if __name__ == "__main__": main()
