#!/usr/bin/env python3
"""Hostile mutations for K1039."""
from copy import deepcopy
from k1039_k1038_mass_horn_nonselection import build, validate


def main():
    mutations = [
        ("horns.0.mass_squared", 2),
        ("horns.1.zero_mode_frequency", 1),
        ("horns.0.passes", False),
        ("horns.1.structural_rows", []),
        ("common_data", "different quotient"),
        ("separating_observable", "none"),
        ("nonselection_theorem", "mass one selected"),
        ("heldout.status", "scored"),
        ("heldout.frozen_score", True),
        ("ownership_boundary", "source selects mass one"),
        ("claim_ceiling", "global GU theorem"),
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
        if key.isdigit():
            node[int(key)] = value
        else:
            node[key] = value
        try:
            validate(data)
        except AssertionError:
            caught += 1
    assert caught == len(mutations)
    print(f"K1039 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
