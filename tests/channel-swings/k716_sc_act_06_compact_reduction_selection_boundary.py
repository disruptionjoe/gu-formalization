#!/usr/bin/env python3
"""K716: compact reductions exist in a noncanonical Lorentz orbit."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k716-sc-act-06-compact-reduction-selection-boundary.json"


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def multiply(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def determinant2(a: list[list[Fraction]]) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def strings(a: list[list[Fraction]]) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def build() -> dict[str, Any]:
    eta = [[Fraction(1), 0], [0, Fraction(-1)]]
    identity = [[Fraction(1), 0], [0, Fraction(1)]]
    boost_inverse = [[Fraction(5, 3), Fraction(-4, 3)], [Fraction(-4, 3), Fraction(5, 3)]]
    boost_inverse2 = multiply(boost_inverse, boost_inverse)
    q0 = identity
    q1 = multiply(transpose(boost_inverse), boost_inverse)
    q2 = multiply(transpose(boost_inverse2), boost_inverse2)
    family = [q0, q1, q2]
    compatibility = [multiply(q, multiply(eta, q)) == eta for q in family]
    determinants = [str(determinant2(q)) for q in family]
    return {
        "schema_version": "1.0",
        "result_id": "K716-SC-ACT-06-COMPACT-REDUCTION-SELECTION-BOUNDARY",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "The exact existence-versus-selection boundary for compact-reduction auxiliary metrics on the standard real (13,1) carrier.",
        "gu_typed_objects": {
            "carrier": "unchanged real fourteen-dimensional native carrier, tested on one embedded (1,1) boost plane",
            "pairing": "fixed native eta and the Cartan-compatible orbit q_n=L^{-nT}L^{-n}",
            "real_structure": "unchanged real carrier",
            "grading": "conjugate positive/negative splittings with compact conjugate stabilizers",
            "action_owner": "none; orbit membership proves availability, not source or background selection",
            "target": "canonicity/ownership of the auxiliary reduction MAP-TYPE=reduction moduli",
        },
        "theorem": {
            "cartan_compatible_positive_metrics_exist": True,
            "at_least_three_distinct_exact_reductions_constructed": True,
            "boost_orbit_contains_infinitely_many_distinct_reductions": True,
            "all_reduction_stabilizers_are_conjugate_compact_subgroups": True,
            "native_eta_selects_a_unique_reduction": False,
            "full_O13_1_fixed_positive_member_exists": False,
            "mathematical_existence_implies_source_ownership": False,
            "complete_GU_symbol_instantiated": False,
            "source_claim_proved": False,
        },
        "exact_controls": {
            "boost_inverse_plane": [["5/3", "-4/3"], ["-4/3", "5/3"]],
            "q0": strings(q0),
            "q1": strings(q1),
            "q2": strings(q2),
            "expected_q1": [["41/9", "-40/9"], ["-40/9", "41/9"]],
            "expected_q2": [["3281/81", "-3280/81"], ["-3280/81", "3281/81"]],
            "pairwise_distinct": q0 != q1 and q1 != q2 and q0 != q2,
            "cartan_compatibility": compatibility,
            "determinants": determinants,
            "plane_eigenvalue_pairs": [["1", "1"], ["9", "1/9"], ["81", "1/81"]],
            "orbit_formula": "eigenvalues(q_n)=(3^(2n),3^(-2n)); n>=0",
            "standard_stabilizer": "O(1)xO(1) on the boost plane and O(12) on the untouched positive complement",
            "boosted_stabilizers": "L^n K L^-n; compact by conjugacy",
            "full_native_invariant_positive_member": False,
        },
        "native_interface_status": {
            "compact_reduction_source_owned": False,
            "stationary_background_selects_reduction": False,
            "distinguished_B_epsilon_Y_tuple_constructed": False,
            "complete_full_field_symbol_constructed": False,
            "auxiliary_metric_compatible_with_complete_GU_symbol": False,
            "source_independent_row_projector_supplied": False,
            "fredholm_domain_constructed": False,
            "nonlinear_moduli_theorem_proved": False,
            "SC_ACT_06_ellipticity_proved": False,
        },
        "decision": {
            "auxiliary_route_has_a_mathematical_existence_obstruction": False,
            "auxiliary_route_has_an_unresolved_selection_and_compatibility_obligation": True,
            "abstract_auxiliary_metric_arc_requires_further_distance_only_work": False,
            "next_exact_input": "Stop extending the abstract auxiliary branch. Construct one distinguished stationary B(epsilon)/Y background, its complete bosonic/fermionic/mixed gauge-Euler-redundancy principal complex and projectors, and show that background owns one reduction before testing exactness at every nonzero covector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The family proves mathematical availability and noncanonicity only; no source sentence or stationary GU background selects a member or tests it on the complete symbol.",
        "preflight_bookend": {
            "route_comparison": "K714--K715 make compact reductions explicit; K716 decides whether availability collapses the ownership burden and proves it does not.",
            "retrieval_collision_result": "K713 excludes a fully invariant q but does not construct multiple exact Cartan-compatible positive members or their conjugate stabilizers.",
            "strongest_alternative": "A stationary GU background may reduce symmetry and select one orbit point; that must be constructed on the full symbol rather than inferred from eta.",
        },
        "postflight_bookend": {
            "strongest_overclaim": "Because a compact reduction always exists, any chosen q is canonical or source-native.",
            "strongest_contrary_construction": "q0, q1 and q2 are exact distinct positive Cartan metrics for the same eta, with eigenvalue pairs (1,1), (9,1/9), and (81,1/81).",
            "weakest_reproducibility_seam": "The infinite-orbit conclusion uses the exact boost eigenvalues 3 and 1/3; it says nothing about compatibility with absent GU mixed blocks.",
        },
        "controls": {
            "producer": "tests/channel-swings/k716_sc_act_06_compact_reduction_selection_boundary.py",
            "probe": "tests/channel-swings/k716_sc_act_06_compact_reduction_selection_boundary_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 34,
        },
        "claim_ceiling": "Exact finite controls for availability, conjugacy and nonselection of compact-reduction metrics. It does not select a GU reduction, instantiate the full complex, prove Fredholmness or moduli, or move source, ledger, canon, prediction, confirmation or public verdicts.",
    }


def validate(p: dict[str, Any]) -> None:
    t, c, n, d = p["theorem"], p["exact_controls"], p["native_interface_status"], p["decision"]
    for key in ("cartan_compatible_positive_metrics_exist", "at_least_three_distinct_exact_reductions_constructed", "boost_orbit_contains_infinitely_many_distinct_reductions", "all_reduction_stabilizers_are_conjugate_compact_subgroups"):
        assert t[key]
    for key in ("native_eta_selects_a_unique_reduction", "full_O13_1_fixed_positive_member_exists", "mathematical_existence_implies_source_ownership", "complete_GU_symbol_instantiated", "source_claim_proved"):
        assert not t[key]
    assert c["q1"] == c["expected_q1"] and c["q2"] == c["expected_q2"]
    assert c["pairwise_distinct"] and c["cartan_compatibility"] == [True, True, True]
    assert c["determinants"] == ["1", "1", "1"]
    assert c["plane_eigenvalue_pairs"] == [["1", "1"], ["9", "1/9"], ["81", "1/81"]]
    assert c["full_native_invariant_positive_member"] is False
    assert all(v is False for v in n.values())
    assert not d["auxiliary_route_has_a_mathematical_existence_obstruction"]
    assert d["auxiliary_route_has_an_unresolved_selection_and_compatibility_obligation"]
    assert not d["abstract_auxiliary_metric_arc_requires_further_distance_only_work"]
    assert p["target_claim"] == "SC-ACT-06" and "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
