#!/usr/bin/env python3
"""Coupled certificate for the complete aged CC-06 chirality/VEV cohort."""
from __future__ import annotations

import argparse
import copy
import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SIDECAR = ROOT / "lab/process/canonical-currency-checks.yaml"
AUDIT = ROOT / "process_gates/canonical_currency_audit.py"
CORRECTION = "CC-06-CHIRALITY-VEV-CONDITIONAL"
WAVE = "CC06-WAVE-2026-08-26"
REPAIR = "CC06-REPAIR-2026-08-26"

EXPECTED = {
    "explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md",
    "explorations/W223-falsification-scorecard-synthesis-2026-07-14.md",
    "explorations/W224-falsify-nielsen-ninomiya-chirality-2026-07-14.md",
    "explorations/c3c-covariant-constancy-structure-2026-08-13.md",
    "explorations/conditional-build/selected-k77-w-mirror-real-action-wholesale-gate-2026-08-14.md",
    "explorations/conditional-build/trace-omega-higgs-chirality-compose-reconciliation-2026-08-05.md",
    "explorations/cycle-gates-and-audits/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-disposition-2026-08-04.md",
    "explorations/cycle-gates-and-audits/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-disposition-2026-08-04.md",
    "explorations/eric-native-physics-equation-replacement-atlas-2026-07-31.md",
    "explorations/k77-post-b2-science-council-next-eight-wave-rendezvous-2026-08-04.md",
    "explorations/old-vs-eric-ten-specialist-gap-opportunity-council-2026-07-31.md",
    "explorations/over-determined-rows-review-considerations-2026-08-07.md",
    "explorations/perspective-and-dialectic/all-perspective-tri-theory-combination-steelman-hegelian-2026-07-06.md",
    "explorations/recovery-nogo-sm-selector-swing2-construction-2026-07-16.md",
    "explorations/resolver-wave-k-conditional-active-shiab-b1-variation-2026-08-04.md",
    "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md",
    "explorations/signature-chirality-conjugation-check-2026-08-13.md",
    "explorations/type-ii1-spectral/type-ii1-sm-checklist-tightening-2026-06-23.md",
    "lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md",
    "lab/active-research/joe-directed/ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md",
    "lab/active-research/joe-directed/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md",
    "lab/process/improvement-register-2026-08-03.md",
    "lab/process/science-council-program-efficiency-2026-08-04.md",
    "lab/sources/claim-mining-toe-weinstein-2026-07-20.md",
    "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md",
    "lab/sources/selected-k77-w-mirror-real-action-wholesale-gate-source-return-2026-08-14.md",
}

REPAIRED = {
    "explorations/W222-falsify-sm-emergence-anomaly-hypercharge-2026-07-14.md",
    "explorations/W223-falsification-scorecard-synthesis-2026-07-14.md",
    "explorations/W224-falsify-nielsen-ninomiya-chirality-2026-07-14.md",
}

BANNER_TOKENS = (
    "Canonical chirality/VEV correction (2026-08-26)",
    "SC-CHI-01",
    "VEV-conditional",
    "SG4 bit 2",
    "only",
    "superseded",
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
        failures.append("cohort record membership differs from the reviewed 23+3 custody set")
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
        failures.append("CC-06 remains dirty")
    if not EXPECTED.issubset(set(row["cleared"]) | set(row["repaired"])):
        failures.append("CC-06 did not clear every reviewed candidate")
    if len(row["repaired"]) != 5:
        failures.append(f"CC-06 repaired count is {len(row['repaired'])}, expected 5")
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
    trial[selected_indexes[-1]]["correction_id"] = "CC-10-UCSD-EDITED-DERIVATIVE"
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
    print("[PASS] complete CC-06 cohort clears with exact source-native scope and repair custody")
    if args.selftest:
        escaped = selftest(records)
        if escaped:
            for failure in escaped:
                print(f"[FAIL] {failure}")
            return 1
        print("[PASS] selftest catches 35/35 record and repair-fence mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
