#!/usr/bin/env python3
"""Hostile mutations for K1035."""
from copy import deepcopy
from k1035_k1034_quantum_apparatus_ownership_matrix import build, validate


def main():
    mutations = [
        ("reverse_lineage", []),
        ("stage", "forward_certification"),
        ("requirements", []),
        ("requirements.0.evidence", "none"),
        ("requirements.0.gu_owned", True),
        ("source_scope.SC-ACT-01", "DISAVOWS"),
        ("source_scope.SC-ACT-02", "UNCERTAIN"),
        ("source_scope.SC-ACT-06", "PROVED"),
        ("source_scope.SC-META-53", "RESOLVED"),
        ("score_status", "ready"),
        ("current_result", "GU confirmed"),
        ("ledger_effect", "rows advanced"),
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
    print(f"K1035 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
