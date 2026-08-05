#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 actual-Y14 receiver-ordering packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-actual-y14-receiver-ordering-conormal.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-actual-y14-receiver-ordering-review.md"
SOURCE = ROOT / "lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md"


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

    assert registry["named_gate"] == (
        "K77_ACTUAL_Y14_EULER_RECEIVER_FAITHFUL_MODULE_AND_COMMON_GREEN_DOMAIN"
    )
    assert registry["gate_status"] == "PARTIAL_WITH_NAMED_MOVEMENT"

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE-AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == (
        "0_SELECTOR_PARAMETERS_IN_ORDINARY_SECTION_PULLBACK_CLASS"
    )
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-ACTUAL-Y14-RECEIVER", "grade": "T3"}
    ]

    source_collision = registry["source_collision"]
    assert source_collision["observerse_section_field_pullback"] == "SOURCE_CONFIRMS"
    assert source_collision["ten_plus_four_trace_reversed_geometry"] == "SOURCE_CONFIRMS"
    assert source_collision["contracted_euler_one_form_reading"] == "SOURCE_GUIDES"
    assert source_collision["direct_omega13_equation_pullback"] == (
        "SOURCE_SILENT_AND_DIMENSIONALLY_ZERO"
    )
    assert source_collision["action_euler_image_horizontality"] == "SOURCE_SILENT"
    assert source_collision["normal_equation_receiver"] == "SOURCE_SILENT"
    assert source_collision["defect_or_induced_density_reduction"] == (
        "SOURCE_SILENT_WITH_PRIOR_N3_CONSTRUCTION"
    )

    for value in registry["layer0"].values():
        assert value == "DISTINCT"

    geometry = registry["k77_local_geometry"]
    assert geometry["horizontal_inertia"] == [1, 3]
    assert geometry["raw_fibre_inertia"] == [7, 3]
    assert geometry["trace_reversed_fibre_inertia"] == [6, 4]
    assert geometry["total_inertia"] == [7, 7]
    assert geometry["section_graph_rank"] == 4
    assert geometry["induced_graph_metric_nondegenerate"] is True
    assert geometry["global_section_existence_claimed"] is False

    theorem = registry["receiver_theorem"]
    assert theorem["direct_omega13_pullback_rank"] == 0
    assert theorem["primalize_then_restrict_rank"] == 4
    assert theorem["primalize_then_restrict_kernel_dimension"] == 10
    assert theorem["kernel_identification"] == "SECTION_CONORMAL_BUNDLE"
    assert theorem["faithful_downstream_module_repairs_conormal_loss"] is False
    assert theorem["metric_horizontal_right_inverse_exact"] is True
    assert theorem["action_image_horizontality_condition"] == "Q_RY_UPSILON_T_EQUALS_ZERO"
    assert theorem["action_image_horizontality_proved"] is False

    alternative = registry["alternative_receiver"]
    assert alternative["tangent_plus_normal_decoder_rank"] == 14
    assert alternative["normal_output_dimension"] == 10
    assert alternative["algebraically_faithful"] is True
    assert alternative["source_owned"] is False
    assert alternative["physical_identification"] == "OPEN"
    assert alternative["fibre_pushforward_degree"] == 3

    reduction = registry["action_reduction_route"]
    assert reduction["literal_omega14_pullback_rank"] == 0
    assert reduction["prior_moving_defect_first_variation"] == "BUILT_IN_N3"
    assert reduction["induced_density_or_thom_current_required"] is True
    assert reduction["complete_source_action_defect_weld"] == "OPEN"
    assert reduction["projection_variation_commutation"] == "OPEN"

    boundary = registry["domain_boundary"]
    assert boundary["finite_horizontal_invariance_condition"] == "Q_D_H_EQUALS_ZERO"
    assert boundary["hostile_same_observed_block_with_normal_leakage"] is True
    assert boundary["actual_operator_invariance_built"] is False
    assert boundary["common_closed_krein_green_domain_built"] is False
    assert boundary["odd_bv_closure_built"] is False

    assert registry["accounting"] == {
        "selector_parameters": 0,
        "new_free_coefficients": 0,
        "new_normal_fields_admitted": 0,
        "free_object_delta": 0,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 7,
        "type": 31,
        "exact": 33,
        "planted": 8,
        "total": 79,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_MATERIAL_SCOPE_REPAIR__THIRD_DEFECT_VARIATIONAL_ROUTE_RESTORED"
    )
    assert registry["next_required_build"] == (
        "K77_ACTION_DERIVED_HORIZONTAL_EULER_IMAGE_OR_DEFECT_VARIATIONAL_RECEIVER"
    )
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    continuation = wave2["continuations"][-1]
    assert continuation["named_gate"] == registry["named_gate"]
    assert continuation["result_ref"] == (
        "explorations/k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md"
    )
    assert continuation["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "DIRECT_OMEGA13_SECTION_PULLBACK_IDENTICALLY_ZERO",
        "PRIMALIZE_THEN_RESTRICT_RANK_FOUR_CONORMAL_RANK_TEN",
        "METRIC_HORIZONTAL_RIGHT_INVERSE_AND_ACTION_IMAGE_CONDITION",
        "MOVING_DEFECT_VARIATION_RESTORED_AS_THIRD_RECEIVER_ROUTE",
    ):
        assert emitted in wave2["emitted"]
    for debt in (
        "COMPLETE_ACTION_EULER_IMAGE_HORIZONTALITY",
        "COMPLETE_SOURCE_ACTION_TO_MOVING_DEFECT_DENSITY_VARIATION_WELD",
        "TYPED_NORMAL_RECEIVER_IF_BOTH_RESTRICTED_ROUTES_FAIL",
        "COMMON_CLOSED_KREIN_GREEN_DOMAIN",
    ):
        assert debt in continuation["replacement_debt"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "direct pullback of the source euler 13-form cannot be the nontrivial observed",
        "rank-ten conormal kernel",
        "q\\,r_y\\upsilon_t=0",
        "the third route: reduce the action honestly, then vary",
        "this is not literal pullback of a 14-form",
        "| `free_object_delta` | `0` |",
        "p1/p2/p3 | unchanged and unused",
        "wave 3 | closed",
    ):
        assert phrase in report
    assert "search_space_dim: 0 selector parameters" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "fence defends a superseded object",
        "false exhaustive fork",
        "old top-form pullback notation is not literal",
        "pass_with_material_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-guides",
        "source-silent",
        "literal pullback of the ambient 14-form",
    ):
        assert phrase in source

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    tests_readme = normalized(ROOT / "tests/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-actual-y14-receiver-ordering-conormal-2026-08-05.md" in surface
        assert "k77_action_derived_horizontal_euler_image_or_defect_variational_receiver" in surface
    assert "channel-swings/` (178)" in tests_readme
    assert "k77_wave2_actual_y14_receiver_ordering_probe.py" in tests_readme
    assert "k77_wave2_actual_y14_receiver_ordering_scope_audit.py" in gates_readme
    assert "revision 33" in improvement
    assert "form degree precedes observation rank" in improvement

    actual_channel_probes = len(list((ROOT / "tests/channel-swings").glob("*.py")))
    assert actual_channel_probes == 178

    print("k77_wave2_actual_y14_receiver_ordering_scope_audit: PASS")
    print("  direct Omega13 pullback zero; primalize/restrict kernel rank ten")
    print("  horizontal, defect-variational and typed-normal routes held distinct")


if __name__ == "__main__":
    main()
