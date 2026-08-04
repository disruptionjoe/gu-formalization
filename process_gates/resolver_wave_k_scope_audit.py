#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave K."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "explorations/resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md"
DISPOSITION = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-k-conditional-active-shiab-b1-variation-disposition-2026-08-04.json"
PROBE = ROOT / "tests/channel-swings/resolver_wave_k_conditional_active_shiab_b1_variation_probe.py"


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


report = REPORT.read_text()
probe = PROBE.read_text()
with DISPOSITION.open() as handle:
    disposition = json.load(handle, object_pairs_hook=lambda pairs: _unique(pairs))


def _fail(message: str) -> None:
    raise AssertionError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        _fail(message)


def main() -> None:
    require(disposition["gate_after"] == "NORMALIZED_TRACE_FIXED_ACTIVE_95_QWEDGE_B1_CANDIDATE_MISMATCH", "wrong Wave-K grade")
    require(disposition["route_disposition"] == "REBASE", "Wave K must rebase")
    require(disposition["signature_ledger"]["source_total"] == [7, 7], "source 7,7 lost")
    require(disposition["signature_ledger"]["active_total"] == [9, 5], "active 9,5 lost")
    require(not disposition["signature_ledger"]["Hstar_flips_inertia"], "H-star may not flip inertia")
    require(disposition["layer_0"]["trace_selector"] == "NORMALIZED_DEWITT_E10", "normalized trace selector lost")
    require(disposition["layer_0"]["source_quadratic"] == "BRACKET_T_T_NORMALIZATION_OPEN", "source bracket fence lost")
    require(disposition["translation_gate"]["fixed_active_qwedge_candidate"] == "MISMATCH", "q-wedge mismatch lost")
    require(disposition["translation_gate"]["source_bracket_identity"].startswith("NOT_TESTED"), "source identity was overpromoted")
    require(not disposition["translation_gate"]["defect_zero"], "live defect erased")
    require(disposition["action"]["source_part_nonzero_at_kappa_zero"], "mass-only false positive returned")
    require(disposition["layer_0"]["strict_RJ_on_raw_shiab"] == "TYPE_REJECTED", "R_J domain fence lost")
    require(disposition["ward_green_port"]["selected_green_channel"].startswith("ZEROTH_ORDER"), "zero-boundary scope lost")
    require(disposition["ward_green_port"]["independent_Ward_theorem"] == "OPEN", "owner witness became Ward theorem")
    require(disposition["matter_route"]["primary_reconstruction"] == "SOURCE_TYPED_CL77", "source matter route lost")
    require(disposition["matter_route"]["atomic_physics_crosswalk"].startswith("REQUIRED"), "atomic crosswalk burden lost")
    require(disposition["layer_0"]["fundamental_chirality"] == "SOURCE_DENIES", "source nonchirality lost")
    require(disposition["matter_route"]["visible_chirality_burden"].startswith("DERIVE_EFFECTIVE"), "effective chiral burden lost")
    require(disposition["external_datum"] == {"P1": "unchanged_unused", "P2": "unchanged_unused", "P3": "unchanged_unused"}, "external datum moved")
    require(not disposition["third_lane_promoted"], "third lane promoted")
    require("K77-A" in report and "atomic physics crosswalk" in report.lower(), "K77 atomic next gate missing")
    require("transgression_defect != 0" in probe, "probe no longer asserts the obstruction")
    require("TRACE_INDEX = 10" in probe, "probe no longer uses the normalized trace")
    require("strict_rj_rejected" in probe, "probe no longer rejects the invalid R_J shortcut")
    print("PASS: Resolver Wave K scope audit")


if __name__ == "__main__":
    main()
