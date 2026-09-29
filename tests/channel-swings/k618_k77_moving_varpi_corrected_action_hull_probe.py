#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K618."""

from __future__ import annotations

import copy
import json

from k618_k77_moving_varpi_corrected_action_hull import build


def controls(p: dict) -> list[bool]:
    h = p["action_hull_theorem"]
    o = p["ownership_and_typing"]
    r = p["revival_gate"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["krylov_ranks_A0_through_A4"] == p["cross_characteristic_packets"][1]["krylov_ranks_A0_through_A4"],
        h["krylov_ranks_A0_through_A4"] == [128, 256, 384, 384, 384],
        h["minimal_action_hull_rank"] == 384,
        h["action_hull_is_full_corrected_carrier"] is False,
        h["corrected_carrier_complement_rank"] == 128,
        h["fast_outgoing_image_rank"] == 128,
        h["fast_incoming_image_rank"] == 128,
        h["slow_outgoing_image_rank"] == 64,
        h["slow_incoming_image_rank"] == 64,
        h["fast_outgoing_missing_rank"] == 64,
        h["fast_incoming_missing_rank"] == 64,
        h["slow_outgoing_missing_rank"] == 0,
        h["slow_incoming_missing_rank"] == 0,
        h["K617_graph_is_A_invariant"] is False,
        o["spectral_vector_components_are_action_derived"] is True,
        o["action_derived_vector_split_owns_mixed_hessian_coupling"] is False,
        o["matching_half_bilinear_packet_constructed"] is False,
        o["historical_receiver_hull_rank"] == 384,
        o["current_corrected_action_hull_rank"] == 384,
        o["equal_rank_identifies_historical_and_current_hulls"] is False,
        o["unrestricted_four_field_Euler_image_rank_nonnull"] == 1920,
        o["bounded_route_action_owned"] is False,
        r["corrected_carrier_supplies_nontrivial_diagnostic_module"] is True,
        r["corrected_carrier_revives_historical_bounded_graph_as_action_subsystem"] is False,
        r["K616_vector_projection_ownership_narrowed"] is True,
        r["K616_core_unsplit_packet_obstruction_retracted"] is False,
        d["K617_nontrivial_descent_retracted"] is False,
        d["K615_frozen_zero_form_obstruction_retracted"] is False,
        d["prior_unrestricted_Euler_route_kill_retracted"] is False,
        d["rank384_coincidence_promoted_to_identity"] is False,
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
        (("target_claim",), "SC-CHI-51"),
        (("action_hull_theorem", "krylov_ranks_A0_through_A4"), [128, 256, 512, 512, 512]),
        (("action_hull_theorem", "minimal_action_hull_rank"), 512),
        (("action_hull_theorem", "action_hull_is_full_corrected_carrier"), True),
        (("action_hull_theorem", "corrected_carrier_complement_rank"), 0),
        (("action_hull_theorem", "fast_outgoing_missing_rank"), 0),
        (("action_hull_theorem", "fast_incoming_missing_rank"), 0),
        (("action_hull_theorem", "slow_outgoing_missing_rank"), 64),
        (("action_hull_theorem", "slow_incoming_missing_rank"), 64),
        (("action_hull_theorem", "K617_graph_is_A_invariant"), True),
        (("ownership_and_typing", "spectral_vector_components_are_action_derived"), False),
        (("ownership_and_typing", "action_derived_vector_split_owns_mixed_hessian_coupling"), True),
        (("ownership_and_typing", "matching_half_bilinear_packet_constructed"), True),
        (("ownership_and_typing", "equal_rank_identifies_historical_and_current_hulls"), True),
        (("ownership_and_typing", "bounded_route_action_owned"), True),
        (("revival_gate", "corrected_carrier_supplies_nontrivial_diagnostic_module"), False),
        (("revival_gate", "corrected_carrier_revives_historical_bounded_graph_as_action_subsystem"), True),
        (("revival_gate", "K616_vector_projection_ownership_narrowed"), False),
        (("revival_gate", "K616_core_unsplit_packet_obstruction_retracted"), True),
        (("decision", "K617_nontrivial_descent_retracted"), True),
        (("decision", "K615_frozen_zero_form_obstruction_retracted"), True),
        (("decision", "prior_unrestricted_Euler_route_kill_retracted"), True),
        (("decision", "rank384_coincidence_promoted_to_identity"), True),
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
