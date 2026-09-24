#!/usr/bin/env python3
"""Independent controls and hostile mutations for K423."""

from __future__ import annotations

import copy
import json

from k423_k77_observer_overlap_schubert_stratification import demo


def valid(result: dict) -> bool:
    rows = result["schubert_strata"]
    histogram = result["coordinate_control"]["histogram"]
    return all(
        [
            result["ambient"]["grassmannian_dimension"] == 49,
            [row["overlap"] for row in rows] == [0, 1, 2, 3],
            [row["at_least_overlap_codimension"] for row in rows] == [0, 5, 12, 21],
            [row["at_least_overlap_dimension"] for row in rows] == [49, 44, 37, 28],
            [row["common_rotation_dimension"] for row in rows] == [0, 0, 1, 3],
            sum(histogram.values()) == 1225,
            result["coordinate_control"]["total"] == 1225,
            histogram == {0: 140, 1: 630, 2: 420, 3: 35},
            result["coordinate_control"]["retained_common_rotation"] == 455,
            result["coordinate_control"]["insufficient_common_rotation"] == 770,
            result["obstruction_locus"]["codimension"] == 12,
            result["obstruction_locus"]["full_observer_spin3_codimension"] == 21,
            result["obstruction_locus"]["generic_background_has_nontrivial_common_rotation"] is False,
            result["decision"]["k420_central_character_obstruction_is_generic"] is False,
            result["decision"]["k420_obstruction_extends_to_continuous_overlap_at_least_two_locus"] is True,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("ambient", "grassmannian_dimension"), 48),
        (("schubert_strata", 1, "at_least_overlap_codimension"), 4),
        (("schubert_strata", 2, "at_least_overlap_codimension"), 11),
        (("schubert_strata", 3, "common_rotation_dimension"), 2),
        (("coordinate_control", "total"), 1224),
        (("coordinate_control", "retained_common_rotation"), 454),
        (("coordinate_control", "insufficient_common_rotation"), 769),
        (("obstruction_locus", "codimension"), 5),
        (("obstruction_locus", "generic_background_has_nontrivial_common_rotation"), True),
        (("decision", "k420_central_character_obstruction_is_generic"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 15, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
