#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-27 probe fail-closed restoration wave."""
from __future__ import annotations

import glob
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "lab/process/probe-fail-closed-restoration-wave.json"
LINT = ROOT / "process_gates/probe_authorship_lint.py"
TARGETS = {
    "geometry": ROOT / "tests/channel-swings/geometry_first_theory_passport_probe.py",
    "source_claim": ROOT / "tests/channel-swings/source_claim_residual_wave_probe.py",
    "source_rollup": ROOT / "tests/channel-swings/source_scope_and_rollup_residual_wave_probe.py",
}

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
check(data["before"] == {"violations": 92, "probe_corpus": 1006, "baseline": 89, "gate_status": "RED"}, "entering red state frozen")
check(data["after"]["repaired_violations"] == 3, "three repairs recorded")
check(len(violations) == baseline == data["after"]["violations"], "global lint returns to the 89 ratchet")
check(len(probe_paths) == data["after"]["probe_corpus"], "probe inventory matches certificate")
check(sum(packet["repaired_violations"] for packet in data["repair_packets"]) == 3, "packet repair counts close")

sources = {name: path.read_text(encoding="utf-8") for name, path in TARGETS.items()}
check(not lint_text(sources["geometry"], str(TARGETS["geometry"].relative_to(ROOT))), "geometry lookup has no L1 finding")
check("assert item is not None" in sources["geometry"], "geometry lookup explicitly asserts presence")
check(not lint_text(sources["source_claim"], str(TARGETS["source_claim"].relative_to(ROOT))), "source-claim probe has no L4 finding")
check(not lint_text(sources["source_rollup"], str(TARGETS["source_rollup"].relative_to(ROOT))), "source-rollup probe has no L4 finding")

safe_lookup = "ne" + 'xt((row for row in agenda["work_items"] if row["id"] == AGENDA_ID), None)'
unsafe_lookup = "ne" + 'xt(row for row in agenda["work_items"] if row["id"] == AGENDA_ID)'
mutated_geometry = sources["geometry"].replace(safe_lookup, unsafe_lookup)
check(any(rule == "L1" for rule, _ in lint_text(mutated_geometry)), "missing geometry default is caught")
geometry_module = runpy.run_path(str(TARGETS["geometry"]))
with tempfile.TemporaryDirectory() as directory:
    missing_agenda = json.loads((ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8"))
    missing_agenda["work_items"] = [row for row in missing_agenda["work_items"] if row["id"] != "CONDITIONAL-BUILD-REVERSE-SCAFFOLD"]
    missing_path = Path(directory) / "agenda.json"
    missing_path.write_text(json.dumps(missing_agenda), encoding="utf-8")
    geometry_module["main"].__globals__["AGENDA"] = missing_path
    try:
        geometry_module["main"]()
    except AssertionError as error:
        controlled_absence = "missing agenda item" in str(error)
    else:
        controlled_absence = False
check(controlled_absence, "missing geometry agenda row fails by controlled assertion")

for name in ("source_claim", "source_rollup"):
    raw_headline = 'check("historical register headline current" in ' + 'register, "headline")'
    mutated = sources[name].replace("census = adjudication_census(register)", raw_headline, 1)
    check(any(rule == "L4" for rule, _ in lint_text(mutated)), f"raw {name} register search is caught")

commands = {
    "geometry": [sys.executable, str(TARGETS["geometry"])],
    "source_claim": [sys.executable, str(TARGETS["source_claim"]), "--selftest"],
    "source_rollup": [sys.executable, str(TARGETS["source_rollup"]), "--selftest"],
}
for name, command in commands.items():
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    check(result.returncode == 0, f"{name} native replay passes")

check(data["hostile_controls"]["caught"] == data["hostile_controls"]["count"] == 6, "hostile control ledger closes")
check(all(value == "none" for value in data["effect"].values()), "protected scientific effects remain none")

if FAILURES:
    raise SystemExit(f"FAIL {len(FAILURES)}/{CHECKS}: {FAILURES}")
print(f"PASS {CHECKS}/{CHECKS}")
