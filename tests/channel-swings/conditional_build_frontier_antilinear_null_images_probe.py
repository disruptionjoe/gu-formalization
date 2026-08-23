#!/usr/bin/env python3
"""Propagation and failure-path probe for corrected T3 null-image typing."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-antilinear-null-images.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-antilinear-null-images-2026-08-22.md"
LEAN = ROOT / "Lean/GUFormalization/LocatedNotForcedLegs.lean"


def load_inputs() -> dict[str, object]:
    agenda = json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text())
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "lean": LEAN.read_text(),
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
    strings = [inputs["result"], inputs["lean"], inputs["readme"], inputs["ledger"], inputs["state"], inputs["next_steps"]]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    assert all(isinstance(item, str) for item in strings)
    result, lean, readme, ledger, state, next_steps = strings

    check(data["schema_version"] == "1.0", "schema")
    check(data["registered_cbrs1_admissible_candidate_count"] == 0, "empty admitted set")
    check(data["cbrs1_state"] == "PARKED_UNTIL_COMPLETE_NEW_OWNER_PACKET", "CBRS-1 parked")
    check("LOCAL_SOLUTION" in data["cbrs2_state"], "CBRS-2 dependency")
    check(data["corrections_applied"] == ["V15-1", "CARRIER-20260810"], "correction custody")
    check(len(data["frontier"]) == 6, "six-arc frontier")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("V15-1" in result and "CARRIER-20260810" in result, "corrections explained")
    check("K-null Lorentzian half" in result and "not a" in result, "Lorentzian transfer ceiling")
    check("does not imply nullness" in result, "map type does not imply isotropy")
    check("L10 old-file triage is now eligible only" in result, "conditional L10 fallback")

    for theorem in data["t3"]["theorems"]:
        check(f"theorem {theorem}" in lean, f"Lean theorem {theorem}")
    check("V →ₗ⋆[ℂ] V" in lean, "star-semilinear map type")
    check("def ImageTotallyIsotropic" in lean, "explicit image-isotropy premise")
    check("W.map C" in lean, "mapped complex submodule")
    check("conjugate-linearity alone does not" in lean, "no implicit nullness")
    check("intersectionDifference" in lean, "finite intersection invariant")
    check("Fredholm index or a" in lean, "Fredholm scope ceiling")
    check("sorry" not in lean.lower(), "no sorry")
    check("axiom" not in lean.lower(), "no axiom")

    check("star-semilinear images" in readme, "Lean README updated")
    check("T3 | Antilinear null-image transversality" in ledger, "T3 ledger row retained")
    check("`LEAN-VERIFIED`; corrected finite" in ledger, "T3 ledger closure")
    check("Post-L9 T3 correction follow-through" in ledger, "execution order closure")
    check("stable queue's remaining T3" in state, "current state T3")
    check("T3 ANTILINEAR NULL-IMAGE" in next_steps, "next steps T3")

    items = {item["id"]: item for item in agenda["work_items"]}
    check("PROOF-STABLE-KERNELS" in items, "proof agenda item")
    next_swing = items["PROOF-STABLE-KERNELS"]["next_swing"]
    check("T3 corrected finite antilinear null-image kernel are complete" in next_swing, "agenda closes T3")
    check("Rebuild the substantial frontier" in next_swing, "agenda rebuilds frontier")
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
    changed["data"]["registered_cbrs1_admissible_candidate_count"] = 1
    mutations.append(("admitted-count", "empty admitted set", changed))

    changed = copy.deepcopy(baseline)
    changed["lean"] = changed["lean"].replace("V →ₗ⋆[ℂ] V", "V →ₗ[ℂ] V")
    mutations.append(("antilinear-type-drop", "star-semilinear map type", changed))

    changed = copy.deepcopy(baseline)
    changed["lean"] = changed["lean"].replace("def ImageTotallyIsotropic", "def HiddenImagePremise")
    mutations.append(("isotropy-premise-hide", "explicit image-isotropy premise", changed))

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
    changed["result"] = changed["result"].replace("V15-1", "V15-REMOVED")
    mutations.append(("correction-drop", "corrections explained", changed))

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
