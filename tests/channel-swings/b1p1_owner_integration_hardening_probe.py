#!/usr/bin/env python3
"""Post-integration certificate for B1P-1 owner hardening."""

from __future__ import annotations

import ast
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MUTATE = os.environ.get("B1P1_INTEGRATION_MUTATE", "")
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


def text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def vertex() -> dict:
    src = text("tests/gu-forces/leg_a_forcing_enumeration.py")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "VERTEX" for t in node.targets
        ):
            value = ast.literal_eval(node.value)
            if MUTATE == "admit_inconsistent":
                value[("ABSENT", "CHIRAL")]["carrier"] = "LIVE"
            return value
    raise RuntimeError("VERTEX not found")


def source_claim() -> dict:
    doc = yaml.safe_load(text("lab/sources/source-claim-register.yaml"))
    row = next((row for row in doc["claims"] if row["id"] == "SC-CHI-01"), None)
    if row is None:
        raise RuntimeError("SC-CHI-01 not found")
    return row


def run_live() -> int:
    global checks, fails
    checks = fails = 0
    v = vertex()
    live = {k: row for k, row in v.items() if row["carrier"] != "INCONSISTENT"}
    check("VERTEX remains the full 2x2", len(v) == 4)
    check("consistent support is exactly three", len(live) == 3)
    check("excluded corner is ABSENT/CHIRAL", set(v) - set(live) == {("ABSENT", "CHIRAL")})
    check("given consistency ABSENT implies MASSIVE", all(p == "MASSIVE" for (i, p) in live if i == "ABSENT"))
    check("given consistency CHIRAL implies PRESENT", all(i == "PRESENT" for (i, p) in live if p == "CHIRAL"))
    check("CHIRAL live carrier is uniquely A", {r["carrier"] for (i, p), r in live.items() if p == "CHIRAL"} == {"A"})
    check("contrary: PRESENT does not imply CHIRAL", {p for (i, p) in live if i == "PRESENT"} == {"CHIRAL", "MASSIVE"})
    check("contrary: MASSIVE does not imply ABSENT", {i for (i, p) in live if p == "MASSIVE"} == {"ABSENT", "PRESENT"})

    canon = text("canon/gu-forces-field-space-declaration-RESULTS.md")
    if MUTATE == "drop_canon_ceiling":
        canon = canon.replace("no corner is selected", "a corner is selected", 1)
    for needle in (
        "no corner is selected",
        "Both converses fail",
        "This is a one-way price, not a bit verdict or an equivalence",
        "non-uniform across the fermionic extension",
        "SG4 stays the sole",
    ):
        check(f"canon carries {needle}", needle in canon)

    method = text("lab/methods/claim-status-consistency.md")
    if MUTATE == "drop_method_ceiling":
        method = method.replace("never weakens `ASSERTS`", "may weaken `ASSERTS`", 1)
    for needle in (
        "Adverse-Mechanism News Fires the Hedge-Watch",
        "name the claim by its `SC-` ID",
        "never weakens `ASSERTS`",
        "never moves a ledger verdict",
        "initial armed case is",
        "`SC-CHI-01`",
    ):
        check(f"method carries {needle}", needle in method)

    claim = source_claim()
    if MUTATE == "move_claim":
        claim["polarity"] = "UNCERTAIN"
    watch = claim["adherence"].get("hedge_watch", {})
    if MUTATE == "drop_watch":
        watch = {}
    check("SC-CHI-01 polarity remains ASSERTS", claim["polarity"] == "ASSERTS")
    check("SC-CHI-01 adherence remains ADHERED", claim["adherence"]["adherence"] == "ADHERED")
    check("hedge_watch status effect is NONE", str(watch.get("status_effect", "")).startswith("NONE."))
    partials = watch.get("adverse_mechanism_partials", [])
    check("hedge_watch carries exactly three adverse partials", len(partials) == 3)
    check("every partial is adverse and conditional", all(p.get("direction") == "adverse" and p.get("conditionality") for p in partials))
    check("partial dates are the filed 2026-08-14/15 set", {p.get("date") for p in partials} == {"2026-08-14", "2026-08-15"})
    check("claim ceiling forbids weakening or adjudication", "do not weaken SC-CHI-01" in watch.get("claim_ceiling", ""))

    ledger = (ROOT / "lab/process/conditional-physics-ledger-v0.263.json").read_bytes()
    ledger_hash = hashlib.sha256(ledger).hexdigest()
    if MUTATE == "ledger_drift":
        ledger_hash = "0" * 64
    check("immutable ledger v0.263 is byte-identical", ledger_hash == "7c75c179c3af512084e50af19043a5d320b38e8c1e53325ee5ec2f97ad9c257b")

    reg = yaml.safe_load(text("lab/process/upgrade-program-register.yaml"))
    item = next(
        (row for row in reg["items"] if row["id"] == "B1P1-PROPOSED-DIFFS"),
        None,
    )
    if item is None:
        raise RuntimeError("B1P1-PROPOSED-DIFFS not found")
    check("remaining item is still queued", item["status"] == "QUEUED")
    check("remaining item is ledger-mint only", "next coherent ledger mint" in item["activation"])
    check("remaining item forbids a standalone annotation mint", "do not create a successor solely" in item["activation"])

    artifact = text("explorations/b1p1-owner-integration-hardening-2026-08-24.md")
    if MUTATE == "artifact_overclaim":
        artifact = artifact.replace("No source claim, bit, carrier", "Source claim and bit", 1)
    check("artifact carries routing notice", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
    check("artifact classification is INTERNAL_STRUCTURAL_ONLY", "Classification: `INTERNAL_STRUCTURAL_ONLY`" in artifact)
    check("artifact target is NONE-NOT-A-KILL", "target_claim: NONE-NOT-A-KILL" in artifact)
    check("artifact carries one typed block", artifact.count("```gu-typed-objects") == 1)
    check("artifact states no source claim or bit moved", "No source claim, bit, carrier" in artifact)

    print(f"CERTIFICATE: {checks - fails}/{checks} checks pass; {fails} failures")
    return 1 if fails else 0


def selftest() -> int:
    clean = subprocess.run([sys.executable, __file__], text=True, capture_output=True)
    if clean.returncode != 0 or "CERTIFICATE:" not in clean.stdout:
        print("SELFTEST RED: clean baseline failed")
        return 1
    mutations = [
        "admit_inconsistent",
        "drop_canon_ceiling",
        "drop_method_ceiling",
        "move_claim",
        "drop_watch",
        "ledger_drift",
        "artifact_overclaim",
    ]
    for mutation in mutations:
        env = dict(os.environ, B1P1_INTEGRATION_MUTATE=mutation)
        run = subprocess.run([sys.executable, __file__], text=True, capture_output=True, env=env)
        if run.returncode == 0 or "[FAIL]" not in run.stdout or "CERTIFICATE:" not in run.stdout:
            print(f"SELFTEST RED: {mutation} was not genuinely caught")
            return 1
        print(f"SELFTEST caught {mutation}")
    print(f"SELFTEST GREEN: clean baseline first; {len(mutations)}/{len(mutations)} targeted mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv else run_live())
