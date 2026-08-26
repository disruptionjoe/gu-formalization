#!/usr/bin/env python3
"""Freeze the current enforceable positive-control/foreground source order."""
from __future__ import annotations

import ast
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "lab/process/positive-control-order-population.yaml"
CONTROL = re.compile(r"positive[ _-]control|planted[ _-]positive", re.I)
FOREGROUND = re.compile(r"claim|verdict|foreground", re.I)
ENFORCERS = {"check", "assert_true", "assert_equal", "assert_close", "require", "ok", "assert_allclose"}


def tracked_python() -> list[str]:
    raw = subprocess.check_output(
        ["git", "ls-files", "-z", "tests/*.py", "process_gates/*.py"], cwd=ROOT
    )
    return sorted(x for x in raw.decode().split("\0") if x)


def call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ""


def census(paths: list[str]) -> list[tuple[str, int, int, str]]:
    rows: list[tuple[str, int, int, str]] = []
    for rel in paths:
        text = (ROOT / rel).read_text(errors="replace")
        if not CONTROL.search(text):
            continue
        try:
            tree = ast.parse(text)
        except SyntaxError:
            continue
        controls: list[int] = []
        foreground: list[int] = []
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assert, ast.Call)):
                continue
            if isinstance(node, ast.Call) and call_name(node) not in ENFORCERS:
                continue
            segment = ast.get_source_segment(text, node) or ""
            if CONTROL.search(segment):
                controls.append(node.lineno)
            if FOREGROUND.search(segment):
                foreground.append(node.lineno)
        if controls and foreground:
            pc, fg = min(controls), min(foreground)
            rows.append((rel, pc, fg, "ordered" if pc < fg else "legacy_exception"))
    return sorted(rows)


def digest(rows: list[tuple[str, int, int, str]]) -> str:
    body = "".join(f"{p}\0{pc}\0{fg}\0{state}\n" for p, pc, fg, state in rows)
    return hashlib.sha256(body.encode()).hexdigest()


def audit_rows(rows: list[tuple[str, int, int, str]], data: dict) -> list[str]:
    failures: list[str] = []
    exceptions = sorted(p for p, _pc, _fg, state in rows if state == "legacy_exception")
    expected = sorted(data["legacy_exceptions"])
    counts = {
        "comparable_files": len(rows),
        "ordered": sum(state == "ordered" for *_rest, state in rows),
        "legacy_exceptions": len(exceptions),
    }
    if counts != data["counts"]:
        failures.append(f"population counts changed: {counts!r}")
    if exceptions != expected:
        failures.append(f"legacy exception set changed: {exceptions!r}")
    if digest(rows) != data["population_digest_sha256"]:
        failures.append("control/foreground line-order digest changed")
    return failures


def audit() -> list[str]:
    return audit_rows(census(tracked_python()), yaml.safe_load(MANIFEST.read_text()))


def selftest() -> int:
    data = yaml.safe_load(MANIFEST.read_text())
    rows = census(tracked_python())
    failures = audit_rows(rows, data)
    if failures:
        print("BASELINE RED -- aborting mutations")
        for item in failures:
            print(f"[FAIL] {item}")
        return 1
    reversed_row = list(rows)
    p, pc, fg, _ = reversed_row[0]
    reversed_row[0] = (p, fg + 1, fg, "legacy_exception")
    added_row = rows + [("tests/_planted.py", 20, 10, "legacy_exception")]
    caught = [bool(audit_rows(reversed_row, data)), bool(audit_rows(added_row, data))]
    for i, ok in enumerate(caught, 1):
        print(f"[{'PASS' if ok else 'FAIL'}] planted order regression {i}")
    return 0 if all(caught) else 1


if __name__ == "__main__":
    failures = audit()
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    for item in failures:
        print(f"[FAIL] {item}")
    print(f"positive_control_order_audit: {len(failures)} failures")
    raise SystemExit(bool(failures))
