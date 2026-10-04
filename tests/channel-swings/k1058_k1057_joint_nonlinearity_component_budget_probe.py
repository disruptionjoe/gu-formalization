#!/usr/bin/env python3
"""Hostile mutations for K1058."""
from copy import deepcopy
from k1058_k1057_joint_nonlinearity_component_budget import build, validate


def main():
    mutations = [
        ("model", "affine"), ("extrema", "independent gaps"), ("separation", "overlap"),
        ("sharp_budget", "eta<1"), ("affine_form.intercept", "1"),
        ("affine_form.slope", "1"), ("affine_form.zero_at_tau", "1"),
        ("fixtures.0", "-1"), ("limiting_cases", "none"),
        ("scope", "universal"), ("reopener", "none"), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if isinstance(node, list) else node[part]
        if isinstance(node, list): node[int(parts[-1])] = value
        else: node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1058 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
