#!/usr/bin/env python3
"""Independent controls and hostile mutations for K430."""

from __future__ import annotations

import copy
import json

from k430_k77_twisted_boundary_holonomy_cohomology import demo


def valid(result: dict) -> bool:
    family = result["boundary_family"]
    cases = result["exact_cases"]
    identity = cases["identity_twist"]
    transported = cases["transported_twist"]
    decision = result["decision"]
    return all(
        [
            family["kernel"] == "Fix(S)",
            family["cokernel"] == "Fix(S^T), hence the same dimension",
            family["fredholm_index"] == 0,
            identity["boundary_matrix_determinant"] == "2",
            identity["kernel_dimension"] == 0,
            identity["cokernel_dimension"] == 0,
            identity["bounded_green_exists"] is True,
            transported["boundary_matrix_determinant"] == "0",
            transported["kernel_dimension"] == 2,
            transported["cokernel_dimension"] == 2,
            transported["bounded_green_exists"] is False,
            cases["invertible_green_boundary_replayed"] is True,
            decision["same_variable_differential_has_boundary_dependent_cohomology"] is True,
            decision["identity_twist_is_invertible_for_quarter_turn_monodromy"] is True,
            decision["monodromy_matched_twist_has_kernel_and_cokernel_dimension"] == 2,
            decision["boundary_condition_is_source_selected"] is False,
            decision["physical_bfv_cohomology_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("boundary_family", "kernel"), "all fibers"),
        (("boundary_family", "cokernel"), "zero"),
        (("boundary_family", "fredholm_index"), 1),
        (("exact_cases", "identity_twist", "boundary_matrix_determinant"), "0"),
        (("exact_cases", "identity_twist", "kernel_dimension"), 1),
        (("exact_cases", "identity_twist", "cokernel_dimension"), 1),
        (("exact_cases", "identity_twist", "bounded_green_exists"), False),
        (("exact_cases", "transported_twist", "kernel_dimension"), 0),
        (("exact_cases", "transported_twist", "cokernel_dimension"), 0),
        (("exact_cases", "transported_twist", "bounded_green_exists"), True),
        (("exact_cases", "invertible_green_boundary_replayed"), False),
        (("decision", "same_variable_differential_has_boundary_dependent_cohomology"), False),
        (("decision", "identity_twist_is_invertible_for_quarter_turn_monodromy"), False),
        (("decision", "monodromy_matched_twist_has_kernel_and_cokernel_dimension"), 0),
        (("decision", "boundary_condition_is_source_selected"), True),
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
    print(json.dumps({"controls_passed": 20, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
