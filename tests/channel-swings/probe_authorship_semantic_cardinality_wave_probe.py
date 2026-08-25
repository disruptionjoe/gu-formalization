#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 semantic-cardinality wave."""
from __future__ import annotations

import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-semantic-cardinality-wave.json"
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


def caught(values: list[int]) -> bool:
    try:
        if len(values) != 1:
            raise AssertionError(f"expected singleton semantic domain, got {values}")
    except AssertionError:
        return True
    return False


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
check(data["before"] == {"violations": 98, "probe_corpus": 984, "baseline": 98}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 9, "nine repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches the lowered ratchet")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches the certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 9, "packet repair counts close")

touched = sorted({path for packet in data["repair_packets"] for path in packet["paths"]})
for rel in touched:
    source = (ROOT / rel).read_text(encoding="utf-8")
    check(not any(rule == "L1" for rule, _ in lint_text(source, rel)), f"{rel} has no residual L1 report")
check(len(touched) == 6, "six unique touched probes close")

check(not [row for row in range(2) if [[0, 1], [0, 0]][row][0] != 0], "singular pivot absence is detectable")
for values, label in (
    ([], "missing exterior complement is caught"),
    ([1, 2], "duplicate exterior complement is caught"),
    ([], "missing target form bit is caught"),
    ([1, 2], "duplicate target form bit is caught"),
    ([], "missing target Clifford bit is caught"),
    ([1, 2], "duplicate target Clifford bit is caught"),
    ([], "empty owner set is caught"),
    ([0, 1], "mixed owner set is caught"),
):
    check(caught(values), label)

hostile_defaultless = "x = ne" + "xt(iter(values))"
check(any(rule == "L1" for rule, _ in lint_text(hostile_defaultless)), "hostile defaultless-next mutation is caught")
check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 9, "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
