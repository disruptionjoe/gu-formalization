#!/usr/bin/env python3
"""K420 exact coordinate-orbit observer/stabilizer census."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from math import comb
from typing import Any


ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
POSITIVE = tuple(index for index, sign in enumerate(ETA) if sign == 1)
NEGATIVE = tuple(index for index, sign in enumerate(ETA) if sign == -1)
OBSERVER_SPATIAL = frozenset((7, 8, 9))
FROZEN_ODD = frozenset(range(1, 14, 2))


def signature(plane: frozenset[int]) -> tuple[int, int]:
    return (
        sum(ETA[index] == 1 for index in plane),
        sum(ETA[index] == -1 for index in plane),
    )


def common_group(overlap: int) -> str:
    if overlap < 2:
        return "no_nontrivial_connected_observer_rotation"
    return f"Spin({overlap})"


def demo() -> dict[str, Any]:
    planes = [
        frozenset((*positive, *negative))
        for positive in itertools.combinations(POSITIVE, 3)
        for negative in itertools.combinations(NEGATIVE, 4)
    ]
    overlap_histogram = Counter(len(plane & OBSERVER_SPATIAL) for plane in planes)
    rows = []
    for overlap in sorted(overlap_histogram):
        count = overlap_histogram[overlap]
        generator_count = comb(overlap, 2)
        central_character_tested = overlap >= 2
        rows.append(
            {
                "observer_axis_overlap": overlap,
                "background_count": count,
                "common_rotation_generators": generator_count,
                "connected_common_group": common_group(overlap),
                "source_central_character": 1 if central_character_tested else None,
                "target_central_character": -1 if central_character_tested else None,
                "equivariant_hom_rank": 0 if central_character_tested else None,
            }
        )

    original_overlap = len(FROZEN_ODD & OBSERVER_SPATIAL)
    full_observer_example = frozenset((1, 2, 3, 7, 8, 9, 10))
    tested = sum(row["background_count"] for row in rows if row["equivariant_hom_rank"] == 0)
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "signature": {
            "ambient": [7, 7],
            "stabilizer_plane": [3, 4],
            "positive_axes": list(POSITIVE),
            "negative_axes": list(NEGATIVE),
        },
        "census": {
            "signature_compatible_coordinate_planes": len(planes),
            "expected_count": comb(7, 3) * comb(7, 4),
            "rows": rows,
            "nontrivial_common_symmetry_backgrounds": tested,
            "symmetry_insufficient_backgrounds": len(planes) - tested,
        },
        "controls": {
            "all_planes_have_signature_3_4": all(signature(plane) == (3, 4) for plane in planes),
            "planes_unique": len(set(planes)) == len(planes),
            "original_odd_plane_signature": list(signature(FROZEN_ODD)),
            "original_observer_axis_overlap": original_overlap,
            "original_common_group": common_group(original_overlap),
            "full_observer_spin3_example": sorted(full_observer_example),
            "full_observer_spin3_example_signature": list(signature(full_observer_example)),
        },
        "decision": {
            "coordinate_backgrounds_tested_by_common_central_character": tested,
            "tested_backgrounds_repair_full_spinor_map": False,
            "backgrounds_without_nontrivial_common_rotation_decided": False,
            "all_continuous_moving_backgrounds_exhausted": False,
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
