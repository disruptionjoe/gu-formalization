#!/usr/bin/env python3
"""Hostile mutations for K1060."""
from copy import deepcopy
from k1060_k1059_nonlinear_transfer_apparatus_boundary import build, validate


def main():
    mutations = [
        ("three_mode_route", "unconditional"), ("four_mode_route", "three modes"),
        ("common_limit", "absolute mass"), ("requirements.0.gu_source_owned", True),
        ("requirements.1.scorable", True), ("score_gate", "open"),
        ("source_scope.SC-ACT-01", "CONFIRMED"), ("ledger_effect", "advanced"),
        ("promotion_effect", "prediction"), ("next_gate", "none"),
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
    print(f"K1060 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
