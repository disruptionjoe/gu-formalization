#!/usr/bin/env python3
"""Hostile mutations for K1151."""
from copy import deepcopy
from k1151_euler_factor_radical_inheritance import build, validate


def main():
    mutations = [
        ("theorem", "constraint_class", "Q arbitrary"),
        ("theorem", "kernel_inclusion", "false"),
        ("theorem", "radical_inclusion", "false"),
        ("theorem", "positive_quotient_necessary_condition", "none"),
        ("exact_control", "Q", []),
        ("exact_control", "all_radical_pairings", [1]),
        ("exact_control", "dim_ker_H", 1),
        ("exact_control", "rank_d_control", 2),
        ("exact_control", "nongauge_radical_dimension", 0),
        (None, "source_scope", "all constraints rejected"),
        (None, "target_claim", "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for section, key, value in mutations:
        d = deepcopy(build())
        (d if section is None else d[section])[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1151 hostile probes: 11/11")


if __name__ == "__main__": main()
