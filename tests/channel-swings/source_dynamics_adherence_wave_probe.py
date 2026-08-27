#!/usr/bin/env python3
"""Mutation-backed custody gate for four source-dynamics adherence rows."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-dynamics-adherence-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-dynamics-adherence-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-dynamics-adherence-wave-review.md"
TRANSCRIPT = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def evaluate(manifest, register, producer, review, transcript):
    register_flat = " ".join(register.split())
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    rows = {
        "SC-ACT-06": row(register, "SC-ACT-06", "SC-FER-01"),
        "SC-CHI-52": row(register, "SC-CHI-52", "SC-CHI-53"),
        "SC-CHI-53": row(register, "SC-CHI-53", "SC-CHI-54"),
        "SC-PRE-54": row(register, "SC-PRE-54", "SC-PRE-55"),
    }
    return [
        ("four exact records", set(records) == set(rows)),
        ("headline transition", manifest.get("headline_before") == "ADHERED 98 / PARTIAL 12 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 102 / PARTIAL 8 / UNTYPED 1"),
        ("headline and population current", "ADHERED 102 / PARTIAL 8 / UNTYPED 1" in register_flat and sum(line.strip() == "adherence: ADHERED" for line in register.splitlines()) == 102 and sum(line.strip() == "adherence: PARTIAL" for line in register.splitlines()) == 8 and sum(line.strip() == "adherence: UNTYPED" for line in register.splitlines()) == 1),
        ("four rows adhered", all("adherence: ADHERED" in value and "adherence: PARTIAL" not in value for value in rows.values())),
        ("Euclidean ceiling", records.get("SC-ACT-06", {}).get("result") == "EUCLIDEAN_MODULI_AND_ELLIPTICITY_ASSERTION_CARRIED_WITHOUT_THEOREM" and "do not refute the distinct Euclidean claim" in producer),
        ("curvature mass ceiling", records.get("SC-CHI-52", {}).get("result") == "CURVATURE_VEV_MASS_AND_DIRAC_WEYL_CHAIN_CARRIED_WITH_MISSING_DYNAMICS" and "supplies no positive threshold" in producer),
        ("belief grade preserved", records.get("SC-CHI-53", {}).get("result") == "BELIEF_GRADED_LUMINOUS_DARK_RECONNECTION_CHAIN_CARRIED" and "what I believe" in transcript and "belief-graded" in producer),
        ("higher-sector ceiling", records.get("SC-PRE-54", {}).get("result") == "HIGHER_SECTOR_STABLE_DIMENSION_AND_RECONNECTION_ASSERTION_CARRIED" and "neither an inter-level representation" in producer),
        ("no dark identity", "source's dark matter" in producer and "not a dark-matter identification" in review),
        ("no prediction promotion", "not yet a testable prediction" in producer and "prediction, confirmation" in review),
        ("review preserves scientific null", "proves no Euclidean ellipticity" in review and "No source polarity" in review),
        ("typed object declaration", "```gu-typed-objects" in producer and "action_owner:" in producer),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()),
        REGISTER.read_text(),
        PRODUCER.read_text(),
        REVIEW.read_text(),
        TRANSCRIPT.read_text(),
    )


def mutate_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    inputs[1] = inputs[1].replace(
        claim_row, claim_row.replace("adherence: ADHERED", "adherence: PARTIAL", 1), 1
    )


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 101 / PARTIAL 9 / UNTYPED 1"),
        lambda x: mutate_adherence(x, "SC-ACT-06", "SC-FER-01"),
        lambda x: x[0]["records"][1].update(result="MASS_LAW_PROVED"),
        lambda x: x[0]["records"][2].update(result="DARK_MATTER_IDENTIFIED"),
        lambda x: x[0]["records"][3].update(result="PREDICTION_CONFIRMED"),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-dynamics mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source-dynamics adherence wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
