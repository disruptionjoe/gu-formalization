#!/usr/bin/env python3
"""Hostile mutations for K1055."""
from copy import deepcopy
from k1055_k1054_spectrum_shape_apparatus_boundary import build, validate


def main():
    mutations = [
        ("identification_result", "absolute mass"), ("two_mode_route", "no offset debt"),
        ("three_mode_route", "same route"), ("sharp_targets.relative_gap_percent", "10"),
        ("sharp_targets.gain_normalized_component_percent", "10"),
        ("requirements.0.gu_source_owned", True), ("requirements.1.scorable", True),
        ("score_gate", "open"), ("source_scope.SC-ACT-01", "CONFIRMED"),
        ("ledger_effect", "advanced"), ("promotion_effect", "prediction"),
        ("target_claim", "CONFIRMED"),
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
    print(f"K1055 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
