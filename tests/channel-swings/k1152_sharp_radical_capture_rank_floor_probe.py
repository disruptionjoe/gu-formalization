#!/usr/bin/env python3
"""Hostile mutations for K1152."""
from copy import deepcopy
from k1152_sharp_radical_capture_rank_floor import build, validate


def main():
    mutations = [
        (None, "hypotheses", []),
        ("theorem", "restricted_kernel", "larger"),
        ("theorem", "restricted_rank_identity", "rank zero"),
        ("theorem", "ambient_rank_floor", "no floor"),
        ("theorem", "euler_factor_consequence", "passes"),
        ("sharp_control", "rank_floor", 0),
        ("sharp_control", "rank_Q_on_ker_H", 0),
        ("sharp_control", "restricted_radical_basis", []),
        ("sharp_control", "positive_quotient_basis", []),
        (None, "scope_boundary", "global theorem"),
        (None, "target_claim", "SC-META-53-SOLVED"),
    ]
    caught = 0
    for section, key, value in mutations:
        d = deepcopy(build()); (d if section is None else d[section])[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1152 hostile probes: 11/11")


if __name__ == "__main__": main()
