#!/usr/bin/env python3
"""Fail-closed scope audit for the hostile-reviewed Resolver Wave A packet.

This gate checks disposition and prose boundaries.  It does not validate the
mathematics performed by the Wave-A probes and moves no scientific status.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "explorations/cycle-gates-and-audits/resolver-wave-a-rebase-2026-08-03.json"
A1 = ROOT / "explorations/chirality-grading-and-77-rerun-2026-08-03.md"
A2 = ROOT / "explorations/de-pipeline-certification-and-bridge-test-2026-08-03.md"
DE12 = ROOT / "tests/de-certification/de12_theta_star_positive_control.py"
W230 = ROOT / "tests/de-certification/w230_ckin_flrw_mapping_check.py"


def require(text: str, needle: str, where: Path) -> None:
    assert needle in text, f"{where}: missing required scope token {needle!r}"


def forbid(text: str, needle: str, where: Path) -> None:
    assert needle not in text, f"{where}: forbidden overclaim survives: {needle!r}"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert data["named_gate"] == "RESOLVER-WAVE-A"
    assert data["gate_after"] == "REBASE_REQUIRED"
    assert data["route_disposition"] == "REBASE"
    assert data["subwaves"]["A1"]["status"] == "COMPLETED_WITH_CORRECTIONS"
    assert data["subwaves"]["A2"]["status"] == "OPEN_REBASE_REQUIRED"
    assert data["subwaves"]["A3"]["commit"] == "b327ad6"
    assert data["next_gate"]["id"] == "RESOLVER-WAVE-B"

    a1 = A1.read_text(encoding="utf-8")
    a2 = A2.read_text(encoding="utf-8")
    de12 = DE12.read_text(encoding="utf-8")
    w230 = W230.read_text(encoding="utf-8")

    for token in ("PH-K1-KINEMATIC", "PH-K1-PHYSICAL", "actual `(7,7)` stabilizer"):
        require(a1, token, A1)
    for token in ("in-sample", "proxy", "W230-NATIVE-BRIDGE = OPEN/BLOCKED"):
        require(a2, token, A2)
    forbid(de12, "pipeline UNBIASED; C10 certified", DE12)
    forbid(w230, "Bridge FAILS AS STATED", W230)
    forbid(w230, "M-H13 NO-GO", W230)

    print("resolver_wave_a_scope_audit: PASS")
    print("  disposition REBASE; A1 kinematic only; A2 proxy/native-map open; A3 absorbed")


if __name__ == "__main__":
    main()
