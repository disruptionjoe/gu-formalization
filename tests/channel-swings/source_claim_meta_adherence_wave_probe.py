#!/usr/bin/env python3
"""Coupled certificate for the 2026-08-25 source-meta adherence wave."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
CERT = ROOT / "lab/process/source-meta-philosophy-and-process-adherence.json"
ARTIFACT = ROOT / "explorations/sc-meta-philosophy-and-process-adherence-2026-08-25.md"
README = ROOT / "README.md"
POSTURE = ROOT / "RESEARCH-POSTURE.md"
CORRECTIONS = ROOT / "lab/process/correction-registry.yaml"
MUTATE = os.environ.get("SOURCE_META_ADHERENCE_MUTATE", "")
MUTATIONS = (
    "meta02_overpromote",
    "meta02_drop_fence",
    "meta51_demote",
    "meta51_physics_overclaim",
    "sig55_promote",
    "count_drift",
)


def load() -> tuple[dict, dict[str, dict], dict, str, str, str, str]:
    register = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))
    rows = {row["id"]: row for row in register["claims"]}
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
    return (
        register,
        rows,
        certificate,
        ARTIFACT.read_text(encoding="utf-8"),
        README.read_text(encoding="utf-8"),
        POSTURE.read_text(encoding="utf-8"),
        CORRECTIONS.read_text(encoding="utf-8"),
    )


def evaluate(register: dict, rows: dict[str, dict], certificate: dict,
             artifact: str, readme: str, posture: str, corrections: str) -> list[tuple[str, bool]]:
    artifact_flat = " ".join(artifact.split())
    counts = {
        key: sum(row["adherence"]["adherence"] == key for row in rows.values())
        for key in ("ADHERED", "PARTIAL", "UNTYPED")
    }
    untyped = {
        identifier for identifier, row in rows.items()
        if row["adherence"]["adherence"] == "UNTYPED"
    }
    headline = " ".join(register["register"]["adjudication_headline"].split())
    checks = [
        ("register contains 111 unique claims", len(rows) == len(register["claims"]) == 111),
        ("current adherence counts are 86/24/1", counts == {"ADHERED": 86, "PARTIAL": 24, "UNTYPED": 1}),
        ("headline prints 86/24/1", "ADHERED 86 / PARTIAL 24 / UNTYPED 1" in headline),
        ("SC-META-02 remains ASSERTS and PARTIAL", rows["SC-META-02"]["polarity"] == "ASSERTS" and rows["SC-META-02"]["adherence"]["adherence"] == "PARTIAL"),
        ("SC-META-51 remains ASSERTS and ADHERED", rows["SC-META-51"]["polarity"] == "ASSERTS" and rows["SC-META-51"]["adherence"]["adherence"] == "ADHERED"),
        ("SC-SIG-55 is the sole UNTYPED residual", untyped == {"SC-SIG-55"}),
        ("SC-SIG-55 remains expositor belief", rows["SC-SIG-55"]["polarity"] == "CURT-ATTRIBUTES-TO-AUTHOR" and "expositor's belief" in rows["SC-SIG-55"]["notes"]),
        ("gambit source wording retained", "This cannot of course be proven" in rows["SC-META-02"]["verbatim"]),
        ("process source wording retained", "We're fumbling" in rows["SC-META-51"]["verbatim"]),
        ("artifact preserves PARTIAL falsifiability fence", "stops at `PARTIAL`" in artifact_flat and "Natural emergence and resemblance" in artifact_flat),
        ("artifact forbids process-as-physics overclaim", "never physics evidence" in artifact_flat and "process discipline is a method product" in artifact_flat),
        ("artifact preserves expositor residual", "`SC-SIG-55` remains the sole `UNTYPED` row" in artifact_flat),
        ("repository charter supplies comparative abduction", "Best-arena abduction" in readme and "Refutation-survival" in readme),
        ("research posture refuses advocacy", "We do not optimize to prove GU" in posture and "process discipline as physics evidence" in posture),
        ("correction registry remains machine readable", "canonical_source_corrections:" in corrections),
        ("certificate mirrors current counts", certificate["register_after"] == counts),
        ("certificate hostile controls close", certificate["hostile_controls"]["caught"] == certificate["hostile_controls"]["count"] == len(MUTATIONS)),
        ("protected effects remain none", all(value == "none" for value in certificate["effect"].values())),
        ("artifact carries routing classification", "GU-COMPARATOR-ROUTING" in artifact and "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`" in artifact),
        ("artifact carries typed objects", "```gu-typed-objects" in artifact),
    ]
    return checks


def mutate(register: dict, rows: dict[str, dict], certificate: dict, artifact: str, name: str) -> str:
    if name == "meta02_overpromote":
        rows["SC-META-02"]["adherence"]["adherence"] = "ADHERED"
    elif name == "meta02_drop_fence":
        artifact = artifact.replace("stops at `PARTIAL`", "confirms the gambit")
    elif name == "meta51_demote":
        rows["SC-META-51"]["adherence"]["adherence"] = "UNTYPED"
    elif name == "meta51_physics_overclaim":
        artifact = artifact.replace("process discipline is a method product", "process discipline validates the theory")
    elif name == "sig55_promote":
        rows["SC-SIG-55"]["adherence"]["adherence"] = "ADHERED"
    elif name == "count_drift":
        certificate["register_after"]["ADHERED"] = 87
    return artifact


def run() -> int:
    register, rows, certificate, artifact, readme, posture, corrections = load()
    if MUTATE:
        artifact = mutate(register, rows, certificate, artifact, MUTATE)
    checks = evaluate(register, rows, certificate, artifact, readme, posture, corrections)
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"SOURCE-META-ADHERENCE: {sum(ok for _, ok in checks)}/{len(checks)} checks pass")
    return 0 if all(ok for _, ok in checks) else 1


def selftest() -> int:
    clean = dict(os.environ)
    clean.pop("SOURCE_META_ADHERENCE_MUTATE", None)
    baseline = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=clean, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("FAIL baseline")
        print(baseline.stdout)
        return 1
    caught = 0
    for name in MUTATIONS:
        env = dict(os.environ, SOURCE_META_ADHERENCE_MUTATE=name)
        result = subprocess.run([sys.executable, str(Path(__file__).resolve())], env=env, capture_output=True, text=True)
        genuine = result.returncode == 1 and "[FAIL]" in result.stdout
        print(f"mutation {name:26s}: {'CAUGHT' if genuine else 'MISSED'}")
        caught += int(genuine)
    print(f"SELFTEST: {caught}/{len(MUTATIONS)} mutations caught")
    return 0 if caught == len(MUTATIONS) else 1


if __name__ == "__main__":
    raise SystemExit(selftest() if "--selftest" in sys.argv or "--self-test" in sys.argv else run())
