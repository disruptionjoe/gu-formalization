#!/usr/bin/env python3
"""Hostile mutations for K1148."""
from copy import deepcopy
from k1148_uniform_positive_cohomology_gap import build, validate


def main():
    caught = 0
    direct = [
        ("theorem", "modewise positivity is sufficient"),
        ("source_positive_pairing_supplied", True),
        ("physical_state_identification_supplied", True),
        ("target_claim", "POSITIVE-PHYSICAL-SPACE-PROVED"),
    ]
    for key, value in direct:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    failure = [
        ("quotient_fibre_form", "1"), ("uniform_lower_bound", "1"),
        ("energy", "1"), ("coercive", True),
        ("bounded_inverse_riesz_map", True),
        ("energy_norm_equivalent_to_ambient", True),
    ]
    for key, value in failure:
        d = deepcopy(build()); d["failure_fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1148 hostile probes: 10/10")


if __name__ == "__main__": main()
