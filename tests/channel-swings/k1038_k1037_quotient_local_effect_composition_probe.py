#!/usr/bin/env python3
"""Hostile mutations for K1038."""
from copy import deepcopy
from k1038_k1037_quotient_local_effect_composition import build, validate


def main():
    mutations = [
        ("carrier", "ambient mixed-sign carrier"),
        ("state", "unnormalized"),
        ("probabilities", ["1", "1"]),
        ("probability_sum", "2"),
        ("marginal_before", {}),
        ("marginal_after", {}),
        ("instrument", "postselected branch"),
        ("composition_grade", "source-derived"),
        ("open_physical_boundary", "GU apparatus complete"),
        ("ownership.candidate_effect_interface", False),
        ("ownership.source_GU_local_algebra", True),
        ("ownership.scorable_apparatus", True),
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
    print(f"K1038 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
