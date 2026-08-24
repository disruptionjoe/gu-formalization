#!/usr/bin/env python3
"""Executable certificate for the Higgs/anomaly/replication disposition wave."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REGISTRY = ROOT / "lab/process/higgs-anomaly-replication-row-disposition-wave.json"
SOURCE = ROOT / "lab/sources/source-claim-register.yaml"
RESULT = ROOT / "explorations/conditional-build/higgs-anomaly-replication-row-disposition-wave-2026-08-24.md"
EXPECTED_LEDGER_SHA256 = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def load_inputs() -> dict[str, object]:
    ledger_bytes = LEDGER.read_bytes()
    return {
        "ledger": json.loads(ledger_bytes),
        "ledger_sha256": hashlib.sha256(ledger_bytes).hexdigest(),
        "registry": json.loads(REGISTRY.read_text()),
        "source": SOURCE.read_text(),
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

    ledger = inputs["ledger"]
    registry = inputs["registry"]
    source = inputs["source"]
    result = inputs["result"]
    assert isinstance(ledger, dict) and isinstance(registry, dict)
    assert isinstance(source, str) and isinstance(result, str)

    rows = {row["id"]: row for row in ledger["rows"]}
    terminal = registry["terminal_rows"]
    terminal_ids = [row["row_id"] for row in terminal]
    expected_ids = {
        "AC-A1", "AC-A2", "AC-A3", "AC-A4", "AC-A6", "AC-A7",
        "AC-B1", "AC-B4", "AC-B5", "AC-C1", "AC-C2", "AC-F2",
        "RA-F2", "RA-E3", "RA-E4", "RA-E5", "RA-F3",
        "LT-SM3", "LT-SM4", "LT-SM6",
    }

    check(inputs["ledger_sha256"] == EXPECTED_LEDGER_SHA256,
          "ledger bytes remain frozen")
    check(registry["ledger_basis"]["sha256"] == EXPECTED_LEDGER_SHA256,
          "registry pins frozen ledger")
    check(set(terminal_ids) == expected_ids and len(terminal_ids) == 20,
          "exact twenty-row terminal set")
    check(len(terminal_ids) == len(set(terminal_ids)), "terminal rows are unique")
    check(all(row_id in rows for row_id in terminal_ids), "terminal rows exist in ledger")
    check(all(rows[row_id]["verdict"] == ("SAME" if row_id.startswith("AC-") or row_id == "RA-F2" else "DIFFERS")
              for row_id in terminal_ids), "original ledger verdict classes are preserved")

    constructions = {item["id"]: item for item in registry["fitting_constructions"]}
    expected_constructions = {
        "FC-ANOMALY-LOCAL-C1-KERNEL-1",
        "FC-ANOMALY-GLOBAL-RECEPTACLE-1",
        "FC-ANOMALY-OBSERVED-BLOCK-BALANCE-1",
        "FC-REP-TRACEQ-H640-REPLICA-1",
    }
    check(set(constructions) == expected_constructions, "exact four fitting constructions")
    check(all(set(item["fc_criteria"]) == {f"FC-{index}" for index in range(1, 8)}
              and all(item["fc_criteria"].values()) for item in constructions.values()),
          "all FC-1 through FC-7 criteria pass")
    check(all(len(item["fingerprint"]) == 6 for item in constructions.values()),
          "fitting fingerprints are complete")
    check(all(item["pathway"] and item["demotion"] and item["nontriviality"]
              for item in constructions.values()),
          "pathway demotion and nontriviality are explicit")

    impossibilities = {item["id"]: item for item in registry["precise_impossibilities"]}
    check(set(impossibilities) == {
        "PI-RANK2-INTERNAL-HIGGS-SCALAR-1",
        "PI-KINEMATIC-BLOCKS-AS-THREE-GENERATIONS-1",
    }, "exact two precise impossibilities")
    check(all(item["class"] and item["certificate"] and item["escape"]
              and item["resurrection_trigger"] and item["claim_ceiling"]
              for item in impossibilities.values()),
          "impossibility boundaries are complete")
    check("zero Higgs doublets" in impossibilities[
        "PI-RANK2-INTERNAL-HIGGS-SCALAR-1"]["certificate"],
          "rank-two scalar-host certificate is exact")
    check("no nonzero chiral index" in impossibilities[
        "PI-KINEMATIC-BLOCKS-AS-THREE-GENERATIONS-1"]["certificate"],
          "decomposition-count certificate is typed")

    b1 = [row for row in terminal if row["terminal_outcome"] == "FITTING_CONSTRUCTION"]
    b2 = [row for row in terminal if row["terminal_outcome"] == "B2_NAMED_REQUIREMENT"]
    precise = [row for row in terminal if row["terminal_outcome"] == "PRECISE_IMPOSSIBILITY"]
    check(len(b1) == 13 and len(b2) == 5 and len(precise) == 2,
          "terminal distribution is 13 B1 5 B2 2 PI")
    check(all(row.get("construction_id") in constructions for row in b1),
          "every B1 row resolves to a fitting construction")
    check(all(row.get("named_requirements") for row in b2),
          "every B2 row names requirements")
    check(all(row.get("impossibility_id") in impossibilities for row in precise),
          "every PI row resolves to a certificate")

    requirements = registry["requirements"]
    check(all(req in requirements for row in b2 for req in row["named_requirements"]),
          "all named requirements resolve")
    check(all(item["owner"] and item["object"] for item in requirements.values()),
          "every requirement names owner and object")

    for claim_id in registry["source_claims_checked"]:
        check(f"id: {claim_id}" in source, f"source claim exists: {claim_id}")
    check("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in result,
          "artifact declares routing classification")
    check("```gu-typed-objects" in result and "MAP-TYPE=evaluation" in result,
          "artifact carries typed-object block")
    check(registry["target_claim"] == "NONE-NOT-A-KILL",
          "kill language does not target a source claim")
    check(all(registry[key] == "none" for key in (
        "ledger_verdict_change", "ledger_row_field_change", "source_ownership_change",
        "prediction_or_confirmation_change", "claim_status_change",
        "canon_verdict_change", "public_posture_change")),
          "all protected movement fields remain none")
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
    changed["ledger_sha256"] = "stale"
    mutations.append(("ledger-moved", "ledger bytes remain frozen", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["terminal_rows"].pop()
    mutations.append(("row-missing", "exact twenty-row terminal set", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["fitting_constructions"][0]["fc_criteria"]["FC-7"] = False
    mutations.append(("fc7-failed", "all FC-1 through FC-7 criteria pass", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["precise_impossibilities"][0]["escape"] = ""
    mutations.append(("pi-unbounded", "impossibility boundaries are complete", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["terminal_rows"][15]["named_requirements"] = []
    mutations.append(("b2-unnamed", "every B2 row names requirements", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["source_claims_checked"].append("SC-MISSING")
    mutations.append(("source-missing", "source claim exists: SC-MISSING", changed))
    changed = copy.deepcopy(baseline)
    changed["result"] = changed["result"].replace(
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`", "Classification: omitted")
    mutations.append(("routing-omitted", "artifact declares routing classification", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["public_posture_change"] = "strengthened"
    mutations.append(("posture-moved", "all protected movement fields remain none", changed))

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
