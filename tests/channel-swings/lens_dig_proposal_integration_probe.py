#!/usr/bin/env python3
"""Certificate for the lens-dig proposal-to-register reconstruction."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MUTATE = os.environ.get("LENS_DIG_INTEGRATION_MUTATE", "")
checks = 0
fails = 0


def check(name: str, condition: bool) -> None:
    global checks, fails
    checks += 1
    if condition:
        print(f"[PASS] {name}")
    else:
        fails += 1
        print(f"[FAIL] {name}")


def run_live() -> int:
    global checks, fails
    checks = fails = 0
    register = yaml.safe_load(
        (ROOT / "lab/process/upgrade-program-register.yaml").read_text(encoding="utf-8")
    )
    rows = {row["id"]: row for row in register["items"]}
    queued = [
        "UR-BIT2-CRITICAL",
        "UR-BIT2-STRATUM",
        "UR-BIT2-PROVENANCE",
        "UR-INSERTION-DIRECTION-STRATIFICATION",
        "BD-D-FERMIONIC-DISANALOGY",
        "CHK2-SETTLED-HORN-MATCHING",
        "SG4-BUILT-ACTION-SELF-CONSISTENCY",
        "SG4-OBSERVED-EPOCH-BINNING",
        "SG4-BIT-2-RECONCILIATION",
        "SG4-BIT-2-SOURCE-SILENCE-FALLBACK",
    ]
    if MUTATE == "drop_row":
        rows.pop(queued[0], None)
    check("all ten surviving proposal ids are registered", all(i in rows for i in queued))
    present = [rows[i] for i in queued if i in rows]
    check("all surviving proposals remain QUEUED", all(row["status"] == "QUEUED" for row in present))
    check("every surviving proposal has a detailed owner", all(len(row["owner"]) > 12 for row in present))
    check("every surviving proposal has a bounded activation", all(len(row["activation"]) > 80 for row in present))
    check("every surviving proposal has its own origin", all("2026-08-17" in row["origin"] for row in present))

    critical = rows.get("UR-BIT2-CRITICAL", {})
    stratum = rows.get("UR-BIT2-STRATUM", {})
    provenance = rows.get("UR-BIT2-PROVENANCE", {})
    direction = rows.get("UR-INSERTION-DIRECTION-STRATIFICATION", {})
    chk2 = rows.get("CHK2-SETTLED-HORN-MATCHING", {})
    self_consistency = rows.get("SG4-BUILT-ACTION-SELF-CONSISTENCY", {})
    binning = rows.get("SG4-OBSERVED-EPOCH-BINNING", {})
    reconciliation = rows.get("SG4-BIT-2-RECONCILIATION", {})
    fallback = rows.get("SG4-BIT-2-SOURCE-SILENCE-FALLBACK", {})
    if MUTATE == "select_binning":
        binning = dict(binning, activation="Choose CHIRAL now")
    if MUTATE == "erase_dependency":
        chk2 = dict(chk2, activation="Run immediately")
    if MUTATE == "soften_fallback":
        fallback = dict(fallback, activation="Retype all rows to EXTERNAL_DATUM")

    check("critical tension selects no SG4 bit", "selects no SG4 bit" in critical.get("activation", ""))
    check("stratum waits on critical-reading disposition", "After UR-BIT2-CRITICAL" in stratum.get("activation", ""))
    check("stratum is not a phase verdict", "not a phase" in stratum.get("activation", ""))
    check("provenance moves no computed bit", "No computed bit" in provenance.get("activation", ""))
    check("direction residue preserves completed form-rank work", "completed invariant-gapping" in direction.get("activation", ""))
    check("direction residue requires a genuinely new input", "Reopen only on a new" in direction.get("activation", ""))
    check("CHK-2 requires an action-owned settled horn", "action-owned settled-horn" in chk2.get("activation", ""))
    check("built-action row names the fermion-sourced Euler equation", "fermion-sourced varpi Euler equation" in self_consistency.get("activation", ""))
    check("observed-epoch binning remains a two-option fork", "Either define" in binning.get("activation", "") and "or rule" in binning.get("activation", ""))
    check("observed-epoch row explicitly does not choose", "does not choose the fork" in binning.get("activation", ""))
    check("reconciliation defines the narrow action/source conflict", "significantly above zero" in reconciliation.get("activation", ""))
    check("fallback requires both exact receipts", "Requires receipts proving both" in fallback.get("activation", ""))
    check("fallback forbids the soft EXTERNAL_DATUM retype", "EXTERNAL_DATUM is forbidden" in fallback.get("activation", ""))

    parent = rows.get("LENS-DIG-REMAINING-PROPOSALS", {})
    if MUTATE == "reopen_parent":
        parent = dict(parent, status="QUEUED")
    check("omnibus proposal item is DONE", parent.get("status") == "DONE")
    check("omnibus receipt counts nineteen residues", "nineteen distinct proposal residues" in parent.get("activation", ""))
    check("omnibus receipt counts ten surviving proposals", "ten surviving proposals" in parent.get("activation", ""))
    check("omnibus receipt preserves non-adjudication", "none of the ten queued questions is" in parent.get("activation", ""))

    done_ids = [
        "UR-BIT2-TRANSPORT",
        "UR-BIT2-BASE",
        "CANON-NULLITY-SCOPE",
        "DISCHARGE-ORDER-NONMONOTONE",
        "RSC1-R5-RESCOPE",
        "SRC-SCCHI-COUPLING-RULE",
        "BIT1-PRICE-PRINT",
        "SG4-BIT2-FORK-ENTRY",
    ]
    check("eight named later receipts are DONE", all(rows[i]["status"] == "DONE" for i in done_ids))
    check("status-inert B1P1 ledger residue stays QUEUED", rows["B1P1-PROPOSED-DIFFS"]["status"] == "QUEUED")

    artifact = (ROOT / "explorations/lens-dig-proposal-integration-2026-08-24.md").read_text(encoding="utf-8")
    if MUTATE == "artifact_overclaim":
        artifact = artifact.replace("No source claim, scientific verdict", "A source claim and scientific verdict", 1)
    check("artifact carries the mandatory comparator notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    check("artifact classification is INTERNAL_STRUCTURAL_ONLY", "Classification: `INTERNAL_STRUCTURAL_ONLY`" in artifact)
    check("artifact target is NONE-NOT-A-KILL", "target_claim: NONE-NOT-A-KILL" in artifact)
    check("artifact carries one typed-object block", artifact.count("```gu-typed-objects") == 1)
    check("artifact states the exact nineteen/nine/ten census", "Nineteen distinct residues" in artifact and "Nine are `DONE_LATER`" in artifact and "Ten remain live" in artifact)
    check("artifact states no scientific truth moved", "No source claim, scientific verdict" in artifact)

    print(f"CERTIFICATE: {checks - fails}/{checks} checks pass; {fails} failures")
    return 1 if fails else 0


def selftest() -> int:
    clean = subprocess.run([sys.executable, __file__], text=True, capture_output=True)
    if clean.returncode != 0 or "CERTIFICATE:" not in clean.stdout:
        print("SELFTEST RED: clean baseline failed")
        return 1
    mutations = [
        "drop_row",
        "select_binning",
        "erase_dependency",
        "soften_fallback",
        "reopen_parent",
        "artifact_overclaim",
    ]
    for mutation in mutations:
        env = dict(os.environ, LENS_DIG_INTEGRATION_MUTATE=mutation)
        run = subprocess.run([sys.executable, __file__], text=True, capture_output=True, env=env)
        if run.returncode == 0 or "[FAIL]" not in run.stdout or "CERTIFICATE:" not in run.stdout:
            print(f"SELFTEST RED: {mutation} was not genuinely caught")
            return 1
        print(f"SELFTEST caught {mutation}")
    print(f"SELFTEST GREEN: clean baseline first; {len(mutations)}/{len(mutations)} targeted mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run_live())
