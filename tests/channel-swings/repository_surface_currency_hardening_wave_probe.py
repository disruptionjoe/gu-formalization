#!/usr/bin/env python3
"""Coupled certificate for six current repository-surface contracts."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / "lab/process/repository-surface-currency-hardening-wave.json"
ANOMALY_README = ROOT / "tests/anomaly/README.md"
SPEC_AUDIT = ROOT / "process_gates/lab_specifications_readme_surface_map_audit.py"
TRANSPORT = ROOT / "lab/methods/research-evidence-contract-v1.0.json"
TESTS_README = ROOT / "tests/README.md"
TESTS_AUDIT = ROOT / "process_gates/tests_manifest_count_audit.py"
GATES_README = ROOT / "process_gates/README.md"
PATH_SOURCE = ROOT / "lab/process/path-dependencies.yaml"
PATH_VIEW = ROOT / "lab/process/path-dependencies.md"

GATES = [
    ROOT / "process_gates/anomaly_readme_inventory_audit.py",
    SPEC_AUDIT,
    ROOT / "process_gates/learning_transport_contract_audit.py",
    TESTS_AUDIT,
    ROOT / "process_gates/process_gate_readme_inventory_audit.py",
    ROOT / "process_gates/path_dependency_audit.py",
]
MISSING_GATE_NAMES = [
    "correction_custody_wave_audit.py",
    "external_datum_claim_ceiling_audit.py",
    "frontmatter_status_schema_audit.py",
    "improvement_register_writeback_adjudication_audit.py",
    "positive_control_order_audit.py",
]
MIXED_ROW = re.compile(
    r"^\| `channel-swings/` \((\d+) Python \+ (\d+) Sage\) \|",
    re.MULTILINE,
)

checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path)], cwd=ROOT, text=True,
        capture_output=True, check=False,
    )


def mixed_counts_match(text: str) -> bool:
    match = MIXED_ROW.search(text)
    if match is None:
        return False
    actual_python = sum(
        1 for path in (ROOT / "tests/channel-swings").iterdir()
        if path.is_file() and path.suffix == ".py"
    )
    actual_sage = sum(
        1 for path in (ROOT / "tests/channel-swings").iterdir()
        if path.is_file() and path.suffix == ".sage"
    )
    return (int(match.group(1)), int(match.group(2))) == (actual_python, actual_sage)


def main() -> None:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    check("six packets declared", len(cert["packets"]) == 6)

    results = [run(path) for path in GATES]
    for path, result in zip(GATES, results, strict=True):
        check(f"{path.name} green", result.returncode == 0)
        check(f"{path.name} no traceback", "Traceback" not in result.stderr)

    anomaly = ANOMALY_README.read_text(encoding="utf-8")
    check("M-H14 certificate inventoried", "`mh14_gs_content_factorization.py`" in anomaly)
    check("M-H14 selftest command inventoried", "mh14_gs_content_factorization.py --selftest" in anomaly)

    spec_audit = SPEC_AUDIT.read_text(encoding="utf-8")
    check("theory-passport expected", '"theory-passport"' in spec_audit)
    check("theory-passport README exists", (ROOT / "lab/specifications/theory-passport/README.md").is_file())

    transport = json.loads(TRANSPORT.read_text(encoding="utf-8"))["standing_ledger"]
    check("transport machine pointer terminal", transport["ref"].endswith("v0.263.json"))
    check("transport human pointer terminal", transport["human_ref"].endswith("v0.263.md"))

    tests_readme = TESTS_README.read_text(encoding="utf-8")
    check("mixed channel-swing count current", mixed_counts_match(tests_readme))
    check("mixed count is enforced", "test_mixed_manifest_rows_match_direct_extensions" in TESTS_AUDIT.read_text(encoding="utf-8"))

    gates_readme = GATES_README.read_text(encoding="utf-8")
    for name in MISSING_GATE_NAMES:
        check(f"{name} inventoried", f"`{name}`" in gates_readme)

    path_view = PATH_VIEW.read_text(encoding="utf-8")
    check("path view names generator", "path_dependency_audit.py --write" in path_view)
    check("path source retains seven chains", PATH_SOURCE.read_text(encoding="utf-8").count("\n  - id: PD-") == 7)

    check("anomaly removal caught", "`mh14_gs_content_factorization.py`" not in anomaly.replace("`mh14_gs_content_factorization.py`", "", 1))
    check("spec scope removal caught", '"theory-passport"' not in spec_audit.replace('"theory-passport"', "", 1))
    check("stale transport mutation caught", not transport["ref"].replace("v0.263", "v0.242").endswith("v0.263.json"))
    mixed = MIXED_ROW.search(tests_readme)
    check("mixed count decrement caught", mixed is not None and not mixed_counts_match(tests_readme.replace(mixed.group(1), str(int(mixed.group(1)) - 1), 1)))
    check("gate inventory removal caught", f"`{MISSING_GATE_NAMES[0]}`" not in gates_readme.replace(f"`{MISSING_GATE_NAMES[0]}`", "", 1))
    check("stale rendered mutation caught", path_view + "stale\n" != path_view)

    for key in (
        "scientific_verdict_change", "source_status_change", "ledger_change",
        "canon_change", "paper_lifecycle_change", "public_posture_change",
    ):
        check(f"{key} none", cert["effect"][key] == "none")

    print(f"repository_surface_currency_hardening_wave_probe: {checks}/{checks} checks pass, exit 0")


if __name__ == "__main__":
    main()
