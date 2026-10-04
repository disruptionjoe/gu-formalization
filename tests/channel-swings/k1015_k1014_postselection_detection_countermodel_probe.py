#!/usr/bin/env python3
"""Hostile mutations for K1015."""
from copy import deepcopy
from k1015_k1014_postselection_detection_countermodel import build, validate


def main():
    mutations = [
        ("hidden_variable", "lambda independent but nonlocal"),
        ("local_detection.alice", "D_A=1 iff y=v"),
        ("local_detection.bob", "D_B=1 iff x=u"),
        ("table", []),
        ("table.0.retained", []),
        ("table.1.retained.0.win", False),
        ("single_party_detection_probability", "1"),
        ("joint_detection_probability", "1/2"),
        ("postselected_win_rate", "3/4"),
        ("disposition", "postselection is harmless"),
        ("claim_ceiling", "optimal detector-efficiency threshold proved"),
        ("ownership.gu_detector_model_constructed", True),
        ("ownership.empirical_loophole_closed", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if isinstance(node, list) else node[part]
        last = parts[-1]
        if isinstance(node, list):
            node[int(last)] = value
        else:
            node[last] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1015 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
