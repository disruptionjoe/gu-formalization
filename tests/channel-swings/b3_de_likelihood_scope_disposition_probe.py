#!/usr/bin/env python3
"""Regression probe for the B3-DE likelihood-scope disposition."""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/b3-de-likelihood-scope-disposition.json"
RESULT = ROOT / "explorations/conditional-build/b3-de-likelihood-scope-disposition-2026-08-23.md"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
SOURCE_REGISTER = ROOT / "lab/process/fc-admission-wave-and-first-b3-register.json"
SOURCE_RESULT = ROOT / "explorations/conditional-build/fc-admission-wave-and-first-b3-register-2026-08-23.md"


def load_inputs() -> dict[str, object]:
    ledger = json.loads(LEDGER.read_text())
    row = next((row for row in ledger["rows"] if row["id"] == "LT-GR2e"), {})
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

    check(reg["b3_id"] == "B3-DE-01", "B3 id pinned")
    check(reg["status"] ==
          "DISPOSED_NO_LEDGER_MOVEMENT__LIKELIHOOD_SCOPE_CORRECTION",
          "no-movement disposition pinned")
    check(reg["target_claim"] == "NONE-NOT-A-KILL", "not-a-kill typing")
    sources = {source["id"]: source for source in reg["primary_sources"]}
    for source_id in (
        "DESI-DR2-II-2025",
        "DESI-DR2-EXTENDED-DE-2025",
        "DESI-DR2-IV-LYA-AP-2026",
    ):
        check(source_id in sources, f"source present: {source_id}")
    baseline = sources.get("DESI-DR2-II-2025", {})
    extended = sources.get("DESI-DR2-EXTENDED-DE-2025", {})
    lya = sources.get("DESI-DR2-IV-LYA-AP-2026", {})
    check("model-conditioned fit parameters" in baseline.get("ceiling", ""),
          "CPL parameter ceiling pinned")
    check("cannot be ruled out" in extended.get("licensed_claim", ""),
          "noncrossing alternatives preserved")
    check("does not by itself directly measure" in lya.get("ceiling", ""),
          "Lyman-alpha pointwise ceiling pinned")
    check("retain the direct and nonparametric lean" in reg["precise_relocation"],
          "crossing evidence retained")
    check(len(reg["dark_energy_07_corrections"]) == 5,
          "DARK-ENERGY-07 chain complete")

    check(row["verdict"] == "NEEDS", "LT-GR2e verdict preserved")
    check(row["reason_kind"] == "MISSING_CONSTRUCTION",
          "LT-GR2e reason preserved")
    check("matter/radiation FLRW perturbations" in row["distance"],
          "perturbation burden preserved")
    check("held-out w(z)" in row["distance"], "held-out w(z) preserved")
    check("action-owned cosmological solution" in row["revival_trigger"],
          "action-owned solution preserved")
    check("held-out DESI/CMB/BAO predictions" in row["revival_trigger"],
          "held-out likelihood burden preserved")

    b3 = source_register["b3_register"]
    check(b3["dispositions"]["B3-DE-01"]["status"] ==
          "DISPOSED_NO_LEDGER_MOVEMENT__LIKELIHOOD_SCOPE_CORRECTION",
          "source register carries disposition")
    check(b3["remaining_entries"] == 3, "remaining B3 count")
    check("B3-DE-SCOPE-20260823" in source_result,
          "owning prose acknowledges correction")
    check("nonparametric" in source_result,
          "owning prose preserves direct evidence")

    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result,
          "routing class")
    check("```gu-typed-objects" in result, "typed-object block")
    check("No laundering" in flat_result, "claim ceiling in prose")
    for forbidden in (
        "all crossing evidence disappears",
        "every noncrossing GU family is ruled out",
        "CPL central pair directly measures w(z)",
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
    mutations.append(("newest-source-dropped",
                      "source present: DESI-DR2-IV-LYA-AP-2026", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["primary_sources"][0]["ceiling"] = \
        "These are literal pointwise measurements."
    mutations.append(("cpl-ceiling-erased", "CPL parameter ceiling pinned", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["primary_sources"][1]["licensed_claim"] = \
        "All noncrossing alternatives are ruled out."
    mutations.append(("noncrossing-ceiling-erased",
                      "noncrossing alternatives preserved", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["dark_energy_07_corrections"] = \
        changed["registry"]["dark_energy_07_corrections"][:4]
    mutations.append(("correction-chain-truncated",
                      "DARK-ENERGY-07 chain complete", changed))

    changed = copy.deepcopy(baseline)
    changed["row"]["verdict"] = "DIFFERS"
    mutations.append(("verdict-laundered", "LT-GR2e verdict preserved", changed))

    changed = copy.deepcopy(baseline)
    changed["source_register"]["b3_register"]["remaining_entries"] = 4
    mutations.append(("remaining-count-stale", "remaining B3 count", changed))

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
