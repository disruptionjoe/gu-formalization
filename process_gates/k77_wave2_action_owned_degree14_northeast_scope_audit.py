#!/usr/bin/env python3
"""Fail-closed scope audit for the K77 action-degree14/northeast packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-wave2-action-owned-degree14-northeast-totalization.json"
CAMPAIGN = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-05-k77-wave2-action-owned-degree14-northeast-totalization-review.md"
SOURCE = ROOT / "lab/sources/gu-action-owned-degree14-northeast-source-reinspection-2026-08-05.md"
PROBE = ROOT / "tests/channel-swings/k77_wave2_action_owned_degree14_northeast_probe.py"
SAGE = ROOT / "tests/channel-swings/k77_wave2_action_owned_degree14_northeast_independent.sage"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def normalized(path):
    return " ".join(path.read_text().lower().split())


def main():
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    report = normalized(REPORT)
    review = normalized(REVIEW)
    source = normalized(SOURCE)
    probe = normalized(PROBE)
    sage = normalized(SAGE)

    assert registry["artifact"] == "K77_WAVE2_ACTION_OWNED_DEGREE14_NORTHEAST_TOTALIZATION"
    assert registry["lane"] == "1"
    assert registry["fork"] == "SIGNATURE_AMBIENT_7_7"
    assert registry["gate_before"] == "K77_ACTION_OWNED_SELECTED_SHIAB_EULER_AND_DEGREE14_TOTALIZATION_WITH_RAW_NORTHEAST_OWNER"
    assert registry["gate_after"] == "K77_FULL_ODD_CLIFFORD_ACTION_CLOSURE_AND_SOURCE_NATURAL_DEGREE3_SHIAB_NORTHEAST_NOETHER_RENDEZVOUS"

    source_disposition = registry["source_disposition"]
    assert source_disposition["degree3_to_degree14_arena"] == "SOURCE_CONFIRMS"
    assert source_disposition["adjoint_shiab"] == "SOURCE_CONFIRMS"
    assert source_disposition["degree3_selector"] == "SOURCE_SILENT"
    assert source_disposition["cyclic_two_connection_square"] == "SOURCE_UNRELEASED"
    assert source_disposition["direct_JD_plus_JF_owner"].startswith("REPO_KILLS")

    assert registry["layer0"]["status"] == "PASS"
    assert all(value == "DISTINCT" for key, value in registry["layer0"].items() if key != "status")

    selected = registry["selected_degree2_shiab"]
    assert selected["products"] == ["comm", "symi", "symi"]
    assert selected["domain_dimension"] == selected["nonzero_columns"] == 8281
    assert selected["support_entries"] == 63336
    assert selected["output_coordinates"] == 10206
    assert (selected["total_rank"], selected["cl1_rank"], selected["cl5_rank"]) == (1197, 196, 1001)
    assert selected["einstein_only_receiver_closed_on_generic_carrier"] is False

    adjoint = registry["formal_adjoint"]
    assert adjoint["entrywise_identities"] == 63336
    assert adjoint["rank"] == 1197
    assert adjoint["grade"] == "FINITE_FORMAL_BILINEAR"
    assert adjoint["positive_closed_analytic_Krein_adjoint"] == "OPEN"

    noether = registry["action_degree14"]
    assert noether["owner"] == "FULL_EVEN_NOETHER_TOTALIZATION"
    assert noether["D_B_E_act_alone"] == "INSUFFICIENT"
    assert noether["Xi_equals_D_Upsilon"] == "DISTINCT_SOURCE_REDUNDANCY"
    assert noether["native_global_Ward_BV_closure"] == "OPEN"

    northeast = registry["raw_northeast"]
    assert northeast["total_rank"] == 8281
    assert (northeast["cl1_rank"], northeast["cl3_rank"]) == (5096, 8281)
    assert all(rank == 91 for rank in northeast["principal_Riemann_rank_by_orbit"].values())
    assert northeast["injective"] is True
    assert northeast["direct_JD_plus_JF_owner"] == "KILLED"

    degree3 = registry["minimal_degree3_shiab"]
    assert degree3["generic_raw_image_rank"] == {"comm": 1092, "symi": 1093}
    assert all(row == {"comm": 0, "symi": 1} for row in degree3["principal_Riemann_rank_by_orbit"].values())
    assert degree3["fixture_response"]["traceless_Ricci"] == {"comm": 0, "symi": 0}
    assert degree3["universal_Einstein_stress_energy_owner"] == "KILLED"
    assert degree3["all_source_natural_degree3_Shiabs"] == "OPEN"

    assert registry["checks"]["main"] == "8 source + 13 type + 15 exact + 10 planted = 46 PASS"
    assert registry["checks"]["machine_learning"].startswith("NOT_WARRANTED")
    assert registry["p1_p2_p3_changed"] is False
    assert registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert registry["third_lane_status"] == "NOT_PROMOTED"

    wave2 = campaign["waves"][1]
    latest = wave2["latest_advance"]
    assert latest["named_gate"] == registry["gate_before"]
    assert latest["result_ref"] == "explorations/k77-wave2-action-owned-degree14-northeast-totalization-2026-08-05.md"
    assert latest["next_required_build"] == registry["gate_after"]
    assert campaign["frontier"]["next_required_build"] == registry["gate_after"]
    assert campaign["frontier"]["latest"]["next_required_build"] == registry["gate_after"]
    assert campaign["frontier"]["next_wave"] == 2

    for phrase in (
        "rank-1001 `cl^5` sector",
        "full even noether totalization",
        "raw northeast is proved injective",
        "cannot universally own this block",
        "erases traceless ricci",
        "candidate-map kill, not an ultimate gu kill",
    ):
        assert phrase in report

    for phrase in (
        "summary outruns artifact",
        "artifact defends superseded object",
        "`cl5` is not a nuisance term",
        "formal adjoint is not yet the krein/riesz object",
        "partial gate movement only",
    ):
        assert phrase in review

    for phrase in (
        "source-confirms",
        "source-silent",
        "source-confirms-missing",
        "source-corrects",
        "does not permit attribution",
    ):
        assert phrase in source

    for phrase in (
        "selected_shiab_rank=1197",
        "selected_shiab_cl1_cl5_ranks=196_1001",
        "formal_adjoint=63336_entrywise_identities",
        "raw_northeast_rank=8281_injective",
        "minimal_degree3_riemann_ranks=comm_0_symi_1",
        "failures=0",
    ):
        assert phrase in probe

    for phrase in (
        "assert raw_matrix.rank() == 8281",
        "assert (raw_bank_matrix.rank(), comm_matrix.rank(), symi_matrix.rank()) == (91, 0, 1)",
        "quadraticfield(-1",
        "entry_checks",
        "gaussian-rational selected-shiab adjoint slice",
    ):
        assert phrase in sage

    process_count = sum(path.suffix == ".py" for path in (ROOT / "process_gates").iterdir())
    channel_python = sum(path.suffix == ".py" for path in (ROOT / "tests/channel-swings").iterdir())
    channel_sage = sum(path.suffix == ".sage" for path in (ROOT / "tests/channel-swings").iterdir())
    tests_readme = normalized(ROOT / "tests/README.md")
    assert process_count == 155
    assert channel_python == 187 and channel_sage == 5
    assert "channel-swings/` (187 python + 5 sage)" in tests_readme

    print("PASS: K77 action-degree14/northeast packet is exact, source-collided and fail-closed")


if __name__ == "__main__":
    main()
