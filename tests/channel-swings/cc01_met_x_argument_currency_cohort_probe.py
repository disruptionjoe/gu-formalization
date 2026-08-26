#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-01 MET(X)-argument cohort."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
WORK_ITEM = "CC01-WAVE-2026-08-26"
CORRECTION = "CC-01-MET-X-ARGUMENT"

EXPECTED = {
    "explorations/HYPOTHESIS-moduli-negative-not-time-negative-2026-08-09.md",
    "explorations/analytic-index-fredholm/oq-rs3-gu-vasiliev-comparison-2026-06-23.md",
    "explorations/conditional-build/selected-action-coupled-diffeomorphism-ward-retype-2026-08-06.md",
    "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
    "explorations/dark-energy-cosmology/dark-energy-divergence-free-proof-2026-06-22.md",
    "explorations/generation-sector/oq3a-k3-variational-selection-2026-06-23.md",
    "explorations/generation-sector/oq3a-willmore-k3-selection-2026-06-23.md",
    "explorations/generation-sector/oq3b-rs-index-8-2026-06-23.md",
    "explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md",
    "explorations/geometry-curvature-emergence/hc1-codazzi-correction-2026-06-23.md",
    "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md",
    "explorations/misc/six-axis-l1l2-coupling-filled-example-2026-06-23.md",
    "explorations/perspective-and-dialectic/4d-reduction-62-perspective-steelman-hegelian-2026-06-22.md",
    "explorations/perspective-and-dialectic/entropic-gravity-antithesis-information-first-2026-07-07.md",
    "explorations/perspective-and-dialectic/gu-vs-entropic-gravity-hegelian-2026-07-07.md",
    "explorations/perspective-and-dialectic/perspective-review-foundational-math-2026-06-24.md",
    "explorations/research-cycles/hourly-20260625-2104-cycle3-qft-branch-admissibility-map-gate.md",
    "explorations/research-cycles/hourly-cycle3-freed-hopkins-xobs-ic4-verification-gate-2026-06-24.md",
    "explorations/shiab-operator/sc1-oq2c-null-mode-interpretation-2026-06-23.md",
    "explorations/time-as-finality-crosswalk/freed-hopkins-xobs-sol-k3-moduli-2026-06-23.md",
    "explorations/vz-evasion/vz1-oq3-gravitational-vz-weyl-tensor-2026-06-23.md",
    "lab/process/NAMES.md",
}

SCOPE_TOKENS = ("action", "section", "comparator", "reference", "gimmel", "candidate")


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
    actual = [
        (str(row.get("file")), str(row.get("correction_id")))
        for row in selected
    ]
    expected = {(path, CORRECTION) for path in EXPECTED}
    if set(actual) != expected:
        failures.append("cohort membership differs from the twenty-two reviewed pairs")
    if len(actual) != len(set(actual)):
        failures.append("cohort contains a duplicate file/correction pair")
    for row in selected:
        if row.get("verdict") != "CLEARED-CONSISTENT":
            failures.append(f"wrong verdict for {row.get('file')}")
        note = str(row.get("note", "")).lower()
        if "metric" not in note or not any(token in note for token in SCOPE_TOKENS):
            failures.append(f"scope note missing for {row.get('file')}")
        if not (ROOT / str(row.get("file"))).is_file():
            failures.append(f"missing reviewed file {row.get('file')}")
    return failures


def validate_dynamic() -> list[str]:
    failures: list[str] = []
    audit = load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-26"
    result = audit.compute(cfg)
    row = result["per"][CORRECTION]
    if row["dirty"] != 0 or row["unchecked"] or row["known_stale"]:
        failures.append("CC-01 remains dirty")
    if not EXPECTED.issubset(set(row["cleared"])):
        failures.append("CC-01 did not clear every reviewed candidate")
    live_dirty = sum(item["dirty"] for item in result["per"].values())
    if live_dirty != 137:
        failures.append(f"live dirty queue is {live_dirty}, expected 137")
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
    trial[selected_indexes[-1]]["correction_id"] = "CC-02-OBSERVED-POSITIVITY-OPEN"
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
    print("[PASS] complete CC-01 cohort clears with exact semantic-scope records")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 25/25 missing, duplicate, verdict and correction mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
