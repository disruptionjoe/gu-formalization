#!/usr/bin/env python3
"""Hostile mutations for K1051."""
from copy import deepcopy
from k1051_k1050_finite_mode_scale_gauge_obstruction import build, validate


def main():
    mutations = [
        ("dispersion", "omega=m"), ("readout", "calibrated"), ("scale_action", "identity"),
        ("invariance", "changes"), ("identified_parameter", "absolute mass"),
        ("mode_scope", "two modes only"), ("fixture.modes.0", 99), ("fixture.scale", 1.0),
        ("fixture.maximum_residual", 1.0), ("consequence", "absolute mass identified"),
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
    print(f"K1051 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
