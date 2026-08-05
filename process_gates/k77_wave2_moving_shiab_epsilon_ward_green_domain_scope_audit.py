#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 moving-Shiab/epsilon/Green packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-moving-shiab-epsilon-ward-green-domain.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-moving-shiab-epsilon-ward-green-domain-review.md"
SOURCE = ROOT / "lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"


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
        "K77_MOVING_SHIAB_MIXED_NORMAL_COEFFICIENT_DEPENDENT_EPSILON_WARD_AND_TRACE_CLOSED_GREEN_DOMAIN"
    )
    assert registry["gate_status"] == (
        "PARTIAL_WITH_EXACT_MOVING_FAMILY_PRIMITIVE_CHAIN_AND_FORMAL_GREEN_PAIR"
    )
    assert registry["gate_after"] == (
        "K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE_AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "8_DISCRETE_SOURCE_CHANNELS_ZERO_FITTED_PARAMETERS"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-MOVING-SHIAB-EPSILON-GREEN", "grade": "T4"}
    ]
    assert len(pre["preregistered_kills"]) == 6

    collision = registry["source_collision"]
    assert collision["displayed_phi_conjugated_shiab_family"] == "SOURCE_CONFIRMS"
    assert collision["preferred_historical_selector"] == (
        "SOURCE_SILENT_EXPLICITLY_UNLOCATED"
    )
    assert collision["overbundled_hodge_density_soldering_epsilon_chain"] == (
        "SOURCE_CORRECTS_TO_SEPARATE_PRIMITIVE_VARIATIONS"
    )
    assert collision["global_coupled_physical_domain"] == "SOURCE_SILENT"
    assert all(value == "DISTINCT" for value in registry["layer0"].values())

    mixed = registry["mixed_normal_family"]
    assert mixed["ambient_two_form_dimension"] == 91
    assert mixed["tangent_two_form_dimension"] == 6
    assert mixed["mixed_normal_two_form_dimension"] == 85
    assert mixed["channels_enumerated"] == 8
    assert mixed["continuous_fitted_parameters"] == 0
    assert mixed["all_channels_live_support"] == 85
    assert mixed["selected_slice_ranks"] == [85, 85, 85, 85, 10, 10, 85, 85]
    assert mixed["full_grade_one_ranks"] == [1190, 1190, 1190, 1190, 14, 14, 374, 374]
    assert mixed["zero_jet_mixed_normal_annihilator_found"] is False
    assert mixed["preferred_product_channel"] == "OPEN"

    moving = registry["moving_shiab"]
    assert moving["analytic_equals_dual_number"] is True
    assert moving["moving_contribution_live"] is True
    assert moving["epsilon_action"] == "INVERTIBLE_CONJUGATION_ORBIT"
    assert moving["rank_preserved"] is True
    assert moving["selector_supplied"] is False

    epsilon = registry["primitive_epsilon"]
    assert epsilon["delta_b"] == "D_B_ETA"
    assert epsilon["delta_t"] == "MINUS_D_B_ETA"
    assert epsilon["euler_row"] == (
        "D_B_ADJOINT_E_B_MINUS_E_T_PLUS_D_EPSILON_SHIAB_ADJOINT_K_SHIAB"
    )
    assert epsilon["direct_chain_rule_exact"] is True
    assert epsilon["hodge_metric_density_section_in_same_primitive_chain"] is False
    assert epsilon["fixed_epsilon_translation_repaired_by_this_row"] is False

    ward = registry["ward"]
    assert ward["complete_owner_contraction_zero"] is True
    assert ward["moving_shiab_owner_required"] is True
    assert ward["inhomogeneous_connection_direction_required"] is True
    assert ward["odd_superig_bv"] == "OPEN"

    domain = registry["green_domain"]
    assert domain["gauge_parameters"] == "H10_INTERSECT_H1_0"
    assert domain["euler_difference"] == "H9"
    assert domain["closed_graph"] is True
    assert domain["dirichlet_boundary_flux"] == 0
    assert domain["value_trace"] == "H9_Y_TO_H4_X"
    assert domain["first_jet_trace"] == "H9_Y_TO_H3_X"
    for key in (
        "global_noncompact_y14",
        "coupled_krein_self_adjoint",
        "hyperbolic_maximal_dissipative",
        "physical_bfv_phase_space",
    ):
        assert domain[key] == "OPEN"

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
        "source": 8,
        "type": 18,
        "exact": 15,
        "planted": 9,
        "total": 50,
        "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    continuation = wave2["latest_advance"]
    assert continuation["named_gate"] == registry["named_gate"]
    assert continuation["result_ref"] == (
        "explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md"
    )
    assert continuation["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "EXHAUSTIVE_EIGHT_CHANNEL_K77_MOVING_SHIAB_FAMILY",
        "ALL_EIGHT_CHANNELS_HAVE_85_OF_85_MIXED_NORMAL_SUPPORT",
        "FULL_GRADE_ONE_RANK_VECTOR_1190_1190_1190_1190_14_14_374_374",
        "MOVING_EPSILON_CONJUGATION_PRESERVES_SUPPORT_AND_RANK",
        "PRIMITIVE_EPSILON_EULER_CHAIN",
        "COMPLETE_OFFSHELL_HOMOGENEOUS_EVEN_WARD_OWNER_FIXTURE",
        "COMPACT_CORE_H10_TO_H9_CLOSED_GREEN_GRAPH",
    ):
        assert emitted in wave2["emitted"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "support is not coefficient rank",
        "1190,1190,1190,1190,14,14,374,374",
        "epsilon orbit provides the correct equivariant family motion but no discriminator",
        "boxed{e_\\epsilon",
        "compact-core",
        "not a global physical domain",
        "p1/p2/p3 | unchanged and unused",
        "wave 3 | closed",
        "k77_action_derived_polarized_euler_shiab_product_selector_and_global_coupled_krein_green_observation_domain",
    ):
        assert phrase in report
    assert "search_space_dim: \"8 discrete source-permitted" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns the artifact",
        "rigor defends a superseded object",
        "support is 85",
        "compact-core dirichlet closure",
        "no preferred product channel",
        "pass_with_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-corrects",
        "source-silent",
        "hodge, density, metric and observation-section derivatives are separate",
        "d_b^!(e_b-e_t)",
    ):
        assert phrase in source

    for phrase in (
        "all eight source-permitted channels have all eighty-five exterior directions live",
        "support is not misreported as full rank",
        "analytic derivative equals exact dual-number differentiation",
        "primitive direct variation equals",
        "complete homogeneous even ward contraction vanishes",
        "dirichlet primitive epsilon data gives the exact zero-flux green identity",
        "no standard model gr particle dark-sector",
    ):
        assert phrase in probe

    print("PASS: K77 moving-Shiab/epsilon/Green packet remains exact and scope-fenced")


if __name__ == "__main__":
    main()
