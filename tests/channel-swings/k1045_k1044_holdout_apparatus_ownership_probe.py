#!/usr/bin/env python3
"""Hostile mutations for K1045."""
from copy import deepcopy
from k1045_k1044_holdout_apparatus_ownership import build, validate


def main():
    mutations = [
        ("requirements", []),
        ("requirements.1.candidate_grade", "scored"),
        ("requirements.3.candidate_grade", "pass"),
        ("requirements.0.gu_source_owned", True),
        ("requirements.0.scorable", True),
        ("counts.candidate_closed_or_frozen", 8),
        ("holdout_result", "absolute mass selected without scale"),
        ("score_gate", "open"),
        ("credit_boundary", "GU confirmed"),
        ("source_scope.SC-ACT-06", "PROVED"),
        ("ledger_effect", "LT-SM8 SAME"),
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
    print(f"K1045 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
