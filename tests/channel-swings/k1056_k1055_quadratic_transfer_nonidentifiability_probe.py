#!/usr/bin/env python3
"""Hostile mutations for K1056."""
from copy import deepcopy
from k1056_k1055_quadratic_transfer_nonidentifiability import build, validate


def main():
    mutations = [
        ("dispersion", "x=mu"), ("transfer_family", "affine only"),
        ("common_readout", "depends on mu"), ("scope", "three modes"),
        ("fixture.modes.0", 99), ("fixture.horns.0", 2.0),
        ("fixture.maximum_residual", 1.0), ("fixture.derivative_floor", 0.0),
        ("consequence", "identified"), ("affine_boundary", "unconditional"),
        ("reopener", "none"), ("target_claim", "CONFIRMED"),
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
    print(f"K1056 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
