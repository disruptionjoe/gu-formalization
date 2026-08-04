#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave K77-A.

This preserves carrier/particle, source/proof, local/joint, and typed-kill
distinctions. It does not reproduce the exact Clifford computation.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "lab/process/resolver-wave-k77a-atomic-particle-crosswalk.json"
DISPOSITION = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-disposition-2026-08-04.json"
REPORT = ROOT / "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"
PROBE = ROOT / "tests/channel-swings/resolver_wave_k77a_real_spinor_atomic_crosswalk_probe.py"


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
    ledger = load(LEDGER)
    disposition = load(DISPOSITION)
    report = REPORT.read_text(encoding="utf-8")
    probe = PROBE.read_text(encoding="utf-8")

    expected_verdict = (
        "NONCHIRAL_PARENT_AND_OBSERVATION_BLOCKS_CONFIRMED__"
        "VEV_BLOCK_CLASSIFIED_NOT_SELECTED__EFFECTIVE_CHIRALITY_NOT_DERIVED"
    )
    assert ledger["verdict"] == expected_verdict
    assert disposition["gate_after"] == expected_verdict
    assert ledger["route_decision"] == disposition["route_disposition"] == "CONTINUE_K77"
    assert disposition["hostile_review_status"] == "PASS_AFTER_MATERIAL_REPAIR_AND_SCOPE_NARROWING"
    assert disposition["third_lane_promoted"] is False

    carrier = disposition["carrier"]
    assert carrier["Cl77"] == "M128_R"
    assert carrier["real_spinor_dimension"] == 128
    assert carrier["real_majorana_weyl_dimensions"] == [64, 64]
    assert carrier["source_split"] == [[1, 3], [6, 4]]
    assert carrier["observation_complex_block_dimensions"] == [32, 32, 32, 32]
    assert carrier["invariant_symmetric_form"] == "B_SPLIT_64_64_CROSS_HALF_PERFECT"

    targets = ledger["atomic_targets"]
    assert len(targets) == disposition["atomic_ledger"]["rows"] == 37
    assert all(row["candidate_status"] and row["reconstruction_debt"] for row in targets)
    assert disposition["atomic_ledger"]["physical_rows_complete"] == 0
    assert len(ledger["source_claims"]) == disposition["atomic_ledger"]["source_claims"] == 13
    assert len(ledger["source_silence_audits"]) == disposition["atomic_ledger"]["source_silence_audits"] == 1
    assert len(ledger["mechanisms"]) == 12
    assert len(ledger["coherence_matrix"]) == 11
    assert {key: len(value) for key, value in ledger["obligation_scopes"].items()} == disposition["kill_policy"]["obligation_counts"]
    assert set().union(*(set(rows) for rows in ledger["obligation_scopes"].values())) == {row["row_id"] for row in targets}

    expected_kills = [
        "FIXTURE_FAIL",
        "CANDIDATE_MAP_KILL",
        "MECHANISM_KILL",
        "LANE_KILL",
        "CONDITIONAL_PROGRAM_KILL",
    ]
    assert [entry["scope"] for entry in ledger["kill_ladder"]] == expected_kills
    assert disposition["kill_policy"]["ordered_scopes"] == expected_kills
    assert disposition["kill_policy"]["target_status"] == "SCOPED_OBLIGATION_ORTHOGONAL_TO_CANDIDATE_STATUS"
    assert disposition["kill_policy"]["lane_kill_requires_exhaustion"] is True
    assert disposition["kill_policy"]["program_kill_requires_layer0_and_seven_axes"] is True

    generation = next(row for row in targets if row["row_id"] == "generation_multiplicity")
    assert generation["kill_scope"] == "CANDIDATE_MAP_KILL"
    assert generation["candidate_status"] == "CANDIDATE_MAP_KILL__LAYER0_WRONG_COUNT_OBJECT"
    assert disposition["drs"]["block_count_is_generation_count"] is False

    assert disposition["bilinear_incidence"]["vertical_KX"] == ["flip_4d", "preserve_ambient"]
    assert disposition["bilinear_incidence"]["selected_VEV"] is False
    assert disposition["bilinear_incidence"]["mass_or_yukawa_derived"] is False
    assert disposition["source_policy"]["descriptions_are_search_directives"] is True
    assert disposition["source_policy"]["math_outranks_source"] is True
    assert disposition["source_policy"]["individual_atomic_poles"] == "SEPARATE_WHOLE_SURFACE_SOURCE_SILENCE_AUDIT_NOT_SPEAKER_CLAIM"
    assert disposition["stale_object_fence"]["status"] == "FENCED"
    corrected_owner = ROOT / disposition["stale_object_fence"]["corrected_owner"]
    assert corrected_owner.exists()
    assert "no natural Spin(7,7)-equivariant R-linear map S -> Lambda^k exists" in corrected_owner.read_text(encoding="utf-8")
    assert ledger["identity_fences"]["cross_half_duality_vs_equivariant_identification"].startswith("B_PROVES_DUALITY")
    assert ledger["group_level_observation_image"].startswith("(Spin(1,3) x Spin(6,4))/diag(Z2)")
    assert disposition["drs"]["K77_FQZ_invariant_subspaces_and_projectors"] == "OPEN"
    assert disposition["standard_model_packet"]["K77_derives_internal_weights_here"] is False
    assert disposition["campaign_dependency"]["Wave_K95_predecessor"].startswith("SEQUENCING_ONLY")

    forbidden = set(ledger["forbidden_k95_imports"])
    assert {"right-H", "Sp(32,32;H)", "R_J", "Kramers index"}.issubset(forbidden)
    assert ledger["external_datum"] == {"P1_P2": "UNUSED", "P3": "UNUSED"}
    assert disposition["external_datum"] == {"P1_P2": "unchanged_unused", "P3": "unchanged_unused"}

    for token in (
        "37 rows",
        "Eric and Curt are search directives, not final authorities",
        "PROGRAM_MANDATORY",
        "LOCAL_PASS__JOINT_FAIL",
        "vertical row is therefore a real opportunity",
        "three kinematic blocks => three observed generations",
        "None of the 37 rows",
        "P1/P2/P3 remain unchanged and unused",
    ):
        assert token in report, f"report missing scope token {token!r}"

    for token in (
        "p77_real_index_twin",
        "historical_text",
        "forbidden_k95_imports",
        "generation count is fenced",
        "locked-leg conflict blocks O3 promotion",
    ):
        assert token in probe, f"probe missing fence {token!r}"

    print("resolver_wave_k77a_scope_audit: PASS")
    print("  scoped obligations, typed kills, source grades, carrier/physics, and K77/K95 fences retained")


if __name__ == "__main__":
    main()
