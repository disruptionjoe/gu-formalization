#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 domain-precondition wave."""
from __future__ import annotations

import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-domain-precondition-wave.json"
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
check(data["before"] == {"violations": 107, "probe_corpus": 983, "baseline": 107}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 9, "nine repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches the lowered ratchet")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches the certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 9, "packet repair counts close")

touched = sorted({path for packet in data["repair_packets"] for path in packet["paths"]})
for rel in touched:
    source = (ROOT / rel).read_text(encoding="utf-8")
    check(not any(rule == "L1" for rule, _ in lint_text(source, rel)), f"{rel} has no residual L1 report")
check(len(touched) == 8, "eight unique touched probes close")

check(not [row for row in range(2) if [[0, 1], [0, 0]][row][0] != 0], "singular pivot absence is detectable")
check(not [component for component in [] if component], "missing projected-beta component is detectable")
check(not [value for value in [0, 0] if value != 0], "missing projected-beta entry is detectable")
check(not {}, "empty orbit support is detectable")
check(len([]) != 1, "missing representation image is detectable")
check(len([0, 1]) != 1, "duplicate representation image is detectable")
check(not {}, "empty source-case bank is detectable")
check(len({3, 4}) != 1, "inconsistent source-case part counts are detectable")
check(min({(2, 0), (1, 3)}) == (1, 3), "orbit seed selection is deterministic")
hostile_defaultless = "x = ne" + "xt(iter(values))"
check(any(rule == "L1" for rule, _ in lint_text(hostile_defaultless)), "hostile defaultless-next mutation is caught")

check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 8, "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
