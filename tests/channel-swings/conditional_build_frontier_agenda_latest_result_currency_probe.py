#!/usr/bin/env python3
"""Propagation probe for agenda latest-result currency reconciliation."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-agenda-latest-result-currency.json"
ARTIFACT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-agenda-latest-result-currency-2026-08-23.md"
CURRENT_STATE = ROOT / "CURRENT-STATE.yaml"
NEXT_STEPS = ROOT / "NEXT-STEPS.md"

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def validate(agenda, registry, artifact):
    items = {item["id"]: item for item in agenda["work_items"]}
    lead = items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]
    latest = lead["latest_result"]
    check("agenda date is current", agenda["updated_at"] == "2026-08-23")
    check("latest result names post-Pin frontier", "post-Pin+ T1 substantial-frontier rebuild" in latest)
    check("completed fallback sequence recorded", all(token in latest for token in ("L7", "L8", "L9", "T3", "both L10")))
    check("L7 is not newly released", "released the strongest independent executable gate, PROOF-STABLE-KERNELS L7" not in latest)
    check("no new execution gate", "none is a newly released execution gate" in latest)
    check("CBRS boundaries preserved", "CBRS-1 remains parked" in latest and "CBRS-2 remains blocked" in latest)
    check("class and T3 boundaries preserved", "OPERATOR-END-PENCIL" in latest and "B5/SRC-COH-1" in latest)
    check("lead still requires frontier rebuild", "rebuild the substantial frontier next" in lead["next_swing"])

    delta = registry["source_to_proof_delta"]
    rec = registry["reconciliation"]
    check("source delta unchanged", delta["movement"] == "unchanged")
    check("registry date current", rec["agenda_updated_at"] == "2026-08-23")
    check("registry exposes no gate", rec["new_execution_gate"] is None)
    check("no verdict movement", registry["effect"]["scientific_verdict_change"] == "none")
    check("artifact states exact defect", "root agenda still declared" in artifact and "releasing L7" in artifact)
    check("artifact records hostile review", "## Hostile review and ceiling" in artifact)


def main():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    validate(agenda, registry, artifact)
    current_state = CURRENT_STATE.read_text(encoding="utf-8")
    next_steps = NEXT_STEPS.read_text(encoding="utf-8-sig")
    current_state_normalized = " ".join(current_state.split())
    check("current-state basis is starting revision", "revision_basis: 622e04661231648640f02f1f7f67e0425f7d3f12" in current_state)
    check("current-state removes stale fallback", "Do not execute L7, L8, L9, T3 or either L10 reconciliation as a newly released" in current_state_normalized)
    check("contributor front door removes duplicate work", "Do not execute any of those gates as newly released work" in next_steps)
    print(f"conditional_build_frontier_agenda_latest_result_currency_probe: {checks}/{checks} checks pass, exit 0")


def selftest():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    validate(agenda, registry, artifact)
    controls = (
        "stale date",
        "stale L7 release",
        "new gate invented",
        "source delta moved",
        "T3 boundary erased",
    )
    caught = 0
    for label in controls:
        a = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
        r = json.loads(REGISTRY.read_text(encoding="utf-8"))
        t = artifact
        lead = next(item for item in a["work_items"] if item["id"] == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD")
        if label == "stale date":
            a["updated_at"] = "2026-08-22"
        elif label == "stale L7 release":
            lead["latest_result"] = "released the strongest independent executable gate, PROOF-STABLE-KERNELS L7"
        elif label == "new gate invented":
            r["reconciliation"]["new_execution_gate"] = "L11"
        elif label == "source delta moved":
            r["source_to_proof_delta"]["movement"] = "advanced"
        elif label == "T3 boundary erased":
            lead["latest_result"] = lead["latest_result"].replace("B5/SRC-COH-1", "complete")
        try:
            validate(a, r, t)
        except AssertionError:
            caught += 1
    check("all planted controls caught", caught == len(controls))
    print(f"SELF-TEST GREEN: {caught}/{len(controls)} planted regressions caught")


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
