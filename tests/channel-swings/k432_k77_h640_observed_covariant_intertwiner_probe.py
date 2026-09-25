#!/usr/bin/env python3
"""Independent contract checks and hostile mutations for K432."""

from __future__ import annotations

import copy
import json

from k432_k77_h640_observed_covariant_intertwiner import demo


def control_predicates(result: dict) -> list[bool]:
    inherited = result["compressed_h640_input"]
    fixture = result["two_carrier_fixture"]
    laws = fixture["exact_laws"]
    descent = result["projector_descent"]
    boundary = result["incoming_boundary_and_green"]
    decision = result["decision"]
    return [
        result["schema_version"] == "1.0",
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        inherited["ambient_rank"] == 1920,
        inherited["native_h640_rank"] == 640,
        inherited["observed_rank"] == 640,
        inherited["observation_restricts_isomorphically"] is True,
        inherited["full_h640_matrix_serialized"] is False,
        inherited["full_1920_matrix_serialized"] is False,
        laws["observation_inverse"] is True,
        laws["lift_inverse"] is True,
        laws["gram_transport"] is True,
        laws["observation_variable"] is True,
        laws["lift_variable"] is True,
        laws["observation_covariant_intertwiner"] is True,
        laws["lift_covariant_intertwiner"] is True,
        laws["native_projector_idempotent"] is True,
        laws["observed_projector_idempotent"] is True,
        laws["native_projector_self_adjoint"] is True,
        laws["observed_projector_h_self_adjoint"] is True,
        laws["observation_projector_intertwines"] is True,
        laws["lift_projector_intertwines"] is True,
        laws["native_projector_parallel"] is True,
        laws["observed_projector_parallel"] is True,
        laws["incoming_boundary_maps"] is True,
        laws["incoming_boundary_inverse"] is True,
        laws["incoming_boundary_projection_preserves"] is True,
        laws["full_green_intertwines"] is True,
        laws["native_projected_green_commutes"] is True,
        laws["observed_projected_green_commutes"] is True,
        laws["projected_green_intertwines"] is True,
        descent["parallel_on_both_carriers"] is True,
        boundary["green_square"] == "J G_H=G_O J",
        decision["conditional_two_carrier_covariant_intertwiner_constructed"] is True,
        decision["actual_full_h640_or_1920_intertwiner_constructed"] is False,
        decision["physical_bv_bfv_observation_constructed"] is False,
        decision["source_or_ledger_effect"] == "none",
    ]


def valid(result: dict) -> bool:
    return all(control_predicates(result))


def main() -> int:
    result = demo()
    controls = control_predicates(result)
    assert len(controls) == 37
    assert all(controls)

    mutations = []
    for path, value in [
        (("compressed_h640_input", "observation_restricts_isomorphically"), False),
        (("compressed_h640_input", "full_h640_matrix_serialized"), True),
        (("compressed_h640_input", "full_1920_matrix_serialized"), True),
        (("two_carrier_fixture", "exact_laws", "observation_inverse"), False),
        (("two_carrier_fixture", "exact_laws", "lift_inverse"), False),
        (("two_carrier_fixture", "exact_laws", "gram_transport"), False),
        (("two_carrier_fixture", "exact_laws", "observation_variable"), False),
        (("two_carrier_fixture", "exact_laws", "observation_covariant_intertwiner"), False),
        (("two_carrier_fixture", "exact_laws", "lift_covariant_intertwiner"), False),
        (("two_carrier_fixture", "exact_laws", "native_projector_idempotent"), False),
        (("two_carrier_fixture", "exact_laws", "observed_projector_idempotent"), False),
        (("two_carrier_fixture", "exact_laws", "observed_projector_h_self_adjoint"), False),
        (("two_carrier_fixture", "exact_laws", "observation_projector_intertwines"), False),
        (("two_carrier_fixture", "exact_laws", "lift_projector_intertwines"), False),
        (("two_carrier_fixture", "exact_laws", "native_projector_parallel"), False),
        (("two_carrier_fixture", "exact_laws", "incoming_boundary_maps"), False),
        (("two_carrier_fixture", "exact_laws", "incoming_boundary_inverse"), False),
        (("two_carrier_fixture", "exact_laws", "full_green_intertwines"), False),
        (("two_carrier_fixture", "exact_laws", "native_projected_green_commutes"), False),
        (("two_carrier_fixture", "exact_laws", "observed_projected_green_commutes"), False),
        (("two_carrier_fixture", "exact_laws", "projected_green_intertwines"), False),
        (("projector_descent", "parallel_on_both_carriers"), False),
        (("decision", "conditional_two_carrier_covariant_intertwiner_constructed"), False),
        (("decision", "actual_full_h640_or_1920_intertwiner_constructed"), True),
        (("decision", "physical_bv_bfv_observation_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)

    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations) == 25
    print(json.dumps({"controls_passed": len(controls), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
