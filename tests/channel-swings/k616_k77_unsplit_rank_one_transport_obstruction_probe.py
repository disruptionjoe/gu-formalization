#!/usr/bin/env python3
"""Independent controls and hostile mutations for K616."""

from __future__ import annotations

import copy
import json

from k616_k77_unsplit_rank_one_transport_obstruction import build


def controls(p: dict) -> list[bool]:
    i = p["input_injectivity"]
    u = p["unsplit_defect_theorem"]
    m = p["matching_half_repair"]
    t = p["transport_theorem"]
    d = p["decision"]
    c = p["exact_control"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        i["outgoing_x_rank"] == 128,
        i["incoming_x_rank"] == 128,
        i["outgoing_y_rank"] == 128,
        i["incoming_y_rank"] == 128,
        i["every_nonzero_v_has_all_four_components_nonzero"] is True,
        u["rank_for_every_nonzero_v"] == 2,
        u["natural_unsplit_packet_satisfies_K596"] is False,
        u["zero_value_defect_rank"] == 0,
        m["typed_square_defect_rank"] == 0,
        m["equals_natural_unsplit_packet"] is False,
        m["split_is_action_owned"] is False,
        m["conditional_K596_packet_remains_live"] is True,
        t["rank_preserved"] is True,
        t["rank_at_every_transport_fibre"] == 2,
        t["fixed_unsplit_packet_becomes_valid"] is False,
        t["moving_nonlinear_action_coupling_covered"] is False,
        c["unsplit_defect_rank"] == 2,
        c["matching_half_defect_rank"] == 0,
        all(row["transported_defect_rank"] == 2 for row in c["transport_rows"]),
        d["K615_stationarity_obstruction_retracted"] is False,
        d["natural_unsplit_packet_rejected_in_frozen_model"] is True,
        d["matching_half_conditional_interface_retracted"] is False,
        d["matching_half_action_ownership_constructed"] is False,
        d["K596_actual_action_owned_packet_released"] is False,
        d["K598_actual_action_owned_packet_released"] is False,
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
        (("target_claim",), "SC-CHI-51"),
        (("input_injectivity", "outgoing_x_rank"), 127),
        (("input_injectivity", "incoming_x_rank"), 127),
        (("input_injectivity", "outgoing_y_rank"), 127),
        (("input_injectivity", "incoming_y_rank"), 127),
        (("input_injectivity", "every_nonzero_v_has_all_four_components_nonzero"), False),
        (("unsplit_defect_theorem", "rank_for_every_nonzero_v"), 1),
        (("unsplit_defect_theorem", "natural_unsplit_packet_satisfies_K596"), True),
        (("unsplit_defect_theorem", "zero_value_defect_rank"), 1),
        (("matching_half_repair", "typed_square_defect_rank"), 1),
        (("matching_half_repair", "equals_natural_unsplit_packet"), True),
        (("matching_half_repair", "split_is_action_owned"), True),
        (("matching_half_repair", "conditional_K596_packet_remains_live"), False),
        (("transport_theorem", "rank_preserved"), False),
        (("transport_theorem", "rank_at_every_transport_fibre"), 0),
        (("transport_theorem", "fixed_unsplit_packet_becomes_valid"), True),
        (("transport_theorem", "moving_nonlinear_action_coupling_covered"), True),
        (("exact_control", "unsplit_defect_rank"), 1),
        (("exact_control", "matching_half_defect_rank"), 1),
        (("decision", "K615_stationarity_obstruction_retracted"), True),
        (("decision", "natural_unsplit_packet_rejected_in_frozen_model"), False),
        (("decision", "matching_half_action_ownership_constructed"), True),
        (("decision", "K596_actual_action_owned_packet_released"), True),
        (("decision", "K598_actual_action_owned_packet_released"), True),
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
