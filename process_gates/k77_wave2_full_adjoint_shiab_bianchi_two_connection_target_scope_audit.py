#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 full-adjoint/Bianchi target packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-full-adjoint-shiab-bianchi-two-connection-target.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-full-adjoint-shiab-bianchi-two-connection-target-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-full-adjoint-bianchi-target-review.md"
SOURCE = ROOT / "lab/sources/gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_full_adjoint_shiab_bianchi_two_connection_target_probe.py"
SAGE = ROOT / "tests/channel-swings/k77_wave2_bianchi_two_connection_target_independent.sage"


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
    sage = normalized(SAGE)

    assert registry["named_gate"] == (
        "K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET"
    )
    assert registry["gate_status"] == (
        "PARTIAL_WITH_FULL_ADJOINT_EXTENSION_AND_INDEPENDENT_PRE_SHIAB_TARGET"
    )
    assert registry["gate_after"] == (
        "K77_PRODUCT_SENSITIVE_MOVING_PHI_EPSILON_BIANCHI_CHAIN_MAP_AND_TYPED_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE_AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "8_DISPLAYED_DISCRETE_PRODUCT_MAPS"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-BIANCHI-TWO-CONNECTION-TARGET", "grade": "T4"}
    ]
    assert len(pre["preregistered_kills"]) == 6

    collision = registry["source_collision"]
    assert collision["displayed_separable_shiab_formula"] == "SOURCE_CONFIRMS"
    assert collision["historical_bianchi_selector"] == "SOURCE_CONFIRMS_MISSING"
    assert collision["quadratic_eddy_completion"] == "SOURCE_CONFIRMS"
    assert collision["two_connection_target_context"].startswith("SOURCE_CORRECTS")
    assert collision["moving_product_sensitive_chain_map"] == "SOURCE_SILENT"
    assert collision["two_connection_to_euler_comparison_functor"] == "SOURCE_SILENT"
    assert all(value == "DISTINCT" for value in registry["layer0"].values())

    span = registry["full_adjoint_channel_span"]
    assert span["displayed_product_maps"] == 8
    assert span["decomposition_coordinates"] == 6
    assert span["structural_formula"] == "S_f_i_o_EQUALS_A_f_PLUS_B_i_o"
    assert span["incidence_rank"] == 5
    assert span["universal_relation_count"] == 3
    assert span["complete_grade_one_lower_bound_rank"] == 5
    assert span["full_operator_span_rank"] == 5
    assert span["full_map_projective_classes"] == 8
    assert span["corroborating_coefficient_grades"] == 15
    assert span["all_grade_representative_relations_pass"] is True
    assert span["scope"].startswith("EIGHT_DISPLAYED")

    bianchi = registry["eddy_bianchi_complex"]
    assert bianchi["ordinary_bianchi"] is True
    assert bianchi["eddy_live"] is True
    assert bianchi["coefficient_solution"] == ["1/2", "1/3"]
    assert bianchi["coefficient_constraint_surplus"] == 0
    assert bianchi["global_moving_k77_chain_map"] == "OPEN"

    target = registry["two_connection_target"]
    assert target["source_context"] == "UNRELEASED_FERMION_COMPLEX_COMPLETION_OR_RIVAL"
    assert target["northeast_block"] == "MINUS_T_WEDGE_F_B_NONZERO"
    assert target["matches_path_average"] is True
    assert target["uses_shiab_product"] is False
    assert target["typed_full_comparison_functor"] == "OPEN"

    selection = registry["selection"]
    assert selection["pre_shiab_constraint_matrix_shape"] == [0, 5]
    assert selection["pre_shiab_selection_rank"] == 0
    assert selection["remaining_full_map_span_dimension"] == 5
    assert selection["historical_product_sensitive_bianchi_selector"] == "OPEN"

    assert registry["independent_sage"] == {
        "incidence_rank": 5,
        "relation_dimension": 3,
        "path_average_reconstruction": "EXACT",
        "mixed_two_connection_defect": "NONZERO",
    }
    assert registry["accounting"] == {
        "fitted_selector_parameters": 0,
        "selection_constraints_from_pre_shiab_bianchi": 0,
        "selection_constraints_from_two_connection_target": 0,
        "new_fields": 0,
        "new_projectors": 0,
        "new_data": 0,
        "free_object_delta": 0,
        "p1_p2_p3_used": False,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 6, "type": 25, "exact": 21, "planted": 9,
        "total": 61, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    latest = wave2["latest_advance"]
    assert latest["named_gate"] == registry["named_gate"]
    assert latest["result_ref"] == (
        "explorations/k77-wave2-full-adjoint-shiab-bianchi-two-connection-target-2026-08-05.md"
    )
    assert latest["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "FULL_EIGHT_DISPLAYED_SHIAB_MAP_SPAN_RANK_FIVE",
        "THREE_UNIVERSAL_FULL_ADJOINT_PRODUCT_RELATIONS",
        "EIGHT_FULL_MAP_PROJECTIVE_CLASSES",
        "EXACT_CONNECTION_PATH_AVERAGE_CURVATURE",
        "EXACT_FIRST_MOMENT_EDDY_BIANCHI_SYZYGY",
        "INDEPENDENT_TWO_CONNECTION_PRE_SHIAB_TARGET_RECONSTRUCTION",
        "NONZERO_MIXED_TWO_CONNECTION_T_WEDGE_F_B_DEFECT_RETAINED",
        "PRE_SHIAB_BIANCHI_TWO_CONNECTION_PRODUCT_SELECTION_RANK_ZERO",
        "TWO_CONNECTION_FERMION_CONTEXT_SCOPE_CORRECTION",
    ):
        assert emitted in wave2["emitted"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "entire adjoint coefficient carrier",
        "full eight-map span has rank **exactly five**",
        "d_b\\bar f+[t,m_1]=0",
        "\\bar f=f_b+\\frac12\\delta f-\\frac16t\\wedge t",
        "product selection rank zero",
        "moving chain-map defect",
        "p1/p2/p3 remain unchanged and unused",
        "wave 3",
    ):
        assert phrase in report

    for phrase in (
        "summary outruns the artifact",
        "rigor defends a superseded object",
        "eight displayed product maps",
        "pre-shiab connection-path target",
        "missing historical bianchi criterion was channel-blind",
        "pass_with_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-corrects",
        "source-silent",
        "quadratic eddy",
        "fermion-roll context",
        "product-sensitive chain-map identity",
    ):
        assert phrase in source

    for phrase in (
        "s_(f,i,o) = a_f + b_(i,o)",
        "full displayed k77 channel-map span is therefore exactly five",
        "quadratic-eddy path average satisfies the exact first-moment bianchi syzygy",
        "reconstructs the path average",
        "pre-shiab bianchi and two-connection targets have shiab selection rank zero",
        "representative grade samples are not used as the full-adjoint proof",
    ):
        assert phrase in probe

    for phrase in (
        "incidence.rank() == 5",
        "incidence.left_kernel().dimension() == 3",
        "from_square == average",
        "-t * f_b != 0",
    ):
        assert phrase in sage

    process_count = sum(path.suffix == ".py" for path in (ROOT / "process_gates").iterdir())
    channel_python = sum(path.suffix == ".py" for path in (ROOT / "tests/channel-swings").iterdir())
    channel_sage = sum(path.suffix == ".sage" for path in (ROOT / "tests/channel-swings").iterdir())
    tests_readme = normalized(ROOT / "tests/README.md")
    assert process_count == 152
    assert channel_python == 184 and channel_sage == 2
    assert "channel-swings/` (184 python + 2 sage)" in tests_readme

    print("PASS: K77 full-adjoint Shiab/Bianchi/two-connection target packet is exact and scope-fenced")


if __name__ == "__main__":
    main()
