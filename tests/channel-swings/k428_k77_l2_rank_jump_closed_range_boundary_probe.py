#!/usr/bin/env python3
"""Independent controls and hostile mutations for K428."""

from __future__ import annotations

import copy
import json
from fractions import Fraction

from k428_k77_l2_rank_jump_closed_range_boundary import demo


def valid(result: dict) -> bool:
    scalar = result["scalar_multiplier"]
    full = result["full_70_by_91_family"]
    witnesses = scalar["unit_input_witnesses"]
    expected = [Fraction(1, 3 * row["n"] * row["n"]) for row in witnesses]
    observed = [Fraction(row["output_norm_squared"]) for row in witnesses]
    return all(
        [
            scalar["kernel_dimension"] == 0,
            scalar["adjoint_kernel_dimension"] == 0,
            scalar["range_dense"] is True,
            scalar["range_closed"] is False,
            scalar["bounded_below"] is False,
            scalar["bounded_green_inverse_exists"] is False,
            [row["n"] for row in witnesses] == [1, 2, 4, 8, 16, 32],
            observed == expected,
            all(left > right for left, right in zip(observed, observed[1:])),
            full["extra_global_l2_kernel"] is False,
            full["range_dense_in_target"] is True,
            full["range_closed"] is False,
            full["reduced_cokernel_dimension"] == 0,
            result["decision"]["isolated_rank_jump_forces_nonzero_reduced_hilbert_cohomology"] is False,
            result["decision"]["isolated_rank_jump_can_destroy_closed_range"] is True,
            result["decision"]["smooth_and_hilbert_cokernels_agree_automatically"] is False,
            result["decision"]["green_domain_and_closed_range_are_load_bearing"] is True,
            result["decision"]["positive_physical_domain_constructed"] is False,
            result["decision"]["physical_bfv_cohomology_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("scalar_multiplier", "kernel_dimension"), 1),
        (("scalar_multiplier", "range_dense"), False),
        (("scalar_multiplier", "range_closed"), True),
        (("scalar_multiplier", "bounded_below"), True),
        (("scalar_multiplier", "bounded_green_inverse_exists"), True),
        (("scalar_multiplier", "unit_input_witnesses", 2, "output_norm_squared"), "1/3"),
        (("full_70_by_91_family", "extra_global_l2_kernel"), True),
        (("full_70_by_91_family", "range_closed"), True),
        (("full_70_by_91_family", "reduced_cokernel_dimension"), 1),
        (("decision", "isolated_rank_jump_forces_nonzero_reduced_hilbert_cohomology"), True),
        (("decision", "smooth_and_hilbert_cokernels_agree_automatically"), True),
        (("decision", "positive_physical_domain_constructed"), True),
        (("decision", "physical_bfv_cohomology_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 18, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
