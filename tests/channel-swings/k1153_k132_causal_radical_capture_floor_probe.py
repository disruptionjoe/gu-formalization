#!/usr/bin/env python3
"""Hostile mutations for K1153."""
from copy import deepcopy
from k1153_k132_causal_radical_capture_floor import build, validate


def main():
    mutations = [
        (None, "source_owner", "auxiliary"),
        ("strata", "timelike", {}),
        ("strata", "spacelike", {}),
        ("strata", "null", {}),
        (None, "causal_rank_floors", {"timelike": 6, "spacelike": 6, "null": 4}),
        (None, "conclusion", "one stratum only"),
        (None, "repair_requirement", "reuse Euler rows"),
        (None, "protected_effect", "SC-ACT-06 killed"),
        (None, "target_claim", "SC-ACT-06-KILL"),
    ]
    caught = 0
    for section, key, value in mutations:
        d = deepcopy(build()); (d if section is None else d[section])[key] = value
        try: validate(d)
        except (AssertionError, KeyError, TypeError): caught += 1
    assert caught == 9
    print("K1153 hostile probes: 9/9")


if __name__ == "__main__": main()
