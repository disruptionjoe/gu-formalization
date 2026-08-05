#!/usr/bin/env python3
"""Fail-closed scope audit for K77 action polarization/common-domain packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-action-polarization-common-observation-domain.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-action-polarization-common-observation-domain-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-action-polarization-common-observation-domain-review.md"
SOURCE = ROOT / "lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_action_polarization_common_observation_domain_probe.py"
SAGE = ROOT / "tests/channel-swings/k77_wave2_action_polarization_channel_rank_independent.sage"


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

    assert registry["named_gate"] == (
        "K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN"
    )
    assert registry["gate_status"] == (
        "PARTIAL_WITH_EXACT_HELMHOLTZ_NONSELECTION_AND_CONDITIONAL_COMMON_OBSERVATION_SCALE"
    )
    assert registry["gate_after"] == (
        "K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET"
    )

    pre = registry["pre_wave"]
    assert pre["fork_assumed"] == "SIGNATURE_AMBIENT"
    assert pre["fork_horn"] == "K77"
    assert pre["search_space_dim"] == "8_DISCRETE_SOURCE_CHANNELS_ZERO_FITTED_PARAMETERS"
    assert pre["free_object_delta"] == 0
    assert pre["residue_touched"] == [
        {"id": "K77-W2-ACTION-POLARIZATION-DOMAIN", "grade": "T4"}
    ]
    assert len(pre["preregistered_kills"]) == 6

    collision = registry["source_collision"]
    assert collision["shiab_inside_bosonic_action"] == "SOURCE_CONFIRMS"
    assert collision["preferred_historical_bianchi_selector"] == "SOURCE_CONFIRMS_MISSING"
    assert collision["multiple_time_ambient_domain"] == "SOURCE_IDENTIFIES_TECHNICAL_DEBT"
    assert collision["global_physical_domain"] == "SOURCE_SILENT"
    assert all(value == "DISTINCT" for value in registry["layer0"].values())

    block = registry["grade_one_channel_block"]
    assert block["input_dimension"] == 1274
    assert block["formal_labels"] == 8
    assert block["nonzero_restrictions"] == 8
    assert block["projective_restriction_classes"] == 8
    assert block["linear_span_rank"] == 5
    assert block["relation_count"] == 3
    assert len(block["relations"]) == 3
    assert block["full_grade_one_ranks"] == [1190, 1190, 1190, 1190, 14, 14, 374, 374]
    assert block["full_adjoint_span"] == "OPEN"

    action = registry["action_polarization"]
    assert action["all_eight_direct_derivatives_exact"] is True
    assert action["all_eight_polarized_hessians_symmetric"] is True
    assert action["helmholtz_selection_rank"] == 0
    assert action["channel_euler_row"] is False

    domain = registry["common_domain"]
    assert domain["field_domain"] == "H10_Y"
    assert domain["euler_codomain"] == "H9_Y"
    assert domain["field_value_trace"] == "H5_X"
    assert domain["field_first_jet_trace"] == "H4_X"
    assert domain["euler_value_trace"] == "H4_X"
    assert domain["channels_sharing_scale"] == 8
    assert domain["observation_is_green_boundary"] is False
    assert domain["actual_boundary_dimension"] == 13
    assert domain["observation_dimension"] == 4
    for key in (
        "arbitrary_y14_global_hypotheses",
        "closed_l2_realization",
        "krein_self_adjoint_extension",
        "hyperbolic_maximal_dissipative",
        "physical_bfv_phase_space",
    ):
        assert domain[key] == "OPEN"

    independent = registry["independent_sage"]
    assert independent == {
        "free_product_transform_rank": 8,
        "determinant": 4096,
        "planted_duplicate_rank": 7,
        "scope": "FORMAL_PRODUCT_BASIS_NOT_FULL_K77_MAP",
    }
    assert registry["accounting"] == {
        "fitted_selector_parameters": 0,
        "selection_constraints_from_action": 0,
        "selection_constraints_from_common_domain": 0,
        "new_fields": 0,
        "new_projectors": 0,
        "new_data": 0,
        "free_object_delta": 0,
        "p1_p2_p3_used": False,
        "phenomenological_constraint_surplus_claimed": False,
    }
    assert registry["probe_receipt"] == {
        "source": 7, "type": 18, "exact": 30, "planted": 8,
        "total": 63, "failures": 0,
    }
    assert registry["wave3_open"] is False
    assert registry["curt_status"] == "FORMALLY_SEPARATE_GUIDANCE_INSIDE_ERIC_LANE"
    assert registry["tg_promotion"] == "TG_1_AND_TG_2_AND_TG_3_NOT_PROMOTED"
    assert registry["claim_status_change"] is False
    assert registry["canon_verdict_change"] is False
    assert registry["public_posture_change"] is False

    wave2 = campaign["waves"][1]
    latest = wave2["latest_advance"]
    assert latest["named_gate"] == registry["named_gate"]
    assert latest["result_ref"] == (
        "explorations/k77-wave2-action-polarization-common-observation-domain-2026-08-05.md"
    )
    assert latest["next_required_build"] == registry["next_required_build"]
    for emitted in (
        "GRADE_ONE_CHANNEL_SPAN_RANK_FIVE",
        "THREE_EXACT_GRADE_ONE_CLIFFORD_HODGE_CHANNEL_RELATIONS",
        "EIGHT_PAIRWISE_NONPROPORTIONAL_GRADE_ONE_RESTRICTIONS",
        "ALL_EIGHT_FROZEN_ACTION_POLARIZATIONS_HELMHOLTZ",
        "ACTION_HELMHOLTZ_PRODUCT_SELECTION_RANK_ZERO",
        "CONDITIONAL_GLOBAL_H10_TO_H9_SOBOLEV_OBSERVATION_SCALE",
        "CODIMENSION_TEN_OBSERVATION_IS_NOT_GREEN_BOUNDARY",
        "INDEPENDENT_SAGE_FREE_PRODUCT_TRANSFORM_RANK_EIGHT",
    ):
        assert emitted in wave2["emitted"]
    assert campaign["frontier"]["next_required_build"] == registry["next_required_build"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["next_required_build"]

    for phrase in (
        "span only **five** linear directions",
        "grade-one restriction identities",
        "rank}_{\\rm helmholtz\\ selection}=0",
        "codimension ten",
        "not a green boundary",
        "conditional bounded-geometry sobolev scale",
        "full adjoint coefficient grades",
        "p1/p2/p3 remain unchanged and unused",
        "wave 3 remains closed",
    ):
        assert phrase in report

    for phrase in (
        "summary outruns the artifact",
        "rigor defends a superseded object",
        "complete grade-one restriction",
        "common sobolev scale",
        "interior trace",
        "pass_with_scope_repair",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-corrects",
        "source-silent",
        "codimension ten",
        "not a green boundary",
        "scalar action has a symmetric polarized hessian",
    ):
        assert phrase in source

    for phrase in (
        "grade1_channel_span_rank={grade1_channel_span_rank}",
        "three exact grade-one k77 clifford/hodge relations",
        "all eight frozen grade-one action-derived euler pairs",
        "helmholtz selection rank is zero",
        "observation section is not a green boundary",
        "shared sobolev scale is not a common closed l2 self-adjoint realization",
    ):
        assert phrase in probe

    for phrase in (
        "m.rank() == 8",
        "m.det() != 0",
        "m_bad.rank() == 7",
        "full k77 channel-map rank remains owned by the main probe",
    ):
        assert phrase in sage

    print("PASS: K77 action-polarization/common-observation-domain packet is exact and scope-fenced")


if __name__ == "__main__":
    main()
