#!/usr/bin/env python3
"""Independent controls and hostile mutations for K442."""

from __future__ import annotations

import copy
import json

from k442_k77_corrected_boundary_kt_product import demo


def controls(result: dict) -> list[bool]:
    finite = result["finite_product_complex"]
    kt = result["homogeneous_orbit_kt"]
    boundary = result["boundary_descent"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        finite["base_dimensions"] == [21, 91, 70],
        finite["corrected_carrier_rank"] == 512,
        finite["product_dimensions"] == [10752, 46592, 35840],
        finite["differential_ranks"] == [10752, 35840],
        finite["middle_kernel_dimension"] == 10752,
        finite["finite_cohomology_dimensions"] == [0, 0, 0],
        finite["incoming_dimensions_by_degree"] == [5376, 23296, 17920],
        all(finite["exact_checks"].values()),
        kt["delta_squared_zero_on_generators"] is True,
        kt["positive_antifield_degree_acyclic"] is True,
        kt["full_nonlinear_k77_properness"] is False,
        boundary["commutator_zero"] is True,
        boundary["contraction_commutes_with_boundary"] is True,
        boundary["boundary_projectors_parallel"] is True,
        boundary["closed_trace_subcomplex"] is True,
        decision["decoupled_kt_boundary_product_constructed"] is True,
        decision["proper_homogeneous_orbit_kt_preserved"] is True,
        decision["moving_boundary_subcomplex_preserved"] is True,
        decision["physical_cohomology_constructed"] is False,
        decision["full_interacting_bv_kt_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    specs = [
        (("classification",), "SUPPORTED"),
        (("direction",), "observed_to_native"),
        (("finite_product_complex", "base_dimensions"), [21, 90, 70]),
        (("finite_product_complex", "corrected_carrier_rank"), 640),
        (("finite_product_complex", "product_dimensions"), [21, 91, 70]),
        (("finite_product_complex", "differential_ranks"), [21, 70]),
        (("finite_product_complex", "middle_kernel_dimension"), 0),
        (("finite_product_complex", "finite_cohomology_dimensions"), [0, 1, 0]),
        (("finite_product_complex", "incoming_dimensions_by_degree"), [21, 91, 70]),
        (("finite_product_complex", "exact_checks", "middle_contraction_identity"), False),
        (("homogeneous_orbit_kt", "delta_squared_zero_on_generators"), False),
        (("homogeneous_orbit_kt", "positive_antifield_degree_acyclic"), False),
        (("homogeneous_orbit_kt", "full_nonlinear_k77_properness"), True),
        (("boundary_descent", "commutator_zero"), False),
        (("boundary_descent", "contraction_commutes_with_boundary"), False),
        (("boundary_descent", "boundary_projectors_parallel"), False),
        (("boundary_descent", "closed_trace_subcomplex"), False),
        (("decision", "decoupled_kt_boundary_product_constructed"), False),
        (("decision", "proper_homogeneous_orbit_kt_preserved"), False),
        (("decision", "moving_boundary_subcomplex_preserved"), False),
        (("decision", "physical_cohomology_constructed"), True),
        (("decision", "full_interacting_bv_kt_constructed"), True),
    ]
    mutations = []
    for path, value in specs:
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
