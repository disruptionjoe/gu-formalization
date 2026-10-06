#!/usr/bin/env python3
"""Hostile mutations for K1179."""
from copy import deepcopy
from k1179_native_stack_complement_boundary import build, validate


def main():
    mutations = [
        ("inputs", []), ("theorem", "ranks add by name"), ("candidate_ceilings", [650]),
        ("optimistic_direct_sum_ceiling", 5000), ("optimistic_residual_deficits", {}),
        ("actual_admission_fields", []), ("current_actual_stack_rank", 4606),
        ("decision", "stack passes"), ("zero_credit_rule", "derivatives always add"),
        ("scope_boundary", "one owned K132 stack"), ("target_claim", "SC-ACT-01"),
        ("candidate_ceilings", [650, 915, 1470, 1572]),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 12
    print("K1179 hostile probes: 12/12")


if __name__ == "__main__": main()
