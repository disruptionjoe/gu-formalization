#!/usr/bin/env python3
"""Hostile mutations for K1085."""
from copy import deepcopy
from k1085_k1084_functional_hessian_boundary import build, validate


def main():
    mutations = [
        ("requirements", []), ("requirements.4.candidate_grade", "pass"),
        ("requirements.0.repository_action_owned", False), ("requirements.0.gu_source_owned", True),
        ("counts.repository_action_owned", 5), ("advance", "finite matrices only"),
        ("nonselection", "selects GU"), ("source_scope.SC-META-53", "RESOLVED"),
        ("ledger_effect", "LT-SM8 SAME"), ("next_condition", "score now"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        try:
            for part in parts[:-1]: node = node[int(part)] if part.isdigit() else node[part]
            node[parts[-1]] = value
            validate(data)
        except (AssertionError, KeyError): caught += 1
    assert caught == len(mutations)
    print(f"K1085 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
