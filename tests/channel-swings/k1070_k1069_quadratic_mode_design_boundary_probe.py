#!/usr/bin/env python3
"""Hostile mutations for K1070."""
from copy import deepcopy
from k1070_k1069_quadratic_mode_design_boundary import build, validate


def main():
    mutations = [
        ("candidate_pass_count", 14), ("rows.0.status", "OPEN"),
        ("gu_source_owned_count", 1), ("empirically_scorable_count", 1),
        ("protected_source_status.SC-ACT-06", "CONFIRMED"),
        ("protected_source_status.SC-META-53", "RESOLVED"),
        ("protected_ledger_status.LT-SM8", "SAME"),
        ("next_condition", "score now"), ("scope", "GU confirmed"),
        ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build()); node = data; parts = path.split(".")
        for part in parts[:-1]: node = node[int(part)] if isinstance(node, list) else node[part]
        if isinstance(node, list): node[int(parts[-1])] = value
        else: node[parts[-1]] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1070 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
