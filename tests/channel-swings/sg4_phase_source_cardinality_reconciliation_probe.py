#!/usr/bin/env python3
"""Certificate for the SG4 phase source/cardinality reconciliation."""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MUTATE = os.environ.get("SG4_PHASE_RECONCILIATION_MUTATE", "")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_live() -> int:
    checks: list[tuple[str, bool]] = []
    check = lambda name, value: checks.append((name, bool(value)))

    register = yaml.safe_load((ROOT / "lab/process/upgrade-program-register.yaml").read_text())
    rows = {row["id"]: row for row in register["items"]}
    if MUTATE == "reopen":
        rows["UR-BIT2-CRITICAL"] = dict(rows["UR-BIT2-CRITICAL"], status="QUEUED")
    for row_id in ("UR-BIT2-CRITICAL", "UR-BIT2-STRATUM", "UR-BIT2-PROVENANCE"):
        check(f"{row_id} is DONE", rows[row_id]["status"] == "DONE")
        check(f"{row_id} points to reconciliation", "sg4-phase-source-cardinality-reconciliation" in rows[row_id]["activation"])
    check("observed-epoch fork remains QUEUED", rows["SG4-OBSERVED-EPOCH-BINNING"]["status"] == "QUEUED")
    check("SG4 bit reconciliation remains QUEUED", rows["SG4-BIT-2-RECONCILIATION"]["status"] == "QUEUED")

    claims = yaml.safe_load((ROOT / "lab/sources/source-claim-register.yaml").read_text())
    claim_rows = {row["id"]: row for row in claims["claims"]}
    if MUTATE == "threshold":
        claim_rows["SC-CHI-52"]["phase_reading_reconciliation"]["reading"] = "strictly-positive threshold proved"
    for claim_id in ("SC-CHI-01", "SC-CHI-02", "SC-CHI-52"):
        row = claim_rows[claim_id]
        check(f"{claim_id} polarity unchanged", row["polarity"] == "ASSERTS")
        check(f"{claim_id} has dated reconciliation", str(row["phase_reading_reconciliation"]["date"]) == "2026-08-24")
    check("SC-CHI-02 preserves exact R zero", "R(y)=0" in claim_rows["SC-CHI-02"]["phase_reading_reconciliation"]["reading"])
    chi52_reading = " ".join(claim_rows["SC-CHI-52"]["phase_reading_reconciliation"]["reading"].split())
    check("SC-CHI-52 does not assert positive threshold", "not a supplied strictly-positive threshold" in chi52_reading and "proved" not in chi52_reading)

    canon = (ROOT / "canon/gu-forces-field-space-declaration-RESULTS.md").read_text()
    artifact = (ROOT / "explorations/sg4-phase-source-cardinality-reconciliation-2026-08-24.md").read_text()
    if MUTATE == "canon_measurement":
        canon = canon.replace("source-imported two-axis declaration", "measured two-axis declaration", 1)
    if MUTATE == "settle_fork":
        artifact = artifact.replace("`SG4-BIT-2-PHASE` remains open", "`SG4-BIT-2-PHASE` is settled")
    check("canon names imported declaration", canon.count("source-imported two-axis declaration") >= 2)
    check("canon says cardinality is not measured", "does not measure either axis's cardinality" in canon)
    check("canon preserves unresolved continuum", "unresolved continuum inside the source mechanism" in canon)
    check("canon does not invent third phase", "not evidence for a third discrete phase" in " ".join(canon.split()))
    check("artifact preserves open SG4 fork", "`SG4-BIT-2-PHASE` remains open" in artifact)
    check("artifact carries comparator notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    check("artifact classification is source native", "Classification: `SOURCE_NATIVE_ROUTE`" in artifact)
    check("artifact has one typed-object block", artifact.count("```gu-typed-objects") == 1)
    check("artifact target is not a kill", "target_claim: NONE-NOT-A-KILL" in artifact)

    check("LEG-A predeclaration byte-identical", digest(ROOT / "tests/gu-forces/leg_a_forcing_enumeration.py") == "3043d29ef2ca97b527113b16a399f7f5256ba8df85902ccff3b3d69a58380197")
    check("LEG-B enumeration byte-identical", digest(ROOT / "tests/gu-forces/leg_b_forcing_enumeration_independent.py") == "b2e13c9a54dc6e888393e40097d9df5ccc7998e84feaa7d5011118404530092e")

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
        return 1
    mutations = ("reopen", "threshold", "canon_measurement", "settle_fork")
    for mutation in mutations:
        env = dict(os.environ, SG4_PHASE_RECONCILIATION_MUTATE=mutation)
        run = subprocess.run([sys.executable, __file__], text=True, capture_output=True, env=env)
        if run.returncode == 0 or "[FAIL]" not in run.stdout:
            print(f"SELFTEST RED: {mutation} escaped")
            return 1
        print(f"SELFTEST caught {mutation}")
    print(f"SELFTEST GREEN: clean baseline first; {len(mutations)}/{len(mutations)} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run_live())
