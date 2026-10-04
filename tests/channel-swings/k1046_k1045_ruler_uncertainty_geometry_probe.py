#!/usr/bin/env python3
"""Hostile mutations for K1046."""
from copy import deepcopy
from k1046_k1045_ruler_uncertainty_geometry import build, validate


def main():
    mutations = [
        ("model", "Q=m"), ("monotonicity", "constant"),
        ("intervals.mass1.0", "0"), ("intervals.mass4.1", "0"),
        ("gap", "1"), ("theorem", "always separated"),
        ("fixture.delta", "3/4"), ("fixture.mass1_interval.0", "0"),
        ("fixture.mass4_interval.1", "0"), ("fixture.gap", "0"),
        ("scope", "ruler calibrated"), ("target_claim", "CONFIRMED"),
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
    print(f"K1046 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
