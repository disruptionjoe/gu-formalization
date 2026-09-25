#!/usr/bin/env python3
"""Independent controls and hostile mutations for K447."""

from __future__ import annotations

import copy
import json

from k447_k152_charge_sector_galerkin_defect_census import demo


def controls(result: dict) -> list[bool]:
    rows = result["sectors"]
    return [
        result["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        result["direction"] == "observed_to_native",
        [row["charge"] for row in rows] == [[0, 0], [1, 0], [0, 1]],
        [row["coarse_dimension"] for row in rows] == [8, 7, 7],
        [row["raw_defect"]["rank"] for row in rows] == [8, 7, 7],
        [row["raw_defect"]["support_count"] for row in rows] == [8, 7, 7],
        [row["raw_defect"]["inertia_positive_negative_zero"] for row in rows] == [[8, 0, 0], [7, 0, 0], [7, 0, 0]],
        rows[0]["raw_defect"]["diagonal"] == ["2/105", "2/105", "8/105", "2/105", "8/105", "8/105", "8/105", "32/105"],
        [row["regular_defect"]["rank"] for row in rows] == [8, 7, 7],
        [row["regular_defect"]["support_count"] for row in rows] == [64, 41, 41],
        [row["regular_defect"]["diagonal_support_count"] for row in rows] == [8, 7, 7],
        [row["regular_defect"]["inertia_positive_negative_zero"] for row in rows] == [[5, 3, 0], [5, 2, 0], [5, 2, 0]],
        all(row["regular_defect"]["entries_are_rational"] for row in rows),
        result["decision"]["raw_defect_full_rank_in_every_sector"] is True,
        result["decision"]["regular_defect_full_rank_in_every_sector"] is True,
        result["decision"]["q10_q01_signatures_match"] is True,
        result["decision"]["finite_control_is_limiting_native_form"] is False,
        result["decision"]["native_K152_interval_emitted"] is False,
    ]


def main() -> int:
    result = demo()
    assert all(controls(result))
    specs = [
        (("classification",), "SOURCE_NATIVE_ROUTE"), (("direction",), "native_to_observed"),
        (("sectors", 0, "coarse_dimension"), 7), (("sectors", 0, "raw_defect", "rank"), 7),
        (("sectors", 1, "raw_defect", "support_count"), 6), (("sectors", 0, "raw_defect", "inertia_positive_negative_zero"), [7, 1, 0]),
        (("sectors", 0, "raw_defect", "diagonal"), []), (("sectors", 0, "regular_defect", "rank"), 7),
        (("sectors", 0, "regular_defect", "support_count"), 63), (("sectors", 1, "regular_defect", "diagonal_support_count"), 6),
        (("sectors", 0, "regular_defect", "inertia_positive_negative_zero"), [8, 0, 0]),
        (("sectors", 2, "regular_defect", "entries_are_rational"), False),
        (("decision", "raw_defect_full_rank_in_every_sector"), False),
        (("decision", "regular_defect_full_rank_in_every_sector"), False),
        (("decision", "q10_q01_signatures_match"), False),
        (("decision", "finite_control_is_limiting_native_form"), True),
        (("decision", "native_K152_interval_emitted"), True),
    ]
    rejected = 0
    for path, value in specs:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        rejected += int(not all(controls(candidate)))
    assert rejected == len(specs)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
