#!/usr/bin/env python3
"""Exact and mutation-tested checks for the stale-fork/vacuum disposition wave."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG_PATH = ROOT / "lab/process/overdetermined-vacuum-stabilizer-row-disposition-wave.json"
LIVE_PATH = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"
LEDGER_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REPORT_PATH = ROOT / "explorations/conditional-build/overdetermined-vacuum-stabilizer-row-disposition-wave-2026-08-24.md"

ROWS = ["LT-GR4", "LT-SM3b", "AC-G1", "RA-A1", "RA-A2", "RA-A6", "RA-A8", "RA-E6", "RA-G4"]
B2 = {
    "RA-A1": ["VAC-1", "VAC-2", "VAC-3"],
    "RA-A2": ["VAC-1", "VAC-2", "VAC-3"],
    "RA-A6": ["SMG-1", "SMG-2", "SMG-3"],
    "RA-A8": ["VAC-1", "VAC-2", "VAC-3"],
    "RA-E6": ["HPH-1", "HPH-2", "HPH-3"],
    "RA-G4": ["VAC-1", "VAC-3", "VAC-4"],
}
PIS = {
    "LT-GR4": "PI-PORTED-NEGATIVE-R2-SIGN-NATIVE-STABILITY-1",
    "LT-SM3b": "PI-PURE-CONTRACTION-CONSTRAINT-PRESERVING-SLOT-1",
    "AC-G1": "PI-K95-SP64-AS-K77-REPLACEMENT-1",
}
LEDGER_SHA = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate(reg: dict, live: dict, report: str, ledger_bytes: bytes) -> list[str]:
    errors: list[str] = []
    terminal = reg.get("terminal_rows", [])
    by_row = {x.get("row_id"): x for x in terminal}
    if list(by_row) != ROWS or len(terminal) != 9 or len(by_row) != 9:
        errors.append("terminal row order/coverage mismatch")

    source_evidence = reg.get("source_evidence", {})
    if set(source_evidence) != set(ROWS):
        errors.append("source evidence row coverage mismatch")
    for row, refs in source_evidence.items():
        if not refs or any(not (ROOT / ref).is_file() for ref in refs):
            errors.append(f"{row} source evidence does not resolve")

    for row, reqs in B2.items():
        item = by_row.get(row, {})
        if item.get("bucket") != "B2" or item.get("terminal_outcome") != "B2_NAMED_REQUIREMENT":
            errors.append(f"{row} is not exact B2 terminal")
        if item.get("named_requirements") != reqs:
            errors.append(f"{row} named requirements mismatch")
    for row, pi_id in PIS.items():
        item = by_row.get(row, {})
        if item.get("bucket") != "B4" or item.get("terminal_outcome") != "PRECISE_IMPOSSIBILITY":
            errors.append(f"{row} is not bounded impossibility terminal")
        if item.get("impossibility_id") != pi_id:
            errors.append(f"{row} impossibility id mismatch")

    requirement_defs = reg.get("named_requirements", {})
    expected_reqs = {r for reqs in B2.values() for r in reqs}
    if set(requirement_defs) != expected_reqs or any(not requirement_defs[x].strip() for x in expected_reqs):
        errors.append("named requirement definitions incomplete")

    impossibilities = reg.get("precise_impossibilities", [])
    by_pi = {x.get("id"): x for x in impossibilities}
    if set(by_pi) != set(PIS.values()):
        errors.append("precise impossibility coverage mismatch")
    for pi_id, item in by_pi.items():
        for field in ("class", "assumptions", "witness", "escape", "resurrection_trigger", "target_claim"):
            if not item.get(field):
                errors.append(f"{pi_id} missing {field}")
        if len(item.get("assumptions", [])) < 2:
            errors.append(f"{pi_id} needs at least two typed assumptions")
    acg1 = by_pi.get(PIS["AC-G1"], {})
    if "AC-G1a" not in str(acg1.get("escape", "")):
        errors.append("AC-G1 must preserve successor AC-G1a")

    effects = reg.get("protected_effects", {})
    if not effects or any(value is not False for value in effects.values()):
        errors.append("protected effects must all remain false")
    actual_sha = hashlib.sha256(ledger_bytes).hexdigest()
    if actual_sha != LEDGER_SHA or reg.get("ledger_basis", {}).get("sha256") != LEDGER_SHA:
        errors.append("ledger v0.263 identity moved")

    live_terminal = {x.get("row_id"): x for x in live.get("terminal_row_dispositions", [])}
    for row in ROWS:
        if row not in live_terminal:
            errors.append(f"live register missing {row}")
    for cohort in live.get("open_row_cohorts", []):
        if cohort.get("ledger_verdict") == "OVER_DETERMINED" and cohort.get("row_ids"):
            errors.append("OVER_DETERMINED cohort must be empty after complete wave")
    exhausted = live.get("exhaustion_evaluation", {})
    for key, value in {"denominator_rows": 91, "terminal_rows": 68, "open_rows": 23, "exhausted": False, "b2_selectable": False}.items():
        if exhausted.get(key) != value:
            errors.append(f"live register {key} mismatch")

    required_report = [
        "GU-COMPARATOR-ROUTING",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "```gu-typed-objects",
        "Successor `AC-G1a` remains open",
        "68 terminal and 23 open rows",
        "No impossibility is a GU verdict",
    ]
    for token in required_report:
        if token not in report:
            errors.append(f"report missing {token}")
    return errors


def baseline() -> tuple[dict, dict, str, bytes]:
    return load(REG_PATH), load(LIVE_PATH), REPORT_PATH.read_text(encoding="utf-8"), LEDGER_PATH.read_bytes()


def selftest(reg: dict, live: dict, report: str, ledger: bytes) -> list[str]:
    mutations = []
    m = copy.deepcopy(reg); m["terminal_rows"].pop(); mutations.append((m, live, report, ledger, "row coverage"))
    m = copy.deepcopy(reg); m["source_evidence"]["RA-A1"] = ["missing.md"]; mutations.append((m, live, report, ledger, "source resolution"))
    m = copy.deepcopy(reg); m["terminal_rows"][3]["named_requirements"] = ["VAC-1"]; mutations.append((m, live, report, ledger, "requirements"))
    m = copy.deepcopy(reg); m["precise_impossibilities"][0]["escape"] = ""; mutations.append((m, live, report, ledger, "escape"))
    m = copy.deepcopy(reg); m["precise_impossibilities"][2]["escape"] = "replacement open"; mutations.append((m, live, report, ledger, "successor"))
    m = copy.deepcopy(reg); m["protected_effects"]["ledger_verdict_change"] = True; mutations.append((m, live, report, ledger, "protected effect"))
    m = copy.deepcopy(live); m["exhaustion_evaluation"]["terminal_rows"] = 67; mutations.append((reg, m, report, ledger, "counts"))
    m = copy.deepcopy(live); m["open_row_cohorts"][2]["row_ids"] = ["AC-G1"]; mutations.append((reg, m, report, ledger, "open overdetermined"))
    mutations.append((reg, live, report.replace("No impossibility is a GU verdict", ""), ledger, "report ceiling"))
    missed = [name for r, l, p, b, name in mutations if not evaluate(r, l, p, b)]
    return missed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    reg, live, report, ledger = baseline()
    errors = evaluate(reg, live, report, ledger)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: stale-fork and vacuum/stabilizer disposition wave")
    if args.selftest:
        missed = selftest(reg, live, report, ledger)
        if missed:
            print("FAIL selftest: " + ", ".join(missed))
            return 1
        print("PASS selftest: 9/9 mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
