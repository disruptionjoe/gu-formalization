#!/usr/bin/env python3
"""Propagation probe for agenda latest-result currency reconciliation."""

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-agenda-latest-result-currency.json"
LIVE_REGISTRY = ROOT / "lab/process/current-frontier-semantic-currency.json"
ARTIFACT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-agenda-latest-result-currency-2026-08-23.md"
CURRENT_STATE = ROOT / "CURRENT-STATE.yaml"

checks = 0


def check(label, condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def validate_historical(registry, artifact):
    delta = registry["source_to_proof_delta"]
    rec = registry["reconciliation"]
    check("source delta unchanged", delta["movement"] == "unchanged")
    check("historical registry date pinned", rec["agenda_updated_at"] == "2026-08-23")
    check("registry exposes no gate", rec["new_execution_gate"] is None)
    check("no verdict movement", registry["effect"]["scientific_verdict_change"] == "none")
    check("artifact states exact defect", "root agenda still declared" in artifact and "releasing L7" in artifact)
    check("artifact records hostile review", "## Hostile review and ceiling" in artifact)


def validate_current(agenda, live_registry):
    items = {item["id"]: item for item in agenda["work_items"]}
    lead = items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]
    b5 = items["B5-INDEPENDENT-RECONSTRUCTION"]
    check("agenda has superseded historical snapshot", agenda["updated_at"] == "2026-08-25")
    check("CBRS current root is empty", "current named root-candidate set is empty" in lead["current_authority"])
    check("CBRS current result is W154 nonadmission", "W154/W229 is nonadmitted" in lead["latest_result"])
    check("CBRS live route is non-B2 rebuild", "strongest disjoint non-B2 native gate" in lead["next_swing"])
    check("B5 completed RB6/Wave One", "RB6 recertification and the full-20 Gram-adjoint wave completed" in b5["latest_result"])
    check("B5 stale Step 0 retired", not b5["next_swing"].startswith("Step 0: recertify"))
    check("B5 exact reopener current", live_registry["b5_agenda_currency"]["live_reopener"] in b5["next_swing"])
    check("B5 graph-mixing ceiling current", "EXTERNAL-VIA-GRAM" in b5["latest_result"])


def main():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    live_registry = json.loads(LIVE_REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    validate_historical(registry, artifact)
    validate_current(agenda, live_registry)
    current_state = CURRENT_STATE.read_text(encoding="utf-8")
    current_state_normalized = " ".join(current_state.split())
    check("current-state removes stale fallback", "Do not execute L7, L8, L9, T3 or either L10 reconciliation as a newly released" in current_state_normalized)
    print(f"conditional_build_frontier_agenda_latest_result_currency_probe: {checks}/{checks} checks pass, exit 0")


def selftest():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    live_registry = json.loads(LIVE_REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    controls = (
        "stale agenda date",
        "stale B5 step",
        "new gate invented",
        "source delta moved",
        "B5 ceiling erased",
    )
    caught = 0
    for label in controls:
        a = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
        r = json.loads(REGISTRY.read_text(encoding="utf-8"))
        lr = json.loads(LIVE_REGISTRY.read_text(encoding="utf-8"))
        t = artifact
        b5 = next(
            (item for item in a["work_items"] if item["id"] == "B5-INDEPENDENT-RECONSTRUCTION"),
            {},
        )
        if label == "stale agenda date":
            a["updated_at"] = "2026-08-23"
        elif label == "stale B5 step":
            b5["next_swing"] = "Step 0: recertify the remaining RB6 null with exact derivatives."
        elif label == "new gate invented":
            r["reconciliation"]["new_execution_gate"] = "L11"
        elif label == "source delta moved":
            r["source_to_proof_delta"]["movement"] = "advanced"
        elif label == "B5 ceiling erased":
            b5["latest_result"] = b5["latest_result"].replace("EXTERNAL-VIA-GRAM", "SELECTED")
        try:
            validate_historical(r, t)
            validate_current(a, lr)
        except AssertionError:
            caught += 1
    check("all planted controls caught", caught == len(controls))
    print(f"SELF-TEST GREEN: {caught}/{len(controls)} planted regressions caught")


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
