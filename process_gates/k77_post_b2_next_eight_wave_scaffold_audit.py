#!/usr/bin/env python3
"""Fail-closed audit for the post-K77-B2 eight-wave rendezvous scaffold."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json"
REPORT = ROOT / "explorations/k77-post-b2-science-council-next-eight-wave-rendezvous-2026-08-04.md"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    report = REPORT.read_text(encoding="utf-8")

    assert registry["decision"] == "CONTINUE_WITH_REBASE_AND_RENDEZVOUS"
    route = registry["route_policy"]
    assert route["primary"] == "SOURCE_FAITHFUL_REAL_CL77_K77_CONSTRUCTION"
    assert route["rival"] == "ACTIVE_95_RIGHT_H_IMPLEMENTATION_AND_NEGATIVE_TEST_BANK"
    assert route["real_form_identification"].startswith("FORBIDDEN")
    assert route["k77_b3_role"] == "LAST_ISOLATED_SELECTOR_WAVE"

    evidence = registry["evidence_inputs"]
    assert evidence["k77_atomic_rows"] == {
        "total": 37,
        "exact_k77_fermion_carrier_support": 8,
        "exact_abstract_gauge_directions": 12,
        "physical_recovery_rows": 0,
    }
    assert evidence["orientation_datum"].startswith("D1_IS_TIMELIKE_LINE_ORIENTATION_COVER")

    assert len(registry["specialist_lenses"]) == 10
    assert len(set(registry["specialist_lenses"])) == 10
    assert registry["kill_policy"]["target_obligations_persist"] is True
    assert registry["kill_policy"]["external_datum_may_manufacture_missing_structure"] is False

    waves = registry["waves"]
    assert len(waves) == 8
    assert [wave["ordinal"] for wave in waves] == list(range(1, 9))
    ids = [wave["id"] for wave in waves]
    gates = [wave["named_gate"] for wave in waves]
    assert len(set(ids)) == len(ids)
    assert len(set(gates)) == len(gates)
    assert all(wave["constructs"] and wave["exit"] and wave["kill_scope"] for wave in waves)

    permitted_dependencies = set(ids) | {"MIDPOINT_BREADTH_RESET"}
    for wave in waves:
        assert set(wave["depends_on"]) <= permitted_dependencies
    assert waves[0]["depends_on"] == []
    assert waves[1]["depends_on"] == [waves[0]["id"]]
    assert "MIDPOINT_BREADTH_RESET" in waves[4]["depends_on"]

    assert "JD_JF_AND_COMPLETE_CONNECTION_VARIATION" in waves[1]["constructs"]
    assert "TIMELIKE_ORIENTATION_COVER_LIFT" in waves[2]["constructs"]
    assert "ATOMIC_LEDGER_REGRADE" in waves[3]["constructs"]
    assert "CLOSED_KREIN_COMPATIBLE_DOMAIN" in waves[4]["constructs"]
    assert "SEALED_PP3_DESI_TEST" in waves[5]["constructs"]
    assert "P3_COUPLING_TO_SAME_OPERATOR_DOMAIN" in waves[6]["constructs"]
    assert "HELDOUT_CONSTRAINT_SURPLUS" in waves[7]["constructs"]

    reset = registry["midpoint_reset"]
    assert reset["required"] is True and reset["after_wave"] == 4
    assert registry["ml_policy"]["standalone_wave"] is False
    assert registry["ml_policy"]["acceptance"].startswith("RATIONAL_RECONSTRUCTION")

    boundary = registry["status_boundary"]
    assert all(value is False for value in boundary.values())

    normalized_report = " ".join(report.lower().split())
    for token in (
        "CONTINUE K77 AS THE PRIMARY SOURCE-FAITHFUL (7,7) CONSTRUCTION",
        "MAKE K77-B3 THE LAST ISOLATED SELECTOR WAVE",
        "External data are late selectors, not repairs",
        "Mandatory midpoint breadth reset",
        "Wave 4 — local Einstein/Dirac/Yang-Mills/contorsion emission",
        "Wave 8 — frozen integrated acceptance tournament",
        "summary outruns artifact",
        "artifact answers a superseded object",
    ):
        assert token.lower() in normalized_report, f"missing report token: {token}"

    print("k77_post_b2_next_eight_wave_scaffold_audit: PASS")
    print("  route separation, eight named gates, datum boundary, early physics, midpoint reset, and exact-only acceptance retained")


if __name__ == "__main__":
    main()
