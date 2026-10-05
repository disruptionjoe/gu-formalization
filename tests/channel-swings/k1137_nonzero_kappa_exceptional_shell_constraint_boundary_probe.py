#!/usr/bin/env python3
"""Hostile mutations for K1137."""
from copy import deepcopy
from k1137_nonzero_kappa_exceptional_shell_constraint_boundary import build, validate


def main():
    mutations = [
        ("inputs", []),
        ("generic_nonzero_kappa_constraint_rank", 6),
        ("spacelike_exceptional_squared_shell_count", 26),
        ("shell_left_null_compatibility_may_exist", False),
        ("shell_rows_extend_to_nonzero_polynomial_local_constraint", True),
        ("conclusion", "shells are propagated field constraints"),
        ("reopeners", []),
        ("protected_disposition", "SC-ACT-06 killed"),
        ("scope_boundary", "all completions excluded"),
        ("target_claim", "SC-ACT-06-KILLED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1137 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
