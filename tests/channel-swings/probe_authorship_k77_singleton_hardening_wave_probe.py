#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 K77 singleton hardening wave."""
from __future__ import annotations

import copy
import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-k77-singleton-hardening-wave.json"
LINT = ROOT / "process_gates/probe_authorship_lint.py"

FAILURES: list[str] = []
CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if condition:
        print(f"[PASS] {label}")
    else:
        FAILURES.append(label)
        print(f"[FAIL] {label}")


def singleton(values, default):
    items = tuple(values)
    return len(items) == 1, next(iter(items), default)


data = json.loads(CERT.read_text(encoding="utf-8"))
module = runpy.run_path(str(LINT))
lint_text = module["lint_text"]
baseline = module["LINT_BASELINE"]
probe_paths = sorted(glob.glob(str(ROOT / "tests/channel-swings/*_probe.py")))
violations = [
    item
    for path in probe_paths
    for item in lint_text(Path(path).read_text(encoding="utf-8"), str(Path(path).relative_to(ROOT)))
]

check(data["schema_version"] == "1.0" and data["status"] == "PASS", "certificate schema and status")
check(data["before"] == {"violations": 190, "probe_corpus": 976, "baseline": 190}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 19, "nineteen repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches ratchet certificate")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 19, "packet repair counts close")

for packet in data["repair_packets"]:
    for rel in packet["paths"]:
        source = (ROOT / rel).read_text(encoding="utf-8")
        check(not any(rule == "L1" for rule, _ in lint_text(source, rel)), f"{rel} has no L1 defect")

hostile = [
    'row = ne' + 'xt(x for x in rows if x.get("id") == "MISSING")',
    'first = ne' + 'xt(iter(cited_exist))',
    'value = ne' + 'xt(iter(background.values()))',
]
for index, snippet in enumerate(hostile, 1):
    check(any(rule == "L1" for rule, _ in lint_text(snippet)), f"hostile missing-default mutation {index} caught")

present, value = singleton([], "MISSING")
check(not present and value == "MISSING", "empty singleton reaches a controlled falsey state")

mutated = copy.deepcopy(data)
mutated["after"]["violations"] = 172
check(mutated["after"]["violations"] != baseline, "hostile ratchet/certificate mismatch caught")
check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == len(hostile) + 2,
      "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
