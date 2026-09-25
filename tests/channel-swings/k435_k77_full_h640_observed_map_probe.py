#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K435."""

from __future__ import annotations

import copy
import json

from k435_k77_full_h640_observed_map import demo


EXPECTED_FINGERPRINT = [
    ["h640_basis", [1920, 640], 640],
    ["coordinate_observation", [640, 1920], 640],
    ["restricted_observation_map", [640, 640], 640],
    ["restricted_observation_inverse", [640, 640], 640],
    ["ambient_inverse_lift", [1920, 640], 640],
    ["ambient_graph_projector", [1920, 1920], 640],
]


def controls(result: dict) -> list[bool]:
    packets = result["cross_characteristic_packets"]
    decisions = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        result["serialization_contract"]["observed_slots"] == [0, 7, 8, 9, 14],
        result["cross_characteristic_shape_rank_fingerprint"] == EXPECTED_FINGERPRINT,
        [row["prime"] for row in packets] == [1009, 1013],
        all(row["pivot_count"] == 640 for row in packets),
        len({row["pivot_sha256"] for row in packets}) == 1,
        all(all(row["checks"].values()) for row in packets),
        all(row["matrices"]["h640_basis"]["nnz"] == 7296 for row in packets),
        all(row["matrices"]["restricted_observation_map"]["nnz"] == 2176 for row in packets),
        all(row["matrices"]["ambient_inverse_lift"]["nnz"] == 5760 for row in packets),
        all(row["matrices"]["ambient_graph_projector"]["nnz"] == 5760 for row in packets),
        decisions["actual_rank_640_observation_map_constructed"] is True,
        decisions["actual_rank_1920_ambient_inverse_lift_constructed"] is True,
        decisions["actual_rank_1920_graph_projector_constructed"] is True,
        decisions["compressed_rank_two_surrogate_needed"] is False,
        decisions["full_lower_order_bv_kt_differential_constructed"] is False,
        decisions["physical_cohomology_constructed"] is False,
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
        (("serialization_contract", "observed_slots"), [0, 1, 2, 3, 14]),
        (("cross_characteristic_shape_rank_fingerprint",), []),
        (("cross_characteristic_packets", 0, "prime"), 1013),
        (("cross_characteristic_packets", 0, "pivot_count"), 639),
        (("cross_characteristic_packets", 1, "pivot_sha256"), "sha256:mutated"),
        (("cross_characteristic_packets", 0, "checks", "graph_projector_idempotent"), False),
        (("cross_characteristic_packets", 0, "matrices", "h640_basis", "nnz"), 1),
        (("cross_characteristic_packets", 0, "matrices", "restricted_observation_map", "nnz"), 1),
        (("cross_characteristic_packets", 0, "matrices", "ambient_inverse_lift", "nnz"), 1),
        (("cross_characteristic_packets", 0, "matrices", "ambient_graph_projector", "nnz"), 1),
        (("decision", "actual_rank_640_observation_map_constructed"), False),
        (("decision", "actual_rank_1920_ambient_inverse_lift_constructed"), False),
        (("decision", "actual_rank_1920_graph_projector_constructed"), False),
        (("decision", "compressed_rank_two_surrogate_needed"), True),
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
