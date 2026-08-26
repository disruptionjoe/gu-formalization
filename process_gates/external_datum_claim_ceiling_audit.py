#!/usr/bin/env python3
"""Keep the exact 2+1 multiplicity result separate from realized chiral P3.

The arithmetic probe is valid, but a green run must not reinstate the retracted
multiplicity-to-index inference. Selftest verifies the clean baseline first and
then mutates each prose/executable custody surface on isolated copies.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = Path("explorations/external-datum-ledger-and-the-2plus1-product-rule-2026-07-29.md")
SOURCE_ACTION = Path("explorations/source-action-term-by-term-against-the-spec-2026-07-29.md")
PROBE = Path("tests/channel-swings/external_datum_ledger_probe.py")

FAILURES: list[str] = []
CHECKS = 0


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        FAILURES.append(label)
        print(f"[FAIL] {label}")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"missing frontmatter: {path}")
    return yaml.safe_load(parts[1])


def audit(root: Path) -> int:
    global CHECKS, FAILURES
    CHECKS, FAILURES = 0, []
    try:
        ledger = frontmatter(root / LEDGER)
        source_action = frontmatter(root / SOURCE_ACTION)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        check("both prose surfaces have parseable frontmatter", False)
        print(f"  {exc}")
        return 1

    ledger_title = str(ledger.get("title", ""))
    action_title = str(source_action.get("title", ""))
    check("ledger live title scopes the result to multiplicity", "2+1 MULTIPLICITY" in ledger_title)
    check("ledger live title does not discharge P3", "does not discharge P3" in ledger_title)
    check("ledger outcome retains P3", ledger.get("outcome") == "P3-REINSTATED-AS-EXTERNAL")
    check("source-action live title keeps SA-C3 open", "does not discharge SA-C3" in action_title)
    check("source-action live title keeps SA-C1 conditional", "does not lapse SA-C1" in action_title)

    probe_path = root / PROBE
    probe_source = probe_path.read_text(encoding="utf-8")
    stale_tokens = (
        "P3-IS-" + "NOT-EXTERNAL",
        "missing pieces reduce from three to " + "TWO",
        "P3  " + "WITHDRAWN as external",
    )
    check("probe source contains no retracted executable verdict", not any(t in probe_source for t in stale_tokens))
    result = subprocess.run(
        [sys.executable, str(probe_path)],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    check("probe exits zero", result.returncode == 0)
    check("probe prints the multiplicity-only verdict", "VERDICT: MULTIPLICITY-ONLY; P3-REMAINS-EXTERNAL" in result.stdout)
    check("probe retains the three-piece external ledger", "external ledger therefore remains at THREE pieces" in result.stdout)
    check("probe preserves the exact product-rule identity", "RS(V+W) = RS(V)xS(W) + S(V)xRS(W) + S(V)xS(W), exactly" in result.stdout)

    print(f"external_datum_claim_ceiling_audit: {CHECKS - len(FAILURES)}/{CHECKS} checks passed")
    return 1 if FAILURES else 0


def selftest() -> int:
    print("SELFTEST: clean baseline FIRST")
    if audit(ROOT) != 0:
        print("BASELINE RED -- mutation results would be meaningless. ABORT.")
        return 1

    plants = (
        (LEDGER, "does not discharge P3", "discharges P3"),
        (LEDGER, "P3-REINSTATED-AS-EXTERNAL", "P3-WITHDRAWN"),
        (SOURCE_ACTION, "does not discharge SA-C3", "may discharge SA-C3"),
        (PROBE, "MULTIPLICITY-ONLY; P3-REMAINS-EXTERNAL", "COUNT-FORCED"),
    )
    ok = True
    for relpath, old, new in plants:
        with tempfile.TemporaryDirectory(prefix="gu-p3-claim-ceiling-") as tmp:
            test_root = Path(tmp)
            for source in (LEDGER, SOURCE_ACTION, PROBE):
                target = test_root / source
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / source, target)
            target = test_root / relpath
            text = target.read_text(encoding="utf-8")
            if old not in text:
                print(f"[FAIL] mutation needle missing: {relpath}: {old}")
                ok = False
                continue
            target.write_text(text.replace(old, new, 1), encoding="utf-8")
            caught = audit(test_root) == 1 and bool(FAILURES)
            print(f"  {'caught via genuine [FAIL]' if caught else 'NOT CAUGHT'}: {relpath}")
            ok = ok and caught
    print("SELFTEST " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else audit(ROOT))
