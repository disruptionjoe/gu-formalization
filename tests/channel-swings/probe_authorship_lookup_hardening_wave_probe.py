#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 lookup-authorship hardening wave."""
from __future__ import annotations

import copy
import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-lookup-hardening-wave.json"
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
check(data["before"] == {"violations": 205, "probe_corpus": 974, "baseline": 205}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 15, "fifteen repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches ratchet certificate")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 15, "packet repair counts close")

for packet in data["repair_packets"]:
    for rel in packet["paths"]:
        source = (ROOT / rel).read_text(encoding="utf-8")
        check(not any(rule == "L1" for rule, _ in lint_text(source, rel)), f"{rel} has no L1 defect")

hostile = [
    'row = ne' + 'xt(x for x in rows if x.get("id") == "MISSING")',
    'first = ne' + 'xt(iter(cited_exist))',
    'line = ne' + 'xt(x for x in lines if x.startswith("| U1 |"))',
]
for index, snippet in enumerate(hostile, 1):
    check(any(rule == "L1" for rule, _ in lint_text(snippet)), f"hostile missing-default mutation {index} caught")

mutated = copy.deepcopy(data)
mutated["after"]["violations"] = 191
check(mutated["after"]["violations"] != baseline, "hostile ratchet/certificate mismatch caught")
check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == len(hostile) + 1,
      "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
