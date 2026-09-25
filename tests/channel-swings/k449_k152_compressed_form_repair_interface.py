#!/usr/bin/env python3
"""K449 exact compression repair and two-sided finite defect interface."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction

from k447_k152_charge_sector_galerkin_defect_census import K163, defect, exact_rank, qstr


def sector(charge: tuple[int, int]) -> dict:
    regular = defect(charge, "regular")
    size = len(regular)
    row_sums = [sum(abs(entry.a) for entry in row) for row in regular]
    if any(entry.b for row in regular for entry in row):
        raise AssertionError("K447 proves the defect is rational")
    beta = max(row_sums)
    root_two = K163.Q2(Fraction(0), Fraction(1))
    coarse = K163.regular_pullback([2], [root_two], charge, 4)
    fine = K163.regular_pullback([1, 3], [1, 1], charge, 4)
    _, _, injection = K163.local_refinement(charge)
    coarse_form = K163.unnormalized_form(coarse, "regular", root_two)
    fine_form = K163.unnormalized_form(fine, "regular", K163.Q2.of(1))
    compressed = K163.congruence(fine_form, injection)
    repaired = K163.add(coarse_form, regular)
    return {
        "charge": list(charge),
        "dimension": size,
        "defect_rank": exact_rank(regular),
        "unique_additive_repair_equals_defect": repaired == compressed,
        "coordinate_l2_two_sided_radius": qstr(beta),
        "radius_row": row_sums.index(beta),
        "bound": "-beta*I <= compression(fine)-independent_coarse <= beta*I",
    }


def demo() -> dict:
    sectors = [sector(charge) for charge in ((0, 0), (1, 0), (0, 1))]
    return {
        "schema_version": "1.0",
        "result_id": "K449-K152-COMPRESSED-FORM-REPAIR-INTERFACE",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "sectors": sectors,
        "repair": {
            "exact_compression_restores_Galerkin_identity": all(row["unique_additive_repair_equals_defect"] for row in sectors),
            "repair_is_nonzero_full_rank_in_every_sector": all(row["defect_rank"] == row["dimension"] for row in sectors),
            "repair_is_scalar_counterterm": False,
            "one_sided_monotone_repair_available": False,
            "finite_coordinate_two_sided_bounds_serialized": True,
        },
        "K152_boundary": {
            "physical_Gram_relative_bound_serialized": False,
            "cofinal_limit_defect_bound_serialized": False,
            "complete_shifted_form_dual_residual_serialized": False,
            "coercivity_serialized": False,
            "next_distinct_spectrum_serialized": False,
            "native_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "prove a cofinal physical-Gram-relative two-sided defect bound for the limiting K139 form, then combine it with the complete shifted residual, coercivity, next-distinct gap and left floor",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--demo", action="store_true"); args = parser.parse_args()
    if not args.demo: parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True)); return 0


if __name__ == "__main__": raise SystemExit(main())
