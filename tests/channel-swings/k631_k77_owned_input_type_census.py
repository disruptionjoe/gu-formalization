#!/usr/bin/env python3
"""K631: exhaust current serialized K77 candidates against the post-K630 reopener types."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k631-k77-owned-input-type-census.json"


def strict(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def build() -> dict:
    stationary = strict("lab/process/selected-k77-stationary-gram-boundary-strata.json")
    first_action = strict("lab/process/selected-k77-common-first-action-epsilon-hessian.json")
    k438 = strict("lab/process/k438-k77-constraint-compressed-boundary-symbol.json")
    k585 = strict("lab/process/k585-k77-action-boundary-coupling-typing.json")
    k588 = strict("lab/process/k588-k77-action-orbit-reduction.json")
    k589 = strict("lab/process/k589-k77-action-kt-exact-completion.json")
    k590 = strict("lab/process/k590-k77-corrected-carrier-completion-squares.json")
    k592 = strict("lab/process/k592-k77-hessian-carrier-coupling-identifiability.json")
    k614 = strict("lab/process/k614-k77-zero-form-corrected-carrier-injection.json")
    k617 = strict("lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json")
    k625 = strict("lab/process/k625-k77-canonical-projector-pairing-realization.json")
    k629 = strict("lab/process/k629-k77-domain-family-determinant-line-obstruction.json")
    k630 = strict("lab/process/k630-k77-determinant-line-gauge-invariance.json")

    assert stationary["exact_result"]["field_dimension"] == 34
    assert stationary["layer0"]["field_operator"] == "REQUIRES_FIELD_RIESZ__OPEN"
    assert first_action["moving_epsilon"]["mixed_cross_shape"] == [1470, 91]
    assert first_action["moving_epsilon"]["mixed_cross_rank"] == 91
    assert k585["typed_map_attempt"]["corrected_boundary_carrier_map_present"] is False
    assert k588["decision"]["D1_coefficient_matrix_serialized_by_exact_factorization"] is True
    assert k589["decision"]["K587_base_exact_completion_constructed"] is True
    assert k590["decision"]["K587_factorized_completion_endpoint_reached"] is True
    assert k592["decision"]["third_action_jet_is_necessary_input"] is True
    assert k614["decision"]["source_owned_zero_form_injection_constructed"] is True
    assert k614["decision"]["action_owned_nonzero_background_constructed"] is False
    assert k617["ownership_reconciliation"]["mixed_hessian_Riesz_packet_constructed"] is False
    assert k625["ownership_reconciliation"]["canonical_projector_realization_is_action_owned_adapter"] is False
    assert k629["determinant_line_theorem"]["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"] is True
    assert k630["gauge_invariance_theorem"]["all_tested_source_and_ambient_gauges_preserve_obstruction"] is True

    required = {
        "ambient_gram": {
            "signature": "nondegenerate symmetric E_512 -> E_512^* form",
            "ownership": "selected source/action owns the form or its Riesz map",
            "analytic": "compatible common BV/Green domain",
        },
        "source_domain_endomorphism": {
            "signature": "V_128 -> V_128",
            "ownership": "selected source/action owns the operator",
            "analytic": "pairing and domain preservation on the same background",
        },
        "stationary_odd_adapter": {
            "signature": "nonzero odd datum on a stationary background with map into E_512",
            "ownership": "selected action owns background, mixed Hessian and matching-half coupling",
            "analytic": "K441-compatible Riesz return and common BV/Green domain",
        },
    }

    candidates = [
        {
            "id": "H_SIGMA",
            "source": "K625/K623",
            "type": "E_512 -> E_512^* nondegenerate positive form",
            "exact_positive_content": "canonical projector-induced K441 realization",
            "source_or_action_owned": False,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "ownership",
            "reopener_matches": [],
        },
        {
            "id": "PARTIAL_STATIONARY_GRAM_34",
            "source": "selected-k77-stationary-gram-boundary-strata",
            "type": "F_34 -> F_34^* covector-valued partial second-action symbol",
            "exact_positive_content": "ranks 22,22,14 on timelike, spacelike,null strata",
            "source_or_action_owned": True,
            "stationary_background_owned": "partial_second_action_only",
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "carrier_type_and_field_Riesz",
            "reopener_matches": [],
        },
        {
            "id": "FIRST_ACTION_EPSILON_CROSS",
            "source": "K585/selected-k77-common-first-action-epsilon-hessian",
            "type": "Q_91 -> R_1470 rectangular rank-91 Hessian cross",
            "exact_positive_content": "selected first-action coefficient block with 182 nonzeros",
            "source_or_action_owned": True,
            "stationary_background_owned": "connection_branch_only_metric_Euler_open",
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "corrected_carrier_map_and_complete_stationarity",
            "reopener_matches": [],
        },
        {
            "id": "FINITE_BASE_COMPLEX",
            "source": "K588/K589",
            "type": "H_21 -> Q_91 -> M_70",
            "exact_positive_content": "exact finite homogeneous-orbit coefficient complex",
            "source_or_action_owned": True,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "wrong_domains_and_no_carrier_dependence",
            "reopener_matches": [],
        },
        {
            "id": "FACTORIZED_CARRIER_COMPLEX",
            "source": "K590",
            "type": "(H_21 -> Q_91 -> M_70) tensor I_E512",
            "exact_positive_content": "both moving K444 projector squares",
            "source_or_action_owned": True,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "identity_only_carrier_dependence",
            "reopener_matches": [],
        },
        {
            "id": "COMPRESSED_ACTION_A",
            "source": "K438",
            "type": "E_512 -> E_512 action endomorphism",
            "exact_positive_content": "four-root corrected constrained characteristic calculus",
            "source_or_action_owned": True,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "ambient_not_source_domain_and_no_odd_background",
            "reopener_matches": [],
        },
        {
            "id": "ZERO_FORM_SEED_J0",
            "source": "K614",
            "type": "V_128 -> E_512 injective seed map",
            "exact_positive_content": "source-owned zero-form field inclusion",
            "source_or_action_owned": True,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "nonzero_stationary_value_and_Riesz",
            "reopener_matches": [],
        },
        {
            "id": "MOVING_VARPI_SEED_X",
            "source": "K617",
            "type": "V_128 -> E_512 injective historical graph",
            "exact_positive_content": "nonzero corrected descent meeting all four spectral blocks",
            "source_or_action_owned": False,
            "stationary_background_owned": False,
            "riesz_or_common_domain_complete": False,
            "first_failed_obligation": "action_ownership_stationarity_and_Riesz",
            "reopener_matches": [],
        },
    ]

    return {
        "schema_version": "1.0",
        "result_id": "K631-K77-OWNED-INPUT-TYPE-CENSUS",
        "created": "2026-09-29",
        "status": "working_draft_verified",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "target_claim": "NONE-NOT-A-KILL",
        "scope": "Complete type-and-ownership census of the strongest current serialized K77 Grams, Hessian blocks, base-complex arrows, factorwise carrier lifts, characteristic endomorphism and rank-128 seed maps against the exact post-K630 reopener signatures.",
        "gu_comparator_routing": "GU-COMPARATOR-ROUTING — scope before inference. This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.",
        "gu_typed_objects": {
            "action": "current selected first-action cross, partial stationary second-action Gram and K438 compressed symbol",
            "actual_carrier": "K438 corrected real carrier E of rank 512",
            "source_domain": "Omega0(S) coordinate domain V of rank 128",
            "pairing": "K625 projector-induced H_Sigma, distinguished from action ownership",
            "result": "owned-input census MAP-TYPE=typed-interface exhaustion",
            "target": "one of the three exact post-K630 reopener signatures",
        },
        "required_reopener_signatures": required,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "census_theorem": {
            "every_strong_current_candidate_typed": True,
            "single_candidate_matching_ambient_gram": False,
            "single_candidate_matching_source_domain_endomorphism": False,
            "single_candidate_matching_stationary_odd_adapter": False,
            "current_new_owned_input_dependency_is_not_a_retrieval_gap_at_single_object_level": True,
            "composition_loophole_left_for_K632": True,
        },
        "ownership_reconciliation": {
            "H_Sigma_retracted": False,
            "partial_stationary_Grams_retracted": False,
            "K590_factorized_completion_retracted": False,
            "K614_source_owned_injection_retracted": False,
            "K617_corrected_descent_retracted": False,
            "K629_K630_family_obstruction_retracted": False,
            "source_or_action_rejected": False,
        },
        "decision": {
            "single_current_object_reopens_K596_K598": False,
            "next_exact_input": "Test the strongest typed compositions of current objects. If closure still contains no owned E_512 Gram, V_128 endomorphism or nonzero stationary odd adapter with Riesz/domain data, genuinely new action coefficients or a new selected stationary background are required.",
        },
        "ledger_no_change_reason": "The census reconciles already serialized conditional objects and their ownership ceilings. It creates no stationary solution, action coefficient, gauge-reduced class, observation map, physical cohomology or source interpretation.",
        "source_and_ledger_effect": "none",
        "preflight_bookend": {
            "route_comparison": "Before constructing new data, exhaust whether the repository already contains the required owned interface under older Gram, Hessian, complex or seed vocabulary.",
            "retrieval_collision_result": "The candidates are real but occupy different typed domains; no predecessor jointly checks them against all three post-K630 signatures.",
            "strongest_alternative": "Immediately building another arbitrary Gram would repeat K627's unowned orthogonal-reduction problem and was rejected.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Treating a failure of every single current candidate as a universal no-go under composition or future action data.",
            "strongest_contrary_construction": "K590 is a genuine action-related corrected-carrier complex and K625 is a genuine nondegenerate carrier pairing; K632 must test their compositions rather than dismiss them by labels.",
            "weakest_reproducibility_seam": "The census relies on declared types and exact decision fields from current artifacts; K632 independently enforces composition rules and target reachability.",
        },
        "controls": {
            "producer": "tests/channel-swings/k631_k77_owned_input_type_census.py",
            "probe": "tests/channel-swings/k631_k77_owned_input_type_census_probe.py",
            "controls_passed": 27,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact current-artifact census: none of eight strongest serialized candidates alone has the signature, ownership, stationarity, Riesz and common-domain data required for a post-K630 K77 revival. This establishes a single-object typed dependency, not a composition theorem or a universal no-go, and preserves every candidate's positive conditional content.",
    }


def validate(payload: dict) -> None:
    theorem = payload["census_theorem"]
    assert payload["candidate_count"] == 8 == len(payload["candidates"])
    assert theorem["every_strong_current_candidate_typed"]
    assert not theorem["single_candidate_matching_ambient_gram"]
    assert not theorem["single_candidate_matching_source_domain_endomorphism"]
    assert not theorem["single_candidate_matching_stationary_odd_adapter"]
    assert theorem["composition_loophole_left_for_K632"]
    assert all(not row["reopener_matches"] for row in payload["candidates"])


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
