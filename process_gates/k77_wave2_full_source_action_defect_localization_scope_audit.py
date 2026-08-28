#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 moving-defect localization packet."""

from __future__ import annotations

import json
from pathlib import Path

from k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit import historical_wave2_checkpoint


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-full-source-action-defect-localization.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-full-source-action-defect-localization-review.md"
SOURCE = ROOT / "lab/sources/gu-defect-localization-ward-bv-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_full_source_action_defect_localization_probe.py"


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
        "K77_FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_MOVING_SECTION_WARD_BV_DESCENT"
    )
    assert registry["gate_status"] == (
        "PARTIAL_WITH_EXACT_LOCALIZATION_AND_VARIATION_DESCENT"
    )
    assert registry["gate_after"] == (
        "K77_ACTUAL_I1B_CONORMAL_LEGENDRE_SYMBOL_BULK_DEFECT_WELD_AND_COMMON_VARIATION_DOMAIN"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE_AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "0_SELECTOR_PARAMETERS_FOR_CANONICAL_LOCALIZATION"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-MOVING-DEFECT-WARD-BV", "grade": "T3"}
    ]
    for kill in (
        "LITERAL_AMBIENT_TOP_FORM_PULLBACK",
        "EULER_FORMULA_WITHOUT_NORMAL_DIPOLE_OR_GRAPH_MIXING",
        "SHAPE_EQUATION_WITHOUT_SUPPORT_OR_DENSITY_MOTION",
        "WARD_OR_BV_CLAIM_WITH_FROZEN_REQUIRED_OWNER",
    ):
        assert kill in pre["preregistered_kills"]

    collision = registry["source_collision"]
    assert collision["first_order_i1b_and_full_augmented_torsion"] == "SOURCE_CONFIRMS"
    assert collision["completed_curvature_eddy_packet"] == "SOURCE_CONFIRMS"
    assert collision["xi_equals_d_upsilon_as_noether_bv"] == (
        "SOURCE_CORRECTS_FALSE_IDENTIFICATION"
    )
    assert collision["odd_action_as_default_gu_prerequisite"] == (
        "SOURCE_CORRECTS_NOT_REQUIRED_UNLESS_SEPARATELY_ASSERTED"
    )
    assert collision["induced_density_defect_localization"] == (
        "SOURCE_SILENT_RECONSTRUCTION"
    )
    assert collision["actual_i1b_conormal_legendre_symbol"] == (
        "SOURCE_SILENT_AND_UNCOMPUTED"
    )

    for value in registry["layer0"].values():
        assert value == "DISTINCT"

    localization = registry["localization"]
    assert localization["definition"] == (
        "LOC_S_L_EQUALS_INTEGRAL_X_OF_SCALAR_COEFFICIENT_AT_J1PHI_ON_S_TIMES_INDUCED_DENSITY"
    )
    assert localization["literal_top_form_pullback"] is False
    assert localization["coordinate_invariant"] is True
    assert localization["vertical_chart_orientation_reversal_exact"] is True
    assert localization["uses_vertical_orientation"] is False
    assert localization["uses_p1"] is False
    assert localization["selector_parameters"] == 0
    assert localization["new_datum"] == 0

    first = registry["first_variation"]
    assert first["monopole"] == "E0_EQUALS_MU_LPHI_MINUS_DI_MU_PI"
    assert first["normal_dipole"] == "EA_EQUALS_MU_PA_MINUS_SIA_PI"
    assert first["ambient_distribution"] == (
        "DELTA_S_E0_MINUS_PARTIAL_A_DELTA_S_EA"
    )
    assert first["graph_slope_mixing_exact"] is True
    assert first["direct_polynomial_variation_exact"] is True
    assert first["normal_dipole_nonzero_in_active_fixture"] is True
    assert first["actual_i1b_expansion"] == "OPEN"

    moving = registry["moving_section"]
    assert moving["shape_euler"] == (
        "PARTIAL_LHAT_PARTIAL_S_MINUS_DI_PARTIAL_LHAT_PARTIAL_SI"
    )
    assert moving["support_motion_exact"] is True
    assert moving["induced_density_motion_exact"] is True
    assert moving["direct_graph_derivative_exact"] is True
    assert moving["n3_current_derivative_extended"] is True
    assert moving["actual_full_shiab_hodge_connection_expansion"] == "OPEN"

    factor = registry["normal_jet_factorization"]
    assert factor["criterion"] == (
        "ALL_CONORMAL_LEGENDRE_COEFFICIENTS_PA_MINUS_SIA_PI_VANISH"
    )
    assert factor["source_shaped_proxy_nonfactorization_exact"] is True
    assert factor["same_zero_jet"] is True
    assert factor["same_tangential_first_jet"] is True
    assert factor["different_normal_first_jet"] is True
    assert factor["actual_moving_k77_i1b_symbol"] == "OPEN_NOT_INFERRED_FROM_PROXY"
    assert factor["retained_ambient_jet_is_new_datum"] is False
    assert factor["source_unowned_extension_law_introduced"] is False

    ward_bv = registry["ward_bv"]
    assert ward_bv["even_gauge_localization_functoriality"] == (
        "EXACT_GIVEN_COMPLETE_INVARIANT_SCALAR_AND_OWNER_LEDGER"
    )
    assert ward_bv["simultaneous_diffeomorphism_descent"] == (
        "EXACT_TO_TANGENTIAL_BOUNDARY_TERM"
    )
    assert ward_bv["section_motion_required"] is True
    assert ward_bv["density_motion_required"] is True
    assert ward_bv["dependent_b_epsilon_shiab_paths_required"] is True
    assert ward_bv["minimal_even_bv"] == (
        "CONDITIONAL_CLOSED_NILPOTENT_ALGEBRA_BOUNDARY_FREE_THEOREM"
    )
    assert ward_bv["primitive_full_field_even_bv_receipt"] == "OPEN"
    assert ward_bv["odd_superig_action_and_bv"] == (
        "OPEN_OPTIONAL_NOT_SOURCE_PREREQUISITE"
    )
    assert ward_bv["physical_bfv_green_domain"] == "OPEN"

    weld = registry["bulk_defect_weld"]
    assert weld["localization_operation_built"] is True
    assert weld["at_least_three_presentations"] == (
        "REPLACE_BULK__ADD_LOCALIZED_COPY__OR_LOCALIZE_ONLY_INDEPENDENT_DEFECT_TERMS__UNSELECTED_NONEXHAUSTIVE"
    )
    assert weld["relative_normalization"].startswith("AT_LEAST_ONE_TYPED")
    assert weld["dimensional_typing"] == "OPEN"
    assert weld["double_counting_audit"] == "OPEN"
    assert weld["common_variation_domain"] == "OPEN"

    assert registry["accounting"] == {
        "selector_parameters": 0,
        "new_free_coefficients_inserted": 0,
        "unselected_weld_normalization_classes": "AT_LEAST_1_NOT_COUNTED_AS_A_PARAMETER",
        "new_fields": 0,
        "new_projectors": 0,
        "new_data": 0,
        "free_object_delta": 0,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 11,
        "type": 22,
        "exact": 22,
        "planted": 14,
        "total": 69,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_MATERIAL_SCOPE_REPAIRS__ACTUAL_I1B_NORMAL_SYMBOL_AND_BULK_DEFECT_WELD_NOT_CLAIMED"
    )
    assert registry["next_required_build"] == registry["gate_after"]
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["p1_p2_p3_used"] is False
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    required_emissions = (
        "CANONICAL_INDUCED_DENSITY_DEFECT_LOCALIZATION",
        "PATCH_DESCENT_ACROSS_VERTICAL_ORIENTATION_REVERSAL_WITHOUT_P1",
        "FIRST_ORDER_SECTION_SUPPORTED_EULER_MONOPOLE_PLUS_NORMAL_DIPOLE",
        "GRAPH_SLOPE_CONORMAL_LEGENDRE_COEFFICIENT",
        "MOVING_SECTION_SUPPORT_PLUS_INDUCED_DENSITY_SHAPE_EULER",
        "SOURCE_SHAPED_NORMAL_JET_NONFACTORIZATION_WITNESS",
        "LOCALIZATION_FUNCTOR_PRESERVES_COMPLETE_EVEN_WARD_IDENTITY",
        "CONDITIONAL_CLOSED_EVEN_ALGEBRA_BV_DESCENT",
        "ODD_ACTION_NOT_DEFAULT_SOURCE_PREREQUISITE",
    )
    historical_wave2_checkpoint(campaign, required_emissions)

    for phrase in (
        "canonical induced-density localization",
        "monopole and normal-dipole currents",
        "e_a=\\mu_s(p^a-s_i^ap^i)",
        "moving section and density",
        "source-shaped witness",
        "does **not** yet prove the actual moving k77 shiab coefficient",
        "minimal even bv",
        "bulk/defect weld is still a separate construction",
        "at least one typed normalization class",
        "k77_actual_i1b_conormal_legendre_symbol_bulk_defect_weld_and_common_variation_domain",
        "p1/p2/p3 | unchanged and unused",
        "wave 3 | closed",
    ):
        assert phrase in report
    assert "search_space_dim: \"0 selector parameters" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends a superseded object",
        "source-shaped normal-jet witness",
        "actual `i1b` conormal symbol",
        "at least one",
        "pass_with_material_scope_repairs",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-corrects",
        "source-silent",
        "first-order ambient action",
        "full odd action is not a default source prerequisite",
        "actual moving k77 shiab/i1b density",
    ):
        assert phrase in source

    for phrase in (
        "monopole plus normal-dipole pairing",
        "support plus density motion",
        "source-shaped first-order localized density distinguishes the normal jets",
        "localization commutes with the pointwise even gauge identity",
        "wave3=closed",
        "actual_i1b_conormal_legendre=open",
    ):
        assert phrase in probe

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md" in surface
        assert "k77_actual_i1b_conormal_legendre_symbol_bulk_defect_weld_and_common_variation_domain" in surface
    assert "k77_wave2_full_source_action_defect_localization_scope_audit.py" in gates_readme
    assert "revision 35" in improvement
    assert "localizing a first-order action emits normal dipoles" in improvement

    print("k77_wave2_full_source_action_defect_localization_scope_audit: PASS")
    print("  canonical density localization; exact monopole/dipole and shape calculus")
    print("  conditional even descent; actual K77 symbol, weld and domain remain open")


if __name__ == "__main__":
    main()
