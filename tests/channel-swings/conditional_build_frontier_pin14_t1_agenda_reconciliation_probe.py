#!/usr/bin/env python3
"""Propagation probe for the Pin+ T1 agenda reconciliation."""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
AGENDA = ROOT / "lab/process/RESEARCH-AGENDA.json"
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-pin14-t1-agenda-reconciliation.json"
ARTIFACT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-pin14-t1-agenda-reconciliation-2026-08-23.md"
PIN_GATE = ROOT / "tests/channel-swings/pin14_smith_degree_gate.py"
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
    item = items["ANOMALY-DESCENT-HARDENING"]
    check("ambient T1 no longer active", item["state"] == "BLOCKED_SOURCE_GAP")
    check("stale hourly pointer removed", "hourly-eligible" not in item["next_swing"])
    check("stale in-progress pointer removed", "shot in progress" not in item["next_swing"])
    check("ambient computation complete", "ambient T1 computation" in item["next_swing"])
    check("class realization stays separate", "OPERATOR-END-PENCIL" in item["next_swing"])
    check("T3 dependency preserved", "B5-INDEPENDENT-RECONSTRUCTION" in item["next_swing"] and "SRC-COH-1" in item["next_swing"])
    check("T2 remains closed", "T2 stays closed" in item["next_swing"])
    check("ambient and GU class distinguished", "does NOT realize GU's proposed class" in item["current_authority"])
    check("forced observable count remains zero", "forced-observable count remains ZERO" in item["current_authority"])

    rec = registry["reconciliation"]
    check("registry closes ambient T1", rec["ambient_t1"] == "COMPLETE_INTERNAL_DERIVATION_GRADE")
    check("registry leaves class open", rec["gu_class_realization"] == "OPEN_OPERATOR_END_PENCIL")
    check("registry leaves T3 blocked", rec["t3"] == "BLOCKED_ON_B5_SRC_COH_1")
    check("registry preserves zero observables", rec["forced_observable_count"] == 0)
    check("source delta unchanged", registry["source_to_proof_delta"]["movement"] == "unchanged")
    check("no verdict movement", registry["effect"]["scientific_verdict_change"] == "none")
    check("artifact names no new topology", "No topology was newly computed" in artifact)
    check("artifact preserves class ceiling", "nonzero ambient `Z/2` group neither supplies" in " ".join(artifact.split()))
    check("artifact records hostile review", "## Hostile review and ceiling" in artifact)


def main():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    validate(agenda, registry, artifact)
    current_state = CURRENT_STATE.read_text(encoding="utf-8")
    next_steps = NEXT_STEPS.read_text(encoding="utf-8-sig")
    check("current-state basis is starting revision", "revision_basis: 770bafb142c26c5a68b764c92245c7fad218f584" in current_state)
    check("current-state preserves open class map", "That map remains open" in current_state and "OPERATOR-END-PENCIL" in current_state)
    check("contributor front door removes duplicate work", "Do not rerun it" in next_steps and "T3 remains blocked" in next_steps)
    gate = subprocess.run([sys.executable, str(PIN_GATE)], cwd=ROOT, text=True,
                          capture_output=True, check=False)
    check("existing Pin derivation gate passes", gate.returncode == 0 and "PIN14-EXACT-Z2" in gate.stdout)
    print(f"conditional_build_frontier_pin14_t1_agenda_reconciliation_probe: {checks}/{checks} checks pass, exit 0")


def selftest():
    agenda = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    artifact = ARTIFACT.read_text(encoding="utf-8")
    validate(agenda, registry, artifact)
    controls = (
        "stale T1 pointer",
        "class realization falsely closed",
        "T3 dependency erased",
        "forced observable invented",
        "new-topology overclaim",
    )
    caught = 0
    for label in controls:
        a = json.loads(AGENDA.read_text(encoding="utf-8-sig"))
        r = json.loads(REGISTRY.read_text(encoding="utf-8"))
        t = artifact
        item = next(item for item in a["work_items"] if item["id"] == "ANOMALY-DESCENT-HARDENING")
        if label == "stale T1 pointer":
            item["next_swing"] = "T1 hourly-eligible now, shot in progress"
        elif label == "class realization falsely closed":
            r["reconciliation"]["gu_class_realization"] = "COMPLETE"
        elif label == "T3 dependency erased":
            item["next_swing"] = "T3 execute now; T2 stays closed"
        elif label == "forced observable invented":
            r["reconciliation"]["forced_observable_count"] = 4
        elif label == "new-topology overclaim":
            t = t.replace("No topology was newly computed", "Topology newly computed")
        try:
            validate(a, r, t)
        except AssertionError:
            caught += 1
    check("all planted controls caught", caught == len(controls))
    print(f"SELF-TEST GREEN: {caught}/{len(controls)} planted regressions caught")


if __name__ == "__main__":
    selftest() if "--selftest" in sys.argv else main()
