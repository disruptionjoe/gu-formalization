#!/usr/bin/env python3
"""Certificate for the residual source-claim typing wave.

The probe pins the primary loci, the honest adherence ceilings, the exact
intentionally-UNTYPED residual, and the three owner artifacts.  Its selftest
first proves a clean baseline and counts only genuine failing checks.
"""

from __future__ import annotations

import copy
import os
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PORTAL = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
EXTRACTION = ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
ARTIFACTS = {
    "SC-SIG-53": ROOT / "explorations/sc-sig53-source-sign-uncertainty-audit-2026-08-24.md",
    "SC-GENERATION": ROOT / "explorations/sc-generation-language-caveat-audit-2026-08-24.md",
    "SC-PRE-50": ROOT / "explorations/sc-pre50-lhc-superpartner-prediction-typing-2026-08-24.md",
}
MUTATE = os.environ.get("SOURCE_RESIDUAL_TYPING_MUTATE", "")
MUTATIONS = (
    "sig_polarity",
    "sig_promote",
    "generation_reopen",
    "mass_flavor_drop",
    "pre_confirm",
    "pre_promote",
    "residual_shrink",
    "count_drift",
)


def load() -> tuple[dict, dict[str, dict], dict[str, str]]:
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    rows = {row["id"]: row for row in data["claims"]}
    artifacts = {key: path.read_text(encoding="utf-8") for key, path in ARTIFACTS.items()}
    return data, rows, artifacts


def evaluate(data: dict, rows: dict[str, dict], artifacts: dict[str, str]) -> list[tuple[str, bool]]:
    portal = PORTAL.read_text(encoding="utf-8")
    toe = TOE.read_text(encoding="utf-8")
    extraction = EXTRACTION.read_text(encoding="utf-8")
    extraction_flat = " ".join(extraction.split())
    signature_flat = " ".join(artifacts["SC-SIG-53"].split())
    adherences = {key: sum(row["adherence"]["adherence"] == key for row in rows.values())
                  for key in ("ADHERED", "PARTIAL", "UNTYPED")}
    untyped = {identifier for identifier, row in rows.items()
               if row["adherence"]["adherence"] == "UNTYPED"}
    checks = [
        ("register contains 111 unique claims", len(rows) == len(data["claims"]) == 111),
        ("adherence counts are 85/23/3", adherences == {"ADHERED": 85, "PARTIAL": 23, "UNTYPED": 3}),
        ("headline prints 85/23/3", "ADHERED 85 / PARTIAL 23 / UNTYPED 3" in data["register"]["adjudication_headline"]),
        ("intentional UNTYPED residual is exact", untyped == {"SC-META-02", "SC-SIG-55", "SC-META-51"}),
        ("SC-SIG-53 polarity remains UNCERTAIN", rows["SC-SIG-53"]["polarity"] == "UNCERTAIN"),
        ("SC-SIG-53 is ADHERED", rows["SC-SIG-53"]["adherence"]["adherence"] == "ADHERED"),
        ("SC-META-05 is ADHERED", rows["SC-META-05"]["adherence"]["adherence"] == "ADHERED"),
        ("SC-GEN-52 polarity remains UNCERTAIN", rows["SC-GEN-52"]["polarity"] == "UNCERTAIN"),
        ("SC-GEN-52 is ADHERED", rows["SC-GEN-52"]["adherence"]["adherence"] == "ADHERED"),
        ("SC-PRE-50 polarity remains DISAVOWS", rows["SC-PRE-50"]["polarity"] == "DISAVOWS"),
        ("SC-PRE-50 remains PARTIAL", rows["SC-PRE-50"]["adherence"]["adherence"] == "PARTIAL"),
        ("primary sign uncertainty is present", "we seem to be off by a sign somewhere, or I could be mistaken" in portal),
        ("primary gamma-language uncertainty is present", "Gamma trace, gamma traceless" in toe and "I don't know if that's the right language" in toe),
        ("primary mass/flavor caveat is present", "mass eigenstates and flavor eigenstates were one and the same" in extraction_flat),
        ("primary superpartner disavowal is present", "you will never see super partners" in toe and "spill out of the LHC" in toe),
        ("signature artifact forbids horn selection", "zero horn-selection power" in artifacts["SC-SIG-53"] and "cannot choose" in signature_flat),
        ("generation artifact preserves J5", "RESOLVED(A)" in artifacts["SC-GENERATION"] and "mass and flavor eigenstates" in artifacts["SC-GENERATION"]),
        ("superpartner artifact refuses confirmation", "no current non-observation is counted as confirmation" in artifacts["SC-PRE-50"]),
        ("all artifacts carry routing classification", all("Classification: `" in text and "GU-COMPARATOR-ROUTING" in text for text in artifacts.values())),
        ("all artifacts carry typed objects", all("```gu-typed-objects" in text for text in artifacts.values())),
    ]
    return checks


def mutate(data: dict, rows: dict[str, dict], artifacts: dict[str, str], name: str) -> None:
    if name == "sig_polarity":
        rows["SC-SIG-53"]["polarity"] = "ASSERTS"
    elif name == "sig_promote":
        artifacts["SC-SIG-53"] = artifacts["SC-SIG-53"].replace("zero horn-selection power", "horn selected")
    elif name == "generation_reopen":
        artifacts["SC-GENERATION"] = artifacts["SC-GENERATION"].replace("RESOLVED(A)", "OPEN")
    elif name == "mass_flavor_drop":
        artifacts["SC-GENERATION"] = artifacts["SC-GENERATION"].replace("mass and flavor eigenstates", "two bases")
    elif name == "pre_confirm":
        artifacts["SC-PRE-50"] = artifacts["SC-PRE-50"].replace("no current non-observation is counted as confirmation", "current non-observation confirms the claim")
    elif name == "pre_promote":
        rows["SC-PRE-50"]["adherence"]["adherence"] = "ADHERED"
    elif name == "residual_shrink":
        rows["SC-SIG-55"]["adherence"]["adherence"] = "ADHERED"
    elif name == "count_drift":
        data["register"]["adjudication_headline"] = data["register"]["adjudication_headline"].replace("ADHERED 85", "ADHERED 86")


def run() -> int:
    data, rows, artifacts = load()
    if MUTATE:
        mutate(data, rows, artifacts, MUTATE)
    checks = evaluate(data, rows, artifacts)
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"SOURCE-RESIDUAL-TYPING: {sum(ok for _, ok in checks)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok in checks) else 1


def selftest() -> int:
    print("SELFTEST: verifying clean baseline before mutations")
    clean = dict(os.environ)
    clean.pop("SOURCE_RESIDUAL_TYPING_MUTATE", None)
    baseline = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=clean, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("FAIL baseline")
        print(baseline.stdout)
        return 1
    caught = 0
    for name in MUTATIONS:
        env = dict(os.environ, SOURCE_RESIDUAL_TYPING_MUTATE=name)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=env, capture_output=True, text=True)
        genuine = result.returncode == 1 and "[FAIL]" in result.stdout
        print(f"mutation {name:20s}: {'CAUGHT' if genuine else 'MISSED'}")
        caught += int(genuine)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv or "--self-test" in sys.argv else run())
