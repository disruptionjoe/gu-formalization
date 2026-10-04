#!/usr/bin/env python3
"""Hostile mutations for K1028."""
from copy import deepcopy
from k1028_k1027_locality_compromise_fraction_boundary import build, validate


def main():
    mutations = [
        ("good_trial_ceiling", "unbounded"),
        ("compromised_trial_ceiling", "<=b_i"),
        ("fraction_bound", "average q"),
        ("aggregate_ceiling", "b+q"),
        ("sharpness", "not sharp"),
        ("finite_count_form", "b+C/n"),
        ("controls.0.ceiling", 1),
        ("controls.1.ceiling", 0.85),
        ("controls.2.ceiling", 0.9),
        ("controls.3.ceiling", 0.75),
        ("scope", "physical locality proved"),
        ("ownership.compromise_fraction_audited", True),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1028 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
