#!/usr/bin/env python3
"""Mutation-backed exact gate for the source-scope and roll-up residual wave."""

from __future__ import annotations

import copy
from math import comb
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/source-scope-and-rollup-residual-wave.json"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
PRODUCER = ROOT / "explorations/source-scope-and-rollup-residual-wave-2026-08-27.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-27-source-scope-and-rollup-residual-wave-review.md"
S9 = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
S11 = ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


def row(text: str, claim_id: str, next_id: str) -> str:
    return text.split(f"- id: {claim_id}", 1)[1].split(f"- id: {next_id}", 1)[0]


def evaluate(manifest, register, producer, review, s9, s11, toe):
    records = {entry["id"]: entry for entry in manifest.get("records", [])}
    degrees = (0, 1, 13, 14)
    dimensions = tuple(comb(14, degree) for degree in degrees)
    complement = {degree: 14 - degree for degree in degrees}
    orbits = {tuple(sorted((degree, complement[degree]))) for degree in degrees}
    claim_rows = {
        "SC-FER-03": row(register, "SC-FER-03", "SC-FER-04"),
        "SC-CHI-03": row(register, "SC-CHI-03", "SC-CHI-04"),
        "SC-PRE-03": row(register, "SC-PRE-03", "SC-META-01"),
        "SC-GEN-58": row(register, "SC-GEN-58", "SC-GEN-59"),
    }

    return [
        ("four exact records", set(records) == {"SC-FER-03", "SC-CHI-03", "SC-PRE-03", "SC-GEN-58"}),
        ("headline transition", manifest.get("headline_before") == "ADHERED 90 / PARTIAL 20 / UNTYPED 1" and manifest.get("headline_after") == "ADHERED 94 / PARTIAL 16 / UNTYPED 1"),
        ("register headline current", "ADHERED 94 / PARTIAL 16 / UNTYPED 1" in register),
        ("four rows adhered", all("adherence: ADHERED" in value and "adherence: PARTIAL" not in value for value in claim_rows.values())),
        ("p46 assignments exact", all(token in s9 for token in ("observed-fermion", "looking-glass", "dark-spinorial", "Rarita--Schwinger", "CKM", "Yukawa", "not derivations"))),
        ("p46 scope preserved", records.get("SC-FER-03", {}).get("result") == "P46_FIELD_AND_FUNCTION_ASSIGNMENTS_CARRIED_AT_SOURCE_LABEL_SCOPE" and "assignments, not derivations" in producer),
        ("p61 labels exact", "Luminous Light Standard Model Family Matter" in s11 and "Dark Decoupled Looking Glass Matter" in s11),
        ("ambient-half dimensions", 2 * 16 + 2 * 16 == 64 and 2 * 64 == 128),
        ("ambient-to-X chirality mixing", "Left handed spinors on Y do not remain exclusively Left handed" in s11 and records.get("SC-CHI-03", {}).get("result") == "P61_AMBIENT_HALF_LABELS_AND_X_CHIRALITY_BRANCHING_CARRIED"),
        ("prediction perimeter", "internal quantum" in claim_rows["SC-PRE-03"] and "energy scales" in claim_rows["SC-PRE-03"] and records.get("SC-PRE-03", {}).get("result") == "P67_ALGEBRAIC_VERSUS_ENERGY_SCALE_PREDICTION_PERIMETER_CARRIED"),
        ("released roll-up exact", "zero to one to 13 to 14" in toe and "leads to three generations" in toe),
        ("exterior dimensions", dimensions == (1, 14, 14, 1)),
        ("Hodge complement involution", all(complement[complement[d]] == d for d in degrees) and orbits == {(0, 14), (1, 13)}),
        ("no count map fence", records.get("SC-GEN-58", {}).get("result") == "ROLLED_0_1_13_14_GRAMMAR_CARRIED_WITH_NO_COUNT_MAP_FENCE" and "do not yet exhibit the required count map" in producer),
        ("producer and review scope", "No source wording" in producer and "No\nphysical mechanism" in review),
    ]


def load():
    return (
        json.loads(MANIFEST.read_text()), REGISTER.read_text(), PRODUCER.read_text(),
        REVIEW.read_text(), S9.read_text(), S11.read_text(), TOE.read_text(),
    )


def mutate_claim_adherence(inputs, claim_id: str, next_id: str) -> None:
    claim_row = row(inputs[1], claim_id, next_id)
    mutated_row = claim_row.replace("adherence: ADHERED", "adherence: PARTIAL", 1)
    inputs[1] = inputs[1].replace(claim_row, mutated_row, 1)


def selftest(inputs) -> int:
    mutators = (
        lambda x: x[0]["records"].pop(),
        lambda x: x[0].update(headline_after="ADHERED 93 / PARTIAL 17 / UNTYPED 1"),
        lambda x: mutate_claim_adherence(x, "SC-GEN-58", "SC-GEN-59"),
        lambda x: x.__setitem__(4, x[4].replace("not derivations", "derivations", 1)),
        lambda x: x.__setitem__(5, x[5].replace("Dark Decoupled Looking Glass Matter", "Dark Matter", 1)),
        lambda x: x[0]["records"][2].update(result="ENERGY_SCALE_PREDICTION_CONFIRMED"),
        lambda x: x.__setitem__(6, x[6].replace("zero to one to 13 to 14", "zero to one to 12 to 14", 1)),
        lambda x: x[0]["records"][3].update(result="THREE_GENERATIONS_DERIVED"),
    )
    caught = 0
    for mutate in mutators:
        trial = [copy.deepcopy(value) for value in inputs]
        mutate(trial)
        caught += any(not ok for _, ok in evaluate(*trial))
    print(f"source-scope roll-up mutation controls: {caught}/{len(mutators)} caught")
    return 0 if caught == len(mutators) else 1


def main() -> int:
    inputs = load()
    checks = evaluate(*inputs)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not all(ok for _, ok in checks):
        return 1
    print(f"source-scope and roll-up residual wave: PASS ({len(checks)}/{len(checks)})")
    return selftest(inputs) if "--selftest" in sys.argv else 0


if __name__ == "__main__":
    raise SystemExit(main())
