#!/usr/bin/env python3
"""Hostile mutations for K1115."""
from copy import deepcopy
from k1115_k1114_loewner_reconstruction_boundary import build, validate


def main():
    mutations = [
        ("requirements", []), ("counts", {}), ("advance", "no inverse"),
        ("nonselection", "selects GU"), ("source_scope", {}),
        ("ledger_effect", "rows pass"), ("next_condition", "continue conditional refinements"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1115 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
