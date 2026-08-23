#!/usr/bin/env python3
"""Regression and failure-path probe for gravitational-anchor bucket disposition."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/gravitational-anchor-bucket-disposition-and-first-fitting-construction.json"
RESULT = ROOT / "explorations/conditional-build/gravitational-anchor-bucket-disposition-and-first-fitting-construction-2026-08-23.md"
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
BENCH = ROOT / "lab/process/ext-gr-benchmark-bench-registry.json"
DESCENT = ROOT / "lab/process/ext-gr-anchors-reverse-track-descents-r5-to-r3.json"

EXPECTED = {
    "LT-GR9": ("EXT-GR-STRONGFIELD", "B2", "PRECISE_NONADMISSION"),
    "LT-GR10": ("EXT-GR-PPN", "B2", "PRECISE_NONADMISSION"),
    "LT-GR11": ("EXT-GR-ROTATION", "B1", "FITTING_CONSTRUCTION"),
}
FC_KEYS = [f"FC-{i}" for i in range(1, 8)]


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "ledger": json.loads(LEDGER.read_text()),
        "bench": json.loads(BENCH.read_text()),
        "descent": json.loads(DESCENT.read_text()),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "agenda": json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
        "research_status": (ROOT / "RESEARCH-STATUS.md").read_text(),
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
    ledger = inputs["ledger"]
    bench = inputs["bench"]
    descent = inputs["descent"]
    assert isinstance(data, dict) and isinstance(result, str)
    assert isinstance(ledger, dict) and isinstance(bench, dict) and isinstance(descent, dict)
    flat_result = " ".join(result.split())

    rows = {row["id"]: row for row in ledger["rows"]}
    bench_ids = {row["id"] for row in bench["benchmarks"]}
    dispositions = {row["row_id"]: row for row in data["dispositions"]}
    check(set(dispositions) == set(EXPECTED), "exact three-row disposition set")
    for row_id, (anchor_id, bucket, outcome) in EXPECTED.items():
        row = dispositions.get(row_id, {})
        check(rows.get(row_id, {}).get("verdict") == "NEEDS", f"{row_id} remains NEEDS")
        check(rows.get(row_id, {}).get("reason_kind") == "MISSING_CONSTRUCTION", f"{row_id} remains MISSING_CONSTRUCTION")
        check(anchor_id in bench_ids, f"{anchor_id} accepted anchor exists")
        check(row.get("anchor_id") == anchor_id, f"{row_id} anchor binding")
        check(row.get("bucket") == bucket, f"{row_id} bucket")
        check(row.get("outcome") == outcome, f"{row_id} outcome")

    sf = dispositions["LT-GR9"]
    ppn = dispositions["LT-GR10"]
    check(sf["named_requirements"] == ["SF-1", "SF-2", "SF-3", "SF-4", "SF-5"], "strong-field named requirements")
    check(ppn["named_requirements"] == ["PPN-1", "PPN-2", "PPN-3", "PPN-4"], "PPN named requirements")
    descent_ids = {
        item["id"]
        for block in descent["descents"].values()
        for item in block["interface"]
    }
    check(set(sf["named_requirements"]).issubset(descent_ids), "strong-field requirements resolve")
    check(set(ppn["named_requirements"]).issubset(descent_ids), "PPN requirements resolve")
    check("TARGET-BEFORE-EVALUATION" in sf["fc_failures"], "imported metric fails target-order rule")
    check("FC-1" in ppn["fc_failures"] and "FC-5" in ppn["fc_failures"], "granted PPN fails build and pathway")

    constructions = data["fitting_constructions"]
    check(len(constructions) == 1, "exactly one fitting construction")
    fc = constructions[0]
    check(fc["id"] == "FC-GR-ROTATION-EINSTEIN-WEYL-STATIC-1", "construction id")
    check(fc["grade"] == "FITTING_CONSTRUCTION", "construction grade")
    check(fc["rung"] == "R5", "construction rung")
    check(fc["construction_created_before_anchor"] is True, "pre-target chronology")
    dates = fc["construction_evidence_dates"]
    check(dates["H45"] < dates["anchor_acceptance"], "H45 predates anchor")
    check(dates["H49"] < dates["anchor_acceptance"], "H49 predates anchor")
    fc_criteria = fc.get("fc_criteria", {})
    check(list(fc_criteria) == FC_KEYS, "FC-1 through FC-7 complete and ordered")
    check("gamma-r" in fc_criteria.get("FC-7", ""), "nontriviality witness")
    check("P2" in fc["next_executable_gate"] and "before rotation comparison" in fc["next_executable_gate"], "target-frozen pathway gate")
    check("ambient K77 adapter explicitly unbuilt" in fc["fingerprint"]["signature_horn"], "structure transport gap explicit")
    check(data["input_currency"]["checked"] is True, "input currency checked")

    for key in (
        "ledger_verdict_change", "ledger_row_field_change", "source_ownership_change",
        "mechanism_commitment_change", "confirmation_credit_change",
        "canon_verdict_change", "public_posture_change",
    ):
        check(data[key] == "none", f"{key} none")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in result, "routing classification")
    check("```gu-typed-objects" in result, "typed objects")
    check("FC-1" in result and "FC-7" in result, "artifact carries full FC audit")
    check("does not construct a native stationary family" in flat_result, "strong-field non-admission prose")
    check("removing the granted reduction removes" in flat_result, "PPN non-admission prose")
    check("No ledger verdict" in result, "claim ceiling")

    state = inputs["state"]
    next_steps = inputs["next_steps"]
    research_status = inputs["research_status"]
    agenda_text = json.dumps(inputs["agenda"], sort_keys=True)
    assert isinstance(state, str) and isinstance(next_steps, str) and isinstance(research_status, str)
    check("FC-GR-ROTATION-EINSTEIN-WEYL-STATIC-1" in state, "current state pointer")
    check("FIRST FITTING CONSTRUCTION" in next_steps, "next steps announcement")
    check("First fitting construction" in research_status, "research status announcement")
    check("FC-GR-ROTATION-EINSTEIN-WEYL-STATIC-1" in agenda_text, "agenda pointer")
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
    changed["data"]["dispositions"][2]["bucket"] = "B2"
    mutations.append(("rotation-bucket-demotion", "LT-GR11 bucket", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["fitting_constructions"][0]["fc_criteria"].pop("FC-7")
    mutations.append(("fc7-drop", "FC-1 through FC-7 complete and ordered", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["fitting_constructions"][0]["construction_created_before_anchor"] = False
    mutations.append(("chronology-flip", "pre-target chronology", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["dispositions"][0]["named_requirements"] = ["needs-source-action"]
    mutations.append(("unnamed-b2", "strong-field named requirements", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["ledger_verdict_change"] = "LT-GR11->SAME"
    mutations.append(("ledger-smuggle", "ledger_verdict_change none", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`", "Classification: `REMOVED`"
    )
    mutations.append(("routing-drop", "routing classification", changed))

    changed = copy.deepcopy(baseline)
    changed["state"] = changed["state"].replace("FC-GR-ROTATION-EINSTEIN-WEYL-STATIC-1", "REMOVED")
    mutations.append(("state-pointer-drop", "current state pointer", changed))

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
