#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave K77-B3."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction.json"
REPORT = ROOT / "explorations/resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-04-resolver-wave-k77b3-review.md"
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


def main() -> None:
    registry = load_json(REGISTRY)
    campaign = load_json(CAMPAIGN)
    report = " ".join(REPORT.read_text(encoding="utf-8").lower().split())
    review = " ".join(REVIEW.read_text(encoding="utf-8").lower().split())

    assert registry["named_gate"] == "RESOLVER-WAVE-K77-B3-FULL-DOMAIN-EXTENSION-CYCLIC-EULER-EXISTENCE-AND-GREEN"
    assert registry["gate_status"] == "COMPLETED_WITH_ZERO_ORDER_LINEAR_MECHANISM_KILL"
    assert registry["verdict"] == "ZERO_ORDER_LINEAR_FULL_DOMAIN_EINSTEIN_CYCLIC_INTERSECTION_ZERO"
    assert registry["reconstruction_return"] == "DERIVATIVE_OR_MOVING_FIELD_ACTION"

    hom = registry["equivariant_hom"]
    assert hom["complexified_full_dimension"] == 200
    assert hom["grade2_to_low_dimension"] == hom["grade2_to_high_dimension"] == 3
    assert hom["riemann_to_low_dimension"] == hom["riemann_to_high_dimension"] == 2
    assert hom["all_91_generator_fixture_checks"] == "PASS"
    assert hom["six_maps_exhaust_full_hom"] is False

    witnesses = registry["kernel_witnesses"]
    assert witnesses["low"]["Q_b_c"] == witnesses["high"]["Q_b_c"] == "ZERO"
    assert witnesses["low"]["endpoint_pairing"] == -16896
    assert witnesses["low"]["defect"] == 11264
    assert witnesses["high"]["endpoint_pairing"] == 19968
    assert witnesses["high"]["defect"] == -13312
    assert witnesses["joint_ideal"] == ["p_LOW", "q_HIGH"]
    assert witnesses["nonzero_survivors"] == 0

    assert registry["layer0"]["observed_einstein"] == "OPEN_AND_NOT_IDENTIFIED"
    assert registry["layer0"]["frobenius_fibre_trace_reversal"] == "OPEN_AND_DISTINCT"
    assert registry["layer0"]["green_domain"] == "NOT_REACHED"
    assert registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"}
    assert registry["physics_status_change"] is False
    assert all(value is False for value in registry["status_boundary"].values())

    wave1 = campaign["waves"][0]
    wave2 = campaign["waves"][1]
    assert wave1["id"] == "K77_B3_FULL_DOMAIN_SHIAB_CYCLIC_ACTION"
    assert wave1["status"] == "COMPLETED_WITH_ZERO_ORDER_LINEAR_MECHANISM_KILL"
    assert wave1["result_ref"].endswith("resolver-wave-k77b3-full-domain-cyclic-kernel-obstruction-2026-08-04.md")
    assert "DERIVATIVE_OR_MOVING_FIELD_ACTION" in wave1["emitted_return"]
    assert wave2["id"] == "RENDEZVOUS_ACTION_CURRENT_RIESZ_SUPERIG_WARD"
    assert "DERIVATIVE_OR_MOVING_FIELD_BOSONIC_REPLACEMENT" in wave2["constructs"]
    assert campaign["frontier"]["next_wave"] == 2
    assert campaign["frontier"]["next_named_gate"] == "RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD"

    for token in (
        "zero_order_linear_full_domain_ambient_einstein_plus_same_endpoint_mechanism_kill",
        "p = 0 q = 0",
        "green/domain is `not_reached`",
        "actual-euler route",
        "moving-shiab route",
        "external datum is not an eligible repair",
    ):
        assert token in report, f"missing report token: {token}"
    for token in (
        "pass_with_material_scope_repairs",
        "source-normalized one-third quadratic",
        "artifact would defend a superseded object",
        "does not kill k77",
    ):
        assert token in review, f"missing review token: {token}"

    print("resolver_wave_k77b3_scope_audit: PASS")
    print("  full-domain linear mechanism kill, derivative return, source/domain caveat, and status boundaries retained")


if __name__ == "__main__":
    main()
