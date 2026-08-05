#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 augmented-torsion receiver packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-augmented-torsion-defect-euler-receiver.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-augmented-torsion-defect-euler-receiver-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-augmented-torsion-defect-euler-receiver-review.md"
SOURCE = ROOT / "lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_augmented_torsion_defect_euler_receiver_probe.py"


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
        "K77_ACTION_DERIVED_HORIZONTAL_EULER_IMAGE_OR_DEFECT_VARIATIONAL_RECEIVER"
    )
    assert registry["gate_status"] == "PARTIAL_WITH_DECISIVE_ROUTE_SELECTION"
    assert registry["gate_after"] == (
        "K77_FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_MOVING_SECTION_WARD_BV_DESCENT"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE-AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == (
        "0_SELECTOR_PARAMETERS_AFTER_SECTION_AND_EXISTING_VERTICAL_RESTRICTION"
    )
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-ACTUAL-Y14-RECEIVER", "grade": "T3"}
    ]

    source_collision = registry["source_collision"]
    assert source_collision["augmented_torsion_full_upstairs_one_form"] == "SOURCE_CONFIRMS"
    assert source_collision["two_connection_difference"] == "SOURCE_CONFIRMS"
    assert source_collision["tilted_equivariance_intent"] == (
        "SOURCE_CONFIRMS_NOT_FULL_WARD_THEOREM"
    )
    assert source_collision["pullback_only_observer_reading"] == (
        "SOURCE_CORRECTS_NAIVE_READING"
    )
    assert source_collision["pullback_plus_vertical_coefficient_retention"] == (
        "SOURCE_GUIDES_AND_REPO_ALREADY_BUILT"
    )
    assert source_collision["inverse_transpose_euler_receiver"] == (
        "SOURCE_SILENT_RECONSTRUCTION"
    )

    for value in registry["layer0"].values():
        assert value == "DISTINCT"

    field = registry["field_receiver"]
    assert field["map"] == "F_S_EQUALS_PAIR_S_STAR_AND_RES_S_VERTICAL"
    assert field["pullback_rank"] == 4
    assert field["vertical_restriction_rank"] == 10
    assert field["combined_rank"] == 14
    assert field["determinant"] == 1
    assert field["inverse_exact"] is True
    assert field["new_field_introduced"] is False

    equation = registry["equation_receiver"]
    assert equation["map"] == "R_DEFECT_EQUALS_M_INVERSE_TRANSPOSE"
    assert equation["rank"] == 14
    assert equation["vertical_row"] == "E_V_MINUS_J_E_H"
    assert equation["complete_pairing_exact"] is True
    assert equation["coefficient_factor_equivariance_exact"] is True
    assert equation["moving_jet_pairing_exact"] is True
    assert equation["global_tilted_and_diffeomorphism_descent"] == "OPEN"

    degree = registry["degree_receiver"]
    assert degree["ambient_degree"] == 13
    assert degree["connection_equation_count"] == 4
    assert degree["vertical_equation_count"] == 10
    assert degree["connection_output_degree"] == 3
    assert degree["vertical_output_degree"] == 4
    assert degree["top_form_pairing_exact"] is True
    assert degree["uses_oriented_volume"] is False
    assert degree["uses_p1"] is False

    horizontal = registry["action_horizontal_route"]
    assert horizontal["automatic_horizontality"] == (
        "KILLED_ON_DISPLAYED_NONZERO_KAPPA_FULL_LOCAL_TRANSLATION_STRATUM"
    )
    assert horizontal["exterior_derivative"] == 0
    assert horizontal["self_bracket"] == 0
    assert horizontal["curvature_contribution"] == 0
    assert horizontal["kappa_value_nonzero"] is True
    assert horizontal["ordinary_pullback"] == 0
    assert horizontal["vertical_receiver_nonzero"] is True
    assert horizontal["source_derived_restricted_variation_domain_could_exclude_fixture"] is True
    assert horizontal["kappa_zero_case_proves_horizontality"] is False
    assert horizontal["global_source_domain_characterized"] is False

    localization = registry["localization_route"]
    assert localization["selected_successor"] == (
        "FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_WITH_FOUR_PLUS_TEN_FIELDS"
    )
    assert localization["literal_top_form_pullback_allowed"] is False
    assert localization["current_or_induced_vertical_density_required"] is True
    assert localization["prior_moving_support_derivative"] == "BUILT_IN_N3"
    for key in (
        "moving_section_jet_variation",
        "moving_vertical_density_variation",
        "moving_hodge_shiab_connection_variation",
        "full_tilted_ward_bv_identity",
        "patch_descent",
        "complete_source_action_weld",
    ):
        assert localization[key] == "OPEN"

    assert registry["accounting"] == {
        "selector_parameters": 0,
        "new_free_coefficients": 0,
        "new_projectors": 0,
        "new_data": 0,
        "free_object_delta": 0,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 11,
        "type": 28,
        "exact": 43,
        "planted": 9,
        "total": 91,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_MATERIAL_SCOPE_REPAIR__FULL_LOCAL_TRANSLATION_DOMAIN_AND_NONZERO_KAPPA_CONDITIONALIZED__DEFECT_LOCALIZATION_NOT_CLAIMED"
    )
    assert registry["next_required_build"] == (
        "K77_FULL_SOURCE_ACTION_DEFECT_LOCALIZATION_MOVING_SECTION_WARD_BV_DESCENT"
    )
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    continuation = next(
        item
        for item in wave2["continuations"]
        if item["named_gate"] == registry["named_gate"]
    )
    assert continuation["named_gate"] == registry["named_gate"]
    assert continuation["result_ref"] == (
        "explorations/k77-wave2-augmented-torsion-defect-euler-receiver-2026-08-05.md"
    )
    assert continuation["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "NONZERO_KAPPA_CONORMAL_SOURCE_ACTION_WITNESS",
        "AUTOMATIC_FULL_TRANSLATION_DOMAIN_HORIZONTALITY_KILLED",
        "CANONICAL_PULLBACK_PLUS_VERTICAL_COEFFICIENT_FIELD_ISOMORPHISM",
        "INVERSE_TRANSPOSE_DEFECT_EULER_RECEIVER",
        "OMEGA13_FOUR_PLUS_TEN_BIGRADING",
        "DEGREE3_CONNECTION_PLUS_VERTICAL_VALUED_DEGREE4_EQUATIONS",
        "LOCAL_RECEIVER_RANK14_PAIRING_EXACT",
    ):
        assert emitted in wave2["emitted"]
    for debt in (
        "COMPLETE_SOURCE_ACTION_DEFECT_CURRENT_LOCALIZATION",
        "MOVING_SECTION_AND_VERTICAL_DENSITY_VARIATION",
        "FULL_TILTED_WARD_BV_AND_GLOBAL_DESCENT",
        "ACTUAL_POST_OBSERVATION_COEFFICIENT_MODULE_AND_IMAGE_FAITHFULNESS",
        "COMMON_CLOSED_KREIN_GREEN_DOMAIN",
    ):
        assert debt in continuation["replacement_debt"]
    assert any(
        item["next_required_build"] == registry["next_required_build"]
        for item in wave2["continuations"]
    )

    for phrase in (
        "the canonical field map along a section",
        "e_q=m^{-t}e_a",
        "e_v-je_h",
        "degree-correct four-plus-ten split",
        "displayed full local translation domain when",
        "source-derived constrained variation domain",
        "vertical-scalar equation",
        "k77_full_source_action_defect_localization_moving_section_ward_bv_descent",
        "p1/p2/p3 | unchanged and unused",
        "wave 3 | closed",
    ):
        assert phrase in report
    assert "search_space_dim: \"0 selector parameters" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends a superseded object",
        "the full action image is not horizontal",
        "receiver is not yet the localized action",
        "pass_with_material_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-corrects-naive-reading",
        "source-guides",
        "source-silent",
        "is not permission to erase the vertical coefficient sector",
    ):
        assert phrase in source

    for phrase in (
        "kappa term emits the nonzero source euler witness",
        "equation-dual receiver is the inverse transpose",
        "degree-three plus bundle-valued degree-four pairing",
        "wave 3 remains closed",
    ):
        assert phrase in probe

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    tests_readme = normalized(ROOT / "tests/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-augmented-torsion-defect-euler-receiver-2026-08-05.md" in surface
        assert "k77_full_source_action_defect_localization_moving_section_ward_bv_descent" in surface
    assert "channel-swings/` (" in tests_readme
    assert "k77_wave2_augmented_torsion_defect_euler_receiver_probe.py" in tests_readme
    assert "k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit.py" in gates_readme
    assert "revision 34" in improvement
    assert "pullback and vertical coefficient restriction precede normal loss" in improvement

    actual_channel_probes = len(list((ROOT / "tests/channel-swings").glob("*.py")))
    assert actual_channel_probes >= 179

    print("k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit: PASS")
    print("  source collision retains the full augmented-torsion carrier")
    print("  exact four-plus-ten field/equation receiver; scoped horizontality kill")
    print("  full moving defect action, Ward/BV descent and domain remain open")


if __name__ == "__main__":
    main()
