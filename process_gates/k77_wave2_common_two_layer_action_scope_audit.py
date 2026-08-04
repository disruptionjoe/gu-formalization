#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 common two-layer action packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-common-two-layer-action-euler-coefficient-selection.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-common-two-layer-action-review.md"
SOURCE = ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md"


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
        "PARTIAL__COMMON_TWO_LAYER_ACTION_FORMULA_WITH_EXACT_VARIATIONAL_CONTROL__"
        "NORM_SQUARE_REDUNDANT_ON_FIRST_LAYER__SELF_DERIVED_SQUARE_TARGET_FREE__"
        "CANCELLATION_PATH_ADAPTER_OPEN"
    )
    assert registry["named_gate"] == "K77_COMMON_TWO_LAYER_DIRAC_YANG_MILLS_HIGGS_ACTION_EULER_COEFFICIENT_SELECTION"
    assert registry["result"] == expected
    assert registry["next_required_build"] == "K77_TWO_LAYER_UP_OVER_PATH_ADAPTER_AND_INDEPENDENT_SQUARE_ROOT_TARGET"

    collision = registry["source_collision"]
    assert collision["two_layer_architecture"] == "SOURCE_CONFIRMS"
    assert collision["norm_square_second_layer"] == "SOURCE_CONFIRMS"
    assert collision["redundancy_on_first_order_solutions"] == "SOURCE_CONFIRMS"
    assert collision["up_back_over_cancellation_burden"] == "SOURCE_CONFIRMS_UNFINISHED"
    assert collision["k77_left_right_as_spoken_paths"] == "SOURCE_SILENT"
    assert collision["independent_k77_second_layer_target"] == "SOURCE_SILENT"

    action = registry["common_action"]
    assert action["finite_exact_variational_control"] is True
    assert action["full_moving_k77_expansion"] is False
    assert action["duplicate_current_bridge"] is False

    actual = registry["actual_k77"]
    assert actual["middle_left_right_rank"] == 2
    assert actual["nonzero_projective_middle_cancellation"] is False
    assert actual["anticommutator_scalar_all_covectors"] is True
    assert actual["quadratic_square_tensor_span_rank"] == 3
    assert actual["full_composed_square_root_target_built"] is False

    selection = registry["selection"]
    assert selection["fixed_coupling_field_euler_selection_rank"] == 0
    assert selection["bosonic_residual_norm_selection_rank"] == 0
    assert selection["total_residual_norm_selection_rank_on_first_order_locus"] == 0
    assert selection["self_derived_square_selection_rank"] == 0
    assert selection["optional_modulus_universal_selection_rank"] == 0
    assert selection["optional_modulus_fixture_roots"] == ["173/13", "1/38"]
    assert selection["source_owned_coefficient_constraints"] == 0
    assert selection["projective_free_parameters"] == 1
    assert selection["constraint_surplus"] == -1

    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected
    assert wave2["result_ref"].endswith("k77-wave2-common-two-layer-action-euler-coefficient-selection-2026-08-04.md")
    for token in (
        "COMMON_TWO_LAYER_ACTION_FORMULA_WITH_MOVING_PAIRING_OWNER",
        "EXACT_NORM_SQUARE_EULER_CHAIN_RULE_CONTROL",
        "FIRST_LAYER_REDUNDANCY_FIXED_COUPLING_SELECTION_RANK_ZERO",
        "K77_MIDDLE_LITERAL_CANCELLATION_RANK_TWO",
        "K77_ANTICOMMUTATOR_SCALAR_ON_ALL_COVECTORS",
        "K77_SELF_DERIVED_QUADRATIC_SQUARE_SPAN_RANK_THREE",
        "OPTIONAL_COEFFICIENT_MODULUS_FIELD_DEPENDENT_NOT_UNIVERSAL",
    ):
        assert token in wave2["emitted"]
    assert "TWO_COMPLEX_UP_BACK_OVER_PATH_ADAPTER" in wave2["carried_debt"]
    assert "INDEPENDENT_K77_SECOND_LAYER_SQUARE_ROOT_TARGET" in wave2["carried_debt"]
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_required_build"] == registry["next_required_build"]

    for token in (
        "every first-layer solution",
        "three independent quadratic coefficient tensors",
        "r_a=\\frac{173}{13}",
        "surplus}=0-1=-1",
        "p1/p2/p3 are not used",
        "wave 3 remains closed",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "full moving k77 action",
        "on the first-order solution locus",
        "rank three",
        "alpha=beta",
        "51/51",
        "no coefficient",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "01:59:12--02:00:49",
        "02:03:07",
        "source-confirms-cancellation-burden",
        "source-silent",
        "three honest second-layer readings",
    ):
        assert token in source, f"missing source token: {token}"

    forbidden = (
        "physical higgs is constructed",
        "yukawa coefficient is selected",
        "wave 3 is open",
        "p1 is consumed",
        "three observed families are derived",
    )
    for phrase in forbidden:
        assert phrase not in report
        assert phrase not in review

    print("k77_wave2_common_two_layer_action_scope_audit: PASS")
    print("  common formula exact at declared grade; redundancy selects nothing; K77 square span 3; path/target adapter open")


if __name__ == "__main__":
    main()
