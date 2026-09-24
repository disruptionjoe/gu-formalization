#!/usr/bin/env python3
"""K423 continuous observer-overlap Schubert stratification."""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def demo() -> dict[str, Any]:
    ambient_dimension = 14
    plane_dimension = 7
    observer_dimension = 3
    grassmannian_dimension = plane_dimension * (ambient_dimension - plane_dimension)
    coordinate_histogram = {0: 140, 1: 630, 2: 420, 3: 35}
    strata = []
    for overlap in range(observer_dimension + 1):
        codimension = overlap * (
            ambient_dimension - plane_dimension - observer_dimension + overlap
        )
        common_rotation_dimension = overlap * (overlap - 1) // 2
        strata.append(
            {
                "overlap": overlap,
                "at_least_overlap_codimension": codimension,
                "at_least_overlap_dimension": grassmannian_dimension - codimension,
                "common_rotation_dimension": common_rotation_dimension,
                "common_spin_group": f"Spin({overlap})" if overlap >= 2 else "trivial_connected_group",
                "coordinate_count": coordinate_histogram[overlap],
            }
        )
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "ambient": {
            "dimension": ambient_dimension,
            "moving_plane_dimension": plane_dimension,
            "observer_plane_dimension": observer_dimension,
            "grassmannian_dimension": grassmannian_dimension,
            "signature_condition": "open (3,4) nondegeneracy condition",
        },
        "schubert_strata": strata,
        "obstruction_locus": {
            "minimum_overlap": 2,
            "codimension": strata[2]["at_least_overlap_codimension"],
            "dimension": strata[2]["at_least_overlap_dimension"],
            "full_observer_spin3_codimension": strata[3]["at_least_overlap_codimension"],
            "generic_background_has_nontrivial_common_rotation": False,
            "signature_open_condition_changes_codimension": False,
        },
        "coordinate_control": {
            "histogram": coordinate_histogram,
            "total": sum(coordinate_histogram.values()),
            "retained_common_rotation": coordinate_histogram[2] + coordinate_histogram[3],
            "insufficient_common_rotation": coordinate_histogram[0] + coordinate_histogram[1],
            "digest": digest(coordinate_histogram),
        },
        "decision": {
            "k420_central_character_obstruction_is_generic": False,
            "k420_obstruction_extends_to_continuous_overlap_at_least_two_locus": True,
            "continuous_trivial_common_rotation_backgrounds_construct_map": False,
            "next_exact_input": "An action-selected background in the open overlap-zero/one stratum and its actual differential, or an action-selected target carrier on the codimension-12 retained-symmetry locus.",
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
