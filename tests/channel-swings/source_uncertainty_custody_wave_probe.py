#!/usr/bin/env python3
"""Mutation-backed custody gate for four source-uncertainty adherence rows."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-uncertainty-custody-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-uncertainty-custody-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-uncertainty-custody-wave-review.md"
OBJECTS = ROOT / "GEOMETER-VS-PHYSICS-OBJECTS.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def evaluate(manifest, register, producer, review, objects, toe):
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    rows = {
        "SC-GRP-04": row(register, "SC-GRP-04", "SC-GRP-05"),
        "SC-PRE-53": row(register, "SC-PRE-53", "SC-PRE-54"),
        "SC-META-53": row(register, "SC-META-53", "SC-META-54"),
        "SC-META-54": row(register, "SC-META-54", "SC-META-55"),
    }
    return [
        ("four exact records", set(records) == set(rows)),
        ("headline transition", manifest.get("headline_before") == "ADHERED 94 / PARTIAL 16 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 98 / PARTIAL 12 / UNTYPED 1"),
        ("register population current", sum(line.strip() == "adherence: ADHERED" for line in register.splitlines()) == 98 and sum(line.strip() == "adherence: PARTIAL" for line in register.splitlines()) == 12 and sum(line.strip() == "adherence: UNTYPED" for line in register.splitlines()) == 1),
        ("four rows adhered", all("adherence: ADHERED" in value and "adherence: PARTIAL" not in value for value in rows.values())),
        ("phantom ten ceiling", records.get("SC-GRP-04", {}).get("result") == "PHANTOM_TEN_CARRIER_AND_HOPED_GR_CONTACT_CARRIED_AT_SOURCE_SCOPE" and "not an action-owned map" in producer),
        ("mass scale uncertainty", records.get("SC-PRE-53", {}).get("result") == "UNKNOWN_NEW_MATTER_MASS_SCALE_AND_ASSUMED_PROHIBITION_CARRIED" and "I don't really know" in toe),
        ("no collider promotion", "no predeclared search window" in producer and "No collider recensus" in producer),
        ("max compact typed", "maximal-compact" in producer and records.get("SC-META-53", {}).get("result") == "MAXIMAL_COMPACT_CHAIN_AND_UNPROVED_SPECTRAL_SHIELDING_CARRIED"),
        ("no positivity promotion", any("positive physical state space" in fact for fact in records.get("SC-META-53", {}).get("decisive_facts", []))),
        ("section denial scoped", records.get("SC-META-54", {}).get("result") == "AUTHORIAL_GLOBAL_SECTION_DENIAL_CARRIED_WITH_SEMANTIC_UNCERTAINTY" and "not a global topology theorem" in producer),
        ("review preserves ceilings", all(token in review for token in ("no preferred", "fixes no mass", "does not imply bounded", "bundle-specific"))),
        ("no protected or verdict movement", "No source wording" in producer and "No physical mechanism" in review),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()), REGISTER.read_text(), PRODUCER.read_text(),
        REVIEW.read_text(), OBJECTS.read_text(), TOE.read_text(),
    )


def mutate_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    inputs[1] = inputs[1].replace(
        claim_row, claim_row.replace("adherence: ADHERED", "adherence: PARTIAL", 1), 1
    )


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 97 / PARTIAL 13 / UNTYPED 1"),
        lambda x: mutate_adherence(x, "SC-GRP-04", "SC-GRP-05"),
        lambda x: x[0]["records"][1].update(result="MASS_SCALE_FIXED"),
        lambda x: x[0]["records"][2]["decisive_facts"].__setitem__(2, "maximal compactness proves positivity"),
        lambda x: x[0]["records"][3].update(result="GLOBAL_NO_SECTION_THEOREM"),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-uncertainty mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source-uncertainty custody wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
