#!/usr/bin/env python3
"""Propagation and failure-path probe for the L8 finite trace-parity kernel."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-l8-chi-parity.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-l8-chi-parity-2026-08-22.md"
LEAN = ROOT / "Lean/GUFormalization/ChiConjugationTraceParity.lean"


def load_inputs() -> dict[str, object]:
    agenda = json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text())
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "lean": LEAN.read_text(),
        "root_lean": (ROOT / "Lean/GUFormalization.lean").read_text(),
        "readme": (ROOT / "Lean/README.md").read_text(),
        "ledger": (ROOT / "lab/process/lean-verification-lane-LEDGER.md").read_text(),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "agenda": agenda,
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
    lean = inputs["lean"]
    root_lean = inputs["root_lean"]
    readme = inputs["readme"]
    ledger = inputs["ledger"]
    state = inputs["state"]
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    assert all(isinstance(x, str) for x in (result, lean, root_lean, readme, ledger, state))

    check(data["schema_version"] == "1.0", "schema")
    check(data["admissible_candidate_count"] == 0, "empty admitted set")
    check(len(data["admission_requirements"]) == 4, "four admission requirements")
    check(len(data["candidate_census"]) == 7, "seven registered candidates")
    check(all(not row["eligible"] for row in data["candidate_census"]), "no eligible candidate")
    check(all(row["missing"] for row in data["candidate_census"]), "each candidate has exact missing owner")
    check(data["cbrs1_state"] == "PARKED_UNTIL_COMPLETE_NEW_OWNER_PACKET", "CBRS-1 parked")
    check("LOCAL_SOLUTION" in data["cbrs2_state"], "CBRS-2 dependency")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("registry-relative" in result, "claim ceiling")
    check("not a universal" in result.lower(), "no universal no-go")
    check("L9 abstract involution" in result, "next gate")

    for theorem in data["l8"]["theorems"]:
        check(f"theorem {theorem}" in lean, f"Lean theorem {theorem}")
    check("trace_mul_comm" in lean, "finite trace cyclicity owner")
    check("sorry" not in lean.lower(), "no sorry")
    check("axiom" not in lean.lower(), "no axiom")
    check("import GUFormalization.ChiConjugationTraceParity" in root_lean, "default target import")
    check("ChiConjugationTraceParity.lean`" in readme, "Lean README surface")
    check("L8 THEOREM E` — **DONE" in ledger, "ledger closure")
    check("finite ordinary/weighted matrix power-trace parity only" in ledger, "ledger claim ceiling")

    check("L8 gate is now Lean-verified" in state, "current state L8")
    check("L9" in state, "current state advances to L9")
    items = {item["id"]: item for item in agenda["work_items"]}
    check("PROOF-STABLE-KERNELS" in items, "proof agenda item")
    check("Execute L9 next" in items["PROOF-STABLE-KERNELS"]["next_swing"], "agenda advances to L9")
    check("park" in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"].lower(), "agenda keeps CBRS-1 parked")

    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["source_ownership_change"] == "none", "source ownership unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")
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
    changed["data"]["admissible_candidate_count"] = 1
    mutations.append(("admitted-count", "empty admitted set", changed))

    changed = copy.deepcopy(baseline)
    changed["lean"] = changed["lean"].replace("theorem trace_pow_conjugation_even", "def trace_pow_conjugation_even")
    mutations.append(("missing-theorem", "Lean theorem trace_pow_conjugation_even", changed))

    changed = copy.deepcopy(baseline)
    changed["lean"] += "\naxiom planted_bad_certificate : True\n"
    mutations.append(("axiom-injection", "no axiom", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    changed = copy.deepcopy(baseline)
    changed["root_lean"] = changed["root_lean"].replace("import GUFormalization.ChiConjugationTraceParity", "")
    mutations.append(("default-target-drop", "default target import", changed))

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
