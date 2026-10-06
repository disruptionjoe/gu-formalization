#!/usr/bin/env python3
"""Hostile mutations for K1176."""
from copy import deepcopy
from k1176_shared_causal_repair_budget import build, validate


def main():
    mutations = [
        ("inputs", []), ("causal_deficits", {}), ("theorem", "average the strata"),
        ("shared_ceiling_floor", 98372), ("dominating_stratum", "timelike"),
        ("nonnull_slack_at_floor", 0), ("pointwise_boundary", "uniform always"),
        ("decision", "98372 is enough"), ("scope_boundary", "global GU no-go"),
        ("target_claim", "SC-ACT-01"),
    ]
    caught = 0
    for key, value in mutations:
        d = deepcopy(build()); d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 10
    print("K1176 hostile probes: 10/10")


if __name__ == "__main__": main()
