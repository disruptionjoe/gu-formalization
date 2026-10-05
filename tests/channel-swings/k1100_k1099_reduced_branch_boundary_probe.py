#!/usr/bin/env python3
"""Hostile mutations for K1100."""
from copy import deepcopy
from k1100_k1099_reduced_branch_boundary import build, validate


def main():
    mutations = [
        ("advance", "no result"), ("requirements", []), ("counts", {}),
        ("nonselection", "selects GU"), ("source_scope", {"SC-ACT-06":"REFUTED"}),
        ("ledger_effect", "LT-SM8 passes"), ("next_condition", "score now"),
        ("target_claim", "FALSIFIED"),
        ("requirements", [{"candidate_grade":"pass","repository_conditional_owned":True,"gu_source_owned":True,"scorable":True}]*7),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1100 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
