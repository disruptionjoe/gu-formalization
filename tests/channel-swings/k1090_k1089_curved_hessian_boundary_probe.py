#!/usr/bin/env python3
"""Hostile mutations for K1090."""
from copy import deepcopy
from k1090_k1089_curved_hessian_boundary import build, validate


def main():
    mutations = [
        ("advance", "flat only"), ("requirements", []),
        ("counts", {"gu_source_owned": 4}), ("nonselection", "selects a GU action"),
        ("source_scope", {"SC-ACT-06": "CONFIRMED", "SC-META-53": "RESOLVED"}),
        ("ledger_effect", "LT-SM8 passes"), ("next_condition", "score now"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1090 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
