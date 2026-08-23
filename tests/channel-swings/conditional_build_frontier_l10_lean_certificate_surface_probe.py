#!/usr/bin/env python3
"""Propagation and failure-path probe for the L10 Lean surface repair."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/conditional-build-frontier-and-l10-lean-certificate-surface.json"
RESULT = ROOT / "explorations/conditional-build/conditional-build-frontier-and-l10-lean-certificate-surface-2026-08-22.md"
IMPORT_LINE = re.compile(r"^import\s+(GUFormalization\.[A-Za-z0-9_.]+)\s*$", re.MULTILINE)


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "entrypoint": (ROOT / "Lean/GUFormalization.lean").read_text(),
        "gate": (ROOT / "process_gates/lean_certificate_surface_audit.py").read_text(),
        "readme": (ROOT / "Lean/README.md").read_text(),
        "ledger": (ROOT / "lab/process/lean-verification-lane-LEDGER.md").read_text(),
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
    agenda = inputs["agenda"]
    assert isinstance(data, dict) and isinstance(agenda, dict)
    entrypoint = str(inputs["entrypoint"])
    gate = str(inputs["gate"])
    readme = str(inputs["readme"])
    ledger = str(inputs["ledger"])
    result = str(inputs["result"])
    state = str(inputs["state"])
    next_steps = str(inputs["next_steps"])
    modules = IMPORT_LINE.findall(entrypoint)

    check(data["schema_version"] == "1.0", "schema")
    check(data["default_target_module_count"] == 16, "registered module count")
    check(len(modules) == data["default_target_module_count"], "actual module count")
    check(data["manual_non_default_certificates"] == ["Lean/GUFormalization/ResidualSelectionAxioms.lean"], "manual receipt boundary")
    check(len(data["frontier"]) == 6, "six-arc frontier")
    check(data["frontier"][0]["disposition"] == "CLOSED_HERE", "L10 closed")

    check("def local_import_modules" in gate, "entrypoint-derived inventory")
    check("LEAN_LIBRARY_CERTIFICATES" not in gate, "duplicated inventory removed")
    check("lab\" / \"methods\" / \"claim-status-consistency.md" in gate, "live owner reference")
    check("runbooks\" / \"claim-status-consistency-quality-workflow.md" not in gate, "removed runbook reference retired")
    check("library,\n            imported | manual" in gate, "complete library equality")

    for module in modules:
        relative = module.replace(".", "/") + ".lean"
        check(f"`{relative}`" in readme, f"README covers {module}")
        check(f"`Lean/{relative}`" in ledger, f"ledger covers {module}")
    check("`GUFormalization/ResidualSelectionAxioms.lean`" in readme, "README manual receipt")
    check("`Lean/GUFormalization/ResidualSelectionAxioms.lean`" in ledger, "ledger manual receipt")
    check("| F |" in ledger and "`LEAN-VERIFIED`; abstract inner-involution" in ledger, "F grade reconciled")
    check("| G |" in ledger and "`LEAN-VERIFIED`; abstract complementary-projector" in ledger, "G grade reconciled")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("proves no new theorem" in result, "claim ceiling")
    check("post-T3 frontier replay" in state, "current state")
    check("L10 RECONCILES" in next_steps, "next steps")

    items = {item["id"]: item for item in agenda["work_items"]}
    check("L10 live certificate-surface reconciliation are complete" in items["PROOF-STABLE-KERNELS"]["next_swing"], "agenda closes L10")
    check(data["theorem_body_change"] == "none", "theorem bodies unchanged")
    check(data["scientific_ledger_verdict_change"] == "none", "scientific verdict unchanged")
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
    changed["data"]["default_target_module_count"] = 15
    mutations.append(("module-count", "registered module count", changed))

    changed = copy.deepcopy(baseline)
    changed["readme"] = changed["readme"].replace("`GUFormalization/InvolutionProjectorKernels.lean`", "`REMOVED.lean`")
    mutations.append(("readme-drop", "README covers GUFormalization.InvolutionProjectorKernels", changed))

    changed = copy.deepcopy(baseline)
    changed["ledger"] = changed["ledger"].replace("`LEAN-VERIFIED`; abstract inner-involution", "`NUMPY-CERT`; abstract inner-involution")
    mutations.append(("stale-f-grade", "F grade reconciled", changed))

    changed = copy.deepcopy(baseline)
    changed["gate"] = changed["gate"].replace("def local_import_modules", "def removed_import_derivation")
    mutations.append(("hardcoded-drift", "entrypoint-derived inventory", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace("proves no new theorem", "upgrades physical truth")
    mutations.append(("scope-overclaim", "claim ceiling", changed))

    ok = True
    for name, expected, mutated in mutations:
        _, caught = collect_failures(mutated)
        if expected not in caught:
            print(f"[FAIL] mutation {name}: expected {expected!r}, got {caught!r}")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: [FAIL] {expected}")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
