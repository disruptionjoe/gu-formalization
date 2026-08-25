#!/usr/bin/env python3
"""Propagation and failure-path probe for the L9 involution/projector kernels."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-l9-involution-projectors.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-l9-involution-projectors-2026-08-22.md"
LEAN = ROOT / "Lean/GUFormalization/InvolutionProjectorKernels.lean"


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
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
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
    agenda = inputs["agenda"]
    strings = [
        inputs["result"],
        inputs["lean"],
        inputs["root_lean"],
        inputs["readme"],
        inputs["ledger"],
        inputs["state"],
        inputs["next_steps"],
    ]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    assert all(isinstance(item, str) for item in strings)
    result, lean, root_lean, readme, ledger, state, next_steps = strings
    result_flat = " ".join(result.split())
    state_flat = " ".join(state.split())

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
    check("L10 old-file triage is conditional" in result_flat, "conditional L10 next gate")

    for theorem in data["l9"]["theorems"]:
        check(f"theorem {theorem}" in lean, f"Lean theorem {theorem}")
    check("theta * theta = 1" in lean, "explicit inner-involution premise")
    check("p.comp p = LinearMap.id" in lean, "explicit linear-involution premise")
    check("[CharZero R]" in lean, "two-invertibility premise")
    check("sorry" not in lean.lower(), "no sorry")
    check("axiom" not in lean.lower(), "no axiom")
    check("import GUFormalization.InvolutionProjectorKernels" in root_lean, "default target import")
    check("InvolutionProjectorKernels.lean`" in readme, "Lean README surface")
    check("L9 THEOREMS F AND G` — **DONE" in ledger, "ledger closure")
    check("abstract inner-involution" in state_flat, "current state L9")
    check("L9 ABSTRACT INVOLUTION" in next_steps, "next steps L9")

    items = {item["id"]: item for item in agenda["work_items"]}
    check("PROOF-STABLE-KERNELS" in items, "proof agenda item")
    check(
        "L9 abstract involution/projector kernels"
        in items["PROOF-STABLE-KERNELS"]["next_swing"]
        and "are complete" in items["PROOF-STABLE-KERNELS"]["next_swing"],
        "agenda closes L9",
    )
    check("Rebuild the substantial frontier" in items["PROOF-STABLE-KERNELS"]["next_swing"], "agenda rebuilds frontier")
    check(
        "strongest disjoint non-B2 native gate"
        in items["CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]["next_swing"],
        "agenda keeps the empty B2 root out of selection",
    )

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
    changed["lean"] = changed["lean"].replace("theorem commutator_even_odd", "def commutator_even_odd")
    mutations.append(("missing-theorem", "Lean theorem commutator_even_odd", changed))

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
    changed["root_lean"] = changed["root_lean"].replace("import GUFormalization.InvolutionProjectorKernels", "")
    mutations.append(("default-target-drop", "default target import", changed))

    changed = copy.deepcopy(baseline)
    changed["lean"] = changed["lean"].replace("[CharZero R]", "")
    mutations.append(("two-invertibility-drop", "two-invertibility premise", changed))

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
