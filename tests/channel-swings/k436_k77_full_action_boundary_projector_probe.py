#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K436."""

from __future__ import annotations

import copy
import json

from k436_k77_full_action_boundary_projector import demo


def controls(result: dict) -> list[bool]:
    packets = result["cross_characteristic_packets"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        result["boundary"]["normal_index"] == 7,
        result["boundary"]["outward_conormal"] == "+dx7",
        [row["prime"] for row in packets] == [1009, 1013],
        all(row["ambient_ranks"] == {"carrier": 1920, "incoming": 960, "outgoing": 960} for row in packets),
        all(row["h640_ranks"] == {"carrier": 640, "incoming": 320, "outgoing": 320} for row in packets),
        all(all(row["checks"].values()) for row in packets),
        all(row["matrices"]["ambient_incoming_projector"]["nnz"] == 25472 for row in packets),
        all(row["matrices"]["observed_incoming_projector"]["nnz"] == 3200 for row in packets),
        all(row["matrices"]["h640_incoming_lift"]["rank"] == 320 for row in packets),
        decision["actual_rank_1920_time_and_normal_symbols_constructed"] is True,
        decision["actual_rank_960_ambient_incoming_projector_constructed"] is True,
        decision["h640_preserved"] is True,
        decision["actual_rank_320_h640_incoming_projector_constructed"] is True,
        decision["orientation_load_bearing"] is True,
        decision["global_closed_domain_constructed"] is False,
        decision["physical_boundary_selected"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    mutations = []
    for path, value in [
        (("classification",), "SUPPORTED"),
        (("direction",), "observed_to_native"),
        (("boundary", "normal_index"), 8),
        (("boundary", "outward_conormal"), "-dx7"),
        (("cross_characteristic_packets", 0, "prime"), 1013),
        (("cross_characteristic_packets", 0, "ambient_ranks", "incoming"), 959),
        (("cross_characteristic_packets", 0, "h640_ranks", "incoming"), 319),
        (("cross_characteristic_packets", 0, "checks", "reduced_symbol_involution"), False),
        (("cross_characteristic_packets", 0, "matrices", "ambient_incoming_projector", "nnz"), 1),
        (("cross_characteristic_packets", 0, "matrices", "observed_incoming_projector", "nnz"), 1),
        (("cross_characteristic_packets", 0, "matrices", "h640_incoming_lift", "rank"), 319),
        (("decision", "actual_rank_1920_time_and_normal_symbols_constructed"), False),
        (("decision", "actual_rank_960_ambient_incoming_projector_constructed"), False),
        (("decision", "h640_preserved"), False),
        (("decision", "actual_rank_320_h640_incoming_projector_constructed"), False),
        (("decision", "orientation_load_bearing"), False),
        (("decision", "global_closed_domain_constructed"), True),
        (("decision", "physical_boundary_selected"), True),
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
