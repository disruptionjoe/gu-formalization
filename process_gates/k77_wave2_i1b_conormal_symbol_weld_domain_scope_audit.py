#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 I1B conormal/weld/domain packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-i1b-conormal-symbol-weld-domain.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-i1b-conormal-symbol-weld-domain-review.md"
SOURCE = ROOT / "lab/sources/gu-i1b-conormal-weld-domain-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_i1b_conormal_symbol_weld_domain_probe.py"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def main() -> None:
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    report = normalized(REPORT)
    review = normalized(REVIEW)
    source = normalized(SOURCE)
    probe = normalized(PROBE)

    assert registry["named_gate"] == (
        "K77_ACTUAL_I1B_CONORMAL_LEGENDRE_SYMBOL_BULK_DEFECT_WELD_AND_COMMON_VARIATION_DOMAIN"
    )
    assert registry["gate_status"] == (
        "PARTIAL_WITH_EXACT_FAMILY_SYMBOL_AND_WELD_SELECTION"
    )
    assert registry["gate_after"] == (
        "K77_MOVING_SHIAB_MIXED_NORMAL_COEFFICIENT_DEPENDENT_EPSILON_WARD_AND_TRACE_CLOSED_GREEN_DOMAIN"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE_AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "0_FITTED_SELECTOR_PARAMETERS"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-I1B-CONORMAL-WELD-DOMAIN", "grade": "T4"}
    ]
    for kill in (
        "UNEARNED_SELECTED_K77_SHIAB_COEFFICIENT",
        "ZERO_JET_DEFECT_ACTION_WITH_LIVE_MIXED_NORMAL_SYMBOL",
        "K95_OR_GENERIC_FIXTURE_PROMOTED_TO_K77_SOURCE_IDENTITY",
        "BULK_PLUS_LOCALIZED_BULK_WITHOUT_NORMAL_DENSITY_AND_DOUBLE_COUNTING_THEOREM",
        "COMMON_DOMAIN_WITHOUT_CODIMENSION_TEN_TRACE_REGULARITY",
    ):
        assert kill in pre["preregistered_kills"]

    collision = registry["source_collision"]
    assert collision["i1b_transgression_grammar"] == "SOURCE_CONFIRMS"
    assert collision["fixed_epsilon_translation_variation"] == "SOURCE_CONFIRMS"
    assert collision["upstairs_action_and_pullback_observation"] == "SOURCE_CONFIRMS"
    assert collision["no_duplicate_weld"] == (
        "SOURCE_GUIDES_RECONSTRUCTION_NOT_UNIQUENESS_THEOREM"
    )
    assert collision["preferred_k77_shiab"] == (
        "SOURCE_SILENT_UNSELECTED_FAMILY_MEMBER"
    )
    assert collision["complete_variation_green_bfv_domain"] == "SOURCE_SILENT"

    for value in registry["layer0"].values():
        assert value == "DISTINCT"

    symbol = registry["principal_symbol"]
    assert symbol["grade"] == "EXACT_FAMILY_LEVEL_FIXED_EPSILON"
    assert symbol["b_symbol"] == "MU_S_PAIR_T_SHIAB_NU_WEDGE_BETA"
    assert symbol["t_symbol"] == "MU_S_OVER_2_PAIR_T_SHIAB_NU_WEDGE_ALPHA"
    assert symbol["b_to_t_ratio_same_direction"] == "2_TO_1"
    assert symbol["graph_conormal"] == "NU_A_EQUALS_DY_A_MINUS_S_I_A_DX_I"
    assert symbol["mass_contribution"] == 0
    assert symbol["cubic_eddy_principal_contribution"] == 0
    assert symbol["direct_jet_differentiation_exact"] is True
    assert symbol["generic_rational_nonvacuity_fixture"] is True
    assert symbol["fixture_is_selected_k77_shiab"] is False
    assert symbol["preferred_k77_coefficient_table"] == "OPEN"

    factor = registry["factorization"]
    assert factor["ambient_two_form_dimension"] == 91
    assert factor["fixed_tangent_two_form_dimension"] == 6
    assert factor["fixed_mixed_normal_two_form_dimension"] == 85
    assert factor["fixed_zero_symbol_entries_per_paired_adjoint_block"] == 1190
    assert factor["fixed_unconstrained_tangential_entries_per_paired_adjoint_block"] == 84
    assert factor["all_section_entries_per_paired_adjoint_block"] == 1274
    assert factor["all_section_theorem"] == (
        "ARBITRARY_T_PLUS_NONDEGENERATE_PAIRING_PLUS_ALL_SPLITTINGS_FORCES_SHIAB_ZERO"
    )
    assert factor["normal_first_jet_retained"] is True
    assert factor["new_extension_law"] is False
    assert factor["new_datum"] is False

    weld = registry["weld"]
    assert weld["selected_primary"] == (
        "BULK_SOURCE_LAYERS_PLUS_ONLY_INDEPENDENT_DIRECT_X_ACTIONS"
    )
    assert weld["bulk_i1b_copies"] == 1
    assert weld["observation_role"] == (
        "FIELD_AND_EULER_RECEIVER_NOT_SECOND_ACTION_OWNER"
    )
    assert weld["duplicate_localized_bulk"] == "NOT_INSERTED"
    assert weld["duplicate_invariant_debt"] == (
        "NORMAL_DENSITY_VALUE_OR_TRANSVERSE_PROFILE"
    )
    assert weld["homogeneous_length_comparator"] == "LENGTH_POWER_10"
    assert weld["homogeneous_units_claimed_for_metric_fibre"] is False
    assert weld["uniqueness_claimed"] is False

    domain = registry["variation_domain"]
    assert domain["fixed_section_ambient_fields"] == "H9"
    assert domain["fixed_section_gauge_parameters"] == "H10"
    assert domain["codimension"] == 10
    assert domain["value_trace"] == "H9_Y_TO_H4_X"
    assert domain["first_jet_trace"] == "H9_Y_TO_H3_X"
    assert domain["moving_section_sobolev_composition"] == "OPEN"
    assert domain["closed_krein_green_hyperbolic_bfv_domain"] == "OPEN"

    primitive = registry["primitive_owner_ledger"]
    assert primitive["fixed_epsilon_t_symbol"] == "BUILT"
    assert primitive["independent_b_owner_audit"] == (
        "BUILT_NOT_INDEPENDENT_PHYSICAL_ROOT"
    )
    assert primitive["d_epsilon_b_chain"] == "OPEN"
    assert primitive["moving_shiab_owner"] == "OPEN"
    assert primitive["gauge_projector"] is False
    assert primitive["physical_bfv"] is False

    assert registry["accounting"] == {
        "fitted_selector_parameters": 0,
        "new_free_coefficients_inserted": 0,
        "new_fields": 0,
        "new_projectors": 0,
        "new_data": 0,
        "free_object_delta": 0,
        "p1_p2_p3_used": False,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 11,
        "type": 31,
        "exact": 25,
        "planted": 8,
        "total": 75,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_SCOPE_REPAIR__FAMILY_SYMBOL_AND_NO_DUPLICATE_WELD_BUILT__PREFERRED_SHIAB_DEPENDENT_EPSILON_AND_CLOSED_DOMAIN_OPEN"
    )
    assert registry["next_required_build"] == registry["gate_after"]
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    continuation = wave2["continuations"][-1]
    assert continuation["named_gate"] == registry["named_gate"]
    assert continuation["result_ref"] == (
        "explorations/k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md"
    )
    assert continuation["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "I1B_SELECTOR_INDEPENDENT_CONORMAL_PRINCIPAL_SYMBOL",
        "INDEPENDENT_B_TO_T_CONORMAL_RATIO_TWO_TO_ONE",
        "FIXED_SECTION_MIXED_NORMAL_SHIAB_BLOCK_85_OF_91",
        "ALL_SECTION_ZERO_JET_FACTORIZATION_FORCES_ZERO_SHIAB_UNDER_EXPLICIT_HYPOTHESES",
        "NORMAL_FIRST_JET_RETAINED_WITHOUT_NEW_DATUM",
        "SOURCE_GUIDED_BULK_PLUS_ONLY_INDEPENDENT_X_DEFECT_WELD",
        "DUPLICATE_LOCALIZED_BULK_NORMAL_DENSITY_DEBT",
        "SMOOTH_COMMON_VARIATION_CORE",
        "FIXED_SECTION_H9_FIELDS_H10_GAUGE_TRACE_COMPLETION",
    ):
        assert emitted in wave2["emitted"]
    for debt in (
        "PREFERRED_SOURCE_COMPATIBLE_MOVING_OR_DERIVATIVE_K77_SHIAB",
        "FULL_FIXED_SECTION_85_COLUMN_MIXED_NORMAL_COEFFICIENT_BLOCK",
        "DEPENDENT_EPSILON_B_SHIAB_HODGE_DENSITY_SOLDERING_SYMBOL_AND_EVEN_BV_LEDGER",
        "MOVING_SECTION_SOBOLEV_COMPOSITION_AND_BOUNDARY_CONDITIONS",
        "TRACE_COMPATIBLE_CLOSED_KREIN_GREEN_DOMAIN",
    ):
        assert debt in continuation["replacement_debt"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "actual **written i1b action family**",
        "sigma_b=2 sigma_t",
        "85 of the 91",
        "per paired adjoint coefficient block",
        "normal-density normalization or transverse profile",
        "source-guided reconstruction choice",
        "h^9",
        "not yet a closed krein",
        "preferred coefficient table remains open",
        "p1/p2/p3 | unchanged and unused",
        "wave 3 | closed",
        "k77_moving_shiab_mixed_normal_coefficient_dependent_epsilon_ward_and_trace_closed_green_domain",
    ):
        assert phrase in report
    assert "search_space_dim: \"0 fitted selector parameters" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends superseded object",
        "length^10",
        "per paired adjoint coefficient block",
        "not a uniqueness theorem",
        "pass_with_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-guides",
        "source-silent",
        "all the action",
        "observed by pullback",
        "normal-density",
        "no second localized copy",
    ):
        assert phrase in source

    for phrase in (
        "b_to_t_principal_ratio=2_to_1",
        "fixed_section_mixed_normal_shiab_columns=85_of_91",
        "selected_k77_shiab_coefficients=open",
        "weld=bulk_i1b_plus_only_independent_defect_actions",
        "common_variation_core=smooth_dense_with_fixed_section_h9_trace_completion",
        "closed_green_domain=open",
        "wave3=closed",
    ):
        assert phrase in probe

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    tests_readme = normalized(ROOT / "tests/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-i1b-conormal-symbol-bulk-defect-weld-domain-2026-08-05.md" in surface
        assert registry["next_required_build"].lower() in surface
    assert "channel-swings/` (181)" in tests_readme
    assert "k77_wave2_i1b_conormal_symbol_weld_domain_probe.py" in tests_readme
    assert "k77_wave2_i1b_conormal_symbol_weld_domain_scope_audit.py" in gates_readme
    assert "revision 36" in improvement
    assert "compute an unselected-family symbol" in improvement

    actual_channel_probes = len(list((ROOT / "tests/channel-swings").glob("*.py")))
    assert actual_channel_probes == 181

    print("k77_wave2_i1b_conormal_symbol_weld_domain_scope_audit: PASS")
    print("  exact family symbol and 85/91 annihilator; no duplicate weld")
    print("  common trace domain only; preferred Shiab, epsilon chain and Green open")


if __name__ == "__main__":
    main()
