#!/usr/bin/env python3
"""Independent serialization controls and hostile mutations for K434."""

from __future__ import annotations

import copy
import json

from k434_k77_action_flux_maximal_dissipative_projector import demo


def controls(result: dict) -> list[bool]:
    theorem = result["spectral_projector_theorem"]
    dissipative = result["maximal_dissipative_proof"]
    transport = result["covariant_transport"]
    ownership = result["ownership_boundary"]
    fixture = result["exact_fixture"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        theorem["rank"] == 2,
        theorem["carrier_rank"] == 4,
        theorem["rank_fraction"] == "1/2",
        theorem["idempotent"] is True,
        theorem["orientation_law"] == "Pi_in(-n)=I-Pi_in(n)=Pi_out(n)",
        dissipative["incoming_flux_gram"] == [["-5", "0"], ["0", "-7"]],
        dissipative["negative_on_nonzero_incoming_vectors"] is True,
        dissipative["nonpositive_on_incoming_space"] is True,
        dissipative["normal_flux_signature"] == [2, 2, 0],
        dissipative["incoming_dimension"] == 2,
        dissipative["maximal_nonpositive"] is True,
        transport["exact_at_rational_samples"] is True,
        ownership["projector_family_action_owned"] is True,
        ownership["member_boundary_geometry_selected"] is True,
        ownership["physical_domain_selected"] is False,
        all(fixture.values()),
        fixture["time_symbol_invertible"] is True,
        fixture["reduced_symbol_involution"] is True,
        fixture["incoming_formula_exact"] is True,
        fixture["incoming_idempotent"] is True,
        fixture["incoming_rank_two"] is True,
        fixture["incoming_rank_half"] is True,
        fixture["flux_restriction_exact"] is True,
        fixture["incoming_flux_negative_definite_on_range"] is True,
        fixture["incoming_flux_nonpositive"] is True,
        fixture["maximal_nonpositive_dimension_two"] is True,
        fixture["projector_transport_covariant"] is True,
        fixture["orientation_reversal_complement"] is True,
        decision["spectral_incoming_projector_derived"] is True,
        decision["rank_half_idempotent"] is True,
        decision["negative_and_nonpositive_flux_proved"] is True,
        decision["maximal_nonpositive_dimension_proved"] is True,
        decision["covariant_transport_proved"] is True,
        decision["full_k77_projector_constructed"] is False,
        decision["physical_boundary_domain_selected"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("spectral_projector_theorem", "rank"), 3),
        (("spectral_projector_theorem", "carrier_rank"), 5),
        (("spectral_projector_theorem", "rank_fraction"), "3/4"),
        (("spectral_projector_theorem", "idempotent"), False),
        (("spectral_projector_theorem", "orientation_law"), "Pi_in(-n)=Pi_in(n)"),
        (("maximal_dissipative_proof", "incoming_flux_gram"), [["5", "0"], ["0", "7"]]),
        (("maximal_dissipative_proof", "negative_on_nonzero_incoming_vectors"), False),
        (("maximal_dissipative_proof", "nonpositive_on_incoming_space"), False),
        (("maximal_dissipative_proof", "normal_flux_signature"), [3, 1, 0]),
        (("maximal_dissipative_proof", "incoming_dimension"), 3),
        (("maximal_dissipative_proof", "maximal_nonpositive"), False),
        (("covariant_transport", "exact_at_rational_samples"), False),
        (("ownership_boundary", "projector_family_action_owned"), False),
        (("ownership_boundary", "member_boundary_geometry_selected"), False),
        (("ownership_boundary", "physical_domain_selected"), True),
        (("exact_fixture", "time_symbol_invertible"), False),
        (("exact_fixture", "reduced_symbol_involution"), False),
        (("exact_fixture", "incoming_formula_exact"), False),
        (("exact_fixture", "incoming_idempotent"), False),
        (("exact_fixture", "incoming_rank_half"), False),
        (("exact_fixture", "incoming_flux_negative_definite_on_range"), False),
        (("exact_fixture", "maximal_nonpositive_dimension_two"), False),
        (("exact_fixture", "projector_transport_covariant"), False),
        (("exact_fixture", "orientation_reversal_complement"), False),
        (("decision", "full_k77_projector_constructed"), True),
        (("decision", "physical_boundary_domain_selected"), True),
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
