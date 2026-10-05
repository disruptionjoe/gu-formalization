#!/usr/bin/env python3
"""Hostile mutations for K1102."""
from copy import deepcopy
from k1102_k1101_four_mode_one_auxiliary_identification import build, validate


def main():
    mutations = [
        ("recovery_identity", "fit numerically"), ("fixture_modes", [0,1,2]),
        ("q0", "0"), ("q1", "0"), ("ratio", "1"), ("recovered", {}),
        ("two_auxiliary_values", []), ("one_auxiliary_alias_values", []),
        ("fourth_mode_residual_original_minus_alias", "0"),
        ("decision", "three modes suffice"), ("scope_boundary", "measured"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError, IndexError): caught += 1
    assert caught == len(mutations)
    print(f"K1102 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
