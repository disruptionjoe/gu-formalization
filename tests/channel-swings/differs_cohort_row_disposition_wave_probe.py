#!/usr/bin/env python3
"""Exact and mutation-tested checks for the complete DIFFERS disposition wave."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG_PATH = ROOT / "lab/process/differs-cohort-row-disposition-wave.json"
LIVE_PATH = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"
LEDGER_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REPORT_PATH = ROOT / "explorations/conditional-build/differs-cohort-row-disposition-wave-2026-08-24.md"

ROWS = ["RA-A4", "RA-A5", "RA-B6", "RA-D2", "RA-G1", "RA-G2", "AC-A5", "AC-F3", "AC-F4", "AC-G2"]
B2 = {
    "RA-A4": ["XU1-1", "XU1-2", "XU1-3"],
    "RA-A5": ["EXG-1", "EXG-2", "EXG-3"],
    "RA-B6": ["NU-1", "NU-2", "NU-3"],
    "RA-G1": ["RS-1", "RS-2", "RS-3"],
    "RA-G2": ["MIR-1", "MIR-2", "MIR-3"],
}
PIS = {
    "RA-D2": "PI-EQUIVARIANT-MASS-SPLIT-CHIRALITY-1",
    "AC-A5": "PI-NET-CHIRALITY-ALONE-LOCAL-ANOMALY-1",
    "AC-F3": "PI-LOCAL-ZERO-ANOMALY-INFLOW-Z3-BRIDGE-1",
    "AC-F4": "PI-SPIN-BORDISM-3PRIMARY-COUNT-1",
    "AC-G2": "PI-GAUGE-OCTIC-PREMISE-NECESSITY-1",
}
LEDGER_SHA = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate(reg: dict, live: dict, report: str, ledger_bytes: bytes) -> list[str]:
    errors: list[str] = []
    terminal = reg.get("terminal_rows", [])
    by_row = {x.get("row_id"): x for x in terminal}
    if list(by_row) != ROWS:
        errors.append("terminal row order/coverage mismatch")
    if len(terminal) != 10 or len(by_row) != 10:
        errors.append("terminal rows must be ten unique rows")

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
    d2 = by_pi.get(PIS["RA-D2"], {})
    if d2.get("target_claim") != "SC-CHI-51" or not str(d2.get("target_claim_verdict", "")).startswith("NOT_KILLED"):
        errors.append("RA-D2 must preserve SC-CHI-51")

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
        if cohort.get("ledger_verdict") == "DIFFERS" and cohort.get("row_ids"):
            errors.append("DIFFERS cohort must be empty after complete wave")
    exhausted = live.get("exhaustion_evaluation", {})
    for key, value in {"denominator_rows": 91, "terminal_rows": 59, "open_rows": 32, "exhausted": False, "b2_selectable": False}.items():
        if exhausted.get(key) != value:
            errors.append(f"live register {key} mismatch")

    required_report = [
        "GU-COMPARATOR-ROUTING",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "```gu-typed-objects",
        "`SC-CHI-51` remains `NOT_KILLED`",
        "59 terminal and 32 open rows",
        "No impossibility\nis a GU verdict",
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
    m = copy.deepcopy(reg); m["source_evidence"]["RA-A4"] = ["missing.md"]; mutations.append((m, live, report, ledger, "source resolution"))
    m = copy.deepcopy(reg); m["terminal_rows"][0]["named_requirements"] = ["XU1-1"]; mutations.append((m, live, report, ledger, "requirements"))
    m = copy.deepcopy(reg); m["precise_impossibilities"][0]["escape"] = ""; mutations.append((m, live, report, ledger, "escape"))
    m = copy.deepcopy(reg); m["precise_impossibilities"][0]["target_claim_verdict"] = "KILLED"; mutations.append((m, live, report, ledger, "claim ceiling"))
    m = copy.deepcopy(reg); m["protected_effects"]["ledger_verdict_change"] = True; mutations.append((m, live, report, ledger, "protected effect"))
    m = copy.deepcopy(live); m["exhaustion_evaluation"]["terminal_rows"] = 58; mutations.append((reg, m, report, ledger, "counts"))
    m = copy.deepcopy(live); m["open_row_cohorts"][1]["row_ids"] = ["AC-F3"]; mutations.append((reg, m, report, ledger, "open differs"))
    mutations.append((reg, live, report.replace("No impossibility\nis a GU verdict", ""), ledger, "report ceiling"))
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
    print("PASS: complete DIFFERS disposition wave")
    if args.selftest:
        missed = selftest(reg, live, report, ledger)
        if missed:
            print("FAIL selftest: " + ", ".join(missed))
            return 1
        print("PASS selftest: 9/9 mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
