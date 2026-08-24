#!/usr/bin/env python3
"""Probe-authorship lint (velocity council item A4, 2026-08-23).

Four defect classes recurred nine times in a single day of probe writing, each
one shipping green or crashing the harness rather than failing a check. All
four are mechanical, so they are linted rather than remembered:

  L1 CRASH-NOT-DETECTION. `next(gen)` with no default raises StopIteration
     when a mutation removes the element, so the harness dies instead of the
     check failing. VERIFICATION.md rule 3 already says a nonzero exit without
     a [FAIL] line is CRASH-NOT-DETECTION; this catches the commonest source.

  L2 STALE GLOBAL PIN. Equality against a hard-coded count (`len(rows) == 28`,
     `LEDGER_BASELINE = 8`) breaks the moment another swing legitimately moves
     the number, so the probe fails for a reason unrelated to its own subject.
     A probe should assert its own contribution plus non-regression: use `>=`
     or `<=` against the recorded value.

  L3 NEGATION-SATISFIABLE PREDICATE. `"conditional" in text` passes on
     "unconditional"; the predicate is satisfied by its own negation and is
     unfalsifiable by construction -- VERIFICATION.md rule 2's family.

  L4 WRAPPED-PROSE CHECK. A multi-word phrase searched in raw file text fails
     silently when the prose reflows across a line. Flatten whitespace first.

Ratchet: LINT_BASELINE records the violation count at installation. RED if the
count rises. Lower it as probes are repaired; retirement condition is zero.

Self-test: --self-test runs planted positive and negative controls for every
rule and exits nonzero if any control misbehaves.
"""
from __future__ import annotations

import glob
import os
import re
import sys

SCOPE = "tests/channel-swings/*_probe.py"
# Violations present when the lint was installed (2026-08-23): pre-existing debt
# across 937 probes, none of it introduced by this gate. Lower as probes are
# repaired; never raise it to make a red go green. Retirement condition: 0.
LINT_BASELINE = 254

# L1: next(...) with no default argument. Regex cannot balance parens, so
# the call is scanned to its matching close and checked for a top-level comma.
def _next_without_default(line: str) -> bool:
    for m in re.finditer(r"\bnext\(", line):
        i, depth, top_comma = m.end(), 1, False
        while i < len(line) and depth:
            ch = line[i]
            if ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth -= 1
            elif ch == "," and depth == 1:
                top_comma = True
            i += 1
        if depth == 0 and not top_comma:
            return True
    return False

# L2: equality against an integer literal for a GLOBAL counter another swing
# can legitimately move. Self-pins (a probe pinning its own subject) are fine,
# so the rule fires only when the check label names a shared counter.
L2 = re.compile(r"==\s*\d+\b")
L2_LABEL = re.compile(r'"[^"]*\b(table|baseline|total|tally|corpus|ledger rows)\b[^"]*"', re.I)
# L3: literals whose negation contains them as a substring.
NEG_PREFIXES = ("un", "in", "non", "im", "ir")
L3_LITERAL = re.compile(r'"([a-z][a-z_ -]{3,40})"\s+in\s+')
# L4: multi-word literal searched in a raw text variable.
L4 = re.compile(r'"([^"]*\s[^"]*\s[^"]*\s[^"]*)"\s+in\s+([A-Za-z_][A-Za-z0-9_]*)')
RAW_TEXT_HINT = re.compile(r"^(result|spec|spec_test|map_text|gate|state|next_steps|register|readme|ledger_text)$")

WORDS = None


def _words() -> set[str]:
    """A small dictionary sufficient for the L3 negation test."""
    global WORDS
    if WORDS is None:
        WORDS = {
            "conditional", "complete", "typed", "correct", "consistent", "valid",
            "dependent", "direct", "formal", "variant", "resolved", "supported",
            "changed", "moved", "bound", "owned", "applied", "derived", "built",
        }
    return WORDS


def lint_text(text: str, path: str = "<memory>") -> list[tuple[str, str]]:
    """Return (rule, detail) violations. Comment lines are exempt."""
    out: list[tuple[str, str]] = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if line.startswith("#"):
            continue
        if _next_without_default(line):
            out.append(("L1", f"{path}:{lineno} next() without a default"))
        if "check(" in line and L2.search(line) and L2_LABEL.search(line):
            out.append(("L2", f"{path}:{lineno} equality against a hard-coded count"))
        for lit in L3_LITERAL.findall(line):
            base = lit.strip()
            if base in _words() and any(p + base in _words() or True for p in NEG_PREFIXES):
                # Only flag when a negated form is plausible for this word.
                if base in {"conditional", "complete", "typed", "correct", "consistent",
                            "valid", "dependent", "direct", "formal", "resolved",
                            "supported", "changed", "moved", "bound", "owned",
                            "applied", "derived", "built"}:
                    out.append(("L3", f"{path}:{lineno} '{base}' is a substring of its own negation"))
        for phrase, var in L4.findall(line):
            if RAW_TEXT_HINT.match(var):
                out.append(("L4", f"{path}:{lineno} multi-word phrase searched in raw '{var}' (flatten first)"))
    return out


def main() -> int:
    paths = sorted(glob.glob(SCOPE))
    violations: list[tuple[str, str]] = []
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            violations.extend(lint_text(fh.read(), os.path.relpath(p)))
    status = "RED " if len(violations) > LINT_BASELINE else "ok  "
    print(f"{status}probe_authorship_lint: {len(violations)} violations "
          f"(baseline {LINT_BASELINE}) across {len(paths)} probes")
    for rule, detail in violations:
        print(f"     {rule}  {detail}")
    if len(violations) < LINT_BASELINE:
        print(f"     NOTE baseline can be lowered to {len(violations)}")
    return 1 if len(violations) > LINT_BASELINE else 0


def selftest() -> int:
    """Planted positive and negative controls for every rule."""
    ok = True
    cases = [
        ("L1", 'x = next(p for p in plan if p["id"] == "A2")', True),
        ("L1", 'x = next((p for p in plan if p["id"] == "A2"), {})', False),
        ("L2", 'check(len(rows) == 28, "spec test table has 28 rows")', True),
        ("L2", 'check(len(rows) >= 28, "spec test table at or above the repair")', False),
        ("L3", 'check("conditional" in map_flat, "carries conditions")', True),
        ("L3", 'check("W154 posit" in map_flat, "carries conditions")', False),
        ("L4", 'check("no chirality for the anomaly" in result, "stance")', True),
        ("L4", 'check("no chirality for the anomaly" in result_flat, "stance")', False),
    ]
    for rule, snippet, should_fire in cases:
        fired = any(r == rule for r, _ in lint_text(snippet))
        if fired != should_fire:
            print(f"[FAIL] control {rule} {'positive' if should_fire else 'negative'}: {snippet!r}")
            ok = False
        else:
            print(f"[PASS] control {rule} {'positive' if should_fire else 'negative'}")
    # A comment must never trip a rule.
    if lint_text('# next(p for p in plan if p["id"] == "A2")'):
        print("[FAIL] control: comment line tripped a rule")
        ok = False
    else:
        print("[PASS] control: comment lines are exempt")
    print("PROBE-LINT SELFTEST: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--self-test" in sys.argv else main())
