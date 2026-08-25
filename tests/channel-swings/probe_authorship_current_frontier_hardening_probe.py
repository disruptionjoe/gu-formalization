#!/usr/bin/env python3
"""Coupled certificate for the current-frontier probe-authorship hardening."""

from __future__ import annotations

import copy
import glob
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/probe-authorship-current-frontier-hardening.json"
LINT_PATH = ROOT / "process_gates/probe_authorship_lint.py"


def load_lint():
    spec = importlib.util.spec_from_file_location("probe_authorship_lint", LINT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("probe-authorship lint cannot be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def count_violations(lint) -> tuple[int, int]:
    paths = sorted(glob.glob(str(ROOT / lint.SCOPE)))
    violations = []
    for path in paths:
        text = Path(path).read_text(encoding="utf-8")
        violations.extend(lint.lint_text(text, str(Path(path).relative_to(ROOT))))
    return len(paths), len(violations)


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
    check(after["repaired_violations"] == data["before"]["violations"] - after["violations"], "repair count")
    check(probes >= after["probe_corpus"], "probe corpus")
    check(violations <= after["violations"], "violation count")
    check(lint.LINT_BASELINE <= after["baseline"], "lint baseline")
    check(violations <= lint.LINT_BASELINE, "ratchet is green")

    declared = {
        path
        for packet in data["repair_packets"]
        for path in packet["paths"]
        if path.startswith("tests/channel-swings/")
        and path != "tests/channel-swings/probe_authorship_current_frontier_hardening_probe.py"
    }
    check(len(declared) == 10, "ten repaired probes declared")
    for relative in sorted(declared):
        text = (ROOT / relative).read_text(encoding="utf-8")
        check(not lint.lint_text(text, relative), f"repaired probe is lint-clean: {relative}")

    effect = data["effect"]
    check(all(value == "none" for value in effect.values()), "no scientific effect")
    check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"], "hostile controls recorded")
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
        "crash-not-detection": "x = ne" + "xt(row for row in rows)",
        "wrapped-prose": 'check("a wrapped phrase with spaces" in ' + "result)",
        "negation-satisfiable": 'check("condi' + 'tional" in text)',
    }
    ok = True
    for name, snippet in plants.items():
        caught = lint.lint_text(snippet, f"plant:{name}")
        if not caught:
            print(f"[FAIL] plant {name} escaped")
            ok = False
        else:
            print(f"MUTATION CAUGHT {name}: {caught[0][0]}")

    changed = copy.deepcopy(data)
    changed["after"]["baseline"] = lint.LINT_BASELINE - 1
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
