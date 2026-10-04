#!/usr/bin/env python3
"""Hostile mutations for K1021."""
from copy import deepcopy
from k1021_k1020_setting_tv_chsh_certificate import build, validate


def main():
    mutations = [
        ("tv_convention", "TV=sum"), ("minimum_pair_floor", "min pi>=1/4"),
        ("local_ceiling", "b<=3/4"), ("sequential_certificate", "iid only"),
        ("sharp_example.tv", 0), ("sharp_example.local_optimum", 0.75),
        ("enumerated_controls.0.local_optimum", 1), ("enumerated_controls.1.one_minus_min", 0),
        ("memory_scope", "iid devices"), ("unowned_assumptions", []),
        ("ownership.gu_setting_source_constructed", True),
        ("ownership.measurement_independence_proved", True), ("target_claim", "CONFIRMED"),
    ]
    caught = 0
    for path, value in mutations:
        d = deepcopy(build())
        node = d
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(d)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1021 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
