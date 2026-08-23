#!/usr/bin/env python3
"""Propagation and failure-path probe for the three gravitational anchor descents."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/ext-gr-anchors-reverse-track-descents-r5-to-r3.json"
RESULT = ROOT / "explorations/conditional-build/ext-gr-anchors-reverse-track-descents-r5-to-r3-2026-08-23.md"
BENCH = ROOT / "lab/process/ext-gr-benchmark-bench-registry.json"

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU reproduces Kerr",
    "the PPN parameters are derived",
    "prediction credit is awarded",
    "the rotation curves are explained",
)

EXPECTED_DESCENTS = ["EXT-GR-STRONGFIELD", "EXT-GR-PPN", "EXT-GR-ROTATION"]
EXPECTED_OWNERS = ["OWNER-A", "OWNER-B", "OWNER-C", "OWNER-D", "OWNER-E"]


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "bench": json.loads(BENCH.read_text()),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
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
    bench = inputs["bench"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    assert isinstance(data, dict) and isinstance(bench, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)

    descents = data["descents"]
    check(list(descents) == EXPECTED_DESCENTS, "three descents in order")
    bench_ids = [row["id"] for row in bench["benchmarks"]]
    check(bench_ids == EXPECTED_DESCENTS, "descents match accepted bench anchors")

    for anchor in EXPECTED_DESCENTS:
        d = descents.get(anchor, {})
        for rung in ("r5_frozen", "r4_frozen", "r3_frozen"):
            check(d.get(rung, {}).get("comparator_driven") is True, f"{anchor} {rung} comparator-driven")
        interface = d.get("interface", [])
        check(len(interface) >= 3, f"{anchor} has at least three demands")
        check(all(item.get("lands_on") for item in interface), f"{anchor} demands land on named gaps")
        check(all(item.get("owner") in EXPECTED_OWNERS for item in interface),
              f"{anchor} demands map to consolidated owners")

    check("O(M^2/r^4)" in descents["EXT-GR-STRONGFIELD"]["r5_frozen"]["comparison_observable"],
          "W225 residual order priced")
    check("T-4" in descents["EXT-GR-STRONGFIELD"]["r4_frozen"]["horizon"], "T-4 inherited")
    check("ill-posed by default" in descents["EXT-GR-STRONGFIELD"]["r3_frozen"]["evolution"],
          "hyperbolicity demanded not inherited")
    check("D1 recurs" in descents["EXT-GR-PPN"]["r3_frozen"]["constraints"], "D1 recurrence recorded")
    check("W220" in descents["EXT-GR-PPN"]["r5_frozen"]["comparison_observable"], "W220 bounds bound")
    check("H49" in descents["EXT-GR-ROTATION"]["r5_frozen"]["comparison_observable"], "H49 killer frozen")
    check("H24" in descents["EXT-GR-ROTATION"]["r4_frozen"]["discriminator"], "H24 ratio-only typed")
    check("external datum" in descents["EXT-GR-ROTATION"]["r4_frozen"]["discriminator"],
          "absolute scale typed external")

    # Consolidated owner ledger: every owner present and demanded by >= 2
    # independent lanes (triangulation), with every interface owner listed.
    ledger = data["consolidated_r1_owner_ledger"]
    check(list(ledger) == EXPECTED_OWNERS, "five owners in order")
    for owner_id, entry in ledger.items():
        check(len(entry.get("demanded_by", [])) >= 2, f"{owner_id} triangulated by >=2 demands")
    interface_owner_refs = {
        item["owner"]
        for d in descents.values()
        for item in d["interface"]
    }
    check(interface_owner_refs.issubset(set(ledger)), "every referenced owner is in the ledger")
    # An unlisted owner must fail the subset check above, not crash this loop.
    for owner_id in interface_owner_refs & set(ledger):
        named = set(ledger[owner_id]["demanded_by"])
        claimed = {
            item["id"]
            for d in descents.values()
            for item in d["interface"]
            if item["owner"] == owner_id
        }
        check(claimed.issubset(named), f"{owner_id} ledger lists all its interface demands")

    check("discharges or materially narrows" in data["progress_rule"], "progress rule")
    check(data["mechanism_commitment"] == "NONE", "mechanism NONE")
    check(data["confirmation_credit"] == "NONE", "confirmation NONE")
    check("CBRS-blocked" in data["instantiation"], "instantiation blocked")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("Demands, not constructions" in result or "DEMANDS, NOT CONSTRUCTIONS" in result, "demand ceiling")
    check("triangulation counts" in result, "triangulation stated")
    check("MISSING_CONSTRUCTION" in result, "realizations stay missing")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    check("consolidated" in state and "OWNER-A" in state, "state records owner ledger")
    check("ANCHOR DESCENTS" in next_steps or "anchor descents" in next_steps, "next steps announcement")
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
    changed["data"]["descents"]["EXT-GR-PPN"]["r5_frozen"]["comparator_driven"] = False
    mutations.append(("comparator-flag-drop", "EXT-GR-PPN r5_frozen comparator-driven", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["consolidated_r1_owner_ledger"]["OWNER-C"]["demanded_by"] = ["PPN-2"]
    mutations.append(("triangulation-loss", "OWNER-C triangulated by >=2 demands", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["descents"]["EXT-GR-STRONGFIELD"]["interface"][0]["owner"] = "OWNER-Z"
    mutations.append(("unlisted-owner", "EXT-GR-STRONGFIELD demands map to consolidated owners", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["descents"]["EXT-GR-ROTATION"]["r4_frozen"]["discriminator"] = (
        "the action derives the absolute galactic scale directly")
    mutations.append(("scale-derivation-smuggle", "H24 ratio-only typed", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["mechanism_commitment"] = "GR_MECHANISM"
    mutations.append(("mechanism-smuggle", "mechanism NONE", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive: the forbidden-grammar detector must fire on an injected claim.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nWith the descents frozen, GU reproduces Kerr.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: GU reproduces Kerr", changed))

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
