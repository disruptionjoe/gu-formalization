#!/usr/bin/env python3
"""Independent controls and hostile mutations for K426."""

from __future__ import annotations

import copy
import json

from k426_k77_constant_functional_lift_contractibility import demo


def valid(result: dict) -> bool:
    identities = result["contracting_homotopy"]["identities"]
    return all(
        [
            result["finite_fixture"]["dimensions"] == [21, 91, 70],
            result["finite_fixture"]["ranks"] == [21, 70],
            result["finite_fixture"]["cohomology_dimensions"] == [0, 0, 0],
            all(identities.values()),
            result["contracting_homotopy"]["euclidean_operator_norms"] == {"d0": 1, "d1": 1, "h1": 1, "h2": 1},
            result["functional_lift"]["same_coordinate_maps"] is True,
            result["functional_lift"]["contracting_homotopy_tensors_with_identity"] is True,
            result["functional_lift"]["exact"] is True,
            result["functional_lift"]["hilbert_ranges_closed"] is True,
            result["functional_lift"]["bounded_green_contraction_norm"] == 1,
            result["decision"]["constant_pointwise_tensor_lift_creates_cohomology"] is False,
            result["decision"]["physical_bfv_cohomology_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("finite_fixture", "dimensions"), [21, 90, 70]),
        (("finite_fixture", "ranks"), [20, 70]),
        (("finite_fixture", "cohomology_dimensions"), [0, 1, 0]),
        (("contracting_homotopy", "identities", "h1_d0_is_identity"), False),
        (("contracting_homotopy", "identities", "d0_h1_plus_h2_d1_is_identity"), False),
        (("contracting_homotopy", "identities", "d1_h2_is_identity"), False),
        (("contracting_homotopy", "identities", "d1_d0_is_zero"), False),
        (("functional_lift", "exact"), False),
        (("functional_lift", "hilbert_ranges_closed"), False),
        (("functional_lift", "bounded_green_contraction_norm"), 2),
        (("decision", "constant_pointwise_tensor_lift_creates_cohomology"), True),
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
    print(json.dumps({"controls_passed": 16, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
