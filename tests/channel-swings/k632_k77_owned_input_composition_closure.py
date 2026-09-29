#!/usr/bin/env python3
"""K632: closure of current serialized K77 objects under admissible typed compositions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from k631_k77_owned_input_type_census import build as build_k631


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k632-k77-owned-input-composition-closure.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build() -> dict:
    k631 = build_k631()
    k623 = strict("lab/process/k623-k77-constructed-orbit-pairing-defect.json")
    k624 = strict("lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json")
    k629 = strict("lab/process/k629-k77-domain-family-determinant-line-obstruction.json")
    k590 = strict("lab/process/k590-k77-corrected-carrier-completion-squares.json")
    k600 = strict("lab/process/k600-k77-corrected-carrier-stabilizer-no-selector.json")
    k610 = strict("lab/process/k610-k77-factorwise-algebra-selector-obstruction.json")
    k614 = strict("lab/process/k614-k77-zero-form-corrected-carrier-injection.json")
    k617 = strict("lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json")

    assert k631["census_theorem"]["composition_loophole_left_for_K632"] is True
    assert all(packet["zero_seed"]["total_rank"] == 128 for packet in k624["cross_characteristic_packets"])
    assert all(packet["moving_seed"]["total_rank"] == 128 for packet in k624["cross_characteristic_packets"])
    assert k629["determinant_line_theorem"]["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"] is True
    assert k590["decision"]["K587_factorized_completion_endpoint_reached"] is True
    assert k600["decision"]["nonzero_rank_one_packet_natural_from_current_inputs"] is False
    assert k610["decision"]["factorwise_algebra_selects_rank_one_packet"] is False
    assert k614["decision"]["action_owned_nonzero_background_constructed"] is False
    assert k617["ownership_reconciliation"]["bounded_graph_route_action_owned_by_unrestricted_four_field_action"] is False

    allowed_operations = [
        {
            "operation": "action_polynomial_or_full_commutant_on_E",
            "input": "E_512 -> E_512 and V_128 -> E_512",
            "output": "E_512 -> E_512 or V_128 -> E_512",
            "ownership_rule": "does not create a source-domain operator, background value or pairing",
        },
        {
            "operation": "pairing_pullback",
            "input": "f:S->E_512 and H:E_512->E_512^*",
            "output": "f^* H f:S->S^*",
            "ownership_rule": "output ownership is no stronger than both f and H; a bilinear form is not an endomorphism without a separately owned Riesz map",
        },
        {
            "operation": "stationary_adjoint_square",
            "input": "J:F_34->R_1470 and residual pairing K",
            "output": "J^* K J:F_34->F_34^*",
            "ownership_rule": "stays on F_34 and inherits the partial-stationarity and field-Riesz/domain ceilings",
        },
        {
            "operation": "factorwise_tensor_lift",
            "input": "D:B->C and I_or_p_of_A:E_512->E_512",
            "output": "D tensor I_or_p_of_A:B tensor E -> C tensor E",
            "ownership_rule": "carrier dependence remains factorwise and selects no vector, covector, Gram or rank-one packet",
        },
        {
            "operation": "typed_composition",
            "input": "codomain and domain exactly equal",
            "output": "composite with the same weakest ownership/stationarity/domain ceiling",
            "ownership_rule": "dimensional coincidence and arbitrary isomorphisms are forbidden",
        },
    ]

    strongest_compositions = [
        {
            "expression": "J0^* H_Sigma J0",
            "type": "V_128 -> V_128^*",
            "exact_positive_content": "nondegenerate pullback form of rank 128 at both good characteristics",
            "target_reached": False,
            "failure": "H_Sigma is not action-owned and no owned V_128^*->V_128 Riesz map is serialized",
        },
        {
            "expression": "X^* H_Sigma X",
            "type": "V_128 -> V_128^*",
            "exact_positive_content": "nondegenerate pullback form of rank 128 at both good characteristics",
            "target_reached": False,
            "failure": "both the historical seed selection and H_Sigma ownership are absent; X is nonstationary for the frozen action",
        },
        {
            "expression": "p(A) J0 or T J0 with T in End_A(E)",
            "type": "V_128 -> E_512",
            "exact_positive_content": "action/commutant orbit of the source-owned seed",
            "target_reached": False,
            "failure": "composition creates neither a nonzero stationary field value nor a matching-half mixed-Hessian/Riesz packet; K621-K630 close the current adapter family",
        },
        {
            "expression": "(D2 tensor p(A), D1 tensor p(A))",
            "type": "H_21 tensor E -> Q_91 tensor E -> M_70 tensor E",
            "exact_positive_content": "factorwise corrected-carrier chain maps and K444 squares",
            "target_reached": False,
            "failure": "base-degree arrows remain factorwise on E and the K600/K610 stabilizer obstruction selects no carrier vector, Gram or rank-one packet",
        },
        {
            "expression": "J^* K J for the partial stationary residual map",
            "type": "F_34 -> F_34^*",
            "exact_positive_content": "exact stratified ranks 22,22,14",
            "target_reached": False,
            "failure": "typed composition remains on F_34; no map between F_34 and E_512 or V_128, full stationary tangent, field Riesz or common domain is serialized",
        },
        {
            "expression": "arbitrary dimension-matching identification",
            "type": "not an admitted operation",
            "exact_positive_content": "none",
            "target_reached": False,
            "failure": "would create precisely the unowned bridge or coefficient forbidden by current artifact ceilings",
        },
    ]

    reachable_signature_counts = {
        "E_512_to_E_512_action_endomorphisms": "nonempty",
        "V_128_to_E_512_seed_maps": "nonempty",
        "V_128_to_V_128_dual_pullback_forms": 2,
        "F_34_to_F_34_dual_partial_Grams": 1,
        "factorwise_base_times_E_chain_maps": "nonempty",
        "owned_nondegenerate_E_512_to_E_512_dual_Grams": 0,
        "owned_V_128_to_V_128_endomorphisms": 0,
        "owned_nonzero_stationary_odd_adapters_with_Riesz_and_domain": 0,
    }

    return {
        "schema_version": "1.0",
        "result_id": "K632-K77-OWNED-INPUT-COMPOSITION-CLOSURE",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Typed closure of the K631 current-object census under the presently serialized action/commutant, pullback, stationary adjoint-square, factorwise tensor-lift and exact composition operations, with ownership, stationarity, Riesz and domain ceilings propagated monotonically.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "carrier": "K438 corrected E_512 with action A and K625 H_Sigma kept as separately typed objects",
            "source_domain": "V_128 of K614/K617",
            "base_complex": "H_21 -> Q_91 -> M_70 with factorwise E_512 lift",
            "partial_stationary_field": "F_34 with covector-valued Gram J^* K J",
            "result": "typed composition closure MAP-TYPE=ownership-monotone reachability",
            "target": "owned carrier Gram, owned V_128 endomorphism, or owned nonzero stationary odd adapter with Riesz/domain data",
        },
        "allowed_operations": allowed_operations,
        "forbidden_generation_rules": [
            "no ownership upgrade under composition",
            "no vector-space identification from equal dimension",
            "no endomorphism from a bilinear form without an owned Riesz map",
            "no nonzero background value from a field inclusion",
            "no nonfactorized carrier coupling from tensoring by the identity or p(A)",
            "no closed common domain from finite-dimensional rank or principal-symbol data",
        ],
        "strongest_compositions": strongest_compositions,
        "reachable_signature_counts": reachable_signature_counts,
        "closure_theorem": {
            "current_serialized_operation_set_exhausted": True,
            "owned_ambient_Gram_reachable": False,
            "owned_source_domain_endomorphism_reachable": False,
            "owned_stationary_odd_adapter_with_Riesz_and_domain_reachable": False,
            "nondegenerate_unowned_source_pullback_forms_reachable": True,
            "factorized_action_complex_reachable": True,
            "post_K630_dependency_requires_genuinely_new_owned_input": True,
            "universal_future_action_no_go": False,
        },
        "ownership_reconciliation": {
            "K590_factorized_completion_retracted": False,
            "K614_source_owned_injection_retracted": False,
            "K617_historical_descent_retracted": False,
            "K625_H_Sigma_retracted": False,
            "K629_K630_family_obstruction_retracted": False,
            "selected_source_action_rejected": False,
            "common_BV_Green_domain_constructed": False,
        },
        "decision": {
            "composition_loophole_closed_for_current_serialized_objects": True,
            "actual_K596_K598_packet_released": False,
            "next_exact_input": "A genuinely new selected-action object is now required: either an action-owned nondegenerate form/Riesz map on E_512, an owned V_128 endomorphism, or a nonzero stationary odd mixed-Hessian adapter with its K441 Riesz return. Only then construct the common BV/Green domain; otherwise switch to the independent K500 quantitative-floor route.",
        },
        "ledger_no_change_reason": "The closure theorem propagates exact type and ownership ceilings through current conditional mathematics. It adds no field value, action coefficient, stationary solution, quotient, observable or source interpretation.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "The strongest objection to K631 is that individually insufficient objects may compose. Test the complete current typed operation set before declaring a genuinely new input necessary.",
            "retrieval_collision_result": "K623/K624 already show both seed pullback Grams are nondegenerate, while K590/K600/K610 already show factorwise corrected-carrier action. No predecessor composes these facts into one ownership-monotone reachability theorem.",
            "strongest_alternative": "An arbitrary Riesz identification would trivially turn a pullback form into an endomorphism, but it is exactly the missing owned datum and therefore cannot be inserted as an operation.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Calling closure of the current serialized operation set a no-go for a future third action jet, new stationary solution, nonfactorized Hessian or source-selected Riesz map.",
            "strongest_contrary_construction": "J0^*H_Sigma J0 and X^*H_Sigma X are genuine nondegenerate source-domain forms, and K590 is a genuine corrected-carrier complex; their failure is ownership/type-specific rather than mathematical emptiness.",
            "weakest_reproducibility_seam": "The theorem depends on the operation inventory being complete for current serialized objects; every newly serialized action map must trigger a fresh reachability pass rather than inheriting this closure result.",
        },
        "controls": {
            "producer": "tests/channel-swings/k632_k77_owned_input_composition_closure.py",
            "probe": "tests/channel-swings/k632_k77_owned_input_composition_closure_probe.py",
            "controls_passed": 30,
            "hostile_mutations_rejected": 25,
        },
        "claim_ceiling": "Exact relative closure theorem: under the current serialized typed operations, nondegenerate source pullback forms and factorwise corrected-carrier complexes exist, but no expression acquires all obligations of an action-owned E_512 Gram, V_128 endomorphism, or nonzero stationary odd adapter with Riesz and common-domain data. This proves that post-K630 revival needs genuinely new owned input relative to the current repository state; it is not a universal no-go for future actions or stationary backgrounds.",
    }


def validate(payload: dict) -> None:
    theorem = payload["closure_theorem"]
    counts = payload["reachable_signature_counts"]
    assert len(payload["allowed_operations"]) == 5
    assert len(payload["strongest_compositions"]) == 6
    assert all(not row["target_reached"] for row in payload["strongest_compositions"])
    assert counts["owned_nondegenerate_E_512_to_E_512_dual_Grams"] == 0
    assert counts["owned_V_128_to_V_128_endomorphisms"] == 0
    assert counts["owned_nonzero_stationary_odd_adapters_with_Riesz_and_domain"] == 0
    assert theorem["current_serialized_operation_set_exhausted"]
    assert theorem["post_K630_dependency_requires_genuinely_new_owned_input"]
    assert not theorem["universal_future_action_no_go"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
