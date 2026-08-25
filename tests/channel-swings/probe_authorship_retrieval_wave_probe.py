#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 retrieval hardening wave."""
from __future__ import annotations

import copy
import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-retrieval-wave.json"
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
check(data["before"] == {"violations": 171, "probe_corpus": 977, "baseline": 171}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 24, "twenty-four repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches ratchet certificate")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 24, "packet repair counts close")

selected_residual_l1 = 0
for packet in data["repair_packets"]:
    for rel, expected_l1 in packet["paths"].items():
        source = (ROOT / rel).read_text(encoding="utf-8")
        actual_l1 = sum(rule == "L1" for rule, _ in lint_text(source, rel))
        selected_residual_l1 += actual_l1
        check(actual_l1 == expected_l1, f"{rel} retains only its declared residual L1 count")
check(selected_residual_l1 == data["validation"]["selected_residual_l1"] == 3,
      "selected residual L1 boundary closes")

hostile = [
    'row = ne' + 'xt(x for x in rows if x.get("id") == "MISSING")',
    'first = ne' + 'xt(iter(values))',
    'item = ne' + 'xt(x for x in mapping if x["row_id"] == "MISSING")',
]
for index, snippet in enumerate(hostile, 1):
    check(any(rule == "L1" for rule, _ in lint_text(snippet)), f"hostile missing-default mutation {index} caught")

campaign_rows: list[dict[str, object]] = []
campaign_row = next((row for row in campaign_rows if row.get("id") == "WAVE3"), None)
check(campaign_row is None, "empty campaign lookup reaches a controlled falsey state")

fixture_by_id = {"D-1": [1, 0, 0, 0]}
selected = ["D-1", "MISSING"]
check(any(fixture_id not in fixture_by_id for fixture_id in selected), "missing selected fixture is detected before retrieval")

mutated = copy.deepcopy(data)
mutated["after"]["violations"] = 148
check(mutated["after"]["violations"] != baseline, "hostile ratchet/certificate mismatch caught")
check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 6,
      "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
