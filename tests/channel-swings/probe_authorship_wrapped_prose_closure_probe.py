#!/usr/bin/env python3
"""Coupled certificate for repository-wide wrapped-prose detector closure."""

from __future__ import annotations

import copy
import glob
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/probe-authorship-wrapped-prose-closure.json"
LINT_PATH = ROOT / "process_gates/probe_authorship_lint.py"


def load_lint():
    spec = importlib.util.spec_from_file_location("probe_authorship_lint", LINT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("probe-authorship lint cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def count_violations(lint) -> tuple[int, list[tuple[str, str]]]:
    paths = sorted(glob.glob(str(ROOT / lint.SCOPE)))
    violations: list[tuple[str, str]] = []
    for path in paths:
        text = Path(path).read_text(encoding="utf-8")
        violations.extend(lint.lint_text(text, str(Path(path).relative_to(ROOT))))
    return len(paths), violations


def collect_failures(data: dict, lint) -> tuple[int, list[str]]:
    failures: list[str] = []
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(label)

    probes, violations = count_violations(lint)
    after = data["after"]
    check(data["schema_version"] == "1.0", "schema")
    check(data["status"] == "PASS", "status")
    check(after["repaired_violations"] == data["before"]["violations"] - after["violations"],
          "repair count")
    check(probes == after["probe_corpus"], "probe corpus")
    check(len(violations) == after["violations"], "violation count")
    check(lint.LINT_BASELINE == after["baseline"], "lint baseline")
    check(len(violations) <= lint.LINT_BASELINE, "ratchet is green")
    check(not [row for row in violations if row[0] == "L4"], "wrapped-prose class closed")

    declared = {
        path
        for packet in data["repair_packets"][:2]
        for path in packet["paths"]
    }
    check(len(declared) == 16, "sixteen repaired probes declared")
    for relative in sorted(declared):
        text = (ROOT / relative).read_text(encoding="utf-8")
        check(not [row for row in lint.lint_text(text, relative) if row[0] == "L4"],
              f"repaired probe has no wrapped-prose defect: {relative}")

    check(all(value == "none" for value in data["effect"].values()),
          "no scientific effect")
    check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"],
          "hostile controls recorded")
    return checks, failures


def main() -> int:
    lint = load_lint()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    checks, failures = collect_failures(data, lint)
    for label in failures:
        print(f"[FAIL] {label}")
    if failures:
        return 1
    print(f"PASS {checks}/{checks}")
    return 0


def selftest() -> int:
    lint = load_lint()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    checks, failures = collect_failures(data, lint)
    if failures:
        for label in failures:
            print(f"[FAIL] baseline: {label}")
        return 1
    print(f"BASELINE PASS {checks}/{checks}")

    plants = {
        "raw-result": 'check("a wrapped scientific phrase" in ' + "result)",
        "raw-state": 'check("a wrapped current phrase" in ' + "state)",
        "raw-spec": 'check("a wrapped specification phrase" in ' + "spec)",
        "raw-register": 'check("a wrapped source phrase" in ' + "register)",
    }
    ok = True
    for name, snippet in plants.items():
        caught = [row for row in lint.lint_text(snippet, f"plant:{name}") if row[0] == "L4"]
        if not caught:
            print(f"[FAIL] plant {name} escaped")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: L4")

    changed = copy.deepcopy(data)
    changed["after"]["baseline"] -= 1
    _, caught = collect_failures(changed, lint)
    if "lint baseline" not in caught:
        print(f"[FAIL] ratchet mismatch escaped: {caught}")
        ok = False
    else:
        print("MUTATION CAUGHT ratchet-mismatch: [FAIL] lint baseline")
    print("FAILURE-PATH SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
