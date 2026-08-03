#!/usr/bin/env python3
"""Fail-closed scope audit for Resolver Wave B.

This checks the disposition and anti-conflation boundaries. It does not prove
the mathematics in the three direct certificates and moves no scientific bar.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-b-disposition-2026-08-03.json"
REPORT = ROOT / "explorations/resolver-wave-b-q3-dq3-dq1-2026-08-03.md"
WAVE_A = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-a-rebase-2026-08-03.md"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    report = REPORT.read_text(encoding="utf-8")
    wave_a = WAVE_A.read_text(encoding="utf-8")
    assert data["named_gate"] == "RESOLVER-WAVE-B"
    assert data["gate_after"] == "REBASE_REQUIRED"
    assert data["route_disposition"] == "REBASE"
    assert data["subwaves"]["Q3"]["projector"] == "P_hinge_internal_rank_128"
    assert data["subwaves"]["Q3"]["external_P3_used"] is False
    assert data["subwaves"]["DQ3"]["inertia"] == [832, 832]
    assert data["subwaves"]["DQ1"]["residual_dimension_R"] == 12
    assert data["subwaves"]["DQ1"]["analytic_classification_status"].startswith("EXACT_CONDITIONAL")
    assert data["assertion_counts"] == {
        "Q3": 584,
        "DQ3": 103,
        "DQ1_base": 21,
        "DQ1_sage": 12,
        "total": 720,
    }
    assert data["external_datum"]["P3"] == "unchanged_unused"
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-C-REBASED"
    for token in ("P_hinge", "external `P3`", "finite kinematic", "P1/P2/P3 remain unchanged and unused"):
        assert token in report, f"report missing scope token {token!r}"
    assert "`P_hinge`" in wave_a and "distinct external count/relative-KO datum `P3`" in wave_a
    assert "actual commutator `[sigma(D_RS), P3]`" not in wave_a
    print("resolver_wave_b_scope_audit: PASS")
    print("  Q3 internal projector separated from external P3; finite kinematic fences retained")


if __name__ == "__main__":
    main()
