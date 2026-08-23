#!/usr/bin/env python3
"""Probe for the program-velocity council.

The load-bearing property is NOT that the council reached agreement -- it is
that it did not. These checks enforce structure (eight lenses, three each),
non-flattening (refusals name the lens they refuse; disagreements name both
sides), and that every plan item traces to a stated diagnosis.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/program-velocity-council.json"
RESULT = ROOT / "explorations/program-velocity-council-2026-08-23.md"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "the council agreed",
    "the lenses converged",
    "on balance the program is healthy",
    "prediction credit is awarded",
)

LENS_REF = re.compile(r"^L[1-8]\.[1-3]$")


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
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
    assert isinstance(data, dict) and isinstance(result, str)

    # ---- structure: eight lenses, exactly three diagnoses each -----------
    lenses = data["lenses"]
    check(len(lenses) == 8, "eight lenses")
    for name, items in lenses.items():
        check(len(items) == 3, f"{name} states exactly three diagnoses")
        check(all(isinstance(i, str) and len(i) > 40 for i in items),
              f"{name} diagnoses are substantive")
    check(data["diagnoses_per_lens"] == 3, "declared three per lens")
    check(data["total_diagnoses"] == 24 == sum(len(v) for v in lenses.values()),
          "recomputed total is 24")

    # ---- non-flattening: refusals and disagreements name their opponents --
    refusals = data["explicit_refusals"]
    check(len(refusals) >= 3, "at least three explicit refusals")
    for r in refusals:
        check(bool(LENS_REF.match(r.get("against_lens", ""))),
              f"refusal '{r.get('refused','?')}' names the lens it refuses")
        check(len(r.get("reason", "")) > 40, f"refusal '{r.get('refused','?')}' gives a reason")
    disagreements = data["standing_disagreements"]
    check(len(disagreements) >= 2, "at least two standing disagreements")
    for d in disagreements:
        check(len(d.get("between", [])) >= 2, "each disagreement names at least two sides")
        check(all(LENS_REF.match(s) for s in d.get("between", [])),
              "disagreement sides are lens references")
        check(bool(d.get("resolution")), "each disagreement states its resolution status")
    # A council that resolved everything would have flattened; at least one
    # disagreement must remain explicitly unresolved.
    check(any("unresolved" in d.get("resolution", "").lower() or "discriminator" in d.get("resolution", "").lower()
              for d in disagreements),
          "at least one disagreement is left unresolved by design")

    # ---- every plan item traces to a stated diagnosis --------------------
    plan = data["action_plan"]
    check([p["id"] for p in plan] == [f"A{i}" for i in range(1, 9)], "eight plan items in order")
    valid_refs = {f"L{i}.{j}" for i in range(1, 9) for j in range(1, 4)}
    for p in plan:
        froms = p.get("from", [])
        check(bool(froms), f"{p['id']} names its source diagnosis")
        check(all(f in valid_refs for f in froms), f"{p['id']} source diagnoses are valid lens refs")
        check(len(p.get("action", "")) > 40, f"{p['id']} states a substantive action")
    # The adversary must not be silently dropped from the plan.
    all_refs = {f for p in plan for f in p.get("from", [])} | {
        r["against_lens"] for r in refusals}
    check(any(f.startswith("L8") for f in all_refs), "the adversary lens reaches the plan or the refusals")
    check(any(f.startswith("L7") for f in all_refs), "the source custodian reaches the plan or the refusals")

    # ---- A2 is the designated discriminator ------------------------------
    a2 = next((p for p in plan if p["id"] == "A2"), {})
    check("necessity theorem" in a2.get("action", ""), "A2 is the necessity theorem")
    check("discriminator" in a2.get("note", ""), "A2 is marked the discriminator")
    term = next((r for r in refusals if "terminal" in r.get("refused", "")), {})
    check("A2" in term.get("reason", "") and "without further delay" in term.get("reason", ""),
          "the terminal-result refusal is conditional on A2 and names the fallback")

    # ---- ceilings and honesty -------------------------------------------
    check(data["target_claim"] == "NONE-NOT-A-KILL", "council types its own kill status")
    check(data["ledger_verdict_change"] == "none", "no verdict moved")
    check("partially answered" in data["counterpoint_recorded_2026_08_23"],
          "the counterpoint to L8.1 is recorded without overclaiming it")

    result_flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: INTERNAL_STRUCTURAL_ONLY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("not merged" in result_flat or "not flattened" in result_flat, "doc states the non-flattening method")
    check("Explicitly refused" in result, "doc carries the refusals section")
    check("Standing disagreements" in result, "doc carries the disagreements section")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result_flat, f"forbidden grammar absent: {phrase}")
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
    changed["data"]["lenses"]["L8_ADVERSARY"] = changed["data"]["lenses"]["L8_ADVERSARY"][:2]
    mutations.append(("lens-truncated", "L8_ADVERSARY states exactly three diagnoses", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["explicit_refusals"] = changed["data"]["explicit_refusals"][:2]
    mutations.append(("refusals-softened", "at least three explicit refusals", changed))

    changed = copy.deepcopy(baseline)
    for d in changed["data"]["standing_disagreements"]:
        d["resolution"] = "merged into a consensus view"
    mutations.append(("flattening", "at least one disagreement is left unresolved by design", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["explicit_refusals"][0]["against_lens"] = "the architect"
    mutations.append(("unattributed-refusal", "refusal 'reduce the propagation surfaces' names the lens it refuses", changed))

    changed = copy.deepcopy(baseline)
    for p in changed["data"]["action_plan"]:
        p["from"] = [f for f in p["from"] if not f.startswith("L8")]
    changed["data"]["explicit_refusals"] = [
        r for r in changed["data"]["explicit_refusals"] if not r["against_lens"].startswith("L8")]
    mutations.append(("adversary-dropped", "the adversary lens reaches the plan or the refusals", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["action_plan"][1]["note"] = "a nice-to-have"
    mutations.append(("discriminator-demoted", "A2 is marked the discriminator", changed))

    # Planted positive for the summary-grammar detector.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nAfter debate the council agreed on a single view.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: the council agreed", changed))

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
