#!/usr/bin/env python3
"""Hostile mutations for K1034."""
from copy import deepcopy
from k1034_k1033_action_generator_compatibility import build, validate


def main():
    mutations = [
        ("closed_flow_theorem.radical_invariance", "optional"),
        ("closed_flow_theorem.pairing_preservation", "K*=K"),
        ("closed_flow_theorem.consequence", "arbitrary flow"),
        ("closed_flow_theorem.local_consequence", "Bell violation"),
        ("exact_control.good_defect", [[1]]),
        ("exact_control.bad_defect", [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ("open_flow_boundary", "closed action supplies dephasing"),
        ("source_scope.SC-ACT-01", "DERIVES quantum generator"),
        ("source_scope.SC-ACT-02", "DERIVES CPTP apparatus"),
        ("claim_ceiling", "GU dynamics derived"),
        ("ownership.gu_generator_selected", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[part]
        node[parts[-1]] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1034 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
