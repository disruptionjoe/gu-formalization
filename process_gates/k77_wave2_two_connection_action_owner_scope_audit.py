#!/usr/bin/env python3
"""Fail-closed scope audit for the shifted two-connection/action packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-two-connection-shifted-superconnection-action-owner.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-two-connection-shifted-superconnection-action-owner-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-two-connection-action-owner-review.md"
SOURCE = ROOT / "lab/sources/gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md"


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
        "PARTIAL__SHIFTED_TOTAL_ODD_OPERATOR_SUPPLIES_BOTH_PARITY_ARROWS__"
        "FULL_OFFSHELL_SQUARE_HAS_MIXED_DEFECT__"
        "PREEXISTING_I1B_ACTION_LOCATED_AS_TRANSGRESSION__"
        "NAIVE_IG_PAIR_ACTION_SHELL_MATCH_FAILS__BOSONIC_EULER_PRIMALIZER_OPEN"
    )
    assert registry["named_gate"] == "K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER"
    assert registry["result"] == expected
    assert registry["next_required_build"] == "K77_BOSONIC_EULER_PRIMALIZER_AND_ACTION_SHELL_TWO_CONNECTION_LIFT"

    collision = registry["source_collision"]
    assert collision["toe_full_construction"] == "SOURCE_UNRELEASED"
    assert collision["toe_pair_identification"] == "SOURCE_SILENT"
    assert collision["ig_pair_difference"] == "SOURCE_CONFIRMS_AUGMENTED_TORSION"
    assert collision["i1b_bosonic_action"] == "SOURCE_CONFIRMS_PREEXISTING"
    assert collision["i1b_owns_2025_cyclic_operator"] == "SOURCE_SILENT"

    layer0 = registry["layer0"]
    assert layer0["augmented_torsion_vs_bosonic_euler_density"] == "DISTINCT"
    assert layer0["cyclic_square_vs_action_variation"] == "DISTINCT"
    assert layer0["diagonal_complex_shell_vs_i1b_critical_shell"] == "EXACT_CONTROL_SHOWS_DIFFERENT"

    shifted = registry["shifted_operator"]
    assert shifted["internal_degrees"] == [0, 1]
    assert shifted["all_blocks_total_degree_one"] is True
    assert shifted["total_parity_odd_exact"] is True
    assert shifted["even_to_odd_restriction_nonzero"] is True
    assert shifted["odd_to_even_restriction_nonzero"] is True
    assert shifted["algebraic_full_parity_pair_built"] is True
    assert shifted["analytic_complex_built"] is False

    square = registry["square"]
    assert square["northeast"] == "MINUS_D_A_F_B_PLUS_F_B_D_B"
    assert square["noncommutative_mixed_defect_nonzero"] is True
    assert square["ig_left_module_mixed_defect"] == "MINUS_T_WEDGE_F_B"
    assert square["scalar_commuting_fixture_erases_defect"] is True
    assert square["diagonal_A_equals_B_square_zero"] is True

    action = registry["source_action"]
    assert action["owner"] == "PREEXISTING_I1B"
    assert action["linear_coefficient"] == "1/2"
    assert action["quadratic_coefficient"] == "1/3"
    assert action["coefficient_solution_unique"] is True
    assert action["finite_cyclic_first_variation_endpoint_curvature_exact"] is True
    assert action["finite_indefinite_hessian_symmetric"] is True
    assert action["actual_moving_k77_shiab_selected"] is False
    assert action["action_for_2025_operator_established"] is False

    shell = registry["shell_comparison"]
    assert shell["naive_ig_pair_complex_shell"] == "T_ZERO"
    assert shell["naive_shell_match"] is False
    assert shell["bosonic_euler_primalizer_built"] is False
    assert shell["candidate_pair_difference"] == "R_B_APPLIED_TO_UPSILON"

    assert registry["selection"] == {
        "transgression_parameters": 2,
        "transgression_constraints": 2,
        "transgression_constraint_surplus": 0,
        "trace_q_selection_rank_added": 0,
        "trace_q_projective_parameters": 1,
        "trace_q_constraint_surplus": -1,
    }
    assert registry["probe_receipt"] == {
        "source": 14, "type": 20, "exact": 22, "planted": 12,
        "total": 68, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"

    wave2 = campaign["waves"][1]
    advance = wave2["latest_advance"]
    assert advance["status"] == expected
    assert advance["result_ref"].endswith(
        "k77-wave2-two-connection-shifted-superconnection-action-owner-2026-08-04.md"
    )
    assert advance["next_required_build"] == registry["next_required_build"]
    assert advance["supersedes_carried_debt"] == [
        "FULL_TWO_CONNECTION_CYCLIC_EVEN_ODD_ARROW_PAIR",
        "TWO_CONNECTION_ACTION_HELMHOLTZ_OWNER",
    ]
    assert "ACTUAL_K77_BOSONIC_EULER_PRIMALIZER" in advance["replacement_debt"]
    for token in (
        "SHIFTED_TOTAL_ODD_TWO_CONNECTION_OPERATOR",
        "BOTH_ALGEBRAIC_PARITY_RESTRICTIONS",
        "NONCOMMUTATIVE_MIXED_T_WEDGE_F_B_DEFECT",
        "PREEXISTING_I1B_ACTION_OWNER_LOCATED",
        "PATH_AVERAGE_CURVATURE_ONE_HALF_ONE_THIRD",
        "NAIVE_IG_PAIR_ACTION_SHELL_MISMATCH",
    ):
        assert token in wave2["emitted"]
    for token in (
        "ACTUAL_K77_BOSONIC_EULER_PRIMALIZER",
        "ACTION_SHELL_TWO_CONNECTION_LIFT",
        "I1B_TO_2025_CYCLIC_OPERATOR_ACTION_IDENTIFICATION",
    ):
        assert token in wave2["carried_debt"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for token in (
        "shifted total-odd operator",
        "mixed defect",
        "connection-path average",
        "diagonal complex shell and the action shell are different",
        "surplus zero",
        "p1/p2/p3: unchanged and unused",
        "wave 3: closed",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "summary outruns the artifact",
        "stale or superseded object",
        "scalar fixture",
        "bosonic primalizer",
        "68/68 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "source-confirms_preexisting",
        "source-silent",
        "augmented torsion",
        "swervature equals displasion",
        "bosonic primalizer",
    ):
        assert token in source, f"missing source token: {token}"

    test_files = list((ROOT / "tests/channel-swings").glob("*.py"))
    gate_files = list((ROOT / "process_gates").glob("*.py"))
    tests_readme = (ROOT / "tests/README.md").read_text(encoding="utf-8")
    gates_readme = (ROOT / "process_gates/README.md").read_text(encoding="utf-8")
    assert len(test_files) == 175
    assert "`channel-swings/` (175)" in tests_readme
    assert len(gate_files) == 140
    assert "k77_wave2_two_connection_action_owner_scope_audit.py" in gates_readme

    forbidden = (
        "i1b is the action of the 2025 cyclic operator",
        "the mixed bianchi identity holds",
        "the actual k77 shiab is selected",
        "the physical dirac Hamiltonian is built",
        "wave 3 is open",
        "p1 is consumed",
    )
    for phrase in forbidden:
        assert phrase not in report
        assert phrase not in review

    print("k77_wave2_two_connection_action_owner_scope_audit: PASS")
    print("  shifted pair built; mixed defect live; I1B located; Euler primalizer open")


if __name__ == "__main__":
    main()
