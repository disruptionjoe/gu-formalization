#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K619."""

from __future__ import annotations

import copy
import json

from k619_k77_zero_form_moving_graph_common_action_module import build


def controls(p: dict) -> list[bool]:
    t = p["common_module_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["filtration_rows"] == p["cross_characteristic_packets"][1]["filtration_rows"],
        t["seed_ranks"] == {"zero_form": 128, "moving_graph": 128},
        t["seed_intersection_rank"] == 0,
        t["depth_2_hull_ranks"] == {"zero_form": 256, "moving_graph": 256},
        t["depth_2_intersection_rank"] == 128,
        t["depth_3_hull_ranks"] == {"zero_form": 384, "moving_graph": 384},
        t["depth_3_join_rank"] == 384,
        t["depth_3_intersection_rank"] == 384,
        t["minimal_common_action_module_rank"] == 384,
        t["filtrations_equal_from_depth_3"] is True,
        t["corrected_carrier_complement_rank"] == 128,
        o["source_owns_zero_form_field_space"] is True,
        o["source_selects_nonzero_zero_form_background"] is False,
        o["historical_moving_graph_is_source_selected"] is False,
        o["equality_of_generated_subspaces_identifies_seed_maps"] is False,
        o["common_module_is_stationary_solution_space"] is False,
        o["common_module_supplies_mixed_hessian_coupling"] is False,
        o["unrestricted_southeast_route_already_completed"] is True,
        o["local_full_field_ordinary_gauge_bv_already_completed"] is True,
        d["two_disjoint_seeds_generate_same_A_module"] is True,
        d["K615_stationarity_obstruction_retracted"] is False,
        d["actual_K596_K598_packet_released"] is False,
        d["selected_source_action_rejected"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def set_path(p: dict, path: tuple[str, ...], value: object) -> None:
    cursor = p
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> int:
    payload = build()
    assert all(controls(payload))
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("target_claim",), "SC-ACT-01"),
        (("common_module_theorem", "seed_intersection_rank"), 128),
        (("common_module_theorem", "depth_2_intersection_rank"), 0),
        (("common_module_theorem", "depth_3_join_rank"), 512),
        (("common_module_theorem", "depth_3_intersection_rank"), 256),
        (("common_module_theorem", "minimal_common_action_module_rank"), 512),
        (("common_module_theorem", "filtrations_equal_from_depth_3"), False),
        (("common_module_theorem", "corrected_carrier_complement_rank"), 0),
        (("ownership_reconciliation", "source_selects_nonzero_zero_form_background"), True),
        (("ownership_reconciliation", "historical_moving_graph_is_source_selected"), True),
        (("ownership_reconciliation", "equality_of_generated_subspaces_identifies_seed_maps"), True),
        (("ownership_reconciliation", "common_module_is_stationary_solution_space"), True),
        (("ownership_reconciliation", "common_module_supplies_mixed_hessian_coupling"), True),
        (("ownership_reconciliation", "unrestricted_southeast_route_already_completed"), False),
        (("ownership_reconciliation", "local_full_field_ordinary_gauge_bv_already_completed"), False),
        (("decision", "two_disjoint_seeds_generate_same_A_module"), False),
        (("decision", "K615_stationarity_obstruction_retracted"), True),
        (("decision", "actual_K596_K598_packet_released"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        set_path(case, path, value)
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
