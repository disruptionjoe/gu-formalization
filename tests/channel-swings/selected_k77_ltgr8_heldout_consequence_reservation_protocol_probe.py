#!/usr/bin/env python3
"""Propagation and failure-path probe for the LT-GR8 D6 preregistration protocol."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/selected-k77-ltgr8-heldout-consequence-reservation-protocol.json"
RESULT = ROOT / "explorations/conditional-build/selected-k77-ltgr8-heldout-consequence-reservation-protocol-2026-08-23.md"
DESCENT = ROOT / "lab/process/selected-k77-ltgr8-reverse-track-descent-r6-to-r3.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU is confirmed",
    "confirms Jacobson",
    "prediction credit is awarded",
    "the consequence is verified",
    "the packet succeeds",
)


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "descent": json.loads(DESCENT.read_text()),
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
    result = inputs["result"]
    descent = inputs["descent"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(descent, dict) and isinstance(agenda, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)

    f1 = data["family_f1_primary"]
    check(f1["name"] == "CROSS_SECTOR_NORMALIZATION_CONSISTENCY", "F1 named")
    check("released after the packet freeze" in f1["confrontation_data"], "F1 future-data-only")
    check("inadmissible as held-out data" in f1["already_read_inadmissible"], "DESI DR2 inadmissible")
    check("30.8059" in f1["already_read_inadmissible"] and "31.9715" in f1["already_read_inadmissible"],
          "recorded amplitudes cited at recorded grade")
    check("sub-percent" in f1["standing_exclusion_observable"], "standing exclusion observable")
    check(f1["data_wake"] == "P-OBS monitor lane", "F1 wake is P-OBS")

    f2 = data["family_f2_fallback"]
    check(f2["name"] == "NONEQUILIBRIUM_CORRECTION_FORM", "F2 named")
    check("not used in the reverse build" in f2["confrontation_data"], "F2 outside build inputs")
    check("equilibrium Clausius" in f2["why_held_out"], "F2 held-out rationale")

    rule = data["selection_rule"]
    check("typed derivation" in rule and "non-coupling proof" in rule, "selection escape needs typed proof")
    check("voids prediction credit" in rule, "third-family voiding")

    protocol = data["reservation_protocol"]
    check(len(protocol) == 5, "five protocol steps")

    def step(index: int) -> str:
        # A truncated list must fail its check, not crash the harness.
        return protocol[index] if index < len(protocol) else ""

    check("numeric content" in step(0), "step 1 numeric content")
    check("packet commit hash" in step(1) and "ledger digest" in step(1), "step 2 stamps")
    check("only after the record is committed" in step(2), "step 3 commit-before-read")
    check("released after the freeze commit" in step(3), "step 4 data custody")
    check("voids prediction credit" in step(4), "step 5 void condition")

    grammar = data["credit_grammar"]
    check("prediction candidate pending independent verification" in grammar["success_ceiling"],
          "success ceiling")
    check("never summarized as GU confirmed" in grammar["success_ceiling"], "no GU-confirmed summary")
    check("kills only the scoped GU-Jacobson" in grammar["failure_scope"], "kill scope preserved")

    acct = data["descent_interface_accounting"]
    check("PROTOCOL_FROZEN_HERE" in acct["D6"], "D6 protocol frozen")
    check("queue empty" in acct["queue"], "descent queue empty")
    check(data["mechanism_commitment"] == "NONE", "mechanism commitment NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation credit NONE")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    # Descent registry linkage.
    interface = {d["id"]: d for d in descent["r2_r1_demand_interface"]}
    d6 = interface["D6_HELD_OUT_CONSEQUENCE_RESERVED"]
    check("PROTOCOL_FROZEN" in d6.get("status", ""), "descent D6 status updated")
    check(d6.get("result_ref", "").endswith("selected-k77-ltgr8-heldout-consequence-reservation-protocol.json"),
          "descent D6 result ref")
    check("R1" in descent["next_demand"] or "FRONTIER" in descent["next_demand"],
          "descent next demand returns to R1/frontier")

    # Document propagation.
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("before any packet exists" in result, "frozen before packet")
    check("INADMISSIBLE" in result or "inadmissible" in result, "inadmissibility in doc")
    check("voids prediction credit" in result, "void condition in doc")
    check("prediction candidate" in result, "success ceiling in doc")
    check("remains `NEEDS`" in result or "remains NEEDS" in result, "LT-GR8 stays NEEDS")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    # Workspace propagation.
    check("D6" in state and "protocol" in state, "state records D6 protocol")
    check("D6 is complete at" in state and "must not be selected again" in state,
          "state forbids duplicate D6 selection")
    check("Next\n  freeze D6's single held-out consequence" not in state,
          "stale next-D6 continuation absent")
    check("LT-GR8 D6" in next_steps, "next steps announcement")
    items = {item["id"]: item for item in agenda["work_items"]}
    check("D6" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"],
          "agenda records D6")
    check("demand D6 is complete" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["latest_result"],
          "agenda latest result is D6")
    check("must not be selected again" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["latest_result"],
          "agenda latest result blocks duplicate D6")
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
    changed["data"]["family_f1_primary"]["confrontation_data"] = "any BAO data including DESI DR2"
    mutations.append(("data-custody-breach", "F1 future-data-only", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["selection_rule"] = "F1 or F2, whichever the packet prefers"
    mutations.append(("selection-loosening", "selection escape needs typed proof", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["reservation_protocol"] = changed["data"]["reservation_protocol"][:4]
    mutations.append(("void-condition-drop", "five protocol steps", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["credit_grammar"]["success_ceiling"] = "GU confirmed on held-out success"
    mutations.append(("credit-inflation", "success ceiling", changed))

    changed = copy.deepcopy(baseline)
    for d in changed["descent"]["r2_r1_demand_interface"]:
        if d["id"] == "D6_HELD_OUT_CONSEQUENCE_RESERVED":
            d["status"] = "DISCHARGED"
    mutations.append(("d6-discharge-smuggle", "descent D6 status updated", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive: the forbidden-grammar detector must fire on an injected claim.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nOn held-out success, GU is confirmed.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: GU is confirmed", changed))

    changed = copy.deepcopy(baseline)
    items = {item["id"]: item for item in changed["agenda"]["work_items"]}
    items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["latest_result"] = "LT-GR8 demand D4 is complete"
    mutations.append(("stale-agenda-latest-result", "agenda latest result is D6", changed))

    changed = copy.deepcopy(baseline)
    changed["state"] += "\nNext\n  freeze D6's single held-out consequence\n"
    mutations.append(("duplicate-d6-continuation", "stale next-D6 continuation absent", changed))

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
