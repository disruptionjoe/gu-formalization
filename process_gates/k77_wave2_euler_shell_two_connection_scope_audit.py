#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 Euler-shell dependent-pair packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-euler-shell-two-connection-lift.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-euler-shell-two-connection-lift-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-euler-shell-two-connection-review.md"
SOURCE = ROOT / "lab/sources/gu-euler-shell-two-connection-source-reinspection-2026-08-04.md"


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

    assert registry["named_gate"] == (
        "K77_BOSONIC_EULER_PRIMALIZER_AND_ACTION_SHELL_TWO_CONNECTION_LIFT"
    )
    assert registry["gate_status"] == "PARTIAL_WITH_NAMED_MOVEMENT"

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE-AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == 1
    assert "ORDER_ZERO_METRIC_DENSITY" in pre["search_space_scope"]
    assert pre["free_object_delta"] == -1
    assert pre["residue_touched"] == [{"id": "K77-W2-ACTION-SHELL", "grade": "T3"}]

    layer0 = registry["layer0"]
    for key in (
        "advertised_upsilon_vs_actual_euler",
        "euler_covector_vs_primal_one_form",
        "ig_augmented_torsion_vs_euler_pair_difference",
        "translation_shell_vs_full_stationarity",
        "algebraic_complex_vs_closed_domain",
        "faithful_module_vs_physical_quotient",
    ):
        assert layer0[key] == "DISTINCT"

    primalizer = registry["primalizer"]
    assert primalizer["associated_bundle_density_grade"] == "BUILT"
    assert primalizer["indefinite"] is True
    assert primalizer["inverse_exact"] is True
    assert primalizer["moving_inverse_identity_exact"] is True
    assert primalizer["orientation_datum_required"] is False
    assert primalizer["positive_riesz"] is False
    assert primalizer["closed_analytic_domain"] is False

    pair = registry["pair_lift"]
    assert pair["euler_owner"] == "E_T_B_ACTUAL_SYMMETRIZED_DERIVATIVE"
    assert pair["dependent_not_free"] is True
    assert pair["source_identified"] is False
    assert pair["source_grade"] == "SOURCE_COMPATIBLE_CONDITIONAL"

    square = registry["square"]
    assert square["off_shell_southwest_live"] is True
    assert square["off_shell_northeast_live"] is True
    assert square["translation_shell_implies_nilpotence"] is True
    assert square["nilpotence_implies_translation_shell"] == (
        "TRUE_IF_COEFFICIENT_ACTION_FAITHFUL_OR_ADJOINT_CENTERLESS"
    )
    assert square["exact_fixture_module"] == "FAITHFUL_LEFT_REGULAR"
    assert square["full_action_stationarity_equivalence"] is False

    naturality = registry["naturality"]
    assert naturality["coadjoint_to_adjoint"] == "CONDITIONAL_ON_ACTION_WARD"
    assert naturality["homogeneous_transition_exact"] is True
    assert naturality["shared_inhomogeneous_term_cancels_exact"] is True
    assert naturality["full_moving_local_gauge_descent"] is False

    accounting = registry["accounting"]
    assert accounting == {
        "natural_map_parameters": 1,
        "duality_constraints": 1,
        "constraint_surplus": 0,
        "new_free_coefficients": 0,
        "free_object_delta": -1,
    }
    assert registry["probe_receipt"] == {
        "source": 8,
        "type": 30,
        "exact": 29,
        "planted": 9,
        "total": 76,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_MATERIAL_SCOPE_REPAIRS__PARTIAL_NAMED_GATE_MOVEMENT"
    )
    assert registry["next_required_build"] == (
        "K77_EULER_LIFT_FULL_FIELD_WARD_DOMAIN_OBSERVATION_PORT"
    )
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    # This is a predecessor audit, so campaign-latest pointers may advance.
    # Preserve the predecessor by its emitted result and require any successor
    # to begin at the next gate recorded in this registry.
    latest = wave2["latest_advance"]
    if latest["named_gate"] == registry["named_gate"]:
        assert latest["next_required_build"] == registry["next_required_build"]
    else:
        assert latest["named_gate"] == registry["next_required_build"]
        assert wave2["result_ref"].endswith(
            "k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md"
        )
    for emitted in (
        "K77_BOSONIC_DENSITY_ADJOINT_PSEUDO_MUSICAL",
        "DIMENSION_ONE_PAIRING_GENERATED_NATURAL_MAP_SPACE",
        "ACTION_OWNED_DEPENDENT_EULER_PAIR_LIFT",
        "TRANSLATION_EULER_SHELL_IFF_SHIFTED_COMPLEX_ON_FAITHFUL_MODULE",
        "OFFSHELL_MIXED_DEFECT_PROPORTIONAL_TO_EULER_LIFT",
    ):
        assert emitted in wave2["emitted"]
    assert "ACTUAL_K77_BOSONIC_EULER_PRIMALIZER" not in wave2["carried_debt"]
    assert "ACTION_SHELL_TWO_CONNECTION_LIFT" not in wave2["carried_debt"]
    current_next = (
        wave2["continuations"][-1]["next_required_build"]
        if wave2.get("continuations")
        else latest["next_required_build"]
    )
    assert campaign["frontier"]["next_required_build"] == current_next
    assert campaign["frontier"]["latest"]["next_required_build"] == current_next

    for phrase in (
        "source-silent",
        "faithful coefficient module",
        "translation euler row",
        "full action stationarity",
        "constraint surplus | 0",
        "free object delta | -1",
        "p1/p2/p3 remain unchanged and unused",
        "wave 3 remains closed",
    ):
        assert phrase in report
    assert "search_space_dim: 1" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends a superseded object",
        "faithful module or centerless adjoint carrier",
        "residue_tightness: {t3: 1}",
        "pass_with_material_scope_repairs__partial_named_gate_movement",
    ):
        assert phrase in review

    assert "source-silent" in source
    assert "source-compatible-conditional" in source
    assert "actual noncyclic euler derivative" in source

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    tests_readme = normalized(ROOT / "tests/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-euler-shell-two-connection-lift-2026-08-04.md" in surface
        assert "k77_euler_lift_full_field_ward_domain_observation_port" in surface
    assert "channel-swings/` (177)" in tests_readme
    assert "k77_wave2_euler_shell_two_connection_probe.py" in tests_readme
    assert "k77_wave2_euler_shell_two_connection_scope_audit.py" in gates_readme
    assert "revision 31" in improvement
    assert "faithful coefficient module" in improvement

    print("k77_wave2_euler_shell_two_connection_scope_audit: PASS")
    print("  dependent Euler pair built; faithful-module shell equivalence exact")
    print("  full-field Ward/domain/observation port remains open")


if __name__ == "__main__":
    main()
