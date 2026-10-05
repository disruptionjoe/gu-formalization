#!/usr/bin/env python3
"""Hostile mutations for K1127."""
from copy import deepcopy
from k1127_k887_t0_gauge_carrier_correction import build, validate


def main():
    mutations = [
        ("native_coordinates", "(g,varpi)"),
        ("t0_distortion_gauge_generator_owned", True),
        ("action_owned_metric_diffeomorphism_rank", 16384),
        ("k720_owned_gauge_ranks", [16384]),
        ("k887_radial_control_dimension", 4),
        ("k887_radial_image_rank", 0),
        ("k887_exact_slice_calculation_survives", False),
        ("k887_radial_control_is_action_owned_t0_gauge", True),
        ("k887_source_action_gauge_descent_failure_survives", True),
        ("reason", "connection gauge equals distortion gauge"),
        ("surviving_scope", "native Noether test"),
        ("affected_chain", "none"),
        ("source_and_ledger_effect", "PROMOTED"),
    ]
    caught = 0
    for key, value in mutations:
        data = deepcopy(build()); data[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1127 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
