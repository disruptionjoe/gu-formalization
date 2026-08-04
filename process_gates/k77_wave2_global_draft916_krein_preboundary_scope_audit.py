#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 draft-9.16 primalizer templates."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-global-draft916-krein-preboundary.json"
REPORT = ROOT / "explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-k77-wave2-global-draft916-krein-preboundary-review.md"
SOURCE = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"


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

    expected_status = (
        "PARTIAL__DRAFT916_SOURCE_MATRIX_AND_FORMAL_PRIMALIZER_TEMPLATES_BUILT__"
        "ACTUAL_D916_K77_ASSEMBLY_OPEN"
    )
    assert registry["gate_status"] == expected_status
    assert len(registry["layer0_objects"]) == 8

    collision = registry["source_collision"]
    assert collision["four_field_matrix"] == "SOURCE_DISPLAYS_CANDIDATE"
    assert collision["southeast_zero"] == "SOURCE_DISPLAYS_2021__REITERATES_PROSPECTIVELY_2025"
    assert collision["nonzero_southeast"] == "SOURCE_ADMITS_UNSPECIFIED_RIVAL"
    assert collision["global_krein_adjoint"].startswith("SOURCE_SILENT")
    assert collision["three_observed_chiral_families"].endswith("DOES_NOT_DERIVE")

    hodge = registry["hodge_primalizer"]
    assert [hodge[f"degree_{p}"] for p in (0, 1, 13, 14)] == [-1, 1, 1, -1]
    assert hodge["omega13_to_omega1_inverse_sign"] == "PLUS_STAR_B_INVERSE"
    assert hodge["omega14_to_omega0_inverse_sign"] == "MINUS_STAR_B_INVERSE"

    built = registry["built_now"]
    assert built["primalizer"].endswith("ACTUAL_128_SPINOR_MAP_OPEN")
    assert built["formal_adjoint"].endswith("ACTUAL_D916_SUBSTITUTION_OPEN")
    assert built["overlap_descent"].endswith("ACTUAL_D916_DESCENT_OPEN")
    assert built["variational_core"].endswith("COMMON_INVARIANCE_OPEN")
    assert len(registry["actual_d916_burden"]) == 8

    fixture = registry["exact_fixture"]
    assert fixture == {
        "source": 7,
        "type": 23,
        "exact": 19,
        "planted": 5,
        "total": 54,
        "failures": 0,
    }

    family = registry["observer_family_disposition"]
    assert "CHOSEN_SPLITTING_IMAGE" in family["kinematic_pieces"][1]
    assert family["three_observed_chiral_families"] == "NOT_DERIVED"
    assert family["wave3_preflight"].endswith("NOT_ADMITTED_UNTIL_WAVE2_CLOSES")

    assert registry["review_contract"]["hostile_review"] == "COMPLETE__UNANIMOUS_REPAIR_AND_PARTIAL_DISPOSITION"
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert all(value is False for value in registry["status_boundary"].values())

    wave2 = campaign["waves"][1]
    frontier = campaign["frontier"]
    successor_status = (
        "PARTIAL__NATIVE_EVEN_SHIAB_HOM0__DEGREE_REALITY_SAT_REQUIRES_ONE_ODD_COVECTOR__"
        "EXACT_Q_REPAIRS_BUILT__OWNERSHIP_ADJOINT_WARD_OPEN"
    )
    assert wave2["status"] == successor_status
    assert "Q_RECEIVER_OWNERSHIP_AND_DEGREE_REALITY_VS_LEFT_RIGHT_SHIAB_PLACEMENT" in wave2["carried_debt"]
    assert frontier["completed_waves"] == [1]
    assert frontier["partial_waves"] == [2]
    assert frontier["next_wave"] == 2
    assert frontier["next_named_gate"] == "RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD"
    assert frontier["next_required_build"] == "K77_D916_Q_RECEIVER_OWNERSHIP_ADJOINT_WARD_SELECTION"
    assert frontier["wave3_preflight_retained"].endswith("NOT_YET_ADMITTED")

    for token in (
        "does **not** yet assemble the actual sixteen-block k77 operator",
        "d_pr = r d916",
        "degrees `0` and `14` have `*^2=-1`",
        "model overlap descent, not actual d916 descent",
        "candidate compact-support variational core",
        "chosen splitting image",
        "wave 2 therefore remains `partial`",
        "p1/p2/p3 use",
        "successor advance and correction",
        "source_sign_duality_shiab_parity_reconciliation",
    ):
        assert token in report, f"missing report token: {token}"

    for token in (
        "repaired_partial__source_and_templates_pass__actual_d916_k77_assembly_open",
        "generic theorem or finite model was being reported",
        "before constructing a primalizer",
        "principal-adjoint test compared an expression with itself",
        "reverted campaign frontier from wave 3 to wave 2 partial",
        "7 source + 23 type + 19 exact + 5 planted = 54 pass",
    ):
        assert token in review, f"missing review token: {token}"

    for token in (
        "rho(epsilon)",
        "displayed covariance ansatz",
        "outer hodge star around the entire column",
        "source-displays-2021 / reiterates-prospectively-2025",
        "chosen gamma-trace complement",
    ):
        assert token in source, f"missing source token: {token}"

    print("k77_wave2_global_draft916_krein_preboundary_scope_audit: PASS")
    print("  rendered matrix and exact templates retained; actual D916 assembly, common core, observation, physics, and datum use remain open")


if __name__ == "__main__":
    main()
