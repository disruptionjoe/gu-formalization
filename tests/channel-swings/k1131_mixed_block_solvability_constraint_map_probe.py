#!/usr/bin/env python3
"""Hostile mutations for K1131."""
from copy import deepcopy
from k1131_mixed_block_solvability_constraint_map import build, validate


def main():
    mutations = []
    for key, value in [
        ("constraint_map", "Q=A"),
        ("solvability_criterion", "always solvable"),
        ("constraint_rank_bound", "rank(Q)>rank(A)"),
        ("invertible_case", "invertible C supplies constraints"),
    ]:
        d = build(); d["theorem"][key] = value; mutations.append(d)
    for i, value in enumerate([1, 1, 0]):
        d = build(); d["fixtures"][i]["constraint_rank"] = value; mutations.append(d)
    d = build(); d["fixtures"] = []; mutations.append(d)
    d = build(); d["scope_boundary"] = "physical positivity proved"; mutations.append(d)
    d = build(); d["target_claim"] = "GU-CONFIRMED"; mutations.append(d)
    caught = 0
    for d in mutations:
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1131 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
