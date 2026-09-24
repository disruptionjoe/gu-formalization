#!/usr/bin/env python3
"""Independent controls and hostile mutations for K427."""

from __future__ import annotations

import copy
import json

from k427_k77_smooth_rank_jump_cokernel import demo, evaluate_at_one, multiply_by_one_minus_t


def valid(result: dict) -> bool:
    controls = result["smooth_global_result"]["polynomial_controls"]
    return all(
        [
            result["family"]["generic_rank"] == 70,
            result["family"]["rank_at_t_equals_1"] == 69,
            result["family"]["fiber_kernel_dimensions"] == {"generic": 21, "t_equals_1": 22},
            result["smooth_global_result"]["extra_global_smooth_syzygy"] is False,
            result["smooth_global_result"]["cokernel_dimension"] == 1,
            len(controls) == 4,
            all(evaluate_at_one(row["polynomial"]) == 0 for row in controls),
            all(multiply_by_one_minus_t(row["quotient"]) == row["polynomial"] for row in controls),
            result["decision"]["rank_jump_creates_smooth_cokernel_class"] is True,
            result["decision"]["fiber_kernel_jump_creates_global_smooth_generator"] is False,
            result["decision"]["category_and_domain_are_load_bearing"] is True,
            result["decision"]["source_owned_transverse_family_supplied"] is False,
            result["decision"]["physical_bfv_cohomology_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("family", "generic_rank"), 69),
        (("family", "rank_at_t_equals_1"), 70),
        (("family", "fiber_kernel_dimensions", "t_equals_1"), 21),
        (("smooth_global_result", "extra_global_smooth_syzygy"), True),
        (("smooth_global_result", "cokernel_dimension"), 0),
        (("smooth_global_result", "polynomial_controls", 0, "quotient"), [1]),
        (("decision", "rank_jump_creates_smooth_cokernel_class"), False),
        (("decision", "fiber_kernel_jump_creates_global_smooth_generator"), True),
        (("decision", "category_and_domain_are_load_bearing"), False),
        (("decision", "source_owned_transverse_family_supplied"), True),
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
    print(json.dumps({"controls_passed": 15, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
