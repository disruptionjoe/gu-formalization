#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-10 UCSD-provenance cohort."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
CORRECTION = "CC-10-UCSD-EDITED-DERIVATIVE"
WAVE = "CC10-WAVE-2026-08-26"
REPAIR = "CC10-REPAIR-2026-08-26"

EXPECTED = {
    "explorations/big-swing-2026-07-06/CROSS-EXAM-weinstein-turok-mannheim-first-principles.md",
    "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
    "explorations/dk-chirality-fork-2026-07-20.md",
    "explorations/eric-curt-wave3d-b2c2-null-clifford-omega1-completion-2026-07-31.md",
    "explorations/eric-native-physics-equation-replacement-atlas-2026-07-31.md",
    "explorations/nguyen-gu-critique/nguyen-critique-full-synthesis.md",
    "explorations/research-cycles/hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md",
    "explorations/research-cycles/hourly-20260625-0103-cycle2-dgu-primary-source-locator.md",
    "explorations/research-cycles/hourly-20260625-0103-cycle2-rs-source-action-noether-locator.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle1-ucsd-transcript-receipt-mining-packet.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle2-family-proof-restart-classifier.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle2-negative-receipt-quarantine-policy.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle2-source-surface-coverage-delta-ledger.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle3-ucsd-visual-slide-capture-batch.md",
    "explorations/research-cycles/hourly-20260625-0703-cycle1-qft-alternate-primary-source-query-execution.md",
    "explorations/research-cycles/hourly-20260625-0703-cycle2-qft-complete-transcript-frame-acquisition-gate.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle3-global-negative-precondition-matrix.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle3-proof-restart-readiness-classifier.md",
    "explorations/research-cycles/hourly-20260625-1302-cycle1-dgu-identity-witness.md",
    "explorations/research-cycles/hourly-20260625-1302-cycle3-global-negative-precondition-matrix.md",
    "explorations/research-cycles/hourly-20260625-1503-cycle1-dgu-identity-field-receipt-bundle.md",
    "explorations/research-cycles/hourly-20260625-1503-cycle3-global-negative-precondition-matrix.md",
    "explorations/research-cycles/hourly-20260625-1602-cycle3-claim-promotion-firewall.md",
    "explorations/research-cycles/hourly-20260625-1702-cycle2-dgu-sector-rule-same-operator-matrix.md",
    "explorations/research-cycles/hourly-20260625-2104-cycle2-dgu-source-stable-row-packet.md",
    "explorations/research-cycles/hourly-20260625-2302-cycle1-dgu-sector-rule-producer-contract.md",
    "explorations/research-cycles/hourly-20260626-0502-cycle1-negative-primary-dgu-source-receipt.md",
    "explorations/research-cycles/hourly-20260626-0502-cycle2-dgu-source-scope-expansion-receipt.md",
    "explorations/research-cycles/hourly-20260626-0502-cycle3-dgu-source-acquisition-transition-closeout.md",
    "explorations/research-cycles/hourly-20260626-0701-cycle1-positive-primary-source-dgu-row-candidate.md",
    "explorations/research-cycles/hourly-20260626-0701-cycle2-dgu-sector-rule-family-identity-delta-packet.md",
    "explorations/research-cycles/hourly-20260626-0701-cycle3-dgu-scoped-negative-delta-receipt-classifier.md",
    "explorations/research-cycles/hourly-20260626-1003-cycle3-kig-primary-source-locator-row.md",
    "explorations/research-cycles/hourly-20260626-1102-cycle1-kig-parent-variation-acquisition-extraction-row.md",
    "explorations/source-domain-selector-prongA-extraction-2026-07-21.md",
    "lab/process/improvement-register-2026-08-03.md",
    "lab/sources/full-norm-gravity-source-reinspection-2026-08-05.md",
    "lab/sources/k77-epsilon-gravitational-soldering-weld-source-reinspection-2026-08-05.md",
    "lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md",
    "lab/sources/selected-k77-curvature-vev-trace-source-reinspection-2026-08-09.md",
    "lab/sources/selected-k77-physical-diffeomorphism-split-source-reinspection-2026-08-08.md",
}

REPAIRED = {
    "explorations/big-swing-2026-07-06/CROSS-EXAM-weinstein-turok-mannheim-first-principles.md",
    "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md",
    "explorations/nguyen-gu-critique/nguyen-critique-full-synthesis.md",
    "explorations/research-cycles/hourly-20260625-0103-cycle2-dgu-primary-source-locator.md",
    "explorations/research-cycles/hourly-20260625-0103-cycle2-rs-source-action-noether-locator.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle1-ucsd-transcript-receipt-mining-packet.md",
    "explorations/research-cycles/hourly-20260625-0203-cycle3-ucsd-visual-slide-capture-batch.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle1-rs-alternate-minus-one-source-bundle-gate.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md",
    "explorations/research-cycles/hourly-20260625-0803-cycle3-proof-restart-readiness-classifier.md",
    "explorations/research-cycles/hourly-20260626-0502-cycle1-negative-primary-dgu-source-receipt.md",
    "explorations/source-domain-selector-prongA-extraction-2026-07-21.md",
    "lab/sources/selected-branch-bv-flrw-source-reinspection-2026-08-05.md",
}

BANNER_TOKENS = (
    "Canonical UCSD-transcript provenance correction (2026-08-26)",
    "edited",
    "derivative",
    "not a primary source",
    "[00:45:00]",
    "audio confirmation",
    "transcript-verified",
)


def load_audit():
    spec = importlib.util.spec_from_file_location("canonical_currency_audit", AUDIT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load canonical-currency audit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expected_record_keys() -> set[tuple[str, str, str]]:
    keys = {
        (path, "CLEARED-CONSISTENT", REPAIR if path in REPAIRED else WAVE)
        for path in EXPECTED
    }
    keys.update((path, "STALE-FOUND", WAVE) for path in REPAIRED)
    return keys


def validate_records(records: list[dict]) -> list[str]:
    failures: list[str] = []
    selected = [row for row in records if row.get("by") in {WAVE, REPAIR}]
    actual = [
        (str(row.get("file")), str(row.get("verdict")), str(row.get("by")))
        for row in selected
    ]
    if set(actual) != expected_record_keys():
        failures.append("cohort record membership differs from the reviewed 31+13 custody set")
    if len(actual) != len(set(actual)):
        failures.append("cohort contains a duplicate file/verdict/author record")
    for row in selected:
        if row.get("correction_id") != CORRECTION:
            failures.append(f"wrong correction for {row.get('file')}")
        if not str(row.get("note", "")).strip():
            failures.append(f"missing semantic-scope note for {row.get('file')}")
        if row.get("verdict") == "STALE-FOUND" and not str(row.get("pointer", "")).strip():
            failures.append(f"missing stale-finding pointer for {row.get('file')}")
        if not (ROOT / str(row.get("file"))).is_file():
            failures.append(f"missing reviewed file {row.get('file')}")
    return failures


def validate_banners(overrides: dict[str, str] | None = None) -> list[str]:
    failures: list[str] = []
    overrides = overrides or {}
    for path in REPAIRED:
        text = overrides.get(path, (ROOT / path).read_text(encoding="utf-8"))
        for token in BANNER_TOKENS:
            if token not in text:
                failures.append(f"repair fence missing {token!r} in {path}")
    return failures


def validate_dynamic() -> list[str]:
    failures: list[str] = []
    audit = load_audit()
    cfg = audit.default_cfg()
    cfg["as_of"] = "2026-08-26"
    result = audit.compute(cfg)
    row = result["per"][CORRECTION]
    if row["dirty"] != 0 or row["unchecked"] or row["known_stale"]:
        failures.append("CC-10 remains dirty")
    if not EXPECTED.issubset(set(row["cleared"]) | set(row["repaired"])):
        failures.append("CC-10 did not clear every reviewed candidate")
    if len(row["repaired"]) != len(REPAIRED):
        failures.append(
            f"CC-10 repaired count is {len(row['repaired'])}, expected {len(REPAIRED)}"
        )
    return failures


def selftest(records: list[dict]) -> list[str]:
    escaped: list[str] = []
    selected_indexes = [
        index for index, row in enumerate(records) if row.get("by") in {WAVE, REPAIR}
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
    trial[selected_indexes[0]]["verdict"] = "FENCED-COMPARATOR"
    if not validate_records(trial):
        escaped.append("wrong-verdict mutation escaped")
    trial = copy.deepcopy(records)
    trial[selected_indexes[-1]]["correction_id"] = "CC-06-CHIRALITY-VEV-CONDITIONAL"
    if not validate_records(trial):
        escaped.append("wrong-correction mutation escaped")
    for path in REPAIRED:
        text = (ROOT / path).read_text(encoding="utf-8")
        trial_text = text.replace(BANNER_TOKENS[0], "missing correction heading", 1)
        if not validate_banners({path: trial_text}):
            escaped.append(f"missing-banner mutation escaped for {path}")
    return escaped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    sidecar = yaml.safe_load(SIDECAR.read_text(encoding="utf-8"))
    records = sidecar.get("checks", [])
    failures = validate_records(records)
    failures.extend(validate_banners())
    failures.extend(validate_dynamic())
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] complete CC-10 cohort clears with exact derivative-provenance custody")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 73/73 record and repair-fence mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
