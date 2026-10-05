#!/usr/bin/env python3
"""Hostile mutations for K1139."""
from copy import deepcopy
from k1139_sharp_negative_capture_graph_criterion import build, validate


def main():
    mutations = [
        ("theorem", "rank alone is sufficient"),
        ("causal_rank_floor_controls", []),
        ("rank_floor_is_sufficient", True),
        ("negative_capture_and_contraction_required", False),
        ("spectral_negative_selector_is_action_owned", True),
        ("scope_boundary", "physical quotient complete"),
        ("target_claim", "GU-CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    for key, value in [("passing_restricted_diagonal", [-1, 3]), ("failing_restricted_diagonal", [1, 3]), ("equal_constraint_rank", 1)]:
        d = deepcopy(build()); d["sharp_fixture"][key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations) + 3
    print(f"K1139 hostile probes: {caught}/{len(mutations)+3}")


if __name__ == "__main__": main()
