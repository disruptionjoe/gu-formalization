#!/usr/bin/env python3
"""Fail-closed scope audit for the R2B2B2H4 source/active port decision."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "lab/process/pw2fr2b2b2h4-source-active-real-form-scope-exit-registry.json"
REPORT = ROOT / "explorations/pw2fr2b2b2h4-source-active-real-form-scope-exit-2026-08-04.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")

    assert data["status"] == "PUBLIC_SOURCE_TO_ACTIVE_REAL_FORM_PORT_EVIDENCE_SCOPE_EXIT__INDEPENDENT_MOVING_J_PORT_OPEN__SEPARATE_CONDITIONAL_ACTIVE_BANKS_ADMITTED"
    cert = data["exact_real_form_certificate"]
    assert cert["source_inertia"] == [7, 7]
    assert cert["active_inertia"] == [9, 5]
    assert cert["real_reality_intertwiner"] == "ZERO_ONLY"
    assert cert["common_complexification"] == "M128C"
    obligations = data["global_port_obligations"]
    assert obligations["published_source_evaluability"].startswith("NOT_EVALUABLE")
    assert obligations["independent_native_status"] == "RECONSTRUCTION_OPEN_NOT_DISPROVED"
    assert obligations["global_nonexistence"] == "NOT_CLAIMED"
    admission = data["admission"]
    assert admission["source_attributed_global_real_form_port"] == "EVIDENCE_SCOPE_EXIT"
    assert admission["complete_I1_A4"].endswith("NOT_ASSEMBLED")
    assert admission["complete_I2B_C4"].endswith("NOT_ASSEMBLED")
    assert admission["bank_identity"].startswith("FORBIDDEN")
    assert admission["projective_kappa1"] == "NOT_RUN"
    assert data["external_datum"] == "P1_P2_P3_UNCHANGED_AND_UNUSED"
    assert data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE"
    assert data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED"

    for token in (
        "PUBLIC_SOURCE_TO_ACTIVE_REAL_FORM_PORT_EVIDENCE_SCOPE_EXIT",
        "INDEPENDENT_MOVING_J_PORT_OPEN",
        "not `GLOBAL_PORT_NONEXISTENT`",
        "Neither bank is source-derived",
        "P1/P2/P3 remain unchanged and unused",
        "FORMALLY_SEPARATE_INSIDE_ERIC_LANE",
        "TG-1 AND TG-2 AND TG-3",
    ):
        assert token in report, token

    for forbidden in (
        "global port nonexistent",
        "global moving-j reduction is impossible",
        "complete i1 a4 bank passes",
        "complete i2b c4 bank passes",
        "kappa1 is selected",
        "third lane promoted",
        "physics verdict proved",
    ):
        assert forbidden not in report.lower(), forbidden

    print("pw2fr2b2b2h4_source_active_real_form_scope_exit_scope_audit: PASS")
    print("  source-scope exit, open moving-J construction, and separate-bank boundary retained")


if __name__ == "__main__":
    main()
