#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 up/back/over target packet."""

from __future__ import annotations

import json
from pathlib import Path

from k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit import historical_wave2_checkpoint


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-up-back-over-path-adapter-independent-square-root-target.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-up-back-over-path-adapter-independent-square-root-target-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-up-back-over-target-review.md"
SOURCE = ROOT / "lab/sources/gu-up-back-over-square-root-source-reinspection-2026-08-04.md"


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
        "PARTIAL__SOURCE_BOUND_TWO_CONNECTION_SQUARE_EXACT__"
        "UNIVERSAL_UP_BACK_OVER_TOTALIZATION_BUILT__"
        "DIRECT_K77_TRACE_Q_PATH_ADAPTER_KILLED__"
        "STABILIZED_MIXED_CROSS_MAPS_OPEN"
    )
    assert registry["named_gate"] == "K77_TWO_LAYER_UP_OVER_PATH_ADAPTER_AND_INDEPENDENT_SQUARE_ROOT_TARGET"
    assert registry["result"] == expected
    assert registry["next_required_build"] == "K77_STABILIZED_MIXED_BOSE_FERMI_CROSS_MAPS_AND_TARGET_MATCH"

    collision = registry["source_collision"]
    assert collision["portal_two_complex_architecture"] == "SOURCE_CONFIRMS"
    assert collision["portal_up_back_over_roles"] == "SOURCE_CONFIRMS_UNFINISHED"
    assert collision["toe_two_connection_tokens_and_signs"] == "SOURCE_BOUNDS_RECONSTRUCTION"
    assert collision["toe_cyclic_formula"] == "SOURCE_UNRELEASED"
    assert collision["draft_1010_mixed_cross_map_cells"] == "SOURCE_DISPLAYS_CAVEATED"
    assert collision["stabilized_cross_maps"] == "SOURCE_SILENT"

    target = registry["two_connection_target"]
    assert target["operator"] == "[[d_A,-F_B],[1,-d_B]]"
    assert target["square"] == "[[F_A-F_B,0],[d_A-d_B,0]]"
    assert target["exact_algebra"] is True
    assert target["finite_noncommuting_sign_solution_count"] == 1
    assert target["finite_noncommuting_sign_solutions"] == [[-1, -1]]
    assert target["grade"] == "SOURCE_BOUND_RECONSTRUCTION_WITH_EXACT_ALGEBRA"

    totalization = registry["totalization"]
    assert totalization["universal_noncommutative_identity"] is True
    assert totalization["stabilized_mixed_cross_maps_built"] is False
    assert totalization["square_diagonal"] == ["D^2+VU", "UV+F^2"]
    assert totalization["square_offdiagonal"] == ["DV+VF", "UD+FU"]

    direct = registry["direct_k77_adapter"]
    assert direct["path_plus_coefficient_rank"] == 2
    assert direct["path_minus_coefficient_rank"] == 2
    assert direct["coefficient_columns"] == 2
    assert direct["surviving_projective_points"] == 0
    assert direct["disposition"] == "CANDIDATE_MAP_KILL_ONLY"

    selection = registry["selection"]
    assert selection["source_owned_coefficient_constraints"] == 0
    assert selection["projective_free_parameters"] == 1
    assert selection["constraint_surplus"] == -1
    assert registry["probe_receipt"] == {
        "source": 11, "type": 17, "exact": 15, "planted": 8,
        "total": 51, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"

    required_emissions = (
        "SOURCE_BOUND_TWO_CONNECTION_SQUARE_WITH_UNIQUE_TWO_MINUS_SIGN_CONTROL",
        "CURVATURE_DIFFERENCE_PLUS_AUGMENTED_TORSION_TARGET",
        "UNIVERSAL_BOSE_FERMI_UP_BACK_OVER_TOTALIZATION",
        "DIRECT_K77_TRACE_Q_PLUS_PATH_RANK_TWO_KILL",
        "DIRECT_K77_TRACE_Q_MINUS_PATH_RANK_TWO_KILL",
    )
    assert historical_wave2_checkpoint(campaign, required_emissions)

    for token in (
        "source-bound reconstruction with exact algebra",
        "rank(a l + l a, a r + r a) = 2",
        "candidate-map kill",
        "surplus}=0-1=-1",
        "p1/p2/p3 are not used",
        "wave 3: **closed**",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "summary outruns the artifact",
        "stale or superseded object",
        "rank two",
        "u,v",
        "51/51 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "01:49:44--01:51:17",
        "02:03:07",
        "two negative signs in the second column",
        "source-blocks-source-exact-grade",
        "caveat emptor",
        "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
    ):
        assert token in source, f"missing source token: {token}"

    test_files = list((ROOT / "tests/channel-swings").glob("*.py"))
    gate_files = list((ROOT / "process_gates").glob("*.py"))
    tests_readme = (ROOT / "tests/README.md").read_text(encoding="utf-8")
    gates_readme = (ROOT / "process_gates/README.md").read_text(encoding="utf-8")
    assert "k77_wave2_up_back_over_target_scope_audit.py" in gates_readme

    forbidden = (
        "we constructed the source-exact cyclic gu operator",
        "physical dirac equation is recovered",
        "wave 3 is open",
        "p1 is consumed",
        "three observed families are derived",
    )
    for phrase in forbidden:
        assert phrase not in report
        assert phrase not in review

    print("k77_wave2_up_back_over_target_scope_audit: PASS")
    print("  source-bounded square exact; totalization exact; direct trace-q path rank 2/2; U,V open")


if __name__ == "__main__":
    main()
