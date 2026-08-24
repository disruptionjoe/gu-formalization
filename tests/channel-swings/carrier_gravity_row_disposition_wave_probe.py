#!/usr/bin/env python3
"""Probe the carrier/gravity terminal-disposition wave and its claim ceilings."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REGISTRY = ROOT / "lab/process/carrier-gravity-row-disposition-wave.json"
SOURCE = ROOT / "lab/sources/source-claim-register.yaml"
RESULT = ROOT / "explorations/conditional-build/carrier-gravity-row-disposition-wave-2026-08-24.md"
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
        "RA-A7", "RA-B7", "RA-B8", "RA-B9", "RA-C1", "RA-D3",
        "LT-GR1b", "LT-GR2a", "LT-GR3", "LT-GR5", "LT-GR6",
    }

    check(inputs["ledger_sha256"] == EXPECTED_LEDGER_SHA256, "ledger bytes remain frozen")
    check(registry["ledger_basis"]["sha256"] == EXPECTED_LEDGER_SHA256,
          "registry pins frozen ledger")
    check(set(terminal_ids) == expected_ids and len(terminal_ids) == 11,
          "exact eleven-row terminal set")
    check(len(terminal_ids) == len(set(terminal_ids)), "terminal rows are unique")
    check(all(row_id in rows for row_id in terminal_ids), "terminal rows exist in ledger")
    check(all(rows[row_id]["verdict"] == ("SAME" if row_id.startswith("RA-") else "DIFFERS")
              for row_id in terminal_ids), "original ledger verdict classes are preserved")

    constructions = {row["id"]: row for row in registry["fitting_constructions"]}
    check(set(constructions) == {"FC-REP-OBSERVED-NORMAL-WEYL16-1",
                                 "FC-GR-MOVING-AUGMENTED-TORSION-1"},
          "exact two fitting constructions")
    check(all(set(row["fc_criteria"].values()) == {True} for row in constructions.values()),
          "all FC-1 through FC-7 criteria pass")
    check(all(len(row["fingerprint"]) == 6 for row in constructions.values()),
          "fitting fingerprints are complete")
    check(all(row["pathway"] and row["demotion"] and row["nontriviality"]
              for row in constructions.values()), "pathway demotion and nontriviality are explicit")

    impossibilities = {row["id"]: row for row in registry["precise_impossibilities"]}
    check(set(impossibilities) == {"PI-D14-SAME-CHIRALITY-SCALAR-1",
                                  "PI-FIXED-LAMBDA-G-AS-VARIABLE-THETA-1"},
          "exact two precise impossibilities")
    check(all(row["class"] and row["certificate"] and row["escape"]
              and row["resurrection_trigger"] and row["claim_ceiling"]
              for row in impossibilities.values()), "impossibility boundaries are complete")
    check("Hom_Spin(S+ tensor S+, Lambda^0)=0" in impossibilities[
        "PI-D14-SAME-CHIRALITY-SCALAR-1"]["certificate"],
          "same-chirality scalar certificate is exact")
    check("no field variation" in impossibilities[
        "PI-FIXED-LAMBDA-G-AS-VARIABLE-THETA-1"]["certificate"],
          "fixed-versus-field certificate is typed")

    b1 = [row for row in terminal if row["terminal_outcome"] == "FITTING_CONSTRUCTION"]
    b2 = [row for row in terminal if row["terminal_outcome"] == "B2_NAMED_REQUIREMENT"]
    pi = [row for row in terminal if row["terminal_outcome"] == "PRECISE_IMPOSSIBILITY"]
    check(len(b1) == 5 and len(b2) == 4 and len(pi) == 2,
          "terminal outcome distribution is 5 B1 4 B2 2 PI")
    check(all(row.get("construction_id") in constructions for row in b1),
          "every B1 row resolves to a fitting construction")
    check(all(row.get("named_requirements") for row in b2),
          "every B2 row names requirements")
    check(all(row.get("impossibility_id") in impossibilities for row in pi),
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
    mutations.append(("row-missing", "exact eleven-row terminal set", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["fitting_constructions"][0]["fc_criteria"]["FC-7"] = False
    mutations.append(("fc7-failed", "all FC-1 through FC-7 criteria pass", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["precise_impossibilities"][0]["escape"] = ""
    mutations.append(("pi-unbounded", "impossibility boundaries are complete", changed))
    changed = copy.deepcopy(baseline)
    changed["registry"]["terminal_rows"][4]["named_requirements"] = []
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
