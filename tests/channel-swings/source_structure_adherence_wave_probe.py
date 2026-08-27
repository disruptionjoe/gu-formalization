#!/usr/bin/env python3
"""Mutation-backed custody gate for four structural source-adherence rows."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-structure-adherence-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-structure-adherence-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-structure-adherence-wave-review.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"
PORTAL = ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def evaluate(manifest, register, producer, review, toe, portal):
    register_flat = " ".join(register.split())
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    rows = {
        "SC-GRP-50": row(register, "SC-GRP-50", "SC-OP-01"),
        "SC-GEN-54": row(register, "SC-GEN-54", "SC-GEN-55"),
        "SC-GEO-50": row(register, "SC-GEO-50", "SC-GEO-51"),
        "SC-GEO-53": row(register, "SC-GEO-53", "SC-GEO-54"),
    }
    return [
        ("four exact records", set(records) == set(rows)),
        ("headline transition", manifest.get("headline_before") == "ADHERED 102 / PARTIAL 8 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 106 / PARTIAL 4 / UNTYPED 1"),
        ("headline and population current", "ADHERED 106 / PARTIAL 4 / UNTYPED 1" in register_flat and sum(line.strip() == "adherence: ADHERED" for line in register.splitlines()) == 106 and sum(line.strip() == "adherence: PARTIAL" for line in register.splitlines()) == 4 and sum(line.strip() == "adherence: UNTYPED" for line in register.splitlines()) == 1),
        ("four rows adhered", all("adherence: ADHERED" in value and "adherence: PARTIAL" not in value for value in rows.values())),
        ("chain ceiling", records.get("SC-GRP-50", {}).get("result") == "BEST_SUPPORTED_NONCOMPACT_CHAIN_CARRIED_WITH_PERMANENT_TRANSCRIPT_AND_REDUCTION_CEILINGS" and "transcript-uncertain" in producer and "global reduction" in review),
        ("count ceiling", records.get("SC-GEN-54", {}).get("result") == "SUPERCHARGE_TO_THREE_ASSERTION_CARRIED_WITHOUT_PHYSICAL_COUNT_MAP" and "include supercharges" in toe and "physical generation theorem" in producer),
        ("tower ceiling", records.get("SC-GEO-50", {}).get("result") == "BASE_TO_TOTAL_DIMENSION_AND_HIGHER_SECTOR_TOWER_ASSERTION_CARRIED" and "one in seven" in toe and "no inter-level map exists" in producer),
        ("emergence ceiling", records.get("SC-GEO-53", {}).get("result") == "CONNECTION_FUNDAMENTAL_METRIC_EMERGENT_REVERSAL_CARRIED_WITH_BASE_FIBRE_SCOPE_SPLIT" and "metric that’s emergent" in portal and "base metric" in producer),
        ("no physical promotions", "No global reduction" in review and "generation-count theorem" in review and "persistence theorem" in review),
        ("review preserves scientific null", "changes no protected path" in review and "No source wording" in producer),
        ("typed object declaration", "```gu-typed-objects" in producer and "action_owner:" in producer),
        ("source polarities preserved", all("polarity: ASSERTS" in value for value in rows.values())),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()),
        REGISTER.read_text(),
        PRODUCER.read_text(),
        REVIEW.read_text(),
        TOE.read_text(),
        PORTAL.read_text(),
    )


def mutate_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    inputs[1] = inputs[1].replace(
        claim_row, claim_row.replace("adherence: ADHERED", "adherence: PARTIAL", 1), 1
    )


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 105 / PARTIAL 5 / UNTYPED 1"),
        lambda x: mutate_adherence(x, "SC-GRP-50", "SC-OP-01"),
        lambda x: x[0]["records"][1].update(result="THREE_PHYSICAL_GENERATIONS_PROVED"),
        lambda x: x[0]["records"][2].update(result="HIGHER_SECTOR_PERSISTENCE_PROVED"),
        lambda x: x[0]["records"][3].update(result="ALL_METRICS_EMERGENT"),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-structure mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source-structure adherence wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
