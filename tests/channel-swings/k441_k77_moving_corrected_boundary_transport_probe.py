#!/usr/bin/env python3
"""Independent controls and hostile mutations for K441."""

from __future__ import annotations

import copy
import json

from k441_k77_moving_corrected_boundary_transport import demo


def controls(result: dict) -> list[bool]:
    carrier = result["factorized_actual_carrier"]
    functional = result["functional_consequence"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        carrier["spectral_block_ranks"] == [192, 64, 192, 64],
        carrier["total_rank"] == 512,
        carrier["incoming_rank"] == 256,
        carrier["outgoing_rank"] == 256,
        carrier["fitted_parameters"] == 0,
        len(result["samples"]) == 4,
        all(all(row["checks"].values()) for row in result["samples"]),
        functional["domain_closed"] is True,
        functional["domain_transport_isometric"] is True,
        functional["l2_green_bound"] == "24",
        functional["physical_boundary_selected"] is False,
        decision["moving_corrected_projectors_constructed"] is True,
        decision["parallel_transport_proved"] is True,
        decision["closed_trace_domain_preserved"] is True,
        decision["full_lower_order_k77_connection_derived"] is False,
        decision["nonlinear_bv_kt_compatibility_proved"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    specs = [
        (("classification",), "SUPPORTED"),
        (("direction",), "observed_to_native"),
        (("factorized_actual_carrier", "spectral_block_ranks"), [192, 64, 128, 128]),
        (("factorized_actual_carrier", "total_rank"), 4),
        (("factorized_actual_carrier", "incoming_rank"), 192),
        (("factorized_actual_carrier", "outgoing_rank"), 320),
        (("factorized_actual_carrier", "fitted_parameters"), 1),
        (("samples", 1, "checks", "projector_parallel"), False),
        (("samples", 2, "checks", "sign_polynomial_preserved"), False),
        (("functional_consequence", "domain_closed"), False),
        (("functional_consequence", "domain_transport_isometric"), False),
        (("functional_consequence", "l2_green_bound"), "1"),
        (("functional_consequence", "physical_boundary_selected"), True),
        (("decision", "moving_corrected_projectors_constructed"), False),
        (("decision", "parallel_transport_proved"), False),
        (("decision", "closed_trace_domain_preserved"), False),
        (("decision", "full_lower_order_k77_connection_derived"), True),
        (("decision", "nonlinear_bv_kt_compatibility_proved"), True),
    ]
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
