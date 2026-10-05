#!/usr/bin/env python3
"""Hostile mutations for K1149."""
from copy import deepcopy
from k1149_boundary_skew_adjoint_generator_gate import build, validate


def main():
    caught = 0
    direct = [
        ("differential_expression", "finite skew matrix"),
        ("green_boundary_form", "0"),
        ("theorem", "formal skewness is sufficient"),
        ("source_boundary_domain_supplied", True),
        ("target_claim", "UNITARY-DYNAMICS-PROVED"),
    ]
    for key, value in direct:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    bad = [
        ("maximal", True), ("skew_adjoint", True),
        ("unitary_group_generator", True), ("adjoint_domain", "H1_0(0,1)"),
    ]
    for key, value in bad:
        d = deepcopy(build()); d["dirichlet_realization"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    d = deepcopy(build()); d["periodic_realization"]["skew_adjoint"] = False
    try: validate(d)
    except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1149 hostile probes: 10/10")


if __name__ == "__main__": main()
