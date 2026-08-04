#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave K77-B.

This gate preserves source-bracket, raw/corrected-product, codomain/Euler,
vacuity/liveness, sampled/displayed-ansatz/broader-rival, and map/lane
distinctions. It does not
reproduce the Clifford, Sage, Hodge, or variational calculations.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation.json"
DISPOSITION = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-disposition-2026-08-04.json"
REPORT = ROOT / "explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md"
PROBE = ROOT / "tests/channel-swings/resolver_wave_k77b_source_bracket_displayed_shiab_b1_variation_probe.py"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=unique_object)


def main() -> None:
    registry = load(REGISTRY)
    disposition = load(DISPOSITION)
    report = REPORT.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    assert registry["named_gate"] == disposition["named_gate"]
    assert disposition["gate_after"] == (
        "SOURCE_BRACKET_NORMALIZED__CANONICAL_LOW_GRADE_RAW_SHIAB_CODOMAIN_KILL__"
        "LOW_GRADE_REPAIRS_NOT_VARIATIONALLY_CERTIFIED"
    )
    assert disposition["route_disposition"] == "CONTINUE_K77_THROUGH_DISPLAYED_ANSATZ_AND_BROADER_SHIAB_RIVAL_CENSUS"
    assert disposition["hostile_review_status"] == "PASS_AFTER_MATERIAL_NORMALIZATION_AND_SCOPE_REPAIR"
    assert registry["hostile_review_status"] == disposition["hostile_review_status"]
    assert disposition["third_lane_promoted"] is False

    assert registry["bracket_normalization"]["source_object"] == "T_WEDGE_MATRIX_T"
    assert registry["bracket_normalization"]["graded_relation"] == "[T,T]_graded=2*T_wedge_matrix_T"
    assert disposition["bracket_normalization"]["independent_cyclic_transgression_check"] == "PASS"

    assert registry["shiab_family"]["displayed_raw_product_status"] == "CANONICAL_LOW_GRADE_RAW_REALIZATION_KILLED_AT_AD_CODOMAIN_ON_EXACT_K77_FIXTURES"
    assert disposition["literal_shiab"]["fixture_A_B_skew_B_self"] == [10, 4]
    assert disposition["literal_shiab"]["fixture_B_B_skew_B_self"] == [2, 12]
    assert disposition["literal_shiab"]["status"] == "CANDIDATE_MAP_KILL"

    repaired = disposition["low_grade_repairs"]
    assert repaired["product_channels"] == repaired["ad_closed"] == 8
    assert repaired["nonvacuous_on_endpoint_bank"] == 6
    assert repaired["nonvacuous_passing"] == 0
    assert repaired["zero_defect_vacuous"] == 2
    assert repaired["source_grade"].startswith("SOURCE_INSPIRED_NODEWISE_BANK")
    assert registry["b1_variation"]["passing_live_low_grade_channels"] == []

    family = disposition["invariant_family"]
    assert family["phi1_multiplicity"] == family["phi2_multiplicity"] == 2
    assert family["low_high_grades"] == [[1, 13], [2, 12]]
    assert family["scope"].startswith("FULL_PHI_CARRIER_INSIDE_DISPLAYED_ANSATZ")
    assert family["broader_source_natural_rival_table"] == "OPEN"
    assert family["selector_status"] == "OPEN"
    assert registry["shiab_family"]["selector_status"] == "OPEN"

    scope = disposition["scope"]
    assert scope["fixed_epsilon_metric_translation_variation"] is True
    assert scope["constant_algebraic_cubic_mass_sector"] is True
    assert scope["derivative_green"] is False
    assert scope["full_euler_noether_bv_domain"] is False
    assert scope["observation_descent"] is False
    assert scope["physics_recovery"] is False

    kill = disposition["kill_policy"]
    assert kill["highest_earned_scope"] == registry["verdict"]["kill_scope"] == "CANDIDATE_MAP_KILL"
    assert kill["mechanism_killed"] is False
    assert kill["lane_killed"] is False
    assert kill["conditional_program_killed"] is False
    assert kill["atomic_targets_preserved"] is True
    assert registry["verdict"]["k77_lane_killed"] is False
    assert registry["verdict"]["atomic_targets_preserved"] is True

    assert disposition["external_datum"] == {
        "P1": "unchanged_unused",
        "P2": "unchanged_unused",
        "P3": "unchanged_unused",
    }
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert registry["next_gate"]["status"] == "OPEN"
    assert disposition["next_gate"] == registry["next_gate"]["id"]

    for token in (
        "SOURCE_BRACKET_NORMALIZED",
        "literal associative-product reading",
        "six channels are nonvacuous",
        "TWO_ZERO_DEFECT_REPAIRS_ARE_VACUOUS",
        "full low/high Phi carrier",
        "P1/P2/P3 remain unchanged and unused",
    ):
        assert token.lower() in report.lower(), f"report missing scope token {token!r}"

    for token in (
        "sample_passing_live_channels",
        "not passing_live_channels",
        "NATIVE_GRADES\" not in globals()",
        "T_WEDGE_MATRIX_T",
        "[T,T]_graded=2*T_wedge_matrix_T",
    ):
        assert token in probe, f"probe missing fence {token!r}"

    print("resolver_wave_k77b_scope_audit: PASS")
    print("  bracket/product/codomain/Euler/vacuity/displayed-ansatz/broader-rival and map/lane fences retained")


if __name__ == "__main__":
    main()
