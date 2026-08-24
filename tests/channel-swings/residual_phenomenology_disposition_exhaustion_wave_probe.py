#!/usr/bin/env python3
"""Exact and mutation-tested checks for residual row dispositions and exhaustion."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG_PATH = ROOT / "lab/process/residual-phenomenology-disposition-exhaustion-wave.json"
LIVE_PATH = ROOT / "lab/process/phenomenology-disposition-register-v0.1.json"
LEDGER_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.263.json"
REPORT_PATH = ROOT / "explorations/conditional-build/residual-phenomenology-disposition-exhaustion-wave-2026-08-24.md"

ROWS = ["LT-GR2d", "LT-GR2e", "LT-GR7", "LT-GR8", "LT-SM1", "LT-SM1a", "LT-SM1b", "LT-SM2", "LT-SM7", "AC-B2", "AC-F5"]
B2 = {
    "LT-GR2d": ["COS-NORM-1", "COS-NORM-2", "COS-NORM-3"],
    "LT-GR2e": ["COS-FWD-1", "COS-FWD-2", "COS-FWD-3"],
    "LT-GR7": ["ABS-1"],
    "LT-GR8": ["JAC-1", "JAC-2", "JAC-3", "JAC-4", "JAC-5", "JAC-6"],
    "LT-SM1a": ["YM-HORN-1"],
    "LT-SM1b": ["YM-BRANCH-1", "YM-NORM-1"],
    "LT-SM2": ["YM-BRANCH-1", "YM-NORM-1", "YM-THRESH-1"],
    "LT-SM7": ["TOP-1", "TOP-2", "TOP-3"],
    "AC-B2": ["BORD-1", "BORD-2"],
    "AC-F5": ["CNT-1", "CNT-2", "CNT-3"],
}
PI_ROW = "LT-SM1"
PI_ID = "PI-SUPERSEDED-SM1-UNSPLIT-1"
LEDGER_SHA = "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate(reg: dict, live: dict, report: str, ledger_bytes: bytes) -> list[str]:
    errors: list[str] = []
    terminal = reg.get("terminal_rows", [])
    by_row = {x.get("row_id"): x for x in terminal}
    if list(by_row) != ROWS or len(terminal) != 11 or len(by_row) != 11:
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
    parent = by_row.get(PI_ROW, {})
    if parent.get("bucket") != "B4" or parent.get("terminal_outcome") != "PRECISE_IMPOSSIBILITY" or parent.get("impossibility_id") != PI_ID:
        errors.append("LT-SM1 bounded impossibility mismatch")

    requirement_defs = reg.get("named_requirements", {})
    expected_reqs = {r for reqs in B2.values() for r in reqs}
    if set(requirement_defs) != expected_reqs:
        errors.append("named requirement definitions incomplete")
    for req, item in requirement_defs.items():
        if not item.get("owner") or not item.get("object"):
            errors.append(f"{req} lacks exact owner/object")

    impossibilities = reg.get("precise_impossibilities", [])
    if len(impossibilities) != 1 or impossibilities[0].get("id") != PI_ID:
        errors.append("precise impossibility coverage mismatch")
    else:
        item = impossibilities[0]
        for field in ("class", "assumptions", "witness", "escape", "resurrection_trigger", "target_claim"):
            if not item.get(field):
                errors.append(f"{PI_ID} missing {field}")
        if len(item.get("assumptions", [])) < 2:
            errors.append(f"{PI_ID} needs at least two typed assumptions")

    effects = reg.get("protected_effects", {})
    if not effects or any(value is not False for value in effects.values()):
        errors.append("protected effects must all remain false")
    actual_sha = hashlib.sha256(ledger_bytes).hexdigest()
    if actual_sha != LEDGER_SHA or reg.get("ledger_basis", {}).get("sha256") != LEDGER_SHA:
        errors.append("ledger v0.263 identity moved")

    live_terminal = {x.get("row_id"): x for x in live.get("terminal_row_dispositions", [])}
    for row in ROWS:
        if row not in live_terminal or live_terminal[row].get("evidence_ref") != str(REG_PATH.relative_to(ROOT)):
            errors.append(f"live register missing exact residual evidence for {row}")
    exhausted = live.get("exhaustion_evaluation", {})
    for key, value in {"denominator_rows": 91, "terminal_rows": 91, "open_rows": 0, "exhausted": True, "b2_selectable": True}.items():
        if exhausted.get(key) != value:
            errors.append(f"live register {key} mismatch")
    gate = reg.get("derived_gate_effect", {})
    for key, value in {"terminal_rows": 91, "open_rows": 0, "exhausted": True, "b2_selectable": True}.items():
        if gate.get(key) != value:
            errors.append(f"registry gate {key} mismatch")

    required_report = [
        "GU-COMPARATOR-ROUTING",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
        "```gu-typed-objects",
        "91 terminal and 0 open\nrows",
        "`exhausted=true` and `b2_selectable=true`",
        "No B2 owner was executed",
        "not a scientific verdict",
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
    m = copy.deepcopy(reg); m["source_evidence"]["AC-B2"] = ["missing.md"]; mutations.append((m, live, report, ledger, "source resolution"))
    m = copy.deepcopy(reg); m["terminal_rows"][0]["named_requirements"] = ["COS-NORM-1"]; mutations.append((m, live, report, ledger, "requirements"))
    m = copy.deepcopy(reg); m["named_requirements"]["ABS-1"]["owner"] = ""; mutations.append((m, live, report, ledger, "owner"))
    m = copy.deepcopy(reg); m["precise_impossibilities"][0]["escape"] = ""; mutations.append((m, live, report, ledger, "escape"))
    m = copy.deepcopy(reg); m["protected_effects"]["ledger_verdict_change"] = True; mutations.append((m, live, report, ledger, "protected effect"))
    m = copy.deepcopy(live); m["exhaustion_evaluation"]["terminal_rows"] = 90; mutations.append((reg, m, report, ledger, "counts"))
    m = copy.deepcopy(live); m["terminal_row_dispositions"] = [x for x in m["terminal_row_dispositions"] if x["row_id"] != "AC-F5"]; mutations.append((reg, m, report, ledger, "live row"))
    m = copy.deepcopy(live); m["exhaustion_evaluation"]["exhausted"] = False; mutations.append((reg, m, report, ledger, "gate"))
    mutations.append((reg, live, report.replace("No B2 owner was executed", ""), ledger, "report ceiling"))
    mutations.append((reg, live, report, ledger + b"x", "ledger identity"))
    return [name for r, l, p, b, name in mutations if not evaluate(r, l, p, b)]


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
    print("PASS: residual phenomenology disposition and exhaustion wave")
    if args.selftest:
        missed = selftest(reg, live, report, ledger)
        if missed:
            print("FAIL selftest: " + ", ".join(missed))
            return 1
        print("PASS selftest: 11/11 mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
