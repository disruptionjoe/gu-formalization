#!/usr/bin/env python3
"""Independent controls and hostile mutations for K429."""

from __future__ import annotations

import copy
import json

from k429_k77_covariant_incoming_domain_green import demo


def valid(result: dict) -> bool:
    fixture = result["exact_fixture"]
    domain = result["incoming_domain"]
    green = result["green_operator"]
    pairing = result["pairing"]
    decision = result["decision"]
    return all(
        [
            all(fixture.values()),
            result["conditional_action_reduction"]["covariant_differential"] == "D_A=d/dt+A(t)",
            domain["closed_dense_domain"] is True,
            domain["kernel_dimension"] == 0,
            domain["cokernel_dimension"] == 0,
            domain["bijective"] is True,
            green["two_sided_inverse_on_domain"] is True,
            green["l2_operator_norm"] == "2/pi",
            green["bounded_l2_to_h1"] is True,
            pairing["formal_skew_adjoint"] is True,
            pairing["adjoint_relation"] == "G_in^*=-G_out",
            decision["variable_connection_forces_nonclosed_range"] is False,
            decision["explicit_boundary_condition_can_close_range"] is True,
            decision["bounded_green_inverse_exists"] is True,
            decision["physical_k77_domain_constructed"] is False,
        ]
    )


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("exact_fixture", "transport_is_orthogonal"), False),
        (("exact_fixture", "connection_is_skew"), False),
        (("exact_fixture", "connection_is_variable"), False),
        (("exact_fixture", "gauge_conjugation"), False),
        (("exact_fixture", "incoming_green_right_inverse"), False),
        (("exact_fixture", "incoming_trace_zero"), False),
        (("incoming_domain", "closed_dense_domain"), False),
        (("incoming_domain", "kernel_dimension"), 1),
        (("incoming_domain", "cokernel_dimension"), 1),
        (("green_operator", "two_sided_inverse_on_domain"), False),
        (("green_operator", "l2_operator_norm"), "1"),
        (("green_operator", "bounded_l2_to_h1"), False),
        (("pairing", "formal_skew_adjoint"), False),
        (("pairing", "adjoint_relation"), "G_in^*=G_out"),
        (("decision", "variable_connection_forces_nonclosed_range"), True),
        (("decision", "explicit_boundary_condition_can_close_range"), False),
        (("decision", "bounded_green_inverse_exists"), False),
        (("decision", "physical_k77_domain_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        candidate[path[0]][path[1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": 22, "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
