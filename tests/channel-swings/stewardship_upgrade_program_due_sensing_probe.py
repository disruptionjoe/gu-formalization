#!/usr/bin/env python3
"""Planted controls for upgrade-register overdue-row sensing.

The control is deliberately process-only: an expired ``next_check`` must be
enumerated for review, while terminal rows with old dates stay out of the due
set.  No result here authorizes activation, priority, or scientific movement.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GATE_PATH = ROOT / "process_gates" / "upgrade_program_register_audit.py"


def load_gate():
    spec = importlib.util.spec_from_file_location("upgrade_register_gate", GATE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load upgrade-program audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fixture(path: Path) -> None:
    data = {
        "schema_version": "1.0",
        "status_vocabulary": ["QUEUED", "ACTIVE", "DONE", "DECLINED"],
        "items": [
            {
                "id": "OVERDUE-QUEUED",
                "title": "queued review",
                "origin": "planted-control origin with enough receipt detail",
                "owner": "control owner",
                "status": "QUEUED",
                "activation": "review only; no execution authority",
                "next_check": "2026-08-28",
            },
            {
                "id": "CURRENT-ACTIVE",
                "title": "current active review",
                "origin": "planted-control origin with enough receipt detail",
                "owner": "control owner",
                "status": "ACTIVE",
                "activation": "review only; no execution authority",
                "next_check": "2026-08-29",
            },
            {
                "id": "OLD-DONE",
                "title": "terminal old row",
                "origin": "planted-control origin with enough receipt detail",
                "owner": "control owner",
                "status": "DONE",
                "activation": "receipt: planted terminal control is complete",
                "next_check": "2026-08-01",
            },
        ],
    }
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def main() -> int:
    gate = load_gate()
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="gu-upgrade-due-") as tmp:
        register = Path(tmp) / "register.yaml"
        fixture(register)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rc = gate.audit(register, date(2026, 8, 29))
        text = output.getvalue()
        if rc != 0:
            failures.append("well-formed planted register did not stay structurally green")
        if gate.DUE != ["OVERDUE-QUEUED"]:
            failures.append(f"wrong planted due set: {gate.DUE!r}")
        if "1 overdue nonterminal: OVERDUE-QUEUED" not in text:
            failures.append("due row was not directly enumerated in audit output")
        if "OLD-DONE" in gate.DUE:
            failures.append("terminal old row was incorrectly reported as overdue")

    actual = io.StringIO()
    with contextlib.redirect_stdout(actual):
        rc = gate.audit(
            ROOT / "lab" / "process" / "upgrade-program-register.yaml",
            date(2026, 8, 30),
        )
    expected = {
        "CT2-SCHEMA-FINDINGS",
        "LEDGER-FULL-ROW-RETYPE",
        "FX1-BD1-PAIR-FLIP",
        "MINT-RESIDUE-AC-ROWS",
        "CB-C-U4-MENU",
        "B1P1-PROPOSED-DIFFS",
        "DS1-REALITY-MAP-GATE",
        "RW1-CHANNEL-INHERITANCES",
    }
    if rc != 0 or set(gate.DUE) != expected:
        failures.append(f"live 2026-08-30 due set mismatch: {gate.DUE!r}")

    register_data = yaml.safe_load(
        (ROOT / "lab" / "process" / "upgrade-program-register.yaml").read_text(
            encoding="utf-8"
        )
    )
    rows = {row["id"]: row for row in register_data["items"]}
    currency_row = rows["CC-DIRTY-QUEUE-DRAIN"]
    if currency_row["status"] != "DONE" or "zero dirty" not in currency_row["activation"]:
        failures.append("canonical-currency queue completion is not durably receipted")

    bad_date = subprocess.run(
        [sys.executable, str(GATE_PATH), "--as-of", "2026-02-30"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if bad_date.returncode != 2 or "real calendar date" not in bad_date.stderr:
        failures.append("malformed --as-of control was not rejected by the CLI")

    if gate.resolve_as_of(None).__class__ is not date:
        failures.append("default UTC-date resolution did not return a date")

    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        print(f"stewardship_upgrade_program_due_sensing_probe: {len(failures)} failures")
        return 1
    print("stewardship_upgrade_program_due_sensing_probe: 6/6 controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
