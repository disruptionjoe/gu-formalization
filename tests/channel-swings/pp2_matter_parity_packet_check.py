#!/usr/bin/env python
"""Validate the PP2 matter-parity prediction packet boundary.

This is a lightweight repository-local check. It does not validate the
underlying group theory, which is covered by ch_sm_chain_sweep.py and
bb_p4_generation_doors_probe.py. It verifies that the frozen packet carries
the standing-rule fields and keeps the no-claim/no-external boundary explicit.

Run:
    python tests/channel-swings/pp2_matter_parity_packet_check.py
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "explorations" / "prediction-package-pp2-matter-parity-stable-state-2026-07-19.md"

REQUIRED_SNIPPETS = {
    "package id": "package_id: PP2",
    "frozen status": "package_status: FROZEN_CONDITIONAL_EVENT_CLASS",
    "claim boundary": "claim_status_change: none",
    "canon boundary": "canon_verdict_change: none",
    "public boundary": "public_posture_change: none",
    "external boundary": "external_action: none",
    "prediction section": "## Frozen Prediction",
    "condition chain": "## Condition Chain",
    "competitor baseline": "## Competitor Baseline",
    "kill thresholds": "## Kill Thresholds",
    "non claims": "## Non-Claims",
    "receipts": "## Receipts",
    "matter parity formula": "P_M = (-1)^(3(B-L))",
    "conditional 126 route": "conditional on the 126 route",
    "not mass claim": "Not a claim that GU predicts a dark-matter mass.",
    "no detection kill": "Absence of a current detection does not kill PP2",
}

FORBIDDEN_SNIPPETS = {
    "external authorization": "external_action: authorized",
    "canon movement": "canon_verdict_change: moved",
    "claim movement": "claim_status_change: moved",
    "public posture movement": "public_posture_change: moved",
    "mass predicted": "package_status: FROZEN_QUANTITATIVE_MASS",
    "selected 126": "the 126 route is selected unconditionally",
}


def main() -> None:
    text = PACKET.read_text(encoding="utf-8")
    failures: list[str] = []

    for label, snippet in REQUIRED_SNIPPETS.items():
        if snippet not in text:
            failures.append(f"missing required snippet: {label}")

    for label, snippet in FORBIDDEN_SNIPPETS.items():
        if snippet in text:
            failures.append(f"forbidden snippet present: {label}")

    if failures:
        print("PP2 packet validation failed:")
        for failure in failures:
            print(f"  - {failure}")
        raise SystemExit(1)

    print("PASS :: PP2 matter-parity packet carries standing-rule fields")
    print("PASS :: no claim/canon/public/external movement declared")
    print("PASS :: conditional 126 route, event-class grade, and kill thresholds are explicit")


if __name__ == "__main__":
    main()
