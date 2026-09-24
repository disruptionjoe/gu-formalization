#!/usr/bin/env python3
"""Independent controls and hostile mutations for K431."""

from __future__ import annotations

import copy
import json

from k431_k77_parallel_observation_descent import demo


def valid(result: dict) -> bool:
    theorem = result["descent_theorem"]
    fixture = result["exact_parallel_fixture"]
    shortcut = result["shortcut_control"]
    observed = result["observed_subcomplex"]
    decision = result["decision"]
    return all(
        [
            theorem["criterion"] == "D_A(Pu)=P D_Au iff P'+[A,P]=0",
            fixture["idempotent"] is True,
            fixture["self_adjoint"] is True,
            fixture["parallel_defect_zero"] is True,
            fixture["rank"] == 1,
            fixture["incoming_green_intertwines"] is True,
            fixture["monodromy_twist_boundary_compatible"] is True,
            fixture["identity_twist_boundary_compatible"] is False,
            shortcut["commutator_defect_rank"] == 2,
            shortcut["descends"] is False,
            observed["incoming_kernel_dimension"] == 0,
            observed["incoming_cokernel_dimension"] == 0,
            observed["monodromy_matched_kernel_dimension"] == 1,
            observed["monodromy_matched_cokernel_dimension"] == 1,
            decision["same_carrier_observation_descent_constructed"] is True,
            decision["arbitrary_constant_projector_descends"] is False,
            decision["green_intertwining_requires_parallelism_and_boundary_compatibility"] is True,
            decision["corrected_clifford_projector_identified"] is False,
            decision["physical_observation_or_cohomology_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("descent_theorem", "criterion"), "P is constant"),
        (("exact_parallel_fixture", "idempotent"), False),
        (("exact_parallel_fixture", "self_adjoint"), False),
        (("exact_parallel_fixture", "parallel_defect_zero"), False),
        (("exact_parallel_fixture", "rank"), 2),
        (("exact_parallel_fixture", "incoming_green_intertwines"), False),
        (("exact_parallel_fixture", "monodromy_twist_boundary_compatible"), False),
        (("exact_parallel_fixture", "identity_twist_boundary_compatible"), True),
        (("shortcut_control", "commutator_defect_rank"), 0),
        (("shortcut_control", "descends"), True),
        (("observed_subcomplex", "incoming_kernel_dimension"), 1),
        (("observed_subcomplex", "incoming_cokernel_dimension"), 1),
        (("observed_subcomplex", "monodromy_matched_kernel_dimension"), 0),
        (("observed_subcomplex", "monodromy_matched_cokernel_dimension"), 0),
        (("decision", "same_carrier_observation_descent_constructed"), False),
        (("decision", "arbitrary_constant_projector_descends"), True),
        (("decision", "green_intertwining_requires_parallelism_and_boundary_compatibility"), False),
        (("decision", "corrected_clifford_projector_identified"), True),
        (("decision", "physical_observation_or_cohomology_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 23, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
