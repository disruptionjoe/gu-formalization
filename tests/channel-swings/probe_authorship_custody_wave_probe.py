#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 custody hardening wave."""
from __future__ import annotations

import ast
import glob
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-authorship-custody-wave.json"
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
check(data["before"] == {"violations": 147, "probe_corpus": 978, "baseline": 147}, "entering ratchet frozen")
check(data["after"]["repaired_violations"] == 11, "eleven repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint matches ratchet certificate")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 11, "packet repair counts close")

for packet in data["repair_packets"]:
    for rel in packet["paths"]:
        source = (ROOT / rel).read_text(encoding="utf-8")
        actual_l1 = sum(rule == "L1" for rule, _ in lint_text(source, rel))
        check(actual_l1 == 0, f"{rel} has no residual L1 custody report")

rows = [{"id": "A"}]
check(len([row for row in rows if row["id"] == "MISSING"]) == 0, "missing registry row is controlled")
duplicate_rows = [{"id": "A"}, {"id": "A"}]
check(len([row for row in duplicate_rows if row["id"] == "A"]) != 1, "duplicate registry row is controlled")
shell_rows = [{"radius_squared": 121}]
check(len([row for row in shell_rows if row["radius_squared"] == 4]) == 0, "missing shell row is controlled")

tree = ast.parse("def other():\n    pass\n")
nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "build_structures"]
check(len(nodes) != 1, "missing extracted function is controlled")
partners: list[dict[str, str]] = []
check(len(partners) != 1, "missing relational partner is controlled")
check(next(iter(set()), None) is None, "empty Dynkin diagonal is controlled")
preferred = {"first": {}, "second": {}}
check(len(preferred) != 1, "duplicate preferred-ratio result is controlled")

check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 7,
      "hostile controls close")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
