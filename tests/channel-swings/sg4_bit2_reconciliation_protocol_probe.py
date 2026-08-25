#!/usr/bin/env python3
"""Certificate for SG4 bit-2 reconciliation protocol enrollment."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MUTATE = os.environ.get("SG4_RECONCILIATION_MUTATE", "")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_live() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name: str, value: bool) -> None:
        checks.append((name, bool(value)))

    registry = yaml.safe_load((ROOT / "lab/process/layer0-fork-registry.yaml").read_text())
    forks = {row["id"]: row for row in registry["forks"]}
    upgrades = yaml.safe_load((ROOT / "lab/process/upgrade-program-register.yaml").read_text())
    upgrade_rows = {row["id"]: row for row in upgrades["items"]}
    fork = forks["SG4-BIT-2-PHASE"]
    protocol = dict(fork.get("reconciliation", {}))
    artifact = (ROOT / "explorations/sg4-bit2-reconciliation-protocol-enrollment-2026-08-24.md").read_text()

    if MUTATE == "settle_phase":
        fork = dict(fork, status="settled")
    if MUTATE == "third_surface":
        protocol["authorized_surfaces"] = [*protocol["authorized_surfaces"], {"id": "THIRD", "question": "synthetic"}]
    if MUTATE == "same_question":
        protocol["question_relation"] = "SAME_QUESTION"
    if MUTATE == "broaden_trigger":
        protocol["conflict_trigger"] = "PROSE_DISAGREEMENT"
    if MUTATE == "new_disposition":
        protocol["on_conflict"] = dict(protocol["on_conflict"], allowed_dispositions=["EXTERNAL_DATUM"])
    if MUTATE == "file_now":
        protocol["current_state"] = "FIRED"
    if MUTATE == "allow_consumer":
        protocol["unresolved_use_rule"] = "MAY_CITE_AS_RESOLVED"

    surfaces = protocol.get("authorized_surfaces", [])
    check("phase fork remains open", fork["status"] == "open")
    check("protocol id is stable", protocol.get("protocol_id") == "SG4-BIT-2-RECONCILIATION")
    check("exactly two authorized surfaces", [row.get("id") for row in surfaces] == ["LANE-1-STATIONARY-PHASE", "SC-CHI-01"])
    check("questions remain distinct", protocol.get("question_relation") == "DIFFERENT_QUESTIONS__NEITHER_OVERRIDES_THE_OTHER")
    check("conflict requires constructed stationary vacuum", protocol.get("conflict_trigger") == "FIRES_ONLY_IF_LANE_1_CONSTRUCTS_AN_ACTION_OWNED_STATIONARY_VACUUM_WITH_VARPI_VEV_SIGNIFICANTLY_ABOVE_ZERO")
    check("prose is explicitly not conflict", "prose disagreement" in protocol.get("non_conflicts", []))
    check("hedge strength is explicitly not conflict", "differing hedge strength" in protocol.get("non_conflicts", []))
    check("future escalation uses coherent mint", protocol.get("on_conflict", {}).get("action") == "FILE_OVER_DETERMINED_ESCALATION_IN_NEXT_COHERENT_LEDGER_MINT")
    check("future escalation owner is exact", protocol.get("on_conflict", {}).get("owner") == "sg4-bit-2-selector")
    check("allowed dispositions match standing taxonomy", protocol.get("on_conflict", {}).get("allowed_dispositions") == ["GENUINE_FALSIFICATION", "FORK_ARTIFACT", "SCOPE_ERROR", "STALE_PREMISE"])
    check("current conflict is not fired", protocol.get("current_state") == "NOT_FIRED__NO_ACTION_OWNED_STATIONARY_VACUUM")
    check("unresolved consumer rule fails closed", protocol.get("unresolved_use_rule") == "NO_CONSUMER_MAY_CITE_BIT_2_AS_RESOLVED")

    upgrade = upgrade_rows["SG4-BIT-2-RECONCILIATION"]
    check("upgrade row is DONE", upgrade["status"] == "DONE")
    check("upgrade receipt names enrollment", "sg4-bit2-reconciliation-protocol-enrollment-2026-08-24.md" in upgrade["activation"])
    check("artifact carries comparator notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    check("artifact is internal structural only", "Classification: `INTERNAL_STRUCTURAL_ONLY`" in artifact)
    check("artifact has one typed-object block", artifact.count("```gu-typed-objects") == 1)
    check("artifact does not claim a kill", "target_claim: NONE-NOT-A-KILL" in artifact)
    check("immutable ledger v0.263 is byte-identical", digest(ROOT / "lab/process/conditional-physics-ledger-v0.263.json") == "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b")

    failures = 0
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        failures += not passed
    print(f"CERTIFICATE: {len(checks) - failures}/{len(checks)} checks pass; {failures} failures")
    return 1 if failures else 0


def selftest() -> int:
    clean = subprocess.run([sys.executable, __file__], text=True, capture_output=True)
    if clean.returncode or "CERTIFICATE:" not in clean.stdout:
        print("SELFTEST RED: clean baseline failed")
        print(clean.stdout)
        return 1
    mutations = (
        "settle_phase", "third_surface", "same_question", "broaden_trigger",
        "new_disposition", "file_now", "allow_consumer",
    )
    for mutation in mutations:
        env = dict(os.environ, SG4_RECONCILIATION_MUTATE=mutation)
        run = subprocess.run([sys.executable, __file__], text=True, capture_output=True, env=env)
        if run.returncode == 0 or "[FAIL]" not in run.stdout:
            print(f"SELFTEST RED: {mutation} escaped")
            return 1
        print(f"SELFTEST caught {mutation}")
    print(f"SELFTEST GREEN: clean baseline first; {len(mutations)}/{len(mutations)} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run_live())
