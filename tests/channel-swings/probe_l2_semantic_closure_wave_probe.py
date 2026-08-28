#!/usr/bin/env python3
"""Coupled certificate for probe-authorship L2 semantic closure."""
from __future__ import annotations

import glob
import importlib.util
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
LINT_PATH = ROOT / "process_gates" / "probe_authorship_lint.py"
SPEC = importlib.util.spec_from_file_location("probe_authorship_lint", LINT_PATH)
assert SPEC and SPEC.loader
LINT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LINT)

CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    CHECKS.append((label, bool(condition)))


moving_pin = 'check(len(rows) == 28, "current repository-wide table has 28 rows")'
nonregression_pin = 'check(len(rows) >= 28, "current repository-wide table at or above the repair")'
expression_key_pin = 'check("coverage frozen", ledger["mapped"] == ledger["total"] == 82)'
exact_invariant_pin = 'check("four blocks total 4 x 32 = 128", 4 * 32 == 128)'
condition_first_pin = 'check(total == 2, "current global tally has two rows")'

check("moving shared-state literal equality is rejected",
      [rule for rule, _ in LINT.lint_text(moving_pin)] == ["L2"])
check("moving shared-state non-regression inequality is accepted",
      not LINT.lint_text(nonregression_pin))
check("quoted expression key is not mistaken for check-label semantics",
      not LINT.lint_text(expression_key_pin))
check("exact algebraic cardinality remains an admissible self-pin",
      not LINT.lint_text(exact_invariant_pin))
check("condition-first check style still exposes an actual moving label",
      [rule for rule, _ in LINT.lint_text(condition_first_pin)] == ["L2"])

# Reproduce the entering broad detector only to prove the reviewed partition.
# This is evidence about the repaired category, not the live lint rule.
old_literal = re.compile(r"==\s*\d+\b")
old_quote = re.compile(
    r'"[^"]*\b(table|baseline|total|tally|corpus|ledger rows)\b[^"]*"',
    re.I,
)
legacy_findings: list[tuple[str, int]] = []
for raw_path in sorted(glob.glob(str(ROOT / "tests/channel-swings/*_probe.py"))):
    path = pathlib.Path(raw_path)
    if path == pathlib.Path(__file__).resolve():
        continue
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if "check(" in line and old_literal.search(line) and old_quote.search(line):
            legacy_findings.append((path.name, lineno))

historical = [
    finding for finding in legacy_findings
    if re.fullmatch(r"conditional_physics_ledger_v\d+_probe\.py", finding[0])
    or finding[0] == "cross_theory_mechanism_donor_crosswalk_probe.py"
    or finding[0] == "source_action_spec_build_wave_currency_probe.py"
]
exact = [finding for finding in legacy_findings if finding not in historical]

check("entering broad detector inventory is reproduced", len(legacy_findings) == 70)
check("historical and frozen-wave pins are explicitly classified", len(historical) == 51)
check("exact scientific or certificate-local pins are explicitly classified", len(exact) == 19)

live_findings: list[tuple[str, str]] = []
paths = sorted(glob.glob(str(ROOT / "tests/channel-swings/*_probe.py")))
for raw_path in paths:
    path = pathlib.Path(raw_path)
    live_findings.extend(
        LINT.lint_text(path.read_text(encoding="utf-8"), str(path.relative_to(ROOT)))
    )
check("live corpus has no probe-authorship finding", live_findings == [])
check("live ratchet is closed at zero", LINT.LINT_BASELINE <= 0)

failures = 0
for label, passed in CHECKS:
    print(f"[{'PASS' if passed else 'FAIL'}] {label}")
    failures += int(not passed)
print(f"PROBE L2 SEMANTIC CLOSURE: {len(CHECKS) - failures}/{len(CHECKS)} pass")
sys.exit(1 if failures else 0)
