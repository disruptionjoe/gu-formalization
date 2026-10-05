#!/usr/bin/env python3
"""Hostile mutations for K1144."""
from copy import deepcopy
from k1144_positive_nonzero_two_term_cohomology import build, validate


def main():
    mutations = [
        ("theorem", "nonzero quotient is automatically positive"),
        ("source_bv_bfv_complex_supplied", True),
        ("physical_identification_supplied", True),
        ("target_claim", "PHYSICAL-STATE-PROVED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    fixture_mutations = [
        ("Qd_zero", False), ("kernel_dimension", 2),
        ("restricted_radical_equals_gauge_image", False),
        ("cohomology_dimension", 0), ("cohomology_gram", [[-1]]),
        ("positive_definite", False),
    ]
    for key, value in fixture_mutations:
        d = deepcopy(build()); d["pass_fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    d = deepcopy(build()); d["negative_control"]["positive_definite"] = True
    try: validate(d)
    except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1144 hostile probes: 11/11")


if __name__ == "__main__": main()
