#!/usr/bin/env python3
"""Hostile mutations for K1040."""
from copy import deepcopy
from k1040_k1039_action_apparatus_ownership_matrix import build, validate


def main():
    mutations = [
        ("requirements", []),
        ("requirements.0.evidence", "none"),
        ("requirements.3.candidate_grade", "pass"),
        ("requirements.0.gu_source_owned", True),
        ("requirements.0.scorable", True),
        ("counts.candidate_pass_or_algebraic", 8),
        ("candidate_result", "GU physical theory complete"),
        ("selection_result", "mass one selected"),
        ("score_gate", "open"),
        ("source_scope.SC-ACT-01", "PROVED"),
        ("source_scope.SC-META-53", "RESOLVED"),
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
    print(f"K1040 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
