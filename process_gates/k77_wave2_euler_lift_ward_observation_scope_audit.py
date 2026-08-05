#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 Euler-lift observation receiver packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-euler-lift-ward-observation-port.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-euler-lift-ward-observation-review.md"
SOURCE = ROOT / "lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md"


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

    assert registry["named_gate"] == "K77_EULER_LIFT_FULL_FIELD_WARD_DOMAIN_OBSERVATION_PORT"
    assert registry["gate_status"] == "PARTIAL_WITH_NAMED_MOVEMENT"

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE-AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "0_SELECTOR_PARAMETERS"
    assert pre["search_space_scope"] == "KERNEL_OF_RHO_X_COMPOSE_SHARP_X_COMPOSE_O_E"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [{"id": "K77-W2-OBSERVATION-PORT", "grade": "T3"}]

    source_collision = registry["source_collision"]
    assert source_collision["observerse_section_pullback"] == "SOURCE_CONFIRMS"
    for key in ("equation_dual_receiver", "euler_no_leakage", "observed_coefficient_faithfulness"):
        assert source_collision[key] == "SOURCE_SILENT"

    for value in registry["layer0"].values():
        assert value == "DISTINCT"

    theorem = registry["receiver_theorem"]
    assert theorem["detection_map"] == "RHO_X_COMPOSE_SHARP_X_COMPOSE_O_E"
    assert theorem["unconditional_observed_shell"] == "UPSTAIRS_EULER_MODULO_DETECTION_KERNEL"
    assert theorem["equation_no_leakage_required"] is True
    assert theorem["faithfulness_on_observed_tau_image_required"] is True
    assert theorem["pseudo_musical_naturality_required"] is True
    assert theorem["restricted_bidirectional_shell_theorem"] is True
    assert theorem["actual_y14_receiver_built"] is False

    fixture = registry["exact_fixture"]
    assert fixture["equation_blind_dimension"] == 2
    assert fixture["complete_blind_kernel_dimension"] == 3
    assert fixture["additional_representation_blind_dimension"] == 1
    assert fixture["faithful_restricted_kernel_dimension"] == 0
    assert fixture["false_shell_by_equation_leakage"] is True
    assert fixture["false_shell_by_representation_blindness"] is True

    boundary = registry["ward_preboundary_domain"]
    assert boundary["even_ward_naturality_exact_finite"] is True
    assert boundary["ward_implies_no_leakage"] is False
    assert boundary["preboundary_pullback_exact_finite"] is True
    assert boundary["derived_bv_differential_built"] is False
    assert boundary["common_closed_analytic_domain_built"] is False
    assert boundary["physical_bfv_phase_space_built"] is False

    assert registry["accounting"] == {
        "selector_parameters": 0,
        "new_free_coefficients": 0,
        "free_object_delta": 0,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 7,
        "type": 29,
        "exact": 32,
        "planted": 7,
        "total": 75,
        "failures": 0,
    }
    assert registry["hostile_review"] == (
        "PASS_WITH_MATERIAL_SCOPE_REPAIRS__PARTIAL_NAMED_GATE_MOVEMENT"
    )
    assert registry["next_required_build"] == (
        "K77_ACTUAL_Y14_EULER_RECEIVER_FAITHFUL_MODULE_AND_COMMON_GREEN_DOMAIN"
    )
    assert registry["wave3_open"] is False
    assert registry["p1_p2_p3_used"] is False
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    assert wave2["result_ref"] == (
        "explorations/k77-wave2-euler-shell-two-connection-lift-2026-08-04.md"
    )
    continuation = wave2["continuations"][-1]
    assert continuation["named_gate"] == registry["named_gate"]
    assert continuation["result_ref"] == (
        "explorations/k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md"
    )
    assert continuation["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "OBSERVED_SHELL_DETECTION_KERNEL_RHO_X_SHARP_X_O_E",
        "EXACT_EQUATION_LEAKAGE_FALSE_SHELL",
        "EXACT_REPRESENTATION_BLINDNESS_FALSE_SHELL",
        "NO_LEAKAGE_PLUS_IMAGE_FAITHFULNESS_RESTORES_CONVERSE",
    ):
        assert emitted in wave2["emitted"]
    for debt in (
        "ACTUAL_POST_OBSERVATION_COEFFICIENT_MODULE_AND_IMAGE_FAITHFULNESS",
        "ACTUAL_Y14_EQUATION_DUAL_AND_ACTION_IMAGE_NO_LEAKAGE",
        "COMMON_CLOSED_KREIN_GREEN_DOMAIN",
    ):
        assert debt in continuation["replacement_debt"]
    assert "TOE_COEFFICIENT_MODULE_IDENTIFICATION_AND_FAITHFULNESS" in continuation["supersedes_debt"]
    assert "OBSERVATION_DESCENT_AND_NO_LEAKAGE" in continuation["supersedes_debt"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "equation leakage",
        "representation blindness",
        "ker(rho_x sharp_x o_e)",
        "ward closure does not replace no-leakage",
        "free object delta | 0",
        "p1/p2/p3 remain unchanged and unused",
        "wave 3 stays closed",
    ):
        assert phrase in report
    assert "search_space_dim: 0 selector parameters" in report
    assert "fork_stack_acknowledged:" in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends a superseded object",
        "characteristic kernel means gauge",
        "residue_tightness: {t3: 1}",
        "pass_with_material_scope_repairs__partial_named_gate_movement",
    ):
        assert phrase in review

    assert "source-confirms" in source
    assert "source-silent" in source
    assert "equation-dual" in source

    next_steps = normalized(ROOT / "NEXT-STEPS.md")
    explorations_readme = normalized(ROOT / "explorations/README.md")
    tests_readme = normalized(ROOT / "tests/README.md")
    gates_readme = normalized(ROOT / "process_gates/README.md")
    improvement = normalized(ROOT / "lab/process/improvement-register-2026-08-03.md")
    for surface in (next_steps, explorations_readme):
        assert "k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md" in surface
        assert "k77_actual_y14_euler_receiver_faithful_module_and_common_green_domain" in surface
    assert "channel-swings/` (177)" in tests_readme
    assert "k77_wave2_euler_lift_ward_observation_probe.py" in tests_readme
    assert "k77_wave2_euler_lift_ward_observation_scope_audit.py" in gates_readme
    assert "revision 32" in improvement
    assert "two independent false-shell" in improvement

    print("k77_wave2_euler_lift_ward_observation_scope_audit: PASS")
    print("  observation shell is quotient-typed; two blindness kernels exact")
    print("  actual Y14 receiver, BV and common Green domain remain open")


if __name__ == "__main__":
    main()
