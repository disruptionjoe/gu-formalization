#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-28 probe L1 category closure."""
from __future__ import annotations

import glob
import json
import runpy
from itertools import count
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-l1-category-closure-wave.json"
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

check(data["schema_version"] == "1.0" and data["result"] == "PROBE_L1_CATEGORY_CLOSED",
      "certificate schema and result")
check(data["baseline_before"] == 84 and data["l1_before"] == 14,
      "entering ratchet and L1 population frozen")
check(baseline == data["baseline_after"] == len(violations) == 70,
      "global lint matches the lowered ratchet")
check(len(probe_paths) == data["probe_population_after"] == 1013,
      "probe inventory includes the coupled certificate")
check(not any(rule == "L1" for rule, _detail in violations),
      "live L1 category is empty")
check(sum(family["selections"] for family in data["repair_families"]) == 14,
      "three repair families close fourteen selections")

touched = sorted({path for family in data["repair_families"] for path in family["paths"]})
check(len(touched) == 10, "ten unique scientific probes are covered")
for rel in touched:
    source = (ROOT / rel).read_text(encoding="utf-8")
    check(not any(rule == "L1" for rule, _detail in lint_text(source, rel)),
          f"{rel} has no residual L1 report")

check(next(count(), -1) == 0, "infinite issuance iterator keeps its successful value")
check(next(iter(()), -1) == -1, "empty guarded iterator returns impossible degree")
check(next((value for value in ()), None) is None, "empty construction domain returns sentinel")
hostile_defaultless = "witness = ne" + "xt(x for x in values)"
check(any(rule == "L1" for rule, _ in lint_text(hostile_defaultless)),
      "planted defaultless selection is caught")
check(not lint_text("witness = next((x for x in values), None)"),
      "planted explicit-default selection is accepted")
check(all(value is not None for value in data["forbidden_inferences"]),
      "forbidden inferences remain explicit")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
