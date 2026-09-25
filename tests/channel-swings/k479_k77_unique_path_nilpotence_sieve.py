#!/usr/bin/env python3
"""K479 two-step unique-path support obstruction to D1 D2 = 0."""

from __future__ import annotations

import argparse
import json


def analyze_support(
    source_size: int,
    middle_size: int,
    target_size: int,
    d2_source_to_middle: list[list[int]],
    d1_middle_to_target: list[list[int]],
    declared_edges_nonzero: bool,
) -> dict:
    if min(source_size, middle_size, target_size) < 0:
        raise ValueError("nonnegative dimensions required")
    if len(d2_source_to_middle) != source_size or len(d1_middle_to_target) != middle_size:
        raise ValueError("support row counts must match dimensions")
    if any(any(not isinstance(m, int) or m < 0 or m >= middle_size for m in row)
           for row in d2_source_to_middle):
        raise ValueError("D2 middle index outside range")
    if any(any(not isinstance(t, int) or t < 0 or t >= target_size for t in row)
           for row in d1_middle_to_target):
        raise ValueError("D1 target index outside range")
    if declared_edges_nonzero is not True:
        raise ValueError("support means declared nonzero coefficient entries")
    path_rows = []
    unique = []
    for source, middles in enumerate(d2_source_to_middle):
        for target in range(target_size):
            witnesses = sorted({m for m in middles if target in set(d1_middle_to_target[m])})
            if witnesses:
                row = {"source": source, "target": target, "path_count": len(witnesses),
                       "middle_witnesses": witnesses}
                path_rows.append(row)
                if len(witnesses) == 1:
                    unique.append(row)
    return {
        "source_size": source_size,
        "middle_size": middle_size,
        "target_size": target_size,
        "nonzero_two_step_pairs": len(path_rows),
        "unique_path_obstruction_count": len(unique),
        "unique_path_obstructions": unique,
        "support_nilpotence_possible": len(unique) == 0,
        "nilpotence_proved": False,
        "cancellation_coefficients_solved": False,
        "path_rows": path_rows,
    }


def demo() -> dict:
    cancellation_possible = analyze_support(
        2, 2, 2,
        [[0, 1], [0, 1]],
        [[0, 1], [0, 1]],
        True,
    )
    unique_obstruction = analyze_support(
        2, 3, 2,
        [[0], [1, 2]],
        [[0], [0, 1], [0, 1]],
        True,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K479-K77-UNIQUE-PATH-NILPOTENCE-SIEVE",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "theorem": {
            "obstruction": "If one target-source entry of D1 D2 has exactly one declared-nonzero two-step path, its single nonzero product cannot cancel.",
            "necessary_support_rule": "Every connected target-source pair needs at least two paths before coefficient cancellation is possible.",
            "ceiling": "Zero or multiple support paths do not prove coefficient-level nilpotence.",
        },
        "controls": {
            "cancellation_possible_support": cancellation_possible,
            "unique_path_obstruction": unique_obstruction,
        },
        "K77_application": {
            "D2_shape": [46592, 10752],
            "D1_shape": [35840, 46592],
            "native_support_present": False,
            "native_nilpotence_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
