#!/usr/bin/env python3
"""Coupled certificate for the source-native comparator scope boundary."""
from __future__ import annotations

import copy
import importlib.util
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
AUDIT_PATH = ROOT / "process_gates" / "source_native_comparator_routing_audit.py"
SPEC = importlib.util.spec_from_file_location("source_native_comparator_routing_audit", AUDIT_PATH)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)

TWG1 = "lab/active-research/joe-directed/theory-wide-gravity/twg1-the-theory-wide-test-is-action-complete-black-hole-existence-2026-08-26.md"
CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    CHECKS.append((label, bool(condition)))


candidates = AUDIT.candidate_artifacts()
entries = AUDIT.scope_exemption_entries()
registered = {
    entry["path"]
    for entry in AUDIT.json.loads(AUDIT.REGISTRY_PATH.read_text(encoding="utf-8"))["artifacts"]
}
exempted = {entry["path"] for entry in entries}
live_gap = AUDIT.coverage_gap(candidates, registered, exempted)
raw_gap = AUDIT.coverage_gap(candidates, registered, set())

check("TWG1 remains in the automatically derived candidate population", TWG1 in candidates)
check("TWG1 is excluded only by one explicit process-side exemption", exempted == {TWG1})
check("the protected TWG1 artifact receives no routing classification", TWG1 not in registered)
check("all live exemptions pass path, scope, disjointness and content-hash validation",
      AUDIT.scope_exemption_errors(entries, candidates, registered) == [])
check("the raw candidate population reproduces the six-item entering gap", len(raw_gap) == 6)
check("the live ratchet returns to the five genuine legacy classification gaps",
      len(live_gap) == AUDIT.UNCLASSIFIED_BASELINE == 5)

without_exemption = AUDIT.coverage_gap(candidates, registered, set())
check("removing the exemption makes the sixth gap red", len(without_exemption) == 6)

def changed_content(path: str) -> bytes:
    payload = (ROOT / path).read_bytes()
    return payload + (b"\nchanged" if path == TWG1 else b"")

changed_errors = AUDIT.scope_exemption_errors(
    entries, candidates, registered, content_loader=changed_content
)
check("any protected-artifact byte change invalidates the exemption",
      any("sha256" in error for error in changed_errors))

known = next(iter(registered), None)
check("the mutation fixture has at least one registered comparator", known is not None)
if known is not None:
    bad_entries = copy.deepcopy(entries)
    bad_entries.append({
        "path": known,
        "sha256": AUDIT.hashlib.sha256((ROOT / known).read_bytes()).hexdigest(),
        "scope": AUDIT.OUTSIDE_LISTED_SCOPE,
        "reason": "planted invalid exemption of an already classified comparator",
    })
    bad_errors = AUDIT.scope_exemption_errors(bad_entries, candidates, registered)
    check("a registered comparator cannot be hidden behind a scope exemption",
          any("registered artifact cannot also be exempt" in error for error in bad_errors))

    synthetic_registered = set(registered)
    synthetic_registered.remove(known)
    check("removing one true comparator registration reopens the ratchet",
          len(AUDIT.coverage_gap(candidates, synthetic_registered, exempted)) == 6)
else:
    check("a registered comparator cannot be hidden behind a scope exemption", False)
    check("removing one true comparator registration reopens the ratchet", False)

failures = 0
for label, passed in CHECKS:
    print(f"[{'PASS' if passed else 'FAIL'}] {label}")
    failures += int(not passed)
print(f"COMPARATOR SCOPE HARDENING: {len(CHECKS) - failures}/{len(CHECKS)} pass")
sys.exit(1 if failures else 0)
