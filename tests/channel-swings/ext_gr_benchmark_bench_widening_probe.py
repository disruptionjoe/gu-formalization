#!/usr/bin/env python3
"""Propagation and failure-path probe for the R6 gravitational bench widening."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/ext-gr-benchmark-bench-registry.json"
RESULT = ROOT / "explorations/ext-gr-benchmark-bench-widening-council-2026-08-23.md"
DELTA = ROOT / "lab/process/conditional-evidence-deltas/gu-ext-gr-bench-widening-2026-08-23.json"

CITED_RECORD_FILES = (
    "explorations/W225-gravity-projected-shadow-schwarzschild-cheap-read-2026-07-15.md",
    "explorations/W220-falsify-ppn-weak-field-2026-07-14.md",
    "explorations/recovery-nogo-gr-w229-swing3-adjudication-2026-07-16.md",
    "GEOMETER-VS-PHYSICS-OBJECTS.md",
)

# Claim-forms only: phrases that cannot occur as a quoted-and-rejected
# overclaim, so their presence is always a genuine summary-grammar regression.
FORBIDDEN_SUMMARY_GRAMMAR = (
    "GU passes the benchmark",
    "confirms GU's gravity",
    "prediction credit is awarded",
    "the benchmark is discharged",
)

EXPECTED_IDS = ["EXT-GR-STRONGFIELD", "EXT-GR-PPN", "EXT-GR-ROTATION"]


def load_inputs() -> dict[str, object]:
    return {
        "data": json.loads(REGISTRY.read_text()),
        "result": RESULT.read_text(),
        "delta": json.loads(DELTA.read_text()),
        "state": (ROOT / "CURRENT-STATE.yaml").read_text(),
        "next_steps": (ROOT / "NEXT-STEPS.md").read_text(),
        "records_exist": {name: (ROOT / name).exists() for name in CITED_RECORD_FILES},
        "geometer": (ROOT / "GEOMETER-VS-PHYSICS-OBJECTS.md").read_text(),
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
    delta = inputs["delta"]
    state = inputs["state"]
    next_steps = inputs["next_steps"]
    records = inputs["records_exist"]
    geometer = inputs["geometer"]
    assert isinstance(data, dict) and isinstance(delta, dict) and isinstance(records, dict)
    assert isinstance(result, str) and isinstance(state, str) and isinstance(next_steps, str)
    assert isinstance(geometer, str)

    rows = {row["id"]: row for row in data["benchmarks"]}
    check(list(rows) == EXPECTED_IDS, "three anchors in order")
    for rid in EXPECTED_IDS:
        row = rows.get(rid, {})
        check(row.get("status") == "ACCEPTED_AS_SCOPED_REVERSE_SCAFFOLD_TARGET", f"{rid} accepted-as-scoped")
        check(row.get("gu_realization_status") == "MISSING_CONSTRUCTION", f"{rid} realization missing")
        check(row.get("mechanism_commitment") == "NONE", f"{rid} mechanism NONE")
        check(row.get("confirmation_credit") == "NONE", f"{rid} confirmation NONE")
        check(bool(row.get("claim_ceiling")), f"{rid} claim ceiling present")
        check(len(row.get("required_separations", [])) >= 2, f"{rid} separations present")

    check("2.3e-5" in rows["EXT-GR-PPN"]["statement"], "PPN Cassini bound recorded")
    check("granted" in rows["EXT-GR-PPN"]["recorded_state"], "PPN pass typed conditional")
    check("BOUNDED_NO_GO" in rows["EXT-GR-STRONGFIELD"]["recorded_state"], "W229 no-go cited")
    check("O(M^2/r^4)" in rows["EXT-GR-STRONGFIELD"]["recorded_state"], "W225 residual order recorded")
    check("H49" in rows["EXT-GR-ROTATION"]["recorded_state"], "H49 cited")
    check("no dark-matter claim" in " ".join(rows["EXT-GR-ROTATION"]["required_separations"]),
          "rotation anchor excludes dark-matter position")
    check(data["acceptance_authority"].startswith("Joe direct chat 2026-08-23"), "acceptance authority recorded")
    check(data["pattern"] == "EXT-J95-SEMI-CLASSICAL-HORIZON", "EXT-J95 pattern named")
    check(data["proposed_ledger_rows"] == ["LT-GR9", "LT-GR10", "LT-GR11"], "proposed rows named")
    check(data["ledger_verdict_change"] == "none", "ledger unchanged")
    check(data["canon_verdict_change"] == "none", "canon unchanged")

    for name, exists in records.items():
        check(exists, f"cited record exists: {name}")
    check("H49" in geometer and "|II|^2" in geometer, "geometer table carries H49 survivor row")

    check(delta["status"] == "pending", "delta pending")
    check(delta["affected_rows"] == ["LT-GR9", "LT-GR10", "LT-GR11"], "delta rows")
    check(delta["integration"] is None, "delta not self-integrated")
    check("Verdict changes: none" in delta["proposed_effect"]["summary"], "delta requests no verdict change")

    check("GU-COMPARATOR-ROUTING" in result, "routing notice")
    check("GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY" in result, "routing class")
    check("```gu-typed-objects" in result, "typed objects")
    check("7-0" in result, "council disposition recorded")
    check("does not exist" in result or "which does not exist" in result, "PPN discharge ceiling in doc")
    check("MISSING_CONSTRUCTION" in result, "realization obligation in doc")
    for phrase in FORBIDDEN_SUMMARY_GRAMMAR:
        check(phrase not in result, f"forbidden grammar absent: {phrase}")

    check("EXT-GR-STRONGFIELD" in state and "EXT-GR-ROTATION" in state, "state records anchors")
    check("R6 BENCH" in next_steps or "R6 bench" in next_steps, "next steps announcement")
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
    changed["data"]["benchmarks"][0]["gu_realization_status"] = "RECOVERED"
    mutations.append(("recovery-smuggle", "EXT-GR-STRONGFIELD realization missing", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["benchmarks"][1]["recorded_state"] = "W220 SURVIVES unconditionally"
    mutations.append(("conditionality-drop", "PPN pass typed conditional", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["benchmarks"][2]["required_separations"] = ["rotation-curve consistency versus derivation"]
    mutations.append(("dark-matter-guard-drop", "rotation anchor excludes dark-matter position", changed))

    changed = copy.deepcopy(baseline)
    changed["data"]["benchmarks"][0]["mechanism_commitment"] = "GR_MECHANISM"
    mutations.append(("mechanism-smuggle", "EXT-GR-STRONGFIELD mechanism NONE", changed))

    changed = copy.deepcopy(baseline)
    changed["records_exist"] = dict(changed["records_exist"])
    changed["records_exist"]["explorations/W220-falsify-ppn-weak-field-2026-07-14.md"] = False
    mutations.append(("cited-record-missing", "cited record exists: explorations/W220-falsify-ppn-weak-field-2026-07-14.md", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY",
        "GU-COMPARATOR-ROUTING-CLASSIFICATION: REMOVED",
    )
    mutations.append(("routing-regression", "routing class", changed))

    # Planted positive: the forbidden-grammar detector must fire on an injected claim.
    changed = copy.deepcopy(baseline)
    changed["result"] += "\nWith W220 in hand, GU passes the benchmark.\n"
    mutations.append(("planted-forbidden-grammar", "forbidden grammar absent: GU passes the benchmark", changed))

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
