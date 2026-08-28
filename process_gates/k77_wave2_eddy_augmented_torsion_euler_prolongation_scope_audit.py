#!/usr/bin/env python3
"""Fail-closed scope audit for the corrected K77 eddy/Euler packet."""

from __future__ import annotations

import json
from pathlib import Path

from k77_wave2_augmented_torsion_defect_euler_receiver_scope_audit import historical_wave2_checkpoint


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-eddy-augmented-torsion-euler-prolongation.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-eddy-augmented-torsion-euler-prolongation-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-eddy-augmented-torsion-euler-prolongation-review.md"
SOURCE = ROOT / "lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_eddy_augmented_torsion_euler_prolongation_probe.py"
SAGE = ROOT / "tests/channel-swings/k77_wave2_eddy_augmented_torsion_euler_prolongation_independent.sage"


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

    assert registry["artifact"] == "K77_WAVE2_EDDY_AUGMENTED_TORSION_EULER_PROLONGATION"
    assert registry["lane"] == "1"
    assert registry["fork"] == "SIGNATURE_AMBIENT_7_7"
    assert registry["gate_before"] == (
        "K77_EDDY_COMPLETED_AUGMENTED_TORSION_CHAIN_MAP_AND_FULL_EULER_COMPARISON_FUNCTOR"
    )
    assert registry["gate_after"] == (
        "K77_ACTION_OWNED_SELECTED_SHIAB_EULER_AND_DEGREE14_TOTALIZATION_WITH_RAW_NORTHEAST_OWNER"
    )
    assert registry["verdict"] == (
        "EDDY_PATH_AVERAGE_RECONSTRUCTED__ACTION_FRECHET_ADJOINT_EULER_FUNCTOR_BUILT_CONDITIONALLY__PRINTED_ENDPOINT_KILL_RETAINED__ACTION_DEGREE14_AND_RAW_NORTHEAST_OPEN"
    )

    source_disposition = registry["source_disposition"]
    assert source_disposition["eddy_action_and_printed_pair"] == "SOURCE_CONFIRMS_FORMULAS"
    assert source_disposition["printed_endpoint_as_selected_action_derivative"] == (
        "REPO_SUPERSEDES_KILLED_RETAINED"
    )
    assert source_disposition["action_frechet_adjoint_euler"] == "REPO_CONSTRUCTS_PRIMARY"
    assert source_disposition["action_owned_degree14"] == "SOURCE_SILENT"
    assert source_disposition["cyclic_two_connection_square"] == "SOURCE_UNRELEASED"
    assert source_disposition["raw_northeast_owner"] == "SOURCE_SILENT"

    assert registry["layer0"]["status"] == "PASS_AFTER_SUPERSEDED_ENDPOINT_RETRACTION"
    assert all(
        value == "DISTINCT"
        for key, value in registry["layer0"].items()
        if key != "status"
    )

    transgression = registry["transgression"]
    assert transgression["path_average"] == "F_B+(1/2)D_B_T+(1/3)T2"
    assert transgression["printed_endpoint"] == "S_omega(F_A)+star_kappa_T"
    assert transgression["action_euler"] == (
        "S_omega(barF)+(D_T_barF)^bang_S_omega^bang_T+star_kappa_T"
    )
    assert transgression["selected_full_domain_printed_endpoint"] == "KILLED_RETAINED"
    assert transgression["bracket_convention"] == "NORMALIZED_PRODUCT_CONVENTION"

    comparison = registry["two_connection_comparison"]
    assert comparison["path_average_reconstruction"] == "F_B+(1/2)DeltaF-(1/6)T2"
    assert comparison["action_euler_functor"] == (
        "BUILT_CONDITIONALLY_AT_FORMAL_VARIATIONAL_GRADE"
    )
    assert comparison["complete_real_K77_selected_adjoint"] == "OPEN"

    printed = registry["printed_rival_symbol"]
    assert printed["input_rank_by_orbit"] == {
        "positive": 182, "negative": 182, "null": 182
    }
    assert printed["defect_rank_by_orbit"] == {
        "positive": 13, "negative": 13, "null": 13
    }
    assert printed["nonzero_columns_by_orbit"] == {
        "positive": 13, "negative": 13, "null": 28
    }
    assert printed["riemann_carrier_rank"] == 91
    assert printed["riemann_defect_rank"] == 0
    assert printed["owner"].startswith("D_omega_OF_SOURCE_PRINTED_ENDPOINT_RIVAL")

    northeast = registry["raw_northeast"]
    assert northeast["formula"] == "-T_wedge_F_B"
    assert northeast["nonzero"] is True
    assert northeast["determined_by_fixed_F_A_and_T"] is False
    assert northeast["identified_with_printed_xi"] is False
    assert northeast["identified_with_stress_energy"] is False
    assert northeast["possible_action_companion_participation"] == "OPEN"

    checks = registry["checks"]
    assert checks["main"] == "7 source + 36 type + 34 exact + 10 planted = 87 PASS"
    assert checks["independent_sage"] == "PASS_PRINTED_RIVAL_AND_IDENTITY_CONTROL_ONLY"
    assert checks["predecessors"] == [
        "K77_WAVE2_PRINCIPAL_BIANCHI_PRODUCT_SELECTOR",
        "K77_WAVE2_TWO_CONNECTION_ACTION_OWNER",
        "RESOLVER_WAVE_K77B3_FULL_DOMAIN_CYCLIC_KERNEL_OBSTRUCTION",
        "K77_WAVE2_ACTION_CURRENT_RIESZ_SUPERIG_WARD",
    ]
    assert checks["hostile_review"] == "PASS_AFTER_SUPERSEDED_ENDPOINT_RETRACTION"

    for debt in (
        "complete_real_K77_selected_Shiab_formal_adjoint",
        "action_owned_degree14_Noether_or_redundancy_row",
        "raw_northeast_stress_energy_fermion_or_homotopy_owner",
        "total_boson_fermion_euler_rendezvous",
        "global_closed_Krein_Green_domain",
        "observation_and_physics",
        "P1_P2_P3",
        "Wave3",
    ):
        assert debt in registry["held_open"]
    assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert registry["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3"
    assert registry["third_lane_status"] == "NOT_PROMOTED"

    required_emissions = (
        "EDDY_PATH_AVERAGE_RECONSTRUCTED_FROM_TWO_CONNECTION_DATA",
        "IDENTITY_SHIAB_ENDPOINT_CONTROL_NOT_SELECTED_SHIAB_PROOF",
        "ACTION_FRECHET_ADJOINT_EULER_FUNCTOR_FORMULA",
        "SOURCE_PRINTED_ENDPOINT_K77B3_KILL_RETAINED",
        "SOURCE_PRINTED_XI_RIVAL_DEFECT_RANK13_ALL_COVECTOR_ORBITS",
        "PRINTED_13_PLUS_14_FIRST_PROLONGED_RIVAL_NOT_ACTION_EULER",
        "ACTION_OWNED_DEGREE14_COMPANION_OPEN",
        "RAW_NORTHEAST_FIXED_ENDPOINT_SPLITTING_NONUNIQUENESS",
        "HOSTILE_REVIEW_SUPERSEDED_ENDPOINT_RETRACTION",
    )
    historical_wave2_checkpoint(campaign, required_emissions)

    for phrase in (
        "outcome first",
        "accidentally revived the killed endpoint",
        "action's actual euler derivative",
        "fréchet/formal-adjoint companion",
        "source_printed_endpoint_as_selected_full_domain_action_derivative:",
        "printed-rival defect rank",
        "action_owned_degree14_companion:",
        "raw_northeast_owner_or_homotopy:",
    ):
        assert phrase in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends a superseded object",
        "decisive correction",
        "proof engineering",
        "pass_after_superseded_endpoint_retraction",
    ):
        assert phrase in review

    for phrase in (
        "source-displays",
        "repo-supersedes",
        "action-owned euler covector",
        "source-unreleased",
        "source-guides-hypothesis",
        "source-silent",
    ):
        assert phrase in source

    for phrase in (
        "complete k77-b3 selected-shiab cyclic-kernel obstruction replays",
        "actual action euler splits into direct, frechet-adjoint companion, and kappa rows",
        "action-owned euler differs from the source-printed endpoint",
        "printed selected-shiab degree-14 rival has rank 13",
        "rank thirteen belongs to d of the printed shiab endpoint",
        "action_owned_degree14_companion=open",
    ):
        assert phrase in probe

    for phrase in (
        "sage_independent_eddy_euler_prolongation_pass",
        '"positive": (182, 13, 13)',
        '"negative": (182, 13, 13)',
        '"null": (182, 13, 28)',
        "assert derivative_coefficient == 1",
        "assert eddy_coefficient == 1",
    ):
        assert phrase in sage

    tests_readme = normalized(ROOT / "tests/README.md")
    assert "k77_wave2_eddy_augmented_torsion_euler_prolongation_probe.py" in tests_readme

    print("PASS: corrected K77 eddy/action-Euler packet retains the printed-endpoint kill")


if __name__ == "__main__":
    main()
