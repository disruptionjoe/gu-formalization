#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 principal-Bianchi selector packet."""

from __future__ import annotations

import json
from pathlib import Path

from k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit import historical_wave2_checkpoint


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-principal-bianchi-product-selector.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-principal-bianchi-product-selector-review.md"
SOURCE = ROOT / "lab/sources/gu-shiab-derivation-principal-bianchi-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"
SAGE = ROOT / "tests/channel-swings/k77_wave2_principal_bianchi_product_selector_independent.sage"


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

    assert registry["artifact"] == "K77_WAVE2_PRINCIPAL_BIANCHI_PRODUCT_SELECTOR"
    assert registry["lane"] == "1"
    assert registry["fork"] == "SIGNATURE_AMBIENT_7_7"
    assert registry["gate_before"] == (
        "K77_PRODUCT_SENSITIVE_MOVING_PHI_EPSILON_BIANCHI_CHAIN_MAP_AND_TYPED_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR"
    )
    assert registry["gate_after"] == (
        "K77_EDDY_COMPLETED_AUGMENTED_TORSION_CHAIN_MAP_AND_FULL_EULER_COMPARISON_FUNCTOR"
    )
    assert registry["verdict"] == (
        "DISPLAYED_EIGHT_ROW_PRODUCT_SELECTOR_CONDITIONALLY_RESOLVED__CURVATURE_COMPARISON_BUILT__FULL_FUNCTOR_OPEN"
    )

    disposition = registry["source_disposition"]
    assert disposition == {
        "derivation_and_bianchi_intent": "SOURCE_CONFIRMS",
        "historical_selector": "SOURCE_CONFIRMS_MISSING",
        "principal_symbol_criterion": "RECONSTRUCTION",
        "selected_product_attribution": "NOT_ATTRIBUTED_TO_WEINSTEIN",
    }
    assert registry["layer0"]["status"] == "PASS_WITH_EXPLICIT_FENCES"
    assert all(
        value == "DISTINCT"
        for key, value in registry["layer0"].items()
        if key != "status"
    )

    search = registry["search_space"]
    assert search["displayed_product_rows"] == 8
    assert search["full_displayed_map_span"] == 5
    assert search["fitted_continuous_parameters"] == 0
    assert search["fixed_relative_coefficient"] == "-1/2"
    assert search["phi_bank"] == "SOURCE_LOW_PHI1_PHI2"

    carrier = registry["principal_carrier"]
    assert carrier["covector_orbits"] == ["positive", "negative", "null"]
    assert carrier["jet_rank_per_orbit"] == 91
    assert carrier["input_symbol"] == "k wedge F=0"

    selector = registry["selector"]
    assert selector["bianchi_passing_rows"] == 4
    assert selector["bianchi_defect_rank"] == 1
    assert selector["continuous_kernel_dimension"] == 4
    assert selector["unique_bianchi_nonzero_row"] == ["comm", "symi", "symi"]
    assert selector["riemann_response"] == "-2_TIMES_AMBIENT14_EINSTEIN"
    assert selector["weyl_response"] == 0
    assert selector["moving_epsilon_adds_selection"] is False
    assert selector["scope"] == "ONLY_THE_EIGHT_FIXED_DISPLAYED_PRODUCT_ASSIGNMENTS"

    comparison = registry["two_connection_comparison"]
    assert comparison["input_relation"] == "DeltaF=D_B_T+T2"
    assert comparison["projection"] == "F_B+(1/2)DeltaF-(1/6)T2"
    assert comparison["path_average"] == "F_B+(1/2)D_B_T+(1/3)T2"
    assert comparison["curvature_square_commutes"] is True
    assert comparison["postselected_shiab_square_commutes"] is True
    assert comparison["full_euler_functor"] == "OPEN"

    assert registry["checks"] == {
        "main": "5 source + 22 type + 25 exact + 6 planted = 58 PASS",
        "independent_sage": "PASS",
        "predecessors": [
            "K77_WAVE2_MOVING_SHIAB_EPSILON_WARD_GREEN_DOMAIN",
            "K77_WAVE2_FULL_ADJOINT_SHIAB_BIANCHI_TWO_CONNECTION_TARGET",
        ],
    }
    assert "full_source_natural_shiab_uniqueness" in registry["held_open"]
    assert "observed_physics" in registry["held_open"]
    assert "P1_P2_P3" in registry["held_open"]
    assert "Wave3" in registry["held_open"]
    assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert registry["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3"
    assert registry["third_lane_status"] == "NOT_PROMOTED"

    required_emissions = (
        "PRINCIPAL_BIANCHI_RANK91_POSITIVE_NEGATIVE_NULL_ORBIT_CARRIERS",
        "PRINCIPAL_BIANCHI_DEFECT_RANK_ONE_ON_DISPLAYED_SPAN",
        "UNIQUE_NONZERO_BIANCHI_DISPLAYED_ROW_COMM_SYMI_SYMI",
        "SELECTED_RIEMANN_RESPONSE_MINUS_TWO_AMBIENT14_EINSTEIN",
        "SELECTED_WEYL_RESPONSE_ZERO",
        "MOVING_EPSILON_TRANSPORTS_WITHOUT_ADDED_SELECTION",
        "TWO_CONNECTION_CURVATURE_COMPARISON_SQUARE",
    )
    historical_wave2_checkpoint(campaign, required_emissions)

    for phrase in (
        "complete principal-bianchi carrier",
        "rank 91",
        "comm / symi / symi",
        "four-dimensional continuous kernel",
        "not independent rows",
        "full_source_natural_shiab_uniqueness:",
        "full_two_connection_to_euler_comparison_functor:",
        "p1/p2/p3 remain unchanged and unused",
        "wave 3",
    ):
        assert phrase in report

    for phrase in (
        "summary outruns artifact",
        "fence defends a superseded object",
        "complete algebraic-riemann principal-symbol grade",
        "counting them as independent would inflate surplus",
        "pass_with_scope_and_independence_repairs",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-confirms-missing",
        "reconstruction",
        "if shiab is a derivation",
        "not a recovered quotation or an attribution to weinstein's missing sheet",
    ):
        assert phrase in source

    for phrase in (
        "complete rank-91 jet carrier in each case",
        "full principal-bianchi defect has rank one on the eight product columns",
        "comm-symi-symi is the unique bianchi-compatible nonzero displayed row",
        "selected row is minus two times the ambient einstein contraction",
        "full source-natural shiab uniqueness remains open",
    ):
        assert phrase in probe

    for phrase in (
        "assert jet_ranks == {\"positive\": 91, \"negative\": 91, \"null\": 91}",
        "assert sparse_rank(defect_columns) == 1",
        "assert unique_nonzero == (selected,)",
        "selected = (\"comm\", \"symi\", \"symi\")",
        "sage_independent_selector_pass",
    ):
        assert phrase in sage

    tests_readme = normalized(ROOT / "tests/README.md")
    assert "k77_wave2_principal_bianchi_product_selector_probe.py" in tests_readme

    print("PASS: K77 principal-Bianchi product selector packet is exact and scope-fenced")


if __name__ == "__main__":
    main()
