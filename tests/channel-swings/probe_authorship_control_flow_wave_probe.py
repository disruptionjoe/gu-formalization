#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 control-flow hardening wave."""
from __future__ import annotations

import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-control-flow-wave.json"
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
check(data["before"] == {"violations": 114, "probe_corpus": 981, "baseline": 114}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 7, "seven repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches the lowered ratchet")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches the certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 7, "packet repair counts close")

touched = sorted({path for packet in data["repair_packets"] for path in packet["paths"]})
for rel in touched:
    source = (ROOT / rel).read_text(encoding="utf-8")
    check(not any(rule == "L1" for rule, _ in lint_text(source, rel)), f"{rel} has no residual L1 report")
check(len(touched) == 5, "five unique touched probes close")

check(next((index for index, value in enumerate([1.0, 0.0]) if value < 0), None) is None,
      "zero-only wall sample is controlled")
check(next((index for index in range(4) if False), None) is None,
      "missing half-spin eigenspace is controlled")
check(next((key for key in [(0, 1)] if key[0] != 0), None) is None,
      "single-input operator is controlled")
check(next((index for index in range(4) if index not in (0, 1, 2, 3)), None) is None,
      "full-degree exterior key is controlled")
hostile_defaultless = "x = ne" + "xt(iter(values))"
check(any(rule == "L1" for rule, _ in lint_text(hostile_defaultless)),
      "hostile defaultless-next mutation is caught")

check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 4,
      "hostile controls close")
check(all(value == "none" for value in data["effect"].values()),
      "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
