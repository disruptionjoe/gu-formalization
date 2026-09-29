#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K617."""

from __future__ import annotations

import copy
import json

from k617_k77_moving_varpi_corrected_carrier_descent import build


def controls(p: dict) -> list[bool]:
    d = p["descent_theorem"]
    o = p["ownership_reconciliation"]
    q = p["decision"]
    rows = p["cross_characteristic_rows"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["rows"] == p["cross_characteristic_packets"][1]["rows"],
        set(rows) == {"row_pin", "column_pin"},
        all(row["corrected_graph_rank"] == 128 for row in rows.values()),
        all(row["removed_trace_rank"] == 128 for row in rows.values()),
        all(row["corrected_zero_seed_join_rank"] == 256 for row in rows.values()),
        all(row["corrected_zero_seed_intersection_rank"] == 0 for row in rows.values()),
        all(row["frozen_action_residual_rank"] == 128 for row in rows.values()),
        d["both_pin_candidates_descend_injectively"] is True,
        d["pin_candidates_become_identical_after_correction"] is True,
        d["corrected_graph_equals_K614_zero_seed"] is False,
        d["all_four_frozen_spectral_sign_blocks_met"] is True,
        d["stationary_for_frozen_K438_action"] is False,
        o["historical_graph_is_source_selected"] is False,
        o["historical_graph_is_repository_constructed"] is True,
        o["bounded_graph_route_action_owned_by_unrestricted_four_field_action"] is False,
        o["corrected_descent_reverses_prior_action_ownership_kill"] is False,
        o["moving_differential_BV_Green_domain_constructed"] is False,
        o["mixed_hessian_Riesz_packet_constructed"] is False,
        q["K615_frozen_stationarity_obstruction_retracted"] is False,
        q["K616_unsplit_packet_obstruction_retracted"] is False,
        q["moving_graph_has_nontrivial_corrected_descent"] is True,
        q["moving_graph_revives_bounded_action_owned_route"] is False,
        q["selected_source_action_rejected"] is False,
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
        (("cross_characteristic_rows", "row_pin", "corrected_graph_rank"), 127),
        (("cross_characteristic_rows", "column_pin", "removed_trace_rank"), 127),
        (("cross_characteristic_rows", "row_pin", "corrected_zero_seed_join_rank"), 128),
        (("cross_characteristic_rows", "column_pin", "corrected_zero_seed_intersection_rank"), 128),
        (("cross_characteristic_rows", "row_pin", "frozen_action_residual_rank"), 0),
        (("descent_theorem", "both_pin_candidates_descend_injectively"), False),
        (("descent_theorem", "pin_candidates_become_identical_after_correction"), False),
        (("descent_theorem", "corrected_graph_equals_K614_zero_seed"), True),
        (("descent_theorem", "all_four_frozen_spectral_sign_blocks_met"), False),
        (("descent_theorem", "stationary_for_frozen_K438_action"), True),
        (("ownership_reconciliation", "historical_graph_is_source_selected"), True),
        (("ownership_reconciliation", "historical_graph_is_repository_constructed"), False),
        (("ownership_reconciliation", "bounded_graph_route_action_owned_by_unrestricted_four_field_action"), True),
        (("ownership_reconciliation", "corrected_descent_reverses_prior_action_ownership_kill"), True),
        (("ownership_reconciliation", "moving_differential_BV_Green_domain_constructed"), True),
        (("ownership_reconciliation", "mixed_hessian_Riesz_packet_constructed"), True),
        (("decision", "K615_frozen_stationarity_obstruction_retracted"), True),
        (("decision", "K616_unsplit_packet_obstruction_retracted"), True),
        (("decision", "moving_graph_has_nontrivial_corrected_descent"), False),
        (("decision", "moving_graph_revives_bounded_action_owned_route"), True),
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
