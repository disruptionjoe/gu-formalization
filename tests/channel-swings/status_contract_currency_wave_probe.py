#!/usr/bin/env python3
"""Coupled certificate for frontmatter-axis and live L10 currency."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
CAPACITYOS = ROOT.parents[2]
FRONTMATTER_GATE = ROOT / "process_gates" / "frontmatter_status_schema_audit.py"
TYPED_GATE = ROOT / "process_gates" / "typed_carrier_declaration_audit.py"
L10_PROBE = ROOT / "tests" / "channel-swings" / "conditional_build_frontier_l10_typed_carrier_surface_probe.py"
CERTIFICATE = ROOT / "lab" / "process" / "status-contract-currency-wave.json"

EXPLORATIONS = [
    "explorations/source-dynamics-adherence-wave-2026-08-27.md",
    "explorations/source-residual-terminalization-wave-2026-08-27.md",
    "explorations/source-structure-adherence-wave-2026-08-27.md",
    "explorations/source-uncertainty-custody-wave-2026-08-27.md",
]
REVIEWS = [
    "lab/process/hostile-reviews/2026-08-27-probe-fail-closed-restoration-wave-review.md",
    "lab/process/hostile-reviews/2026-08-27-source-dynamics-adherence-wave-review.md",
    "lab/process/hostile-reviews/2026-08-27-source-residual-terminalization-wave-review.md",
    "lab/process/hostile-reviews/2026-08-27-source-structure-adherence-wave-review.md",
    "lab/process/hostile-reviews/2026-08-27-source-uncertainty-custody-wave-review.md",
]
PROTECTED = ROOT / "lab/active-research/joe-directed/theory-wide-gravity/twg1-the-theory-wide-test-is-action-complete-black-hole-existence-2026-08-26.md"

checks = 0


def check(label: str, condition: bool) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def metadata(rel: str) -> dict:
    text = (ROOT / rel).read_text(encoding="utf-8")
    check(f"{rel} has frontmatter", text.startswith("---\n"))
    end = text.find("\n---\n", 4)
    check(f"{rel} frontmatter closes", end >= 0)
    return yaml.safe_load(text[4:end])


def run(path: Path, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path)], cwd=cwd, text=True,
        capture_output=True, check=False,
    )


def validate_pair(fm: dict, role: str, operational: str) -> bool:
    return fm.get("status") == role and fm.get("operational_state") == operational


def main() -> None:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    check("certificate exploration set exact", cert["typed_paths"]["exploration"] == EXPLORATIONS)
    check("certificate review set exact", cert["typed_paths"]["process"] == REVIEWS)

    for rel in EXPLORATIONS:
        check(f"{rel} axes", validate_pair(metadata(rel), "exploration", "complete"))
    for rel in REVIEWS:
        expected = "review_complete" if rel.endswith("source-dynamics-adherence-wave-review.md") else "complete"
        check(f"{rel} axes", validate_pair(metadata(rel), "process", expected))

    protected = PROTECTED.read_bytes()
    check("protected TWG1 sha256 unchanged", hashlib.sha256(protected).hexdigest() == cert["protected_exclusion"]["sha256"])
    blob = subprocess.run(
        ["git", "hash-object", str(PROTECTED)], cwd=ROOT,
        text=True, capture_output=True, check=True,
    ).stdout.strip()
    check("protected TWG1 git blob unchanged", blob == cert["protected_exclusion"]["git_blob"])

    front = run(FRONTMATTER_GATE, ROOT)
    typed_root = run(TYPED_GATE, ROOT)
    typed_aggregate = run(TYPED_GATE, CAPACITYOS)
    l10 = run(L10_PROBE, ROOT)
    check("frontmatter contract green", front.returncode == 0 and "0 failures" in front.stdout)
    check("typed-carrier gate green", typed_root.returncode == 0 and "0 red" in typed_root.stdout)
    check("caller root cannot change typed report", typed_root.stdout == typed_aggregate.stdout)
    check("L10 propagation current", l10.returncode == 0 and "checks pass" in l10.stdout)
    check("no subprocess stderr", not front.stderr and not typed_root.stderr and not typed_aggregate.stderr and not l10.stderr)

    clean = {"status": "exploration", "operational_state": "complete"}
    check("clean axis fixture accepted", validate_pair(clean, "exploration", "complete"))
    check("role mutation caught", not validate_pair({**clean, "status": "complete"}, "exploration", "complete"))
    check("missing operational axis caught", not validate_pair({"status": "exploration"}, "exploration", "complete"))

    check("scientific verdict unchanged", cert["effect"]["scientific_verdict_change"] == "none")
    check("source status unchanged", cert["effect"]["source_status_change"] == "none")
    check("ledger unchanged", cert["effect"]["ledger_change"] == "none")
    check("canon unchanged", cert["effect"]["canon_change"] == "none")
    check("public posture unchanged", cert["effect"]["public_posture_change"] == "none")
    print(f"status_contract_currency_wave_probe: {checks}/{checks} checks pass, exit 0")


if __name__ == "__main__":
    main()
