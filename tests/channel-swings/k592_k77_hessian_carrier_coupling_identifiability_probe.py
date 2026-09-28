#!/usr/bin/env python3
"""Independent controls and hostile mutations for K592."""

from __future__ import annotations

import copy
import json

from k592_k77_hessian_carrier_coupling_identifiability import build


def controls(payload: dict) -> list[bool]:
    native = payload["selected_native_inputs"]
    theorem = payload["theorem"]
    exact = payload["exact_controls"]
    decision = payload["decision"]
    return [
        payload["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        payload["direction"] == "observed_to_native",
        native["hessian_block_shape"] == [1470, 91],
        native["hessian_block_rank"] == 91,
        native["hessian_gram_scalar"] == "50/257049",
        native["factorized_carrier_rank"] == 512,
        native["actual_nonfactorized_third_action_jet_serialized"] is False,
        "third action jet" in theorem["identifiability"],
        "[Pi,T]=0" in theorem["typed_square"],
        exact["all_actions_share_background_hessian"] is True,
        exact["all_three_third_jets_distinct"] is True,
        exact["zero_control"]["typed_square_defect_rank"] == 0,
        exact["compatible_control"]["typed_square_defect_rank"] == 0,
        exact["hostile_exchange_control"]["typed_square_defect_rank"] == 2,
        exact["hostile_exchange_actual_commutator_rank"] == 128,
        decision["K585_K588_hessian_determines_nonfactorized_carrier_coupling"] is False,
        decision["third_action_jet_is_necessary_input"] is True,
        decision["actual_selected_third_action_jet_tested"] is False,
        decision["K590_factorized_completion_retracted"] is False,
        decision["source_action_rejected"] is False,
        payload["source_and_ledger_context"]["ledger_effect"] == "none",
        payload["target_claim"] == "NONE-NOT-A-KILL",
    ]


def valid(payload: dict) -> bool:
    return all(controls(payload))


def set_path(payload: dict, path: tuple[str, ...], value: object) -> None:
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main() -> int:
    payload = build()
    assert valid(payload)
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("selected_native_inputs", "hessian_block_shape"), [91, 1470]),
        (("selected_native_inputs", "hessian_block_rank"), 70),
        (("selected_native_inputs", "hessian_gram_scalar"), "1"),
        (("selected_native_inputs", "factorized_carrier_rank"), 256),
        (("selected_native_inputs", "actual_nonfactorized_third_action_jet_serialized"), True),
        (("theorem", "identifiability"), "The Hessian determines the coupling."),
        (("theorem", "typed_square"), "Compatibility is automatic."),
        (("exact_controls", "all_actions_share_background_hessian"), False),
        (("exact_controls", "all_three_third_jets_distinct"), False),
        (("exact_controls", "zero_control", "typed_square_defect_rank"), 1),
        (("exact_controls", "compatible_control", "typed_square_defect_rank"), 1),
        (("exact_controls", "hostile_exchange_control", "typed_square_defect_rank"), 0),
        (("exact_controls", "hostile_exchange_actual_commutator_rank"), 64),
        (("decision", "K585_K588_hessian_determines_nonfactorized_carrier_coupling"), True),
        (("decision", "third_action_jet_is_necessary_input"), False),
        (("decision", "actual_selected_third_action_jet_tested"), True),
        (("decision", "K590_factorized_completion_retracted"), True),
        (("decision", "source_action_rejected"), True),
        (("source_and_ledger_context", "ledger_effect"), "moved"),
        (("target_claim",), "SC-ACT-01"),
    ]
    rejected = 0
    for path, value in mutations:
        candidate = copy.deepcopy(payload)
        set_path(candidate, path, value)
        rejected += int(not valid(candidate))
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
