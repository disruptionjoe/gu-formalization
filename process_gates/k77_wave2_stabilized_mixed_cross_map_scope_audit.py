#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 stabilized mixed-cross-map packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-stabilized-mixed-cross-map-review.md"
SOURCE = ROOT / "lab/sources/gu-mixed-bose-fermi-cross-map-source-reinspection-2026-08-04.md"


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

    expected = (
        "PARTIAL__ACTION_DERIVED_RAW_MIXED_HESSIAN_BLOCKS_BUILT__"
        "EQ1010_RETYPED_AS_RECTANGULAR_DEFORMATION_COMPLEX__"
        "DIRECT_TWO_CONNECTION_TARGET_MATCH_ILL_TYPED__"
        "PRIMALIZERS_AND_COMPARISON_FUNCTOR_OPEN"
    )
    assert registry["named_gate"] == "K77_STABILIZED_MIXED_BOSE_FERMI_CROSS_MAPS_AND_TARGET_MATCH"
    assert registry["result"] == expected
    assert registry["next_required_build"] == "K77_MIXED_HESSIAN_PRIMALIZERS_AND_TWO_CONNECTION_COMPARISON_FUNCTOR"

    collision = registry["source_collision"]
    assert collision["draft_1010_topology"] == "SOURCE_CONFIRMS_RECTANGULAR_DEFORMATION_TO_EULER_COMPLEX"
    assert collision["draft_1010_mixed_cells"] == "SOURCE_DISPLAYS_CAVEATED"
    assert collision["global_primalizers"] == "SOURCE_SILENT"
    assert collision["comparison_functor"] == "SOURCE_SILENT"

    layer0 = registry["layer0"]
    assert layer0["equation_1010_vs_bose_fermi_endomorphism_square"] == "DISTINCT"
    assert layer0["field_space_vs_density_dual"] == "DISTINCT"
    assert layer0["raw_hessian_block_vs_primalized_cross_map"] == "DISTINCT"
    assert layer0["two_connection_grading_vs_bose_fermi_grading"] == "DISTINCT"
    assert layer0["sensitivity_rank_vs_selection_rank"] == "DISTINCT"

    action = registry["common_action"]
    assert action["raw_u_type"] == "B_TO_F_DENSITY_DUAL"
    assert action["raw_v_type"] == "F_TO_B_DENSITY_DUAL"
    assert action["finite_hessian_symmetric"] is True
    assert action["both_raw_blocks_nonzero"] is True
    assert action["independent_bridge_equation_added"] is False

    witness = registry["actual_k77_witness"]
    assert witness["mixed_hessian_reciprocity_exact"] is True
    assert witness["mixed_map_coefficient_rank"] == 2
    assert witness["coefficient_columns"] == 2
    assert witness["global_sixteen_cell_hessian_built"] is False

    primalizer = registry["primalizer_gate"]
    assert primalizer["fermion_primalizer_built_globally"] is False
    assert primalizer["boson_primalizer_built_globally"] is False
    assert primalizer["bosonic_composite_depends_on_primalizer"] is True
    assert primalizer["fermionic_composite_depends_on_primalizer"] is True

    target = registry["target_match"]
    assert target["two_connection_comparison_functor_built"] is False
    assert target["direct_entrywise_match"] == "ILL_TYPED_WITHOUT_COMPARISON_FUNCTOR"
    assert target["numerical_mismatch_claimed"] is False

    selection = registry["selection"]
    assert selection["action_hessian_selection_rank"] == 0
    assert selection["projective_free_parameters"] == 1
    assert selection["constraint_surplus"] == -1
    assert registry["probe_receipt"] == {
        "source": 11, "type": 15, "exact": 13, "planted": 7,
        "total": 46, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected
    assert wave2["result_ref"].endswith("k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match-2026-08-04.md")
    for token in (
        "EQ1010_THREE_TERM_MIXED_DEFORMATION_TO_EULER_TOPOLOGY",
        "COMMON_ACTION_RAW_MIXED_HESSIAN_RECIPROCITY",
        "ACTUAL_K77_FROZEN_ONE_FORM_MIXED_MAP_RANK_TWO",
        "DIRECT_TWO_CONNECTION_ENTRYWISE_TARGET_MATCH_LAYER0_KILL",
    ):
        assert token in wave2["emitted"]
    for token in (
        "GLOBAL_MOVING_HODGE_KREIN_DENSITY_PRIMALIZERS",
        "TWO_CONNECTION_TO_COMMON_EULER_COMPARISON_FUNCTOR",
        "FULL16_MIXED_HESSIAN_ASSEMBLY_AND_HELMHOLTZ_CHECK",
    ):
        assert token in wave2["carried_debt"]
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_required_build"] == registry["next_required_build"]

    for token in (
        "raw mixed hessian blocks",
        "ill-typed without a comparison functor",
        "frozen one-form-sector witness",
        "selection rank}=0",
        "surplus}=0-1=-1",
        "p1/p2/p3 remain unused",
        "wave 3: **closed**",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "summary outruns the artifact",
        "stale or superseded object",
        "b->f!",
        "two exact primalizer choices",
        "46/46 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "delta_2^omega circle delta_1^omega = upsilon_omega",
        "source-confirms-rectangular-topology",
        "source-blocks-stabilized-global-promotion",
        "caveat emptor",
        "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
        "raw cross blocks without a separate bridge equation",
    ):
        assert token in source, f"missing source token: {token}"

    test_files = list((ROOT / "tests/channel-swings").glob("*.py"))
    gate_files = list((ROOT / "process_gates").glob("*.py"))
    tests_readme = (ROOT / "tests/README.md").read_text(encoding="utf-8")
    gates_readme = (ROOT / "process_gates/README.md").read_text(encoding="utf-8")
    assert len(test_files) == 173
    assert "`channel-swings/` (173)" in tests_readme
    assert len(gate_files) == 138
    assert "k77_wave2_stabilized_mixed_cross_map_scope_audit.py" in gates_readme

    forbidden = (
        "global primalized cross maps are built",
        "the direct target numerically fails",
        "physical yukawa coupling is recovered",
        "wave 3 is open",
        "p1 is consumed",
    )
    for phrase in forbidden:
        assert phrase not in report
        assert phrase not in review

    print("k77_wave2_stabilized_mixed_cross_map_scope_audit: PASS")
    print("  raw mixed Hessians built; primalizers/comparison functor open; surplus -1")


if __name__ == "__main__":
    main()
