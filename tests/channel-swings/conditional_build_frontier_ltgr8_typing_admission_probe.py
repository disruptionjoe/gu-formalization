#!/usr/bin/env python3
"""Propagation and failure-path probe for the LT-GR8 typing-arc frontier admission."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-ltgr8-typing-admission.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-ltgr8-typing-admission-2026-08-22.md"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.260.json"

DELTA_TEMPLATE = (
    "primary source claim -> native carrier/action/reduction/observable "
    "-> current certificate -> exact missing bridge -> evidence that would reopen it"
)

FORBIDDEN_SUMMARY_GRAMMAR = (
    "confirms Jacobson",
    "GU predicts the Einstein equation",
    "prediction credit is awarded",
)


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "ledger": json.loads(LEDGER.read_text()),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
        "agenda": json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    data = inputs["data"]
    ledger = inputs["ledger"]
    agenda = inputs["agenda"]
    result = inputs["result"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    assert isinstance(data, dict) and isinstance(ledger, dict) and isinstance(agenda, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)

    check(data["schema_version"] == "1.0", "schema")
    check(data["registered_cbrs1_admissible_candidate_count"] == 0, "empty admitted set")
    check(data["cbrs1_state"] == "PARKED_UNTIL_COMPLETE_NEW_OWNER_PACKET", "CBRS-1 parked")
    check("LOCAL_SOLUTION" in data["cbrs2_state"], "CBRS-2 dependency")
    check(len(data["frontier"]) == 7, "seven-arc frontier")
    check(data["frontier"][0]["id"] == "LTGR8_TYPING", "LT-GR8 arc first")
    check(data["frontier"][0]["disposition"] == "EXECUTABLE_SELECTED", "LT-GR8 selected")
    check("NO_CBRS2_ADVANCE" in data["frontier"][0]["scope"], "typing scope excludes CBRS-2")
    check(data["ltgr8_admission"]["ledger_row"] == "LT-GR8", "ledger row named")
    check(data["ltgr8_admission"]["mechanism_commitment"] == "NONE", "mechanism commitment NONE")
    check(data["ltgr8_admission"]["confirmation_credit"] == "NONE", "confirmation credit NONE")
    delta = data["source_to_proof_delta"]
    check(delta["template"] == DELTA_TEMPLATE, "delta template exact")
    for field in (
        "primary_source_claim",
        "native_carrier_action_reduction_observable",
        "current_certificate",
        "exact_missing_bridge",
        "evidence_that_would_reopen",
        "delta_motion",
    ):
        check(bool(delta.get(field)), f"delta field {field}")
    check("maintenance" in data["maintenance_labeling_rule"], "maintenance labeling rule")

    rows = {row["id"]: row for row in ledger["rows"] if isinstance(row, dict) and "id" in row}
    check("LT-GR8" in rows, "ledger LT-GR8 exists")
    check(rows["LT-GR8"]["verdict"] == "NEEDS", "ledger LT-GR8 NEEDS")
    check(rows["LT-GR8"]["mechanism_commitment"] == "NONE", "ledger mechanism NONE")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check(DELTA_TEMPLATE.split(" -> ")[0] in result and "evidence that would reopen it" in result, "delta template in doc")
    check("labeled maintenance" in result, "maintenance rule in doc")
    check("owner-before-evaluation" in result, "CBRS-1 boundary named")
    check("does not advance CBRS-2" in result or "not advance CBRS-2" in result or "does not open it" in result, "no CBRS-2 advance")
    check("true only because the enumeration was incomplete" in result, "claim-indexed binding of prior replay sentence")
    check("No scientific ledger verdict" in result, "claim ceiling")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    check("first type the K77-to-observed-3+1 carrier and boundary map" in state, "state licenses typing step")
    check("LT-GR8 typing arc" in state, "state records admission")
    check("LT-GR8 TYPING ARC" in next_steps, "next steps announcement")

    items = {item["id"]: item for item in agenda["work_items"]}
    check("LT-GR8" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"], "agenda selects typing swing")

    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")
    check(data["source_ownership_change"] == "none", "source ownership unchanged")
    check(data["public_posture_change"] == "none", "public posture unchanged")
    return checks, failures


def main() -> int:
    checks, failures = collect_failures(load_inputs())
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    baseline = load_inputs()
    checks, failures = collect_failures(baseline)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    mutations: list[tuple[str, str, dict[str, object]]] = []

    changed = copy.deepcopy(baseline)
    changed["data"]["registered_cbrs1_admissible_candidate_count"] = 1
    mutations.append(("admitted-count", "empty admitted set", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["frontier"][0]["disposition"] = "PARKED"
    mutations.append(("selection-drop", "LT-GR8 selected", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["source_to_proof_delta"]["template"] = "claims -> proofs"
    mutations.append(("delta-template-corrupt", "delta template exact", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["ltgr8_admission"]["mechanism_commitment"] = "JACOBSON_1995"
    mutations.append(("mechanism-smuggle", "mechanism commitment NONE", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive for the absence detector: the forbidden sentence must fire.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nThis result confirms Jacobson mechanism realization in GU.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: confirms Jacobson", changed))

    changed = copy.deepcopy(baseline)
    items = changed["agenda"]["work_items"]
    for item in items:
        if item["id"] == "CONDITIONAL-BUILD-REVERSE-SCAFFOLD":
            item["next_swing"] = item["next_swing"].replace("LT-GR8", "LT-REMOVED")
    mutations.append(("agenda-revert", "agenda selects typing swing", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected failing check {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
