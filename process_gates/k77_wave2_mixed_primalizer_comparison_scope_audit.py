#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 primalizer/comparison packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-mixed-primalizers-two-connection-comparison.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-primalizer-comparison-review.md"
SOURCE = ROOT / "lab/sources/gu-primalizer-two-connection-comparison-source-reinspection-2026-08-04.md"


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
        "PARTIAL__ACTUAL_MOVING_DENSITY_KREIN_PRIMALIZERS_BUILT__"
        "TWO_CONNECTION_RETYPED_TO_FERMION_CYCLIC_RIVAL__"
        "ONE_WAY_HODGE_ROLLING_BUILT__"
        "FULL_CYCLIC_ARROW_PAIR_AND_ACTION_OWNER_OPEN"
    )
    assert registry["named_gate"] == "K77_MIXED_HESSIAN_PRIMALIZERS_AND_TWO_CONNECTION_COMPARISON_FUNCTOR"
    assert registry["result"] == expected
    assert registry["next_required_build"] == "K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER"

    collision = registry["source_collision"]
    assert collision["toe_two_connection_context"] == "SOURCE_CONFIRMS_IMMEDIATE_FERMION_CONTEXT"
    assert collision["toe_full_cyclic_completion"] == "SOURCE_UNRELEASED"
    assert collision["reverse_arrow"] == "SOURCE_SILENT"
    assert collision["cyclic_action_owner"] == "SOURCE_SILENT"

    layer0 = registry["layer0"]
    assert layer0["d916_vs_two_connection_rival"] == "DISTINCT"
    assert layer0["two_connection_rival_vs_bose_fermi_mixed_hessians"] == "DISTINCT"
    assert layer0["one_way_arrow_vs_full_cyclic_complex"] == "DISTINCT"
    assert layer0["density_vs_oriented_top_form"] == "DISTINCT"

    primalizer = registry["primalizer"]
    assert primalizer["scope"] == "ADMISSIBLE_REAL_K77_ASSOCIATED_BUNDLE_DENSITY_SECTOR"
    assert primalizer["four_field_inverse_exact"] is True
    assert primalizer["moving_inverse_variation_exact"] is True
    assert primalizer["nonorthogonal_frame_naturality_exact"] is True
    assert primalizer["actual_spin_transition_naturality_exact"] is True
    assert primalizer["free_coefficients"] == 0
    assert primalizer["orientation_required_for_density_formulation"] is False
    assert primalizer["global_closed_analytic_domain_built"] is False

    rival = registry["two_connection_reconstruction"]
    assert rival["source_context"] == "FERMION_CYCLIC_COMPLETION_OR_RIVAL"
    assert rival["one_way_hodge_rolled_arrow_built"] is True
    assert rival["reverse_arrow_built"] is False
    assert rival["full_cyclic_pair_built"] is False
    assert rival["action_owner_built"] is False

    comparison = registry["d916_comparison"]
    assert comparison["slot_preserving_match"] is False
    assert comparison["general_chain_equivalence_tested"] is False
    assert comparison["replacement_completion_or_rival_decided"] is False

    assert registry["selection"] == {
        "action_hessian_selection_rank": 0,
        "projective_free_parameters": 1,
        "constraint_surplus": -1,
    }
    assert registry["probe_receipt"] == {
        "source": 9, "type": 19, "exact": 22, "planted": 8,
        "total": 58, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    assert wave2["status"] == expected
    assert wave2["result_ref"].endswith("k77-wave2-mixed-primalizers-two-connection-comparison-2026-08-04.md")
    for token in (
        "ACTUAL_K77_FOUR_FIELD_DENSITY_KREIN_PRIMALIZER",
        "MOVING_INVERSE_VARIATION_AND_TRANSITION_NATURALITY",
        "ORIENTATION_FREE_DENSITY_FORMULATION_NO_P1",
        "TWO_CONNECTION_FERMION_CONTEXT_SOURCE_CORRECTION",
        "HODGE_ROLLED_ONE_WAY_TWO_CONNECTION_ARROW",
        "D916_SLOT_PRESERVING_ORDER_MISMATCH",
    ):
        assert token in wave2["emitted"]
    for token in (
        "FULL_TWO_CONNECTION_CYCLIC_EVEN_ODD_ARROW_PAIR",
        "TWO_CONNECTION_ACTION_HELMHOLTZ_OWNER",
        "GENERAL_CHAIN_EQUIVALENCE_OR_PRECISE_RIVAL_DISPOSITION",
    ):
        assert token in wave2["carried_debt"]
    assert frontier["next_required_build"] == registry["next_required_build"]

    for token in (
        "actual moving density/krein primalizers",
        "two-connection source classification",
        "one-way hodge-rolled two-connection arrow",
        "slot-preserving equality with d916",
        "surplus}=0-1=-1",
        "p1/p2/p3 remain unused",
        "wave 3 stays closed",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "summary outruns the artifact",
        "stale or superseded object",
        "source-silent",
        "wrong degree-14 hodge inverse",
        "58/58 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "source-confirms-fermion-rolling-context",
        "source-unreleased-full-completion",
        "source-silent",
        "density-valued action",
        "one arrow only",
    ):
        assert token in source, f"missing source token: {token}"

    test_files = list((ROOT / "tests/channel-swings").glob("*.py"))
    gate_files = list((ROOT / "process_gates").glob("*.py"))
    tests_readme = (ROOT / "tests/README.md").read_text(encoding="utf-8")
    gates_readme = (ROOT / "process_gates/README.md").read_text(encoding="utf-8")
    assert len(test_files) == 174
    assert "`channel-swings/` (174)" in tests_readme
    assert len(gate_files) == 139
    assert "k77_wave2_mixed_primalizer_comparison_scope_audit.py" in gates_readme

    forbidden = (
        "the full cyclic d squared is built",
        "the two-connection target is bosonic",
        "a general chain inequivalence is proved",
        "the coefficient is selected",
        "wave 3 is open",
        "p1 is consumed",
    )
    for phrase in forbidden:
        assert phrase not in report
        assert phrase not in review

    print("k77_wave2_mixed_primalizer_comparison_scope_audit: PASS")
    print("  primalizer built; fermion rival retyped; full cyclic/action owner open")


if __name__ == "__main__":
    main()
