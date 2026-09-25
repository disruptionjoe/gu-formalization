#!/usr/bin/env python3
"""Independent controls and hostile mutations for K449."""

from __future__ import annotations

import copy
import json

from k449_k152_compressed_form_repair_interface import demo


def controls(r: dict) -> list[bool]:
    rows, repair, boundary = r["sectors"], r["repair"], r["K152_boundary"]
    return [
        r["classification"] == "INTERNAL_STRUCTURAL_ONLY", r["direction"] == "observed_to_native",
        [row["dimension"] for row in rows] == [8, 7, 7], [row["defect_rank"] for row in rows] == [8, 7, 7],
        all(row["unique_additive_repair_equals_defect"] for row in rows),
        [row["coordinate_l2_two_sided_radius"] for row in rows] == ["451831/727650", "673219948537327450574663/1548644690229713556480000", "673219948537327450574663/1548644690229713556480000"],
        [row["radius_row"] for row in rows] == [7, 5, 4],
        repair["exact_compression_restores_Galerkin_identity"] is True,
        repair["repair_is_nonzero_full_rank_in_every_sector"] is True,
        repair["repair_is_scalar_counterterm"] is False,
        repair["one_sided_monotone_repair_available"] is False,
        repair["finite_coordinate_two_sided_bounds_serialized"] is True,
        boundary["physical_Gram_relative_bound_serialized"] is False,
        boundary["cofinal_limit_defect_bound_serialized"] is False,
        boundary["complete_shifted_form_dual_residual_serialized"] is False,
        boundary["coercivity_serialized"] is False,
        boundary["next_distinct_spectrum_serialized"] is False,
        boundary["native_left_floor_serialized"] is False,
        boundary["native_K152_interval_emitted"] is False,
    ]


def main() -> int:
    result = demo(); assert all(controls(result))
    specs = [
        (("classification",), "SOURCE_NATIVE_ROUTE"), (("direction",), "native_to_observed"),
        (("sectors", 0, "dimension"), 7), (("sectors", 0, "defect_rank"), 7),
        (("sectors", 0, "unique_additive_repair_equals_defect"), False), (("sectors", 0, "coordinate_l2_two_sided_radius"), "0"),
        (("sectors", 1, "radius_row"), 4), (("repair", "exact_compression_restores_Galerkin_identity"), False),
        (("repair", "repair_is_nonzero_full_rank_in_every_sector"), False), (("repair", "repair_is_scalar_counterterm"), True),
        (("repair", "one_sided_monotone_repair_available"), True), (("repair", "finite_coordinate_two_sided_bounds_serialized"), False),
        (("K152_boundary", "physical_Gram_relative_bound_serialized"), True), (("K152_boundary", "cofinal_limit_defect_bound_serialized"), True),
        (("K152_boundary", "complete_shifted_form_dual_residual_serialized"), True), (("K152_boundary", "coercivity_serialized"), True),
        (("K152_boundary", "next_distinct_spectrum_serialized"), True), (("K152_boundary", "native_left_floor_serialized"), True),
        (("K152_boundary", "native_K152_interval_emitted"), True),
    ]
    rejected = 0
    for path, value in specs:
        candidate = copy.deepcopy(result); target = candidate
        for key in path[:-1]: target = target[key]
        target[path[-1]] = value; rejected += int(not all(controls(candidate)))
    assert rejected == len(specs)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True)); return 0


if __name__ == "__main__": raise SystemExit(main())
