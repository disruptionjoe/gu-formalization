#!/usr/bin/env python3
"""K418 exact observer/frozen-stabilizer intersection and branching test."""

from __future__ import annotations

import argparse
import json
from typing import Any


def hom_rank(source: dict[str, int], target: dict[str, int]) -> int:
    return sum(source.get(irrep, 0) * multiplicity for irrep, multiplicity in target.items())


def demo() -> dict[str, Any]:
    odd_axes = {1, 3, 5, 7, 9, 11, 13}
    observer_spatial_axes = {7, 8, 9}
    observer_generators = {
        tuple(sorted((a, b)))
        for a in observer_spatial_axes
        for b in observer_spatial_axes
        if a < b
    }
    frozen_stabilizer_generators = {
        tuple(sorted((a, b)))
        for a in odd_axes
        for b in odd_axes
        if a < b
    }
    common = sorted(observer_generators & frozen_stabilizer_generators)

    # Spin(2) uses the double-cover parameter: vectors have weight 2 and
    # spinors have weight 1. A 7-vector has a rotating real plane plus five
    # fixed axes. The full 128-real-dimensional spinor is 64 weight-one planes.
    source = {"real_trivial": 21 + 7 * 5, "real_weight_2_plane": 7}
    target = {"real_weight_1_plane": 64}
    dimensions = {
        "real_trivial": 1,
        "real_weight_2_plane": 2,
        "real_weight_1_plane": 2,
    }
    source_dimension = sum(source[k] * dimensions[k] for k in source)
    target_dimension = sum(target[k] * dimensions[k] for k in target)

    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "observer": {
            "status": "conditional A>0 principal-stratum timelike-line selection",
            "adapted_lorentz_axes": [0, 7, 8, 9],
            "spatial_axes": sorted(observer_spatial_axes),
            "spatial_rotation_generators": [list(pair) for pair in sorted(observer_generators)],
        },
        "frozen_stabilizer": {
            "group": "Spin(3,4)",
            "odd_axes": sorted(odd_axes),
            "generator_count": len(frozen_stabilizer_generators),
        },
        "intersection": {
            "lie_algebra": "spin(2)",
            "generators": [list(pair) for pair in common],
            "dimension": len(common),
            "equals_k416_all_factor_diagonal_su2": False,
        },
        "spin2_branching": {
            "weight_convention": "Spin(2) double-cover parameter; vector weight 2, spinor weight 1",
            "source": source,
            "target": target,
            "source_dimension": source_dimension,
            "target_dimension": target_dimension,
            "common_irreducibles": sorted(set(source) & set(target)),
            "equivariant_hom_rank": hom_rank(source, target),
        },
        "decision": {
            "observer_selected_common_symmetry_repairs_k416_route": False,
            "tested_full_spinor_trace_map_obstructed_at_frozen_background": True,
            "source_owned_global_symmetry_breaking_selected": False,
            "quotient_or_target_differential_tested": False,
            "green_domain_solved": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
