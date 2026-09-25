#!/usr/bin/env python3
"""Independent controls and hostile mutations for K440."""

from __future__ import annotations

import copy
import json

from k440_k77_corrected_boundary_green_domain import demo


def controls(result: dict) -> list[bool]:
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        [row["eigenvalue"] for row in result["spectral_blocks"]] == ["1", "1/24", "-1", "-1/24"],
        [row["rank"] for row in result["spectral_blocks"]] == [192, 64, 192, 64],
        all(result["exact_checks"].values()),
        result["green_operator"]["right_and_left_inverse"] is True,
        result["green_operator"]["l2_operator_norm_upper_bound"] == "24",
        result["green_operator"]["l2_to_derivative_bound"] == "25",
        result["green_operator"]["l2_to_h1_sum_bound"] == "49",
        result["closed_domain_theorem"]["domain_closed_in_h1"] is True,
        result["closed_domain_theorem"]["kernel_dimension"] == 0,
        result["closed_domain_theorem"]["cokernel_dimension"] == 0,
        decision["conditional_closed_green_domain_constructed"] is True,
        decision["constraint_preservation_inherited_from_k439"] is True,
        decision["moving_lower_order_domain_constructed"] is False,
        decision["nonlinear_bv_kt_invariance_proved"] is False,
        decision["physical_boundary_selected"] is False,
        decision["physical_cohomology_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("spectral_blocks", 1, "eigenvalue"), "0"),
        (("spectral_blocks", 1, "rank"), 0),
        (("exact_checks", "spectral_gap_one_over_24"), False),
        (("green_operator", "right_and_left_inverse"), False),
        (("green_operator", "l2_operator_norm_upper_bound"), "1"),
        (("green_operator", "l2_to_derivative_bound"), "2"),
        (("green_operator", "l2_to_h1_sum_bound"), "2"),
        (("closed_domain_theorem", "domain_closed_in_h1"), False),
        (("closed_domain_theorem", "kernel_dimension"), 1),
        (("closed_domain_theorem", "cokernel_dimension"), 1),
        (("decision", "conditional_closed_green_domain_constructed"), False),
        (("decision", "constraint_preservation_inherited_from_k439"), False),
        (("decision", "moving_lower_order_domain_constructed"), True),
        (("decision", "nonlinear_bv_kt_invariance_proved"), True),
        (("decision", "physical_boundary_selected"), True),
        (("decision", "physical_cohomology_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
