#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-02 and CC-08 cohorts."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
WORK_ITEM = "CC0208-WAVE-2026-08-25"

EXPECTED = {
    "CC-02-OBSERVED-POSITIVITY-OPEN": {
        "explorations/W123-native-r2-running-sign-convention-audit-2026-07-13.md",
        "explorations/W143-steelman-sweep-applied-frontier-2026-07-14.md",
        "explorations/W170-turok-bateman-nonperturbative-2026-07-14.md",
        "explorations/blockbuster-p3-one-bit-dossier-v2-2026-07-19.md",
        "explorations/geometry-curvature-emergence/pc4-torsion-lambda-derivation-2026-06-23.md",
        "explorations/krein-ratio-set-tail-coherence-2026-07-11.md",
        "explorations/n2-end-family-2026-07-20.md",
        "explorations/path2-wave1-synthesis-and-wave2-design-2026-07-11.md",
        "explorations/path5-branchA-krein-modular-conjugation-2026-07-11.md",
        "explorations/wave-swing1-the-lemma-2026-07-21.md",
        "explorations/wave39/H54-branch3-PS-as-susy-ward-2026-07-11.md",
    },
    "CC-08-DARK-PARTNER-OBLIGATION": {
        "explorations/research-cycles/hourly-20260625-0601-cycle1-author-manuscript-rs-rule-extraction-candidate.md",
        "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md",
        "lab/process/hostile-reviews/2026-08-03-imposter-ab-review.md",
        "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md",
    },
}

NOTE_TOKENS = {
    "CC-02-OBSERVED-POSITIVITY-OPEN": ("quotient", "source"),
    "CC-08-DARK-PARTNER-OBLIGATION": ("obligation", "source"),
}


def load_audit():
    spec = importlib.util.spec_from_file_location("canonical_currency_audit", AUDIT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load canonical-currency audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_records(records: list[dict]) -> list[str]:
    failures: list[str] = []
    selected = [row for row in records if row.get("by") == WORK_ITEM]
    expected_pairs = {
        (path, correction_id)
        for correction_id, paths in EXPECTED.items()
        for path in paths
    }
    actual_pairs = [
        (str(row.get("file")), str(row.get("correction_id")))
        for row in selected
    ]
    if set(actual_pairs) != expected_pairs:
        failures.append("cohort membership differs from the fifteen reviewed pairs")
    if len(actual_pairs) != len(set(actual_pairs)):
        failures.append("cohort contains a duplicate file/correction pair")
    for row in selected:
        correction_id = str(row.get("correction_id"))
        if row.get("verdict") != "CLEARED-CONSISTENT":
            failures.append(f"wrong verdict for {row.get('file')}")
        note = str(row.get("note", "")).lower()
        tokens = NOTE_TOKENS.get(correction_id, ())
        if tokens and not any(token in note for token in tokens):
            failures.append(f"scope note missing for {row.get('file')}")
        if not (ROOT / str(row.get("file"))).is_file():
            failures.append(f"missing reviewed file {row.get('file')}")
    return failures


def validate_dynamic() -> list[str]:
    failures: list[str] = []
    audit = load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-25"
    result = audit.compute(cfg)
    for correction_id, paths in EXPECTED.items():
        row = result["per"][correction_id]
        if row["dirty"] != 0 or row["unchecked"] or row["known_stale"]:
            failures.append(f"{correction_id} remains dirty")
        if not paths.issubset(set(row["cleared"])):
            failures.append(f"{correction_id} did not clear every reviewed candidate")
    live_dirty = sum(row["dirty"] for row in result["per"].values())
    if live_dirty != 159:
        failures.append(f"live dirty queue is {live_dirty}, expected 159")
    return failures


def selftest(records: list[dict]) -> list[str]:
    escaped: list[str] = []
    selected_indexes = [
        index for index, row in enumerate(records) if row.get("by") == WORK_ITEM
    ]
    for index in selected_indexes:
        trial = copy.deepcopy(records)
        trial.pop(index)
        if not validate_records(trial):
            escaped.append(f"missing-record mutation {index} escaped")
    trial = copy.deepcopy(records)
    trial.append(copy.deepcopy(records[selected_indexes[0]]))
    if not validate_records(trial):
        escaped.append("duplicate-record mutation escaped")
    trial = copy.deepcopy(records)
    trial[selected_indexes[0]]["verdict"] = "STALE-FOUND"
    if not validate_records(trial):
        escaped.append("wrong-verdict mutation escaped")
    trial = copy.deepcopy(records)
    trial[selected_indexes[-1]]["correction_id"] = "CC-01-MET-X-ARGUMENT"
    if not validate_records(trial):
        escaped.append("wrong-correction mutation escaped")
    return escaped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    sidecar = yaml.safe_load(SIDECAR.read_text(encoding="utf-8"))
    records = sidecar.get("checks", [])
    failures = validate_records(records)
    failures.extend(validate_dynamic())
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] complete CC-02/CC-08 cohorts clear with exact scope records")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 18/18 missing, duplicate, verdict and correction mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
