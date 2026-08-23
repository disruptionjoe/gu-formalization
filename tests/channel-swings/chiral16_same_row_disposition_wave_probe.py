#!/usr/bin/env python3
"""Regression probe for the chiral-16 SAME-row disposition wave."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REGISTRY = ROOT / "lab/process/chiral16-same-row-disposition-wave.json"
RESULT = ROOT / "explorations/conditional-build/chiral16-same-row-disposition-wave-2026-08-23.md"

G_EMB = {"RA-A3", "RA-B1", "RA-B2", "RA-B3", "RA-B4", "RA-B5"}
G_SHADOW = {"AC-D1", "AC-D2", "AC-D3", "AC-D4", "AC-D5"}
ALL_ROWS = G_EMB | G_SHADOW
LEDGER_SHA256 = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def load_inputs() -> dict[str, object]:
    ledger_bytes = LEDGER.read_bytes()
    ledger = json.loads(ledger_bytes)
    return {
        "ledger_sha256": hashlib.sha256(ledger_bytes).hexdigest(),
        "rows": {row["id"]: row for row in ledger["rows"]},
        "registry": json.loads(REGISTRY.read_text()),
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

    rows = inputs["rows"]
    registry = inputs["registry"]
    result = inputs["result"]
    assert isinstance(rows, dict) and isinstance(registry, dict) and isinstance(result, str)

    check(inputs["ledger_sha256"] == LEDGER_SHA256, "ledger v0.263 byte identity")
    check(registry["ledger_basis"]["sha256"] == LEDGER_SHA256,
          "registry pins ledger identity")
    check(registry["status"].startswith("ELEVEN_B2_NAMED_REQUIREMENT_TERMINALS"),
          "eleven-terminal result status")
    check(registry["target_claim"] == "NONE-NOT-A-KILL", "not-a-kill target typing")
    check(registry["layer0"]["routing_classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
          "Layer-0 routing classification")
    check(registry["layer0"]["relation"] == "UNTYPED_MISSING_OBSERVATION_ACTION_BRIDGE",
          "missing bridge remains explicit")

    groups = {group["id"]: group for group in registry["row_groups"]}
    check(set(groups) == {"G-EMB", "G-SHADOW"}, "two shared grant groups")
    check(set(groups["G-EMB"]["rows"]) == G_EMB, "G-EMB row set")
    check(set(groups["G-SHADOW"]["rows"]) == G_SHADOW, "G-SHADOW row set")
    check(groups["G-EMB"]["named_requirements"] == ["U1-1", "U1-2", "U1-3"],
          "G-EMB exact requirements")
    check(groups["G-SHADOW"]["named_requirements"] == ["AD4-1", "AD4-2", "AD4-3"],
          "G-SHADOW exact requirements")
    check(all(group["bucket"] == "B2" for group in groups.values()),
          "both groups are B2")
    check(all(group["terminal_outcome"] == "B2_NAMED_REQUIREMENT"
              for group in groups.values()), "both groups use terminal B2 vocabulary")
    check(all(set(group["fc_failures"]) == {"FC-1", "FC-7", "TARGET-BEFORE-EVALUATION"}
              for group in groups.values()), "FC failures are explicit")

    requirements = registry["requirements"]
    check(set(requirements) == {"U1-1", "U1-2", "U1-3", "AD4-1", "AD4-2", "AD4-3"},
          "complete named-requirement vocabulary")
    check(requirements["U1-1"]["owner"] == "OWNER-A", "stationary-action owner")
    check(requirements["U1-3"]["owner"] == "OWNER-D", "observation-transport owner")
    check(requirements["AD4-1"]["owner"] == "OWNER-A+OWNER-D",
          "physical-carrier joint owners")
    check(requirements["AD4-3"]["owner"] == "OWNER-B", "anomaly evaluator owner")

    terminal = {row["row_id"]: row for row in registry["terminal_rows"]}
    check(set(terminal) == ALL_ROWS, "exact eleven terminal rows")
    check(len(registry["terminal_rows"]) == len(terminal), "terminal rows are unique")
    check(all(row["bucket"] == "B2" for row in terminal.values()),
          "every terminal row is B2")
    check(all(row["terminal_outcome"] == "B2_NAMED_REQUIREMENT"
              for row in terminal.values()), "every row names terminal B2 outcome")
    check(all(row["named_requirements"] for row in terminal.values()),
          "every terminal row names requirements")
    check(all(terminal.get(row_id, {}).get("named_requirements") == ["U1-1", "U1-2", "U1-3"]
              for row_id in G_EMB), "G-EMB per-row requirements")
    check(all(terminal.get(row_id, {}).get("named_requirements") == ["AD4-1", "AD4-2", "AD4-3"]
              for row_id in G_SHADOW), "G-SHADOW per-row requirements")

    for row_id in sorted(ALL_ROWS):
        check(rows[row_id]["verdict"] == "SAME", f"ledger verdict preserved: {row_id}")
    check(all(rows[row_id]["reason_kind"] == "DERIVED_CONDITIONAL" for row_id in G_EMB),
          "G-EMB conditional grade preserved")
    check(all(rows[row_id]["reason_kind"] == "DERIVED_CONDITIONAL" for row_id in G_SHADOW),
          "G-SHADOW conditional grade preserved")

    pi = registry["bounded_precise_impossibility"]
    cert = pi["certificate"]
    check(pi["id"] == "PI-4D-ANOMALY-SELECTOR-CHIRAL16-1",
          "bounded impossibility id")
    check(cert["rank"] == 4, "anomaly matrix rank four")
    check(cert["relation"] == "2 D1 - 27 D2 - 36 D3 - 9 D4 + 9 D5 = 0",
          "exact anomaly relation")
    check(cert["integer_kernel"] == "Z*(15 of SU(5)) + Z*(nu^c)",
          "exact saturated kernel")
    check(cert["saturated"] and cert["negation_closed"] and cert["contains_zero"],
          "kernel blindness properties")
    check("source-native physical carrier" in pi["escape"], "bounded escape named")
    check("kills only the anomaly-selector inference" in pi["claim_ceiling"],
          "impossibility ceiling")

    flat = re.sub(r"\s+", " ", result)
    check("GU-COMPARATOR-ROUTING — scope before inference." in flat,
          "routing notice present")
    check("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in result,
          "routing classification present")
    check("```gu-typed-objects" in result, "typed-object block present")
    check("The bounded impossibility is not the terminal token" in flat,
          "impossibility versus B2 boundary")
    check("Eleven ledger rows now have evidence-backed terminal dispositions" in flat,
          "result states terminal effect")
    check("no source claim, physical carrier or GU theory class is killed" in
          registry["target_claim_note"], "no source-theory kill")

    for field in (
        "ledger_verdict_change", "ledger_row_field_change", "source_ownership_change",
        "prediction_or_confirmation_change", "claim_status_change",
        "canon_verdict_change", "public_posture_change",
    ):
        check(registry[field] == "none", f"no prohibited movement: {field}")
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
    changed["registry"]["terminal_rows"].pop()
    mutations.append(("terminal-dropped", "exact eleven terminal rows", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["row_groups"][0]["named_requirements"] = ["source action"]
    mutations.append(("generic-b2", "G-EMB exact requirements", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["bounded_precise_impossibility"]["certificate"]["rank"] = 5
    mutations.append(("rank-inflated", "anomaly matrix rank four", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["bounded_precise_impossibility"]["certificate"]["negation_closed"] = False
    mutations.append(("chirality-blindness-dropped", "kernel blindness properties", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["layer0"]["routing_classification"] = "SOURCE_NATIVE_ROUTE"
    mutations.append(("comparator-laundered", "Layer-0 routing classification", changed))

    changed = copy.deepcopy(baseline)
    changed["rows"]["AC-D1"]["verdict"] = "NEEDS"
    mutations.append(("ledger-moved", "ledger verdict preserved: AC-D1", changed))

    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace("```gu-typed-objects", "```objects", 1)
    mutations.append(("typed-block-dropped", "typed-object block present", changed))

    changed = copy.deepcopy(baseline)
    changed["registry"]["public_posture_change"] = "changed"
    mutations.append(("posture-moved", "no prohibited movement: public_posture_change", changed))

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
