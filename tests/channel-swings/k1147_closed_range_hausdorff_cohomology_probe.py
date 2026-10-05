#!/usr/bin/env python3
"""Hostile mutations for K1147."""
from copy import deepcopy
from k1147_closed_range_hausdorff_cohomology import build, validate


def main():
    caught = 0
    direct = [
        ("theorem", "algebraic cohomology is automatically Hilbert"),
        ("source_gauge_range_supplied", True),
        ("target_claim", "PHYSICAL-COHOMOLOGY-PROVED"),
    ]
    for key, value in direct:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    failure = [
        ("d_symbol", "1"), ("singular_value_infimum", "1"),
        ("range_dense", False), ("range_closed", True),
        ("limit_vector_in_ell2", False), ("formal_preimage_in_ell2", True),
        ("algebraic_quotient_hausdorff", True),
    ]
    for key, value in failure:
        d = deepcopy(build()); d["failure_fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1147 hostile probes: 10/10")


if __name__ == "__main__": main()
