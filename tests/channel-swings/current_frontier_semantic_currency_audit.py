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
        check("K614" in live and "K441" in live, "K77 zero-form injection boundary missing")
        check("nonzero" in live and "zero-form fermion" in live,
              "K77 nonzero-background reopener missing")
        check("K596" in live and "K598" in live,
              "K77 discriminator/transport succession missing")
        check("K609" in live and "below 1/3" in live,
              "K500 complete leakage route missing")
        check("K612" in live and "cancelled-core" in live,
              "K500 quantitative-custody obstruction missing")
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
