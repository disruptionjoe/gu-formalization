#!/usr/bin/env python3
"""Hostile mutations for K1022."""
from copy import deepcopy
from k1022_k1021_setting_min_entropy_boundary import build, validate


def main():
    muts = [("assumption", "marginal entropy"), ("minimum_pair_floor", "min pi>=2^-h"),
            ("local_ceiling", "b<=3/4"), ("critical_entropy", "all positive h suffice"),
            ("extremal_family.0.local_ceiling", .75), ("extremal_family.2.pi", [.25]*4),
            ("extremal_family.3.local_ceiling", 1), ("interpretation", "entropy proves freshness"),
            ("unowned_assumptions", []), ("ownership.gu_randomness_source_constructed", True),
            ("ownership.entropy_certified", True), ("target_claim", "CONFIRMED")]
    caught = 0
    for path, value in muts:
        d = deepcopy(build()); node = d; parts = path.split(".")
        for p in parts[:-1]: node = node[int(p)] if p.isdigit() else node[p]
        p = parts[-1]
        if p.isdigit(): node[int(p)] = value
        else: node[p] = value
        try: validate(d)
        except AssertionError: caught += 1
    assert caught == len(muts)
    print(f"K1022 hostile probes: {caught}/{len(muts)}")


if __name__ == "__main__": main()
