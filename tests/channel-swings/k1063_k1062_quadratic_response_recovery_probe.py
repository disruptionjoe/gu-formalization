#!/usr/bin/env python3
"""Hostile mutations for K1063."""
from copy import deepcopy
from k1063_k1062_quadratic_response_recovery import build, validate


def main():
    mutations = [
        ("modes.3", 25), ("mass_one_exact_row.0", "-40/20"),
        ("response_rows.1.0", 0.0), ("response_rows.4.0", 0.0),
        ("component_error_amplification.1", 1.0), ("component_error_amplification.4", 1.0),
        ("recovery_rule", "exact under noise"), ("nonzero_certificate", "automatic"),
        ("conditioning_warning", "no amplification"), ("scope", "physical calibration owned"),
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
    print(f"K1063 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
