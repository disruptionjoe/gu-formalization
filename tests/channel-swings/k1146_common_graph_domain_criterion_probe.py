#!/usr/bin/env python3
"""Hostile mutations for K1146."""
from copy import deepcopy
from k1146_common_graph_domain_criterion import build, validate


def main():
    mutations = [
        ("theorem", "an algebraic identity automatically supplies a common domain"),
        ("source_action_domain_supplied", True),
        ("target_claim", "COMMON-DOMAIN-PROVED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    model = [
        ("hilbert_space", "finite"), ("common_graph_weight", "1+n^2"),
        ("product_graph_weight", "n^4"), ("closed_common_domain", False),
    ]
    for key, value in model:
        d = deepcopy(build()); d["multiplier_model"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    counter = [
        ("sequence", "u_n=n^-4"), ("G_graph_series_exponent", 0),
        ("QG_graph_series_exponent", -2),
    ]
    for key, value in counter:
        d = deepcopy(build()); d["composition_counterexample"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1146 hostile probes: 10/10")


if __name__ == "__main__": main()
