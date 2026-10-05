#!/usr/bin/env python3
"""Hostile mutations for K1110."""
from copy import deepcopy
from k1110_k1109_loewner_identifiability_boundary import build, validate


def main():
    mutations = [
        ("requirements", []), ("counts", {}), ("advance", "none"),
        ("nonselection", "selects GU Hessian"), ("source_scope", {"SC-ACT-06": "FALSIFIED"}),
        ("ledger_effect", "rows pass"), ("next_condition", "score now"),
        ("target_claim", "FALSIFIED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    data = build(); data["requirements"][0]["gu_source_owned"] = True
    try: validate(data)
    except AssertionError: caught += 1
    data = build(); data["requirements"][0]["scorable"] = True
    try: validate(data)
    except AssertionError: caught += 1
    assert caught == 10
    print("K1110 hostile probes: 10/10")


if __name__ == "__main__": main()
