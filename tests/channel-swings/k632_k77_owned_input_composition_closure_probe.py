#!/usr/bin/env python3
"""Independent controls and hostile mutations for K632."""

from __future__ import annotations

import copy
import json

from k632_k77_owned_input_composition_closure import build


def controls(p: dict) -> list[bool]:
    t = p["closure_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    c = p["reachable_signature_counts"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["allowed_operations"]) == 5,
        p["allowed_operations"][0]["operation"] == "action_polynomial_or_full_commutant_on_E",
        len(p["forbidden_generation_rules"]) == 6,
        p["forbidden_generation_rules"][0] == "no ownership upgrade under composition",
        len(p["strongest_compositions"]) == 6,
        all(row["target_reached"] is False for row in p["strongest_compositions"]),
        all(row["failure"] for row in p["strongest_compositions"]),
        c["owned_nondegenerate_E_512_to_E_512_dual_Grams"] == 0,
        c["owned_V_128_to_V_128_endomorphisms"] == 0,
        c["owned_nonzero_stationary_odd_adapters_with_Riesz_and_domain"] == 0,
        c["V_128_to_V_128_dual_pullback_forms"] == 2,
        t["current_serialized_operation_set_exhausted"] is True,
        t["owned_ambient_Gram_reachable"] is False,
        t["owned_source_domain_endomorphism_reachable"] is False,
        t["owned_stationary_odd_adapter_with_Riesz_and_domain_reachable"] is False,
        t["nondegenerate_unowned_source_pullback_forms_reachable"] is True,
        t["factorized_action_complex_reachable"] is True,
        t["post_K630_dependency_requires_genuinely_new_owned_input"] is True,
        t["universal_future_action_no_go"] is False,
        o["K590_factorized_completion_retracted"] is False,
        o["K614_source_owned_injection_retracted"] is False,
        o["K617_historical_descent_retracted"] is False,
        o["K625_H_Sigma_retracted"] is False,
        o["K629_K630_family_obstruction_retracted"] is False,
        o["selected_source_action_rejected"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        d["composition_loophole_closed_for_current_serialized_objects"] is True,
    ]


def set_path(p: dict, path: tuple[object, ...], value: object) -> None:
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
        (("allowed_operations", 0, "operation"), "arbitrary_isomorphism"),
        (("forbidden_generation_rules", 0), "ownership may strengthen"),
        (("strongest_compositions", 0, "target_reached"), True),
        (("strongest_compositions", 0, "failure"), ""),
        (("reachable_signature_counts", "owned_nondegenerate_E_512_to_E_512_dual_Grams"), 1),
        (("reachable_signature_counts", "owned_V_128_to_V_128_endomorphisms"), 1),
        (("reachable_signature_counts", "owned_nonzero_stationary_odd_adapters_with_Riesz_and_domain"), 1),
        (("reachable_signature_counts", "V_128_to_V_128_dual_pullback_forms"), 0),
        (("closure_theorem", "current_serialized_operation_set_exhausted"), False),
        (("closure_theorem", "owned_ambient_Gram_reachable"), True),
        (("closure_theorem", "owned_source_domain_endomorphism_reachable"), True),
        (("closure_theorem", "owned_stationary_odd_adapter_with_Riesz_and_domain_reachable"), True),
        (("closure_theorem", "nondegenerate_unowned_source_pullback_forms_reachable"), False),
        (("closure_theorem", "factorized_action_complex_reachable"), False),
        (("closure_theorem", "post_K630_dependency_requires_genuinely_new_owned_input"), False),
        (("closure_theorem", "universal_future_action_no_go"), True),
        (("ownership_reconciliation", "K590_factorized_completion_retracted"), True),
        (("ownership_reconciliation", "K614_source_owned_injection_retracted"), True),
        (("ownership_reconciliation", "K617_historical_descent_retracted"), True),
        (("ownership_reconciliation", "K625_H_Sigma_retracted"), True),
        (("ownership_reconciliation", "K629_K630_family_obstruction_retracted"), True),
        (("decision", "composition_loophole_closed_for_current_serialized_objects"), False),
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
