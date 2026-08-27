#!/usr/bin/env python3
"""Mutation-backed gate for four intentional residual source boundaries."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-residual-terminalization-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-residual-terminalization-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-residual-terminalization-wave-review.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def evaluate(manifest, register, producer, review, toe):
    register_flat = " ".join(register.split())
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    rows = {
        "SC-META-02": row(register, "SC-META-02", "SC-META-03"),
        "SC-GEN-53": row(register, "SC-GEN-53", "SC-GEN-54"),
        "SC-SIG-51": row(register, "SC-SIG-51", "SC-SIG-52"),
        "SC-PRE-50": row(register, "SC-PRE-50", "SC-PRE-51"),
    }
    return [
        ("four exact records", set(records) == set(rows)),
        ("headline unchanged", manifest.get("headline_before") == "ADHERED 106 / PARTIAL 4 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 106 / PARTIAL 4 / UNTYPED 1"),
        ("headline and population current", "ADHERED 106 / PARTIAL 4 / UNTYPED 1" in register_flat and sum(line.strip() == "adherence: ADHERED" for line in register.splitlines()) == 106 and sum(line.strip() == "adherence: PARTIAL" for line in register.splitlines()) == 4 and sum(line.strip() == "adherence: UNTYPED" for line in register.splitlines()) == 1),
        ("four rows remain partial", all("adherence: PARTIAL" in value and "TERMINAL_AT_CURRENT_EVIDENCE" in value for value in rows.values())),
        ("terminal states exact", all(entry.get("terminal_state", "").startswith("TERMINAL_") and entry.get("exact_reopener") for entry in records.values())),
        ("philosophy ceiling", records.get("SC-META-02", {}).get("result") == "NATURAL_UNIFYING_ARENA_GAMBIT_CARRIED_WITHOUT_LIKELY_CORRECTNESS_INFERENCE" and "cannot of course be proven" in register_flat and "likely-correctness inference" in producer),
        ("prediction ceiling", records.get("SC-GEN-53", {}).get("result") == "TWO_PLUS_ONE_HIGH_ENERGY_ASSERTION_CARRIED_WITHOUT_PHYSICAL_PREDICTION_PACKET" and "two of them will" in toe and "not a prediction" in producer),
        ("selector ceiling", records.get("SC-SIG-51", {}).get("result") == "FOUR_NORMALIZED_FORMS_CARRIED_WITH_UNOWNED_EXPERIMENTAL_SELECTOR" and "two obvious ones are ruled out by experiment" in toe and "zero owned experiment-to-form map" in producer),
        ("collider ceiling", records.get("SC-PRE-50", {}).get("result") == "CONVENTIONAL_SUPERPARTNER_DISAVOWAL_CARRIED_WITH_UNDEFINED_UNIVERSAL_TARGET" and "spill out of the LHC" in toe and "not preregistered confirmation" in producer),
        ("untyped residual preserved", manifest.get("excluded_residual", {}).get("id") == "SC-SIG-55" and manifest["excluded_residual"].get("adherence") == "UNTYPED"),
        ("no status promotions", "All four rows remain `PARTIAL`" in review and "No source polarity" in producer),
        ("typed object declaration", "```gu-typed-objects" in producer and "action_owner:" in producer),
        ("source polarities preserved", records and all("polarity:" in value for value in rows.values())),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()),
        REGISTER.read_text(),
        PRODUCER.read_text(),
        REVIEW.read_text(),
        TOE.read_text(),
    )


def mutate_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    inputs[1] = inputs[1].replace(
        claim_row, claim_row.replace("adherence: PARTIAL", "adherence: ADHERED", 1), 1
    )


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 107 / PARTIAL 3 / UNTYPED 1"),
        lambda x: mutate_adherence(x, "SC-META-02", "SC-META-03"),
        lambda x: x[0]["records"][1].update(result="PHYSICAL_HIGH_ENERGY_PREDICTION"),
        lambda x: x[0]["records"][2].update(result="EXPERIMENT_SELECTS_TRACE_REVERSED_PAIR"),
        lambda x: x[0]["records"][3].update(result="LHC_NULL_CONFIRMS_GU"),
        lambda x: x[0]["records"][0].update(exact_reopener=""),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-residual mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source residual terminalization wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
