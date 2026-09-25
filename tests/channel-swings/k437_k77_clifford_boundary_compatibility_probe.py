#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K437."""

from __future__ import annotations

import copy
import json

from k437_k77_clifford_boundary_compatibility import demo


EXPECTED_RANKS = {
    "observed_carrier": 640,
    "corrected_clifford_range": 512,
    "corrected_trace_lift": 128,
    "incoming_boundary_range": 320,
    "common_intersection": 192,
    "incoming_trace_lift_intersection": 0,
    "commutator": 256,
    "boundary_preservation_defect": 128,
    "corrected_preservation_defect": 128,
    "ordered_product": 320,
    "ordered_product_idempotence_defect": 128,
    "gamma_on_incoming": 128,
}


def controls(result: dict) -> list[bool]:
    packets = result["cross_characteristic_packets"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        [row["prime"] for row in packets] == [1009, 1013],
        result["cross_characteristic_rank_fingerprint"] == EXPECTED_RANKS,
        all(row["ranks"] == EXPECTED_RANKS for row in packets),
        all(all(row["checks"].values()) for row in packets),
        decision["corrected_clifford_projector_constructed_on_actual_observed_carrier"] is True,
        decision["boundary_and_corrected_projectors_commute"] is False,
        decision["boundary_preserves_corrected_range"] is False,
        decision["corrected_split_preserves_incoming_boundary_range"] is False,
        decision["canonical_product_intersection_projector_constructed"] is False,
        decision["nontrivial_set_theoretic_linear_intersection_exists"] is True,
        decision["common_green_domain_derived"] is False,
        decision["repair_selected"] is False,
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
        (("cross_characteristic_packets", 0, "prime"), 1013),
        (("cross_characteristic_rank_fingerprint", "commutator"), 0),
        (("cross_characteristic_packets", 0, "ranks", "common_intersection"), 320),
        (("cross_characteristic_packets", 0, "checks", "projectors_do_not_commute"), False),
        (("decision", "corrected_clifford_projector_constructed_on_actual_observed_carrier"), False),
        (("decision", "boundary_and_corrected_projectors_commute"), True),
        (("decision", "boundary_preserves_corrected_range"), True),
        (("decision", "corrected_split_preserves_incoming_boundary_range"), True),
        (("decision", "canonical_product_intersection_projector_constructed"), True),
        (("decision", "nontrivial_set_theoretic_linear_intersection_exists"), False),
        (("decision", "common_green_domain_derived"), True),
        (("decision", "repair_selected"), True),
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
