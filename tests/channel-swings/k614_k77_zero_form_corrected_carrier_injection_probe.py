#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K614."""

from __future__ import annotations

import copy
import json

from k614_k77_zero_form_corrected_carrier_injection import build


def controls(payload: dict) -> list[bool]:
    ranks = payload["cross_characteristic_rank_fingerprint"]
    theorem = payload["injection_theorem"]
    background = payload["background_and_riesz_reconciliation"]
    decision = payload["decision"]
    return [
        payload["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        payload["direction"] == "observed_to_native",
        payload["target_claim"] == "NONE-NOT-A-KILL",
        len(payload["cross_characteristic_packets"]) == 2,
        payload["cross_characteristic_packets"][0]["ranks"] == payload["cross_characteristic_packets"][1]["ranks"],
        ranks["source_zero_form"] == 128,
        ranks["corrected_image"] == 128,
        ranks["fast_projection"] == 128,
        ranks["slow_projection"] == 128,
        ranks["incoming_projection"] == 128,
        ranks["outgoing_projection"] == 128,
        [ranks[key] for key in ("fast_incoming_projection", "fast_outgoing_projection", "slow_incoming_projection", "slow_outgoing_projection")] == [128, 128, 64, 64],
        theorem["source_owned_zero_form_field"] is True,
        theorem["image_lies_in_corrected_carrier"] is True,
        theorem["incoming_projection_is_injective"] is True,
        theorem["outgoing_projection_is_injective"] is True,
        theorem["fast_projection_is_injective"] is True,
        theorem["slow_projection_is_injective"] is True,
        theorem["all_four_action_spectral_sign_blocks_met"] is True,
        theorem["every_nonzero_zero_form_value_has_nonzero_incoming_and_outgoing_components"] is True,
        theorem["field_space_is_not_a_selected_field_value"] is True,
        background["active_background"] == "zero fermion",
        background["injection_evaluated_on_active_background_is_zero"] is True,
        background["zero_fermion_current_rank"] == 0,
        background["zero_fermion_mixed_hessian_rank"] == 0,
        background["nonzero_fermion_stationary_solution_owned"] is False,
        background["K441_action_Riesz_return_for_zero_form_background_owned"] is False,
        background["K596_actual_rank_one_packet_released"] is False,
        background["K598_actual_covariant_packet_released"] is False,
        decision["K613_hypothetical_field_to_carrier_map_narrowed"] is True,
        decision["source_owned_zero_form_injection_constructed"] is True,
        decision["action_owned_nonzero_background_constructed"] is False,
        decision["actual_action_owned_soldering_constructed"] is False,
        decision["K590_factorized_completion_retracted"] is False,
        decision["K613_central_parity_obstruction_retracted"] is False,
        decision["selected_source_action_rejected"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def set_path(payload: dict, path: tuple[object, ...], value: object) -> None:
    cursor = payload
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
        (("cross_characteristic_rank_fingerprint", "corrected_image"), 127),
        (("cross_characteristic_rank_fingerprint", "fast_projection"), 127),
        (("cross_characteristic_rank_fingerprint", "slow_projection"), 127),
        (("cross_characteristic_rank_fingerprint", "incoming_projection"), 127),
        (("cross_characteristic_rank_fingerprint", "outgoing_projection"), 127),
        (("cross_characteristic_rank_fingerprint", "slow_incoming_projection"), 0),
        (("injection_theorem", "source_owned_zero_form_field"), False),
        (("injection_theorem", "image_lies_in_corrected_carrier"), False),
        (("injection_theorem", "incoming_projection_is_injective"), False),
        (("injection_theorem", "outgoing_projection_is_injective"), False),
        (("injection_theorem", "field_space_is_not_a_selected_field_value"), False),
        (("background_and_riesz_reconciliation", "injection_evaluated_on_active_background_is_zero"), False),
        (("background_and_riesz_reconciliation", "zero_fermion_current_rank"), 1),
        (("background_and_riesz_reconciliation", "zero_fermion_mixed_hessian_rank"), 1),
        (("background_and_riesz_reconciliation", "nonzero_fermion_stationary_solution_owned"), True),
        (("background_and_riesz_reconciliation", "K441_action_Riesz_return_for_zero_form_background_owned"), True),
        (("background_and_riesz_reconciliation", "K596_actual_rank_one_packet_released"), True),
        (("background_and_riesz_reconciliation", "K598_actual_covariant_packet_released"), True),
        (("decision", "source_owned_zero_form_injection_constructed"), False),
        (("decision", "action_owned_nonzero_background_constructed"), True),
        (("decision", "actual_action_owned_soldering_constructed"), True),
        (("decision", "K590_factorized_completion_retracted"), True),
        (("decision", "K613_central_parity_obstruction_retracted"), True),
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
