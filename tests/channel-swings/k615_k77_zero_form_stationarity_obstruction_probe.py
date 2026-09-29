#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K615."""

from __future__ import annotations

import copy
import json

from k615_k77_zero_form_stationarity_obstruction import build


def controls(p: dict) -> list[bool]:
    r = p["rank_fingerprint"]
    f = p["fibrewise_stationarity_theorem"]
    d = p["closed_domain_stationarity_theorem"]
    z = p["stationarity_riesz_dichotomy"]
    q = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["ranks"] == p["cross_characteristic_packets"][1]["ranks"],
        r["zero_form_injection"] == 128,
        r["action_euler_image"] == 128,
        r["outgoing_zero_form"] == 128,
        r["incoming_zero_form"] == 128,
        r["outgoing_euler"] == 128,
        r["incoming_euler"] == 128,
        r["fast_euler"] == 128,
        r["slow_euler"] == 128,
        f["kernel_dimension"] == 0,
        f["only_solution"] == "v=0",
        f["nonzero_zero_form_value_has_nonzero_euler_covector"] is True,
        f["nonzero_zero_form_value_is_stationary"] is False,
        d["K440_kernel_dimension"] == 0,
        d["K440_cokernel_dimension"] == 0,
        d["four_source_fermion_slots_direct_sum_kernel_dimension"] == 0,
        d["moving_lower_order_or_nonlinear_operator_covered"] is False,
        d["source_selected_physical_boundary_covered"] is False,
        z["nonzero_stationary_K441_Riesz_packet_released"] is False,
        q["K614_field_injection_retracted"] is False,
        q["K440_green_domain_retracted"] is False,
        q["nonzero_stationary_zero_form_in_K440_model_exists"] is False,
        q["four_field_frozen_stationary_background_nonzero"] is False,
        q["moving_nonlinear_nonzero_background_excluded"] is False,
        q["selected_source_action_rejected"] is False,
        q["K596_K598_released_by_stationarity"] is False,
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
        (("rank_fingerprint", "action_euler_image"), 127),
        (("rank_fingerprint", "outgoing_zero_form"), 127),
        (("rank_fingerprint", "incoming_zero_form"), 127),
        (("rank_fingerprint", "outgoing_euler"), 127),
        (("rank_fingerprint", "incoming_euler"), 127),
        (("rank_fingerprint", "fast_euler"), 127),
        (("rank_fingerprint", "slow_euler"), 127),
        (("fibrewise_stationarity_theorem", "kernel_dimension"), 1),
        (("fibrewise_stationarity_theorem", "nonzero_zero_form_value_has_nonzero_euler_covector"), False),
        (("fibrewise_stationarity_theorem", "nonzero_zero_form_value_is_stationary"), True),
        (("closed_domain_stationarity_theorem", "K440_kernel_dimension"), 1),
        (("closed_domain_stationarity_theorem", "K440_cokernel_dimension"), 1),
        (("closed_domain_stationarity_theorem", "four_source_fermion_slots_direct_sum_kernel_dimension"), 1),
        (("closed_domain_stationarity_theorem", "moving_lower_order_or_nonlinear_operator_covered"), True),
        (("closed_domain_stationarity_theorem", "source_selected_physical_boundary_covered"), True),
        (("stationarity_riesz_dichotomy", "nonzero_stationary_K441_Riesz_packet_released"), True),
        (("decision", "K614_field_injection_retracted"), True),
        (("decision", "nonzero_stationary_zero_form_in_K440_model_exists"), True),
        (("decision", "four_field_frozen_stationary_background_nonzero"), True),
        (("decision", "moving_nonlinear_nonzero_background_excluded"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("decision", "K596_K598_released_by_stationarity"), True),
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
