#!/usr/bin/env python3
"""Fail-closed audit for CURRENT-STATE live-versus-historical frontier custody."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "CURRENT-STATE.yaml"
REGISTRY = ROOT / "lab/process/current-frontier-semantic-currency.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_inputs() -> dict:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    basis = registry["basis"]
    return {
        "current": yaml.safe_load(CURRENT.read_text(encoding="utf-8")),
        "registry": registry,
        "agenda": json.loads((ROOT / basis["research_agenda"]["path"]).read_text()),
        "dispositions": json.loads(
            (ROOT / basis["phenomenology_disposition_register"]["path"]).read_text()
        ),
        "b2": json.loads((ROOT / basis["b2_frontier"]["path"]).read_text()),
        "qualification": json.loads(
            (ROOT / basis["w154_w229_qualification"]["path"]).read_text()
        ),
        "b5_artifact": (ROOT / registry["b5_agenda_currency"]["result_ref"]).read_text(),
        "k633": json.loads((ROOT / "lab/process/k633-k77-zero-form-polynomial-endomorphism-obstruction.json").read_text()),
        "k634": json.loads((ROOT / "lab/process/k634-k500-equivalent-domain-repair-obstruction.json").read_text()),
        "k631": json.loads((ROOT / "lab/process/k631-k77-owned-input-type-census.json").read_text()),
        "k632": json.loads((ROOT / "lab/process/k632-k77-owned-input-composition-closure.json").read_text()),
        "k629": json.loads((ROOT / "lab/process/k629-k77-domain-family-determinant-line-obstruction.json").read_text()),
        "k630": json.loads((ROOT / "lab/process/k630-k77-determinant-line-gauge-invariance.json").read_text()),
        "k627": json.loads((ROOT / "lab/process/k627-k77-block-gauge-positive-pairing-nonselection.json").read_text()),
        "k628": json.loads((ROOT / "lab/process/k628-k77-k622-domain-map-pairing-obstruction.json").read_text()),
        "k625": json.loads((ROOT / "lab/process/k625-k77-canonical-projector-pairing-realization.json").read_text()),
        "k626": json.loads((ROOT / "lab/process/k626-k77-ambient-pairing-embedding-gauge.json").read_text()),
        "k623": json.loads((ROOT / "lab/process/k623-k77-constructed-orbit-pairing-defect.json").read_text()),
        "k624": json.loads((ROOT / "lab/process/k624-k77-pairing-preserving-commutant-orbit-obstruction.json").read_text()),
        "k621": json.loads((ROOT / "lab/process/k621-k77-full-action-commutant-seed-adapter-obstruction.json").read_text()),
        "k622": json.loads((ROOT / "lab/process/k622-k77-domain-reparameterized-commutant-orbit.json").read_text()),
        "k619": json.loads((ROOT / "lab/process/k619-k77-zero-form-moving-graph-common-action-module.json").read_text()),
        "k620": json.loads((ROOT / "lab/process/k620-k77-action-functional-calculus-selection-obstruction.json").read_text()),
        "k617": json.loads((ROOT / "lab/process/k617-k77-moving-varpi-corrected-carrier-descent.json").read_text()),
        "k618": json.loads((ROOT / "lab/process/k618-k77-moving-varpi-corrected-action-hull.json").read_text()),
        "k615": json.loads((ROOT / "lab/process/k615-k77-zero-form-stationarity-obstruction.json").read_text()),
        "k616": json.loads((ROOT / "lab/process/k616-k77-unsplit-rank-one-transport-obstruction.json").read_text()),
        "k614": json.loads((ROOT / "lab/process/k614-k77-zero-form-corrected-carrier-injection.json").read_text()),
        "k612": json.loads((ROOT / "lab/process/k612-k139-quantitative-semibound-custody-audit.json").read_text()),
        "k613": json.loads((ROOT / "lab/process/k613-k77-central-parity-tensor-network-obstruction.json").read_text()),
    }


def audit(data: dict, check_digests: bool = True) -> list[str]:
    failures: list[str] = []
    current = data["current"]
    registry = data["registry"]
    surface = registry["surface_contract"]
    live = current.get(surface["live_key"])
    history = current.get(surface["history_key"])

    def check(ok: bool, message: str) -> None:
        if not ok:
            failures.append(message)

    check(isinstance(live, str) and bool(live.strip()), "live next_condition missing")
    check(isinstance(history, str) and bool(history.strip()), "prior_conditions history missing")
    if isinstance(live, str):
        check("K77 route" in live, "K77 nonfactorized route missing")
        check("K633" in live and "scalar stabilizer" in live,
              "K77 polynomial source-seed stabilizer missing")
        check("outside `R[A]`" in live and "full-commutant" in live,
              "K77 polynomial-scope reopener missing")
        check("K631" in live and "K632" in live and "current typed operation closure" in live,
              "K77 current-owned-input closure missing")
        check("J0^* H_Sigma J0" in live and "X^* H_Sigma X" in live,
              "K77 nondegenerate pullback-form custody missing")
        check("K627" in live and "41,216" in live and "orthogonal reduction" in live,
              "K77 block-gauge pairing nonselection missing")
        check("K625" in live and "H_Sigma" in live,
              "K77 canonical projector point missing")
        check("K629--K630" in live, "K77 family-wide determinant-line predecessor missing")
        check("v0.163--v0.165" in live and "already banked" in live,
              "K77 completed unrestricted/BV route repeat fence missing")
        check("mixed Hessian" in live and "common BV/Green" in live,
              "K77 current reopener/ownership fence missing")
        check("universal" in live and "no-go" in live,
              "K77 relative-closure scope fence missing")
        check("K614" in live and "K617" in live and "K625" in live,
              "K77 current positive-content preservation missing")
        check("K596/K598" in live, "K77 unsplit-packet interface missing")
        check("nonzero stationary moving background" in live and "independently action-owned" in live,
              "K77 moving reopener missing")
        check("K596" in live and "K598" in live,
              "K77 discriminator/transport succession missing")
        check("K609" in live and "below 1/3" in live,
              "K500 complete leakage route missing")
        check("K612" in live and "cancelled-core" in live,
              "K500 quantitative-custody obstruction missing")
        check("K634" in live and "equivalent-norm" in live and "bounded-correlation" in live,
              "K500 equivalent-domain closure missing")
        check("genuinely non-equivalent cancellation domain" in live,
              "K500 surviving topology class missing")
        check("cancellation-adapted" in live,
              "live complete-complement route missing")
        check("25/9" in live, "live residual target missing")
        check("shifted-form residual or spectral-error bound" in live,
              "live K152 claim ceiling missing")
        for marker in surface["stale_live_markers_forbidden"]:
            check(marker not in live, f"stale marker remains live: {marker}")
    if isinstance(history, str):
        check("25 terminal rows and 66 open rows" in history, "historical 25/66 condition lost")
        check("b2_selectable=false" in history, "historical B2 gate condition lost")
    summary = current.get("current_result", {}).get("summary", "")
    check("K633--K634 advance two independent post-K632 fronts" in summary,
          "current K633--K634 result lost")
    check("K631--K632 prove that the post-K630 demand for new owned input" in summary,
          "current K631--K632 result lost")
    check("K629--K630 close the alternative K622 domain-map family" in summary,
          "current K629--K630 predecessor lost")
    check("K627--K628 sharpen the ambient-pairing result" in summary,
          "current K627--K628 result lost")
    check("K625--K626 resolve the ambient-pairing seam" in summary,
          "current K625--K626 result lost")
    check("K623--K624 close the projector-induced pairing repair" in summary,
          "current K623--K624 result lost")
    check("K621--K622 classify the complete nonpolynomial commutant escape" in summary,
          "current K621--K622 result lost")
    check("K619--K620 compose K614's source-owned zero-form seed" in summary,
          "current K619--K620 result lost")
    check("K617--K618 test the strongest already-owned moving-background candidate" in summary,
          "current K617--K618 result lost")
    check("K615--K616 close K614's natural frozen-background successor" in summary,
          "current K615--K616 result lost")
    check("K614 closes the map half of K613's cheapest odd-data reopener" in summary,
          "current K614 result lost")
    check("K612--K613 close two post-K611/K610 extraction routes" in summary,
          "current K612--K613 result lost")
    check("no named" in summary and "floor" in summary,
          "current claim ceiling lost")

    question = current.get("current_question", "")
    check(
        registry["live_frontier"]["current_question_contains"] in question,
        "current_question disagrees with live frontier",
    )

    disposition = data["dispositions"]["exhaustion_evaluation"]
    expected = registry["basis"]["phenomenology_disposition_register"]
    for key in ("terminal_rows", "open_rows", "exhausted", "b2_selectable"):
        check(disposition.get(key) == expected[key], f"disposition mismatch: {key}")

    root = data["qualification"]["root_candidate_rebuild"]
    qual = data["qualification"]["admission_result"]
    check(root.get("current_named_root_candidate_set") == [], "named B2 root is not empty")
    check(
        root.get("state") == registry["basis"]["w154_w229_qualification"]["root_candidate_state"],
        "root-candidate state mismatch",
    )
    check(qual.get("candidate_admitted") is False, "W154/W229 unexpectedly admitted")

    check(
        "polynomial route"
        in data["agenda"].get("latest_result_2026_09_29_k633_k634", ""),
        "agenda K633--K634 result is not current",
    )
    check(
        "eight strongest current serialized K77 candidates"
        in data["agenda"].get("latest_result_2026_09_29_k631_k632", ""),
        "agenda K631--K632 result is not current",
    )
    check(
        "8,192-dimensional family"
        in data["agenda"].get("latest_result_2026_09_29_k629_k630", ""),
        "agenda K629--K630 result is not current",
    )
    check(
        "41,216-dimensional homogeneous space"
        in data["agenda"].get("latest_result_2026_09_29_k627_k628", ""),
        "agenda K627--K628 result is not current",
    )
    check(
        "ambient-embedding gauge"
        in data["agenda"].get("latest_result_2026_09_29_k625_k626", ""),
        "agenda K625--K626 result is not current",
    )
    check(
        "pullback Gram forms" in data["agenda"].get("latest_result_2026_09_29_k623_k624", ""),
        "agenda K623--K624 result is not current",
    )
    check(
        "full K438 action commutant"
        in data["agenda"].get("latest_result_2026_09_29_k621_k622", ""),
        "agenda K621--K622 result is not current",
    )
    check(
        "same rank-384 K438 module"
        in data["agenda"].get("latest_result_2026_09_29_k619_k620", ""),
        "agenda K619--K620 result is not current",
    )
    check(
        "Krylov ranks are 128,256,384,384,384"
        in data["agenda"].get("latest_result_2026_09_29_k617_k618", ""),
        "agenda K617--K618 result is not current",
    )
    check(
        "rank-two K596 defect" in data["agenda"].get("latest_result_2026_09_29_k615_k616", ""),
        "agenda K615--K616 result is not current",
    )
    check(
        "rank-128 zero-form inclusion" in data["agenda"].get("latest_result_2026_09_29_k614", ""),
        "agenda K614 result is not current",
    )
    check(
        "central parity" in data["agenda"].get("latest_result_2026_09_29_k612_k613", ""),
        "agenda K612--K613 result is not current",
    )
    check(
        "K600 proves" in data["agenda"].get("latest_result_2026_09_28_k600_k601", ""),
        "agenda K600--K601 result is not current",
    )
    check(
        "109,732" in data["agenda"].get("latest_result_2026_09_28_k602_k603", ""),
        "agenda K602--K603 result is not current",
    )
    check(
        "minimum nonzero carrier-idempotent rank is 64"
        in data["agenda"].get("latest_result_2026_09_28_k608_k610", ""),
        "agenda K77 route is not current",
    )
    check(
        "uniformly below 1/3"
        in data["agenda"].get("latest_result_2026_09_28_k608_k610", ""),
        "agenda K500 route is not current",
    )
    check(
        "operator product is ill-typed"
        in data["agenda"].get("latest_result_2026_09_29_k611", ""),
        "agenda K611 floor obstruction is not current",
    )
    check(
        "41,063 exact determinant-simplex classes"
        in data["agenda"].get("latest_result_2026_09_28_k604_k605", ""),
        "agenda K604--K605 result is not current",
    )
    check(
        "1,614 positive diagonal self norms"
        in data["agenda"].get("latest_result_2026_09_28_k606_k607", ""),
        "agenda K606--K607 result is not current",
    )

    b5 = next(
        item for item in data["agenda"]["work_items"]
        if item["id"] == registry["b5_agenda_currency"]["work_item"]
    )
    b5_contract = registry["b5_agenda_currency"]
    check(b5["state"] == b5_contract["state"], "B5 agenda state is stale")
    check("RB6 recertification and the full-20 Gram-adjoint wave completed" in b5["latest_result"],
          "B5 latest result does not retire RB6/Wave One")
    check("EXTERNAL-VIA-GRAM" in b5["latest_result"],
          "B5 graph-mixing branch ceiling lost")
    check(b5_contract["live_reopener"] in b5["next_swing"],
          "B5 live reopener missing")
    check("Do not repeat RB6 recertification" in b5["next_swing"],
          "B5 completed work is not forbidden as a repeat")
    check("odd rank-128 spinor" in b5["current_authority"],
          "B5 boundary multiplier typing lost")
    check("source-native `B5-MIDDLE-DIFFERENTIAL` row remains" in data["b5_artifact"],
          "B5 source-native/independent boundary lost")
    check("## Hostile review and ceiling" in data["b5_artifact"],
          "B5 currency hostile review missing")

    check(data["b2"]["basis"]["terminal_rows"] == 91, "B2 basis terminal count moved")
    check(data["b2"]["basis"]["b2_selectable"] is True, "B2 selectability history moved")
    check(all(value is False for value in registry["protected_effects"].values()),
          "protected movement field changed")

    k633 = data["k633"]
    k633_t = k633["stabilizer_theorem"]
    k633_o = k633["ownership_reconciliation"]
    k633_d = k633["decision"]
    check(len(k633["cross_characteristic_packets"]) == 2,
          "K633 characteristic packet count moved")
    check(all(packet["seed_action_seed_join_rank"] == 256 and
              packet["nonconstant_quotient_coefficient_rank"] == 3 and
              packet["nonconstant_stabilizer_nullity"] == 0
              for packet in k633["cross_characteristic_packets"]),
          "K633 quotient fingerprint moved")
    check(k633_t["polynomial_stabilizer_dimension"] == 1 and
          k633_t["polynomial_stabilizer_basis"] == ["identity"] and
          k633_t["every_induced_source_endomorphism_is_scalar"],
          "K633 stabilizer theorem moved")
    check(not k633_t["nontrivial_owned_source_endomorphism_obtained"] and
          not k633_o["arbitrary_commutant_or_mixed_hessian_excluded"],
          "K633 ownership or scope ceiling moved")
    check(k633_d["frozen_action_polynomial_route_to_new_V128_endomorphism_closed"] and
          not any((k633_d["independently_owned_V128_endomorphism_found"],
                   k633_d["actual_K596_K598_packet_released"],
                   k633_d["selected_source_action_rejected"])),
          "K633 decision boundary moved")

    k634 = data["k634"]
    k634_t = k634["equivalent_norm_theorem"]
    k634_c = k634["bounded_correlation_corollary"]
    k634_s = k634["surviving_domain_class"]
    k634_d = k634["decision"]
    check(k634["reciprocity_witness"]["lower_is_unbounded"] and
          not k634["reciprocity_witness"]["positive_diagonal_domain_with_both_requirements_exists"],
          "K634 reciprocity input moved")
    check(k634_t["underlying_domain_set_is_unchanged"] and
          k634_t["membership_of_boundary_profile_is_unchanged"] and
          k634_t["continuity_of_every_linear_trace_is_invariant"] and
          k634_t["unbounded_trace_cannot_become_bounded"],
          "K634 equivalent-norm theorem moved")
    check(not any((k634_c["chart_membership_repaired"],
                   k634_c["point_trace_continuity_repaired"],
                   k634_c["same_domain_K611_product_well_typed"],
                   k634_c["bounded_correlation_is_genuinely_new_domain"])),
          "K634 bounded-correlation corollary moved")
    check(k634_s["genuinely_non_equivalent_correlated_domain_not_excluded"] and
          k634_s["complete_matched_form_estimated_before_factor_separation_not_excluded"] and
          not k634_s["named_quantitative_floor_constructed"],
          "K634 surviving domain class moved")
    check(k634_d["bounded_equivalent_domain_repair_route_closed"] and
          not any((k634_d["all_correlated_domains_ruled_out"],
                   k634_d["named_complete_sector_floor_emitted"],
                   k634_d["K473_released"],
                   k634_d["native_K152_interval_emitted"])),
          "K634 decision boundary moved")

    k631 = data["k631"]
    k631_t = k631["census_theorem"]
    k631_o = k631["ownership_reconciliation"]
    check(k631["candidate_count"] == 8 and len(k631["candidates"]) == 8,
          "K631 candidate census moved")
    check(k631_t["every_strong_current_candidate_typed"] and
          k631_t["current_new_owned_input_dependency_is_not_a_retrieval_gap_at_single_object_level"],
          "K631 census theorem moved")
    check(not any((k631_t["single_candidate_matching_ambient_gram"],
                   k631_t["single_candidate_matching_source_domain_endomorphism"],
                   k631_t["single_candidate_matching_stationary_odd_adapter"])),
          "K631 reopener invented")
    check(k631_t["composition_loophole_left_for_K632"] and
          not any((k631_o["H_Sigma_retracted"], k631_o["K590_factorized_completion_retracted"],
                   k631_o["K614_source_owned_injection_retracted"],
                   k631_o["K617_corrected_descent_retracted"],
                   k631_o["K629_K630_family_obstruction_retracted"],
                   k631_o["source_or_action_rejected"])),
          "K631 ownership/continuation boundary moved")

    k632 = data["k632"]
    k632_t = k632["closure_theorem"]
    k632_o = k632["ownership_reconciliation"]
    k632_d = k632["decision"]
    check(k632_t["current_serialized_operation_set_exhausted"] and
          k632_t["post_K630_dependency_requires_genuinely_new_owned_input"],
          "K632 closure theorem moved")
    check(not any((k632_t["owned_ambient_Gram_reachable"],
                   k632_t["owned_source_domain_endomorphism_reachable"],
                   k632_t["owned_stationary_odd_adapter_with_Riesz_and_domain_reachable"],
                   k632_t["universal_future_action_no_go"])),
          "K632 target or universal no-go invented")
    check(k632_t["nondegenerate_unowned_source_pullback_forms_reachable"] and
          k632_t["factorized_action_complex_reachable"],
          "K632 positive current content lost")
    check(k632_d["composition_loophole_closed_for_current_serialized_objects"] and
          not k632_d["actual_K596_K598_packet_released"],
          "K632 decision boundary moved")
    check(not any((k632_o["K590_factorized_completion_retracted"],
                   k632_o["K614_source_owned_injection_retracted"],
                   k632_o["K617_historical_descent_retracted"],
                   k632_o["K625_H_Sigma_retracted"],
                   k632_o["K629_K630_family_obstruction_retracted"],
                   k632_o["selected_source_action_rejected"],
                   k632_o["common_BV_Green_domain_constructed"])),
          "K632 ownership ceiling moved")

    k629 = data["k629"]
    k629_t = k629["determinant_line_theorem"]
    k629_o = k629["ownership_reconciliation"]
    k629_d = k629["decision"]
    check(len(k629["cross_characteristic_packets"]) == 2, "K629 characteristic packet count moved")
    check(k629_t["family_parameter_group_dimension"] == 8192, "K629 family dimension moved")
    check(k629_t["combined_slow_ratio_squares"] == [949, 1004] and k629_t["both_fast_ratio_squares"] == [1, 1], "K629 determinant-line fingerprint moved")
    check(k629_t["every_K622_family_member_tested"] and k629_t["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"], "K629 family theorem moved")
    check(k629_t["K622_abstract_nonisometric_orbit_exists"] and not k629_o["K622_abstract_orbit_retracted"], "K629 abstract-orbit boundary moved")
    check(not any((k629_o["family_wide_pairing_obstruction_is_action_selection"], k629_o["source_owned_domain_map_or_Gram_constructed"], k629_o["mixed_hessian_or_stationary_background_constructed"], k629_o["common_BV_Green_domain_constructed"])), "K629 ownership ceiling moved")
    check(k629_d["broader_K622_family_pairing_orbit_decided"] and not k629_d["K622_family_contains_pairing_preserving_repair"] and not any((k629_d["actual_K596_K598_packet_released"], k629_d["selected_source_action_rejected"])), "K629 decision ceiling moved")

    k630 = data["k630"]
    k630_t = k630["gauge_invariance_theorem"]
    k630_o = k630["ownership_reconciliation"]
    k630_d = k630["decision"]
    check(len(k630["cross_characteristic_packets"]) == 2, "K630 characteristic packet count moved")
    check(k630_t["invariant_slow_ratio_squares"] == [949, 1004] and k630_t["all_tested_source_and_ambient_gauges_preserve_obstruction"], "K630 gauge fingerprint moved")
    check(not k630_t["K629_family_obstruction_is_coordinate_artifact"] and not k630_t["K628_serialized_row_basis_witness_is_required_for_K629"], "K630 coordinate/pivot theorem moved")
    check(not any((k630_o["K629_family_obstruction_retracted"], k630_o["ambient_gauge_invariance_selects_a_positive_Gram"], k630_o["source_coordinate_invariance_selects_a_source_endomorphism"], k630_o["mixed_hessian_or_stationary_background_constructed"], k630_o["common_BV_Green_domain_constructed"])), "K630 ownership ceiling moved")
    check(k630_d["K629_obstruction_survives_allowed_coordinate_changes"] and not k630_d["admissible_common_basis_or_pivot_change_reopens_K622_pairing_family"] and not any((k630_d["actual_K596_K598_packet_released"], k630_d["selected_source_action_rejected"])), "K630 decision ceiling moved")

    k627 = data["k627"]
    k627_t = k627["pairing_nonselection_theorem"]
    k627_o = k627["ownership_reconciliation"]
    k627_d = k627["decision"]
    check(k627_t["block_ranks"] == [192, 192, 64, 64], "K627 block ranks moved")
    check(k627_t["block_positive_pairing_dimensions"] == [18528, 18528, 2080, 2080] and k627_t["total_positive_pairing_family_dimension"] == 41216, "K627 pairing dimensions moved")
    check(not k627_t["full_block_gauge_has_nonzero_invariant_symmetric_form"] and k627_t["selecting_a_gram_is_a_gauge_reduction"], "K627 nonselection theorem moved")
    check(k627_t["K625_H_Sigma_is_one_projector_induced_point"] and not k627_t["K441_abstract_data_select_a_positive_gram"], "K627 canonical-point boundary moved")
    check(not any((k627_o["K625_canonical_realization_retracted"], k627_o["K626_embedding_gauge_retracted"], k627_o["full_gauge_nonselection_is_source_or_action_selection"], k627_o["orthogonal_reduction_is_supplied_by_K441"], k627_o["mixed_hessian_or_stationary_background_constructed"], k627_o["common_BV_Green_domain_constructed"])), "K627 ownership ceiling moved")
    check(not k627_d["abstract_K441_pairing_is_canonical_on_actual_carrier"] and k627_d["extra_reduction_data_required_to_select_pairing"] and not any((k627_d["actual_K596_K598_packet_released"], k627_d["selected_source_action_rejected"])), "K627 decision ceiling moved")

    k628 = data["k628"]
    k628_t = k628["determinant_obstruction_theorem"]
    k628_o = k628["ownership_reconciliation"]
    k628_d = k628["decision"]
    check(len(k628["cross_characteristic_packets"]) == 2, "K628 characteristic packet count moved")
    check(k628_t["obstructed_blocks"] == ["fast_outgoing", "fast_incoming", "slow_outgoing"] and k628_t["unobstructed_blocks"] == ["slow_incoming"], "K628 block obstruction fingerprint moved")
    check(not k628_t["K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing"] and k628_t["K622_abstract_nonisometric_orbit_exists"], "K628 serialized-map/orbit boundary moved")
    check(not k628_t["every_K622_family_member_tested"] and not k628_t["alternative_domain_map_family_excluded"], "K628 family scope broadened")
    check(not any((k628_o["K622_abstract_orbit_retracted"], k628_o["K624_H_Sigma_obstruction_retracted"], k628_o["K627_gauge_nonselection_retracted"], k628_o["serialized_map_all_pairing_obstruction_is_action_selection"], k628_o["source_owned_domain_map_or_Gram_constructed"], k628_o["mixed_hessian_or_stationary_background_constructed"], k628_o["common_BV_Green_domain_constructed"])), "K628 ownership ceiling moved")
    check(not k628_d["K622_serialized_witness_can_be_repaired_by_only_changing_positive_Gram"] and not k628_d["broader_K622_family_pairing_orbit_decided"] and not any((k628_d["actual_K596_K598_packet_released"], k628_d["selected_source_action_rejected"])), "K628 decision ceiling moved")

    k625 = data["k625"]
    k625_t = k625["real_pairing_theorem"]
    k625_o = k625["ownership_reconciliation"]
    k625_d = k625["decision"]
    check(len(k625["cross_characteristic_packets"]) == 2, "K625 characteristic packet count moved")
    check(k625_t["four_eigenspaces_are_H_Sigma_orthogonal"] and k625_t["restricted_pairing_is_positive_definite_on_each_block"], "K625 positive orthogonal split moved")
    check(k625_t["isometric_factorized_coordinate_map_exists"] and k625_t["K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries"], "K625 factorized bridge moved")
    check(k625_t["K441_closed_trace_domain_and_Green_conjugation_pull_back"] and not k625_t["ambient_coordinate_map_is_unique"], "K625 transport/nonuniqueness boundary moved")
    check(k625_o["K624_applies_to_canonical_projector_realization"] and not any((k625_o["K623_projector_pairing_retracted"], k625_o["K624_H_Sigma_obstruction_retracted"], k625_o["K441_selects_this_realization_uniquely"], k625_o["canonical_projector_realization_is_action_owned_adapter"], k625_o["stationary_background_or_mixed_hessian_constructed"])), "K625 ownership ceiling moved")
    check(k625_d["missing_ambient_pairing_bridge_constructed"] and k625_d["canonical_K441_realization_available"] and not any((k625_d["all_K441_ambient_realizations_identified"], k625_d["actual_K596_K598_packet_released"], k625_d["selected_source_action_rejected"])), "K625 decision ceiling moved")

    k626 = data["k626"]
    k626_t = k626["embedding_gauge_theorem"]
    k626_o = k626["ownership_reconciliation"]
    k626_d = k626["decision"]
    check(len(k626["cross_characteristic_packets"]) == 2, "K626 characteristic packet count moved")
    check(k626_t["gauge_group"] == "GL(192) x GL(192) x GL(64) x GL(64)", "K626 gauge group moved")
    check(k626_t["all_blockwise_changes_preserve_four_root_action_up_to_factorized_coordinates"] and not k626_t["K441_serializes_one_ambient_embedding"], "K626 abstract-model gauge boundary moved")
    check(k626_t["H_Sigma_is_a_canonical_projector_point_in_the_family"] and not k626_t["K624_normalized_trace_fingerprints_are_embedding_gauge_invariant"], "K626 canonical/gauge-invariance boundary moved")
    check(k626_t["actual_carrier_shears_tested"] == 8 and k626_t["every_tested_shear_changes_both_seed_fingerprints"], "K626 shear discriminator moved")
    check(not any((k626_o["K625_canonical_realization_retracted"], k626_o["K624_H_Sigma_obstruction_retracted"], k626_o["K624_universalized_to_every_K441_embedding"], k626_o["K441_abstract_transport_selects_an_ambient_Gram"], k626_o["embedding_gauge_is_source_or_action_selection"], k626_o["pairing_gauge_constructs_mixed_hessian_or_stationary_background"])), "K626 ownership ceiling moved")
    check(k626_d["canonical_projector_realization_classified"] and not k626_d["abstract_K441_pairing_alone_decides_K622_orbit"] and k626_d["source_or_action_owned_embedding_required_for_broader_verdict"], "K626 decision boundary moved")
    check(not any((k626_d["actual_K596_K598_packet_released"], k626_d["selected_source_action_rejected"])), "K626 protected decision moved")

    k623 = data["k623"]
    k623_t = k623["pairing_theorem"]
    k623_o = k623["ownership_reconciliation"]
    k623_d = k623["decision"]
    check(len(k623["cross_characteristic_packets"]) == 2, "K623 characteristic packet count moved")
    check(k623_t["domain_orthogonality_defect_rank"] == 96, "K623 domain orthogonality defect moved")
    check(k623_t["block_pullback_gram_defect_ranks"] == [128, 128, 64, 0], "K623 block Gram defects moved")
    check(k623_t["three_of_four_necessary_gram_identities_fail"] and not k623_t["K622_constructed_orbit_preserves_projector_pairing"], "K623 pairing verdict moved")
    check(not k623_t["arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded"], "K623 scope broadened")
    check(k623_t["projector_pairing_is_action_self_adjoint"] and not k623_t["projector_pairing_identified_with_K441_factorized_pairing"], "K623 projector/K441 pairing boundary moved")
    check(not any((k623_o["K622_abstract_orbit_equivalence_retracted"], k623_o["K622_constructed_domain_map_is_source_selected"], k623_o["pairing_failure_supplies_action_owned_adapter"], k623_o["common_BV_Green_domain_constructed"], k623_o["nonzero_stationary_background_constructed"])), "K623 ownership ceiling moved")
    check(not any((k623_d["constructed_K622_witness_passes_pairing_gate"], k623_d["K441_pairing_preservation_decided"], k623_d["actual_K596_K598_packet_released"], k623_d["selected_source_action_rejected"])), "K623 decision ceiling moved")

    k624 = data["k624"]
    k624_t = k624["simultaneous_congruence_theorem"]
    k624_o = k624["ownership_reconciliation"]
    k624_d = k624["decision"]
    check(len(k624["cross_characteristic_packets"]) == 2, "K624 characteristic packet count moved")
    check(k624_t["total_pullback_forms_are_nondegenerate"] and k624_t["trace_is_similarity_invariant"], "K624 normalized-form theorem moved")
    check(k624_t["all_four_first_traces_mismatch_at_both_primes"], "K624 trace obstruction moved")
    check(not k624_t["projector_pairing_preserving_commutant_and_domain_orbit_exists"] and k624_t["abstract_nonisometric_K622_orbit_exists"], "K624 orbit boundary moved")
    check(k624_t["pairing_model"] == "projector_induced_H_Sigma" and not k624_t["K441_factorized_pairing_identification_serialized"], "K624 projector/K441 pairing boundary moved")
    check(k624_o["projector_pairing_preserving_same_data_repair_excluded"] and not k624_o["different_action_owned_mixed_hessian_excluded"], "K624 same-data/new-data boundary moved")
    check(not any((k624_o["K621_fixed_domain_obstruction_retracted"], k624_o["K622_abstract_orbit_equivalence_retracted"], k624_o["common_BV_Green_domain_constructed"], k624_o["nonzero_stationary_background_constructed"])), "K624 ownership ceiling moved")
    check(not any((k624_d["current_seed_identification_can_preserve_projector_pairing"], k624_d["K441_pairing_preservation_decided"], k624_d["actual_K596_K598_packet_released"], k624_d["selected_source_action_rejected"])), "K624 decision ceiling moved")

    k621 = data["k621"]
    k621_t = k621["commutant_theorem"]
    k621_o = k621["ownership_reconciliation"]
    k621_d = k621["decision"]
    check(len(k621["cross_characteristic_packets"]) == 2, "K621 characteristic packet count moved")
    check(k621_t["full_commutant_dimension"] == 81920, "K621 commutant dimension moved")
    check(k621_t["fast_block_solution_affine_dimensions"] == [12288, 12288], "K621 fast solution dimensions moved")
    check(k621_t["slow_block_row_space_intersections"] == [0, 0] and k621_t["slow_block_row_space_joins"] == [128, 128], "K621 slow row-space obstruction moved")
    check(not k621_t["fixed_domain_commuting_adapter_exists"], "K621 fixed-domain adapter obstruction moved")
    check(k621_o["fixed_domain_nonpolynomial_commutant_adapter_excluded"] and not any((k621_o["full_commutant_is_action_owned_as_a_selected_adapter"], k621_o["source_domain_reparameterization_tested"], k621_o["mixed_hessian_or_domain_adapter_excluded"], k621_o["nonzero_stationary_background_constructed"])), "K621 ownership ceiling moved")
    check(k621_d["K620_functional_calculus_obstruction_strengthened"] and not any((k621_d["K619_common_module_retracted"], k621_d["actual_K596_K598_packet_released"], k621_d["selected_source_action_rejected"])), "K621 decision ceiling moved")

    k622 = data["k622"]
    k622_t = k622["orbit_theorem"]
    k622_o = k622["ownership_reconciliation"]
    k622_d = k622["decision"]
    check(len(k622["cross_characteristic_packets"]) == 2, "K622 characteristic packet count moved")
    check(k622_t["zero_seed_slow_row_pair_is_direct_sum"] and k622_t["moving_seed_slow_row_pair_is_direct_sum"], "K622 slow decompositions moved")
    check(k622_t["one_invertible_domain_reparameterization_matches_both_slow_rows"] and k622_t["invertible_commutant_and_domain_orbit_equivalence_exists"], "K622 orbit existence moved")
    check(not k622_t["fixed_domain_commutant_adapter_exists"] and k622_t["block_transport_affine_freedom_for_constructed_domain_map"] == 24576 and not k622_t["orbit_equivalence_selects_unique_adapter"], "K622 nonuniqueness/fixed-domain boundary moved")
    check(not any((k622_o["K621_fixed_domain_obstruction_retracted"], k622_o["domain_reparameterization_is_source_selected"], k622_o["commutant_transport_is_action_selected"], k622_o["orbit_equivalence_identifies_seed_constructions"], k622_o["pairing_or_Green_domain_preservation_proved"], k622_o["mixed_hessian_or_stationary_background_constructed"])), "K622 ownership ceiling moved")
    check(k622_d["full_abstract_commutant_orbit_is_nonempty"] and not any((k622_d["K619_common_module_retracted"], k622_d["actual_K596_K598_packet_released"], k622_d["selected_source_action_rejected"])), "K622 decision ceiling moved")

    k619 = data["k619"]
    k619_t = k619["common_module_theorem"]
    k619_o = k619["ownership_reconciliation"]
    k619_d = k619["decision"]
    check(len(k619["cross_characteristic_packets"]) == 2, "K619 characteristic packet count moved")
    check(k619_t["seed_intersection_rank"] == 0, "K619 seed intersection moved")
    check(k619_t["depth_2_intersection_rank"] == 128, "K619 depth-two intersection moved")
    check(k619_t["depth_3_join_rank"] == k619_t["depth_3_intersection_rank"] == 384, "K619 common hull equality moved")
    check(k619_t["filtrations_equal_from_depth_3"] and k619_t["corrected_carrier_complement_rank"] == 128, "K619 stabilization/complement moved")
    check(k619_o["source_owns_zero_form_field_space"] and not k619_o["source_selects_nonzero_zero_form_background"], "K619 source ownership boundary moved")
    check(not any((k619_o["historical_moving_graph_is_source_selected"], k619_o["equality_of_generated_subspaces_identifies_seed_maps"], k619_o["common_module_is_stationary_solution_space"], k619_o["common_module_supplies_mixed_hessian_coupling"])), "K619 ownership ceiling moved")
    check(k619_o["unrestricted_southeast_route_already_completed"] and k619_o["local_full_field_ordinary_gauge_bv_already_completed"], "K619 prior-route currency moved")
    check(k619_d["two_disjoint_seeds_generate_same_A_module"] and not any((k619_d["K615_stationarity_obstruction_retracted"], k619_d["actual_K596_K598_packet_released"], k619_d["selected_source_action_rejected"])), "K619 decision ceiling moved")

    k620 = data["k620"]
    k620_m = k620["module_projector_theorem"]
    k620_a = k620["seed_adapter_theorem"]
    k620_o = k620["ownership_reconciliation"]
    k620_d = k620["decision"]
    check(len(k620["cross_characteristic_packets"]) == 2, "K620 characteristic packet count moved")
    check(k620_m["fast_eigenspace_ranks"] == [192, 192] and k620_m["common_module_fast_ranks"] == [128, 128], "K620 fast block ranks moved")
    check(k620_m["slow_eigenspace_ranks"] == k620_m["common_module_slow_ranks"] == [64, 64], "K620 slow block ranks moved")
    check(not any((k620_m["common_module_is_union_of_full_eigenspaces"], k620_m["polynomial_projector_with_image_common_module_exists"], k620_m["polynomial_projector_with_image_rank128_complement_exists"])), "K620 module-projector obstruction moved")
    check(k620_a["each_seed_meets_all_four_eigenspaces"] and not k620_a["corresponding_seed_maps_scalar_proportional_in_any_eigenspace"] and not k620_a["scalar_polynomial_p_with_pA_J0_equals_X_exists"], "K620 seed-adapter obstruction moved")
    check(not k620_a["arbitrary_commutant_or_domain_endomorphism_tested"] and not k620_a["mixed_hessian_bilinear_adapter_constructed"], "K620 scope broadened")
    check(k620_o["A_owns_four_spectral_projectors"] and not any((k620_o["A_owns_common_module_projector"], k620_o["A_owns_seed_identification"], k620_o["A_invariance_of_common_module_implies_action_selection"], k620_o["nonpolynomial_action_owned_adapter_excluded"], k620_o["moving_nonlinear_mixed_hessian_excluded"])), "K620 ownership ceiling moved")
    check(not any((k620_d["K619_common_module_retracted"], k620_d["common_module_selected_by_frozen_action"], k620_d["zero_form_and_moving_graph_seeds_identified"], k620_d["actual_K596_K598_packet_released"], k620_d["selected_source_action_rejected"])), "K620 decision ceiling moved")

    k617 = data["k617"]
    k617_t = k617["descent_theorem"]
    k617_o = k617["ownership_reconciliation"]
    k617_d = k617["decision"]
    check(len(k617["cross_characteristic_packets"]) == 2, "K617 characteristic packet count moved")
    check(k617_t["both_pin_candidates_descend_injectively"] and k617_t["pin_candidates_become_identical_after_correction"], "K617 descent/collapse moved")
    check(k617_t["corrected_graph_rank"] == 128, "K617 corrected graph rank moved")
    check(k617_t["corrected_graph_intersection_K614_zero_seed_rank"] == 0 and k617_t["corrected_graph_join_K614_zero_seed_rank"] == 256, "K617 zero-seed relation moved")
    check(k617_t["all_four_frozen_spectral_sign_blocks_met"], "K617 spectral/sign coverage moved")
    check(k617_t["frozen_action_residual_rank"] == 128 and not k617_t["stationary_for_frozen_K438_action"], "K617 frozen-action residual moved")
    check(not any((k617_o["historical_graph_is_source_selected"], k617_o["bounded_graph_route_action_owned_by_unrestricted_four_field_action"], k617_o["corrected_descent_reverses_prior_action_ownership_kill"], k617_o["moving_differential_BV_Green_domain_constructed"], k617_o["mixed_hessian_Riesz_packet_constructed"])), "K617 ownership ceiling moved")
    check(k617_d["moving_graph_has_nontrivial_corrected_descent"] and not any((k617_d["K615_frozen_stationarity_obstruction_retracted"], k617_d["K616_unsplit_packet_obstruction_retracted"], k617_d["moving_graph_revives_bounded_action_owned_route"], k617_d["selected_source_action_rejected"])), "K617 decision ceiling moved")

    k618 = data["k618"]
    k618_h = k618["action_hull_theorem"]
    k618_o = k618["ownership_and_typing"]
    k618_r = k618["revival_gate"]
    k618_d = k618["decision"]
    check(len(k618["cross_characteristic_packets"]) == 2, "K618 characteristic packet count moved")
    check(k618_h["krylov_ranks_A0_through_A4"] == [128, 256, 384, 384, 384], "K618 Krylov ranks moved")
    check(k618_h["minimal_action_hull_rank"] == 384 and k618_h["corrected_carrier_complement_rank"] == 128 and not k618_h["action_hull_is_full_corrected_carrier"], "K618 hull/complement moved")
    check([k618_h[key] for key in ("fast_outgoing_missing_rank", "fast_incoming_missing_rank", "slow_outgoing_missing_rank", "slow_incoming_missing_rank")] == [64, 64, 0, 0], "K618 block complement moved")
    check(k618_o["spectral_vector_components_are_action_derived"] and not k618_o["action_derived_vector_split_owns_mixed_hessian_coupling"], "K618 vector/coupling ownership boundary moved")
    check(not k618_o["equal_rank_identifies_historical_and_current_hulls"] and not k618_o["bounded_route_action_owned"], "K618 rank coincidence or route ownership moved")
    check(k618_r["corrected_carrier_supplies_nontrivial_diagnostic_module"] and not k618_r["corrected_carrier_revives_historical_bounded_graph_as_action_subsystem"], "K618 revival gate moved")
    check(k618_r["K616_vector_projection_ownership_narrowed"] and not k618_r["K616_core_unsplit_packet_obstruction_retracted"], "K618 K616 reconciliation moved")
    check(not any((k618_d["K617_nontrivial_descent_retracted"], k618_d["K615_frozen_zero_form_obstruction_retracted"], k618_d["prior_unrestricted_Euler_route_kill_retracted"], k618_d["rank384_coincidence_promoted_to_identity"], k618_d["actual_K596_K598_packet_released"], k618_d["selected_source_action_rejected"])), "K618 decision ceiling moved")

    k615 = data["k615"]
    k615_r = k615["rank_fingerprint"]
    k615_f = k615["fibrewise_stationarity_theorem"]
    k615_c = k615["closed_domain_stationarity_theorem"]
    k615_d = k615["decision"]
    check(len(k615["cross_characteristic_packets"]) == 2, "K615 characteristic packet count moved")
    check(k615_r["action_euler_image"] == 128, "K615 Euler image rank moved")
    check(k615_r["outgoing_zero_form"] == k615_r["incoming_zero_form"] == 128, "K615 zero-form half ranks moved")
    check(k615_r["outgoing_euler"] == k615_r["incoming_euler"] == 128, "K615 Euler half ranks moved")
    check(k615_r["fast_euler"] == k615_r["slow_euler"] == 128, "K615 fast/slow Euler ranks moved")
    check(k615_f["kernel_dimension"] == 0 and not k615_f["nonzero_zero_form_value_is_stationary"], "K615 fibrewise stationarity moved")
    check(k615_c["K440_kernel_dimension"] == k615_c["K440_cokernel_dimension"] == 0, "K615 K440 kernel/cokernel moved")
    check(k615_c["four_source_fermion_slots_direct_sum_kernel_dimension"] == 0, "K615 four-field consequence moved")
    check(not k615_c["moving_lower_order_or_nonlinear_operator_covered"], "K615 scope broadened")
    check(not any((k615_d["nonzero_stationary_zero_form_in_K440_model_exists"], k615_d["four_field_frozen_stationary_background_nonzero"], k615_d["moving_nonlinear_nonzero_background_excluded"], k615_d["selected_source_action_rejected"], k615_d["K596_K598_released_by_stationarity"])), "K615 decision ceiling moved")

    k616 = data["k616"]
    k616_i = k616["input_injectivity"]
    k616_u = k616["unsplit_defect_theorem"]
    k616_m = k616["matching_half_repair"]
    k616_t = k616["transport_theorem"]
    k616_d = k616["decision"]
    check([k616_i[k] for k in ("outgoing_x_rank", "incoming_x_rank", "outgoing_y_rank", "incoming_y_rank")] == [128, 128, 128, 128], "K616 input half ranks moved")
    check(k616_i["every_nonzero_v_has_all_four_components_nonzero"], "K616 injectivity consequence moved")
    check(k616_u["rank_for_every_nonzero_v"] == 2 and not k616_u["natural_unsplit_packet_satisfies_K596"], "K616 unsplit defect moved")
    check(k616_m["typed_square_defect_rank"] == 0 and not k616_m["equals_natural_unsplit_packet"] and not k616_m["split_is_action_owned"], "K616 matching-half boundary moved")
    check(k616_t["rank_preserved"] and k616_t["rank_at_every_transport_fibre"] == 2 and not k616_t["moving_nonlinear_action_coupling_covered"], "K616 transport ceiling moved")
    check(k616_d["natural_unsplit_packet_rejected_in_frozen_model"] and not any((k616_d["matching_half_action_ownership_constructed"], k616_d["K596_actual_action_owned_packet_released"], k616_d["K598_actual_action_owned_packet_released"], k616_d["selected_source_action_rejected"])), "K616 decision ceiling moved")

    k614 = data["k614"]
    k614_f = k614["cross_characteristic_rank_fingerprint"]
    k614_t = k614["injection_theorem"]
    k614_b = k614["background_and_riesz_reconciliation"]
    k614_d = k614["decision"]
    check(len(k614["cross_characteristic_packets"]) == 2, "K614 characteristic packet count moved")
    check(k614_f["source_zero_form"] == k614_f["corrected_image"] == 128, "K614 corrected injection rank moved")
    check(k614_f["fast_projection"] == k614_f["slow_projection"] == 128, "K614 fast/slow ranks moved")
    check(k614_f["incoming_projection"] == k614_f["outgoing_projection"] == 128, "K614 sign-half ranks moved")
    check([k614_f[key] for key in ("fast_incoming_projection", "fast_outgoing_projection", "slow_incoming_projection", "slow_outgoing_projection")] == [128, 128, 64, 64], "K614 four-block ranks moved")
    check(k614_t["source_owned_zero_form_field"] and k614_t["image_lies_in_corrected_carrier"], "K614 source/injection ownership lost")
    check(k614_t["incoming_projection_is_injective"] and k614_t["outgoing_projection_is_injective"], "K614 sign-half injectivity lost")
    check(k614_t["fast_projection_is_injective"] and k614_t["slow_projection_is_injective"], "K614 speed injectivity lost")
    check(k614_t["all_four_action_spectral_sign_blocks_met"], "K614 spectral/sign coverage lost")
    check(k614_t["field_space_is_not_a_selected_field_value"], "K614 field/value distinction lost")
    check(k614_b["active_background"] == "zero fermion" and k614_b["injection_evaluated_on_active_background_is_zero"], "K614 zero-background boundary moved")
    check(k614_b["zero_fermion_current_rank"] == k614_b["zero_fermion_mixed_hessian_rank"] == 0, "K614 zero-background action ranks moved")
    check(not any((k614_b["nonzero_fermion_stationary_solution_owned"], k614_b["K441_action_Riesz_return_for_zero_form_background_owned"], k614_b["K596_actual_rank_one_packet_released"], k614_b["K598_actual_covariant_packet_released"])), "K614 missing background/Riesz packet invented")
    check(k614_d["source_owned_zero_form_injection_constructed"] and k614_d["K613_hypothetical_field_to_carrier_map_narrowed"], "K614 decision advance lost")
    check(not any((k614_d["action_owned_nonzero_background_constructed"], k614_d["actual_action_owned_soldering_constructed"], k614_d["K590_factorized_completion_retracted"], k614_d["K613_central_parity_obstruction_retracted"], k614_d["selected_source_action_rejected"])), "K614 decision ceiling moved")

    k612 = data["k612"]
    k612_s = k612["serialized_numeric_custody"]
    k612_m = k612["missing_quantitative_custody"]
    k612_c = k612["same_interface_countermodels"]
    k612_r = k612["dependency_reconciliation"]
    k612_d = k612["decision"]
    check(k612_s["chart_contraction_upper"] == "3/8", "K612 chart constant moved")
    check(k612_s["chart_inverse_norm_upper"] == "8/5", "K612 inverse constant moved")
    check(k612_s["physical_gram_interval"] == ["64/121", "64/25"], "K612 Gram interval moved")
    check(k612_s["existential_complete_sector_semibound"] and k612_s["matched_counterterm_cancellation_identified"], "K612 existential/cancellation input lost")
    check(not k612_s["raw_counterterm_separately_convergent"], "K612 raw counterterm incorrectly converges")
    check(not any((k612_m["named_regular_lower_bound_r0"], k612_m["named_complete_lower_bound_L0"], k612_m["named_graph_relative_bound_for_complete_cancelled_X"], k612_m["named_identity_constant_for_complete_cancelled_X"], k612_m["named_common_domain_for_chart_and_complete_core"])), "K612 missing custody fabricated")
    check(k612_c["floors_are_distinct"] and k612_c["no_uniform_floor_follows_from_serialized_interface"], "K612 countermodel conclusion lost")
    check(len(k612_c["rows"]) == 4, "K612 countermodel family size moved")
    check([row["native_floor"] for row in k612_c["rows"]] == ["-3", "-9", "-66", "-1026"], "K612 countermodel floors moved")
    check(not any((k612_r["K139_semiboundedness_retracted"], k612_r["K462_existential_coercivity_retracted"], k612_r["K581_noncyclic_inheritance_retracted"])), "K612 dependency retraction invented")
    check(k612_r["K611_mixed_graph_obstruction_preserved"] and k612_r["new_cancellation_adapted_estimate_still_live"], "K612 live escape lost")
    check(k612_d["K139_constant_extraction_from_current_serialized_custody_rejected"] and not any((k612_d["named_complete_sector_floor_emitted"], k612_d["named_noncyclic_floor_emitted"], k612_d["K473_released"], k612_d["native_K152_interval_emitted"])), "K612 decision ceiling moved")

    k613 = data["k613"]
    k613_p = k613["carrier_parity"]
    k613_s = k613["full_stabilizer_consequence"]
    k613_k = k613["K594_replay"]
    k613_r = k613["reopener"]
    k613_x = k613["dependency_reconciliation"]
    k613_d = k613["decision"]
    check(k613_p["all_available_generators_have_even_carrier_parity"], "K613 generator parity moved")
    check(k613_p["allowed_contractions_remove_carrier_slots_in_pairs"], "K613 contraction parity moved")
    check(k613_p["homogeneous_tensor_networks_preserve_even_carrier_parity"], "K613 tensor parity moved")
    check(not k613_p["nonzero_natural_vector_or_covector_from_even_inputs"], "K613 vector selector invented")
    check(k613_s["spectral_block_ranks"] == [192, 192, 64, 64], "K613 block ranks moved")
    check(k613_s["minimum_nonzero_invariant_endomorphism_rank"] == 64, "K613 minimum invariant rank moved")
    check(k613_s["possible_invariant_idempotent_ranks"] == [0, 64, 128, 192, 256, 320, 384, 448, 512], "K613 invariant ranks moved")
    check(not k613_s["rank_one_natural_endomorphism_from_current_tensors"], "K613 rank-one selector invented")
    check(k613_s["arbitrary_tensor_contraction_stronger_than_K610_factorwise_scope"], "K613 scope regression")
    check(not any((k613_k["one_carrier_slot_component_serialized"], k613_k["odd_carrier_valence_background_contraction_serialized"], k613_k["existing_third_jet_breaks_central_parity"])), "K613 K594 odd datum invented")
    check(not k613_r["affine_field_dependent_or_odd_action_data_ruled_out"], "K613 live odd escape lost")
    check(not any((k613_d["all_current_homogeneous_tensor_networks_select_vector_or_covector"], k613_d["all_current_homogeneous_tensor_networks_select_rank_one_packet"], k613_d["K598_released"])), "K613 decision ceiling moved")
    check(not any((k613_x["K590_factorized_complex_retracted"], k613_x["K600_no_selector_retracted"], k613_x["K607_action_symbol_refinement_retracted"], k613_x["K610_factorwise_obstruction_retracted"], k613_x["K598_actual_action_owned_packet_constructed"], k613_x["selected_source_action_rejected"])), "K613 dependency boundary moved")

    if check_digests:
        for name, entry in registry["basis"].items():
            if "path" in entry:
                check(digest(ROOT / entry["path"]) == entry["sha256"],
                      f"basis digest mismatch: {name}")
    return failures


def selftest(base: dict) -> tuple[int, int]:
    mutations = []

    def add(name: str, fn) -> None:
        case = copy.deepcopy(base)
        fn(case)
        mutations.append((name, case))

    add("live-key-missing", lambda d: d["current"].pop("next_condition"))
    add("history-key-missing", lambda d: d["current"].pop("prior_conditions"))
    add("stale-25-66-live", lambda d: d["current"].__setitem__(
        "next_condition", d["current"]["next_condition"] + " 25 terminal and 66 open"))
    add("root-fabricated", lambda d: d["qualification"]["root_candidate_rebuild"].__setitem__(
        "current_named_root_candidate_set", ["SYNTHETIC-CBRS-1AC"]))
    add("terminal-count-moved", lambda d: d["dispositions"]["exhaustion_evaluation"].__setitem__(
        "terminal_rows", 90))
    add("b2-gate-reversed", lambda d: d["b2"]["basis"].__setitem__("b2_selectable", False))
    add("agenda-stale", lambda d: d["agenda"].__setitem__(
        "latest_result_2026_09_28_k608_k610", "Repeat the superseded K466 shifted-coercivity bridge."))
    add("agenda-latest-stale", lambda d: d["agenda"].__setitem__(
        "latest_result_2026_09_28_k600_k601", "K599 remains the latest result."))
    add("b5-rb6-repeat", lambda d: next(
        item for item in d["agenda"]["work_items"]
        if item["id"] == "B5-INDEPENDENT-RECONSTRUCTION"
    ).__setitem__("next_swing", "Step 0: recertify the remaining RB6 null with exact derivatives."))
    add("protected-effect-moved", lambda d: d["registry"]["protected_effects"].__setitem__(
        "ledger_verdict_change", True))

    add("k633-join", lambda d: d["k633"]["cross_characteristic_packets"][0].__setitem__("seed_action_seed_join_rank", 128))
    add("k633-quotient", lambda d: d["k633"]["cross_characteristic_packets"][0].__setitem__("nonconstant_quotient_coefficient_rank", 2))
    add("k633-stabilizer", lambda d: d["k633"]["stabilizer_theorem"].__setitem__("polynomial_stabilizer_dimension", 2))
    add("k633-endomorphism", lambda d: d["k633"]["stabilizer_theorem"].__setitem__("nontrivial_owned_source_endomorphism_obtained", True))
    add("k633-scope", lambda d: d["k633"]["ownership_reconciliation"].__setitem__("arbitrary_commutant_or_mixed_hessian_excluded", True))
    add("k633-release", lambda d: d["k633"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k634-membership", lambda d: d["k634"]["equivalent_norm_theorem"].__setitem__("membership_of_boundary_profile_is_unchanged", False))
    add("k634-continuity", lambda d: d["k634"]["equivalent_norm_theorem"].__setitem__("continuity_of_every_linear_trace_is_invariant", False))
    add("k634-repair", lambda d: d["k634"]["bounded_correlation_corollary"].__setitem__("point_trace_continuity_repaired", True))
    add("k634-scope", lambda d: d["k634"]["decision"].__setitem__("all_correlated_domains_ruled_out", True))
    add("k634-floor", lambda d: d["k634"]["surviving_domain_class"].__setitem__("named_quantitative_floor_constructed", True))

    add("k631-count", lambda d: d["k631"].__setitem__("candidate_count", 7))
    add("k631-ambient", lambda d: d["k631"]["census_theorem"].__setitem__("single_candidate_matching_ambient_gram", True))
    add("k631-composition", lambda d: d["k631"]["census_theorem"].__setitem__("composition_loophole_left_for_K632", False))
    add("k631-retract", lambda d: d["k631"]["ownership_reconciliation"].__setitem__("K614_source_owned_injection_retracted", True))
    add("k632-exhausted", lambda d: d["k632"]["closure_theorem"].__setitem__("current_serialized_operation_set_exhausted", False))
    add("k632-gram", lambda d: d["k632"]["closure_theorem"].__setitem__("owned_ambient_Gram_reachable", True))
    add("k632-pullback", lambda d: d["k632"]["closure_theorem"].__setitem__("nondegenerate_unowned_source_pullback_forms_reachable", False))
    add("k632-universal", lambda d: d["k632"]["closure_theorem"].__setitem__("universal_future_action_no_go", True))
    add("k632-release", lambda d: d["k632"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k632-retract", lambda d: d["k632"]["ownership_reconciliation"].__setitem__("K625_H_Sigma_retracted", True))

    add("k629-dimension", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("family_parameter_group_dimension", 4096))
    add("k629-slow-ratios", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("combined_slow_ratio_squares", [1, 1]))
    add("k629-fast-ratios", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("both_fast_ratio_squares", [949, 1004]))
    add("k629-family", lambda d: d["k629"]["determinant_line_theorem"].__setitem__("every_K622_family_member_tested", False))
    add("k629-repair", lambda d: d["k629"]["decision"].__setitem__("K622_family_contains_pairing_preserving_repair", True))
    add("k629-owner", lambda d: d["k629"]["ownership_reconciliation"].__setitem__("family_wide_pairing_obstruction_is_action_selection", True))
    add("k630-ratios", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("invariant_slow_ratio_squares", [1, 1]))
    add("k630-invariant", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("all_tested_source_and_ambient_gauges_preserve_obstruction", False))
    add("k630-artifact", lambda d: d["k630"]["gauge_invariance_theorem"].__setitem__("K629_family_obstruction_is_coordinate_artifact", True))
    add("k630-pivot", lambda d: d["k630"]["decision"].__setitem__("admissible_common_basis_or_pivot_change_reopens_K622_pairing_family", True))
    add("k630-owner", lambda d: d["k630"]["ownership_reconciliation"].__setitem__("ambient_gauge_invariance_selects_a_positive_Gram", True))

    add("k627-dimension", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("total_positive_pairing_family_dimension", 41215))
    add("k627-invariant", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("full_block_gauge_has_nonzero_invariant_symmetric_form", True))
    add("k627-reduction", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("selecting_a_gram_is_a_gauge_reduction", False))
    add("k627-selected", lambda d: d["k627"]["pairing_nonselection_theorem"].__setitem__("K441_abstract_data_select_a_positive_gram", True))
    add("k627-owner", lambda d: d["k627"]["ownership_reconciliation"].__setitem__("orthogonal_reduction_is_supplied_by_K441", True))
    add("k627-release", lambda d: d["k627"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k628-blocks", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("obstructed_blocks", ["fast_outgoing"]))
    add("k628-pairing", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing", True))
    add("k628-family", lambda d: d["k628"]["determinant_obstruction_theorem"].__setitem__("every_K622_family_member_tested", True))
    add("k628-retract", lambda d: d["k628"]["ownership_reconciliation"].__setitem__("K622_abstract_orbit_retracted", True))
    add("k628-owner", lambda d: d["k628"]["ownership_reconciliation"].__setitem__("source_owned_domain_map_or_Gram_constructed", True))
    add("k628-broader", lambda d: d["k628"]["decision"].__setitem__("broader_K622_family_pairing_orbit_decided", True))

    add("k625-orthogonal", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("four_eigenspaces_are_H_Sigma_orthogonal", False))
    add("k625-positive", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("restricted_pairing_is_positive_definite_on_each_block", False))
    add("k625-bridge", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("isometric_factorized_coordinate_map_exists", False))
    add("k625-rotation", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries", False))
    add("k625-unique", lambda d: d["k625"]["real_pairing_theorem"].__setitem__("ambient_coordinate_map_is_unique", True))
    add("k625-k624", lambda d: d["k625"]["ownership_reconciliation"].__setitem__("K624_applies_to_canonical_projector_realization", False))
    add("k625-action-owner", lambda d: d["k625"]["ownership_reconciliation"].__setitem__("canonical_projector_realization_is_action_owned_adapter", True))
    add("k625-all-embeddings", lambda d: d["k625"]["decision"].__setitem__("all_K441_ambient_realizations_identified", True))
    add("k625-release", lambda d: d["k625"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k626-gauge", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("gauge_group", "O(512)"))
    add("k626-embedding-selected", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("K441_serializes_one_ambient_embedding", True))
    add("k626-invariant", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("K624_normalized_trace_fingerprints_are_embedding_gauge_invariant", True))
    add("k626-shears", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("actual_carrier_shears_tested", 4))
    add("k626-fingerprints", lambda d: d["k626"]["embedding_gauge_theorem"].__setitem__("every_tested_shear_changes_both_seed_fingerprints", False))
    add("k626-universalize", lambda d: d["k626"]["ownership_reconciliation"].__setitem__("K624_universalized_to_every_K441_embedding", True))
    add("k626-action-owner", lambda d: d["k626"]["ownership_reconciliation"].__setitem__("embedding_gauge_is_source_or_action_selection", True))
    add("k626-orbit", lambda d: d["k626"]["decision"].__setitem__("abstract_K441_pairing_alone_decides_K622_orbit", True))
    add("k626-requirement", lambda d: d["k626"]["decision"].__setitem__("source_or_action_owned_embedding_required_for_broader_verdict", False))
    add("k626-release", lambda d: d["k626"]["decision"].__setitem__("actual_K596_K598_packet_released", True))

    add("k623-domain-defect", lambda d: d["k623"]["pairing_theorem"].__setitem__("domain_orthogonality_defect_rank", 0))
    add("k623-gram-defects", lambda d: d["k623"]["pairing_theorem"].__setitem__("block_pullback_gram_defect_ranks", [0, 0, 0, 0]))
    add("k623-pairing", lambda d: d["k623"]["pairing_theorem"].__setitem__("K622_constructed_orbit_preserves_projector_pairing", True))
    add("k623-scope", lambda d: d["k623"]["pairing_theorem"].__setitem__("arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded", True))
    add("k623-self-adjoint", lambda d: d["k623"]["pairing_theorem"].__setitem__("projector_pairing_is_action_self_adjoint", False))
    add("k623-k441-identification", lambda d: d["k623"]["pairing_theorem"].__setitem__("projector_pairing_identified_with_K441_factorized_pairing", True))
    add("k623-k441-decision", lambda d: d["k623"]["decision"].__setitem__("K441_pairing_preservation_decided", True))
    add("k623-retract", lambda d: d["k623"]["ownership_reconciliation"].__setitem__("K622_abstract_orbit_equivalence_retracted", True))
    add("k623-release", lambda d: d["k623"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k624-trace", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("all_four_first_traces_mismatch_at_both_primes", False))
    add("k624-isometric-orbit", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("projector_pairing_preserving_commutant_and_domain_orbit_exists", True))
    add("k624-pairing-model", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("pairing_model", "K441_factorized_pairing"))
    add("k624-k441-identification", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("K441_factorized_pairing_identification_serialized", True))
    add("k624-abstract-orbit", lambda d: d["k624"]["simultaneous_congruence_theorem"].__setitem__("abstract_nonisometric_K622_orbit_exists", False))
    add("k624-new-data", lambda d: d["k624"]["ownership_reconciliation"].__setitem__("different_action_owned_mixed_hessian_excluded", True))
    add("k624-domain", lambda d: d["k624"]["ownership_reconciliation"].__setitem__("common_BV_Green_domain_constructed", True))
    add("k624-release", lambda d: d["k624"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k624-k441-decision", lambda d: d["k624"]["decision"].__setitem__("K441_pairing_preservation_decided", True))

    add("k621-dimension", lambda d: d["k621"]["commutant_theorem"].__setitem__("full_commutant_dimension", 4))
    add("k621-fast-solutions", lambda d: d["k621"]["commutant_theorem"].__setitem__("fast_block_solution_affine_dimensions", [0, 0]))
    add("k621-slow-intersection", lambda d: d["k621"]["commutant_theorem"].__setitem__("slow_block_row_space_intersections", [64, 64]))
    add("k621-slow-join", lambda d: d["k621"]["commutant_theorem"].__setitem__("slow_block_row_space_joins", [64, 64]))
    add("k621-adapter", lambda d: d["k621"]["commutant_theorem"].__setitem__("fixed_domain_commuting_adapter_exists", True))
    add("k621-owner", lambda d: d["k621"]["ownership_reconciliation"].__setitem__("full_commutant_is_action_owned_as_a_selected_adapter", True))
    add("k621-domain-tested", lambda d: d["k621"]["ownership_reconciliation"].__setitem__("source_domain_reparameterization_tested", True))
    add("k621-release", lambda d: d["k621"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k622-slow-pair", lambda d: d["k622"]["orbit_theorem"].__setitem__("zero_seed_slow_row_pair_is_direct_sum", False))
    add("k622-domain-map", lambda d: d["k622"]["orbit_theorem"].__setitem__("one_invertible_domain_reparameterization_matches_both_slow_rows", False))
    add("k622-orbit", lambda d: d["k622"]["orbit_theorem"].__setitem__("invertible_commutant_and_domain_orbit_equivalence_exists", False))
    add("k622-fixed-domain", lambda d: d["k622"]["orbit_theorem"].__setitem__("fixed_domain_commutant_adapter_exists", True))
    add("k622-unique", lambda d: d["k622"]["orbit_theorem"].__setitem__("orbit_equivalence_selects_unique_adapter", True))
    add("k622-source-selected", lambda d: d["k622"]["ownership_reconciliation"].__setitem__("domain_reparameterization_is_source_selected", True))
    add("k622-pairing", lambda d: d["k622"]["ownership_reconciliation"].__setitem__("pairing_or_Green_domain_preservation_proved", True))
    add("k622-release", lambda d: d["k622"]["decision"].__setitem__("actual_K596_K598_packet_released", True))

    add("k617-rank", lambda d: d["k617"]["descent_theorem"].__setitem__("corrected_graph_rank", 127))
    add("k617-collapse", lambda d: d["k617"]["descent_theorem"].__setitem__("pin_candidates_become_identical_after_correction", False))
    add("k617-zero-seed", lambda d: d["k617"]["descent_theorem"].__setitem__("corrected_graph_intersection_K614_zero_seed_rank", 128))
    add("k617-stationary", lambda d: d["k617"]["descent_theorem"].__setitem__("stationary_for_frozen_K438_action", True))
    add("k617-ownership", lambda d: d["k617"]["ownership_reconciliation"].__setitem__("bounded_graph_route_action_owned_by_unrestricted_four_field_action", True))
    add("k617-revival", lambda d: d["k617"]["decision"].__setitem__("moving_graph_revives_bounded_action_owned_route", True))
    add("k618-krylov", lambda d: d["k618"]["action_hull_theorem"].__setitem__("krylov_ranks_A0_through_A4", [128, 256, 512, 512, 512]))
    add("k618-complement", lambda d: d["k618"]["action_hull_theorem"].__setitem__("corrected_carrier_complement_rank", 0))
    add("k618-slow-missing", lambda d: d["k618"]["action_hull_theorem"].__setitem__("slow_incoming_missing_rank", 64))
    add("k618-coupling-owned", lambda d: d["k618"]["ownership_and_typing"].__setitem__("action_derived_vector_split_owns_mixed_hessian_coupling", True))
    add("k618-rank-identity", lambda d: d["k618"]["ownership_and_typing"].__setitem__("equal_rank_identifies_historical_and_current_hulls", True))
    add("k618-route-revived", lambda d: d["k618"]["revival_gate"].__setitem__("corrected_carrier_revives_historical_bounded_graph_as_action_subsystem", True))
    add("k618-k616-retracted", lambda d: d["k618"]["revival_gate"].__setitem__("K616_core_unsplit_packet_obstruction_retracted", True))
    add("k618-packet", lambda d: d["k618"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k619-seed-intersection", lambda d: d["k619"]["common_module_theorem"].__setitem__("seed_intersection_rank", 128))
    add("k619-depth2", lambda d: d["k619"]["common_module_theorem"].__setitem__("depth_2_intersection_rank", 0))
    add("k619-depth3", lambda d: d["k619"]["common_module_theorem"].__setitem__("depth_3_join_rank", 512))
    add("k619-seed-identity", lambda d: d["k619"]["ownership_reconciliation"].__setitem__("equality_of_generated_subspaces_identifies_seed_maps", True))
    add("k619-stationary", lambda d: d["k619"]["ownership_reconciliation"].__setitem__("common_module_is_stationary_solution_space", True))
    add("k619-packet", lambda d: d["k619"]["decision"].__setitem__("actual_K596_K598_packet_released", True))
    add("k620-fast", lambda d: d["k620"]["module_projector_theorem"].__setitem__("common_module_fast_ranks", [192, 192]))
    add("k620-module-projector", lambda d: d["k620"]["module_projector_theorem"].__setitem__("polynomial_projector_with_image_common_module_exists", True))
    add("k620-complement-projector", lambda d: d["k620"]["module_projector_theorem"].__setitem__("polynomial_projector_with_image_rank128_complement_exists", True))
    add("k620-seed-proportional", lambda d: d["k620"]["seed_adapter_theorem"].__setitem__("corresponding_seed_maps_scalar_proportional_in_any_eigenspace", True))
    add("k620-seed-adapter", lambda d: d["k620"]["seed_adapter_theorem"].__setitem__("scalar_polynomial_p_with_pA_J0_equals_X_exists", True))
    add("k620-commutant-excluded", lambda d: d["k620"]["ownership_reconciliation"].__setitem__("nonpolynomial_action_owned_adapter_excluded", True))
    add("k620-action-selects", lambda d: d["k620"]["decision"].__setitem__("common_module_selected_by_frozen_action", True))

    add("k615-euler-rank", lambda d: d["k615"]["rank_fingerprint"].__setitem__("action_euler_image", 127))
    add("k615-zero-half", lambda d: d["k615"]["rank_fingerprint"].__setitem__("incoming_zero_form", 127))
    add("k615-euler-half", lambda d: d["k615"]["rank_fingerprint"].__setitem__("outgoing_euler", 127))
    add("k615-fast", lambda d: d["k615"]["rank_fingerprint"].__setitem__("fast_euler", 127))
    add("k615-fibre-kernel", lambda d: d["k615"]["fibrewise_stationarity_theorem"].__setitem__("kernel_dimension", 1))
    add("k615-stationary", lambda d: d["k615"]["fibrewise_stationarity_theorem"].__setitem__("nonzero_zero_form_value_is_stationary", True))
    add("k615-domain-kernel", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("K440_kernel_dimension", 1))
    add("k615-four-field", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("four_source_fermion_slots_direct_sum_kernel_dimension", 1))
    add("k615-scope", lambda d: d["k615"]["closed_domain_stationarity_theorem"].__setitem__("moving_lower_order_or_nonlinear_operator_covered", True))
    add("k615-overclaim", lambda d: d["k615"]["decision"].__setitem__("selected_source_action_rejected", True))
    add("k615-release", lambda d: d["k615"]["decision"].__setitem__("K596_K598_released_by_stationarity", True))

    add("k616-x-rank", lambda d: d["k616"]["input_injectivity"].__setitem__("outgoing_x_rank", 127))
    add("k616-y-rank", lambda d: d["k616"]["input_injectivity"].__setitem__("incoming_y_rank", 127))
    add("k616-components", lambda d: d["k616"]["input_injectivity"].__setitem__("every_nonzero_v_has_all_four_components_nonzero", False))
    add("k616-defect", lambda d: d["k616"]["unsplit_defect_theorem"].__setitem__("rank_for_every_nonzero_v", 1))
    add("k616-pass", lambda d: d["k616"]["unsplit_defect_theorem"].__setitem__("natural_unsplit_packet_satisfies_K596", True))
    add("k616-repair", lambda d: d["k616"]["matching_half_repair"].__setitem__("equals_natural_unsplit_packet", True))
    add("k616-owner", lambda d: d["k616"]["matching_half_repair"].__setitem__("split_is_action_owned", True))
    add("k616-transport", lambda d: d["k616"]["transport_theorem"].__setitem__("rank_preserved", False))
    add("k616-transport-rank", lambda d: d["k616"]["transport_theorem"].__setitem__("rank_at_every_transport_fibre", 0))
    add("k616-scope", lambda d: d["k616"]["transport_theorem"].__setitem__("moving_nonlinear_action_coupling_covered", True))
    add("k616-release", lambda d: d["k616"]["decision"].__setitem__("K596_actual_action_owned_packet_released", True))
    add("k616-action", lambda d: d["k616"]["decision"].__setitem__("selected_source_action_rejected", True))

    add("k614-rank", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("corrected_image", 127))
    add("k614-fast", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("fast_projection", 127))
    add("k614-incoming", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("incoming_projection", 127))
    add("k614-block", lambda d: d["k614"]["cross_characteristic_rank_fingerprint"].__setitem__("slow_incoming_projection", 0))
    add("k614-source", lambda d: d["k614"]["injection_theorem"].__setitem__("source_owned_zero_form_field", False))
    add("k614-carrier", lambda d: d["k614"]["injection_theorem"].__setitem__("image_lies_in_corrected_carrier", False))
    add("k614-half", lambda d: d["k614"]["injection_theorem"].__setitem__("incoming_projection_is_injective", False))
    add("k614-field-value", lambda d: d["k614"]["injection_theorem"].__setitem__("field_space_is_not_a_selected_field_value", False))
    add("k614-background", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("injection_evaluated_on_active_background_is_zero", False))
    add("k614-current", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("zero_fermion_current_rank", 1))
    add("k614-stationary", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("nonzero_fermion_stationary_solution_owned", True))
    add("k614-riesz", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("K441_action_Riesz_return_for_zero_form_background_owned", True))
    add("k614-release", lambda d: d["k614"]["background_and_riesz_reconciliation"].__setitem__("K596_actual_rank_one_packet_released", True))
    add("k614-decision", lambda d: d["k614"]["decision"].__setitem__("source_owned_zero_form_injection_constructed", False))
    add("k614-overclaim", lambda d: d["k614"]["decision"].__setitem__("actual_action_owned_soldering_constructed", True))

    add("k612-chart", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("chart_contraction_upper", "1/2"))
    add("k612-inverse", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("chart_inverse_norm_upper", "2"))
    add("k612-gram", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("physical_gram_interval", ["1", "1"]))
    add("k612-raw", lambda d: d["k612"]["serialized_numeric_custody"].__setitem__("raw_counterterm_separately_convergent", True))
    for key in ("named_regular_lower_bound_r0", "named_complete_lower_bound_L0", "named_graph_relative_bound_for_complete_cancelled_X", "named_identity_constant_for_complete_cancelled_X", "named_common_domain_for_chart_and_complete_core"):
        add("k612-missing-" + key, lambda d, key=key: d["k612"]["missing_quantitative_custody"].__setitem__(key, True))
    add("k612-distinct", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("floors_are_distinct", False))
    add("k612-uniform", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("no_uniform_floor_follows_from_serialized_interface", False))
    add("k612-row", lambda d: d["k612"]["same_interface_countermodels"]["rows"][0].__setitem__("native_floor", "0"))
    add("k612-family", lambda d: d["k612"]["same_interface_countermodels"].__setitem__("rows", d["k612"]["same_interface_countermodels"]["rows"][:3]))
    for key in ("K139_semiboundedness_retracted", "K462_existential_coercivity_retracted", "K581_noncyclic_inheritance_retracted"):
        add("k612-retract-" + key, lambda d, key=key: d["k612"]["dependency_reconciliation"].__setitem__(key, True))
    add("k612-k611", lambda d: d["k612"]["dependency_reconciliation"].__setitem__("K611_mixed_graph_obstruction_preserved", False))
    add("k612-escape", lambda d: d["k612"]["dependency_reconciliation"].__setitem__("new_cancellation_adapted_estimate_still_live", False))
    add("k612-decision", lambda d: d["k612"]["decision"].__setitem__("K139_constant_extraction_from_current_serialized_custody_rejected", False))
    add("k612-floor", lambda d: d["k612"]["decision"].__setitem__("named_complete_sector_floor_emitted", True))
    add("k612-k473", lambda d: d["k612"]["decision"].__setitem__("K473_released", True))

    add("k613-even", lambda d: d["k613"]["carrier_parity"].__setitem__("all_available_generators_have_even_carrier_parity", False))
    add("k613-contract", lambda d: d["k613"]["carrier_parity"].__setitem__("allowed_contractions_remove_carrier_slots_in_pairs", False))
    add("k613-network", lambda d: d["k613"]["carrier_parity"].__setitem__("homogeneous_tensor_networks_preserve_even_carrier_parity", False))
    add("k613-vector", lambda d: d["k613"]["carrier_parity"].__setitem__("nonzero_natural_vector_or_covector_from_even_inputs", True))
    add("k613-blocks", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("spectral_block_ranks", [256, 256]))
    add("k613-minrank", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("minimum_nonzero_invariant_endomorphism_rank", 1))
    add("k613-ranks", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("possible_invariant_idempotent_ranks", [0, 1, 512]))
    add("k613-rankone", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("rank_one_natural_endomorphism_from_current_tensors", True))
    add("k613-scope", lambda d: d["k613"]["full_stabilizer_consequence"].__setitem__("arbitrary_tensor_contraction_stronger_than_K610_factorwise_scope", False))
    add("k613-slot", lambda d: d["k613"]["K594_replay"].__setitem__("one_carrier_slot_component_serialized", True))
    add("k613-background", lambda d: d["k613"]["K594_replay"].__setitem__("odd_carrier_valence_background_contraction_serialized", True))
    add("k613-thirdjet", lambda d: d["k613"]["K594_replay"].__setitem__("existing_third_jet_breaks_central_parity", True))
    add("k613-escape", lambda d: d["k613"]["reopener"].__setitem__("affine_field_dependent_or_odd_action_data_ruled_out", True))
    add("k613-decision-vector", lambda d: d["k613"]["decision"].__setitem__("all_current_homogeneous_tensor_networks_select_vector_or_covector", True))
    add("k613-decision-rank", lambda d: d["k613"]["decision"].__setitem__("all_current_homogeneous_tensor_networks_select_rank_one_packet", True))
    add("k613-release", lambda d: d["k613"]["decision"].__setitem__("K598_released", True))

    caught = 0
    for name, case in mutations:
        failures = audit(case, check_digests=False)
        if failures:
            caught += 1
        else:
            print(f"RED selftest mutation escaped: {name}")
    return caught, len(mutations)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = load_inputs()
    failures = audit(data)
    if failures:
        for failure in failures:
            print(f"RED current_frontier_semantic_currency: {failure}")
        return 1
    print("PASS current_frontier_semantic_currency: live/history/owner facts")
    if args.selftest:
        caught, total = selftest(data)
        print(f"PASS hostile mutations caught: {caught}/{total}")
        return 0 if caught == total else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
