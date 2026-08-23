#!/usr/bin/env python3
"""Regression probe for the B3-J95 primary-source scope disposition."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/b3-j95-primary-scope-disposition.json"
RESULT = ROOT / "explorations/conditional-build/b3-j95-primary-scope-disposition-2026-08-23.md"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
SOURCE_REGISTER = ROOT / "lab/process/fc-admission-wave-and-first-b3-register.json"
SOURCE_RESULT = ROOT / "explorations/conditional-build/fc-admission-wave-and-first-b3-register-2026-08-23.md"


def load_inputs() -> dict[str, object]:
    ledger = json.loads(LEDGER.read_text())
    row = next((row for row in ledger["rows"] if row["id"] == "LT-GR8"), {})
    return {
        "registry": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "row": row,
        "source_register": json.loads(SOURCE_REGISTER.read_text()),
        "source_result": SOURCE_RESULT.read_text(),
    }


def collect_failures(inputs: dict[str, object]) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    reg = inputs["registry"]
    result = inputs["result"]
    row = inputs["row"]
    source_register = inputs["source_register"]
    source_result = inputs["source_result"]
    assert isinstance(reg, dict) and isinstance(row, dict)
    assert isinstance(source_register, dict)
    assert isinstance(result, str) and isinstance(source_result, str)
    flat_result = re.sub(r"\s+", " ", result)

    check(reg["b3_id"] == "B3-J95-03", "B3 id pinned")
    check(reg["status"] == "DISPOSED_NO_LEDGER_MOVEMENT__SOURCE_SCOPE_CORRECTION",
          "no-movement disposition pinned")
    check(reg["target_claim"] == "NONE-NOT-A-KILL", "not-a-kill typing")
    sources = {source["id"]: source for source in reg["primary_sources"]}
    for source_id in ("JACOBSON-1995", "ELING-GUEDENS-JACOBSON-2006",
                      "GUEDENS-JACOBSON-SARKAR-2012"):
        check(source_id in sources, f"source present: {source_id}")
    egj = sources.get("ELING-GUEDENS-JACOBSON-2006", {})
    gjs = sources.get("GUEDENS-JACOBSON-SARKAR-2012", {})
    check("Ricci scalar" in egj.get("licensed_claim", ""),
          "2006 result remains Ricci-scalar scoped")
    check("algebraic in the metric and Riemann tensor" in
          gjs.get("licensed_claim", ""),
          "2012 algebraic-Riemann route recorded")
    check("integrability" in gjs.get("licensed_claim", ""),
          "2012 integrability condition recorded")
    check("not licensed" in reg["precise_impossibility"],
          "single-branch tightening precisely refused")

    check(row["verdict"] == "NEEDS", "LT-GR8 verdict preserved")
    check(row["reason_kind"] == "MISSING_CONSTRUCTION", "LT-GR8 reason preserved")
    check(row["mechanism_commitment"] == "NONE", "mechanism remains none")
    check(row["confirmation_credit"] == "NONE", "confirmation remains none")
    check("equilibrium or explicitly nonequilibrium law" in row["distance"],
          "distance preserves both branches")
    check("equilibrium or entropy-production law" in row["revival_trigger"],
          "revival trigger preserves both branches")

    b3 = source_register["b3_register"]
    check(b3["dispositions"]["B3-J95-03"]["status"] ==
          "DISPOSED_NO_LEDGER_MOVEMENT__SOURCE_SCOPE_CORRECTION",
          "source register carries disposition")
    check(b3["direction_scope"] == "historical_first_pass_before_primary_source_disposition",
          "old direction count is explicitly historical")
    check("B3-J95-SCOPE-20260823" in source_result,
          "owning prose acknowledges correction")
    check("equilibrium branch remains open" in source_result,
          "owning prose preserves equilibrium branch")

    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result,
          "routing class")
    check("```gu-typed-objects" in result, "typed-object block")
    check("No canon, ledger, source ownership" in flat_result, "claim ceiling in prose")
    for forbidden in (
        "the Weyl sector requires nonequilibrium thermodynamics",
        "the 2012 paper proves GU equilibrium",
        "LT-GR8 is discharged",
    ):
        check(forbidden not in flat_result, f"forbidden grammar absent: {forbidden}")
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
    changed["registry"]["status"] = "LEDGER_MOVED"
    mutations.append(("movement-inflation", "no-movement disposition pinned", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["primary_sources"] = changed["registry"]["primary_sources"][:2]
    mutations.append(("2012-source-dropped", "source present: GUEDENS-JACOBSON-SARKAR-2012", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["primary_sources"][1]["licensed_claim"] = \
        "Every curvature correction requires nonequilibrium thermodynamics."
    mutations.append(("fR-scope-widened", "2006 result remains Ricci-scalar scoped", changed))

    changed = copy.deepcopy(baseline)
    changed["row"]["verdict"] = "SAME"
    mutations.append(("verdict-laundered", "LT-GR8 verdict preserved", changed))

    changed = copy.deepcopy(baseline)
    changed["row"]["distance"] = changed["row"]["distance"].replace(
        "equilibrium or explicitly nonequilibrium law", "nonequilibrium law")
    mutations.append(("branch-collapsed", "distance preserves both branches", changed))

    changed = copy.deepcopy(baseline)
    changed["source_register"]["b3_register"]["direction_scope"] = "current"
    mutations.append(("historical-scope-erased", "old direction count is explicitly historical", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] += "\nthe Weyl sector requires nonequilibrium thermodynamics\n"
    mutations.append(("planted-overclaim",
                      "forbidden grammar absent: the Weyl sector requires nonequilibrium thermodynamics",
                      changed))

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
