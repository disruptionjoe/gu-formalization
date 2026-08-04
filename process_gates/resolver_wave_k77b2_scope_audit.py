#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave K77-B2.

This gate preserves ambient/Riemann, three-Bianchi, three-trace,
displayed/broader, restriction/full-domain, transgression/Green, and
ansatz/lane distinctions.  It does not reproduce the mathematics.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/resolver-wave-k77b2-shiab-family-curvature-selector-transgression.json"
DISPOSITION = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-disposition-2026-08-04.json"
REPORT = ROOT / "explorations/resolver-wave-k77b2-shiab-family-curvature-selector-transgression-2026-08-04.md"
PROBE = ROOT / "tests/channel-swings/resolver_wave_k77b2_shiab_family_curvature_selector_transgression_probe.py"


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
        "RIEMANN_INJECTION_AND_FOUR_COORDINATE_HOM_CONSTRUCTED__"
        "DISPLAYED_AMBIENT_EINSTEIN_SAME_ACTION_INTERSECTION_ZERO__BROADER_EXTENSION_OPEN"
    )
    assert disposition["route_disposition"] == (
        "CONTINUE_K77_THROUGH_BOUNDED_FULL_DOMAIN_EXTENSION_AND_CYCLIC_EULER_EXISTENCE_SEARCH"
    )
    assert disposition["hostile_review_status"] == "PASS_AFTER_REPAIRS"
    assert disposition["third_lane_promoted"] is False

    dimensions = registry["dimension_ladder"]
    assert dimensions["ambient_omega2_ad"] == 1490944
    assert dimensions["sym2_lambda2"] == 4186
    assert dimensions["lambda4_bianchi_rows"] == 1001
    assert dimensions["algebraic_riemann"] == 3185
    assert list(dimensions["algebraic_riemann_irreps"].values()) == [1, 104, 3080]

    hom = registry["riemann_restriction_hom"]
    assert hom["dimension"] == 4
    assert hom["dimension_scope"].startswith("REAL_POINTWISE_FIXED_FRAME")
    assert hom["multiplicities"] == {"scalar": 2, "traceless_ricci": 2, "weyl": 0}
    assert hom["weyl_killing_selects"] is False

    displayed = registry["candidate_tiers"][0]
    assert displayed["complete_within_declared_tier"] is True
    assert displayed["verdict"].startswith("ZERO_NONVACUOUS_INTERSECTION")
    assert disposition["displayed_family"]["joint_nonzero_survivors"] == 0
    assert disposition["kill_policy"]["highest_earned_scope"].startswith("DISPLAYED_ANSATZ_KILL")

    broader = registry["candidate_tiers"][1]
    assert broader["complete_within_declared_tier"] is False
    assert broader["exhausts_all_shiabs"] is False
    assert broader["status"].startswith("PROVISIONAL_SIGNATURE_DECLARED")
    assert disposition["bounded_grammar"]["typed"] is False
    assert disposition["bounded_grammar"]["canonical_dag_enumeration"] == "OPEN"

    survivor = registry["constructive_survivor"]
    assert survivor["riemann_restriction_dimension"] == 2
    assert survivor["grade"] == "EXACT_POINTWISE_FIXED_FRAME_EQUIVARIANT_RESTRICTION"
    assert survivor["associated_bundle_descent"] == "OPEN"
    assert survivor["full_domain_extension"] == "OPEN"
    assert survivor["same_action_transgression"] == "OPEN"

    scope = disposition["scope"]
    assert scope["ambient_einstein_trace"] is True
    assert scope["observed_four_dimensional_trace"] is False
    assert scope["frobenius_fibre_trace_reversal"] is False
    assert scope["algebraic_bianchi"] is True
    assert scope["differential_bianchi"] is False
    assert scope["constant_cubic_transgression_counterexamples"] is True
    assert scope["derivative_green"] is False
    assert scope["physics_recovery"] is False

    assert disposition["kill_policy"]["lane_killed"] is False
    assert disposition["kill_policy"]["conditional_program_killed"] is False
    assert disposition["kill_policy"]["atomic_targets_preserved"] is True
    assert registry["verdict"]["k77_lane_killed"] is False
    assert registry["verdict"]["atomic_targets_preserved"] is True

    assert disposition["external_datum"] == {
        "P1": "unchanged_unused", "P2": "unchanged_unused", "P3": "unchanged_unused"
    }
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert disposition["next_gate"] == registry["next_gate"]["id"]

    for token in (
        "Weyl-killing cannot select",
        "ambient fourteen-dimensional Einstein",
        "displayed low/high factorized family is killed",
        "two-coordinate restriction",
        "executable AST typing",
        "P1/P2/P3 remain unchanged and unused",
    ):
        assert token.lower() in report.lower(), f"report missing scope token {token!r}"

    for token in (
        "1001 sparse first-Bianchi rows",
        "target multiplicities 2,2,0",
        "VIABLE_A",
        "VIABLE_B",
        "ZERO_MAP_ONLY",
        "DISPLAYED_ANSATZ_KILL_UNDER_AMBIENT_EINSTEIN_PLUS_SAME_ACTION",
        "original-parameter ideal reduces exactly to <a,b>",
        "all 91 raised bivector images have an exact coefficient inverse",
    ):
        assert token in probe, f"probe missing fence {token!r}"

    print("resolver_wave_k77b2_scope_audit: PASS")
    print("  curvature/Bianchi/trace/displayed/broader/transgression/Green and ansatz/lane fences retained")


if __name__ == "__main__":
    main()
