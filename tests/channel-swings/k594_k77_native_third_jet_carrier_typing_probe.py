#!/usr/bin/env python3
"""Independent controls and hostile mutations for K594."""

from __future__ import annotations

import copy
import json

from k594_k77_native_third_jet_carrier_typing import build


def controls(p: dict) -> list[bool]:
    j, t, a, d = p["selected_action_third_jet"], p["corrected_carrier_target"], p["type_audit"], p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY", p["direction"] == "observed_to_native",
        j["actual_selected_native_third_action_jet_serialized"] is True, j["complete_full_field_third_jet_serialized"] is False,
        j["serialized_coefficients"]["D3_t_t_t"] == "8736", j["serialized_coefficients"]["D3_t_v_v_over_native_norm"] == "-56/3",
        j["serialized_coefficients"]["K124_C_t_h_v_evaluations"] == 120, j["serialized_coefficients"]["K124_C_t_h_v_failures"] == 0,
        t["K589_degree_dimensions"] == [21, 91, 70], t["K441_carrier_rank"] == 512, t["K590_lifted_degree_dimensions"] == [10752, 46592, 35840],
        a["native_third_jet_is_scalar_trilinear"] is True, a["corrected_coupling_requires_carrier_endomorphism_valued_degree_arrow"] is True,
        a["field_to_carrier_soldering_map_serialized"] is False, a["carrier_to_field_injection_serialized"] is False,
        a["degree_sector_to_native_field_map_serialized"] is False, a["action_Riesz_map_on_K441_pairing_serialized"] is False,
        a["canonical_composition_exists_from_current_inputs"] is False, a["dimension_mismatch_alone_is_not_a_no_go"] is True,
        d["selected_native_third_action_jet_tested"] is True, d["selected_third_jet_defines_K441_endomorphism"] is False,
        d["K590_nonfactorized_square_test_released"] is False, d["K590_factorized_completion_retracted"] is False,
        d["selected_source_action_rejected"] is False, p["source_and_ledger_context"]["ledger_effect"] == "none", p["target_claim"] == "NONE-NOT-A-KILL",
    ]


def set_path(p: dict, path: tuple[object, ...], value: object) -> None:
    x = p
    for key in path[:-1]: x = x[key]
    x[path[-1]] = value


def main() -> int:
    p = build(); assert all(controls(p))
    mutations = [
        (("classification",), "SUPPORTED"), (("direction",), "native_to_observed"),
        (("selected_action_third_jet", "actual_selected_native_third_action_jet_serialized"), False),
        (("selected_action_third_jet", "complete_full_field_third_jet_serialized"), True),
        (("selected_action_third_jet", "serialized_coefficients", "D3_t_t_t"), "0"),
        (("selected_action_third_jet", "serialized_coefficients", "D3_t_v_v_over_native_norm"), "0"),
        (("selected_action_third_jet", "serialized_coefficients", "K124_C_t_h_v_evaluations"), 119),
        (("selected_action_third_jet", "serialized_coefficients", "K124_C_t_h_v_failures"), 1),
        (("corrected_carrier_target", "K589_degree_dimensions"), [21, 70, 91]),
        (("corrected_carrier_target", "K441_carrier_rank"), 256),
        (("corrected_carrier_target", "K590_lifted_degree_dimensions"), [1, 2, 3]),
        (("type_audit", "native_third_jet_is_scalar_trilinear"), False),
        (("type_audit", "corrected_coupling_requires_carrier_endomorphism_valued_degree_arrow"), False),
        (("type_audit", "field_to_carrier_soldering_map_serialized"), True),
        (("type_audit", "carrier_to_field_injection_serialized"), True),
        (("type_audit", "degree_sector_to_native_field_map_serialized"), True),
        (("type_audit", "action_Riesz_map_on_K441_pairing_serialized"), True),
        (("type_audit", "canonical_composition_exists_from_current_inputs"), True),
        (("type_audit", "dimension_mismatch_alone_is_not_a_no_go"), False),
        (("decision", "selected_native_third_action_jet_tested"), False),
        (("decision", "selected_third_jet_defines_K441_endomorphism"), True),
        (("decision", "K590_nonfactorized_square_test_released"), True),
        (("decision", "K590_factorized_completion_retracted"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_context", "ledger_effect"), "moved"), (("target_claim",), "SC-ACT-01"),
    ]
    rejected = 0
    for path, value in mutations:
        q = copy.deepcopy(p); set_path(q, path, value); rejected += int(not all(controls(q)))
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(controls(p)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__": raise SystemExit(main())
