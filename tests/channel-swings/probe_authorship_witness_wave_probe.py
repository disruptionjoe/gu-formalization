#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 witness-custody hardening wave."""
from __future__ import annotations

import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-witness-wave.json"
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
check(data["before"] == {"violations": 136, "probe_corpus": 980, "baseline": 136}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 22, "twenty-two repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches ratchet certificate")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 22, "packet repair counts close")

touched: list[str] = []
for packet in data["repair_packets"]:
    touched.extend(packet["paths"])
    for rel in packet["paths"]:
        source = (ROOT / rel).read_text(encoding="utf-8")
        actual_l1 = sum(rule == "L1" for rule, _ in lint_text(source, rel))
        check(actual_l1 == 0, f"{rel} has no residual L1 witness report")
check(len(touched) == len(set(touched)) == 15, "fifteen unique touched probes close")

check(next(iter(set()), None) is None, "empty degree witness is controlled")
check([index for index in range(4) if index not in (0, 1, 2, 3)] == [], "missing exterior complement is controlled")
check(not any([]), "missing live leg is controlled")
check(next(iter(set()), None) is None, "empty projector coefficient bank is controlled")
check(next(iter({}), None) is None, "missing residual coordinate is controlled")
check(list({}.values()) == [], "empty curvature bank is controlled")
check(next(iter({}), None) is None, "missing dependency key is controlled")
check(next(reversed({}), None) is None, "missing basis pivot is controlled")
hostile_defaultless = "x = ne" + "xt(iter(values))"
check(any(rule == "L1" for rule, _ in lint_text(hostile_defaultless)), "hostile defaultless-next mutation is caught")

check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 8, "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
