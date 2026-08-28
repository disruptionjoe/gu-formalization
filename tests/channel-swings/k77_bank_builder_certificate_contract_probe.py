#!/usr/bin/env python3
"""Fail-closed contract probe for the two canonical K77 bank builders."""

from __future__ import annotations

from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parents[2]
BUILDERS = (
    ROOT / "tests/channel-swings/k77_exact_bank_build.py",
    ROOT / "tests/channel-swings/k77_minimal_tangent_bank_build.py",
)
checks = []


def check(kind, label, condition):
    ok = bool(condition)
    checks.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def load(path):
    name = path.stem + "_contract"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def accepted(module, output, failures=()):
    try:
        module.require_producer_pass(output, failures, "planted producer")
    except RuntimeError:
        return False
    return True


for builder in BUILDERS:
    module = load(builder)
    prefix = builder.stem
    check("exact", f"{prefix} accepts the current RESULT-prefixed 31/31 certificate",
          accepted(module, "noise\nRESULT: PASS 31/31\n"))
    check("exact", f"{prefix} accepts an annotated count without pinning its value",
          accepted(module, "PASS 48/48 (44 exact + 4 planted)\n"))
    check("planted", f"PLANT {prefix} rejects a mismatched summary",
          not accepted(module, "RESULT: PASS 30/31\n"))
    check("planted", f"PLANT {prefix} rejects a vacuous zero-count summary",
          not accepted(module, "PASS 0/0\n"))
    check("planted", f"PLANT {prefix} rejects a missing summary",
          not accepted(module, "all checks looked fine\n"))
    check("planted", f"PLANT {prefix} rejects named failures despite a green summary",
          not accepted(module, "FAIL [exact] witness\nPASS 31/31\n", ["witness"]))
    try:
        module.require_producer_pass(
            "FAIL [exact] witness\nRESULT: PASS 30/31\n", ["witness"], "diagnostic producer"
        )
    except RuntimeError as error:
        diagnostic = str(error)
    else:
        diagnostic = ""
    check("exact", f"{prefix} failure exposes summary, failures and output tail",
          "summary=(30, 31)" in diagnostic
          and "failures=['witness']" in diagnostic
          and "output_tail=" in diagnostic)

failures = [label for _, label, ok in checks if not ok]
exact = sum(kind == "exact" for kind, _, _ in checks)
planted = sum(kind == "planted" for kind, _, _ in checks)
print(f"PASS {len(checks) - len(failures)}/{len(checks)} ({exact} exact + {planted} planted)")
if failures:
    raise SystemExit("; ".join(failures))
