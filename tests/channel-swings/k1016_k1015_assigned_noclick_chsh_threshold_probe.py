#!/usr/bin/env python3
"""Hostile mutations for K1016."""
from copy import deepcopy
from k1016_k1015_assigned_noclick_chsh_threshold import build, validate


def main():
    mutations = [
        ("model", "postselected model"), ("correlator_map", "E'=eta E"),
        ("observed_chsh", "S=2sqrt2 eta"), ("violation_iff", "eta>2/3"),
        ("threshold", 2/3), ("controls.at_zero", 0), ("controls.at_threshold", 2.1),
        ("controls.at_one", 2), ("disposition", "discard no-clicks"),
        ("claim_ceiling", "optimal universal detector threshold"),
        ("ownership.gu_detector_model_constructed", True),
        ("ownership.loophole_free_experiment_claimed", True), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        d = deepcopy(build()); node = d; parts = path.split(".")
        for part in parts[:-1]: node = node[part]
        node[parts[-1]] = value
        try: validate(d)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1016 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
