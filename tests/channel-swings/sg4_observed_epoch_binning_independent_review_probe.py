#!/usr/bin/env python3
"""Certificate for the SG4 observed-epoch binning independent review."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MUTATE = os.environ.get("SG4_EPOCH_BINNING_MUTATE", "")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_live() -> int:
    checks: list[tuple[str, bool]] = []

    def check(name: str, value: bool) -> None:
        checks.append((name, bool(value)))

    register = yaml.safe_load((ROOT / "lab/process/upgrade-program-register.yaml").read_text())
    rows = {row["id"]: row for row in register["items"]}
    fork_registry = yaml.safe_load((ROOT / "lab/process/layer0-fork-registry.yaml").read_text())
    forks = {row["id"]: row for row in fork_registry["forks"]}
    canon = (ROOT / "canon/gu-forces-field-space-declaration-RESULTS.md").read_text()
    st1 = (ROOT / "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md").read_text()
    scur1 = (ROOT / "lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md").read_text()
    artifact = (ROOT / "explorations/sg4-observed-epoch-binning-independent-review-2026-08-24.md").read_text()

    if MUTATE == "requeue":
        rows["SG4-OBSERVED-EPOCH-BINNING"] = dict(rows["SG4-OBSERVED-EPOCH-BINNING"], status="QUEUED")
    if MUTATE == "settle_phase":
        forks["SG4-BIT-2-PHASE"] = dict(forks["SG4-BIT-2-PHASE"], status="settled")
    if MUTATE == "observed_chiral":
        canon = canon.replace("**Observed-epoch routing scope correction", "**Historical note", 1)
    if MUTATE == "drop_st1":
        st1 = st1.replace("Observed-epoch routing correction", "Historical note", 1)
    if MUTATE == "drop_scur1":
        scur1 = scur1.replace("Observed-epoch routing correction", "Historical note", 1)

    row = rows["SG4-OBSERVED-EPOCH-BINNING"]
    check("observed-epoch row is DONE", row["status"] == "DONE")
    check("row names continuous-modulus routing", "continuous-modulus" in row["activation"])
    check("row preserves phase fork", "SG4-BIT-2-PHASE remains open" in row["activation"])
    check("phase fork stays open", forks["SG4-BIT-2-PHASE"]["status"] == "open")
    check("independent review remains required for phase settlement", forks["SG4-BIT-2-PHASE"]["independent_review_required"] is True)

    canon_flat = " ".join(canon.split())
    st1_flat = " ".join(st1.split())
    scur1_flat = " ".join(scur1.split())
    artifact_flat = " ".join(artifact.split())
    check("canon excludes observed binary assignment", "Observed-epoch routing scope correction" in canon and "is not assigned to either binary endpoint" in canon_flat)
    check("canon requires continuous observed routing", "epoch statements therefore use the continuous modulus" in canon_flat)
    check("canon preserves coarse endpoint declaration", "binary remains the exact coarse endpoint declaration" in canon_flat)
    check("canon preserves open phase fork", "The action-owned `SG4-BIT-2-PHASE` fork remains open" in canon)
    check("ST-1 carries additive routing correction", "Observed-epoch routing correction" in st1 and "does not assign the" in st1_flat and "observed epoch to the coarse" in st1_flat)
    check("SCUR-1 carries additive routing correction", "Observed-epoch routing correction" in scur1 and "not an observed assignment" in scur1_flat)

    check("artifact declares observed carrier inadmissible", "binary is **inadmissible as an observed-value carrier" in artifact)
    check("artifact preserves open SG4 fork", "`SG4-BIT-2-PHASE` remains open" in artifact)
    check("artifact states reversible input", "source-authenticated or action-derived coarse-graining map" in artifact_flat)
    check("artifact carries comparator notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    check("artifact classification is semantic boundary", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in artifact)
    check("artifact has one typed-object block", artifact.count("```gu-typed-objects") == 1)
    check("artifact target is not a kill", "target_claim: NONE-NOT-A-KILL" in artifact)

    check("LEG-A byte-identical", digest(ROOT / "tests/gu-forces/leg_a_forcing_enumeration.py") == "3043d29ef2ca97b527113b16a399f7f5256ba8df85902ccff3b3d69a58380197")
    check("LEG-B byte-identical", digest(ROOT / "tests/gu-forces/leg_b_forcing_enumeration_independent.py") == "b2e13c9a54dc6e888393e40097d9df5ccc7998e84feaa7d5011118404530092e")

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
    mutations = ("requeue", "settle_phase", "observed_chiral", "drop_st1", "drop_scur1")
    for mutation in mutations:
        env = dict(os.environ, SG4_EPOCH_BINNING_MUTATE=mutation)
        run = subprocess.run([sys.executable, __file__], text=True, capture_output=True, env=env)
        if run.returncode == 0 or "[FAIL]" not in run.stdout:
            print(f"SELFTEST RED: {mutation} escaped")
            return 1
        print(f"SELFTEST caught {mutation}")
    print(f"SELFTEST GREEN: clean baseline first; {len(mutations)}/{len(mutations)} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run_live())
